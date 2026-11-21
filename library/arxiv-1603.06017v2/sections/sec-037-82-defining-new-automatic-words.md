---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-037-82-defining-new-automatic-words
section_title: "Defining New Automatic Words"
section_number: 8.2
pages: 33-33
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.879
latex_coverage_ratio: 0.967
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:define new automatic words}
The eval and def commands always produce automata accepting a predicate, therefore the result is never an automaton with output. So to define an automatic word $W$, we need to manually define its corresponding automaton with output in the directory ``/Walnut/Word Automata Library/''. For example, the Thue-Morse word is defined in the file ``/Walnut/Word Automata Library/T.txt'' as follows:
\begin{figure}[H]
\begin{CenteredBox}
\begin{lstlisting}[style=file]
msd_2
0 0
0 -> 0
1 -> 1
1 1
0 -> 1
1 -> 0
\end{lstlisting}
\end{CenteredBox}
\captionof{lstlisting}{T.txt}
\label{file:thue morse}
\end{figure}
