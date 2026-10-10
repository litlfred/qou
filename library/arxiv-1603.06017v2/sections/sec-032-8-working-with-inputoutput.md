---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut Hamoon Mousavi"
section_id: sec-032-8-working-with-inputoutput
section_title: "Working with Input/Output"
section_number: 8
pages: 32-34
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut Hamoon Mousavi — 34 sections: Introduction; Basics; Words and Automata"
---
\label{sec:working with input and output}
Throughout this section it is assumed that all files have UTF-8 encoding. This is the default encoding for most text editors.

\subsection{Defining Automata in Text Files}\label{sec:define automata in text files}
In this section we learn how to manually define all automata types in
text files. Recall that an ordinary automaton can be thought of as an
automaton with output, in which states with non-zero outputs are
treated as final states; see Section \ref{sec:words and automata}.
Therefore suppose
$M\big(Q,q_0,O,\delta,\Sigma,\mathbf{S_1},\mathbf{S_2},\ldots,\mathbf{S_n}\big)$
is an automaton with output with $m$ states and $n$ inputs over number
systems $\mathbf{S_i}$. Furthermore suppose that the states are labeled
$0$ to $m-1$, i.e., $Q=\big\{0,1,\ldots,m-1\big\}$, and that
$q_0=0$\footnote{If an automaton does not follow these criteria we can
always come up with an isomorphic one that does.}. To define $M$ in a
text file, first create a text file M.txt\footnote{File names in Walnut
start with letters and can contain alphanumerics and underscore.}. The
first line must be $$S_1\text{  }S_2\text{  }\cdots\text{  }S_n$$which
declares inputs' number systems. The second line is declaring state $0$
as follows: $$0\text{  }\alpha$$ where $\alpha=O(0)$. Next lines are
declarations of transitions of state $0$ which can come in any order.
For every $\alpha_1\in \Sigma_{\mathbf{S_1}}, \alpha_2\in
\Sigma_{\mathbf{S_2}}, \ldots ,\alpha_n\in \Sigma_{\mathbf{S_n}}$
transitions are of the following form
$$\alpha_1\text{  }\alpha_2\text{  } \cdots \text{  }\alpha_n \mathbin{\text{->}} q$$
whenever $\delta\big(0,\alpha_1,\alpha_2,\ldots,\alpha_n\big) = q$.
There is no need to declare transitions to a dead state. For any pair
$(\alpha_1,\alpha_2,\ldots,\alpha_n)$ that no declaration of the form
above is mentioned, it is assumed that
$\delta(0,\alpha_1,\alpha_2,\ldots,\alpha_n)$ is a dead state. We can
use $*$, the wildcard matching symbol, in place of any symbol
$\alpha_i$. If there is a transition of the form $$\alpha_1\text{  }
\alpha_2\text{  } \ldots\text{  } \alpha_{i-1}\text{  } *\text{  }
\alpha_{i+1}\text{  }\ldots\text{  }\alpha_n \mathbin{\text{->}} q$$ it
is understood that
$\delta\big(0,(\alpha_1,\alpha_2,\ldots,\alpha_{i-1},\beta,\alpha_{i+1},\ldots,\alpha_n)\big)
= q$ for every $\beta \in \Sigma_{\mathbf{S_i}}$.  After transitions of
the state $0$ are declared, we declare state $1$ followed by its
transitions. We continue like this until all states and their
transitions are declared. Note that nowhere in M.txt we are defining
the output alphabet $\Sigma$. The output alphabet is inferred
indirectly by looking at the state declarations. To see examples refer
to Files \ref{file:two inputs}--\ref{file:general_power2}.

A non-arithmetic automaton is defined in the same way, except that in
the first line, for inputs that do not have number systems associated
with them, we write down the alphabet between curly brackets. Alphabets
can be any subset of integers. As an example see File
\ref{file:general_power2}.

Defining true or false automata in text files is easy. They have only
one line and it is either true or false.

As one last example, the paperfolding words are given by the following automaton; see Section \ref{sec:non-arithmetic automata} and article \cite{paperfolding} for more details:
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{paperfoldings}
	\caption{Automata for paperfolding words}
	\label{fig:paperfoldings}
\end{figure}
This automaton is defined in the file PF.txt in directory ``/Walnut/Word Automata Library/'':
\begin{figure}[H]
\begin{CenteredBox}
\begin{lstlisting}[style=file]
{-1,1} lsd_2

0 0
* 0 -> 0
1 1 -> 1
-1 1 -> 2

1 1
* 1 -> 4
* 0 -> 3

2 -1
* 0 -> 4
* 1 -> 3

3 1
* * -> 3

4 -1
* * -> 4
\end{lstlisting}
\end{CenteredBox}
\captionof{lstlisting}{PF.txt}
\label{file:paperfoldings}
\end{figure}


\subsection{Defining New Automatic Words}\label{sec:define new automatic words}
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

\subsection{Defining New Number Systems}\label{sec:define new number systems}

Based on Definition \ref{def:walnut_number_system}, to define a new
number system $\mathbf{S}$, we need to define automata for
$R_{\mathbf{S}}$, $+_{\mathbf{S}}$, and $<_{\mathbf{S}}$. We do not
need to define an automaton for $=_{\mathbf{S}}$, because it can be
generated easily, since we assumed that $w_1=_{\mathbf{S}} w_2$ if and
only if $w_1 = w_2$ for any two words $w_1$ and $w_2$ of the same
length. The automata for number systems must be defined in the
directory ``/Walnut/Custom Bases/''. For example, for the number system
$\mathbf{S}$, assuming it is $\MSD$, one needs to create msd\_S.txt,
msd\_S\_addition.txt, and msd\_S\_less\_than.txt for $R_{\mathbf{S}}$,
$+_{\mathbf{S}}$, and $<_{\mathbf{S}}$ respectively.  If $\mathbf{S}$
is $\LSD$, file names must be lsd\_S.txt, lsd\_S\_addition.txt, and
lsd\_S\_less\_than.txt respectively. The number system $\mathbf{S}$
defined in this way can be used in predicates by typing ?msd\_S or
?lsd\_S depending on whether $\mathbf{S}$ is $\MSD$ or $\LSD$. If the
automaton for $<_{\mathbf{S}}$ is not defined by the user, Walnut
assumes that $<_{\mathbf{S}}$ is the lexicographic ordering, i.e., if
$w_1$ and $w_2$ are of the same length, then $w_1 <_{\mathbf{S}} w_2$
if and only if $w_1$ comes before $w_2$ in lexicographic
order\footnote{Lexicographic ordering on symbols is assumed to be
$\cdots<-2<-1<0<1<2<\cdots$.}. If the automata for $R_{\mathbf{S}}$ is
not given, then $R_{\mathbf{S}}$ is assumed to be
$\Sigma_{\mathbf{S}}^*$. The alphabet $\Sigma_{\mathbf{S}}$ is inferred
from the automaton for $+_{\mathbf{S}}$ which is always given.

Note that reversing all automata for $\MSD[n]$ we get the corresponding
automata for $\LSD[n]$. The same goes with $\MSD[fib]$ and $\LSD[fib]$.
Thus for a number system $\MSD[S]$ if we only define files for
$\MSD[S]$, but then typing ?lsd\_S in a predicate, Walnut automatically
creates automata for $\LSD[S]$ by reversing those of $\MSD[S]$ and vice
versa. However the user should be cautious since there could very well
be number systems for which the difference between $\MSD$ and $\LSD$ is
more than the direction of the arrows in their corresponding automata.

\subsection{Converting .gv files to .jpeg}
The drawings of automata in Walnut are stored in .gv files. Not only can the software Graphviz open the files with this extension,
but it can also convert them to many different file formats. For example, suppose you have a file named automaton.gv. To convert it to automaton.jpeg type the following in the terminal:
\begin{lstlisting}[language=bash]
$dot -Tjpg automaton.gv -o automaton.jpeg 
\end{lstlisting} 
See \href{http://www.graphviz.org/}{Graphviz} to learn how to convert
.gv files to other file types.

\printbibliography[heading=bibintoc]
