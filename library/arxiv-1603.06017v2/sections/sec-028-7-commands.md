---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-028-7-commands
section_title: "Commands"
section_number: 7
pages: 20-22
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.597
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:commands}
Every command ends in either a colon, double colon, or a semicolon. If you want to see the reports on the intermediate steps of a computation use colon or double colon, otherwise use semicolon. For example, if we type:
\begin{lstlisting}[style=cmd]
eval test "(*\textcolor{blue}{$a=b+1$}*)":
\end{lstlisting}
we get an output similar to the following written in the console:
\begin{lstlisting}[style=out]
(*\textcolor{out}{$a=b+1$}*):2 states - 1ms
total computation time: 2ms
\end{lstlisting}
which explains that the automaton for predicate $a=b+1$ has 2 states
and it took 2 milliseconds to compute it. We use {\color{blue}blue} to
denote predicates. Here we use {\color{out} grey} to indicate the
output produced by Walnut in the console. We use {\color{red} red} to
indicate errors in the console.

Walnut prints to console only the major steps of a computation when a single colon is used to end a command. Use two colons if you want to see all the steps behind the scene (cross product \ref{sec:cross product}, quantification \ref{sec:quantification}, minimizations, converting NFAs to DFAs (determinizations), etc.):

\begin{lstlisting}[style=cmd]
eval test "(*\textcolor{blue}{$a=b+1$}*)"::
\end{lstlisting}
then we get an output similar to the following written in the console:
\begin{lstlisting}[style=out]
computing (*\textcolor{out}{$b+1$}*)
computed (*\textcolor{out}{$a+1$}*)
computing (*\textcolor{out}{$a=(b+1)$}*)
	computing (*\textcolor{out}{$\&$}*):1 states - 2 states
	computing cross product:1 states - 2 states
	computed cross product:2 states - 1ms
		minimizing:2 states
			determinizing:2 states
			determinized:2 states - 0ms
		minimized:2 states - 0ms
	computed (*\textcolor{out}{$\&$}*):2 states - 1ms
	quantifying:2 states
		minimizing:2 states
			determinizing:2 states
			determinized:2 states - 0ms
		minimized:2 states - 0ms
	quantified:2 states - 0ms
	fixing leading zeros:2 states
		determinizing:2 states
		determinized:2 states - 1ms
		minimizing:2 states
			determinizing:2 states
			determinized:2 states - 0ms
		minimized:2 states - 0ms
	fixed leading zeros:2 states - 1ms
computed (*\textcolor{out}{$a=(b+1)$}*)
(*\textcolor{out}{$a=(b+1)$}*):2 states - 2ms
total computation time: 34ms
\end{lstlisting}

Whitespace is ignored. You can, for example, span one single command into multiple lines to improve readability. So, for example, you can write the following interchangeably:
\begin{lstlisting}[style=cmd]
eval test "(*\textcolor{blue}{$a=b+1$}*)";
eval test
"(*\textcolor{blue}{$a=b+1$}*)";
eval test "(*\textcolor{blue}{$a$}*)
(*\textcolor{blue}{$=b+1$}*)";
eval test
"(*\textcolor{blue}{$a=b+1$}*)"
;
\end{lstlisting}

In case we forget to separate the name test and predicate $a=b+1$ of the eval command, Walnut catches it by returning an error:
\begin{lstlisting}[style=cmd]
eval test"(*\textcolor{blue}{$a=b+1$}*)":
\end{lstlisting}
\vspace*{-\baselineskip}
\begin{lstlisting}[style=err]
invalid use of eval/def command
	: eval test"(*$a=b+1$*)":
\end{lstlisting}


Here is the full list of commands in Walnut and we will go over them one by one in detail:
\begin{itemize}
\item exit
\item eval <name> <predicate> 
\item def <name> <predicate>
\item macro <name> <template>
\item reg <name> <number system> <regular expression>
\item reg <name> <alphabet> <regular expression>
\item load <file name>
\end{itemize}
