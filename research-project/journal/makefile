all: draft_journal_entry.txt readme.txt

draft_journal_entry.txt:
	touch draft_journal_entry.txt
	
readme.txt: toc.txt
	echo "This journal contains the following number of entries:" > readme.txt
	wc -l toc.txt | egrep -o "[0-9]+" >> readme.txt
	
clean:
	rm draft_journal_entry.txt
	rm readme.txt
