---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

Getting started with Python
==============================================

In this section we will be going over some of the basics of `Python`. There are several excellent resources to get a better understanding of the language and I will reference them in this text. The best way to learn a new language is to try and code up something that you care about. Think about a specific project and try to implement it using the new language. Along the way you will encounter many stumbling blocks, but it is through the process of repeatedly failing that we figure out how things work at a fundamental level.

While there will be a fair bit of coding in this course, the goal of this portion of the module is not to focus on package development. Hopefully some of you will go on to develop packages of your own, but we will not try and turn you into software engineers just yet. The aim is to get you comfortable with basic expression in the language. At this stage in your career, it is best to use carefully crafted existing packages when the need arises. You are more than welcome to look at the source code of the packages that you are using to see how professional software engineers go about developing packages. 

## Installing Python and git

In order to get started with `Python` I would advise you to install [Anaconda](https://www.anaconda.com/products/individual) (or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)) and I also recommend installing [git](https://git-scm.com/downloads). I believe that Nico will have covered some of the details on using version control. For this course it is important that you use `git`, you can use the a command line interface, or a graphical user interface. If you are starting out and are not that comfortable with computers, then a GUI is recommended. When I use a GUI, I prefer to use [Gitkraken](https://www.gitkraken.com/), but [Github Desktop](https://desktop.github.com/) is an acceptable alternative. Installation for most of these should be quite easy to do, but if you are struggling please email me so that I can try and help. I will also send a link via email that provides some installation instructions. 

## Can I still use RStudio for Python?

I believe that one of the reasons why `R` is so popular is the `RStudio` desktop environment. For many economics students that have experience with `Stata` or `Matlab`, it is quite comforting to move to `R` and find that there is a fully fleshed out development environment where you can execute scripts within minutes. In fact, one of the most commonly asked questions that I get for people starting out with `Python` is, *how do I run my scripts?*. For the complete beginner I would recommend trying to execute their commands in `Jupyterlab`. One can establish a nice workflow in this environment and there are several excellent extensions that make the experience quite enjoyable. There are options for `Python` that work similar to `RStudio`, such as `Spyder` and `PyCharm`, but I prefer to use `Visual Studio Code`. 

The big downside with `VS Code` is that it takes a bit more effort to set up and it is not immediately clear how to execute code. In addition, there are new concepts like terminals, workspaces and extensions that can leave the first time user confused. However, once the initial trepidation is dealt with, the end result is worth it. If you are new to `VS Code`, all you need to do is download and install the program on your system, [here](https://code.visualstudio.com/) is a link to the website. After you have installed the program, go to **Extensions** under the **View** tab and search for `Python`. Install the `Python` extension and you will be able to run `Python` code inside of `VS Code`. Remember that if you want `VS Code` to recognise the script as `Pyton` code you need to add the `.py` suffix to the name of your script. We will go through this in detail in the lecture. You can basically set up `VS Code` to have a look and feel quite similar to that of `RStudio`.

## Introductory Python resources

In the context of economics, there is no better resource than the `QuantEcon` page to get started, which can be found [here](https://python.quantecon.org/). In addition to QuantEcon, I will also be referencing [`Think Python`](http://greenteapress.com/thinkpython2/html/index.html), [`Composing Programs`](https://composingprograms.com/) and the [`Python Data Science Handbook`](https://github.com/jakevdp/PythonDataScienceHandbook). These resources cover the topics in much more detail than I will attempt to do here, so if you want to find out more I suggest you read through those.

# Python Fundamentals

We will start with some of the basics which you have already covered with Nico Katzke in the first part of the course. This section is self-study and just gives an idea of the fundamental concepts like variables, data-types, functions, control flow and so forth. If you want to continue working exclusively with `R` that is completely acceptable. I will often also include the `R` and `Julia` code so that you can compare across languages. 

## Basics 

Please take note that this is not a course in computer science, so I will be quite selective about the components that I include in this section. In other words, I consider these components the bare minimum that you need to get started with data science in `Python`. As you can imagine the most basic operations in any programming language are going to be arithmetic operations. 

### Arithmetic

Python will provide you with operators, think about these as special symbols that represent some form of computation. There are some operators that you are already comfortable with, even since primary school. Think about the basic operations of addition, subtraction and multiplication. Python provides operators such as `+`, `-` and `*` to express these computations. We note that the division operator is represented by `/`, while we express exponentiation with the `**` operator. **NB**, the usage of the exponentiation operator is different from many other programming languages, so remember to use this instead of the more traditional `^` that is used in languages such as `Julia` and `R`. In `Python` the `^` is a bitwise operator. You are not expected to know what a bitwise operator is and it won't really feature in our work. 

````{tab} Python
```python3
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

```{code-cell} python3
8 + 7 - 9 * 19 ** 2 / 5
```

### Values and types

Values are the basic building blocks that the program works with. We have used numerical values thus far in our arithmetic operations, but values can belong to different **types**. 


## Collections 

## Control Flow

## Functions