---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-039-84-converting-gv-files-to-jpeg
section_title: "Converting .gv files to .jpeg"
section_number: 8.4
pages: 34-34
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.842
latex_coverage_ratio: 0.97
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
The drawings of automata in Walnut are stored in .gv files. Not only can the software Graphviz open the files with this extension,
but it can also convert them to many different file formats. For example, suppose you have a file named automaton.gv. To convert it to automaton.jpeg type the following in the terminal:
\begin{lstlisting}[language=bash]
$dot -Tjpg automaton.gv -o automaton.jpeg 
\end{lstlisting} 
See \href{http://www.graphviz.org/}{Graphviz} to learn how to convert
.gv files to other file types.

\printbibliography[heading=bibintoc]
