Working with data
==============================================

Working with data in `Julia` will entail some basic familiarity with the `DataFrames.jl` and `CSV.jl` packages. These package form part of the `Julia Data` group of packages that are used for data manipulation, storage and input/output in `Julia`. One could also work with packages from the `Queryverse`, which are packages written for data science application. However, let's not get ahead of ourselves. We start with `DataFrames.jl` and `CSV.jl` and move on from there. 

## Importing data 

One of the first things that you will most likely do in data science is to import an existing dataset. Most of the time in economics these datasets will take a comma separated value (CSV) file format. These are delimited text files that use a comma to separate the values. This is not the only file format that you will encounter, but we will start with CSV and then move on to more exotic file formats such as Feather, Excel, Parquet, Stata, etc.  
