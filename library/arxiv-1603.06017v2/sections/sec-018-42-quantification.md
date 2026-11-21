---
doc_id: arxiv-1603.06017v2
doc_title: "Automatic Theorem Proving in Walnut"
section_id: sec-018-42-quantification
section_title: "Quantification"
section_number: 4.2
pages: 14-15
source_pdf: 1603.06017v2.pdf
source_sha256: 3ff091e40573a5dd
toc_source: outline
text_source: latex
latex_prose_ratio: 0.944
latex_coverage_ratio: 0.993
doc_brief: "Automatic Theorem Proving in Walnut — 42 sections: Front matter; Introduction; Basics"
---
\label{sec:quantification}
In this section we learn how to construct an automaton
$(x_1,\ldots,x_{i-1},x_{i+1},\ldots,x_m): \text{E}x_{i}\text{ }P$ from
automaton $(x_1,\ldots,x_m): P$. Let
$M\big(Q,q_0,F,\delta,\mathbf{S_1},\ldots,\mathbf{S_m}\big)$ be the
automaton $(x_1,\ldots,x_m):P$ and let $P'$ be the predicate
$\text{E}x_{i}\text{ }P$. We first construct the nondeterministic
automaton $E(M,i)$
$$\big(Q,q_0,F,\delta',\mathbf{S_1},\ldots,\mathbf{S_{i-1}},\mathbf{S_{i+1}},\ldots,\mathbf{S_m}\big)$$
from $M$ by eliminating the $i$'th input (coordinate) on all
transitions, i.e., letting
$$\delta'\big(q,(\alpha_1,\ldots,\alpha_{i-1},\alpha_{i+1},\ldots,\alpha_m)\big)
=
\big\{\delta(q,(\alpha_1,\ldots,\alpha_{i-1},\alpha_i,\alpha_{i+1},\ldots,\alpha_m)):\text{
for all } \alpha_i \in \Sigma_{S_{i}} \big\}.$$

For example, letting $M$ be the automaton $(a,b):a=1\mathbin{\&}b=2$ depicted in Figure \ref{fig:minimized}, the automaton $E(M,2)$ is depicted as follows: 
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{quantified}
	\caption{Non-deterministic automaton $E(M,2)$}
	\label{fig:quantified}
\end{figure}

By the definition of transition function of $E(M,i)$, i.e., $\delta'$,
it is easy to see that if $M$ accepts
\allowbreak$(w_1,\ldots,w_{i-1},w_i,w_{i+1},\ldots,w_m)$, then $E(M,i)$
accepts $$(w_1,\ldots,w_{i-1},w_{i+1},\ldots,w_m).$$ However, there
might be $t=(w_1,\ldots,w_{i-1},w_{i+1},\ldots,w_m)$ where the $|w_j|$
are equal for all $j\neq i$ and substitutions $x_j =
[w_j]_{\mathbf{S_j}}$ for all $j\neq i$, satisfies $P'$ but $E(M,i)$
does not accept $t$. In other words, there are cases where $E(M,i)$
does not accept $P'$.

In our example $M$ accepts $(0^n1,0^{n-1}10)$ for all $n\geq 1$, and as
it is clear $E(M,2)$ accepts $(0^n1)$ for all $n\geq 1$. However
$E(M,2)$ does not accept $(1)$, whereas $(1)$ should be accepted by any
automaton accepting $\text{E}b\text{ }(a=1\mathbin{\&}b=2)$.

Therefore, we have to do more work on $E(M,i)$, to get to an automaton
for $P'$. However as we will see in Lemma \ref{lemma:leading zeros
problem}, the automaton $E(M,i)$ might only miss an insignificant
portion of accepted tuples of an automaton accepting $P'$. These
insignificant tuples missed by $E(M,i)$ are those with leading or
trailing zeros. The good news is that with a little bit of technical
work, it is possible to revive even these insignificant tuples.

\begin{LMA}\label{lemma:leading zeros problem} 
Let $M$,$P$,$P'$, and $i$ be as in the discussion above, and suppose
$t=(w_1,\ldots,w_{i-1},w_{i+1},\ldots,w_m)$ is some tuple of same
length words. If $P'$ is satisfied with substitutions
$x_j=[w_j]_{\mathbf{S_j}}$ for $j\neq i$, then there exists a constant
$k\geq 0$ and\linebreak
$t_k=(w_{k,1},\ldots,w_{k,i-1},w_{k,i+1},\ldots,w_{k,m})$ such that for
all $j\neq i$ we have $w_{k,j}=0^kw_j$ or $w_{k,j}=w_j0^k$ depending on
whether $\mathbf{S_j}$ is $\MSD$ or $\LSD$, and $t_k$ is accepted by
$E(M,i)$. It is also the case that whenever $t_k$ for any $k\geq 0$,
with the appropriate substitutions, is satisfying $P'$, then $t$ is
also satisfying $P'$.
\end{LMA}

\begin{proof}
Substitutions $x_j=[w_j]_{\mathbf{S_j}}$ for $j\neq i$ satisfying
predicate $P'\coloneqq\text{E}x_i\text{ }P$ means that there exists a
natural number $v$, such that the substitutions above together with
$x_i=v$ is satisfying the predicate $P$.  By definition of number
systems, there exists a word $w_i$ such that $v=[w_i]_{\mathbf{S_i}}$.
Also by definition of number systems for any integer $y$ and word $w$,
if we have $y=[w]_{\mathbf{S}}$, then either $y=[0^kw]_{\mathbf{S}}$
for all $k\geq 0$ or $y=[w0^k]_{\mathbf{S}}$ for all $k\geq 0$
depending on whether $\mathbf{S}$ is $\MSD$ or $\LSD$.  Therefore there
exists an integer $k$ such that $w_{k,i}$ is either $0^kw_i$ or
$w_i0^k$ depending on whether $\mathbf{S_j}$ is $\MSD$ or $\LSD$ and
$v=[w_{k,i}]_{\mathbf{S_i}}$ and $|w_{k,i}|=|w_j|+k$ for all $j\neq i$.
Therefore $(w_{k,1},\ldots,w_{k,i-1},w_{k,i},w_{k,i+1},\ldots,w_{k,m})$
is accepted by $M$ where for all $j$ we have $w_{k,j}=0^kw_j$ or
$w_{k,j}=w_j0^k$ depending on whether $\mathbf{S_j}$ is $\MSD$ or
$\LSD$. Now by definition of $E(M,i)$, we know that
$t_k=(w_{k,1},\ldots,w_{k,i-1},w_{k,i+1},\ldots,w_{k,m})$ is accepted
by $E(M,i)$. This completes the first part of the lemma.

The second part follows very easily from the same properties of number
systems mentioned in the proof of the first part of the lemma.
\end{proof}

Based on Lemma \ref{lemma:leading zeros problem}, to get
$(x_1,\ldots,x_{i-1},x_{i+1},\ldots,x_m): \text{E}x_{i}\text{ }P$ we
just have to construct an automaton from $E(M,i)$ such that whenever
$t_k$ for any $k\geq 0$ is accepted, $t$ is also accepted. For the case
where all $\mathbf{S_j}$ for $j\neq i$ are either all $\MSD$ or all
$\LSD$, we can come up with an easy algorithm to revive tuples $t$ from
$t_k$. In case of all $\MSD$, let $I$ be the set of all states in
$E(M,i)$ reachable from the initial state by reading $(0,\ldots,0)^*$,
or in case of all $\LSD$, let $F'$ be the set of all states reaching to
a final state by reading $(0,\ldots,0)^*$.  We can compute $I$ or $F'$
using breadth-first search. In the case of $\MSD$ the nondeterministic
automaton\footnote{This is an automaton with multiple initial states.
One can show that for every nondeterministic automaton with multiple
initial states, there is an equivalent automaton with only one initial
state.}
 $$(Q,I,F,\delta',\mathbf{S_1},\ldots,\mathbf{S_{i-1}},\mathbf{S_{i+1}},\ldots,\mathbf{S_n})$$
and in the case of $\LSD$ the nondeterministic automaton
$$(Q,q_0,F',\delta',\mathbf{S_1},\ldots,\mathbf{S_{i-1}},\mathbf{S_{i+1}},\ldots,\mathbf{S_n})$$
is equivalent to $(x_1,\ldots,x_{i-1},x_{i+1},\ldots,x_m):
\text{E}x_{i}\text{ }P$. Determinizing and minimizing this automaton
gives us $(x_1,\ldots,x_{i-1},x_{i+1},\ldots,x_m): \text{E}x_{i}\text{
}P$.

In Figure \ref{fig:quantified}, the variable $a$ is over $\MSD[2]$. So
the set $I$ is $\{0,1\}$, therefore the following nondeterministic
automaton accepts $\text{E}b\text{ } a=1\mathbin{\&}b=2$:

\begin{figure}[H]
\centering
\includegraphics[scale=.5]{quantified2}
\caption{Non-deterministic automaton accepting $\text{E}b\text{ } a=1\mathbin{\&}b=2$}
\label{fig:quantified2}
\end{figure}

Now determinizing and minimizing this automaton gives us $(a):\text{E}b\text{ } a=1\mathbin{\&}b=2$:
\begin{figure}[H]
	\centering
	\includegraphics[scale=.5]{quantified3}
	\caption{$(a):\text{E}b\text{ } a=1\mathbin{\&}b=2$}
	\label{fig:quantified3}
\end{figure}

\begin{mdframed}[style=MyFrame]
Currently if for $(x_1,\ldots,x_n): P$ it is not the case that for all
$j\neq i$ number systems $\mathbf{S_j}$ are all $\MSD$ or all $\LSD$,
then Walnut only constructs $E(M,i)$ for $\text{E}x_{i}\text{ }P$,
which is not theoretically accurate. So the user has to be very
cautious when quantifying predicates over mixed $\MSD$ and $\LSD$
number systems, or in cases where the quantified automaton is
non-arithmetic. For a definition of the latter see Section
\ref{sec:non-arithmetic automata}.
\end{mdframed}

To obtain an automaton for $Ax_i P$, note its equivalence to ${\sim
(\text{E}x_i\text{ }{\sim (P)})}$, where $\sim$ is the logical
complement (negation). See the next section to learn about the
complement operator.
