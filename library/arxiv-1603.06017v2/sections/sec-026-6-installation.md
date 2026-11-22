---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-026-6-installation
section_title: "Installation"
section_number: 6
pages: 20-20
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.949
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:installation}
Walnut is a command line program. You can run Walnut on any platform as long as you have Java 8 or later (preferably JDK 8 or higher) installed. To see which version of Java is installed on your machine type the following in the terminal (without the command line prompt \$):
\begin{lstlisting}[language=bash]
$java -version
\end{lstlisting}
If you download Walnut as the zipped file Walnut.zip first thing you need to do is to uncompress it. Then open the terminal (or command prompt in Windows), and change the directory to ``.../Walnut/bin/'', and run Walnut by typing:
\begin{lstlisting}[language=bash]
$java Main.prover
\end{lstlisting}
To exit Walnut, type the following command (with the semicolon):
\begin{lstlisting}[style=cmd]
exit;	
\end{lstlisting}
To make the distinction that we are typing a Walnut command, names of
all Walnut's commands are written in {\color{cmd} green}.  Walnut
produces graphical representations of automata among other things.
Those representations are files with .gv extensions. In order to open
these files you need to install Graphviz, a graph visualization package
which is available for all platforms.
\emph{All text files that Walnut produces are in the UTF-8 encoding.
All text files that Walnut reads have to be in the  UTF-8 encoding as well. Most editors, e.g., vim, notepad, etc., use UTF-8 encoding by default.}
