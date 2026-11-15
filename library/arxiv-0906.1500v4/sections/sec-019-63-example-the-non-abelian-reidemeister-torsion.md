---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-019-63-example-the-non-abelian-reidemeister-torsion
section_title: "Example: the non-abelian Reidemeister torsion of the Whitehead link exterior"
section_number: 6.3
pages: 19-20
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 1.0
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
\label{ex:Whitehead}

We apply Corollary~\ref{cor:DerFormula_one _variable} to the
polynomial torsion $\PolyTors{E_L}{\otAd{\varphi}{\rho}}(t_1, t_2)$ of
the Whitehead link exterior $E_L$ (see Fig.~\ref{fig:WhiteheadLinkMeridians}).  First we substitute $t$ into both
variables $t_1$ and $t_2$ in Equation~$(\ref{eqn:PolyTorsion_WL})$.  The
resulting homomorphism $\varphi_{(1,1)}$ corresponds to the induced
homomorphism $\pi_1(E_L) \to \pi_1(S^1)$ by the fibered structure of
$E_L$.  The dual surface is the fiber and is also a Seifert surface
for $L$.  Thus:
\[
\PolyTors{E_L}{\otAd{\varphi}{\rho}}(t,t) = \tau_0 \cdot
\frac{(t-1)^2}{t^3} \left( -2xyv t^2 + x^2 t(t+1)^2 + y^2 t (t+1)^2 -
  (t+1)^4 \right).
\]

Multiplying $(t-1)^{-2}$ and taking the limit for $t$ goes to $1$, we
obtain the hyperbolic torsion (the non--abelian Reidemeister torsion):
\begin{equation}\label{eqn:Whitehead}
  \RTors{E_L}{\smallbm{\lambda}}(\rho_{x, y, v}) 
  = \tau_0 \cdot 
  \left( 4(x^2+y^2)-16-2xyv \right).
\end{equation}
Since a lift of the holonomy representation is irreducible and the
traces of meridians are $\pm 2$, Equation~$(\ref{eqn:Whitehead})$ is also
valid at $x = \pm 2$.  Moreover the points $(\pm 2, \pm 2, 1 +
\sqrt{-1})$ and $(\pm 2, \pm 2, 1 - \sqrt{-1})$ correspond to lifts of
the holonomy representation and its complex conjugate.  When we
substitute $(\pm 2, \pm 2, 1 + \sqrt{-1})$ and $(\pm 2, \pm 2, 1 -
\sqrt{-1})$ into $(x, y, v)$, we have the following values of the
hyperbolic torsion (the non--abelian Reidemeister torsion) for the Whitehead link exterior and
its holonomy representation $\rho_0$ and the complex conjugate $\bar
\rho_0$
\[
\left\{\RTors{E_L}{\smallbm{\lambda}}(\rho_0),
\RTors{E_L}{\smallbm{\lambda}}(\bar \rho_0) \right\} = \left\{\tau_0 \cdot 8(1 \mp
\sqrt{-1})\right\}.
\]


\section{$\PolyTors{M}{\otAd{\varphi}{\rho}}$ is a polynomial}
\label{section:poly}

The torsion $\PolyTors{M}{\otAd{\varphi}{\rho}}$ is an element in the
fraction field $\CC(t_1, \ldots. t_n)$ by definition of the
Reidemeister torsion.  But actually, under a technical condition on
the representations $\rho \colon \pi_1(M) \to \SL$ and $\varphi \colon
\pi_1(M) \to \ZZ^n$, this torsion is in fact contained in $\CC[t_1,
\ldots, t_n]$, up to a factor $t_1^{m_1} \cdots t_n^{m_n}$ for some
integers $m_1, \ldots, m_n$.  This result is obtained by a cut and
paste argument by using the Multiplicativity Lemma for torsions.
This divisibility problem for link exteriors in $S^3$ has been also investigated by
Kitano and Morifuji~\cite{KitanoMorifuji05:divisibility} and Wada~\cite{Wada94}.


\subsection{Dual surfaces of $\varphi$ with rank one}\label{subsec:dual}

Using the universal coefficient theorem, a homomorphism $\varphi
\colon \pi_1(M) \to \ZZ$ can be regarded as a cohomology class in
$H^1(M, \ZZ)$, and its Poincar\'e dual $PD(\varphi)$ lies in
$H_2(M;\ZZ)$. Each representative of $PD(\varphi)$ consists of proper embedded
surfaces, \ie, embedded surfaces whose boundary is contained in $\bord
M$.  By Turaev~\cite{turaev:homol_estim}, we can choose proper
embedded surfaces satisfying that the complement $M \setminus S$ of $S$ in $M$ is connected
as a representative of $PD(\varphi)$.  We let $S_\varphi$ denote such 
representative surfaces.

In the case of the Reidemeister torsion with multivariable $(t_1,
\ldots, t_n)$, if we substitute $t_\ell = t^{a_\ell}$ for all $\ell$, then we have the homomorphism $\varphi_{(a_1, \ldots, a_n)}
\colon \pi_1(M) \to \ZZ$.  Moreover if $(a_1, \ldots,
a_n)$ are relatively prime positive integers then the composition $\varphi_{(a_1, \ldots, a_n)}$ satisfies assumption
$(A_\varphi)$.  When we regard $\varphi_{(a_1, \ldots, a_n)}$ as an
element in $H^1(M;\ZZ)$, we let $S_{(a_1, \ldots, a_n)}$ denote a
representative of $PD(\varphi_{(a_1, \ldots, a_n)})$ such that $M
\setminus S_{(a_1, \ldots, a_n)}$ is connected.
