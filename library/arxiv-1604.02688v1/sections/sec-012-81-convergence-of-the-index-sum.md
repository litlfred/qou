---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-012-81-convergence-of-the-index-sum
section_title: "Convergence of the index sum"
section_number: 8.1
pages: 21-27
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.772
---
To understand the convergence of the index sum (as a formal Laurent series) 
we need to examine the lowest degree of the terms in this sum.  Given any 
coset $[S]=S+ \TT$, we can choose its ``minimal non-negative coset 
representative'' $S^*$. Explicitly,
given 
$$
S=(a_1, b_1, c_1, a_2, b_2, c_2, \ldots , a_n, b_n, c_n) \in  Q(\T;\Z)
$$
we have
$$
S^*=(a^*_1, b^*_1, c^*_1, a^*_2, b^*_2, c^*_2, \ldots , a^*_n, b^*_n, c^*_n),
$$
where 
$(a_j^*,b_j^*,c_j^*)=(a_j-m_j,b_j-m_j,c_j-m_j)$ and $m_j=\min\{a_j,b_j,c_j\}$.

Now $J(S^*)$ has leading term $q^{\frac{1}{2} \delta(S^*)}$ of degree 
$\frac{1}{2} \delta(S^*)$. So each surface $[S]$ occurring in the index 
sum (\ref{index_from_normal_surfaces}) contributes a term 
$I([S]) = (-q^{1/2})^{-\chi(S^*)}  J(S^*)$ of lowest $q^{1/2}$-degree 

\be
d([S])=d(S^*) =-\chi(S^*) + \delta(S^*)
\label{index_deg_surface}
\ee
and leading coefficient $(-1)^{-\chi(S^*)}$.

\begin{rmk}
Note that $S^*$ need not give an embedded normal surface, but there are 
{\em at most two} non-zero quad coordinates in each tetrahedron. In the 
next section we will show how to replace such a normal class by a unique 
{\em embedded generalised normal surface} $\tilde S$.
\end{rmk}

From this, it is easy to analyse the convergence of the index sums. First 
we give a new proof that the sum $I_\T^0(0)$ converges (as formal Laurent 
series) if and only if $\T$ contains no embedded normal surfaces of 
Euler characteristic $\ge 0$.

\begin{thm} 
\label{index0_cgce}
The index sum for $I_\T^0(0)$  converges (as a formal Laurent series) if 
and only if the triangulation $\T$ is 1-efficient.
\end{thm}

\begin{proof}
($\Rightarrow$) If the triangulation $\T$ is not 1-efficient then it 
contains a closed embedded normal surface  with non-negative Euler 
characteristic. Doubling this, if necessary, gives a closed embedded 
normal surface $S \in Q_0(\T;\Z_+)$ with
$\chi(S)\ge 0$, $\delta(S)=0$ and $S^*=S \ne 0$. 
Then for each integer $k\ge0$, $(kS)^* = k S$ contributes a term to the sum
(\ref{index0_from_normal_surfaces}) for $I_\T^0(0)$
with $q^{1/2}$-degree $d(kS) = -k\chi(S) \le 0$. So the index sum
cannot converge as a formal Laurent series in $q^{1/2}$.
 
($\Leftarrow$) Assume that  $\T$ is a 1-efficient ideal triangulation.  
First we note the following general fact.

\begin{lemma} 
\label{subadditive}
The function $d = -\chi + \delta: Q(\T;\R_+) \to \Z$ is superadditive, i.e.
$$
d(S+S') \ge d(S)+d(S').
$$
Hence $d(\sum_i n_i S_i) \ge \sum_i d(n_i S_i) \ge \sum_i n_i d(S_i)$ for 
all $S_i \in Q(\T;\R_+)$ and all integers $n_i \ge 0$.
\end{lemma} 

\begin{proof}
This follows since $\chi$ is a linear function and $\delta(S+S') 
\ge \delta(S)+\delta(S')$ provided all quad coordinates of $S$ and $S'$ 
are non-negative.
\end{proof}

Next we observe that $N(\T;\Z_+)$ is the set of integer points in a cone 
defined by homogeneous linear inequalities with integer coefficients. 
So we can choose a set of {\em fundamental solutions} 
(or {\em Hilbert basis} in integer linear programming theory) 
$F_1, \ldots,  F_m$  for  $N(\T;\Z_+)$. This means that every 
$S \in N(\T;\Z_+)$ can written (not necessarily uniquely)
as a finite sum $S= \sum_{i=1}^m n_i F_i$ 
where $n_i \in \Z_+$ and each $F_i$ is irreducible, i.e. has no 
decomposition $F_i=x+y$ where $x,y \in N(\T;\Z_+)$ and $x,y \ne 0$.

Now consider $f_i(x) = d(x F_i) = -\chi(F_i)x+\delta(F_i) x^2$, where $x \ge 0$.
Since $\T$ is 1-efficient, for each $i=1,\ldots,m$, we have either
(i) $\delta(F_i)=0$ and $-\chi(F_i) \ge 1$, or (ii) $\delta(F_i) \ge 1$.
Hence $f_i(x) \to \infty$ as $x \to +\infty$,  and in fact there are 
constants $a_i,b_i  \in \R$ with $a_i >0$ such that
$f_i(x) \ge a_i x - b_i$ for all $x \ge 0$.

Then each $S\in N(\T;\Z)$ can be written as a linear combination 
$S= \sum_{i=1}^m x_i F_i$ with $x_i \in \Z_+$
and, using Lemma  \ref{subadditive},  its $q^{1/2}$-degree satisfies 
$$d(S) \ge \sum_{i=1}^m d(x_i F_i) \ge \sum_i (a_i x_i -b_i).$$
Thus, $d(S) \le D$ implies $\sum_i a_i x_i \le D + \sum_i b_i$,
which has only finitely many solutions with $x_i \in \Z_+$. Hence $I_\T^0(0)$  
converges as a formal Laurent series.
\end{proof}

A similar argument gives the following

\begin{thm} 
\label{1-eff_cgce_I_T(b)}
If $\T$ is 1-efficient, then $I_\T^a(b)$ converges for all $a$ and $b$; 
in fact $\sum_a I_\T^a(b)$ is convergent for all $b$.
\end{thm}

\begin{proof} 
We may assume that  $b \ne 0$. Now consider  the set $Q_b(\T;\Z_+)$ of 
Q-normal classes $S \in Q(\T;\Z_+)$ whose boundary $\bd S$ is a 
non-negative integer multiple of $b$. This is the set of integer points 
in a cone defined by a set of homogeneous linear equations and inequalities 
with integer coefficients, so we can choose a finite set $F_1, \ldots, F_m$  
of fundamental solutions for $Q_b(\T;\Z_+)$ where $\bd F_i = s_i b$ with 
$s_i \in \Z_+$.

Given $S \in Q_b(\T;\Z_+)$ we can write $S = \sum x_i F_i$ where 
$x_i \in \Z_+$ and  $\bd S = (\sum s_i x_i )b$.
Let $I:=\{1,2,\ldots,m\}$ and write  $I= I_0  \cup I_1$ where 
$I_0 = \{ i \in I : s_i=0 \}$ and $I_1 = \{ i \in I : s_i \ge 1 \}$.
Then $S = S_0 + S_1$ where $S_0 = \sum_{i \in I_0} x_i F_i$ and 
$S_1 = \sum_{i \in I_1} x_i F_i$ and $\bd S = b$ if and only if 
$\sum_{i \in I_1} s_i x_i = 1$. So $S_1$ belongs to the finite set 
$\{ F_i : i \in I_1 \text{ and } s_i=1\}$, and $S_0 \in  N(\T;\Z)$. 

As in the proof of Theorem \ref {index0_cgce} there are constants 
$a_i,b_i  \in \R$ with $a_i >0$ such that $d(x_i F_i) \ge a_i x_i - b_i$ for 
each $i \in I_1$. Now
$$
d(S) \ge d(S_1)+d(S_0) \ge d(S_1) + \sum_{i \in I_1} d(x_i F_i) \ge 
d(S_1) + \sum_{i \in I_1}(a_i x_i - b_i).
$$
Hence given any $D \ge 0$ there are at most finitely many 
$S \in Q_b(\T;\Z_+)$ with $\bd S = b$ and  $d(S) \le D$. 
This implies the result.
\end{proof}

\begin{thm}
If $\T$ is {\em spun 1-efficient}, i.e. contains no embedded spun normal 
surface $S\ne 0$ with $\chi(S)\ge 0$, then the ``total index'' 
$I^{tot}_\T = \sum_{\text{all } (a,b)}  I_\T^a(b)$ converges.
\end{thm}

\begin{proof} 
Let $F_1, \ldots, F_m$ be a set of fundamental solutions for the set 
$Q(\T;\Z_+)$ of non-negative integer solutions to the Q-matching equations.   

Now consider $f_i(x) = d(x F_i) = -\chi(F_i)x+\delta(F_i) x^2$, where $x \ge 0$.
Since $\T$ is spun 1-efficient, for each $i=1,\ldots,m$, we have either
(i) $\delta(F_i)=0$ and $-\chi(F_i) \ge 1$, or (ii) $\delta(F_i) \ge 1$.
Hence $f_i(x) \to \infty$ as $x \to +\infty$, and in fact there are 
constants $a_i,b_i \in \R$ with $a_i >0$ such that
$f_i(x) \ge a_i x - b_i$ for all $x \ge 0$.

Then each $S\in Q(\T;\Z)$ can be written as a linear combination 
$S= \sum_{i=1}^m x_i F_i$ with $x_i \in \Z_+$
and, using Lemma \ref{subadditive},  its $q^{1/2}$-degree satisfies 
$$
d(S) \ge \sum_{i=1}^m d(x_i F_i) \ge \sum_i (a_i x_i -b_i).
$$
Thus, $d(S) \le D$ implies $\sum_i a_i x_i \le D + \sum_i b_i$,
which has only finitely many solutions with $x_i \in \Z_+$. Hence the total
index sum converges.
\end{proof}

\begin{thm}
Every 1-efficient ideal triangulation of an anannular 3-manifold other 
than the solid torus or solid Klein bottle is spun 1-efficient. 
\end{thm}

\begin{proof} 
This follows by a simple barrier argument. For more details see 
Jaco-Rubinstein \cite{JR} and Section \ref{barriers}. Assume that $\T$ 
is a 1-efficient triangulation of an anannular 3-manifold $M$, which is 
not spun 1-efficient. So there is an embedded spun normal surface $S$ 
with $\chi(S)\ge 0$ in $M$. Clearly then $S$ is a M\"obius band, annulus 
or disk. If $S$ is a disk, $M$ must be a solid torus or solid Klein bottle, 
which are excluded by assumption. So $S$ must be an annulus or M\"obius band. 
On the other hand, if $S$ is an annulus or M\"obius band, since $M$ is 
anannular, $S$ must be topologically boundary parallel, so is contained in 
a collar of a boundary component of $M$. (The M\"obius band case only occurs 
if $M$ is non-orientable and the corresponding cusp is a Klein bottle).
We can then push the appropriate boundary surface across this collar to 
give a torus or Klein bottle $T$ which is boundary parallel. Moreover the 
product region bounded by $T$ and a cusp contains $S$. 

We now wish to construct a barrier using $S$. Choose a normal torus or 
Klein bottle $T_0$ which consists entirely of triangular disks and is 
parallel to the cusp in the previous paragraph. We can assume that $S$ 
and $T_0$ are chosen to intersect transversely.  $S \cup T_0$ separates 
$M$ into various regions, with one such region $R$ homeomorphic to $M$. 
The boundary of $R$ contains a `piecewise normal' torus or Klein bottle 
and this is a barrier for normalisation of surfaces in $R$ in the sense 
of Jaco-Rubinstein \cite{JR}. So we can normalise the essential torus or 
Klein bottle $T_0$ in $R$ to give an embedded normal torus or Klein bottle 
which is not normally peripheral, contradicting  the assumption that $\T$ 
is 1-efficient. 
\end{proof}

\begin{rmk}
A 1-efficient ideal triangulation of an (open) solid torus can contain an 
embedded spun normal disk. In fact this happens in 
Example \ref{solid_torus_ex} below. 
\end{rmk}

A discussion of angle structures and angle structure with rotational 
holonomy zero on each peripheral curve follows in 
Appendix \ref{gen_angle_euler}.

\begin{cor}
If $\T$ admits a strict angle structure with rotational holonomy zero on 
each peripheral curve, then it is spun 1-efficient. In particular, this 
applies to any geometric triangulation of a cusped hyperbolic 3-manifold. 
\end{cor}

\begin{proof}
The Euler characteristic of any embedded spun normal surface $S$ can be 
calculated as $\sum_{q \in \quads} -\alpha(q)/\pi$,  if 
$\alpha: \quads \to (0,\pi)$ is an generalised angle structure 
with rotational holonomy zero on each peripheral curve. If $\alpha$ is a 
strict angle structure then the sum is negative, unless $S=0$.
\end{proof}

\begin{ex}
The 2-tetrahedron triangulation $\T$ of the trefoil knot complement in 
Example \ref{trefoil_ex}, is not spun 1-efficient. Here 
$I^0_\T(x \mu + y \lambda) =  \delta_{0,x+6y}$ for 
$x \in \Z, y \in \frac{1}{2} \Z$ so the total index 
$\sum_{x,y} I^0_\T(x \mu + y \lambda)$ diverges.
\end{ex}


\subsection{Non 1-efficient ideal triangulations}

When the triangulation $\T$ is not 1-efficient, it turns out that the 
series $I_\T^a(b)$ may converge for some $b \ne {\bf 0}$
even when the series $I_\T^0(0)$ diverges.  See Example \ref{toroidal_ex} 
below. The following result gives an obstruction to convergence.

\begin{lemma} 
Assume that an ideal triangulation $\T$ contains a Q-normal class 
$S \in Q(\T;\Z_+)$ with $[S]_2=a$ and $\bd S$ satisfying $[\bd S]=b$,
and there is a closed normal surface $0 \ne S' \in N(\T;\Z_+)$ such that 
$S'$ is embedded and $-\chi(S')+ 2\delta(S,S') \le 0$.
Then the index sum for $I_\T^a(b)$ diverges.
\end{lemma}

\begin{proof}
By replacing $S'$ by $2 S'$, if necessary, we can assume that 
$S' \in Q_0(\T;\Z_+)$. Then for all $k \in \Z_+$, the normal class 
$S_k=S+k S'$ contributes a term in the index sum 
(\ref{explicit_index_computation}) for $I_\T^a(b)$ with $q^{1/2}$-degree 
\begin{align}
d (S_k) &= -\chi(S+k S') + \delta(S+k S') \nonumber \\
&= -\chi(S)-k\chi(S') +\delta(S)+2k \delta(S,S')+k^2\delta(S') \nonumber \\
& = d(S)+k\left( -\chi(S')+2 \delta(S,S')\right)+k^2\delta(S').
\label{degree_S_k}
\end{align}
Hence $d(S_k)$ remains bounded above as $k \to +\infty$ if $\delta(S')=0$ 
and $-\chi(S')+2 \delta(S,S')\le 0$. Thus the index sum diverges.
\end{proof}

In general, we have the following converse.

\begin{thm} 
\label{cgce_I_T(b)} 
Assume that an ideal triangulation $\T$ does not contain a Q-normal class 
$S \in Q(\T;\Z_+)$ with $\bd S = b$, and a closed normal surface 
$S' \in N(\T;\Z_+)$ such that $S'$ is embedded and 
$-\chi(S')+ 2\delta(S,S') \le 0$. Then the index sum $I_\T^a(b)$ converges.
\end{thm}

\begin{proof}
We start by following the proof of Theorem \ref{1-eff_cgce_I_T(b)}. This 
shows that there exist finitely many normal classes
$S_1, \ldots, S_k \in Q(\T;\Z_+)$ with $\bd S_i=b$ and finitely many 
normal classes  $F_1, \ldots, F_m \in Q(\T;\Z_+)$ with $\bd F_i=0$ 
such that every $S \in Q_b(\T;\Z_+)$ with $\bd S = b$  can be written as
$$
S= S_j + \sum_{i=1}^m x_i F_i, \text{ where } 1\le j \le k 
\text{ and } x_i \in \Z_+.
$$

Now 
\begin{align*}
d(S) 
&= d(S_j)+ \sum_{i} (-\chi(F_i)+ 2 \delta(F_i,S_j))x_i 
+ \sum_{i ,j } \delta(F_i,F_j) x_i x_j \\
&\ge  d(S_j)+ \sum_{i} (-\chi(F_i)+ 2 \delta(F_i,S_j))x_i  
+ \delta(F_i) x_i ^2 .
\end{align*}
For each $i \in I_0$ we have, by assumption,  either $\delta(F_i)\ge 1$ 
or $-\chi(F_i)+ 2 \delta(F_i,S_1) \ge 1$ so it follows that 
$$
f_i(x):=(-\chi(F_i)+ 2 \delta(F_i,S_1))x  + \delta(F_i) x^2
$$
is bounded below for $x \ge 0$ and approaches 
$+\infty \text{ as } x\to +\infty.$
Since  there are only finitely possibilities  for $S_1$,
it follows that there are only finitely
many $S \in Q_b(\T;\Z)$ such that $\bd S = b$ and $d(S) \le D$. Hence the 
index sum for $I_\T^a(b)$ converges.
\end{proof}

\medskip

\begin{rmk}
\begin{enumerate}
\item 
When $b=0$ this reduces to Theorem \ref{index0_cgce}, as we can take $S=0$ 
in the above theorem.
\item 
If the triangulation $\T$ is {\em $0$-efficient} then 
Theorem \ref{cgce_I_T(b)} simplifies to the following: \\
$I_\T^a(b)$ converges if and only if $\T$ 
does not contain a Q-normal class $S \in Q(\T;\Z_+)$ with $\bd S = b$,  
and an \emph{embedded} closed normal surface $S'$ disjoint from $S$ such 
that  $\chi(S') =0$.
\end{enumerate}
\end{rmk}





\section{Invariance under 2-3 and 0-2 moves}  

The arguments of \cite{GHRS} extend easily to prove the following. 

\begin{thm} 
Let $\CT$ be an ideal triangulation of $M$ and let $\tilde \CT$ be obtained 
from $\CT$  by a 2-3 move. Then for all $a,b$ as above,
$I_{\CT}^a(b)=I_{\tilde\CT}^a(b)$ provided both sides are defined.
\end{thm} 

\begin{proof} 
We follow the argument from \cite[Theorem A.1]{GHRS}, indicating the main 
changes needed in the current setting. Consider a 2-3 move from $\CT$ to 
$\tilde \CT$; this occurs in a bipyramid consisting of $2$ tetrahedra in 
$\CT$ which are replaced by 3 tetrahedra sharing an edge of order 3 in 
$\tilde \CT$.

First note that each $Q$-normal class $S \in Q(\CT;\S)$  can be written 
as a linear combination of edge solutions, tetrahedral solutions and 
peripheral curve solutions with coefficients in $\frac{1}{2} \Z$, by the 
results of Section 6 (see Remark \ref{half-integer-coefs}).
As in section 4.4 of \cite{GHRS}, we can represent $S$ by a linear 
combination $\omega$ of oriented normal arcs in the induced triangulation 
$\T_\bd$ of $\bd M$, chosen so that each quad coordinate for $S$ is a sum 
of 4 ``turning numbers'' of normal arcs, coming from the 4 corners of the 
tetrahedron containing the quad (see figure 7 of \cite{GHRS}).

Explicitly, for each edge solution we choose a small normal linking
circle in  $\bd M$ around one end of the edge in $\T$,  we choose oriented 
normal curves representing each peripheral class, and for each tetrahedral 
solution we choose three normal arcs  oriented anticlockwise in a triangle 
coming from one corner of the tetrahedron. (If tetrahedral solutions are 
needed in the bipyramid, we choose the two triangles at the degree 3 
vertices at the top and bottom.) One difference from \cite{GHRS}  is that 
the coefficients of the normal arcs here can be {\em half-integers}; 
but each sum of turning numbers giving a quad coefficient is still an 
integer. 

To compute the index $I_\T^a(b)$, we choose a normal class $S_0$ with 
$[S_0]_2=a$ and $[\bd S_0]=b$, and have a contribution from each normal class
$$
S_{\kk} = S_0 + \sum k_i E_i,
$$ 
where $\kk=(k_i) \in \Z^{n-r}$ is a set of integer weights on a set
of $n-r$ ``basic edges''.  (The excluded edges are taken from a 
``maximal tree with 1- or 3- cycle for $\T$'' as in Theorem 4.3 
of \cite{GHRS}; this ensures that the map 
$\kk=(k_i) \mapsto \sum k_i E_i + \TT$ 
is an isomorphism from $\Z^{n-r}$ onto $(\EE+\TT)/\TT$.)
We can represent $S_0$ by a linear combination $\omega$ of oriented 
normal arcs as described above.
By adding $k_i$ small linking circles around one end of the $i$th edge 
in $\T$ we obtain a linear combination $\omega_{\kk}$ of oriented normal 
arcs which gives the 
quad coordinates of $S_{\kk} = S_0 + \sum k_i E_i$.

The construction of \cite{GHRS} shows how to replace $\omega$ by a linear 
combination $\tilde\omega$ of oriented normal arcs in $\tilde\T_\bd$ 
representing a normal class $\tilde S_0$ in $\tilde \T$ and this satisfies 
$[\tilde S_0]_2=[S_0]_2$ and $[\bd S_0] = [\bd \tilde S_0]$.   
(Essentially, $\tilde S_0$ is obtained by subdividing the normal disks of 
$S_0$, so its homology classes do not change.) 
Then the index sum for $I_{\tilde \T}^a(b)$ has a contribution for each 
normal class 
$$
\tilde S_{\tilde \kk} = \tilde S_0 + k_0 \tilde E_0 + \sum k_i \tilde E_i,
$$
where $k_0$ is the integer weight on the new edge class $\tilde E_0$ in 
$\tilde \T$, and $\kk=(k_i)\in\Z^{n-r}$ as above give the weights
on the edge classes $\tilde E_i$ coming from $\T$.
Adding small linking circles around one end of each  edge in $\T$ gives a 
linear combination of normal arcs  $\tilde\omega_{\tilde \kk}$
which gives the quad coordinates of $\tilde S_{\tilde \kk}$.

The proof of the Pentagon Equality (Lemma A.3 in \cite{GHRS}) now goes 
through verbatim; this gives the result. The only difference in the 
current setting is that coefficients of normal arcs and turning numbers 
can now be half-integers. However since the sums giving quad coefficients 
used in the tetrahedral index functions are integers,
the arguments of \cite{GHRS} go through without change.  
\end{proof}

The arguments from \cite{GHRS} also extend to give the following.

\begin{thm} 
\label{0-2invariance}
Let  $\CT$ be an ideal triangulation of $M$ and let $\tilde \CT$ be 
obtained from $\CT$  by a 0-2 move. Then for all $a,b$ as above,
$I_{\CT}^a(b)=I_{\tilde\CT}^a(b)$ provided both sides are defined.
\end{thm} 

\begin{proof}
Here the proof of Theorem 5.1 in  \cite{GHRS} applies, if we start with a 
linear combination $\omega$ of oriented normal arcs in $\T_\bd$
with $\frac{1}{2} \Z$ coefficients  giving the quad coordinates of $S_0$ 
with homology classes $[S_0]_2=a$ and $[\bd S_0]=b$.
\end{proof}
