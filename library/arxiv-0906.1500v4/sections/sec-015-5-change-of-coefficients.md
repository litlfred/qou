---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-015-5-change-of-coefficients
section_title: "Change of coefficients"
section_number: 5
pages: 14-15
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.965
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
\label{section:naturality}

The aim of this section is to give some notation and explanation
about the reduction of variables (for more details,
see~\cite{Milnor:1966}).

Let $\varphi$ be a surjective homomorphism of $\pi_1(M)$ onto
$\ZZ^n=\langle t_1, \ldots, t_n \,|\, t_i t_j = t_j t_i \rangle$.  
We let $h_{(a_1, \ldots, a_n)}$ be the homomorphism of $\ZZ^n$ into
$\ZZ=\langle t \rangle$, given by 
\[
h_{(a_1, \ldots, a_n)} (t_1, \ldots, t_n)
=
(t^{a_1}, \ldots, t^{a_n})
\]
where each $a_\ell$ is a positive
integer. We use the notation $\varphi_{(a_1, \ldots, a_n)}$ for the composition of
$\varphi$ and $h_{(a_1, \ldots, a_n)}$:
\begin{equation}\label{diagram:Zm_to_Z}
  \xymatrix@R=20pt{
    \pi_1(M) \ar[r]^-\varphi \ar[dr]_{\varphi_{(a_1, \ldots, a_n)}} & \ZZ^n \ar[d]^{h_{(a_1, \ldots, a_n)}} \\  & \ZZ}
\end{equation}

Observe that $\varphi_{(\alpha_1, \ldots,
  \alpha_n)}$ is onto if and only if G.C.D $(a_1, \ldots, a_n)$
is $1$.  Moreover $\varphi_{(\alpha_1, \ldots, \alpha_n)}$
satisfies the condition $(A_\varphi)$ since each $a_\ell$ is positive.

Later in this paper, we often make a reduction of several variables
into one variable.
We let $\varphi$ be a surjective homomorphism of $\pi_1(M)$ onto
$\ZZ^n$ satisfying $(A_\varphi)$ and $\rho$ be an $\SL$-representation
satisfying $(A_\rho)$.  We choose relatively prime positive integers
$(a_1, \ldots, a_n)$ and let $\varphi_{(a_1, \ldots, a_n)}$ be the
composition of $\varphi$ and $h_{(a_1, \ldots, a_n)}$.  From
Section~\ref{section:acyclicity_complex}, the Reidemeister torsion
$\PolyTors{M}{\otAd{\varphi}{\rho}}(t_1, \ldots, t_n)$ and
$\PolyTors{M}{\otAd{\varphi_{(a_1, \ldots, a_n)}}{\rho}}(t)$ are
defined for both the abelian homomorphisms $\varphi$ and
$\varphi_{(a_1, \ldots, a_n)}$.
The following result (with sign) is a consequence of the definitions. 

\begin{proposition}[\cite{Milnor:1966}]\label{cor:naturality}
  One has the following formula:
  \[
  \PolyTors{M}{\otAd{\varphi}{\rho}}(t^{a_1}, \ldots, t^{a_n}) =
  \PolyTors{M}{\otAd{\varphi_{(a_1, \ldots, a_n)}}{\rho}}(t).
  \]
\end{proposition}
