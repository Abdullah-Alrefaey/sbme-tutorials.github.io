---
layout: presentation
style: laminal
highlighter: monokai
course: "sbe201"
category: "presentation"
year: "2019"
title: "Week 4: Struct, Stacks, Linked Lists, and Queues"
by: "Asem"
author: "Asem Alaa"
---

<textarea id="source">

---
class: left, top
## Stack as Data Structure != Stack Memory


---
## C++ Struct

#### Types in C++

--
* Premitive Data Types (PDT), or first-class-citizens
--
* Custom, user-defined types.


--
```c++
namespace rectangle
{
double area( double w , double h )
{
    return w * h;
}
}
```

--
```c++
struct Rectangle
{
    double w;
    double h;
};
```

--
* `Rectangle` is now a custom type, 
--
* consists of two `double`s. 
--
* Think of it as a package.


---
```c++
struct Rectangle
{
    double w; // First member
    double h; // Second member
}; // Don't forget a semicolon here!

double area( Rectangle rectangle )
{
    return rectangle.w * rectangle.h;
}

double area2( Rectanle *pRect )
{
    return pRect->w * pRect->h;
}
```

---
```c++
int main()
{
    rectangle::Rectangle rect{ 3 , 5 }; // declaration+initialization of Rectangle type!

    std::cout << rectangle::area( rect ) << std::endl;
    std::cout << rectangle::area2( &rect ) << std::endl;
    return 0;
}
```

---
class: left, top
We may also package an array with its size, using `struct`

--
```c++
struct IntegerArray
{
    int *base;
    int size;
};

int sumArray( IntegerArray array )
{
    int sum = 0;
    for( int i = 0; i < array.size ; ++i )
    {
        sum += array.base[ i ];
    }
    return sum;
}
```

---
```c++
int main()
{
    int *buffer = new int[10];
    IntegerArray array{ &buffer[0] , 10 }; // Initializes base and size members.

    std::cout << sumArray( array ) << std::endl;

    // We still need to delete the array on the heap
    delete [] array.base;

    return 0;
}
```

---
class: left, top
### Struct for returning multiple values

--
```c++
struct ECGArray // We could name it also DoubleArray
{
    double *samples;
    int size;
};

struct Statistics
{
    double mean = 0 ;
    double variance = 0 ;
    double min = 0;
    double max = 0;
};

// Very self-explaining function header!
Statistics analyzeECG( ECGArray ecg )
{
    Statistics analysis; // Declaration, and no need for explicit initialization now

    analysis.mean = // Some logic here
    analysis.variance = // Some logic there
    // And so on.

    return analysis;
}
```

---
## Functions overloading

--
C++ allows *functions with same name*, **but different parameters**.

--
For example, this is **not allowed** in C++:

```c++
double area( double w , double h )
{
    return w * h;
}

double area( double base , double height ) // Compiler Error, redefinition of area(double,double)
{
    return base * height / 2;
}
```

**AMBIGUOUS** when calling `area(1.4,5)`

---

.green[This works]

--
```c++
struct Rectangle
{
    double w;
    double h;
};

double area( double d )
{
    return d * d; // square area
}

double area( double w, double h)
{
    return w * h;
}

double area( Rectangle rect )
{
    return rect.w * rect.h;
}
```

---
## Stacks (ADT)

--
**Stack** is more of *behaviour* than being a **structure** itself. 

--
#### Possible Implementations:

--
* arrays.
--
* linked lists.


--
#### For any implementation, the following functions should exist:

--
* **push**.
--
* **pop**.
--
* **front**.


---
## Stack is LIFO

<img src="/gallery/Lifo_stack.png" style="width:400">


---
### Implementing a Stack using Array


#### 1. Buffer (array)

--
* Size of array = capacity of the **Stack**.
--
* **Stack** is initially empty.

--
```c++
// Let's make a new type for our stack with a name indicating its properties:
// 1. Our element types are integers.
// 2. The ADT is Stack
// 3. Maximum size is 100
struct IntegerStack100
{
    int buffer[ 100 ];
    int capacity = 100;
};
```

---
#### Finally, the top element

--
```c++
struct IntegerStack100
{
    int buffer[ 100 ];
    int capacity = 100;
    int top = -1;
    // Default value of top is -1 when declaring the stack.
    // -1 means our stack is empty
};
```

--
Now we are ready!


---
#### Stack: Push

--
1. **increment** *top*.
--
2. **add** new element.


--
```c++
IntegerStack100 push( IntegerStack100 stack , int newElement )
{
    ++stack.top;
    stack.buffer[ stack.top ] = newElement;
    return stack;
}
```

--
* .red[This version passes by value then returns the new stack.]

---
#### Stack: Push
##### Alternatively.. 

```c++
void push( IntegerStack100 &stack , int newElement )
{
    ++stack.top;
    stack.buffer[ stack.top ] = newElement;
}
```

--
* .red[This version passes by reference then modifies in-place, so no need to return the modified stack.]

---
#### Stack: Front

--
1. return the **first element**, which is pointed to by **top**.

---
```c++
int front( IntegerStack100 &stack )
{
    return stack.buffer[ stack.top ];
}
```
---
#### Stack: Pop

1. decrement **top**.

--
```c++
IntegerStack100 pop( IntegerStack100 stack )
{
    --stack.top;
    return stack;
}
```

--
* .red[This version passes by value then returns the new stack.]


---
#### Stack: Pop
##### Alternatively.. 

1. decrement **top**.

--
```c++
void pop( IntegerStack100 &stack )
{
    --stack.top;
}
```

--
* .red[This version passes by reference then modifies in-place, so no need to return the modified stack.]

---
#### Stack: Size
##### Retrieving the size of stack

--
```c++
int size( IntegerStack100 &stack )
{
    return ( stack.top + 1 ); // simple
}
```

---
#### Stack: Empty?
##### Asking our stack if it is empty

--
```c++
bool isEmptyStack( IntegerStack100 &stack )
{
    if( stack.top == -1 )
    {
        return true;
    }
    else
    {
        return false;
    }
}
```

---
#### Stack: Empty?
##### Asking our stack if it is empty

--
###### Alternatively..

```c++
bool isEmptyStack( IntegerStack100 &stack )
{
    return ( stack.top == -1 );
}
```

---
class: center, middle

## .red[**Tutorial 4 ENDS HERE**]


---
class: left, top
## Linked Lists

#### Arrays vs. LL

--
* **Arrays** => **contiguous elements** in the memory. 
--
* **LL** => **sparse** in memory, 


--
Each element in **LL** can see the *next* element.

--
#### Why linked lists

--
* .green[Very flexible in insertion/removal.]
--
* **Arrays** => .red[fixed sizes]
--
* **Arrays** => .red[expensive insertion]


---
### The Memory Mode: Array vs. Linked List

<img src="/gallery/dna_array.svg" style="width:80%">

<img src="/gallery/dna_ll.svg" style="width:80%">


---
### Pointers revisited

--
* Each element => *node*. 
--
* To connect between nodes => **pointers**. 
--
* *node* has a **pointer** pointing to the *next node*.


---
#### **DNA** sequence as a Linked List (LL)

--
```c++
struct node
{
    char data;
    node* next;
};
```

--
<img src="/gallery/dna_ll_annotated.svg" style="width:100%">


---
#### The last node (back)

--
```c++
void printLL( node* front )
{
    node *current = front;

    while( current != nullptr )
    {
        std::cout << current->data;
        current = current->next;
    }
}
```

---
### The LL Structure

We need to make a `struct` that will **encapsulate** our **LL**.

--
### Head (front)

--
```c++
struct CharLinkedList
{
    node *head;
};
```

---
#### *Insert* element to the front:

--
```c++
void insertToFront( CharLinkedList &list , char newElement )
{
    node *newFront = new node{ newElement , list.head };
    list.head = newFront;
}
```

--
##### Alternatively...
```c++
void insertToFront( CharLinkedList &list , char newElement )
{
    list.head = new node{ newElement , list.head };
}
```

--
### Tail (back)

--
So our **LL** `struct` is now consisting of:

```c++
struct CharLinkedList
{
    node *head;
    node *tail;
};
```

---
#### *Insert* element to the back:

--
```c++
void insertToList( CharLinkedList &list , char newElement )
{
    list.tail->next = new node{ newElement , nullptr };
    list.tail = list.tail->next;
}
```

---
## Queues (ADT)

--
* **Queues** are another Abstract Data Type (ADT), 
--
* implemented using: arrays or linked lists. 
--
* **Queue** behaviour: **FIFO** (first in, first out).


#### The ADT **Queue** should satisfy:

--
* **enqueue**,
--
* **dequeue**.

---
<img src="/gallery/Data_Queue.svg" style="width:400">

---
### **Biomedical Application**: Queues of Biological Signals

--
<img src="/gallery/biosignal.gif" style="width:400">


---
### Implementing Queue using concrete array

--
#### 1. The circular buffer

--
* Size of buffer = Capacity of **Queue**.
--
* Buffer is initially empty


--
```c++
// Let's make a new type for our Queue with a name indicating its properties:
// 1. Our element types are integers.
// 2. The ADT is Queue
// 3. Maximum size is 100
struct DoubleQueue100
{
    double buffer[ 100 ];
    int capacity = 100;
};
```

---
class:left, top
#### Finally, let's make two variables indicating the front and the back of our Queue

```c++
struct DoubleQueue{
    double buffer[ 100 ];
    int capacity = 100;
    int front = -1;
    int back = -1;
};
```

---
#### Making our buffer to act as a circular buffer

--
<img src="/gallery/circular-buffer-animation.gif" style="width:400">


* the **blue pointer** is the front, where we *dequeue* elements.
* the **red pointer** is the back, where we *enqueue* new elements.

---
class: left, top
# Thank you

</textarea>
