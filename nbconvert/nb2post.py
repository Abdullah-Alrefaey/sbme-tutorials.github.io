"""Converts Jupyter Notebooks to Jekyll compliant blog posts"""
from datetime import datetime
import re, os, logging
from pathlib import Path
from nbdev import export2html
from nbdev.export2html import Config, Path, _re_digits, _to_html, _re_block_notes
from fast_template import rename_for_jekyll
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--free_structure", action="store_true", 
                    default=False,
                    help="Allow free notebooks which are not necessarily located in _notebooks dir to be converted.")
parser.add_argument("--force_date", action="store_true", 
                    default=False,
                    help="Force the date prefix for the Markdown converted files from the notebooks.")
args = parser.parse_args()

warnings = set()
    
# Modify the naming process such that destination files get named properly for Jekyll _posts
def _nb2htmlfname(nb_path, dest=None): 
    fname = rename_for_jekyll(nb_path, warnings=warnings, force_date=args.force_date)
    if dest is None: dest = Config().doc_path
    return Path(dest)/fname

# Add embedded links for youtube and twitter
def add_embedded_links(cell):
    "Convert block quotes to embedded links in `cell`"
    _styles = ['youtube', 'twitter']
    def _inner(m):
        title,text = m.groups()
        if title.lower() not in _styles: return f"> {m.groups()[0]}: {m.groups()[1]}"
        return '{% include '+title.lower()+".html content=\'`"+_to_html(text)+"`\' %}"
    if cell['cell_type'] == 'markdown':
        cell['source'] = _re_block_notes.sub(_inner, cell['source'])
    return cell

# TODO: Open a GitHub Issue in addition to printing warnings
for original, new in warnings:
    print(f'{original} has been renamed to {new} to be complaint with Jekyll naming conventions.\n')
    
## apply monkey patches
export2html._nb2htmlfname = _nb2htmlfname
export2html.process_cell.append(add_embedded_links)

if args.free_structure:
    notebooks = list(Path("../2020/cv").rglob("*.ipynb"))
    for notebook_path in notebooks:
        export2html.notebook2html(fname=notebook_path, dest=os.path.dirname(notebook_path), template_file='fastpages.tpl')
else:
    export2html.notebook2html(fname='_notebooks/*.ipynb', dest='_posts/', template_file='fastpages.tpl')
