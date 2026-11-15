---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-020-72-a-sufficient-condition-to-be-a-polynomial
section_title: "A sufficient condition to be a polynomial"
section_number: 7.2
pages: 20-21
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.726
latex_coverage_ratio: 1.0
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
Under some additional assumptions for the $\SL$-representation $\rho$
and dual surfaces determined by $\varphi$, we prove that the Reidemeister torsion
$\PolyTors{M}{\otAd{\varphi}{\rho}}$ is a polynomial.

\begin{theorem}\label{theorem:poly}

  Let $M$ be a hyperbolic three--manifold with
  tori boundary which satisfy $(A_M)$.  Let $\varphi$ be a surjective
  homomorphism $\pi_1(M) \to \ZZ^n$ which satisfies $(A_\varphi)$ and
  $\rho$ be an $\SL$-representation of $\pi_1(M)$ satisfying
  $(A_\rho)$.
  Let $S_\varphi = \cup_\ell S_\ell$ be the dual surfaces corresponding to
  $\varphi$.

  \begin{enumerate}
  \item Suppose that $n=1$. If the restriction $\rho|_{\pi_1(S_\ell)}$ of
    $\rho$ is non--abelian for all $\ell$, then $\PolyTors{M}{\otAd{\varphi}{\rho}}$
    is a polynomial in $t$, up to a factor $t^m$, $m \in \ZZ$.
  \item Suppose that $n \mygeq 2$. If for any natural number $N$ there
    exists relatively prime integers $(a_1, \ldots, a_n)$ such that
    $|a_i - a_j| > N$ for all distinct $i, j$ and the restriction
    $\rho|_{\pi_1(S)}$ on every component $S$ of the dual surfaces
    $S_{(a_1, \ldots, a_n)}$ corresponding to $\varphi_{(a_1, \ldots,
      a_n)}$ is non--abelian, then
    $\PolyTors{M}{\otAd{\varphi}{\rho}}$ is a polynomial in $t_1,
    \ldots, t_n$, up to a factor $t_1^{m_1} \cdots t_n^{m_n}$ for
    $m_1, \ldots, m_n \in \ZZ$.
  \end{enumerate}

\end{theorem}


Before proving this theorem, we give some explanations, examples and
counterexamples.

\begin{remark}
  Let $K$ be a hyperbolic knot in $S^3$. Consider $\rho_0 \colon
  \pi_1(E_K) \to \SL$ (a lift of) the holonomy representation and
  $\varphi \colon \pi_1(E_K) \to \ZZ$ the abelianization. The dual
  surface $S_\varphi$ corresponding to $\varphi$ is a Seifert surface of $K$. One can observe that the longitude 
  lies in the second commutator subgroup of $\pi_1(E_K)$. Thus,
  the restriction $\rho_0|_{\bord E_K}$ sends the longitude to a
  parabolic element which is not $\pm \I$.  This means that the
  restriction of $\rho_0$ on $\pi_1(S_\varphi)$ is non--abelian.
\end{remark}

\begin{remark}
  Let $K$ be a fibered knot in $S^3$. Consider an irreducible,
  non--metabelian representation $\rho \colon \pi_1(E_K) \to \SL$ and
  the homomorphism $\varphi \colon \pi_1(E_K) \to \pi_1(S^1) =\ZZ$
  induced by the fibration $E_K \to S^1$. The dual surface
  $S_\varphi$ corresponding to $\varphi$ is the fiber of $K$. One can easily
  observe that $\rho|_{\pi_1(S_\varphi)}$ is non--abelian, because the commutator
  subgroup $[\pi_1(E_K), \pi_1(E_K)]$ of $\pi_1(E_K)$ is $\pi_1(S_\varphi)$.
\end{remark}










\begin{remark}
For every $\SL$-representation $\rho$ and $\gamma \in \pi_1(M)$,
the linear map $Ad \circ \rho(\gamma)$ always has eigenvalue $1$.
In the one variable case with the ${\rm SL}_3(\CC)$-representation $Ad \circ \rho$, 
we can not use Wada's criterion~\cite[Proposition 8]{Wada94} directly.
\end{remark}


\subsection{Proof of Theorem~\ref{theorem:poly}}

The proof is divided into two main steps: we first consider the case
of a single variable $t$ and next use the naturality property of
$\PolyTors{M}{\otAd{\varphi}{\rho}}$ (see Section~\ref{section:naturality}) to deduce by an algebraic
argument the multivariable case form the one variable case.

\begin{remark}
  In what follows the sign in the Reidemeister torsion will be not
  relevant; so, we will work \emph{up to sign}.  We let
  $\Tor{W}{\cbasis{*}_W}{\emptyset}$ denote 
  the (acyclic) Reidemeister torsion of the manifold $W$ with 
  coefficients in $\sllt$ and computed in 
  the appropriate geometric basis $\cbasis{*}_W$.
\end{remark}
