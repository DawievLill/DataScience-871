#!/usr/bin/env python
# coding: utf-8

# # Getting started with Python
# 
# In this section we will be going over some of the basics of Python. There are several excellent resources to get a better understanding of the language and I will reference them when needed. The best way to learn a new language is to try and code up something that you care about. Think about a specific project and try to implement it using the new language. Along the way you will encounter many stumbling blocks, but it is through the process of repeatedly failing that we figure out how things work at a fundamental level.
# 
# While there will be a fair bit of coding in this course, the goal of this portion of the module is not to focus on package development. Hopefully some of you will go on to develop packages of your own, but we will not try and turn you into software engineers just yet. The aim is to get you comfortable with basic expression in the language. At this stage in your career, it is best to use carefully crafted existing packages when the need arises. You are more than welcome to look at the source code of the packages that you are using to see how professional software engineers go about developing packages. 
# 
# ## Installing Python
# 
# In order to get started with Python I would advise you to install [Anaconda](https://www.anaconda.com/products/individual) (or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)). If you want detailed instructions, go to the [Software Carpentry](https://swcarpentry.github.io/python-novice-gapminder/setup.html) website and watch the video that corresponds to your operating system. If you are struggling with the installation, please let me know. 
# 
# ## How do I run Python programs?
# 
# I believe that one of the reasons why R is so popular is the `RStudio` desktop environment. For many economics students that have experience with `Stata` or `Matlab`, it is quite comforting to move to R and find that there is a fully fleshed out development environment where you can execute scripts within minutes. In fact, one of the most commonly asked questions that I get for people starting out with Python is, *how do I run my scripts?*. For the complete beginner I would recommend trying to execute their commands in [`Jupyterlab`](https://jupyter.org/install.html). If you want more information on how to run Python in a JupyterLab setting, you can look at the following [tutorial](https://swcarpentry.github.io/python-novice-gapminder/01-run-quit/index.html). One can establish a nice workflow in this environment and there are several excellent extensions that make the experience quite enjoyable. There are options for Python that work similar to RStudio, such as `Spyder` and `PyCharm`, but I prefer to use `Visual Studio Code`. 
# 
# The big downside with `VS Code` is that it takes a bit more effort to set up and it is not immediately clear how to execute code. In addition, there are new concepts like terminals, workspaces and extensions that can leave the first time user confused. However, once the initial trepidation is dealt with, the end result is worth it. If you are new to VS Code, all you need to do is download and install the program on your system, [here](https://code.visualstudio.com/) is a link to the website. After you have installed the program, go to **Extensions** under the **View** tab and search for *python*. Install the Python extension. [Here](https://www.youtube.com/watch?v=CH3IOVGLCAQ&list=PLVR_rJLcetzkqoeuhpIXmG9uQCtSoGBz1&index=1) is a video that outlines the installation process. 
# 
# ## Basics 
# 
# We will start with some of the basics which you have already covered with Nico Katzke in the first part of the course. This section is self-study and just gives an idea of the fundamental concepts like variables, data-types, functions, control flow and so forth. The primary source for most of the material is [`Think Python`](http://greenteapress.com/thinkpython2/html/index.html). If you want to continue working exclusively with R that is completely acceptable. I will often include the R and Julia code so that you can compare across languages. 
# 
# In the context of economics, there is no better resource than the [`QuantEcon`](https://python.quantecon.org/) page to get started. Kevin Sheppard at Oxford also provides a [complete set of notes](https://www.kevinsheppard.com/files/teaching/python/notes/python_introduction_2020.pdf) that are appropriate for economics. In addition to QuantEcon and Kevin Sheppard's notes, I will also be referencing [`Think Python`](http://greenteapress.com/thinkpython2/html/index.html), [`Composing Programs`](https://composingprograms.com/) and the [`Python Data Science Handbook`](https://github.com/jakevdp/PythonDataScienceHandbook). These resources cover the topics in much more detail than I will attempt to do here, so if you want to find out more I suggest you read through those.
# 
# Please take note that this is not a course in computer science, so I will be quite selective about the components that I include in this section. In other words, I consider these components the bare minimum that you need to get started with data science in Python. If you want to engage with the material in a more active manner, I recommend going through this [Python tutorial](https://www.learnpython.org/) or doing some basic introductory exercises at [DataCamp](https://www.datacamp.com/). Now let us get started with some of the essentials. As you can imagine the most basic operations in any programming language are going to be arithmetic operations. 
# 
# ### Arithmetic
# 
# The Python interpreter makes use of several operators, think about these as special symbols that represent some form of computational process. You are already comfortable with arithmetic operators. Think about the basic operations of addition, subtraction and multiplication. Python comes with operators such as `+`, `-`, `*` and `/` to express these computations. Note that we express exponentiation with the `**` operator. The usage of the exponentiation operator is different from many other programming languages, so remember to use this instead of the more traditional `^` that is used in languages such as R. In Python the `^` is a bitwise operator. You are not expected to know what a bitwise operator is and it won't really feature in our work. 
# 
# ````{tab} Python
# ```python
# 39 + 3
# 55 - 13
# 6 * 7
# 84 / 2
# 4**3
# ```
# ````
# ````{tab} R
# ```R
# 39 + 3
# 55 - 13
# 6 * 7
# 84 / 2
# 4^3
# ```
# ````
# 
# In Python one could execute the following combination of operations to arrive at a numerical answer, similar to what you would do with a calculator.

# In[1]:


8 + 7 - 9 * 19 ** 2 / 5


# These arithmetic operators are not the only ones we will encounter, we will also see logical, relational, bitwise, identity, membership and assignment operators. We will discuss some of these operators once appropriate. 
# 
# ### Values and types
# 
# Values are the basic building blocks that the program works with. We have used numbers thus far in our arithmetic operations, but values can belong to different **types**. In the realm of numbers, one can classify the number `2` as an integer and `42.0` as a floating point number. These are values that belong to different types. In Python it is easy to determine what the type of a specific value is. One can find out by issuing the following command.

# In[2]:


type(2)


# In[3]:


type(42.0)


# Different programming languages differ slightly in terms of syntax to find out the type of the value. 
# 
# ````{tab} Python
# ```python
# type(42.0)
# ```
# ````
# ````{tab} R
# ```R
# typeof(42.0)
# ```
# ````
# 
# We won't be working exclusively with different types of numbers as that would be quite limiting. Another important type that we take note of is the **string** type. This generally refers to any form of text. We refer to a statement such as *'I love Data Science!'* as a combination of letters that are strung together, which is why we call it a string.

# In[4]:


type('I love Data Science!')


# There are several data types that we will work with in Python. Some of the important types include booleans, lists, tuples, dictionaries and sets. We will introduce the different types as we progress through the coding exercises. Kevin Sheppard has a nice [video](https://www.youtube.com/watch?v=XYH318V76ng&list=PLVR_rJLcetzkqoeuhpIXmG9uQCtSoGBz1&index=5) that gives an oversight of the basic Python types.  
# 
# **Remark**: You will often see that Python is referred to as a dynamically typed language, while other languages like `C++` or `Java` are statically typed. [Here](https://realpython.com/lessons/dynamic-vs-static/) is a nice description of the differences between the two and why it matters.  
# 
# ### Variables
# 
# Working with data wouldn't be interesting if were only able to work with values. One of the best features of any programming language is the ability to manipulate *variables*. We define a variable to be a name that refers to a specific value. Variables allow us to store specific values. In order to better understand this we want to introduce the idea of variable assignment. Variable assignment is the association of a value to a variable with the `=` operator (equals sign). We could assign the value of `42` to a specific variable `x` to get the following assignment statement.

# In[5]:


x = 42


# Python will place this object in memory and will conveniently keep it there as long as we are busy with our session. It is important to note that the way the computer reads this assignment statement is from right to left. The right side is evaluated first and that computed value gets assigned to the variable name on the left hand side. 
# 
# ````{margin}
# ```{tip}
# When naming variables
#  - choose meaningful names
#  - you can include letters, digits and underscores
#  - don't start with digits
#  - naming is case sensitive
# ```
# ````
# 
# Generally, we would like to choose variable names that are meaningful. In other words, they give us some notion of what the variable is used for. These variable names can be as long as you like and contain letters and numbers, but don't start a variable with a number. Lower case is usually used for variable names (this is merely a programming convention, not a rule). You can also use the underscore when you have a variable name with multiple words.

# In[6]:


answer_to_ultimate_question = 42


# There are some **keywords** in Python that you cannot use, they are reserved. For example, you cannot use the word `if` or `for` as variable names, since these things mean something specific in the programming language. You don't need to remember these keywords. If you are using a development environment with syntax highlighting you will see that typing in a keyword will change the color of that word. 
# 
# 
# ## Collections 
# 
# These include lists, tuples, sets, dictionaries. List and tuples are sequence containers, while set and dict are mapping containers.
# 
# ### Ordered collections
# 
# ### Associative collections
# 
# 
# ## Control flow
# 
# Introduce `if` and ternary operator. Discuss, `while`, `break, continue` and `pass`.
# 
# ### Conditional statements and blocks
# 
# ### Iteration
# 
# ## Functions
# 
# In the most general terms, a function can be defined as a process that takes an input (or inputs) and maps it to an output. From your mathematical training you are used function called `f` that takes an argument `x` to produce some output `f(x)`. In Python these functions operate in a similar manner, where the function takes and argument and **returns** a result. One could have a `print` function that prints the input that it is provided. In the example below the value of the variable is evaluated by the interpreter and then the print statement is executed to deliver a **return value**.

# In[7]:


x = 42
print(x)


# ````{margin}
# ```{note}
# We will talk about classes, packages and modules again at a later stage. 
# ```
# ````
# An attractive feature of Python is the ability to import functions from modules and packages. Modules are files that contain collections of functions that we might want to use. Packages are folders that could contain multiple files and is usually a collection of modules. It is possible to write all the functions we want to use on our own, but often someone else has written functions that are easy to use and computationally efficient. My advice would be to work with modules and packages that other people have written till you feel comfortable enough programming your own functions. If you want to import a module you simply use the import command. In R the process is quite similar, you would simply use the package managers in those languages to install the required packages / modules. For the code example below, let us assume that there is a module called `Example` across the different programming languages, so that you can just see the process involved. The code below won't work, it is merely for illustrative purposes.  
# 
# ````{tab} Python
# ```python
# import Example
# ```
# ````
# ````{tab} R
# ```R
# install.packages("Example")
# library(Example)
# ```
# ````
# 
# In Python if you were to import the `math` module you would be able to use all the functions and variables contained in that module object. You are bringing the functionality associated with that module into your session. One can now access any function or object from the package by the name of package together with the name of the function, separated by a dot. This **dot notation** has some benefits, but I much prefer the way in which R incorporates functions from modules. The main reason for this notation is to avoid potential naming conflicts, which we will discuss at the end of this section. Below is an example of the dot notation in action. 
# 
# ````{tab} Python
# ```python
# import math
# 
# degrees = 45
# radians = degrees / 180.0 * math.pi
# math.sin(radians)
# ```
# ````
# ````{tab} R
# ```R
# degrees = 45
# radians = degrees / 180.0 * pi
# sin(radians)
# ```
# ````
# 
# In this example we see that the value for $\pi$ and $\sin$ is called from the `math` module using the dot notation, `math.pi` and `math.sin`. In the case of R we don't have to worry about the dot notation for now, since $\pi$ and $\sin$ are built-in components of the language. However, there are instances with naming conflicts from different packages and those languages have their own way to deal with this. 
# 
# ### Defining your own functions
# 
# So far we have discussed functions that are included in Python, but we could also add functions of our own. When specifying our own function we need to give it a name and a sequence of statements to run whenever the function is called. The basic syntax to create a function is as follows:
# 
# ````{tab} Python
# ```python
# def function_name(inputs):
#     # step 1
#     # step 2
#     # ...
#     return outputs
# ```
# ````
# ````{tab} R
# ```R
# function_name <- function(inputs) {
#     # step 1
#     # step 2
#     # ...
#     return(outputs)
# }
# ```
# ````
# 
# The basic anatomy of the user defined function is the same across programming languages. In the case of Python `def` is used to tell Python that we are defining a new function. While in R we use the keyword `function` to indicate that a new function is being created. Within the body of the function we specify a `return` keyword to indicate the value that we would like the language to return. In some languages, like Julia, the `return` keyword is not strictly required, but it often makes the code more easily readable. 
# 
# Note that the statements inside the defined function do not run until the function is called. We call functions in the following manner
# 
# It is important to include a docstring with your functions. This means including . Discussion on commenting in general as precursor to this discussion. In addition, discuss the idea of class methods.
