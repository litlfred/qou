---
doc_id: arxiv-1501.01574v3
doc_title: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL"
section_id: sec-002-12-cable-knots
section_title: "Cable knots"
section_number: 1.2
pages: 2-4
source_pdf: 1501.01574v3.pdf
source_sha256: 8af5d6264a0ad5e0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.989
doc_brief: "KNOT CABLING AND THE DEGREE OF THE COLORED JONES POLYNOMIAL — We study the behavior of the degree of the colored Jones polynomial and the boundary slopes of knots under the operation of cabling."
---
Suppose $K$ is a knot with framing 0, and $p,q$ are coprime integers.
The $(p,q)$-cable $K_{p,q}$ of $K$ is the $0$-framed satellite of $K$ with
pattern $(p,q)$-torus knot (see Section \ref{boundary-slopes} for more details).
In the statements of results below, and throughout the paper,  we will assume that our cables are non-trivial in the  sense  that $\abs{q}>1$.


\begin{theorem} \label{bdry slope}
 For every knot $K \subset S^3$ and  $(p, q)$ coprime  integers
we have 
 $$\left( q^2 bs_K \cup \{pq\} \right) \subset bs_{K_{p,q}}.$$
\end{theorem}

To continue, we recall
that  for any knot $K\subset S^3$
the degrees $ d_+[J_{K}(n)] $ and $ d_-[J_{K}(n)] $ are quadratic quasi-polynomials in $n$  \cite{ga-quasi}. This implies that their coefficients are periodic functions $\BN \to \BQ$.
The common period  of $d_+[J_K(n)]$ and $d_-[J_K(n)]$ is called \emph{the period of $K$}, denoted  by $\pi(K)$. 

In this paper we are concerned with the Jones slopes 
for knots with $\pi(K)\leq 2$ and for knots where the leading coefficient  of $d_+[J_K(n)]$ becomes constant for $n$ large enough.
We show that the Jones slopes of these  knots behave similarly to  boundary slopes under cabling operations (Propositions \ref{quasi} and \ref{quasi-constant}).
In particular, for knots with period at most two, combining  our results about Jones slopes with Theorem \ref{bdry slope} we obtain the following.

\begin{theorem}
 \label{period2}
 Let $K$ be a knot such that, for $n \gg 0$,
$$
d_+[J_K(n)]=a(n)n^2+b(n)n+d(n) \  {\rm and } \  d_-[J_K(n)]=a^*(n)n^2+b^*(n)n+d^*(n)$$
are  quadratic quasi-polynomials of period $\le 2$, with $b(n) \le 0$ and $b^*(n) \ge 0$. Suppose $\frac{p}{q} \notin js_K$. 
Then, we have 
$$ js_{\K} \subset  \big( q^2js_{K} \cup \{pq/4\} \big) \ {\rm and} \  js^*_{\K} \subset  \big( q^2js^*_{K} \cup \{pq/4\} \big).$$
Furthermore, if $(js_K \cup js^*_K) \subset bs_K$ we have $(js_{\K} \cup js^*_{\K}) \subset bs_{\K}$.
 \end{theorem}

The proof of Theorem \ref{period2} reveals that the properties that
 $b(n) \le 0$ and $b^*(n) \ge 0$ are preserved under cabling. We conjecture that these properties hold for all knots,
and that   $b(n)$ and $b^*(n)$  detect the presence of essential annuli in the knot complement.  This is stated in Conjecture
\ref{conj}, which we have verified for all the knots for which the degrees $d_+[J_K(n)]$ and $d_-[J_K(n)]$
are known.


Note that since we take  $\abs{q}>1$, the hypothesis that $p/q$  is not a Jones slope of $K$ will automatically be satisfied  for knots that have all of their Jones slopes
 integers.
A large class of knots with integer Jones slopes is the class of \emph{adequate} knots, which
includes alternating knots, Montesinos knots of length at least four,  pretzel knots with at least four strings
and Conway sums of strongly alternating tangles. The class of \emph{semi-adequate} knots (knots that are
$A$-- or  $B$--adequate) is much broader including all but a handful of prime knots up to 12 crossings, all Montesinos and pretzel knots, positive knots, torus knots, and closed 3-braids. 
The reader is referred to Section 3 below for the precise definition (Definition \ref{defi:adequate}) and to  \cite{fkp:survey, FKP-guts, FKP-semi, adam} and references therein
for more details and examples of semi-adequate knots.



\begin{theorem}
\label{main:js} Let $K$ be a knot and let  $K'$ be an iterated cable knot of $K$. 
\begin{enumerate}
\item If $K$ is a $B$-adequate knot, then $js_{K'} \subset bs_{K'}$.

\item If $K$ is an $A$-adequate knot, then $js^*_{K'} \subset bs_{K'}$.
\end{enumerate}
Hence, if $K$ is an adequate knot then $K'$ satisfies the Slope Conjecture.
\end{theorem}

An iterated torus knot is an iterated cable of the trivial knot.  As a corollary of Theorem \ref{main:js} we have the following.
\begin{corollary} \label{torusi}
Iterated torus knots satisfy the Slope Conjecture. 
\end{corollary}


 
Theorem \ref{period2} also  applies to several non-alternating  prime knots with up to nine crossings
(see Corollary \ref{low}). We should mention that Motegi-Takata \cite{MoTa} used Theorem  \ref{period2}
to  generalize Corollary \ref{torusi} to all  knots of zero Gromov norm (graph knots).

The proofs of Theorems  \ref{bdry slope} and \ref{period2} reveal that there is a remarkable similarity 
in the behaviors, under cabling,  of the  linear terms of $d_+[J_K(n)]$ and $d_-[J_K(n)]$ and the Euler characteristic of the essential surfaces
``selected" by the Slope Conjecture.  We conjecture that
the cluster points of the sets $\{2b_K(n)\}$ and $\{2b_K^{*}(n)\}$ contain information about the topology of essential surfaces
 that satisfy the Slope Conjecture for $K$. 
To state the conjecture, 
let  $\ell d_+[J_K(n)]$ denote the linear term of $d_+[J_K(n)]$ and let
$$jx_K:= \left\{ 2n^{-1}\ell d_+[J_K(n)]  \right\}'=\{2b_K(n)\}'.$$
\begin{conjecture} [{\rm Strong Slope Conjecture}] \label{slopeaug} Let $K$ be a knot and $a/b\in js_K$, with $b>0$ and $\gcd(a, b)=1$,  a  Jones slope of $K$. Then there is an essential surface $S\subset M_K$, with $\abs{\partial S}$  boundary components, 
and such that each component of $\partial S$ has slope $a/b$ and
$$\frac{\chi(S)}{{\abs{\partial S} b}} \in jx_K.$$
\end{conjecture}

Conjecture \ref{slopeaug}  implies a similar statement for $\{2b^*_K(n)\}'$ since it is know that
$d_-[J_K(n)] =d_+[J_K^*(n)]$, where $K^*$ denotes the mirror image of $K$.
An immediate corollary of Theorem \ref{slopeadequate} is the following:

\begin{corollary} Iterated cables of adequate knots satisfy the Strong Slope Conjecture. In particular, iterated torus knots satisfy the Strong Slope Conjecture.
\end{corollary}

We  also prove Conjecture \ref{slopeaug}  for 
pretzel knots of type $(-2, 3, p)$ and all
Montesinos knots with up to nine crossings (see Section 5).
