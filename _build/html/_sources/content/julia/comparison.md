
# Comparing performance between R and Julia

Quote from Chris Rackaukus

``Julia is faster than other scripting languages, allowing you to have the rapid development of Python/MATLAB/R while producing code that is as fast as C/Fortran``

https://ucidatascienceinitiative.github.io/IntroToJulia/Html/WhyJulia

There are multiple metrics that one can use to compare languages. I want to provide you with some reasons why I prefer Julia over R (especially for tasks that are computationally intensive). I will also direct you to some resources that do similar comparisons.

A well known-example of the computational efficiency of Julia is provided by Doug Bates. He is a developer responsible for many of the R packages that are at the core of the language. The example below uses Gibbs sampling. Don't worry about the specifics of Gibbs sampling for now, we will cover this in great detail in the Advanced Time Series course in the second semester. I am developing some notes for that [here].

## Douglas Bates Gibbs sampling example

Gibbs sampling is quite common in statistics, especially in Bayesian statistics. In the Bayesian context this Markov Chain Monte Carlo (MCMC) method attempts to sample from full conditional distributions to help us understand (via Bayes theorem) some specific quantities related to the posterior distribution. Here is the specific code for the example in R.

R"""
library(Matrix)

Rgibbs <- function(N, thin) {
  mat <- matrix(0, nrow=N, ncol=2)
  x <- y <- 0
  for (i in 1:N) {
    for (j in 1:thin) {
      x <- rgamma(1, 3, y * y + 4) # 3rd arg is rate
      y <- rnorm(1, 1 / (x + 1), 1 / sqrt(2 * (x + 1)))
    }
    mat[i,] <- c(x, y)
  }
  mat
}
"""
R"""
system.time(Rgibbs(10000, 500))
"""

Conversely the code for Julia is provided below.

using Distributions

function jgibbs(N, thin)
    mat = zeros(N, 2)
    x = y = 0.0
    for i in 1:N
        for j in 1:thin
            x = rand(Gamma(3, 1 / (y * y + 4)))
            y = rand(Normal(1 / (x + 1), 1 / sqrt(2(x + 1))))
        end
        mat[i, 1] = x
        mat[i, 2] = y
    end
    mat
end

jgibbs(100, 5); # warm-up
@elapsed jgibbs(10000, 500)

In this example we see that Julia is somewhere in the range of 40 to 80 times faster. This is quite significant, considering that the actual coding related to the functions specified is very similar. It does not require much in terms of a time investment to learn the difference in syntax. Programming does not stop at difference in syntax, but the general point is that even for someone with little programming experience, the increase in speed is perhaps enough motivation to take interest in the Julia project.

It is true that one can use `Rcpp`, which is a library in `R` that allows you to input `C++` code and interface with `R`. The benefit here is that you will also see an immense increase in terms of performance. The disadvantage is that you will need to learn some `C++`, which is arguably more difficult to learn than `Julia`. I have some base level knowledge of `C++`, but have to spend much more time with it to reap the benefits. In contrast, in my opinion as an economist, and not a programmer, by profession, `Julia` is easier to digest.

There are other examples that we can use that are perhaps a bit easier to digest.

## Julia, R, Python, C?

Compare a few different languages.

Construct an example using some basic method that uses a for loop. Something like the mean builtin function -- see the example here https://ucla-biostat-257-2020spring.github.io/slides/02-langs/langs.html
