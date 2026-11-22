---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.94
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
Hyperbolic Reidemeister torsion, \emph{i.e.} the Reidemeister torsion
twisted by the adjoint representation associated to an irreducible
representation into $\SL$, was first introduced by D. Johnson in
unpublished notes~\cite{Johnson}. Later it was considered by
E. Witten~\cite{Witten:1991} as a symplectic volume form on the moduli
space of $\SU$-flat connections over two--dimensional surfaces and
developed to the case for closed three--manifolds by L.~Jeffrey and
 J.~Weitsman~\cite{JeffreyWeitsman:1993} and
J. Park~\cite{JPark:1997}. Furthermore, J. Porti~\cite{Porti:1997} applied the Reidemeister torsion
twisted by the adjoint representation to the study of three--dimensional hyperbolic manifolds eventually with cusps via $\SL$-character varieties.

Let $M$ be a hyperbolic three--dimensional manifold with
cusps. We consider the character variety $X(M)$ of $M$, which is in a
sense the ``algebraic quotient" of the representation space
$\mathrm{Hom}\big(\pi_1(M), \SL\big)$ under the action by conjugation. This set
has the structure of a complex algebraic affine set as it is proved in~\cite{CS:1983, LubotzkyMagid85}). The
\emph{geometric component} of $X(M)$ is the connected component which
contains the discrete and faithful representation of the complete
hyperbolic structure.

The construction of the hyperbolic torsion uses $\SL$-representations
whose conjugacy classes lie in the geometric component.
In general, it is not easy to compute the hyperbolic torsion directly from the definition because the twisted complex involved for the computation is not acyclic is that case.
But for hyperbolic knot exteriors, we can carry out the computation of the 
hyperbolic torsion by using the derivative of {\it the twisted Alexander invariant}
given by second author's work~\cite{YY:Fourier}. Such formula gives a link between the hyperbolic torsion, which is a ``non--acyclic" Reidemeister torsion, and another one which has the advantage to be computed using an acyclic complex. 
We call this procedure the {\it derivative formula} of the twisted Alexander invariant
and we use the terminology {\it non--abelian Reidemeister torsion} instead of the hyperbolic Reidemeister torsion
following author's previous works~\cite{JDFourier, DuboisVuYam09:RTorsionTwistKnots}.


This paper provides the generalized framework to compute the non--abelian Reidemeister torsion of a hyperbolic three--dimensional manifold with cusps 
by using the derivative of the twisted Alexander invariant with multivariables.
We proceed from the technical conditions required by our framework to the computation procedure of 
the non--abelian Reidemeister torsion.
Our framework requires the following three kinds of assumptions:
\begin{itemize}
\item topological conditions on the hyperbolic three--dimensional manifold $M$ whose boundary consists in the disjoint union of $b$ two--dimensional tori: $$\partial M = \bigcup_{\ell =1}^b T_\ell^2;$$
\item conditions on the surjective homomorphism $$\varphi\colon \pi_1(M) \to \ZZ^n = \langle t_1, \ldots, t_n \; |\; t_it_j = t_jt_i \;(\forall\, i,j)\,\rangle$$ which gives the variables of the twisted Alexander invariant and;
\item conditions on an irreducible $\SL$-character $\rho\colon \pi_1(M) \to \SL$ which lies in the geometric component of the character variety.
\end{itemize}
These assumptions are referred to as the symbols $(A_M)$,
$(A_\varphi)$ and $(A_\rho)$.  Under these assumptions, we show the following four results:
\begin{itemize}
\item the non--abelian Reidemeister torsion $\RTors{M}{\smallbm{\lambda}}(\rho)$ and the twisted Alexander
  invariant $\PolyTors{M}{\otAd{\varphi}{\rho}}(t_1, \ldots, t_n)$ are well--defined;
\item the derivative of the twisted Alexander invariant with
  multivariables gives the non--abelian Reidemeister torsion. More precisely, we have:
  \[
  \lim_{t_1, \ldots, t_n \longrightarrow 1}\; 
    \frac{
      \PolyTors{M}{\otAd{\varphi}{\rho}}(t_1, \ldots, t_n)
    }{
      \prod_{\ell = 1}^b \big( t_1^{a_1^{(\ell)}} \cdots t_n^{a_n^{(\ell)}} - 1 \big )
    } 
    = (-1)^b \cdot \RTors{M}{\smallbm{\lambda}}(\rho).
    \]
    Here $b$ denotes the number of tori components of the boundary $\partial M$ of $M$ and $\varphi\big(\pi_1(T_\ell^2)\big) = \big\langle t_1^{a_1^{(\ell)}} \cdots
  t_n^{a_n^{(\ell)}}\big \rangle$ for some positive integers $a_1^{(\ell)}, \ldots, a_n^{(\ell)}$;
  \item under some technical conditions on the representations $\varphi$ and $\rho$, we prove that the twisted Alexander invariant $\PolyTors{M}{\otAd{\varphi}{\rho}}(t_1, \ldots, t_n)$, which a priori lies in the fraction field $\CC(t_1, \ldots, t_n)$, is in fact  contained in $\CC[t_1^{\pm 1}, \ldots, t_n^{\pm 1}]$ (up to a factor $t_1^{m_1} \cdots t_n^{m_n}$ for some integers $m_1, \ldots, m_n$), and;
\item we give the computation example of the non--abelian Reidemeister
  torsion for the Whitehead link exterior by using this generalized
  formula.
\end{itemize}

The advantage of our generalization of the derivative formula lies in
the fact that we can obtain a sequences of hyperbolic knot exteriors
by Dehn filling a hyperbolic link exterior with some solid tori.
Since twist knots are obtained by Dehn filling the Whitehead link
exterior, the computations result of the non--abelian Reidemeister
torsion for the Whitehead link exterior is useful to observe the
asymptotic behavior of the non--abelian Reidemeister torsions for the
twist knot exteriors, as observed in~\cite{DuboisVuYam09:RTorsionTwistKnots} by
V. Huynh and the authors.

It is expected that the twisted Alexander invariant in our framework
has other properties than the derivative formula.  We also prove a duality formula (with sign) for the twisted Alexander invariant which can be compared with the well--known symmetry property of the usual Alexander polynomial. More precisely, if $M$ is a link exterior $M = E_L = S^3 \setminus N(L)$, then
the polynomial torsion of $E_L$ satisfies the following formula:
\[
    \PolyTors{E_L}{\otAd{\varphi}{\rho}}(t^{-1}) 
      =(-1)^b \PolyTors{E_L}{\otAd{\varphi}{\rho}}(t). 
\]
