all:
	latex beamer.tex
	latex beamer.tex
	bibtex beamer
	latex beamer.tex
	latex beamer.tex
	dvips -o beamer.ps beamer.dvi
	ps2pdf -sPAPERSIZE=a4 -DMaxSubsetPct=100 -dCompatibilityLevel=1.2 -dSubsetFonts=true -dEmbedAllFonts=true beamer.ps beamer.pdf

clean:
	rm -f *.toc *.ps *.log *.lof *.lot *.dvi *.aux *.blg *.bbl
