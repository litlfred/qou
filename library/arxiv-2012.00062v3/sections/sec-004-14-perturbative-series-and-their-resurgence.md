---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-004-14-perturbative-series-and-their-resurgence
section_title: "Perturbative series and their resurgence"
section_number: 1.4
pages: 6-8
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.96
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
\label{sub.pert}

We now discuss the resurgence properties of the asymptotic
expansion of the state-integral $Z_M(u;\tau)$. Once we fix an
integral presentation of $Z_M(u;\tau)$, the critical points of
the integrand are described by an affine curve $S$ defined
by a polynomial equation
\begin{equation}
\label{S}
S: p(x,y)=0 \,.
\end{equation}
We denote by $\calP$ the labeling set of the branches
$y=y_\s(x)$ of $S$. The perturbative expansion of the
state-integral  has the form
\begin{equation}
  \label{Phix}
  \Phi(x,y;\tau) =
  \re^{\frac{V(u,v)}{2\pi \ri \tau}} \varphi(x,y;\tau), \qquad
  \varphi(x,y;\tau) \in \frac{1}{\sqrt{\ri\delta}} \BQ[x^\pm, y^\pm,
  \delta^{-1}][[2\pi \ri \tau]]
\end{equation}
where $V: S^* \to \BC/(2\pi \ri)$, $S^*$ is the exponentiated defined
by $p(x,y)=0$ with $x=\re^{u}$, $y=-\re^{v}$ and
$\delta \in \BQ(x,y)$ is the so-called 1-loop invariant.  
The asymptotic series $\varphi(x,y;\tau)$ satisfies
$\varphi(x,y;0) = 1$.  The 8-th root of unity that appears as a
prefactor in $\phi(x,y;\tau)$ exactly matches with one appearing in
the asymptotics of the Kashaev invariant noticed
in~\cite[Sec.1]{GZ:kashaev}. After choosing local branches, we define
the vector
$\varphi(x;\tau)=(\varphi_\s(x;\tau))_{\s\in\calP} =
(\varphi(x,y_\s(x);\tau))_{\s \in \calP}$ of asymptotic series.
Recall the vector of holomorphic blocks $B(x;q)$ from~\eqref{ZM-desc}.
We now discuss the relation between the asymptotics of
$B(x;q)$ when $q=\re^{2\pi \ri \tau}$ and $\tau$ approaches zero (in
sectors) and the Borel resummation $s(\Phi)$ of the vector of power
series $\Phi(x;\tau)$.

The next conjecture summarizes the singularities of $\Phi(x;\tau)$
in the Borel plane, the relation between the asymptotics of the
holomorphic blocks with the Borel resummation $s_\th(\Phi)(x;\tau)$
as well as the properties of the Stockes automorphism matrices
$\ms{S}$, whose detailed definition is given in Section~\ref{sec.borel}.

\begin{conjecture}
  \label{conj.asy}
  \rm{(a)} The singularities of $\Phi_{\s}(x;\tau)$ in the Borel plane
  are a subset of
  \begin{equation}
    \label{Phising}
    \{ \iota_{\s,\s'}^{(\ell,k)} \,\, |
    \,\, \s' \in \calP, \,\, k, \ell \in \BZ, \,\, k=O(\ell^2) \} 
  \end{equation}
  where
  \begin{equation}
    \label{iota}
    \iota_{\s,\s'}^{(\ell,k)} = \frac{V(\s) - V(\s')}{2\pi\ri} +
    2\pi\ri k + \ell \log x \qquad (\s,\s' \in \calP, \,\, k, \ell \in \BZ) \,.
  \end{equation}
  In particular, the set of trans-series is labeled by three indices,
  $\sigma \in \calP$ and $k, \ell \in \IZ$, and they are of the form
  $\Phi_\s(\tau) \tq^k \tx^\ell$.  \newline
  \rm{(b)} On each ray $\rho$ in the complement of the singularities
  of $\Phi(x;\tau)$ in Borel plane, there exist a matrix
  $M_\rho(\tx;\tq)$ with entries in $\BZ[\tx^{\pm}][[\tq]]$ such that

  \begin{equation}
    \label{abrelx}
    \Delta(\tau) B(x;\tau) = M_\rho(\tx;\tq) s_\rho(\Phi)(x;\tau) \,. 
  \end{equation}

  \rm{(c)} The Stokes matrices $\ms{S}^{+}(x,q)$, $\ms{S}^{-}(x,q^{-1})$
  are given by
  \begin{equation}
  \label{2S}
  \ms{S}^{+}(x;q) \stackrel{\cdot}=
  W_{-1}(x^{-1};q^{-1})\cdot W_{-1}(x;q)^T, \qquad
  \ms{S}^{-}(x;q^{-1}) \stackrel{\cdot}= W_{-1}(x;q)\cdot W_{-1}(x^{-1};q^{-1})^T
  \end{equation}
  where $\stackrel{\cdot}=$ means equality up to multiplication on the
  left and on the right by a matrix in $\GL(r,\BZ[x^\pm])$.  \newline
  \rm{(d)} The Stokes matrix $\ms{S}$ uniquely determines the Stokes
  matrices at each Stokes ray, and the Stokes constants are integers
  corresponding to the Donaldson--Thomas invariants in
  \cite{KS,KS:wall-crossing,KS:stability} and the BPS degeneracies 
  in \cite{gmn,gmn2}.  \newline
  \rm{(e)} The Stokes matrices satisfy the inversion relation
    \begin{equation}
    \label{Ssym}
    \ms{S}^+(x;q)^T \ms{S}^-(x^{-1};q) = \md{1}\,.
  \end{equation}
\end{conjecture}

The Stokes automorphism matrix has an interesting
connection to physics which we now discuss.  Given a hyperbolic knot
$K$ in $S^3$, one can construct a three-dimensional $\mc{N}=2$
supersymmetric theory $T_M$ associated to the knot complement
$M = S^3\backslash K$ \cite{DGG1} (see also~\cite{ter-yama}), whose
BPS invariants are conjectured to coincide with the Stokes constants
of $s(\Phi)(x;\tau)$.  This conjecture can be made more precise in the
following manner. The BPS invariants of $T_M$ are encoded in the
3D-index $\mc{I}_{K}(m,e)(q)$ labeled by two integers $(m,e)$ called
magnetic and electric fluxes respectively~\cite{DGG1}. One can further
define the 3D-index in the fugacity basis (also known as the rotated
index) by~\cite{DGG2}
\begin{equation}
  \text{Ind}^{\text{rot}}_{K}(m,\zeta;q) =
  \sum_{e\in\IZ}\mc{I}_{K}(m,e)(q)\zeta^e.
\end{equation}
The 3D-index is a topological invariant of hyperbolic 3-manifolds with
at least one cusp (see~\cite{GHRS}).  And it can be evaluated using
holomorphic blocks $B_{K}^\alpha(x;q)$ by \cite{Beem}
\begin{equation}
  \text{Ind}_{K}^{\text{rot}}(m,\zeta;q) = \sum_{\alpha}
  B_K^\alpha(q^{m/2}\zeta;q)B_K^\alpha(q^{m/2}\zeta^{-1};q^{-1}).
  \label{eq:IndB}
\end{equation}




We have observed the following relation between the Stokes
matrix and the rotated 3D-index, and have proven it for the case of
the $\knot{4}_1$ and $\knot{5}_2$ knots using the explicit formulas
for the Stokes matrices.

\begin{conjecture}
  \label{conj.S3D}
  For every hyperbolic knot $K$, we have
  \begin{equation}
    \ms{S}^+(x;q) \stackrel{\cdot\cdot}=
    \left(\text{Ind}^{\text{rot}}_K(j-i,q^{\frac{j+i}{2}}x;q)
    \right)_{i,j=0,1,\ldots}
    \label{eq:SInd}
  \end{equation}
  where $\stackrel{\cdot\cdot}=$ means equality up to multiplication
  on the left and on the right by a matrix in $\GL(r,\BZ(x,q))$.  In
  particular, we find
  \begin{equation}
    \label{S3Dx}
    \ms{S}^+_{\s_1\s_1}(x;q) =
    \text{Ind}^{\text{rot}}_{K}(0,x;q)
    \,,
  \end{equation}
  where the equality is exact.  This holds true for the $\knot{4}_1$
  and the $\knot{5}_2$ knots.
\end{conjecture}

One consequence of~\eqref{abrelx} is that (after multiplying both
terms of~\eqref{abrelx} by the inverse of $M_R(\tx;\tq)$), we can
express the Borel resummation of the factorially divergent series
$\Phi(\tau)$ in terms of descendant state-integrals which are
holomorphic functions in the cut plane
$\BC'=\BC\setminus (-\infty,0]$.

Another consequence of the $q$-holonomic module defined by the
annihilation ideal $\calI_M$ is a refinement of the $\Ahat$-polynomial
of a knot as well as a new $\Bhat$-polynomial whose classical limit is
new.  The refinement comes in the form of a new variable $q^m$ where
$m$ is the descendant variable, whose geometric meaning is not
understood but might be related to some kind of quantum K-theory, or
perhaps related to the Weil-Gelfand-Zak transform of~\cite{AK:new}.
This refinement does not seem to be directly related to other refinements
of the $\Ahat$-polynomial, as those considered in
\cite{av-knots,super,GLL:HOMFLY}. At any rate, the $q$-holonomic ideal
$\calI_M$ contains unique
polynomials $\Ahat_M(S_x,x,q^m,q) \in \calW$ and $\Bhat_M(S_m,q^m,x,q)$
(of lowest degree, content-free) that annihilate the functions
$z_{M,m,k}(u;\tau)$ in the variables $(m,x)$.

\begin{conjecture}
  \label{conj.ann}
  When $M=S^3\setminus K$ is the complement of a knot $K$, then
  \begin{itemize}
  \item[(a)] $\Ahat_M(S_x,x,1,q)$ is the homogeneous
    $\Ahat$-polynomial of the knot~\cite{Ga:AJ} and
    $\Ahat_M(S_x,x,1,1)$ is the $A$-polynomial of the knot with
    meridian variable $x^2$ and longitude variable $S_x$~\cite{CCGLS}
  \item[(b)] $\Bhat_M(y,x,1,1)$ is the defining polynomial of the curve
    $S$.
  \end{itemize}
\end{conjecture}

In theorems~\ref{thm.41c} and~\ref{thm.52c} we prove the following.

\begin{theorem}
  \label{thm.4152ann}
  Conjecture~\ref{conj.ann} holds for the $\knot{4}_1$ and
  $\knot{5}_2$ knots.
\end{theorem}
