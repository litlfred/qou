---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-036-81-defining-automata-in-text-files
section_title: "Defining Automata in Text Files"
section_number: 8.1
pages: 32-33
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:define automata in text files}
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
