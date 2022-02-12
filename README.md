# Data Science for Economics and Finance

[`Schedule`](#schedule) | [`Project`](#project) |
[`Resources`](#resources) 

On this page we have the course notes for the second part of the Data Science 871 module. 

The first part is taught by [Nico Katzke](https://github.com/nicktz) and focuses on data wrangling and good programming practices. You can find his notes [here](https://datsci.nfkatzke.com/).

In this part of the course we will cover many different topics. The idea is to give you a whirlwind tour of many of the important ideas in Data Science. 

We will be using R as our primary language for this course. However, I would like to introduce you to the basics of Julia. 

I really enjoy coding in **Julia**, which is one of the main reasons I like to share it with others. Julia is used primarily in scientific computing, but recently there has been a shift toward using Julia for application in Data Science. This will definitely be a language to keep an eye out for in the future. The syntax of the language feels like a combination of Matlab and Python. If you are thinking of taking the advanced time series course then you might want to pay careful attention to the Julia component of the course, since we will use it there. Julia is not used as much in industry. It is used more at research institutions such as Universities.  

The most popular language for machine learning is **Python**. I will provide some nice links to resources for getting started with Python. We will quickly talk about the differences between languages throughout the course. We hope that you realise after this course that the choice of language is *not important to your success*. Most languages are very similar and you should be able to switch pretty easily between languages once you know the basic principles of programming. I have found that a lot of people in industry use Python, especially engineers, applied mathematicians, computer scientists, etc. So a getting to know some Python in the future is not a bad idea. 

My advice for the beginner is to pick the language you can most easily express yourself in when attempting new projects (try and start with R). Become comfortable with that language and then you can look to expand your portfolio after you feel like you can code in that one language. The reason for showing Julia in this course is so that you can compare it with R (and any other language you know) and decide which language you prefer. If you enjoy programming in a language you will do more of it, so it is worthwhile figuring out what you like. I mostly use Julia and Python, but you might find your niche somewhere else. 

Below are my details. You can contact me via email. If I don't respond within a day or so, please remind me with a follow up email. 

|  | [Dawie van Lill](https://dawievanlill.netlify.app/) |
|--------------|--------------------------------------------------------------|
| Email | [dvanlill@sun.ac.za](mailto:dvanlill@sun.ac.za) |
| Office | Schumann 511 |
| GitHub | [DawievLill](https://github.com/DawievLill) |

## Schedule 

This course schedule will be updated frequently, so please check before lecture for the requisite readings and lecture notes. The notebooks and slides that I provide are like brief summaries of the readings. If you want more information you should do the readings or look at the references below. 

| Topic | R Notebooks | Julia Notebooks 🚧 | Python Notebooks 🚧 | Readings
|---|---|---|---|---|
| Shell |  [[.rmd](https://github.com/DawievLill/DataScience-871/blob/master/01-shell/01-shell.Rmd) / [.html]()]  | | |  Merely Useful [Ch2-5](https://merely-useful.tech/py-rse/bash-basics.html) + EC607 [Slides](https://raw.githack.com/uo-ec607/lectures/master/03-shell/03-shell.html#1) |
| Git, Github and Make  | [[.rmd]() / [.html]()]  | | | EC 607 [Slides](https://raw.githack.com/uo-ec607/lectures/master/02-git/02-Git.html#1) |
| SQL basics | [[.rmd]() / [.html]()]  | | | EC 607 [notes](https://raw.githack.com/uo-ec607/lectures/master/16-databases/16-databases.html) + Software Carpentry [notes](https://swcarpentry.github.io/sql-novice-survey/) |
| Introduction to Julia | | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()] | [Basics](https://juliadatascience.io/julia_basics) + QE [notes](https://julia.quantecon.org/intro.html) + CTU [notes](https://juliateachingctu.github.io/Julia-for-Optimization-and-Learning/stable/)   |
| Data basics with Julia | | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()] | [DataFrames.jl](https://juliadatascience.io/dataframes) + official documentation [here](https://dataframes.juliadata.org/stable/)  |
| Fundamentals of machine learning | [[.rmd]() / [.html]()]      | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()] |BB [notes](https://bradleyboehmke.github.io/HOML/intro.html)   |
| Regularized regression  | [[.rmd]() / [.html]()]    | [[.rmd]() / [.html]()]   | [[.rmd]() / [.html]()] | BB [notes](https://bradleyboehmke.github.io/HOML/regularized-regression.html)  |
| Decision trees and bagging | [[.rmd]() / [.html]()]   | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()] | BB [notes](https://bradleyboehmke.github.io/HOML/DT.html)   |
| Random forests and gradient boosting | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()] | BB [notes](https://bradleyboehmke.github.io/HOML/gbm.html)  |
| Functions | [[.rmd]() / [.html]()]     | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()] | EC 607 [notes # 1](https://raw.githack.com/uo-ec607/lectures/master/10-funcs-intro/10-funcs-intro.html) + EC607 [notes #2](https://raw.githack.com/uo-ec607/lectures/master/11-funcs-adv/11-funcs-adv.html)   |
| Parallel programming | [[.rmd]() / [.html]()]     | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()] | EC 607 [notes](https://raw.githack.com/uo-ec607/lectures/master/12-parallel/12-parallel.html)  |
| Cloud computing  |  [[.rmd]() / [.html]()]    | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()] | EC 607 [notes # 1](https://raw.githack.com/uo-ec607/lectures/master/14-gce-i/14-gce-i.html) + EC607 [notes #2](https://raw.githack.com/uo-ec607/lectures/master/14-gce-ii/14-gce-ii.html)   |
| Working with Big Data |  [[.rmd]() / [.html]()]    | [[.rmd]() / [.html]()]  | [[.rmd]() / [.html]()] | EC 607 [notes](https://raw.githack.com/uo-ec607/lectures/master/17-spark/17-spark.html)   |

## Project

In this part of the course there is no exam, only a final project. We will discuss this project in more detail during the semester. However, the basic idea is that you apply machine learning techniques to any type of data that you find interesting. The topic should ideally be related to economics. Please consult with me or Nico about your topics, so that we can talk about the availability of data and whether the project is feasible. We prefer that you code in R, but for those that want to code in Python or Julia please come and have a chat. 

## Resources

An alternative to the shell notes that I linked would be the following

- [Shell] Software Carpentry. The Unix Shell. https://swcarpentry.github.io/shell-novice/

For the SQL component we will reference the following,

- [SQL] Software Carpentry. Databases and SQL. https://swcarpentry.github.io/sql-novice-survey/

We will work through the basics of Python, but if you want a good introduction to Julia I would recommend, 

- [Julia] QuantEcon. Getting Started with Julia. https://julia.quantecon.org/getting_started_julia/index.html
- [Julia] Paul Soderlind. Julia Tutorial. https://github.com/PaulSoderlind/JuliaTutorial
- [Julia] Ben Lauwens and Allen Downey (2018). Think Julia: How to Think Like a Computer Scientist. https://benlauwens.github.io/ThinkJulia.jl/latest/book.html

For data science components in R we will use, 

- [R] Grant McDermott (2021). Data Science for Economists and Other Animals. https://grantmcdermott.com/ds4e/index.html

For data science in Julia a good textbook is, 

- [Julia] Jose Storopoli, Rik Huijzer and Lazaro Alonso (2021). Julia Data Science. https://juliadatascience.io.

For the machine learning in R we will be using material from the following book, 

- [R] Bradley Boehmke and Brandon Greenwell (2021). Hands-on Machine Learning with R. https://bradleyboehmke.github.io/HOML/

If you want machine learning tutorials in Julia then you could look at, 

- [Julia] Data Science Tutorials in Julia. https://juliaai.github.io/DataScienceTutorials.jl/

Other resources might also be used, check the reading list for each of the lectures. 








