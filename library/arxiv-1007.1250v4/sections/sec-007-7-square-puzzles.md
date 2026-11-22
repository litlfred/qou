---
doc_id: arxiv-1007.1250v4
doc_title: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES"
section_id: sec-007-7-square-puzzles
section_title: "Square Puzzles"
section_number: 7
pages: 91-105
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.971
doc_brief: "NONABELIAN MULTIPLICATIVE INTEGRATION ON SURFACES — We construct a 2-dimensional twisted nonabelian multiplicative integral."
---
\label{sec:puzzles}
\numberwithin{equation}{subsection}

In this section we work with  the pointed polyhedron
$(X, x_0) := (\mbf{I}^2, v_0)$. Let us fix some Lie quasi crossed module
with additive feedback 
\[ \mbf{C} / \mbf{I}^2 = (G, H, \Psi, \Phi_0, \Phi_{X}) \]
over $(\mbf{I}^2, v_0)$, and a piecewise smooth connection-curvature pair 
$(\alpha, \beta)$ in $\mbf{C} / \mbf{I}^2$.
See Definitions \ref{dfn:6} and \ref{dfn:19}.
We will show that under certain homotopical restrictions,
moving little square kites around inside $\mbf{I}^2$
doesn't alter the multiplicative surface integral. 



\subsection{The Free Monoid with Involution} \label{subec:freemon}
It will be helpful for us to have some terminology for abstract words and
cancellation. 

Recall that a {\em monoid} is a unital semigroup. Suppose $M, N$ are monoids.
By homomorphism of monoids we mean a function
$\phi : M \to N$ that preserves the multiplications and the units. 

Let $S$ be some set, possibly infinite, whose elements we consider as symbols.
A {\em word} in $S$ is by definition a finite sequence $w = (s_1, \ldots, s_n)$
of elements of $S$. Thus $w$ is a function
\[ w : \{ 1, \ldots, n \} \to S . \] 
The natural number $n$ is the {\em length} of $w$.
We denote the set of all these words by 
$\opn{Wrd}(S)$. This is a monoid under the operation of
concatenation, which we denote by $*$, and the unit is the empty word 
$1 := ()$. We consider $S$ as a subset of $\opn{Wrd}(S)$, namely the words of
length $1$.
In fact $\opn{Wrd}(S)$ a free monoid: any function $S \to M$, where $M$
is a monoid, extends uniquely to a homomorphism of monoids
$\opn{Wrd}(S) \to M$. 

Next suppose $\bsym{s} = (s_1, \ldots, s_n)$ is a sequence of distinct elements
of $S$. We refer to such a sequence of distinct elements as an {\em alphabet}.
We denote by 
\[ \opn{Wrd}(\bsym{s}) = \opn{Wrd}(s_1, \ldots, s_n) \]
the subset of $\opn{Wrd}(S)$ consisting of the words in the alphabet $\bsym{s}$
only. More precisely, a word $w$ of length $m$ belongs to $\opn{Wrd}(\bsym{s})$
if and only if the function
$w : \{ 1, \ldots, m \} \to S$ factors as
$w = \bsym{s} \circ \til{w}$, for a function (necessarily unique)
\[ \til{w} : \{ 1, \ldots, m \} \to \{ 1, \ldots, n \} . \]
The elements of $\opn{Wrd}(\bsym{s})$ are denoted by $w(\bsym{s})$, and are
called {\em words in $\bsym{s}$}. Clearly $\opn{Wrd}(\bsym{s})$ is a sub-monoid
of $\opn{Wrd}(S)$; and
it is also a free monoid, on the $n$ symbols $s_1, \ldots, s_n$.
Given a homomorphism of monoids 
$\phi :  \opn{Wrd}(S) \to M$, and a word $w(\bsym{s}) \in \opn{Wrd}(\bsym{s})$, 
we shall use the following ``substitution notation'':
\[ w(\bsym{\gamma}) = w(\gamma_1, \ldots, \gamma_n) := \phi(w(\bsym{s})) \in M 
, \]
where $\bsym{\gamma}$ is the sequence
\[ \bsym{\gamma} = (\gamma_1, \ldots, \gamma_n) := 
\bigl( \phi(s_1), \ldots, \phi(s_n) \bigr) \]
in $M$. 

Let $M$ be a monoid. By an anti-automorphism of $M$ we mean a bijection 
$\psi : M \to  M$ that reverses the order of multiplication, and preserves the
unit. An {\em involution} of the monoid $M$ is an anti-automorphism $\psi$ such
that $\psi \circ \psi = \opn{id}$. 
The pair $(M, \psi)$ is then called a {\em monoid with involution}.

Let $S$ be a set. Let $S^{-1}$ be a new copy of $S$; i.e.\ $S^{-1}$
is a set disjoint from $S$, equipped with a bijection
$\psi_S : S \iso S^{-1}$. This bijection extends to an involution 
$\psi_S$ of the set $S \cup S^{-1}$. 
We define 
\[ \opn{Wrd}^{\pm 1}(S) := \opn{Wrd}(S \cup S^{-1}) . \]
This monoid has a canonical involution $\psi_S$, extending the involution on
the set $S \cup S^{-1}$. We sometimes write 
$w^{-1} := \psi_S(w)$ for a word $w \in \opn{Wrd}^{\pm 1}(S)$.
Note however that the product $w * w^{-1}$ is not $1$
(unless $w = 1$, the empty word). Indeed, the length of 
$w * w^{-1}$ is twice the length of $w$ (as words in $S \cup S^{-1}$).

The monoid $\opn{Wrd}^{\pm 1}(S)$ is a {\em free monoid with involution}. 
Here is what this means: let $(M, \psi)$ be any monoid with involution, and let
$f : S \to M$ be a function. Then there is a unique homomorphism of monoids
$\phi : \opn{Wrd}^{\pm 1}(S) \to M$ that commutes with the involutions and
extends
$f$. 

Given a sequence $\bsym{s} = (s_1, \ldots, s_n)$ of distinct elements of $S$,
we write 
\[ \begin{aligned}
&\opn{Wrd}^{\pm 1}(\bsym{s}) = \opn{Wrd}^{\pm 1}(s_1, \ldots, s_n) \\
& \qquad := \opn{Wrd}(s_1, \ldots, s_n, s_1^{-1}, \ldots, s_n^{-1}) \subset 
\opn{Wrd}^{\pm 1}(S) .
\end{aligned} \]
This is also a free monoid with involution.

Suppose the words 
$w$ and $w'$ in $\opn{Wrd}^{\pm 1}(S)$ satisfy this condition: 
\[ w = v_1 * u * v_2 \quad \text{and} \quad w' = v_1  * v_2 , \]
where $v_1$ and $v_2$ are some elements of $\opn{Wrd}^{\pm 1}(S)$, and
$u$ is either $s * s^{-1}$ or $s^{-1} * s$ for some $s \in S$. 
Then we say that $w'$ is {\em gotten from $w$ by cancellation}.
The equivalence relation generated by this condition is called {\em cancellation
equivalence}, and is denoted by $\sim_{\mrm{can}}$. Thus words 
$w, w' \in \opn{Wrd}(S)$ satisfy $w \sim_{\mrm{can}} w'$ 
if and only if there are words
\[ w = w_0, w_1, \ldots, w_r = w' \]
such that for each $i$ either $w_{i+1}$ is gotten from $w_i$
by cancellation, or vice versa. Note that the set of equivalence classes
$\opn{Wrd}^{\pm 1}(S) / \sim_{\mrm{can}}$ is a free group, with basis the image
of $S$. 

When we talk about $\opn{Wrd}^{\pm 1}(s_1, \ldots, s_n)$, we always
mean implicitly that it is the free monoid with involution on some sequence
$(s_1, \ldots, s_n)$ of distinct elements in 
some set $S$ (possibly $S = \{ s_1, \ldots, s_n \}$). 

If $\Gamma$ is a group, then by default we put on it the involution
$\psi(\gamma) := \gamma^{-1}$. In this way $\Gamma$ becomes a monoid with
involution. 

Let $(M, \psi)$ be a monoid with involution. Given an element
$m \in M$, define the operation
$\opn{Ad}(m) : M \to M$ by
\begin{equation} \label{eqn:249}
\opn{Ad}(m)(m') := m * m' * \psi(m) .
\end{equation}
Warning: $\opn{Ad}(m)$ is not a homomorphism of monoids (unless $M$ is a
group). 

Let $Y$ be a finite graph (i.e.\ a finite $1$-dimensional cellular complex),
with base point $y_0$ that's a vertex, and $n$ edges $\tau_1, \ldots, \tau_n$.
Choose an orientation on each $\tau_i$ (i.e.\ a homeomorphism 
$\mbf{I}^{1} \cong \tau_i$). 
The reversely oriented cell is denoted by $\tau_i^{-1}$. 
Take an alphabet $\bsym{s} = (s_1, \ldots, s_n)$.
Any word $w(\bsym{s}) \in \opn{Wrd}^{\pm 1}(\bsym{s})$ gives rise, by the
evaluation
$s_i \mapsto \tau_i$ and $s_i^{-1} \mapsto \tau_i^{-1}$, a sequence of oriented
cells $w(\tau_1, \ldots, \tau_n)$, which might or might
not be a path in $Y$. 

\begin{lem} \label{lem:15}
In the situation described above, suppose $w(\tau_1, \ldots, \tau_n)$ is a
closed path in $Y$ based at $y_0$, such that 
$[w(\tau_1, \ldots, \tau_n)] = 1$ in the fundamental group
$\bsym{\pi}_1(Y, y_0)$. Then $w(\bsym{s}) \sim_{\mrm{can}} 1$ 
in $\opn{Wrd}^{\pm 1}(\bsym{s})$. 
\end{lem}

\begin{proof}
We learned this proof from Y. Glasner.
First consider a pointed tree $(\til{Y}, \til{y}_0)$, and a sequence 
$(\til{\rho}_1, \ldots, \til{\rho}_l)$ of edges in $\til{Y}$ which is a path
starting at $\til{y}_0$.
If this path is closed, then it is cancellation equivalent to
a point. This can be seen by induction on $l$. 
Indeed, let $i$ be an index such that the endpoint of the path
$(\til{\rho}_1, \ldots, \til{\rho}_i)$ is at maximal distance from the
base vertex $\til{y}_0$. Then we must have
$\til{\rho}_{i+1} = \til{\rho}_i^{-1}$; so we can cancel these two edges,
yielding a shorter closed path. 

Getting back to our problem, write
$(\rho_1, \ldots, \rho_l) := [w(\tau_1, \ldots, \tau_n)]$, where 
$\rho_i \in \{ \tau_1^{\pm 1}, \ldots, \tau_n^{\pm 1} \}$.
Then $w(\bsym{s}) \sim_{\mrm{can}} 1$ if and only if 
$(\rho_1, \ldots, \rho_l)$ is cancellation equivalent to a point. 
Let $p : (\til{Y}, \til{y}_0) \to (Y, y_o)$ be the universal covering map; so 
$(\til{Y}, \til{y}_0)$ is a pointed tree.
Since the closed path 
$(\rho_1, \ldots, \rho_l)$ is trivial in the fundamental group of $Y$, it lifts
to a closed path $(\til{\rho}_1, \ldots, \til{\rho}_l)$
based at $\til{y}_0$ in the tree $\til{Y}$. By the first paragraph the 
path $(\til{\rho}_1, \ldots, \til{\rho}_l)$ is cancellation equivalent to a
point. Hence so is $(\rho_1, \ldots, \rho_l)$.
\end{proof}



\subsection{Generating Sequences}
Recall that for $k \geq 0$, the $k$-th binary subdivision 
$\opn{sd}^k \mbf{I}^2$ of $\mbf{I}^2$ is the cellular decomposition of 
$\mbf{I}^2$ into $4^k$ squares, each of side $(\smfrac{1}{2})^k$. 
The $1$-skeleton of $\opn{sd}^k \mbf{I}^2$ is the topological space
$\opn{sk}_1 \opn{sd}^k \mbf{I}^2$, and its fundamental group, based at $v_0$, is
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.
For a closed string $\sigma$ based at $v_0$ and patterned on 
$\opn{sd}^k \mbf{I}^2$ we denote by 
$[\sigma]$ the corresponding element of 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.

\begin{dfn} \label{dfn:33}
Let $k \in \N$, and let
\[ \bsym{\rho}^{\natural} = \bigl( (\sigma^{\natural}_1, \tau^{\natural}_1),
\ldots, (\sigma^{\natural}_{4^k}, \tau^{\natural}_{4^k}) \bigr) \]
be a sequence of kites in $(\mbf{I}^2, v_0)$, all patterned on 
$\opn{sd}^k \mbf{I}^2$.
For any $i$ let
\[ a^{\natural}_i := [\partial (\sigma^{\natural}_i, \tau^{\natural}_i)]
\in \bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2) . \]
\begin{enumerate}
\item If the sequence $(a^{\natural}_1, \ldots, a^{\natural}_{4^k})$
is a basis of the group 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$,
then we say that $\bsym{\rho}^{\natural}$ is a {\em generating sequence for
$\opn{sd}^k \mbf{I}^2$}.

\item Let $(\sigma, \tau)$ be a kite in $(\mbf{I}^2, v_0)$ patterned on 
$\opn{sd}^k \mbf{I}^2$. If $\tau = \tau^{\natural}_i$ for some $i$ then 
we say that $(\sigma, \tau)$ is {\em aligned with $\bsym{\rho}^{\natural}$}.
\end{enumerate}
\end{dfn}

The $k$-th binary tessellation $\opn{tes}^k \mbf{I}^2$ 
(see Definition \ref{dfn:14}) is an example of a 
generating sequence for $\opn{sd}^k \mbf{I}^2$.

\begin{lem} \label{lem:17}
Let $\bsym{\rho}^{\natural}$ be a generating sequence for 
$\opn{sd}^k \mbf{I}^2$, and let 
$a^{\natural}_i = \lb [\partial (\sigma^{\natural}_i, \tau^{\natural}_i)]$
as in the definition above.
Let 
$w(\bsym{s}) \in \opn{Wrd}^{\pm 1}(\bsym{s}) = \opn{Wrd}^{\pm 1}(s_1, \ldots,
s_{4^k})$ 
be a word such that 
\[ w(a^{\natural}_1, \ldots, a^{\natural}_{4^k}) = 1  \]
in the group $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.
Then 
\[ w(\bsym{s}) \sim_{\mrm{can}} 1 \]
in $\opn{Wrd}^{\pm 1}(\bsym{s})$.
\end{lem}

\begin{proof}
This is because the sequence 
$(a^{\natural}_1, \ldots, a^{\natural}_{4^k})$
is a basis of the free group \linebreak
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.
\end{proof}

\begin{lem} \label{lem:11}
Let $\sigma_1, \sigma_2$ be linear strings in $\mbf{I}^2$, and let
$\tau : \mbf{I}^2 \to \mbf{I}^2$ be a linear map, all patterned on 
$\opn{sd}^k \mbf{I}^2$ for some $k \geq 0$. 
\begin{enumerate}
\item Suppose $\sigma_1, \sigma_2$ are closed strings based at $v_0$, and
$[\sigma_1] = [\sigma_2]$ in \lb 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$. 
Then 
\[ \opn{MI} (\alpha \vert \sigma_1) = \opn{MI} (\alpha \vert \sigma_1) \]
in $G$.

\item Suppose that $\sigma_i(v_0) = v_0$ and 
$\sigma_i(v_1) = \tau(v_0)$ for $i = 1, 2$; so that 
$(\sigma_i, \tau)$ are kites in $\mbf{I}^2$ and 
$\sigma_2 * \sigma_1^{-1}$ is a closed string based at $v_0$. 
If 
$[\sigma_2 * \sigma_1^{-1}] = 1$ in 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$, then 
\[ \opn{MI} (\alpha, \beta \vert \sigma_1, \tau) = 
\opn{MI} (\alpha, \beta \vert \sigma_2, \tau) \]
in $H$. 
\end{enumerate}
\end{lem}

\begin{proof}
(1) Take 
$n := 2^{k+1} \cdot (2^k + 1)$, the number of $1$-cells in 
$\opn{sd}^k \mbf{I}^2$. Let us denote these $1$-cells by
$\tau_1, \ldots, \tau_n$, and let's choose an orientation for these cells, as
in Lemma \ref{lem:15}. There are unique words 
\[ w_1(\bsym{s}), w_2(\bsym{s}) \in \opn{Wrd}^{\pm 1}(\bsym{s}) = 
\opn{Wrd}^{\pm 1}(s_1, \ldots, s_n) \]
such that 
$w_i(\tau_1, \ldots, \tau_n) = \sigma_i$ as strings. 
Lemma \ref{lem:15} implies that \lb
$w_1(\bsym{s}) \sim_{\tup{can}} w_2(\bsym{s})$ in 
$\opn{Wrd}^{\pm 1}(\bsym{s})$. Now Definition \ref{dfn:10} and Proposition
\ref{prop:1}
tell us that 
\[ \opn{MI} \bigl( \alpha \vert w_1(\tau_1, \ldots, \tau_n) \bigr) = 
\opn{MI} \bigl( \alpha \vert w_2(\tau_1, \ldots, \tau_n) \bigr) . \]

\medskip \noindent
(2) Let
$g_i := \opn{MI} (\alpha \vert \sigma_i) \in G$.
By part (1) we know that 
\[ g_2 \cdot g_1^{-1} = \opn{MI} (\alpha \vert \sigma_2) \cdot
\opn{MI} (\alpha \vert \sigma_1^{-1}) = 
\opn{MI} (\alpha \vert \sigma_2 * \sigma_1^{-1}) = 1 ; \]
so that $g_1 = g_2$. Let $g := g_1 = g_2$.

Let $\sigma_0$ denote the empty string. So
$\sigma_i * \sigma_0 = \sigma_i$ for $i = 1, 2$.
Now according to Theorem \ref{thm:14} we have 
\[ \opn{MI}(\alpha, \beta \vert \sigma_i, \tau) =
\Psi(g) \bigl( \opn{MI}^g (\alpha, \beta \vert \sigma_0, \tau) \bigr) . \]
for $i = 1, 2$. But the right hand side is independent of $i$.
\end{proof}

\begin{lem} \label{lem:12}
Let $\bsym{\rho}^{\natural}$ be a generating sequence for 
$\opn{sd}^k \mbf{I}^2$, let 
$a^{\natural}_i$ be as in definition \tup{\ref{dfn:33}}, and let
\[ h^{\natural}_i := \opn{MI} (\alpha, \beta \vert 
\sigma^{\natural}_i, \tau^{\natural}_i) \in H . \]
Suppose $(\sigma, \tau)$ is a kite in $(\mbf{I}^2, v_0)$ patterned on
$\opn{sd}^k \mbf{I}^2$ and aligned with $\bsym{\rho}^{\natural}$. Then there
is a word 
\[ w(\bsym{s}) \in \opn{Wrd}^{\pm 1}(\bsym{s}) = 
\opn{Wrd}^{\pm 1}(s_1, \ldots, s_{4^k}) \]
such that
\[ [\partial (\sigma, \tau)] = 
w(a^{\natural}_1, \ldots, a^{\natural}_{4^k} ) \]
in $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$, and 
\[ \opn{MI} (\alpha, \beta \vert \sigma, \tau) = 
w(h^{\natural}_1, \ldots, h^{\natural}_{4^k}) \]
in $H$. 
\end{lem}

\begin{proof}
Let $i$ be an index such that 
$\tau = \tau^{\natural}_i$. Then 
$\sigma *  (\sigma^{\natural}_i)^{-1}$ is a closed string based at $v_0$ and
patterned on $\opn{sd}^k \mbf{I}^2$. 
(See Figure \ref{fig:33} for an illustration where $k = 1$
$\bsym{\rho}^{\natural} = \opn{tes}^1 \mbf{I}^2$.)
There is a  word
$u(\bsym{s}) \in \opn{Wrd}^{\pm 1}(\bsym{s})$ such that
\[ [ \sigma *  (\sigma^{\natural}_i)^{-1} ] = 
u(a^{\natural}_1, \ldots, a^{\natural}_{4^k}) \]
in the group $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.

\begin{figure}
\includegraphics[scale=0.36]{fig33.jpg}
\caption{A kite $(\sigma, \tau)$ patterned on 
$\opn{sd}^1 \mbf{I}^2$ and aligned with $\opn{tes}^1 \mbf{I}^2$, the
corresponding kite $(\sigma^{1}_i, \tau^{1}_i)$, and the closed string 
$\sigma * (\sigma^{1}_i)^{-1}$. Here $i = 2$.} 
\label{fig:33}
\end{figure}

We can also consider the monoid $M$ of finite sequences of closed strings
patterned on $\opn{sd}^k \mbf{I}^2$
and based at $v_0$, where composition is concatenation of sequences, and the
involution is given by reversal of order and (\ref{eqn13}). 
Consider the sequence
\[ \partial \bsym{\rho}^{\natural} :=
\bigl( \partial (\sigma^{\natural}_1, \tau^{\natural}_1),  \ldots,
\partial (\sigma^{\natural}_{4^k}, \tau^{\natural}_{4^k}) \bigr) . \]
The evaluation 
$u(\partial \bsym{\rho}^{\natural})$ of the word $u(\bsym{s})$
on the sequence
$\partial \bsym{\rho}^{\natural}$ is an element of $M$. And we have
\begin{equation} \label{eqn:35}
\bigl[ u(\partial \bsym{\rho}^{\natural}) \bigr] = 
u(a^{\natural}_1, \ldots, a^{\natural}_{4^k})
\end{equation}
in the group $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.

Take
\[ w(\bsym{s}) := u(\bsym{s}) * s_i * u(\bsym{s})^{-1} \in \opn{Wrd}^{\pm
1}(\bsym{s}) .
\]
It is easy to check that 
\[ [\partial (\sigma, \tau)] = w(a_1^{\natural}, \ldots, a^{\natural}_{4^k}) \]
holds in $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$. Next, using Corollary
\ref{cor:6} recursively, equation (\ref{eqn:35}) 
and Lemma \ref{lem:11}(2), we obtain
\[ \begin{aligned}
w(h^{\natural}_1, \ldots, h^{\natural}_{4^k}) & =
u(h^{\natural}_1, \ldots, h^{\natural}_{4^k}) \cdot h^{\natural}_i \cdot 
u(h^{\natural}_1, \ldots, h^{\natural}_{4^k})^{-1}  \\
& =
\opn{MI} \bigl( \alpha, \beta \vert 
u(\partial \bsym{\rho}^{\natural}) * \sigma^{\natural}_i, \tau^{\natural}_i
\bigr)  \\
& =
\opn{MI} \bigl( \alpha, \beta \vert \sigma , \tau \bigr) .
\end{aligned} \]
\end{proof}

\begin{lem} \label{lem:13}
Let $\bsym{\rho}^{\natural}$ be a generating sequence for 
$\opn{sd}^k \mbf{I}^2$, and let 
\[ \bsym{\rho} = \bigl( (\sigma_1, \tau_1), \, \ldots, \, (\sigma_m, \tau_m) 
\bigr) \]
be some sequence of kites in $(\mbf{I}^2, v_0)$ patterned on 
$\opn{sd}^k \mbf{I}^2$ and aligned with $\bsym{\rho}^{\natural}$.
Write
\[ a_i := [\partial (\sigma_i, \tau_i)]  \in
\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2) \]
and
\[ h_i := \opn{MI} (\alpha, \beta \vert \sigma_i, \tau_i)\in H . \]
Let 
\[ u(\bsym{s}) \in \opn{Wrd}^{\pm 1}(\bsym{s}) = 
\opn{Wrd}^{\pm 1}(s_1, \ldots, s_{m}) \]
be a word such that
\[ u(a_1, \ldots, a_m) = 1 . \]
Then 
\[ u(h_1, \ldots, h_m) = 1 . \]
\end{lem}

\begin{proof}
Using Lemma \ref{lem:12}, for each $i \in \{ 1, \ldots, m \}$ we can find
a word 
\[ w_i(\bsym{t}) \in \opn{Wrd}^{\pm 1}(\bsym{t}) = 
\opn{Wrd}^{\pm 1}(t_1, \ldots, t_{4^k}) \]
such that
\[ a_i = w_i(a^{\natural}_1, \ldots, a^{\natural}_{4^k}) \]
and
\[ h_i = w_i(h^{\natural}_1, \ldots, h^{\natural}_{4^k})  \]
(with notation as in the previous lemmas). Define
\[ w(\bsym{t}) := u \bigl( w_1(\bsym{t}), \ldots, w_m(\bsym{t}) \bigr) \in
\opn{Wrd}^{\pm 1}(\bsym{t}) . \]
Then
\[ w(a^{\natural}_1, \ldots, a^{\natural}_{4^k}) = 1 \] 
in 
$\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$, 
and 
\[ w(h^{\natural}_1, \ldots, h^{\natural}_{4^k}) = u(h_1, \ldots, h_m)  \]
in $H$.

Now according to Lemma \ref{lem:17} we have
$w(\bsym{t}) \sim_{\mrm{can}} 1$ in $\opn{Wrd}^{\pm 1}(\bsym{t})$. 
Hence by cancellation in the group $H$ we get
$w(h^{\natural}_1, \ldots, h^{\natural}_{4^k}) = 1$.
\end{proof}


\subsection{The Flip}
The flip of $\mbf{I}^2$ is the linear automorphism whose action on vertices is
\[ \opn{flip}(v_0, v_1, v_2) := (v_0, v_2, v_1) . \]
Given a kite $(\sigma, \tau)$ in $(\mbf{I}^2, v_0)$, its flip is the kite 
\[ \opn{flip}(\sigma, \tau) := (\sigma, \tau \circ \opn{flip} ) . \]
See Figure \ref{fig:34} for an illustration.

\begin{figure}
\includegraphics[scale=0.36]{fig34.jpg}
\caption{A kite $(\sigma, \tau)$ in $(\mbf{I}^2, v_0)$, and the kite
$\opn{flip} (\sigma, \tau)$.} 
\label{fig:34}
\end{figure}

Note that 
\[ \opn{flip} (\sigma, \tau) 
= (\sigma, \tau) \circ \opn{flip} (\sigma^{0}_1, \tau^{0}_1) , \] 
where $(\sigma^{0}_1, \tau^{0}_1)$ is the basic kite. 
By associativity of kite composition it follows that given any two kites
$(\sigma_1, \tau_1)$ and $(\sigma_2, \tau_3)$ in $\mbf{I}^{2}$, one has
\begin{equation} \label{eqn:55}
\opn{flip} \bigl( (\sigma_1, \tau_1) \circ (\sigma_2, \tau_2) \bigr)
= (\sigma_1, \tau_1) \circ \opn{flip} (\sigma_2, \tau_2)
\end{equation}

If  $(\sigma, \tau)$ is a kite patterned on $\opn{sd}^k \mbf{I}^2$ for
some $k$, then the effect of flipping is:
\begin{equation} \label{eqn:177}
[ \partial \opn{flip}(\sigma, \tau) ] =  [ \partial (\sigma, \tau) ]^{-1}
\end{equation}
in $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.

\begin{lem} \label{lem:41}
Let $(\sigma, \tau)$ be a kite in $(\mbf{I}^2, v_0)$, and let 
$k \geq 0$. Then 
\begin{equation} \label{eqn:178}
\opn{MI} \bigl( \alpha, \beta \vert \opn{flip}(\sigma, \tau) \bigr) = 
\prod_{i = 4^k}^1 \, 
\opn{MI} \bigl( \alpha, \beta \vert \opn{flip}( (\sigma, \tau) \circ 
(\sigma^k_i, \tau^k_i) ) \bigr) .
\end{equation}
\end{lem}

Note that the order of the product is reversed!

\begin{proof}
By moving the base point from $v_0$ to $x_0 := \tau(v_0)$ along the string
$\sigma$, and using Theorem \ref{thm:14}, we now have to prove that 
(\ref{eqn:178}) holds for a kite $(\sigma, \tau)$ in the pointed polyhedron
$(\mbf{I}^2, x_0)$, and moreover $\sigma$ is the empty string. 
Next we use Proposition \ref{prop:10} for the map of pointed polyhedra
$\tau : (\mbf{I}^2, v_0) \to (\mbf{I}^2, x_0)$ to reduce to proving 
(\ref{eqn:178}) for $(\sigma, \tau) = (\sigma^0_1, \tau^0_1)$,
the basic kite  in $(\mbf{I}^2, v_0)$.

So we have to prove that 
\begin{equation} \label{eqn:181}
\opn{MI} \bigl( \alpha, \beta \vert \opn{flip}(\sigma^0_1, \tau^0_1) \bigr) = 
\prod_{i = 4^k}^1 \, 
\opn{MI} \bigl( \alpha, \beta \vert \opn{flip}(\sigma^k_i, \tau^k_i) \bigr) .
\end{equation}
holds. 

For any $i \in \{ 1, \ldots, 4^k \}$ define
\[ (\sigma^{\natural}_i, \tau^{\natural}_i) :=
\opn{flip} (\sigma^0_1, \tau^0_1) \circ (\sigma^k_i, \tau^k_i) . \]
Then 
\[ \bsym{\rho}^{\natural} := \bigl( (\sigma^{\natural}_1, \tau^{\natural}_1),
\ldots, (\sigma^{\natural}_{4^k}, \tau^{\natural}_{4^k}) \bigr) \]
is a generating sequence for $\opn{sd}^k \mbf{I}^2$. By Proposition
\ref{prop:3} we know that
\begin{equation} \label{eqn:179}
\opn{MI} \bigl( \alpha, \beta \vert \opn{flip}(\sigma^0_1, \tau^0_1) \bigr) = 
\prod_{i = 1}^{4^k} \, h^{\natural}_i ,
\end{equation}
where $h^{\natural}_i$ are as in Lemma \ref{lem:12}.
And it is clear from Definition \ref{dfn:4}(2) and formula (\ref{eqn:177}) that 
\begin{equation} \label{eqn:180}
\prod_{i = 1}^{4^k} \, a^{\natural}_i = [ \partial \mbf{I}^2 ] ^{-1} ,
\end{equation}
where $a^{\natural}_i$ are as in Definition \ref{dfn:33}.

Consider another sequence of kites
\[ \bsym{\rho} := \bigl( (\sigma^{}_1, \tau^{}_1),
\ldots, (\sigma^{}_{4^k}, \tau^{}_{4^k}) \bigr) , \]
where we define
\[ (\sigma_i, \tau_i) := \opn{flip}(\sigma^k_i, \tau^k_i) . \]
It is not hard to show, by induction on $k$, that these kites are aligned with
the generating sequence $\bsym{\rho}^{\natural}$.
Let $a_i$ and $h_i$ be as in Lemma \ref{lem:13}, where we take 
$m := 4^k$ of course. Again by induction on $k$ one shows that 
\[ \prod_{i = 4^k}^1 \, a_i = [ \partial \mbf{I}^2 ] ^{-1} . \]
Combining this with (\ref{eqn:180}) we deduce
\[ a_{4^k} \cdots a_2 \cdot a_1 \cdot 
(a^{\natural}_{4^k})^{-1} \cdots (a^{\natural}_2)^{-1} \cdot
(a^{\natural}_1)^{-1} = 1  \]
in $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.
Now Lemma \ref{lem:13} says that 
\[  h_{4^k} \cdots h_2 \cdot h_1 \cdot 
(h^{\natural}_{4^k})^{-1} \cdots (h^{\natural}_2)^{-1} \cdot
(h^{\natural}_1)^{-1} = 1 \]
in $H$. Using (\ref{eqn:179}) we get
\[ \prod_{i = 4^k}^1 \, h_i =
\opn{MI} \bigl( \alpha, \beta \vert \opn{flip}(\sigma^0_1, \tau^0_1) \bigr) . \]
This is precisely (\ref{eqn:181}).
\end{proof}

\begin{dfn}
In this section, a kite $(\sigma, \tau)$ in $(\mbf{I}^2, v_0)$ will be called 
{\em $(\alpha, \beta)$-tiny} if it is a square kite, 
$\opn{len}(\sigma) \leq 5$,
and
\[ \opn{side}(\tau) < \min \bigl( \epsilon_4(\alpha, \beta), \,
\epsilon_5(\alpha, \Psi_{\h}) \bigr) \, . \]
See Lemma \ref{lem:10} and Proposition \ref{prop:21} regarding the constants 
$\epsilon_4(\alpha, \beta)$ and $\epsilon_5(\alpha, \Psi_{\h})$.
\end{dfn}

\begin{lem} \label{lem:14}
Let $(\sigma, \tau)$ be a kite in $(\mbf{I}^2, v_0)$. Then
\begin{equation} \label{eqn:184}
\opn{MI} \bigl( \alpha, \beta \vert \opn{flip}(\sigma, \tau) \bigr) =
\opn{MI} (\alpha, \beta \vert \sigma, \tau)^{-1} .
\end{equation}
\end{lem}

\begin{proof}
Step 1. Assume $(\sigma, \tau)$ is $(\alpha, \beta)$-tiny and 
$\beta|_{\tau(\mbf{I}^2)}$ is smooth. 
We may assume that $\epsilon := \opn{side}(\tau)$ is positive
(since the case $\epsilon = 0$ is trivial).

Since the flip reverses the orientation, it follows that
\[ \opn{RP}_0  \bigl( \alpha, \beta \vert \opn{flip}(\sigma, \tau) \bigr) =
\opn{RP}_0 ( \alpha, \beta \vert \sigma, \tau)^{-1} ; \]
cf.\ Definition \ref{dfn:11}.
Next, by applying Proposition \ref{prop:8} to both $(\sigma, \tau)$ and \lb
$\opn{flip}(\sigma, \tau)$, we have 
\begin{equation} \label{eqn:182}
\Norm{ \log_H \bigl( 
\opn{MI} \bigl( \alpha, \beta \vert \opn{flip}(\sigma, \tau) \bigr) \bigr)
- \log_H \bigl( 
\opn{MI} (\alpha, \beta \vert \sigma, \tau)^{-1} \bigr) }
\leq 2 \cdot c_2(\alpha, \beta) \cdot \epsilon^4 \, . 
\end{equation}

\medskip \noindent
Step 2. Again we assume that $(\sigma, \tau)$ is $(\alpha, \beta)$-tiny
and $\epsilon := \opn{side}(\tau)$ is positive; but we do not assume smoothness.

Take $k \geq 0$. For each index $i \in \{ 1, \ldots, 4^k \}$ we let
\[ (\sigma_i, \tau_i) := (\sigma, \tau) \circ (\sigma^k_i, \tau^k_i)
= \opn{tes}^k_i (\sigma, \tau) . \]
Note that 
$\opn{side}(\tau_i) = (\smfrac{1}{2})^k \cdot \epsilon$. 
The subsets $\opn{good}(\tau, k)$ and $\opn{bad}(\tau, k)$ of 
$\{ 1, \ldots, 4^k \}$ were defined in Definition \ref{dfn:45}.
According to Lemma \ref{lem:51}, there are constants 
\[ a_j := a_j(\alpha, \beta, \tau(\mbf{I}^2)) \]
such that 
\[ \abs{ \opn{bad}(\tau, k) } \leq a_0 + a_1 \cdot 2^k \, . \]

If $i$ is a good index, then by step 1 we know that 
\[ \begin{aligned}
& \Norm{ \log_H \bigl( 
\opn{MI} ( \alpha, \beta \vert \opn{flip}(\sigma_i, \tau_i) ) \bigr)
- \log_H \bigl( 
\opn{MI} ( \alpha, \beta \vert \sigma_i, \tau_i)^{-1} \bigr) } \\
& \qquad \leq 2 \cdot  c_2(\alpha, \beta) \cdot (\smfrac{1}{2})^{4 k} \cdot 
\epsilon^4 \, .
\end{aligned} \]
And if $i$ is a bad index, then by Proposition \ref{prop:8}(1) we have
\begin{equation} \label{eqn:192}
\begin{aligned}
& \Norm{ \log_H \bigl( 
\opn{MI} ( \alpha, \beta \vert \opn{flip}(\sigma_i, \tau_i) ) \bigr)
- \log_H \bigl( 
\opn{MI} ( \alpha, \beta \vert \sigma_i, \tau_i)^{-1} \bigr) } \\
& \qquad \leq 2 \cdot  c_1(\alpha, \beta) \cdot (\smfrac{1}{2})^{2 k} \cdot 
\epsilon^2 \, .
\end{aligned}
\end{equation}
The conditions in property (ii) of Theorem \ref{thm:6} are satisfied. Hence,
using Lemma \ref{lem:41} and Proposition \ref{prop:3}, we obtain these
estimates:
\[ \begin{aligned}
& \Norm{ \log_H \bigl( 
\opn{MI} ( \alpha, \beta \vert \opn{flip}(\sigma, \tau) ) \bigr) -
\log_H \bigl( 
\opn{MI} ( \alpha, \beta \vert \sigma, \tau)^{-1} \bigr) } \\
& \quad = \Norm{ \log_H \Bigl( \,
\prod_{i = 4^k}^1 \, 
\opn{MI} ( \alpha, \beta \vert \opn{flip}(\sigma_i, \tau_i) ) \Bigr) \\
& \qquad \qquad - \log_H \Bigl( \,
\prod_{i = 4^k}^1 \, 
\opn{MI} ( \alpha, \beta \vert \sigma_i, \tau_i)^{-1} \Bigr) } \\
& \quad \leq 
\abs{ \opn{good}(\tau, k) } \cdot 2 \cdot  c_2(\alpha, \beta) \cdot
(\smfrac{1}{2})^{4 k} \cdot  \epsilon^4 \\
& \qquad \qquad +
\abs{ \opn{bad}(\tau, k) } \cdot 2 \cdot  c_1(\alpha, \beta) \cdot 
(\smfrac{1}{2})^{2 k} \cdot  \epsilon^2 \\
& \quad \leq 
4^k \cdot 2 \cdot  c_2(\alpha, \beta) \cdot
(\smfrac{1}{2})^{4 k} \cdot  \epsilon^4 +
(a_0 + a_1 \cdot 2^k) \cdot 2 \cdot  c_1(\alpha, \beta) \cdot 
(\smfrac{1}{2})^{2 k} \cdot  \epsilon^2 \, . 
\end{aligned} \]
As $k \to \infty$ the last term goes to $0$. Hence (\ref{eqn:184}) holds in
this case.

\medskip \noindent
Step 3. Now $(\sigma, \tau)$ is an arbitrary kite in $(\mbf{I}^2, v_0)$. 
We may assume that $\tau(\mbf{I}^2)$ is $2$-dimensional, for otherwise things
are trivial. As done in the beginning of the proof of Lemma \ref{lem:41}, we can
modify the setup so that $(\sigma, \tau)$ is a square kite and 
$\opn{len}(\sigma) \leq 1$. Take $k$ large enough so that all the kites
\[ (\sigma_i, \tau_i) := (\sigma, \tau) \circ (\sigma^k_i, \tau^k_i) , \]
$i \in \{ 1, \ldots, 4^k \}$, are $(\alpha, \beta)$-tiny. 
By Step 2 we know that 
\[ \opn{MI} \bigl( \alpha, \beta \vert \opn{flip}(\sigma_i, \tau_i) \bigr) =
\opn{MI} (\alpha, \beta \vert \sigma_i, \tau_i)^{-1} \]
holds for all $i$. Hence, using Lemma \ref{lem:41} and Proposition
\ref{prop:3}, we conclude that
\[ \begin{aligned}
& \opn{MI} ( \alpha, \beta \vert \opn{flip}(\sigma, \tau) ) = 
\prod_{i = 4^k}^1 \, 
\opn{MI} ( \alpha, \beta \vert \opn{flip}(\sigma_i, \tau_i) ) \\
& \qquad = 
\prod_{i = 4^k}^1 \, 
\opn{MI} ( \alpha, \beta \vert \sigma_i, \tau_i)^{-1} 
 = \Bigl( \prod_{i = 1}^{4^k} \, 
\opn{MI} ( \alpha, \beta \vert \sigma_i, \tau_i) \Bigr)^{-1} \\
& \qquad  = \opn{MI} ( \alpha, \beta \vert \sigma, \tau)^{-1} . 
\end{aligned} \]
\end{proof}



\subsection{The Turn}
The (counterclockwise) turn of $\mbf{I}^2$ is the linear automorphism
$\opn{turn} : \mbf{I}^2 \to \mbf{I}^2$ defined on vertices by
\[ \opn{turn}(v_0, v_1, v_2) := (v_1, (1, 1), v_0) . \]
The turn of the basic kite $(\sigma^0_1, \tau^0_1)$ is
\[ \opn{turn}(\sigma^0_1, \tau^0_1) 
:= \bigl( (v_0, v_1), \opn{turn} \Bigr) . \]
Given any kite $(\sigma, \tau)$ in $(\mbf{I}^2, v_0)$, its turn is the kite
\[ \opn{turn}(\sigma, \tau) := 
(\sigma, \tau) \circ \opn{turn}(\sigma^0_1, \tau^0_1) . \]
See figure \ref{fig:36}.

\begin{figure}
\includegraphics[scale=0.36]{fig36.jpg}
\caption{A kite $(\sigma, \tau)$ in $(\mbf{I}^2, v_0)$, and the kite
$\opn{turn} (\sigma, \tau)$.} 
\label{fig:36}
\end{figure}

Observe that for kites $(\sigma_1, \tau_1)$ and $(\sigma_2, \tau_2)$ in 
$(\mbf{I}^2, v_0)$, one has
\begin{equation} \label{eqn:56}
\opn{turn} \bigl( (\sigma_1, \tau_1) \circ (\sigma_2, \tau_2) \bigr)
= (\sigma_1, \tau_1) \circ \opn{turn} (\sigma_2, \tau_2) . 
\end{equation}
If $(\sigma, \tau)$ is patterned on $\opn{sd}^k \mbf{I}^2$, then the boundaries
satisfy
\begin{equation} \label{eqn:185}
[ \partial \opn{turn}(\sigma, \tau) ] =  [ (\sigma, \tau) ]
\end{equation}
in $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.

\begin{lem} \label{lem:42}
Let $(\sigma, \tau)$ be a kite in $(\mbf{I}^2, v_0)$, and let $k \geq 0$. Then 
\begin{equation*} \label{eqn:186}
\opn{MI} \bigl( \alpha, \beta \vert \opn{turn}(\sigma, \tau) \bigr) = 
\prod_{i = 1}^{4^k} \, 
\opn{MI} \bigl( \alpha, \beta \vert \opn{turn}( (\sigma, \tau) \circ 
(\sigma^k_i, \tau^k_i) ) \bigr) .
\end{equation*}
\end{lem}

\begin{proof}
The proof is very similar to that of Lemma \ref{lem:41}. As we showed there, it 
suffices to consider the case
$(\sigma, \tau) = (\sigma^0_1, \tau^0_1)$.
So we have to prove
\begin{equation} \label{eqn:187} 
\opn{MI} \bigl( \alpha, \beta \vert \opn{turn}(\sigma^0_1, \tau^0_1) \bigr) = 
\prod_{i = 1}^{4^k} \, 
\opn{MI} \bigl( \alpha, \beta \vert \opn{turn}(\sigma^k_i, \tau^k_i) \bigr) .
\end{equation}

For any $i \in \{ 1, \ldots, 4^k \}$ let
\[ (\sigma^{\natural}_i, \tau^{\natural}_i) :=
\opn{turn}(\sigma^0_1, \tau^0_1) \circ  (\sigma^k_i, \tau^k_i) . \]
The sequence
\[ \bsym{\rho}^{\natural} := \bigl( (\sigma^{\natural}_1, \tau^{\natural}_1),
\ldots, (\sigma^{\natural}_{4^k}, \tau^{\natural}_{4^k}) \bigr) \]
is a generating sequence of kites for $\opn{sd}^k \mbf{I}^2$.
Define elements $a^{\natural}_i$ and $h^{\natural}_i$ as 
in Definition \ref{dfn:33} and Lemma \ref{lem:12}, with respect to
the this new generating sequence $\bsym{\rho}^{\natural}$. 
By Proposition \ref{prop:3} we know that
\begin{equation} \label{eqn:188} 
\opn{MI} \bigl( \alpha, \beta \vert \opn{turn}(\sigma^0_1, \tau^0_1) \bigr) = 
\prod_{i = 1}^{4^k} \, h^{\natural}_i  \, .
\end{equation}
And by induction on $k$ it is not hard to see that 
\begin{equation} \label{eqn:189} 
\prod_{i = 1}^{4^k} \, a^{\natural}_i  = [ \partial \mbf{I}^2 ] . 
\end{equation}

Next consider the sequence of kites
\[ \bsym{\rho} := \bigl( (\sigma_1, \tau^{}_1),
\ldots, (\sigma^{}_{4^k}, \tau^{}_{4^k}) \bigr) , \]
where
\[ (\sigma_i, \tau_i) := \opn{turn}(\sigma^k_i, \tau^k_i) . \]
These kites are all aligned with $\bsym{\rho}^{\natural}$.
Take $a_i$ and $h_i$ defined as in Lemma \ref{lem:13}. We then have
\[ \prod_{i = 1}^{4^k} \, a_i = [ \partial \mbf{I}^2 ] . \]
Applying Lemma \ref{lem:13} we conclude that 
\[ \prod_{i = 1}^{4^k} \, h_i = \prod_{i = 1}^{4^k} \, h^{\natural}_i . \]
Combining this equation with (\ref{eqn:188})
we can deduce that equation (\ref{eqn:187}) is true.
\end{proof}

\begin{lem} \label{lem:16}
Let $(\sigma, \tau)$ be a kite in $(\mbf{I}^2, v_0)$. 
Then
\begin{equation} \label{eqn:190}
\opn{MI} \bigl( \alpha, \beta \vert \opn{turn}(\sigma, \tau) \bigr) =
\opn{MI} (\alpha, \beta \vert \sigma, \tau) .
\end{equation}
\end{lem}

\begin{proof}
The proof is organized like that of Lemma \ref{lem:14}, so we allow ourselves
to be less detailed.

\medskip \noindent
Step 1. Here we assume that $(\sigma, \tau)$ is an $(\alpha, \beta)$-tiny kite,
the number $\epsilon := \opn{side}(\tau)$ is positive, and 
$\beta|_{\tau(\mbf{I}^2)}$ is smooth. Going back to Definition \ref{dfn:11},
and using its notation mixed with the present notation, we have
\[ \opn{RP}_0(\alpha, \beta \vert \sigma, \tau) = 
\exp_H \bigl( \epsilon^2 \cdot \Psi_{\h}(g)(\til{\beta}(z)) \bigr) . \]
Recall that 
\[ g = \opn{MI} \bigl( \alpha \vert \sigma * (\tau \circ \sigma_{\mrm{pr}})
\bigr) . \]

The turn does not change the area of the square 
$Z = \tau(\mbf{I}^2)$, nor its midpoint $z$; it only changes the string that
leads from $v_0$ to $z$. Indeed, the string that is related to 
$\opn{turn}(\sigma, \tau)$ is $\sigma * (\tau \circ \rho')$, 
where $\rho'$ is the string
\[ \rho' := (v_0, v_1) * (v_1, y) * (y, w) , \]
in $\mbf{I}^2$ with  
$y := (\smfrac{1}{2}, 1)$ and $w := (\smfrac{1}{2}, \smfrac{1}{2})$.
The formula for the Riemann product is
\[ \opn{RP}_0(\alpha, \beta \vert \opn{turn}(\sigma, \tau)) = 
\exp_H \bigl( \epsilon^2 \cdot \Psi_{\h}(g')(\til{\beta}(z)) \bigr) , \]
with 
\[ g' := \opn{MI} \bigl( \alpha \vert \sigma * (\tau \circ \rho') \bigr) . \]

Let
$\rho'' := \sigma_{\mrm{pr}}^{-1} * \rho'$, 
which is a closed string based at $w$. The group element
\[ g'' := \opn{MI} ( \alpha \vert \tau \circ \rho'' ) \]
satisfies $g' = g \cdot g''$. Since  
$\opn{len}(\tau \circ \rho'') = 3 \epsilon$,
we know by Proposition \ref{prop:21} that 
\[ \Norm{ \Psi_{\h}(g'') - \bsym{1} } \leq 
c_5(\alpha, \Psi_{\h}) \cdot 3 \epsilon \, . \]
But by Proposition \ref{prop:13} we have
\[ \norm{ \Psi_{\h}(g) } \leq  \exp \bigl( c_4(\alpha, \Psi_{\h}) \cdot 5
\bigr) \, . \]
Therefore
\[ \begin{aligned}
& \Norm{ \log_H \bigl(  \opn{RP}_0(\alpha, \beta \vert \opn{turn}(\sigma, \tau))
\bigr) -
\log_H \bigl(  \opn{RP}_0(\alpha, \beta \vert \sigma, \tau) \bigr) } \\
& \qquad = \epsilon^2 \cdot \bigl( \Psi_{\h}(g) \circ 
( \Psi_{\h}(g'') - \bsym{1} ) \bigr) (\til{\beta}(z)) \\
& \qquad \leq
\epsilon^3 \cdot c \, , 
\end{aligned} \]
where we write
\[ c := 
\exp \bigl( c_4(\alpha, \Psi_{\h}) \cdot 5 \bigr) \cdot 
3 \cdot c_5(\alpha, \Psi_{\h}) \cdot \norm{\beta}_{\mrm{Sob}} \, . \]
Combining this estimate with Proposition \ref{prop:8}(2), we obtain
\begin{equation} \label{eqn:191}
\begin{aligned}
& \Norm{ \log_H \bigl(  \opn{MI}(\alpha, \beta \vert \opn{turn}(\sigma, \tau))
\bigr) -
\log_H \bigl(  \opn{MI}(\alpha, \beta \vert \sigma, \tau) \bigr) } \\
& \qquad \leq  2 \cdot c_2(\alpha, \beta) \cdot \epsilon^4 +
c \cdot \epsilon^3 \, .
\end{aligned} 
\end{equation}

\medskip \noindent
Step 2. In this step we assume that $(\sigma, \tau)$ is an
$(\alpha, \beta)$-tiny kite and $\epsilon := \opn{side}(\tau)$ is
positive; but no smoothness is assumed. 

Take $k \geq 0$, and define kites $(\sigma_i, \tau_i)$ and  sets
$\opn{good}(\tau, k)$
and $\opn{bad}(\tau, k)$ like in step 2 of the proof of Lemma \ref{lem:14}.
If $i \in \opn{good}(\tau, k)$ then by equation (\ref{eqn:191}) in step 1 we
know
that 
\[ \begin{aligned}
& \Norm{ \log_H \bigl(  \opn{MI}(\alpha, \beta \vert 
\opn{turn}(\sigma_i, \tau_i)) \bigr) -
\log_H \bigl(  \opn{MI}(\alpha, \beta \vert \sigma_i, \tau_i) \bigr) } \\
& \qquad \leq  2 \cdot c_2(\alpha, \beta) \cdot (\smfrac{1}{2})^{4 k} \cdot
\epsilon^4 + 
c \cdot (\smfrac{1}{2})^{3 k} \cdot \epsilon^3 \, .
\end{aligned} \]
For $i \in \opn{bad}(\tau, k)$ we use the estimate (\ref{eqn:192}). 
As in the proof of Lemma \ref{lem:14}, but using Lemma \ref{lem:42} instead of
Lemma \ref{lem:41}, we arrive at the estimate
\[ \begin{aligned}
& \Norm{ \log_H \bigl( 
\opn{MI} ( \alpha, \beta \vert \opn{turn}(\sigma, \tau) ) \bigr) -
\log_H \bigl( 
\opn{MI} ( \alpha, \beta \vert \sigma, \tau) \bigr) } \\
& \qquad = \Norm{ \log_H \Bigl( \,
\prod_{i = 1}^{4^k} \, 
\opn{MI} ( \alpha, \beta \vert \opn{turn}(\sigma_i, \tau_i) ) \Bigr) -
\log_H \Bigl( \,
\prod_{i = 1}^{4^k} \, 
\opn{MI} ( \alpha, \beta \vert \sigma_i, \tau_i) \Bigr) } \\
& \qquad \leq 
\abs{ \opn{good}(\tau, k) } \cdot 
\bigl( 2 \cdot c_2(\alpha, \beta) \cdot (\smfrac{1}{2})^{4 k} \cdot
\epsilon^4 + c \cdot (\smfrac{1}{2})^{3 k} \cdot \epsilon^3 \bigr) \\
& \qquad \quad +
\abs{ \opn{bad}(\tau, k) } \cdot \bigl( 2 \cdot  c_1(\alpha, \beta) \cdot
(\smfrac{1}{2})^{2 k} \cdot \epsilon^2 \bigr) \\
& \qquad \leq 
4^k \cdot \bigl( 2 \cdot c_2(\alpha, \beta) \cdot (\smfrac{1}{2})^{4 k} \cdot
\epsilon^4 + c \cdot (\smfrac{1}{2})^{3 k} \cdot \epsilon^3 \bigr) \\
& \qquad \quad + 
(a_0 + a_1 \cdot 2^k) \cdot 
\bigl( 2 \cdot  c_1(\alpha, \beta) \cdot
(\smfrac{1}{2})^{2 k} \cdot \epsilon^2 \bigr) \, . 
\end{aligned} \]
As $k \to \infty$ the last term goes to $0$. Hence (\ref{eqn:190}) holds in
this case.

\medskip \noindent
Step 3. For an arbitrary kite $(\sigma, \tau)$ in $(\mbf{I}^2, v_0)$ we prove
that (\ref{eqn:190}) holds using step 2, as was done in step 3 of the proof of  
Lemma \ref{lem:14}, but using Lemma \ref{lem:42} instead of Lemma \ref{lem:41}.
\end{proof}


\subsection{Putting it all Together}

\begin{thm} \label{thm:7}
Let 
\[ \mbf{C} / \mbf{I}^2  = (G, H, \Psi, \Phi_0, \Phi_{X}) \]
be a Lie quasi crossed module over $(X, x_0) := (\mbf{I}^2, v_0)$,  let
$(\alpha, \beta)$ be a connection-curvature pair  in $\mbf{C} / \mbf{I}^2$,
and let 
\[ \bsym{\rho} = \bigl( (\sigma_1, \tau_1), \, \ldots, \, (\sigma_m, \tau_m) 
\bigr) \]
be a sequence of kites in $(\mbf{I}^2, v_0)$ patterned on 
$\opn{sd}^k \mbf{I}^2$, for some $k \in \N$.
For $i \in \{ 1, \ldots, m \}$ define
\[ a_i := [\partial (\sigma_i, \tau_i)] \in 
\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2) \]
and
\[ h_i := \opn{MI} ( \alpha, \beta \vert \sigma_i, \tau_i) \in H . \]

Suppose 
\[  w(\bsym{s}) \in \opn{Wrd}^{\pm 1}(\bsym{s}) = \opn{Wrd}^{\pm 1}(s_1, \ldots,
s_m) \]
is a word such that 
\[ w(a_1, \ldots, a_m) =  1 \]
in $\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2)$.
Then 
\[ w(h_1, \ldots, h_m) = 1 \]
in $H$.
\end{thm}

\begin{proof}
We can find $l_i \in \{ 0, 1 \}$ and 
$j_i \in \{ 0, 1, 2, 3 \}$, such that the kites
\[ (\sigma'_i, \tau'_i) := \opn{flip}^{l_i} \bigl( 
\opn{turn}^{j_i} (\sigma_i, \tau_i) \bigr) \]
are aligned with the generating sequence 
$\opn{tes}^k \mbf{I}^2$.  Here the exponents
$l_i$ and $j_i$ refer to iteration of the corresponding operation. Let
$e_i := (-1)^{l_i}$, 
\[ a'_i := [\partial (\sigma'_i, \tau'_i)] \in 
\bsym{\pi}_1(\opn{sk}_1 \opn{sd}^k \mbf{I}^2) \]
and 
\[ h'_i := \opn{MI} (\alpha, \beta \vert \sigma'_i, \tau'_i) \in H . \]
Then 
$a_i^{e_i} = a'_i$, 
and by Lemmas \ref{lem:14} and \ref{lem:16} we also have
$h_i^{e_i} = h'_i$.

Consider the word
\[ u(\bsym{s}) := w \bigl( s_1^{e_1}, \ldots, s_m^{e_m} \bigr)
\in \opn{Wrd}^{\pm 1}(\bsym{s}) . \]
Then
\[ w(a_1, \ldots, a_m) = u(a'_1, \ldots, a'_m) \]
and
\[ w(h_1, \ldots, h_m) =u(h'_1, \ldots, h'_m) . \]
Now we can finish the proof with the use of Lemma \ref{lem:13}.
\end{proof}

\begin{cor} \label{cor:2}
Let 
\[ \mbf{C} / \mbf{I}^2  = (G, H, \Psi, \Phi_0, \Phi_{X}) \]
be a Lie quasi crossed module over $(X, x_0) := (\mbf{I}^2, v_0)$,  let
$(\alpha, \beta)$ be a connection-curvature pair  in $\mbf{C} / \mbf{I}^2$,
and let 
\[ \bsym{\rho} = \bigl( (\sigma_1, \tau_1), \, \ldots, \, 
(\sigma_{4^k}, \tau_{4^k}) \bigr) \]
be a tessellation of $\mbf{I}^2$ patterned on 
$\opn{sd}^k \mbf{I}^2$ \tup{(}cf.\ Definition \tup{\ref{dfn:4}}\tup{)}.
Then 
\[ \prod_{i = 1}^{4^k} \, 
\opn{MI} ( \alpha, \beta \vert \sigma_i, \tau_i)  = 
\opn{MI} (\alpha, \beta \vert \mbf{I}^2) . \]
\end{cor}

\begin{proof}
This is an immediate consequence of the theorem, taking
$m := 4^k + 1$,  
\[ w(\bsym{s}) := \Bigl( \prod\nolimits_{i = 1}^{m - 1} s_i \Bigr) 
\cdot s_m^{-1}  \]
and $(\sigma_m, \tau_m)$ the basic kite. 
\end{proof}









\cleardoublepage
