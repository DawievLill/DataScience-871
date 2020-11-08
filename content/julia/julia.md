
Getting started with Julia
==============================================

In this notebook we will be going over some of the basics that you will need. There are several excellent resources to get a better understanding of the language. I will provide a list of sources that you can use to become more comfortable in using the language. The best way to learn a new language is to try and code up something that you care about. Think about a specific project and try to implement it using the new language. Along the way you will encounter many stumbling blocks, but it is through the process of failing that we figure out how things work.

While there will be a fair bit of coding in this course. The goal of this portion of the course is not to focus on package development, but hopefully some of you will go on to develop packages of your own. The aim is to get you comfortable with basic expression in the language. At this stage in your career, it is best to use carefully crafted existing packages when the need arises. You are more than welcome to look at the source code of the packages that you are using to see how professional software engineers go about developing packages.

## Installing Julia

In order to install `Julia` you need to go the `Julia` homepage, which can be found [here](https://julialang.org/), and follow the specific instructions. Installation is quite easy to do. [Here](https://www.youtube.com/watch?v=OOjKEgbt8AI) is a video that provide some details on how to perform the installation on Windows. The process is similar (easier) for Linux and Mac. 

## Can I still use RStudio for Julia?

One of the most commonly asked questions that I get for people starting out with `Julia` or `Python` is, how do I run my scripts? One of the reasons why `R` is so easy to use for many people is the `RStudio` environment. For many economics students that have experience with `Stata` or `Matlab`, it is quite comforting to move to `R` and find that there is a fully fleshed out development environment where you can execute scripts within minutes. While there are similar options for `Python` such as `Spyder` and `PyCharm`, I prefer to use `Visual Studio Code` for `Python` and `Julia`. It takes a bit more effort to set up, but the end result is worth it. If you are new to `VS Code`, all you need to do is download and install the program on your system, [here](https://code.visualstudio.com/) is a link to the website. After you have installed the program, go to **Extensions** under the **View** tab and search for `Julia`. Install the `Julia` extension and you will be able to run `Julia` code inside of `VS Code` by pressing *Shift-Enter*, or you can run single lines by pressing *Alt-Enter*. We will go through this in detail in the lecture. You can basically set up `VS Code` to have a look and feel quite similar to that of `RStudio`. Another option would be to use `Jupyterlab`. However, I don't have enough experience with that interface to tell you whether it is quite as feature rich as `VS Code`.

## Introductory Julia resources

In the context of economics, there is no better resource than the `QuantEcon` page to get started, which can be found [here](https://julia.quantecon.org/). I will often be referencing the material on this page. The official `Julia` documentation is also quite good and worth reading. If you are interested in `Python`, there is a `QuantEcon` page dedicated to programming in `Python` that you might want to visit.

The number of resources, in comparison to other languages, are limited. However, there are some really nice tutorials that you can use to get started with `Julia`. The first place to look is on the `Julia` homepage. If you navigate to the `learn` section of the page, you will see that there are some introductory tutorials from the Julia Academy. These tutorials are well structured and we will borrow some of the material to form the basis of the notes that we present here. There are also some recommended books here. I think that the `Think Julia` book is quite nice for beginners and the `Introduction to Applied Linear Algebra` book will also feature in our development of ideas on linear algebra. Links to these books can be found [here](https://benlauwens.github.io/ThinkJulia.jl/latest/book.html) and [here](http://vmls-book.stanford.edu/).

This should be enough to get you started. I will introduce more advanced material and sources as we progress. I am not going to provide extensive lists of resources on `R` and `Python` in this notebook. I will reference some resources that I think are useful as we work through the material of the course. 

# Julia Fundamentals

We will start with some of the basics which you have already covered with Nico Katzke in the first part of the course. This section is selft-study and just gives an idea of the fundamental concepts like variables, data-types, functions, control flow and so forth. For a more complete description of the concepts I refer you to the `Think Julia` book, which covers the topics in much more detail. You can also consult the `QuantEcon` notes for a similar description of the basics. Once you have worked through this section you should have a good idea of the core concepts in `Julia` and then we can proceed to working with data in the next section. 

## Basics 

## Collections 

## Control Flow

## Functions