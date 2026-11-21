---
doc_id: arxiv-2304.12545v1
doc_title: "HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF WALTER NEUMANN"
section_id: sec-005-6-connections-to-number-theory
section_title: "Connections to number theory"
section_number: 6
pages: 12-17
source_pdf: 2304.12545v1.pdf
source_sha256: bfc3c2be395b1b2d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.993
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
---
\label{sec.7}

The paper~\cite{NZ} and its sequel~\cite{N:combinatorics} suggested or led to
several interesting developments in pure number theory as well as in topology.
In this final section we describe of a few of these.

\bigskip

\noindent{\bf Values of Dedekind zeta functions and higher Bloch groups}

\smallskip\noindent
An important subclass of hyperbolic manifolds~$M=\BH^3/\G$ are the arithmetic ones, 
where $\G$ is either the Bianchi group $\SL_2(\calO_F)$ for some imaginary quadratic 
field~$F$ or more generally a group of units in a quaternion
algebra over a number field~$F$ of higher degree $n=r_1+2$ having only
one complex embedding up to complex conjugation.  In both cases,
classical results (proved in the first case by Humbert already in~1919) say
that the volume of ~$M$ is a simple multiple (a power of~$\pi$ times the
square-root of the discriminant) of the value at $s=2$ of the Dedekind zeta
function~$\z_F(s)$ of the field~$F$.  An immediate consequence of this and
of the volume formulas discussed in Section~\ref{sec.3} is that this zeta value
is a multiple of a linear combination of values of the Bloch-Wigner dilogarithm
at algebraic arguments.  This consequence was observed in~\cite{Z:hyperbolic}
and was also generalized there to the value of~$\z_F(2)$ for arbitrary number fields~$F$, 
with $[F:\BQ]=r_1+2r_2$ for any value of~$r_2\ge1$.  (If~$r_2=0$, then the well-known 
Klingen-Siegel theorem asserts that $\z_F(2)$ is a rational multiple of
$\pi^{2r_1}\sqrt{D_F}\,$.) Now the group $\SL_2(\calO_F)$ acts as a discrete group of
isometries of $(\BH^2)^{r_1}\times(\BH^3)^{r_2}$ with a quotient of finite volume, and
there are also quaternionic groups~$\G$ over~$F$ that acts freely and discretely
on~$(\BH^3)^{r_2}$, the volume of the quotient in both cases being an elementary
multiple of~$\z_F(2)$. This gives a ``poly-3-hyperbolic'' manifold $M=(\BH^3)^{r_2}/\G$
with volume proportional to~$\z_F(2)$.  A rather amusing lemma says that any such
manifold has a decomposition (disjoint except for the boundaries) into finitely many
$r_2$-fold products of hyperbolic tetrahedra, and it follows that~$\z_F(2)$  for any
number field has an expression as a linear combination of $r_2$-fold products of
values of~$D(z)$ at algebraic arguments, generalizing the Klingen-Siegel theorem
in an unexpected way. 

The connection with 3-dimensional hyperbolic geometry applies only to the values of
Dedekind zeta functions at~$s=2$, but suggested that there might be similar statements for
$\z_F(m)$ with $m>2$ in terms of the $m$th polylogarithm function~$\Li_m(z)$.  Extensive
numerical experiments led to a concrete conjecture saying that this is the case and also to
a definition (originally highly speculative, but now supported by more theory) of ``higher
Bloch groups" $\B_m(F)$ that should be isomorphic after tensoring with~$\Q$ to the higher
algebraic \hbox{$K$-groups} $K_{2m-1}(F)$ and should express the Borel regulator in terms of
polylogarithms. (For a survey, see~\cite{Z:polylogs}.)  This conjecture, now over 30 years
old, has been studied extensively by Beilinson, Deligne, de Jeu, Goncharov, Rudenko and 
others, with the cases~$m=3$ and~$m=4$ now being essentially settled.

\bigskip 

\noindent{\bf Units in cyclotomic extensions of number fields}

\smallskip\noindent
As already mentioned in the last section, the analysis of the Kashaev invariant
and the modular generalization of the Volume Conjecture discussed below led to the
definition of
certain power series $\Phi_\a^K(h)$ associated to a hyperbolic knot and a number $\a\in\Q/\Z$
that can be computed numerically in any given case.  Extensive numerical computations
for simple knots and simple rational numbers~$\a$ suggested that this power series not
only has algebraic coefficients, but that (up to a root of a unity and the square-root
of a number in the trace field~$F_K$ of the knot independent of~$\a$) its $n$th power
belongs to $F_{K,n}[[h]]$, where $n$ is the denominator of~$\a$ and $F_{K,n}=F_K(e^{2\pi i\a})$
the $n$th cyclotomic extension of~$F_K$.  Equivalently, $\Phi_\a^K(h)$ itself is the product
of a power series in $F_{K,n}[[h]]$ with the $n$th root of an element of $F_{K,n}^\times$.
Moreover, in each case studied the latter factor turned out to be the $n$th root of a
{\it unit}, and not just a non-zero number, of~$F_{K,n}$, and in the case of ``sister knots''
(like~$5_2$ and the $(-2,3,7)$-pretzel knot) having the same Bloch group class were the
same for both knots, even though the rest of the power series were completely different.
This led us, together with Frank Calegari, to conjecture and later to prove~\cite{CGZ},
that there was a canonical class of elements in cyclotomic extensions of arbitrary number
fields associated to elements of their Bloch groups, whether or not the fields arise
from topology.  Explicitly, to any number field~$F$ and any element~$\xi$ of the Bloch
group of~$F$ one can associate canonically defined elements of $U(F_n)/U(F_n)^n$ for
every~$n$, where $U(F_n)$ denotes the group of units (more precisely, of $S$-units
for some~$S$ depending on~$\xi$ but independent of~$n$) of the $n$th cyclotomic
extension~$F_n$ of~$F$.  Actually, two quite different constructions were given, one in
terms of an element of~$\B(F)$ and one in terms of an element in~$K_3(F)$, and work in
progress announced in~\cite{CGZ} suggests that there will be a generalization to
$\B_m(F)$ and $K_{2m-1}(F)$ for any~$m>2$.  The construction in terms of the Bloch group
is quite simple, although the proof that it gives units and is independent (up
to~$n$th powers) of all choices is long: if $\xi$ is represented by $\sum[z_i]\in\Z[F]$,
then the number $\prod D_{\z}(z_i^{1/n})$ is the product of an $n$th power in~$F_n$ with
an $S$-unit, and this is the unit we are looking for. Here $\z$ is a primitive $n$th root
of unity and $D_{\z}(x)=\prod_{k=1}^{n-1}(1-\z^kx)^k$ is the ``cyclic quantum dilogarithm''
function, which by a result of Kashaev, Mangazeev and Stroganov satisfies an analogue of
the 5-term relation of the classical dilogarithm.

\bigskip

\noindent{\bf $q$-series and Nahm's conjecture}

\smallskip\noindent
An unexpected consequence of the work on units just described was a proof of one direction
of a conjecture by the mathematical physicist Werner Nahm that had predicted an
extremely surprising connection between the Bloch group and the modularity of certain
$q$-hypergeometric series.  The simplest case of such a ``Nahm sum" is the infinite series
\be
\label{Nahm0}
F_{a,b,c}(q)\= \sum_{n=0}^\infty\frac{q^{\frac12an^2 +bn +c}}{(q)_n}
\qquad(a,b,c\in\Q,\; a>0),
\ee
where $(q)_n=(1-q)(1-q^2)\cdots(1-q^n)$ is the so-called quantum factorial. This function
is known to be modular (in~$\tau$, where $q=e^{2\pi i\tau}$) when $(a,b,c)$ is
$(2,0,-\frac1{60})$ or $(2,1,\frac{11}{60})$ by the famous Rogers-Ramanujan identities
and in a handful of other cases by classical results of Euler, Gauss and others.  It is very
rare that a $q$-hypergeometric series (meaning an infinite sum whose adjacent terms differ by
fixed rational functions of $q$ and $q^n$) is at the same time a modular function, and in fact
for the special series~\eqref{Nahm0} this happens only for seven triples~$(a,b,c)$,
as predicted by Nahm's conjecture and proved in~\cite{Z:dilogarithm}.  Nahm raised the
general question when a (multi-dimensional) $q$-hypergeometric series can be modular and,
motivated by examples coming from characters of vertex operator algebras, discovered a 
possible answer in terms of the Bloch group. Concretely, he generalized~\eqref{Nahm1} to
\be
\label{Nahm1} 
F_{a,b,c}(q)\= \sum_{n_1,\dots,n_N\ge0}
\frac{q^{\frac12n^tan\+b^tn\+c}}{(q)_{n_1}\cdots(q)_{n_N}}
\ee
for any~$N\ge1$, where $a$ is now a positive definite symmetric $N\times N$ matrix with
rational coefficients, $b$ a vector in~$\Q^N$, and $c$ a rational number. There is still no
complete ``if and only if'' conjecture predicting exactly when these Nahm sums are modular
functions, but Nahm gave a precise conjecture for a necessary condition and a partial
conjecture for the sufficiency.  It is the first part that was proved in~\cite{CGZ}, while
the correct formulation and proof of the converse direction is still an active research
subject. 

The modularity criterium that Nahm found depended on his observation that for any
solution $(z_1,\dots,z_N)$ of the system of equations
\be
\label{NahmEq}
 1\m z_i \= \prod_{j=1}^N z_j^{a_{ij}} \qquad(i=1,\dots,N)\,, 
\ee
the element $[z_1]+\cdots+[z_N]$ of~$\Z[\C]$ belongs to~$\B(\C)$. This is a direct consequence
of the symmetry of~$a$, because $\sum_i(z_i)\wedge(1-z_i)=\sum_{i,j}a_{ij}\,(z_i)\wedge(z_j)=0$. 
(This is the same argument as was used in Section~\ref{sec.5} for the corresponding statement
for the Neumann-Zagier equations, and applies more generally to all half-symplectic matrices,
as discussed below.)  The ``only if'' direction of Nahm's conjecture then says that
$F_{a,b,c}(q)$ can be modular only if this element of the Bloch group vanishes for the
unique solution of the Nahm equation having all $z_i\in(0,1)$.  The proof, given
in~\cite{CGZ}, uses both the results there about the units coming from Bloch elements
as described above and an asymptotic analysis of Nahm sums near roots of unity published
separately by the two of us.

\bigskip

\noindent{\bf Half-symplectic matrices and the Bloch group}

\smallskip\noindent
At the end of Section~\ref{sec.5}, we saw how the NZ equations lead to a ``half-symplectic
matrix,'' meaning the upper half $H=(A\,B)$ of a $2N\times2N$ symplectic matrix $\vsma ABCD$ 
over~$\Z$. To any such matrix we associate the system of polynomial equations
\be
\label{NZeq}
\prod_{j=1}^N z_j^{A_{ij}} \=
(-1)^{(AB^t)_{ii}\vphantom{y_{y_y}}}\,\prod_{j=1}^N (1-z_j)^{B_{ij}}
\qquad(i=1,\dots,N)\,.
\ee
This is a straight generalization of the original NZ equations in the topological setting
except possibly for the sign, but we checked in thousands of examples using Snappy~\cite{snappy}
that this is the right sign, and this could presumably be proved using the ``parity 
condition'' in~\cite{N:combinatorics}.  Another special case of~\eqref{NZeq} is the Nahm 
equation~\eqref{NahmEq}, at least when the matrix~$a$ is integral and even, the
half-symplectic matrix then being~$(1\,a)$ and the full symplectic matrix~$\vsma 1a01$.

For any solution~$z$ of~\eqref{NZeq}, the element $2\sum_{j=1}^N[z_j]$ belongs to the usual
Bloch group by the same argument as was used for Nahm sums. We can in fact divide by~2
and lift to an element $[H,z]$ of the extended Bloch group by setting
\be
\label{Hz}
[H,z] \= \sum_{j=1}^N [u_j,v_j] \+ [\xi,\xi'] \+ [-\xi,\,\xi'-\xi+\pi i]\,,
\ee
where $u_j$ and $v_j$ are arbitrary choices of logarithms of $z_j$ and~$1-z_j$, respectively, 
$\xi$ is defined as $\frac1\pi\,(Au-Bv)^t(Cu-Dv)$ for any completion $(C\,D)$ of~$H$ to a full
symplectic matrix, and $\xi'$ is any choice of logarithm of~$1-e^\xi$.
The facts that this is in the kernel of~$d:\Z[\wh\C]\to\WW(\C)$ and that its image modulo
extended 5-term relations is independent of all choices (at least modulo 8-torsion in the
Bloch group of the field generated by the~$z$'s) can be checked by direct computations which
are sketched in Section~6.1 of~\cite{GZ:kashaev}, together with a more precise form that
eliminates the torsion ambiguity.

We have the five following equivalence relations among pairs, each motivated by a change of
the choices made in the topological situation, that do not change this class:
\begin{itemize}
\item Stability: increase~$N$ by $N+1$, replace $A$ and~$B$ in~$H=(A\,B)$ by their direct
sums with $(1)$ and~$(0)$, respectively, and set $z_{N+1}=1$, corresponding in the topological
case to adding a degenerate simplex to a 3-manifold triangulation.
\item Changing the equations: multiply $H$ on the left by an element of~$\GL_N(\Z)$ without
  changing the $z$'s.  This corresponds to replacing the $N$ relations~\eqref{NZeq} by
  multiplicative combinations of them in an invertible way.
\item  Renumbering: multiply~$H$ on the right  by an $N\times N$ permutation matrix, and
  permute the $z_j$'s by the same matrix, corresponding to a renumbering of the simplices of
  a triangulation. 
\item  New shape parameters: for each $j=1,\dots,N$, multiply the $N\times2$ matrix
  $(A_j\,B_j)$ (where $A_j$ and $B_j$ denote the $j$th columns of $A$ and~$B$, respectively)
  by a power of the element $\sma0{-1}1{-1}$ of order~3 in~$\SL_2(\Z)$, and replace $z_j$
  correspondingly by $z_j$, $z_j'=1/(1-z_j)$, or $z_j''=1/(1-z_j)$.
\item Algebraic 2--3 Pachner moves: remove two columns of $A$ and the same two columns of
  $B$ and replace them by 3 new columns that are specific $\Z$-linear combinations,
  simultaneously replacing $N$ by $N+1$ and changing two of the $z_j$ to three others in
  such a way that the corresponding change of $[H,z]$ is a 5-term relation.
  The explicit formulas were first written down in the special case corresponding to the
  Nahm sums~\eqref{Nahm1} by Sander Zwegers in an unpublished 2011 conference talk and were
  then given for abritrary symplectic matrices in Equation (3-27) of~\cite{DG}. This
  corresponds to stabilizing $H$ three times and then multiplying it on the left by a specific 
  element of~$\Sp_{10}(\Z)$, and then unstabilizing three times.
\end{itemize}
This gives us a new abelian group that maps to the extended Bloch group, namely the set of
all pairs $(H,z)$ as above modulo these equivalence relations, with addition given by
direct sum. In fact this map is an isomorphism, meaning that any element of the Bloch group
can be realized by some half-symplectic matrix and solution of the coresponding generalized
Neumann-Zagier equations and that any 5-term relation can be lifted to one coming from an
algebraic 2--3 Pachner move. A more complete discussion is given in Section~6.1
of~\cite{GZ:kashaev} (full details will be given later), while Section~6.3 of the same paper
shows how to attach Nahm sum-like $q$-series to arbitrary half-symplectic matrices.

\bigskip 

\noindent{\bf From the Kashaev invariant to quantum modular forms}

\smallskip\noindent 
Nahm's conjecture already highlighted a connection between half-symplectic matrices and 
questions of modularity, but there are other and more direct connections between hyperbolic 
3-manifolds and the modular group~$\SL_2(\Z)$ that we now describe.

At the end of Section~\ref{sec.6} we discussed Kashaev's volume conjecture and its 
refinement~\eqref{arithmVolConj}.  That statement in turn was generalized in~\cite{Z:QMF}
on the basis of numerical computations to a conjectural asymptotic formula having a strong
modular flavor. To state it, we first note that the Kashaev invariant $\la K\ra_n$ of a
knot~$K$ can be generalized to a function $J^K:\Q/\Z\to\Qbar$ whose value at $-1/n$ for any
$n\ge1$ is $\la K\ra_n$ and which is $\text{Gal}(\Qbar/\Q)$-equivariant.
Then the conjectural generalization of~\eqref{arithmVolConj} is the statement that
\be
\label{QMCb}
J^K\Bigl(\frac{an+b}{cn+d}\Bigr) \;\sim\; (cn+d)^{3/2} \;
e^{\Vol_\C(K)(n+d/c)/2\pi i}\; \Phi^K_{a/c}\Bigl(\frac{2 \pi i}{c(cn+d)}\Bigr)\; J^K(n)
\ee
for every matrix $\sma abcd\in\SL_2(\Z)$ as $n$ tends to infinity through either 
integers or rational numbers with bounded denominator, with~\eqref{arithmVolConj} being
the special case when $\sma abcd=\sma 0{-1}10$ and $n$ is integral.  Here $\Phi^K_\a(h)$
for $\a\in\Q/\Z$ is a power series that is conjectured to be the one constructed in~\cite{DG2}
and discussed at the end of Section~\ref{sec.6}.

In~\cite{GZ:kashaev}, this modularity conjecture was verified experimentally for a few knots 
to many terms and to a high degree of precision, and was also successively refined in
several different directions, the final statement being the existence of a whole matrix
$\J^K$ of $\Qbar$-valued functions on~$\Q/\Z$ (generalized Kashaev invariants) which
conjecturally has much better modularity properties than the original scalar function~$J^K$.
Explicitly, \eqref{QMCb} lifts to a similar statement with $J^K$ replaced by the
matrix~$\J^K$ and the completed formal power series
$\wh\Phi^K_{a/c}(h)=e^{\Vol_\C(K)/2\pi ic^2h}\,\Phi^K_{a/c}(h)$ by a matrix $\wh\bPhi^K_{a/c}(h)$
of completed formal power series acting by right multiplication. 
The rows and columns of these matrices are indexed by the bounded parabolic
flat connections, or equivalently by an index~0 (trivial connection) and indices~$1,\dots,r$
corresponding to the solutions of the NZ equation for a triangulation of the knot complement,
with the original scalar-valued functions $J^K$ and $\Phi^K$ being the $(0,1)$ and $(1,1)$ 
entries of $\J^K$ and $\bPhi^K$, respectively.  The really new aspect is that, by replacing
the original scalar functions by matrices, we obtain a matrix of completed formal power
series in~$h$ that (conjecturally, like everything else in this story) extend to
real-analytic functions on the 
positive and negative real line and in fact to holomorphic functions on the two cut planes
$\C\ssm(-\infty,0]$ and $\C\ssm[0,\infty)$. This discovery, which arises through the
possibility of associating matrix-valued $q$-series to the knot~\cite{GZ:qseries}, gives
rise to the new concept of ``holomorphic quantum modular form" that then turned out to
appear also in many other situations, including various known modular objects like mock
modular forms or Eisenstein series of odd weight on the full modular group.

Finally, we mention that the new generalized Kashaev invariants have beautiful arithmetic
properties generalizing the known property~\cite{Hab} that the original Kashaev invariant
belongs to the so-called Habiro ring~$\calH=\varprojlim\Z[q]/(q)_n\,$.  The results
of~\cite{GZ:kashaev} and~\cite{GZ:qseries} suggest that there should be a Habiro
ring~$\calH_F$ associated to any number field~$F$ in which the generalized Kashaev invariants
take their values and which is graded by the Bloch group of~$F$. (The latter property is
invisible in the classical case since $\B(\Q)\otimes\Q=\{0\}$.)  We are currently working
on this jointly with Peter Scholze, and already have a candidate for~$\calH_F$, as well as
a partial lifting of the algebraic units of~\cite{CGZ} to formal power series with
Habiro-like properties.

\medskip 





\bibliographystyle{plain}
