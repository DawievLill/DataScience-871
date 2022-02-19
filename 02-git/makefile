all: report.html

clean:
	rm -f ./data/stellies-speech.pdf
	rm -f ./data/stellies-speech.txt
	rm -f ./figures/wordcloud.pdf
	
stellies-speech.pdf:
	curl -s "https://www.resbank.co.za/content/dam/sarb/publications/speeches/speeches-by-governors/2021/gov-kganyago/A%20public%20lecture%20by%20Lesetja%20Kganyago%20Governor%20of%20the%20South%20African%20Reserve%20Bank%20at%20Stellenbosch%20University.pdf" > ./data/stellies-speech.pdf   

pdf_to_text: stellies_speech.pdf
	pdftotext ./data/stellies-speech.pdf
	
wordcloud: ./scripts/wordcloud.R ./data/stellies-speech.txt
	Rscript $<
	
move_plot: wordcloud
	mv Rplots.pdf ./figures/wordcloud.pdf

report.html: ./scripts/report.rmd move_plot 
	Rscript -e 'rmarkdown::render("$<")'
