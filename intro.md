
Data Science for Economics
==============================================

In this part of the course we will focus on machine learning methods. At this stage in the world of data science four of the most frequently used programming languages are `R`, `Python`, `Julia` and `SQL`. This means that when you enter the job market, you will be required to have some knowledge of at least one of these languages. We will be using both `Julia` and `R` as our preferred programming languages, touching briefly on the basics of `SQL`. Don't worry if you have never worked with `Julia`, you can continue working in `R` if you are more comfortable focusing on just one language at a time. Most of your `R` code can also be called into `Julia` with a a package called `RCall.jl`. Originally this course used `Python` in addition to `R`, however I have started using `Julia` more in my daily workflow and believe it has several distinct advantages over `Python`. Fortunately, the syntax of `Julia` is quite similar to that of `Python`, so it should be quite easy for you to transfer your newfound knowledge into a `Python` environment.

Just to make it clear, in this course we **officially** use `R`, which means I will provide you with `R` code (even if we work with `Julia`). For my section it is more important that you understand the machine learning concepts and then you can implement it in any language that you prefer. At this stage in your career as an economist / data scientist, you can focus on one programming language to fulfill most of your needs. However, as you develop your skills you will notice that the language you use is almost irrelevant. Someone that is highly trained in `Julia`, for example, and knows how to execute certain ideas effectively in that language should be able to transfer those skills to other languages in a short time frame. The reason to showcase `Julia` in this course is then partly to introduce you to a new language and then show that you can easily switch between languages if needed. In addition, I will show (using examples) that sometimes one tool might be better for a specific goal.  

# Topics

Below are some of the topics that we will cover during this term.

1. Introduction to `Julia` (self-study)
2. Working with data in `Julia` (self-study)
3. Linear algebra and optimisation
4. Linear and polynomial regression
5. k-Nearest neighbours
6. Tree-based methods
7. Support vector machines
8. Neural networks 
9. Parallel programming
10. Cloud computing with Google Compute Engine
11. Databases (SQL and BigQuery)
12. Spark and `R` / `Julia`

We will not have time to cover all the topics in full detail, so you can refer to the notes if you would like to know more. I will also link to other sets of notes so that you can read in more detail on some of the issues at hand. Since most of you have little experience with machine learning and programming, we will be taking things quite slow. In that sense this course provides you the basic tools from which you can go and further explore. 

# Textbook

For the linear algebra we will use a small portion of `Introduction to Applied Linear Algebra` by Stephen Boyd and Lieven Vandenberghe and for the optimisation section I will be looking at some of the material in the textbook `Algorithms for Optimization` by Mykel J. Kochenderfer and Tim A. Wheeler. The linear algebra book can be downloaded [here](http://vmls-book.stanford.edu/). Unfortunately, I don't have a free book for optimisation at present, so you will have to rely on my notes for the basic ideas. 

In terms of machine learning the main textbook that we will use is Introduction to Statistical Learning by Gareth James, Daniela Witten, Trevor Hastie (a fellow South African) and Robert Tibshirani. A free version of the book can be downloaded [here](http://faculty.marshall.usc.edu/gareth-james/ISL/). The code for the book is presented in `R`, but I will provide both `Julia` and `Python` code to replicate the labs and figures in the book, so that you can see how we can use different languages to solve the same problem. 