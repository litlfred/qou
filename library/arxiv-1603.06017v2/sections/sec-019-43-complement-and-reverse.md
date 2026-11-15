---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-019-43-complement-and-reverse
section_title: "Complement and Reverse"
section_number: 4.3
pages: 15-16
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.844
latex_coverage_ratio: 0.927
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:complement and reverse}
To obtain $(x_1,\ldots,x_m): \sim (P)$ from $(x_1,\ldots,x_m): P$, one
has to add all transitions to dead state (in Walnut, we call this
totalizing an automaton), and then switching final and non-final
states, but one also has to make sure that the resulting automaton is
intersected with the automaton accepting
$R_{\mathbf{S_1}}\times\cdots\times R_{\mathbf{S_m}}$ where
$\mathbf{S_i}$ is the number system assigned to $x_i$ in (annotated)
predicate $P$. (Recall that $R_{\mathbf{S}}$ is the set of all valid
representations in the number system $\mathbf{S}$. Also recall that to
define and use a number system in Walnut, one has to provide automaton
accepting the set of all representations in that number system,
therefore automaton accepting $R_{\mathbf{S_1}}\times\cdots\times
R_{\mathbf{S_m}}$ could be constructed easily using cross product
explained in Section \ref{sec:cross product}.)

Take a look at automaton $(a): \text{?msd\_fib }a=1$ depicted in Figure \ref{fig:orig} that accept words representing $1$ in $\MSD[fib]$.
\begin{figure}[h]
	\centering
	\includegraphics[scale=.5]{orig}
	\caption{Number 1 in Fibonacci}
	\label{fig:orig}
\end{figure}

Now to obtain $(a):\sim(\text{?msd\_fib }a=1)$, we first add the dead state and all the transitions to it:
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{orig_dead_state}
	\caption{Totalized automaton}
	\label{fig:orig_dead_state}
\end{figure}
Switching final and non-final states we obtain an automaton accepting $\{0,1\}^*\setminus 0^*1$:
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{orig_switch_final}
	\caption{Switching final and non-final states}
	\label{fig:orig_switch_final}
\end{figure}
But then this automaton accepts words that have consecutive $1$'s which
are not acceptable Fibonacci representations. So to get the final
answer we have to intersect this automaton with the one depicted in
Figure \ref{fig:fib_representations}. The result is depicted in
\ref{fig:orig_complement}.
\begin{figure}[h]
	\centering
	\includegraphics[scale=.5]{orig_complement}
	\caption{Automata accepting all numbers in Fibonacci except $1$}
	\label{fig:orig_complement}
\end{figure}

The reverse operator is not a logical operator per se, but we include
it because it is useful when working with automata. The operand of the
reverse operator is an automaton \footnote{Unlike the reverse operator,
operands for logical operators are predicates. The reader however
understands the very thin and superficial distinction between automata
and predicates in this article.}. The result is an automaton with all
its transitions reversed.
