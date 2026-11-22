---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-034-76-load-load-file-name
section_title: "load: load <file name>"
section_number: 7.6
pages: 31-32
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.926
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:load}
We can write any series of legitimate Walnut commands in a text file and save it in the directory ``/Walnut/Command Files/''. Then we can load it by writing the following in Walnut:
\begin{lstlisting}[style=reg]
load file_name.txt;
\end{lstlisting}
This runs all commands in file\_name.txt in the order they appear. 
Recall that the file's encoding must be UTF-8.
