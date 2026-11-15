---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-002-21-words-and-automata
section_title: "Words and Automata"
section_number: 2.1
pages: 3-4
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 1.0
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:words and automata}
A word $(a_i)_{i\in I}$ for a finite, infinite, or a possibly empty
subset $I$ of natural numbers $\mathbb{N}$, is a sequence of symbols
$a_i$ over a finite set called an alphabet. The set $I$ usually equals
$\mathbb{N}$ or $\mathbb{N}_l=\{k\in \mathbb{N}:k<l \}$ for some $l$.
The set of finite and infinite words over the alphabet $\Sigma$ are
denoted by $\Sigma^*$ and $\Sigma^\omega$, respectively. The empty word
is denoted by $\epsilon$. For the finite word $w = a_0a_1\cdots
a_{l-1}$, the length $|w|$, is defined and equals $l$. We let
$\Sigma^l$ denote the set of all words over $\Sigma$ of length $l$. A
subword (sometimes called ``factor'' in the literature) is a finite and
contiguous subsequence of a word. The subword of $w$ starting at
position $i$ of length $k\geq 0$ is denoted by $w[i..i+k-1]=a_i\cdots
a_{i+k-1}$. Many interesting properties of words can be expressed in
terms of their subwords. For example, the property of having two equal
and adjacent subwords, referred to as a square, is discussed in
numerous papers in the area of combinatorics on words. The product of
two words $x$ and $y$, denoted by $xy$, is the result of concatenating
$x$ by $y$.

There are cases where our words are defined over alphabets consisting
of tuples of symbols, so let us fix our notation regarding these words.
For a word $w$ over an alphabet
$\Sigma_1\times\Sigma_2\ldots\times\Sigma_n$, we let the projection map
$\pi_j(w)$ for $1\leq j\leq n$ denote the word over $\Sigma_j$,
obtained from $w$ by looking at the $j$'th coordinates, i.e., words
$\pi_j(w)$ are uniquely defined by
$$w=\prod\limits_{i=0}^{|w|-1}\big(\pi_1(w)[i],\pi_2(w)[i],\ldots,\pi_n(w)[i]\big).$$
For example, for $w= (0,1)(1,1)(0,0)$ over $\{0,1\}\times \{0,1\}$ we
have $\pi_1(w)=010$ and $\pi_2(w)=110$.

The reader is probably familiar with the notions of deterministic and
nondeterministic finite state automata. In Walnut, an automaton $M$
with $n$ inputs (input tapes), is an $(n+4)$-tuple
$\big(Q,q_0,F,\delta,\Sigma_1,\Sigma_2,\ldots,\Sigma_n\big)$, where $Q$
is the (finite) set of states, $q_0\in Q$ is the initial state,
$F\subseteq Q$ is the set of final states,
$\delta:Q\times\Sigma_1\times\Sigma_2\times\cdots\times\Sigma_n\rightarrow
Q$ is the transition function, and $\Sigma_i$ is the alphabet of the
$i$'th input (tape). The automaton's alphabet is defined to be the
cross product $\Sigma_1\times\Sigma_2\times\cdots\times\Sigma_n$, and
the notions of accepting a word $w$ or a language over this alphabet is
defined as usual. A nondeterministic automaton is defined similarly,
except that the transition function is defined by
$\delta:Q\times\Sigma_1\times\Sigma_2\times\cdots\times\Sigma_n\rightarrow
2^Q$. In Walnut and throughout this article, the $\Sigma_i$ are finite
subsets of integers $\mathbb{Z}$.

Two automata are equal (isomorphic) if their underlying graphs are
isomorphic. Two automata are equivalent if they accept the same
language. There exists a determinization algorithm that converts a
nondeterministic automaton to an equivalent deterministic automaton.
There exists a minimization algorithm that converts an automaton to an
equivalent automaton with the least number of states (which is unique
up to isomorphism). It is known that extending the automata model by
allowing multiple initial states (similar to how there can be multiple
final states) does not add to the model's expressiveness.

Next we extend the notion of accepting languages to relations, since
the latter is more natural in Walnut:

\begin{DEFN}[relations computed by automata]\label{relation}
The relation $R\subset
\Sigma_1^*\times\Sigma_2^*\times\ldots\times\Sigma_n^*$
computed/accepted by $M$ is defined by
$$R=\big\{\big(\pi_1(w),\pi_2(w),\ldots,\pi_n(w)\big):M \text{ accepts
} w\big\}.$$ Since for every word $w$, the words $\pi_i(w)$ are all of
the same length, the relation $R$ accepted by an automaton is consisted
of tuples of the words of the same length, i.e., we have
$$R\subseteq\bigcup\limits_{l\geq
0}\big(\Sigma_1^l\times\Sigma_2^l\times\cdots\times\Sigma_n^l\big)\subset
\Sigma_1^*\times\Sigma_2^*\times\ldots\times\Sigma_n^* .$$ 
\end{DEFN}

For example, the language accepted by the following automaton is $L=(0,0)^*(1,1)(0,0)(0,1)$, whereas the relation accepted is $R=\big\{(w_1,w_2):w_1\in0^*100, w_2\in0^*101,\text{ and } |w_1|=|w_2| \big\}$:
\begin{figure}[H]
\centering
\includegraphics[scale=.5]{automaton_accepting_tuples}
\caption{Automaton accepting tuples of same length representations of $4$ and $5$ in binary}
\label{fig:automaton_accepting_tuples}
\end{figure}
In other words, the automaton accepts tuples $t=(w_1,w_2)\in
\{0,1\}^*\times\{0,1\}^*$ where $w_1$ and $w_2$ are representations of
the \textbf{the same length}, in the most-significant-digit-first
binary system, of natural numbers $4$ and $5$ respectively.  On the
other hand, referring to the words $w$ in $(\{0,1\}\times\{0,1\})^*$ that
are accepted by this automaton is not very descriptive. That is why, in
this article, we prefer the relation (tuple) terminology over the
language (word) terminology.

In almost all depictions of the underlying graphs of automata, such as the
one in Figure \ref{fig:automaton_accepting_tuples}, when a transition
is not specified, it is assumed to be a transition to a dead state. In
Walnut we do not store transitions to the dead state. Adding the dead
state and all implicit transitions to it, is called totalizing an
automaton.

An automaton with output is a tuple
$\big(Q,q_0,O,\delta,\Sigma,\Sigma_1,\Sigma_2,\ldots,\Sigma_n\big)$
where $Q, q_0,\delta, \Sigma_j$ are as before, the set $\Sigma$ is the
output alphabet, and, instead of a set of final states, we have a map
$O:Q\rightarrow \Sigma$. The symbol $O(q)$ is called the output of the
state $q$. An automaton with output can be thought of as an automaton
that reads a word over $\Sigma_1\times\Sigma_2\cdots\times\Sigma_n$ and
outputs whatever is the last state's output. In Walnut, the output
alphabet $\Sigma$ is a finite subset of integers. We can think of
ordinary automata as a special case of automata with output by letting
the set of final states to be $F=\{q:O(q)\neq 0\}$. This is indeed how
ordinary automata are stored in Walnut.

In the next section, we learn how to add more structure to alphabets by
defining number systems. As we saw in the example, the automaton in
Figure \ref{fig:automaton_accepting_tuples} accepts binary
representations of numbers. In a moment we will extend our definition
of automata to
$\big(Q,q_0,F,\delta,\mathbf{S_1},\mathbf{S_2},\ldots,\mathbf{S_n}\big)$,
where the $\mathbf{S_j}$ are number systems and concealed in them are
alphabets $\Sigma_{\mathbf{S_j}}$ among other things.
