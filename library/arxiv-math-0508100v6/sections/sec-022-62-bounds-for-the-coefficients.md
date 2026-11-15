---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-022-62-bounds-for-the-coefficients
section_title: "Bounds for the coefficients"
section_number: 6.2
pages: 14-16
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.971
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
\lbl{sub.coeffbounds}

For a Laurent polynomial $f\in \BZ[q^{\pm 1/4}]$, we define $||f||_1$ as in
Definition \ref{def.l1norm}, i.e. $||f||_1$ is the sum of the absolute
values of its coefficients. Observe that

\begin{equation}
 ||f+g||_1 \leq ||f||_1+||g||_1, \qquad ||fg||_1 \leq
||f||_1 \, ||g||_1. \label{eq.ineq}
\end{equation}

Since $||\{j\}||_1 =2$, we have, for $k \leq n$
\begin{equation}
\left| \left|\{a\}_k\right|\right|_1  = \left|\! \left| \prod_{j=a-k+1}^a\{ j \}\right|\!\right|_1  \leq 2^k \leq 2^n
\label{32}
\end{equation}

It is known that the quantum binomial $\qbinom{m}{k}$ is a Laurent
polynomial in $q^{1/2}$ with {\em positive} integer coefficients,
hence its $l^1$-norm is obtained by putting $q^{1/2}=1$, which is
the classical  binomial $\binom{m}{k}$. One has, if $m \leq
n$,
\begin{equation} \left|\! \left|\qbinom{m}{k}\right|\!\right|_1=\binom{m}{k} \leq 2^m \leq
2^n \label{31}
\end{equation}



\begin{theorem}
\lbl{thm.3}
For every knot $K$ of $c+2$ crossings and
every $n$ we have:

\begin{equation}
\lbl{eq.l1}
||J_{K,n}||_1 \leq n^c 4^{c n}.
\end{equation}
\end{theorem}

\begin{proof}
The proof of the Theorem is easy using the state sum
definition of the colored Jones polynomial: The colored Jones
polynomial is the sum, over all states, of the weights of the
states. There are $n^c$ states, the weight of each is the product of
several $q$-factorials and $q$-binomial coefficients for which an
upper bound can be easily found. Let us now go to the details of the proof.

The knot $K$ is the closure of a $(1,1)$-tangle $T$ (or long knot),
with orientation given by the direction from the bottom boundary
point to the top boundary point. The crossing points of the diagram
of $T$ (on the standard 2-plane) break $T$ into $2c+5$ arcs, two of
which are {\em boundary} (i.e. each contains a boundary point of
$T$). The two crossings adjacent to the boundary arcs are called
{\em boundary crossings}.


To get from $c+2$ to $c$ in the estimate, we will choose
 the $(1,1)$-tangle $T$  such that (1) when going along $T$, starting at
 the bottom boundary point, we must pass the very first  crossing
(resp. very last crossing) by an
 overpass (respectively, an underpass) and (2) the two strands
 at each crossing are pointing upwards, as in the following figure:
\begin{equation}
\lbl{cross}
\psdraw{R+}{0.5in} \qquad \psdraw{R-}{0.5in}
\end{equation}


Here is how to get such a $(1,1)$-tangle $T$. Consider a diagram of
$K$ on a 2-sphere $S^2$. The $c+2$ crossings break the knot diagram
into $2c+4$ arcs. At each crossing we have an overpass and an
underpass. When we go along the knot starting at some point,
following the direction of the orientation, we pass through all
these underpasses and overpasses. Hence there must be an arc which
starts at an underpass and ends at an overpass, assuming there is at
leat one crossing. Remove from $S^2$ a small disk which is a small
neighborhood of a point inside this arc. What is left is a long knot
diagram on a disk, which can also be considered as a $(1,1)$-tangle
diagram in the strip $\BR\times [0,1]$ in the standard 2-plane which
satisfies requirement (1). Using the isotopy of the form
$$
\psdraw{rotateR}{2in}
$$
which moves crossings (positive or negative) into standard upright
position, we get the desired $(1,1)$-tangle.

A state $\bk$ is an assignment of numbers, called the colors, to the
crossings of the diagram of $T$, where each color is in
$\{0,\dots,n-1\}$. For a fixed state we will color the $2c+5$ arcs
as follow. First color the bottom boundary arc by 0. Going along the
diagram of $T$ from the bottom boundary point, if we are on an arc
of color $a$ and pass a crossing, the next arc will have color $a+k$
or $a-k$, according as the pass is an underpass or an overpass, see
 \eqref{cross}. Here $k$ is the color of the crossing.


We will only consider states such that  the colors of arcs are
between 0 and $n-1$ and the color of the top boundary arc is 0. The
under/overpass configuration at the two boundary crossings ensures
that the two boundary crossings have color 0, otherwise the arcs
next to the two boundary arcs would have negative colors. It follows
that the number of states is at most $n^c$.

The weights of the positive crossing  (on the left) and negative
crossing (on the right in \eqref{cross}) are

\begin{eqnarray}
\lbl{eq.R+-} R_+(n;a,b,k) &=&  (\text{unit})\,
\qbinom{b+k}{k} \{n-1+k-a\}_k, \\
R_- (n;a,b,k) &=& (\text{unit})\,\qbinom{a+k}{k} \{n-1+k-b\}_k,
\end{eqnarray}
where $(\text{unit})$ stands for $\pm$ a power of $q^{\pm 1/4}$,
which does not affect the $l^1$ norm. Note that both $a+k$ and $b+k$
in the above formulas are between $0$ and $n-1$.


The weight of a maximum/minimum point is a also $\pm$  a power of
$q^{\pm 1/4}$, whose exact formula is not important for us.  Let
$F(n,\bk)$ denote the product of weights of all the crossings and
all the extreme points. Then

\begin{equation}
\lbl{eq.statesum}
J_{K,n}(q)=\sum_{\bk} F(n,\bk).
\end{equation}


 Using the estimates \eqref{31} and \eqref{32}, we see
that $||R_{\pm}(n;a,b,k)||_1 \leq 4^n$. Since the weight of the two
boundary crossing is just a unit, the $l^1$ norm of $F(n,\bk)$ is
less than $4^{cn}$. From \eqref{eq.statesum} and the fact that there
are $n^c$ states, we get  $ ||J_{K,n}||_1 \le n^c 4^{cn}$.
\end{proof}

Since there is a constant $b$ such that $n^c \le b^n$, we have the
following.

\begin{theorem}
\lbl{95}
For every knot $K$, there is a constant $A_6$ such
that for every positive integer $n$,
$$ ||J_{K,n}||_1 \le (A_6)^n.$$

\end{theorem}



\subsection{Proof of Theorem \ref{thm.up}}
\lbl{sub.thmup}




Fix a knot with $c+2$ crossings. The bounds for the degrees of
$J_{K,n}$ (see Proposition \ref{21}) allow us to write
$$
J_{K,n}(q)=\sum_{j} a_{n,j} q^j
$$
where $ |j|\leq  n^2 (c+2+|w|)/4 + O(n)$. For such $j$, we have:
$$
|e^{j\a/n}|=e^{\Re(j\a)/n} \leq e^{ (c+2+|w|)n/4 + O(1))|\Re(\a)|}.
$$
Using Theorem \ref{thm.3} we get
$$
|J_{K,n}(e^{\a/n})| \leq  n^c 4^{cn} e^{ (c+2+|w|)n/4 +
O(1))|\Re(\a)|}.
$$
Thus,
$$
\frac{1}{n} \log|f_{K,n}(\a)| \leq c\log4 + \frac{c+2+|w|}{4}
|\Re(\a)| + O\left(\frac{\log n}{n} \right).
$$
The result follows from the observation that $|\w| \le c+2$, since
$c+2$ is the total number of crossings.

\qed






\section{Proof of Theorem \ref{thm.boundC}}
\lbl{sec.boundscyclotomic}


The goal of this Section is to prove  Theorem \ref{thm.boundC}.
