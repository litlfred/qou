---
doc_id: arxiv-math-0305275v1
doc_title: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds"
section_id: sec-006-corollaries
section_title: "Corollaries"
section_number: null
pages: 34-38
source_pdf: 0305275v1.pdf
source_sha256: 9b356a9d716a0d3e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.694
doc_brief: "Hyperbolic volume of representations of fundamental groups of cusped 3-manifolds — Let W be a compact manifold and let ρ be a representation of its fundamental group into PSL(2, C)."
---
\label{s cor}

In this section we prove some corollaries that can be useful 
for studying hyperbolic $3$-manifolds.



First we show how
from Theorem~\ref{t ug} one gets a proof of Mostow's rigidity
for non-compact manifolds (see~\cite{P} and~\cite{BCS} for a more
general statement and a different proof).

\begin{teo}[Mostow's rigidity for non-compact manifold]\label{t mstw}
Let $f:M\to N$ be a proper map between two orientable non-compact,
complete hyperbolic $3$-manifolds of finite volume. Suppose that
\vol(M)={\rm deg}(f)\vol(N).
Then $f$ is properly homotopic to a locally isometric covering with the
same degree as $f$.   
\end{teo}
\proof 
Let $\omega$ be the volume form of $N$. For $X=M,N$ let
$\Gamma_X\cong \pi_1(X)$ be the subgroup of ${\rm PSL}(2,\M C)$ such that  
$X=\M H^3/\Gamma_X$.
Let $f_*$ denote both the map induced in homology and the 
representation $f_*:\pi_1(M)\to{\rm PSL}(2,\M C)$. 

First assume that the lift $\wt f:\wt M\to\wt N$ has the cone-property
on the cusps. This implies that $\wt f$ is a pseudo-developing map for $f_*$.
Since $f_*[M]=\deg(f)[N]$ we have
$$
\begin{array}{l}
\vol(M)=\deg(f)\cdot\vol(N)=\langle\omega,\deg(f)[N]\rangle\\
=\langle\omega,f_*[M]\rangle=\langle f^*\omega,[M]\rangle=\vol(f_*).
\end{array}$$

Thus, by Theorem~\ref{t ug} there exists an isometry $\f$ such that 
for any $\gamma\in\Gamma_M$
$$f_*(\gamma)=\f\circ\gamma\circ\f^{-1}.$$
As $\wt M\cong \M H^3$, we consider the 
isometry \f\ as an $f_*$-equivariant map from
$\wt M$ to $\M H^3$. Namely, for any $x\in\M H^3$ and
$\gamma\in\Gamma_M$
$$\f(\gamma(x))=f_*(\gamma)(\f(x)).$$
It follows that $\f$ projects to a locally isometric covering 
$\f:M\to N$ and the convex combination from $\wt f$ to $\f$ projects to
a proper homotopy from $f$ to $\f$. 
{Since the degree of a map is invariant under proper homotopies, then 
$\deg(\f)=\deg(f)$.

We prove now that $f$ is always properly homotopic to a map whose lift
has the cone property on the cusps.
Let $\wt f$ be a lift of $f$. 
For each cusp $N_p=P_p\times[0,\infty)$ let $f_p=\wt
f|_{P_p\times\{0\}}$. Since $f$ is proper it follows that $\wt
f(N_p\times\{\infty\})$ is well-defined. 
Let $F_p:N_p\times[0,\infty)\to\M H^3$ be the map
obtained by coning $f_p$ to $\wt f(N_p\times\{\infty\})$ along geodesic
rays. Let $\wt {f'}$ be the map obtained by replacing, on each cusp $N_p$,
the map $\wt f|_{N_p}$ with the map $F_p$. The map $\wt{f'}$ obviously
has the cone-property on the cusps, and projects to a map 
$f':M\to N$. Moreover, the convex combination from $\wt f$ to
$\wt{f'}$ projects 
to a proper homotopy between $f$ and $f'$.  
\qed

From Theorem~\ref{t ug}, Theorem~\ref{t mstw}, Corollary~\ref{c df}
 and the corresponding statements for compact manifolds, we get the following
statement.
\begin{teo}
  Let M be a complete, oriented hyperbolic $3$-manifold of finite
  volume. Let $\Gamma\cong\pi_1(M)$ be the sub-group of ${\rm PSL}(2,\M C)$
  such that $M=\M H^3/\Gamma$. 
  Let $\rho:\Gamma\to$ {\rm PSL}$(2,\M C)$ be a representation.
  Then $|\vol(\rho)|\leq|\vol(M)|$ and equality holds if and only if
  $\rho$ is discrete and faithful.
\end{teo}

\begin{cor}
Let $M$ be an atoroidal, irreducible, ideally triangulated
$3$-manifold. Let $\z\in\{\M C\setminus\{0,1\}\}^n$ be a solution
of the hyperbolicity equations such that 
$\vol(\z)\neq 0$. Then $M$ is hyperbolic. 
\end{cor}
\proof
This immediately follows from Corollary~\ref{c vg} and 
Thurston's Hyperbolization Theorem~(\cite{Th2}).
\qed 

In~\cite{F3} the notion of {\em geometric} solution of the
hyperbolicity equations is introduced.
Roughly speaking, a geometric solution of the hyperbolicity equations 
for a given ideal triangulation $\tau$ is a choice of moduli 
which is compatible with a global hyperbolic structure on $M$.
In~\cite{F3} it is shown that 
not each solution of hyperbolicity equations is geometric 
(see~\cite{F3} for more details on
algebraic and geometric solutions of hyperbolicity equations).


\begin{cor}\label{c ac}
Let $M$ be a complete hyperbolic $3$-manifold of
finite volume and let $\tau$ be an ideal triangulation of $M$. 
If there exists a solution $\z\in\{\M C\setminus\{0,1\}\}^n$ 
of the hyperbolicity equations for $\tau$, 
then there exists a solution
  $z'$ of hyperbolicity equations that is geometric. Moreover such a
  solution is the one of maximal volume. 
\end{cor}
\proof
Consider a natural straightening of $\tau$, and let $\z'$ be the moduli
induced on $\tau$. By Proposition~\ref{p so}, we have only to prove
that the moduli are not in 
$\{0,1,\infty\}$. Suppose that there is a degenerate tetrahedron
$\Delta_i$. Then
at least two vertices, say $v$ and $w$, of $\Delta_i$  coincide. 

Let $\rho(\z)$ be the holonomy
relative to \z\ and let $D_\z$ be a developing map that is also a
pseudo-developing map for $\rho(\z)$. Then $D_\z$ maps $\Delta_i$ into a
tetrahedron of modulus $z_i$. But by hypothesis, $\z$ is in $\{\M
C\setminus\{0,1\}\}^n$ and so the vertices of $\Delta_i$ are four
distinct points. The last assertion follows from Corollary~\ref{c df}
and Theorem~\ref{t ug}\qed

Corollary~\ref{c ac} tells that, 
once one has a solution $\z\in\{\M C\setminus\{0,1\}\}^n$
of the hyperbolicity equations for a
triangulation $\tau$ of a cusped manifold $M$, 
in order to know if $M$ admits a complete hyperbolic structure of
finite volume, 
it suffices to study the solution of
maximal volume. Namely, if one succeeds to prove that the solution of
maximal volume is geometric, then $M$ is hyperbolic. Conversely, if
one proves that such a solution is not geometric (for example if its
holonomy is not discrete) then $M$ cannot be hyperbolic, and this does
not depend on the chosen triangulation. 

As an example of application
of Corollary~\ref{c ac} we give the following:


\begin{cor}\label{c zeron}
Let $M$ be a cusped $3$-manifold 
equipped with  an ideal triangulation  $\tau$. 
If there exists a solution $\z\in\{\M C\setminus\{0,1\}\}^n$ 
of the hyperbolicity equations for $\tau$, and all the solutions have
zero volume, then $M$ is not hyperbolic. 
\end{cor}

We notice that the hypothesis that all the solutions have
zero volume can be replaced by requiring that the volumes are {\em too small}.
This is because the set of the volumes of the hyperbolic manifolds 
is bounded from below by a positive constant. 

Finally, we obtain another proof of the well-know fact that no
Dehn filling of a Seifert manifold is hyperbolic.
\begin{cor}\label{c fr}
  Let $M$ be a $3$-manifold such that $||(M,\partial M)||=0$ and let $N$
  be a Dehn filling of $M$. Then $N$ is not hyperbolic. 
\end{cor}
\proof Suppose the contrary. Let $\rho$ be the holonomy of the
hyperbolic structure of $N$. From Theorem~\ref{t sv} it follows that
$\vol(\rho)=0$, but from Proposition~\ref{p f2} and 
Corollary~\ref{c nat} it follows that $\vol(\rho)=$ $\vol(N)>0$.\qed
