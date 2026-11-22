---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-005-24-automata-accepting-predicates
section_title: "Automata accepting Predicates"
section_number: 2.4
pages: 7-9
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.996
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:automata accepting predicates}
In Walnut, we are interested in automaton $M$ accepting same-length
representations in number systems
$\mathbf{S_1},\mathbf{S_2},\ldots,\mathbf{S_n}$ of integers
$x_1,x_2,\ldots,x_n$ satisfying some predicate $P$. When this is the
case we say that automaton $M$ accepts the predicate $P$ (or
equivalently$M$ accepts relation $R$ of tuples satisfying $P$). We
already saw a few examples of such automata in Figures
\ref{fig:automaton_accepting_tuples}--\ref{fig:fib_representations}.
From \cite{Buchi:1966}, also see \cite{Schaeffer:thesis}, and as it
will be proved again in Section \ref{sec:decision procedure}, for
predicate $P$ in Presburger arithmetic such an automaton always exists.
Presburger arithmetic is the first-order theory of natural numbers, in
which predicates are consisted of constants (natural numbers),
variables over natural numbers, existential quantifiers, universal
quantifiers, logical operators (conjunction, disjunction, negation,
exclusive disjunction, implication, equivalence), arithmetic operators
(addition, subtraction, multiplication and division by constants), and
comparison operators (equality, less than, greater than, less than or
equal, greater than or equal)\footnote{Presburger arithmetic in its
formal definition recognizes only a minimal subset of constants and
operators: $0$,$1$,$+$,$=$,$<$,$\forall$, but it is not difficult to
show that all the other objects and operators we mentioned, e.g.,
multiplication by constants, does not add to the power of Presburger
arithmetic and can be derived from that minimal set of objects. See
Section \ref{sec:arithmetic and alphabetic constants} for more details.
One thing to note here is that subtraction $a-b$ exists only when there
exists a non-negative number $c$ for which $b+c=a$.}.

You can find the list of all operators in table \ref{tab:operators}.
This list has three operators, namely, reverse\ReverseBlack,indexing
$[]$, and calling $\$$, that are not allowed in Presburger arithmetic.
By indexing we mean indexing into an automatic word, e.g., writing
things like $W[i+j]=W[i+n+j]$; see Section \ref{sec:indexing
expressions} for more details. In
\cite{Shallit:survey},\cite{Charlier&Rampersad&Shallit:enumeration},\cite{Schaeffer:thesis},
and also in Section \ref{sec:indexing to an automatic word} we learn
that extending Presburger arithmetic to include indexing is still
decidable. In Section \ref{sec:calling expressions} we learn about
calling and in Section \ref{sec:calling an automaton} we learn that it
is just a syntactic sugar and does not add to the power of the extended Presburger
arithmetic (one that includes indexing into automatic words). We learn about reverse operation in Section
\ref{sec:complement and reverse}. From here on, by ``predicate'' we mean a
predicate over this extended Presburger arithmetic (extended to include
indexing into automatic words) and until we see the proof in Section
\ref{sec:decision procedure}, we accept the fact that there exist
automata accepting such predicates.

In Section \ref{sec:syntax and semantic} we formally define what constitutes a predicate, but first let us see a few examples:
\begin{itemize}
\itemsep0em
\item $P_1\coloneqq a=4\mathbin{\&}b=5$
\item $P_2\coloneqq a=b+c$
\item $P_3\coloneqq\text{A}x\text{ }\text{E}y\text{ } x=2*y \mid x=2*y+1$
\item $P_4\coloneqq T[i+j]=T[i+n+j]$
\end{itemize}

We adopt the terminology of free variables from mathematical logic,
i.e., a variable that is not bound to a quantifier (quantified). For
example $P_3$ has no free variables, and can be regarded as a constant,
in this case it is always true.

We have seen that, given a predicate $P$, for any ordering
$x_1,x_2,\ldots,x_n$ of free variables and for every assignment of
number systems $\mathbf{S_1},\mathbf{S_2},\ldots,\mathbf{S_n}$ to those
variables, there exists an automaton $M$ accepting such a predicate,
i.e., a tuple of same length words $t=(w_1,w_2,\ldots,w_n)$ is accepted
by $M$ if and only if the substitutions $x_i=[w_i]_{\mathbf{S_i}}$ satisfy
$P$.

For example, consider the predicate $P_1$. The automaton in Figure
\ref{fig:automaton_accepting_tuples} accepts $P_1$. Furthermore there
exists automaton $M$ accepting tuples $(x,y)$ for which $|x|=|y|$ and
substitutions $a=[y]_{\MSD[2]}$, and $b=[x]_{\MSD[2]}$ are satisfying
$P_1$. There also exists an automaton $N$ accepting tuples $(x,y)$ for
which $|x|=|y|$ and substitutions $a=[x]_{\MSD[fib]}$ and
$b=[y]_{\LSD[2]}$ are satisfying $P_1$. By definition, both $M$ and $N$
also accept the predicate $P_1$.

We would like to annotate predicates so that they contain information
on number systems without ambiguity (we will see how shortly). For such
an annotated predicate $P$ and the ordering $x_1,x_2,\ldots,x_n$ on
free variables, there exists a unique minimized automaton accepting the
predicate. We denote this unique automaton by $$(x_1,x_2,\ldots,x_n):
P.$$

\emph{The ordering we fix on variables, in Walnut and throughout this
article, is the lexicographic ordering on the variables' name.}

The following are examples of annotated predicates\footnote{Names for variables, words, and automata in Walnut start with a letter and can contain alphanumerics and underscores. So to distinguish number system annotations in a predicate we use the prefix $?$.}:
\begin{itemize}
\itemsep0em
\item $P'_1\coloneqq\text{?msd\_2 } a=4\mathbin{\&}b=5$
\item $P'_2\coloneqq\text{?msd\_fib } a=b+c$
\end{itemize}
From the annotated predicate $P'_1$ we understand that $a,b,4,5$ should
all be interpreted in $\MSD[2]$ and $=$ should be interpreted as
$=_{\MSD[2]}$. Hence $(a,b): P'_1$ is the automaton accepting $\MSD[2]$
representations of $4$ and $5$ as its first and second inputs
respectively. Also from annotation ?msd\_fib in $P'_2$ it is clear what
to expect from automaton $(a,b,c):P'_2$.

We can annotate a predicate with multiple number systems, e.g., see
Figure \ref{fig:one_and_one}. Here are the rules with which we assign
number systems to constants, variables, and operators in a predicate:

\begin{itemize}
\item If ?S appears inside a pair of parentheses or brackets, then the number system $\mathbf{S}$ is effective from the place it occurs in the predicate to the nearest closing parenthesis or bracket\footnote{Brackets $[]$ only appear in indexing expressions. See Sections \ref{sec:syntax and semantic} and \ref{sec:indexing expressions} for more details.}.
\item If ?S appears outside all parentheses and brackets, then the number system $\mathbf{S}$ is effective from the place it occurs in the predicate to the end of predicate.
\item If none of the rules above applies, the number system is assumed to be $\MSD[2]$ by default.
\item\label{itm:number_system_declarations} It is assumed that the number systems do not contradict each other, i.e., a single variable cannot have two different number systems in one predicate, and all operands of an arithmetic or comparison operator must belong to the same number system. 
\end{itemize}

We saw in Figure \ref{fig:automaton_accepting_tuples}, the \emph{unique} automaton $(a,b):P'_1$. In Figure \ref{fig:fourAndThirteen}, we see the automaton $(a,b):a=4\mathbin{\&}b=13$ (recall that when the number system is not specified it is assumed to be $\MSD[2]$):
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{fourAndThirteen}
	\caption{The automaton accepting $a=4\mathbin{\&}b=13$, does not accept all representations of $4$}
	\label{fig:fourAndThirteen}
\end{figure}

Note how this automaton fails to accept $t=(100,w_2)$ for any $w_2$.
This is obviously due to the fact that $13$ does not have a
representation of length $3$ in $\MSD[2]$. So we stress again that when
we say automaton $M$ accepts predicate $P$, we mean that $M$ accepts
all (tuples of) \emph{equal length representations} of $x_1,\ldots,x_n$
satisfying $P$. Therefore this example conforms to the definition.

Let us see an example of an automaton having multiple number systems. Figure \ref{fig:one_and_one} depicts the automaton \linebreak $(a,b): a=1\mathbin{\&}(\text{?lsd\_2 }b=1)$. 
\begin{figure}[h]
	\centering
	\includegraphics[scale=.5]{one_and_one}
	\caption{Automaton accepting $a=1\mathbin{\&}(\text{?lsd\_2 }b=1)$}
	\label{fig:one_and_one}
\end{figure}
