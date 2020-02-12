---
layout: page
course: "sbe404b"
category: "assignment"
year: "2019"
title:  "Assignment 2: Spatial domain filters, Images in frequency domain, and Hough Transforms"
by: "Ayman"
pdf: true
---


## Objectives

* 2D Convolution.
* Image Histograms.
* 2D Fourier Transform.
* Image Gradients.
* Spatial domain filters.
* Frequency domain filters.
* Hough Transforms (Hough Lines and Circles)

## Prerequisites (Before you start)

* Read [Section 2 Notes]({% link 2018/cv/notes/2_week2.md %}){:target="_blank"}.
* Read [Section 3 slide]({{ site.baseurl }}{% link 2019/cv/presentations/3_week3/index.md %}){:target="_blank"}
* Read [Section 4 Notes]({% link 2018/cv/notes/4_week4.md %}){:target="_blank"}.


## Deadline

**Tuesday 9/4/2019 11:59 PM.**

Discussion **TBA**.

## Joining to Assignment Repository

This is a Group assignment 3 members maximum.

1. Go to the [Assignment Page](https://classroom.github.com/g/VKu8qGpP).
2. Accept the assignment.
3. Wait till your repository created.
4. Open the link and Clone repository.

## Requirements

Regarding the Assignment page you will find a .ui file for the CV toolbox you are going to build. you should implement all the required function the .ui file using PyQt. **you should build all the algorithms as its forbidden to use OpenCv package**.

you toolbox should implement the following:

* spatial domain filtering with all filters below:
    * Edge detection filters: Prewitt, Sobel, Laplacian, Laplacian of Gaussian (LoG), Difference of Gaussian (DoG).
    * Noise reduction filters: box, Gaussian, Median (non-linear).
    * Sharpening filter.
* frequency domain transform.
* frequency domain filters.
* Hough transform (lines and circles).

## Part 2: Written

Report all details about your implementations in markdown file `README.md`. Report must show sample results of your code. Compare between spatial and frequency domain filters, organize the report and be concise. State issues you faced in the assignment and how you treated with it. Mention any kind of contribution of other students.


## Important Notes 

* Each team should implements all algorithm without using any image processing packages. 
* You are allowed to discuss task problems with your mates. But code must be on your own.
* You can get code lines from internet and include them in your own code and you must cite the source.
* Report must include summary about your implementation, sample results and issues that you faced and how you fixed it.
* You must mention any kind of contribution of other mates.

## Version tagging

You will work on this repository until the end of semester. Each subsequent task you will develop incrementally on this repository. It is recommended that for each task you **tag** the corresponding commit, so we can return back to any tagged commit version after making lots of updates.

### After finishing the requirements of the current assignment

```terminal
git commit -a -m "solved all requirements!"
```

### Tagging the last commit

```terminal
git tag v1-assignment2
```

### Transfer tagging to GitHub

```terminal
git push origin master --tags
```

### Transfer commits to GitHub

```terminal
git push origin master
```