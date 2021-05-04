
if (!require("pacman")) install.packages("pacman")
pacman::p_load(pbapply, data.table, tidyverse, memoise, here)


square =        ## Our function name
  function(x) { ## The argument(s) that our function takes as an input
    x^2         ## The operation(s) that our function performs
  }

square(3)

square = 
  function(x) { 
    x_sq = x^2    ## Create an intermediary object (that will be returned)
    return(x_sq)  ## The value(s) or object(s) that we want returned.
  }

square(5)

square = 
  function(x) { ## The argument(s) that our function takes as an input
    x_sq = x^2  ## The operation(s) that our function performs
    return(list(value=x, value_squared=x_sq)) ## The list of object(s) that we want returned.
  }

square(3)

square = 
  function(x) { 
    x_sq = x^2 
    df = tibble(value=x, value_squared=x_sq) ## Bundle up our input and output values into a convenient dataframe.
    return(df)
  }

square(12)

square = 
  function(x = 1) { ## Setting the default argument value 
    x_sq = x^2 
    df = tibble(value=x, value_squared=x_sq)
    return(df)
  }

square()  ## Will take the default value of 1 since we didn't provide an alternative.
square(2) ## Now takes the explicit value that we give it.

square = 
  function(x = NULL) {  ## Default value of NULL
    if (is.null(x)) x=1 ## Re-assign default to 1
    x_sq = x^2 
    df = tibble(value=x, value_squared=x_sq)
    return(df)
  }
square()

square = 
  function(x = NULL) {
    if (is.null(x)) { ## Start multiline if statement with `{`
      x=1
      message("No input value provided. Using default value of 1.") ## Message to users
    } ## Close multiline if statement with `}`
    x_sq = x^2 
    df = tibble(value=x, value_squared=x_sq)
    return(df)
  }
square()


eval_square =
  function(x) {
    if (square(x)$value_squared == x*x) { ## condition
      ## What to do if the condition is TRUE 
      message("Nailed it.")
    } else {
      ## What to do if the condition is FALSE
      message("Dude, your function sucks.")
    }
  }
eval_square(64)


x = 1:10
## dplyr::case_when()
case_when(
  x <= 3 ~ "small",
  x <= 7 ~ "medium",
  TRUE ~ "big" ## Default value. Could also write `x > 7 ~ "big"` here.
)
## data.table::fcase()
fcase(
  x <= 3, "small",
  x <= 7, "medium",
  default = "big" ## Default value. Could also write `x > 7, "big"` here.
)

## dplyr::case_when()
tibble(x = 1:10) %>%
  mutate(grp = case_when(x <= 3 ~ "small",
                         x <= 7 ~ "medium",
                         TRUE ~ "big"))
## data.table::fcase()
data.table(x = 1:10)[, grp := fcase(x <= 3, "small",
                                    x <= 7, "medium",
                                    default = "big")][]


square(1:5)
square(c(2, 4))

for(i in 1:10) print(LETTERS[i])


kelvin = 300:305
fahrenheit = NULL
# fahrenheit = vector("double", length(kelvin)) ## Better than the above. Why?
for(k in 1:length(kelvin)) {
  fahrenheit[k] = kelvin[k] * 9/5 - 459.67
}
fahrenheit

# for(i in 1:10) print(LETTERS[i]) ## Our original for loop (for comparison)
lapply(1:10, function(i) LETTERS[i])

lapply(1:10, function(i) {
  df = tibble(num = i, let = LETTERS[i])
  return(df)
}) %>%
  bind_rows()

sapply(1:10, function(i) LETTERS[i]) 

# library(pbapply) ## Already loaded

pblapply(1:10, function(i) {
  df = tibble(num = i, let = LETTERS[i])
  Sys.sleep(1)
  return(df)
}) %>%
  bind_rows()

map(1:10, function(i) { ## only need to swap `lapply` for `map`
  df = tibble(num = i, let = LETTERS[i])
  return(df)
})

map_df(1:10, function(i) { ## don't need bind_rows with `map_df`
  df = tibble(num = i, let = LETTERS[i])
  return(df)
})

## Create a named function
num_to_alpha = 
  function(i) {
    df = tibble(num = i, let = LETTERS[i])
    return(df)
  }

lapply(1:10, num_to_alpha) %>% bind_rows()

map_df(c(1, 5, 26, 3), num_to_alpha)

## Create a named function
multi_func = 
  function(x, y) {
    df = 
      tibble(x = x, y = y) %>%
      mutate(z = (x + y)/sqrt(x))
    return(df)
  }

multi_func(1, 6)

## Note that the inputs are now moved to the *end* of the call. 
## Also, mapply() is based on sapply(), so we also have to tell it not to 
## simplify if we want to keep the list structure.
mapply(
  multi_func,
  x = 1:5,         ## Our "x" vector input
  y = 6:10,        ## Our "y" vector input
  SIMPLIFY = FALSE ## Tell it not to simplify to keep the list structure
) %>%
  bind_rows()

## Note that the inputs are combined in a list.
pmap_df(list(x=1:5, y=6:10), multi_func)

parent_func =
  ## Main function: Takes a single data frame as an input
  function(input_df) {
    df =
      ## Nested iteration function
      map_df(
        1:nrow(input_df), ## i.e. Iterate (map) over each row of the input data frame
        function(n) {
          ## Extract the `x` and `y` values from row "n" of the data frame
          x = input_df$x[n]
          y = input_df$y[n]
          ## Use the extracted values
          df = multi_func(x, y)
          return(df)
        })
    return(df)
  }

## Case 1: Iterate over x=1:5 and y=6:10
input_df1 = tibble(x=1:5, y=6:10)
parent_func(input_df1)

## Case 2: Iterate over *all possible combinations* of x=1:5 and y=6:10
input_df2 = expand.grid(x=1:5, y=6:10)
# input_df2 = expand(input_df1, x, y) ## Also works
parent_func(input_df2)

square = 
  function(x = 1) {
    x_sq = x^2 
    d = tibble(value=x, value_squared=x_sq)
    return(d)
  }

square("one") 


square_ifelse = 
  function (x = 1) { 
    if (is.numeric(x)) { ## Check that this is a valid argument to our function.
      x_sq = x^2 
      d = tibble(value=x, value_squared=x_sq)
      return(d) 
    } else { ## Return a warning message if not.
      message("Sorry, you need to provide a numeric input variable.")
    }
  }


square_ifelse("one") ## Will trigger our warning message.
square_ifelse(1) ## Works.


square_stop = 
  function (x = 1) { 
    if (!is.numeric(x)) stop("Sorry, you need to provide a numeric input variable.")
    x_sq = x^2 
    d = tibble(value=x, value_squared=x_sq)
    return(d) 
  }
square_stop("one") ## Triggers a stop error and warning
square_stop(1) ## Works

tryCatch(
  square("three"), 
  error = function(e) message("Sorry, something went wrong. Did you try to square a string instead of a number?")
)

tryCatch(
  square(c(1,2,"three")), 
  error = function(e) message("Sorry, something went wrong. Did you try to square a string instead of a number?")
)

square_trycatch =
  function (x = 1) {
    x_sq = tryCatch(x^2, error = function(e) NA_real_) ## tryCatch goes here now. Produce an NA value if we can't square the input.
    d = tibble(value=x, value_squared=x_sq)
    return(d)
  }

square_trycatch(c(1,2,"three"))

str(c(1,2,"three"))

map_df(list(1,2,"three"),  square_trycatch)

square_trycatch2 =
  function (x = 1) {
    x_sq = tryCatch(x^2, error = function(e) NA_real_) 
    d = tibble(value=as.numeric(x), value_squared=x_sq) ## Convert input to numeric
    return(d)
  }

map_df(list(1,2,"three"), square_trycatch2)

square_simple =
  function (x = 1) {
    x_sq = x^2
  }
square_safely = safely(square_simple)
square_safely("three")

square_safely = safely(square_simple, otherwise = NA_real_)
square_safely("three")

## Emulate slow function
slow_square = 
  function(x) {
    Sys.sleep(2)
    square(x)
  }

# library(memoise) ## Already loaded

mem_square = memoise(slow_square)

system.time({
  m1 = map_df(1:10, mem_square)
})

system.time({
  m2 = map_df(1:10, mem_square)
})

all.equal(m1, m2)
m2

system.time({
  m3 = map_df(1:15, mem_square)
})

mem_square_verbose = 
  function(x) {
    ## 1. Load cached data if already generated
    if (has_cache(mem_square_persistent)(x)) {
      cat("Loading cached data for x =", x, "\n")
      my_data = mem_square_persistent(x)
      return(my_data)
    }
    
    ## 2. Generate new data if cache not available
    cat("Generating data from scratch for x =", x, "...")
    my_data = mem_square_persistent(x)
    cat("ok\n")
    
    return(my_data)
  }


