---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-003-22-number-systems
section_title: "Number Systems"
section_number: 2.2
pages: 4-6
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.951
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:number systems}
In any course on theory of computation, it is customary to talk about
the representations of the objects an algorithm/Turing machine takes as
inputs. At the core of Walnut are automata taking natural numbers as
inputs, and doing various computations on them, so fixing a
representation for natural numbers is essential. We could limit
ourselves to binary representations. However, there are many
interesting automata accepting representations in number systems other
than the binary one. So we are going to define, in general terms, the
concept of a number system. Walnut allows number systems to be defined
and used (with a few restrictions to the general definition below).

\begin{DEFN}[number systems]\label{def:number systems}
A number system $\mathbf{S}$ is a $3$-tuple $(\Sigma_\mathbf{S},R_\mathbf{S},[]_\mathbf{S})$ of alphabet $\Sigma_\mathbf{S} \supseteq \{0,1\}$, language $R_\mathbf{S} \subset \Sigma_\mathbf{S}^*$ of valid representations containing $0^*$ and at least one of $0^*1$ or $10^*$, and decoding function $[]_\mathbf{S}:R_\mathbf{S}\rightarrow \mathbb{N}$ that assigns integers to every word in $R_\mathbf{S}$ and for which $[]_\mathbf{S}(w)$ is usually written as $[w]_\mathbf{S}$. The decoding function has the following additional properties:
\begin{itemize}
\item $[z]_\mathbf{S}=0$ if and only if $z\in 0^*$
\item $[1]_\mathbf{S}=1$
\item For all $w\in R_\mathbf{S}$, either $zw\in R_\mathbf{S}$ and $[zw]_\mathbf{S}=[w]_S$ for all $z\in 0^*$, or $wz\in R_\mathbf{S}$ and $[wz]_\mathbf{S}=[w]$ for all $z\in 0^*$. The former is called an $\MSD$ number system and the latter is called an $\LSD$ number system\footnote{$\MSD$ and $\LSD$ are short for most-significant-digit-first and least-significant-digit-first, respectively. 
However, it should not be taken literally in this definition, as one
could define $\MSD$ number systems (in the sense defined here), with
no direct correspondence to the notion of most-significant-digit-first
representation.}.  \item For all positive $n\in
\mathbb{N}$, there exists $w\in R_\mathbf{S}$ for which
$[w]_\mathbf{S}=n$ and $w[0]\neq 0$ if $\mathbf{S}$ is $\MSD$ or
$w[|w|-1]\neq 0$ if $\mathbf{S}$ is $\LSD$. The word $w$, if unique, is called the
canonical encoding of $n$ in $\mathbf{S}$, and is sometimes denoted by
$(n)_\mathbf{S}$. We let $(0)_\mathbf{S}=\epsilon$.

\end{itemize}
The addition relation $+_\mathbf{S} \subset R_\mathbf{S}^3$ is defined such that $(x,y,z)\in +_\mathbf{S}$ if and only if $x,y,z$ are of the same length and $[x]_\mathbf{S}=[y]_\mathbf{S}+[z]_\mathbf{S}$. The equality relation $=_\mathbf{S}\subset R_\mathbf{S}^2$ is defined such that $(x,y)\in =_\mathbf{S}$ if and only if $x$ and $y$ are of the same length and $[x]_\mathbf{S}=[y]_\mathbf{S}$.  The less than relation is defined as $<_\mathbf{S} \subset R_\mathbf{S}^2$ for which $(x,y)\in <_\mathbf{S}$ if and only if $x$ and $y$ are of the same length and $[x]_\mathbf{S} < [y]_\mathbf{S}$. We adopt the in-order notation for $+_\mathbf{S}$, $=_\mathbf{S}$, and $<_\mathbf{S}$, i.e., we write $x=y+_\mathbf{S}z$, $x=_\mathbf{S}y$, and $x<_\mathbf{S}y$ as opposed to the more cumbersome $(x,y,z)\in +_\mathbf{S}$, $(x,y)\in =_\mathbf{S}$, and $(x,y) \in <_\mathbf{S}$ respectively. It follows from the definition that for all $n\in \mathbb{N}$, the set of representations of $n$ in $\mathbf{S}$, defined by $\{w:[w]_{\mathbf{S}}=n\}$ is non-empty.
\end{DEFN}

For example, the most-significant-digit binary system, denoted by $\MSD[2]$, is defined by $(\{0,1\},\{0,1\}^*,[]_{\MSD[2]})$ where $$[w]_{\MSD[2]} = \mathlarger{\sum\limits_{i=0}^{|w|-1}} [w[i]]_{\MSD[2]}2^{|w|-i-1},$$ e.g., $[001001]_{\MSD[2]} = 0\cdot 2^5 + 0\cdot 2^4 + 1\cdot 2^3+0\cdot 2^2+0\cdot 2^1+1\cdot 2^0=9$. For $\MSD[2]$, we are very fortunate to have simple automata computing all of its important aspects, namely, valid representations $R_{\MSD[2]}$, the addition relation $+_{\MSD[2]}$, the equality relation $=_{\MSD[2]}$, and the less-than relation $<_{\MSD[2]}$. See Figures \ref{fig:binary_representations},\ref{fig:binary_addition},\ref{fig:binary_equality}, and \ref{fig:binary_less_than} respectively. 
\begin{figure}[H]
\centering
\includegraphics[scale=.5]{binary_representations}
\caption{Automaton computing $R_{\MSD[2]}$}
\label{fig:binary_representations}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[scale=.5]{binary_addition}
\caption{Automaton computing $+_{\MSD[2]}$}
\label{fig:binary_addition}
\end{figure}

\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{binary_equality}
	\caption{Automaton computing $=_{\MSD[2]}$}
	\label{fig:binary_equality}
\end{figure}

\begin{figure}[H]
\centering
\includegraphics[scale=.5]{binary_less_than}
\caption{Automaton computing $<_{\MSD[2]}$}
\label{fig:binary_less_than}
\end{figure}

We can define the least-significant-digit-first binary system, denoted
by $\LSD[2]$, in a similar way. In fact, we can define $\MSD[n]$ and
$\LSD[n]$ for all $n\geq 2$, and for all of them, there are simple
automata computing valid representations, addition, equality, and
less-than relations. In fact we can define the following:

\begin{DEFN}[number systems in Walnut]\label{def:walnut_number_system}
Number systems for which the automata for representations, addition,
equality, and less-than exist, and equality is the same as word
equality, i.e., $x=_\mathbf{S}y$ if and only if $x=y$, are exactly the
type of number systems one can define and use in Walnut. Note that the
alphabet of a number system is restricted to finite subsets of
$\mathbb{Z}$ due to the same restriction on automata in Walnut.
\end{DEFN}
In addition to base-$n$ number systems, Walnut has a
built-in definition for the Fibonacci number system.

The most-significant-digit-first Fibonacci system, denoted by $\MSD[fib]$, is defined by $(\{0,1\},0^*(\epsilon\mid 1)(0\mid 01)^*,[]_{\MSD[fib]})$ where
$$[w]_{\MSD[fib]} = \mathlarger{\sum\limits_{i=0}^{|w|-1}} [w[i]]_{\MSD[fib]}F_{|w|-i-1},$$
where $F_i$ is the $i$'th Fibonacci number given by $F_0=1,F_1=2$, and $F_i=F_{i-1}+F_{i-2}$ for $i\geq 2$. For example, $[001001]_{\MSD[fib]}= 0\cdot F_5 + 0\cdot F_4 + 1\cdot F_3+0\cdot F_2+0\cdot F_1+1\cdot F_0=6$. The set of valid representations is exactly the set of binary words avoiding consecutive $1$s. The avid reader might want to verify that $\MSD[fib]$ is a number system. There are automata computing all major aspects of $\MSD[fib]$. For example, here is the automaton accepting $R_{\MSD[fib]}$\footnote{The automaton accepting $+_{\MSD[fib]}$ has $16$ states, which is too big to be represented here.}:
\begin{figure}[H]
\centering
\includegraphics[scale=.5]{fib_representations}
\caption{Automaton computing $R_{\MSD[fib]}$}
\label{fig:fib_representations}
\end{figure}

In cases, where an automaton's inputs are representations of integers in
some number system, which by far are the most important type of
automata in Walnut, we would like to signify these number systems
instead of the input alphabets. For example, we might write
$\big(Q,q_0,F,\delta,\mathbf{S_1},\mathbf{S_2},\ldots,\mathbf{S_n}\big)$
to mean
$\big(Q,q_0,F,\delta,\Sigma_{\mathbf{S_1}},\Sigma_{\mathbf{S_2}},\ldots,\Sigma_{\mathbf{S_n}}\big)$.
It should be understood that in these cases, if for a word $w$ input
$\pi_j(w)$ is not a valid representation in $\mathbf{S_j}$, it does not
mean that the automaton's behavior is not defined for $w$. This just
means that $w$ is, by default, not going to get accepted. The behaviors
of both automata and automata with output that are taking
representations of numbers in some number systems as inputs are
defined for all words (even those not representing numbers in the given
number systems).
