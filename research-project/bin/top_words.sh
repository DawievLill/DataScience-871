#!/usr/bin/env bash

curl -sL "https://www.gutenberg.org/files/11/11-0.txt" |                        
tr '[:upper:]' '[:lower:]' |            
grep -oE "[a-z\']{2,}" |                
sort |                              
uniq -c |           
sort -nr |          
head -n 10   
