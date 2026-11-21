---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-022-731-proof-for-one-variable
section_title: "Proof for one variable"
section_number: 7.3.1
pages: 21-22
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 1.0
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
We cut the manifold $M$ along $S = S_\varphi$ and obtain the following splitting:
$M = N \cup (S \times I)$, where $I= [0,1]$ is the closed unit
interval. The boundaries of $N$ and $S \times I$ are equal and consist
in the disjoint union of two copies of $S$ denoted $S^- = S \times
\{0\}$ and $S^+ = S \times \{1\}$. We apply the Multiplicativity Lemma
to the Mayer--Vietoris sequence associated to this splitting to compute
the Reidemeister torsion of $M$. Our assumptions on $\rho \colon
\pi_1(M) \to \SL$ and $\varphi \colon \pi_1(M) \to \ZZ^n$ say that
every restrictions of $\rho$ to $\pi_1(S_\ell)$ are non--abelian,
so we have:
\begin{lemma}\label{lemma:twist-H}
  The twisted homology groups of $N$ and $S \times I$ are given by:
  \[
  H_*(S \times I; \sllrhot) = \CC(t) \otimes_\CC H_*(S \times
  I;\sllrho) \simeq \CC(t) \otimes H_*(S; \sllrho),
  \]
  \[
  H_*(N; \sllrhot) = \CC(t) \otimes_\CC H_*(N; \sllrho).
  \]
  Moreover, $H_0(S \times I; \sllrhot) = H_2(S \times I; \sllrhot) =
  0$.
\end{lemma}
\begin{proof}[Proof of Lemma~\ref{lemma:twist-H}]
  One has $M = N \cup (S \times I)$, where $N$ is a three--dimensional
  connected manifold whose boundary consists in $S^- \cup S^+$.  One
  can observe that the actions of the restrictions
  $\varphi_{|\pi_1(N)}$ and $\varphi_{|\pi_1(S_\ell)}$ of the
  representation $\varphi$ are trivial. So the first two equalities of the
  lemma hold.
  
  As $\rho|_{\pi_1(S_\ell)}$ is
  non--abelian, then $H_0(S_\ell \times I; \sllrhot) = 0$. In the case of a closed surface,
 last equality $H_2(S_\ell \times I; \sllrhot) = 0$ follows from Poincar\'e duality. For (compact) surface with boundary, last equality $H_2(S_\ell \times I; \sllrhot) = 0$ follows from the fact that $S_\ell \times I$ has the same homotopy type as a one--dimensional complex. So that $H_0(S \times I; \sllrhot) = H_2(S \times I; \sllrhot) = 0$.
\end{proof}

As $H_*(M; \sllrhot) = 0$, see Proposition~\ref{prop:acyclic}, the
Mayer--Vietoris sequence with coefficients in $\sllt$, denoted
$\mathcal{V}$, reduces to a single isomorphism:
\begin{equation}\label{eqn:MV}
  \mathcal{V}: 
  H_1(S^-;\sllrhot) \oplus H_1(S^+;\sllrhot) \xrightarrow{\simeq}
  H_1(N;\sllrhot) \oplus H_1(S \times I;\sllrhot) 
\end{equation}
where $H_1(S^\pm;\sllrhot) \simeq H_1(S;\sllrhot) \simeq H_1(S \times
I;\sllrhot)$.  The isomorphism in sequence~(\ref{eqn:MV}) is represented by the following matrix:
\[
\left(
  \begin{array}{cc}
    i^-_* & -i^+_* \\ 
    -\I & t\I
  \end{array}
\right),
\]
here $i^{\pm}\colon S_\pm \to N$ is the inclusion and $\I$ is the
identity matrix.  The Multiplicativity Lemma for Reidemeister
torsion gives us the identity below, because the common boundary of
$N$ and $S \times I$ is the disjoint union of two copies of $S$:
\[
\pm \PolyTors{M}{\rho}(t) \cdot \Tor{S}{\cbasis{*}_S}{\hbasis{*}_S}^2
\cdot \Tor{\mathcal{V}}{\{\hbasis{*}_S, \hbasis{*}_N\}}{\emptyset} =
\Tor{N}{\cbasis{*}_N}{\hbasis{*}_N} \cdot \Tor{S\times
  I}{\cbasis{*}_S}{\hbasis{*}_S}.
\]
Thus, since the torsions of $S$ and $S \times I$ are the same,
\[
\pm\PolyTors{M}{\rho}(t) = \Tor{\mathcal{V}}{\{\hbasis{*}_S,
  \hbasis{*}_N\}}{\emptyset}^{-1} \frac{
  \Tor{N}{\cbasis{*}_N}{\hbasis{*}_N} }{
  \Tor{S}{\cbasis{*}_S}{\hbasis{*}_S} } = \det \left(
  \begin{array}{cc}
    i^-_* & -i^+_* \\
    -\I & t\I
  \end{array}
\right) \frac{ \Tor{N}{\cbasis{*}_N}{\hbasis{*}_N} }{
  \Tor{S}{\cbasis{*}_S}{\hbasis{*}_S} }.
\]
The fraction of torsions $\Tor{N}{\cbasis{*}_N}{\hbasis{*}_N} /
\Tor{S}{\cbasis{*}_S}{\hbasis{*}_S}$ is independent of $t$ (because as
we have already observed in the proof of Lemma~\ref{lemma:twist-H},
the actions of the restrictions $\varphi_{|\pi_1(N)}$ and
$\varphi_{|\pi_1(S)}$ are trivial).  This proves that, up to sign,
$$
\pm \PolyTors{M}{\rho}(t) = \det(t i^-_* - i^+_*) \frac{
  \Tor{N}{\cbasis{*}_N}{\hbasis{*}_N} }{
  \Tor{S}{\cbasis{*}_S}{\hbasis{*}_S} }
$$ is a polynomial in $t$.
The one variable case in Theorem~\ref{theorem:poly} is proved.

\begin{remark}
  A result similar to Lemma~\ref{lemma:twist-H} can be found
  in~\cite[Proposition 3.6]{KL}.
\end{remark}
