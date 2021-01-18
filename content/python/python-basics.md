---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python
---

# Getting started with Python

In this section we will be going over some of the basics of Python. There are several excellent resources to get a better understanding of the language and I will reference them when needed. The best way to learn a new language is to try and code up something that you care about. Think about a specific project and try to implement it using the new language. Along the way you will encounter many stumbling blocks, but it is through the process of repeatedly failing that we figure out how things work at a fundamental level.

While there will be a fair bit of coding in this course, the goal of this portion of the module is not to focus on package development. Hopefully some of you will go on to develop packages of your own, but we will not try and turn you into software engineers just yet. The aim is to get you comfortable with basic expression in the language. At this stage in your career, it is best to use carefully crafted existing packages when the need arises. You are more than welcome to look at the source code of the packages that you are using to see how professional software engineers go about developing packages. 

## Installing Python

In order to get started with Python I would advise you to install [Anaconda](https://www.anaconda.com/products/individual) (or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)). If you want detailed instructions, go to the [Software Carpentry](https://swcarpentry.github.io/python-novice-gapminder/setup.html) website and watch the video that corresponds to your operating system. If you are struggling with the installation, please let me know. 

## How do I run Python programs?

I believe that one of the reasons why R is so popular is the `RStudio` desktop environment. For many economics students that have experience with `Stata` or `Matlab`, it is quite comforting to move to R and find that there is a fully fleshed out development environment where you can execute scripts within minutes. In fact, one of the most commonly asked questions that I get for people starting out with Python is, *how do I run my scripts?*. For the complete beginner I would recommend trying to execute their commands in [`Jupyterlab`](https://jupyter.org/install.html). If you want more information on how to run Python in a JupyterLab setting, you can look at the following [tutorial](https://swcarpentry.github.io/python-novice-gapminder/01-run-quit/index.html). One can establish a nice workflow in this environment and there are several excellent extensions that make the experience quite enjoyable. There are options for Python that work similar to RStudio, such as `Spyder` and `PyCharm`, but I prefer to use `Visual Studio Code`. 

The big downside with `VS Code` is that it takes a bit more effort to set up and it is not immediately clear how to execute code. In addition, there are new concepts like terminals, workspaces and extensions that can leave the first time user confused. However, once the initial trepidation is dealt with, the end result is worth it. If you are new to VS Code, all you need to do is download and install the program on your system, [here](https://code.visualstudio.com/) is a link to the website. After you have installed the program, go to **Extensions** under the **View** tab and search for *python*. Install the Python extension. [Here](https://www.youtube.com/watch?v=CH3IOVGLCAQ&list=PLVR_rJLcetzkqoeuhpIXmG9uQCtSoGBz1&index=1) is a video that outlines the installation process. 

# Python Fundamentals

We will start with some of the basics which you have already covered with Nico Katzke in the first part of the course. This section is self-study and just gives an idea of the fundamental concepts like variables, data-types, functions, control flow and so forth. The primary source for most of the material is [`Think Python`](http://greenteapress.com/thinkpython2/html/index.html). If you want to continue working exclusively with R that is completely acceptable. I will often include the R and Julia code so that you can compare across languages. 

In the context of economics, there is no better resource than the [`QuantEcon`](https://python.quantecon.org/) page to get started. Kevin Sheppard at Oxford also provides a [complete set of notes](https://www.kevinsheppard.com/files/teaching/python/notes/python_introduction_2020.pdf) that are appropriate for economics. In addition to QuantEcon and Kevin Sheppard's notes, I will also be referencing [`Think Python`](http://greenteapress.com/thinkpython2/html/index.html), [`Composing Programs`](https://composingprograms.com/) and the [`Python Data Science Handbook`](https://github.com/jakevdp/PythonDataScienceHandbook). These resources cover the topics in much more detail than I will attempt to do here, so if you want to find out more I suggest you read through those.

## Basics 

Please take note that this is not a course in computer science, so I will be quite selective about the components that I include in this section. In other words, I consider these components the bare minimum that you need to get started with data science in Python. If you want to engage with the material in a more active manner, I recommend going through this [Python tutorial](https://www.learnpython.org/) or doing some basic introductory exercises at [DataCamp](https://www.datacamp.com/). Now let us get started with some of the essentials. As you can imagine the most basic operations in any programming language are going to be arithmetic operations. 

### Arithmetic

Python makes use of several operators, think about these as special symbols that represent some form of computational process. There are some operators that you are already comfortable with. Think about the basic operations of addition, subtraction and multiplication. Python comes with operators such as `+`, `-`, `*` and `/` to express these computations. Note that we express exponentiation with the `**` operator. The usage of the exponentiation operator is different from many other programming languages, so remember to use this instead of the more traditional `^` that is used in languages such as Julia and R. In Python the `^` is a bitwise operator. You are not expected to know what a bitwise operator is and it won't really feature in our work. 

````{tab} Python
```python
39 + 3
55 - 13
6 * 7
84 / 2
4**3
```
````
````{tab} Julia
```julia
39 + 3
55 - 13
6 * 7
84 / 2
4^3
```
````
````{tab} R
```R
39 + 3
55 - 13
6 * 7
84 / 2
4^3
```
````

In Python one could execute the following combination of operations to arrive at a numerical answer, similar to what you would do with a calculator. 

```{code-cell} python
8 + 7 - 9 * 19 ** 2 / 5
```

### Values and types

Values are the basic building blocks that the program works with. We have used numbers thus far in our arithmetic operations, but values can belong to different **types**. In the realm of numbers, one can classify the number `2` as an integer and `42.0` as a floating point number. These are values that belong to different types. In Python it is easy to determine what the type of a specific value is. One can find out by issuing the following command. 

```{code-cell} python
type(2)
```

```{code-cell} python
type(42.0)
```
Different programming languages differ slightly in terms of syntax to find out the type of the value. 

````{tab} Python
```python
type(42.0)
```
````
````{tab} Julia
```julia
typeof(42.0)
```
````
````{tab} R
```R
typeof(42.0)
```
````

We won't be working exclusively with different types of numbers as that would be quite limiting. Another important type that we take note of is the **string** type. This generally refers to any form of text. We refer to a statement such as *'I love Data Science!'* as a combination of letters that are strung together, which is why we call it a string. 

```{code-cell} python
type('I love Data Science!')
```

There are several data types that we will work with in Python. Some of the important types include booleans, lists, tuples, dictionaries and sets. We will learn more about some of these types and how to use them soon. 

**Remark**: You will often see that Python is referred to as a dynamically typed language, while other languages like `C++` or `Java` are statically typed. [Here](https://realpython.com/lessons/dynamic-vs-static/) is a nice description of the differences between the two and why it matters.  

### Variables, expressions and statements

One of the best features of any programming language is the ability to manipulate variables. We define a variable to be a name that refers to a specific value. In order to better understand this we want to introduce the idea of variable assignment. Variable assignment is the association of a value to a variable. We could assign the value of `42` to a specific variable `x` to get the following assignment statement. 

```{code-cell} python
x = 42
```
`Python` will place this object in memory and will conveniently keep it there as long as we are busy with our session. It is important to note that the way the computer reads this assignment statement is from right to left. The right side is evaluated first and that computed value gets assigned to the variable name on the left hand side. 

Generally, we would like to choose variable names that are meaningful. In other words, they give us some notion of what the variable is used for. These variable names can be as long as you like and contain letters and numbers, but don't start a variable with a number. Lower case is usually used for variable names (this is merely a programming convention, not a rule). You can also use the underscore when you have a variable name with multiple words. 

```{code-cell} python
answer_to_ultimate_question = 42
```

Finally, there are some **keywords** in Python that you cannot use, they are reserved. For example, you cannot use the word `if` or `for` as variable names, since these things mean something specific in the programming language. You don't need to remember these keywords. If you are using a development environment with syntax highlighting you will see that typing in a keyword will change the color of that word. 


## Collections 

## Control Flow

## Functions