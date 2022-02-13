#!/usr/bin/env Rscript

n <- as.integer(commandArgs(trailingOnly = TRUE))
if (length(n) == 0) n <- 10

f_text <- file("stdin")
lines <- tolower(readLines(f_text))
words <- unlist(regmatches(lines, gregexpr("[a-z']{2,}", lines)))
counts <- sort(table(words), decreasing = TRUE)
cat(sprintf("%7d %s\n", counts[1:n], names(counts[1:n])), sep = "")
close(f_text)
