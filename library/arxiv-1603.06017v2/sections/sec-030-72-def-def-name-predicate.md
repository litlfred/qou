---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-030-72-def-def-name-predicate
section_title: "def: def <name> <predicate>"
section_number: 7.2
pages: 26-27
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.963
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:def}
The word def stands for define. The syntax for this command is exactly the same as the syntax for eval command. The only difference between this command and eval is that the automaton constructed is saved in the directory ``/Walnut/Automata Library/'' for later use.  Suppose we write the following:
\begin{lstlisting}[style=cmd]
def sum10 "(*\textcolor{blue}{$x+y=10$}*)";
\end{lstlisting}
This creates as usual the files sum10.gv, sum10.txt, and sum10\_log.txt in the directory ``/Walnut/Result/''. However, it also saves a copy of sum10.txt in the directory ``/Walnut/Automata Library/''. Any automaton saved in this directory can be called in other predicates by referring to its name and the special character \$. To learn about calling see Sections \ref{sec:calling expressions} and \ref{sec:calling an automaton}.

Let us see examples of predicates calling the automaton sum10:
\begin{lstlisting}[style=cmd]
eval lessThanThree "(*\textcolor{blue}{$\text{E}a\text{ }a\mathbin{\text{>=}}8 \mathbin{\&} \$\text{sum10}(b,a)$}*)";
\end{lstlisting}
This predicate is satisfied by numbers $b$ for which there exist an $a\mathbin{\text{>=}}8$ such that $b+a=8$, i.e., $0,1,2$:
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{lessThanThree}
	\caption{lessThanThree.gv}
	\label{fig:lessThanThree}
\end{figure}

We can send the same variable to both arguments of sum10:
\begin{lstlisting}[style=cmd]
eval five "(*\textcolor{blue}{$\$\text{sum10}(a,a)$}*)";
\end{lstlisting}
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{five}
	\caption{five.gv}
	\label{fig:five}
\end{figure}

We can send constants to any arguments of sum10:
\begin{lstlisting}[style=cmd]
eval three "(*\textcolor{blue}{$\$\text{sum10}(7,a)$}*)";
\end{lstlisting}
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{three}
	\caption{three.gv}
	\label{fig:three}
\end{figure}

Indeed, we can send any arithmetic expressions or predicates with one free variable to arguments:
\begin{lstlisting}[style=cmd]
eval three "(*\textcolor{blue}{$\$\text{sum10}(a-2,3*a)$}*)";
\end{lstlisting}
\begin{lstlisting}[style=cmd]
eval three "(*\textcolor{blue}{$\text{E}b\text{ }\$\text{sum10}(a,b+3=10)$}*)";
\end{lstlisting}
The resulting automaton for both of these is depicted in Figure \ref{fig:three}. We can call sum10 to define new automata:
\begin{lstlisting}[style=cmd]
def threeSum10 "(*\textcolor{blue}{$\$\text{sum10}(x+y,z)$}*)";
\end{lstlisting}
Now we can write 
\begin{lstlisting}[style=cmd]
eval three "(*\textcolor{blue}{$\text{E}y,z\text{ }\$\text{threeSum10}(x,y,z) \mathbin{\&} y=2 \mathbin{\&} z=5$}*)";
\end{lstlisting}
The result of this evaluation is again depicted in Figure \ref{fig:three}.

Now look at the following example:
\begin{lstlisting}[style=cmd]
eval nonsense "(*\textcolor{blue}{$\$\text{sum10}(a=b,4)$}*)";
\end{lstlisting}
\vspace*{-\baselineskip}
\begin{lstlisting}[style=err]
argument 1 of function sum10 cannot be an automaton with != 1 inputs
	: char at 1
	: eval nonsense "(*$\$\text{sum10}(a=b,4)$*)";
\end{lstlisting}
This is because the first argument is a predicate with two free variables.

We cannot send a variable in $\LSD[2]$ to an automaton that accepts only $\MSD[2]$, and expect getting anything interesting in return. The following example would run fine, but the result is another nonsense:
\begin{lstlisting}[style=cmd]
eval another_nonsense "(*\textcolor{blue}{$\text{?lsd\_2 }\$\text{sum10}(x,4)$}*)";
\end{lstlisting}
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{another_nonsense}
	\caption{another\_nonsense.gv}
	\label{fig:another nonsense}
\end{figure}

The number of arguments when calling an automaton should match the number of inputs of that automaton:
\begin{lstlisting}[style=cmd]
eval invalid "(*\textcolor{blue}{$\$\text{sum10}(x,y,z)$}*)";
\end{lstlisting}
\vspace*{-\baselineskip}
\begin{lstlisting}[style=err]
function sum10 requires 2 arguments
	: char at 1
	: eval invalid "(*$\$\text{sum10}(x,y,z)$*)";
\end{lstlisting}

Always remember the roles of the inputs to an automaton created by the def command. For example, look at the following examples of the def command:
\begin{lstlisting}[style=cmd]
def f1 "(*\textcolor{blue}{$y < x$}*)";
def f2 "(*\textcolor{blue}{$x < y$}*)";
\end{lstlisting}
Now the following evaluates to an automaton accepting representations of numbers $>1$:
\begin{lstlisting}[style=cmd]
eval greater_than_1 "$f1(a,1)";
\end{lstlisting}
whereas the following evaluates to an automaton accepting representations of numbers $<1$: 
\begin{lstlisting}[style=cmd]
eval less_than_1 "$f2(a,1)";
\end{lstlisting}
This is because f1 is an automaton for which the first argument is greater than the second argument, whereas, f2 is an automaton for which the first argument is less than the second argument. \emph{Always remember that Walnut sorts inputs of an automaton based on their labels' lexicographic order.}
