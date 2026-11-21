---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-021-45-calling-an-automaton
section_title: "Calling an Automaton"
section_number: 4.5
pages: 17-18
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:calling an automaton}
In Section \ref{sec:calling expressions}, we learned about the syntax
and semantic of calling an automaton. A calling expression is a kind of
syntactic
sugar to save some space when writing long and complicated predicates.
Suppose we already have computed the automaton $(x_1,x_2,\ldots,x_n): P$ and
given it the name $M$. We can refer to $P$ in a predicate $P'$
without writing $P$ all over again, by just writing
$\$M(e_1,e_2,\ldots,e_n)$, where $\$$ symbol is to signify that $M$ is
an automaton, and the $e_i$ are either arithmetic expressions or
predicates with exactly one free variable. In such case, we say,
predicate $P'$ is calling $M$ (or is calling predicate $P$).

To construct automaton for $\$M(e_1,e_2,\ldots,e_n)$, Walnut constructs
the equivalent automaton:
$$\text{E}x_1,x_2,\ldots,x_n\text{ }P \mathbin{\&} (x_1=e'_1)\mathbin{\&} (x_2=e'_2)\mathbin{\&} \cdots\mathbin{\&}(x_n=e'_n)\mathbin{\&} (e_{j_1})\mathbin{\&} (e_{j_2})\mathbin{\&} \ldots\mathbin{\&} (e_{j_k})$$
where $x_1,x_2,\ldots,x_n$ are the free variables in $P$, $k$ is the
number of predicates in $e_1,e_2,\ldots,e_n$, $j_1,j_2,\ldots,j_k$ are
indices of predicates among $e_1,e_2,\ldots,e_n$, and if $e_j$ is an
arithmetic expression, then $e'_j=e_j$, otherwise $e_j$ is a predicate,
and $e'_j$ is the free variable occurring in $e_j$.

The fact that this predicate is equivalent to $\$M(e_1,e_2,\ldots,e_n)$
could be obtained easily using the semantic rule explained in Section
\ref{sec:calling expressions}. Walnut's implementation includes some
considerations to improve efficiency. For example, obviously when $e_j$
is a variable, we do not need to introduce a new variable $x_j$.

\begin{mdframed}[style=MyFrame]
Calling an automaton inside a predicate $P'$ is also more efficient than copying $P$ over and over again in $P'$. This is because Walnut does not need to construct $M$ every time we write $\$M$ in $P'$.
\end{mdframed}

The commands def and eval in Walnut are responsible for constructing the
automaton $M$ from predicate $P$. Unlike eval, the command def saves
the automaton $M$ so it can be called later from other predicates like
$P'$. See Section \ref{sec:def} for more information on def command.

To see an example, let $M$ be the automaton $(a,b):a+b=10$, and let $Q$
be the predicate $\$M(x,y)\mathbin{\&}y=8$. The automaton in Figure
\ref{fig:call_example} accepts $Q$.
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{call_example}
	\caption{Automaton accepting $Q$}
	\label{fig:call_example}
\end{figure}

Please refer to Section \ref{sec:def}, which is devoted to examples of calling automata.  

\begin{mdframed}[style=MyFrame]
When calling an automaton $M$, one has to make sure that the $j$'th argument is in the same number system as $j$'th input in $M$ for all $j$.
\end{mdframed}
