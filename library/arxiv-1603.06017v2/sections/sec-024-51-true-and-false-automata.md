---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-024-51-true-and-false-automata
section_title: "True and False Automata"
section_number: 5.1
pages: 19-19
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.935
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:true and false}
In Section \ref{sec:automata accepting predicates} we saw an example of a predicate with no free variables: 
$$\text{A}x\text{ }\text{E}y\text{ } x=2*y \mid x=2*y+1$$
This predicate evaluates to true (it is a tautology). Here is an example of a predicate with no free variable that evaluates to false (contradiction):
$$\text{E}x\text{ } x>x+1$$
Walnut assigns a special automaton called true (false) automaton to predicates with no free variable that evaluate to true (false). However there could be predicates with free variables that are converted to true or false automata. See the following conventions implemented in Walnut:
\begin{itemize}
\item Conjunction (disjunction) of true automaton with automaton $M$ yields $M$ (true automaton, respectively).
\item Conjunction (disjunction) of false automaton with automaton $M$ yields false automaton ($M$, respectively).
\item Negation of true automaton is false automaton and vice versa.
\item Conventions for other logical operators follow from the above.
\end{itemize}
These conventions are reflecting the following facts from mathematical logic (for a predicate $P$):
\begin{itemize}
\item $P\mathbin{\&}\text{true}$ and $P\mid \text{true}$ are equivalent to $P$ and true respectively.
\item $P\mathbin{\&}\text{false}$ and $P\mid \text{false}$ are equivalent to false and $P$ respectively.
\item $\sim\text{true}=\text{false}$ and $\sim\text{false}=\text{true}$.
\end{itemize}
As an example, the automaton $(y): (\text{A}x\text{ } x<x+1)
\mathbin{\&} y=2$ is exactly the same as automaton $(y): y=2$. As
another example, the automaton $(y):(\text{E}x\text{ } x<0)
\mathbin{\&} y=2$ is the false automaton. As in our last example, note
that $\sim(\text{E}x\text{ } x<0)$ is the true automaton.

Figures~\ref{fig:true} and \ref{fig:false} show the special way Walnut
represents true and false automata.
\begin{figure}[h]
\centering
\begin{minipage}[t]{.5\textwidth}
\centering
\includegraphics[scale=.5]{true}
\caption{True automaton}
\label{fig:true}
\end{minipage}
\begin{minipage}[t]{.5\textwidth}
\centering
\includegraphics[scale=.5]{false}
\caption{False automaton}
\label{fig:false}
\end{minipage}
\end{figure}
