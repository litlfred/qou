---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-016-6-a-derivative-formula
section_title: "A derivative formula"
section_number: 6
pages: 15-15
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 1.0
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — We study a computational method of the hyperbolic Reidemeister torsion (also called in the literature"
---
\label{section:derform}

We prove a relation between the polynomial torsion and 
the non--abelian Reidemeister torsion. 
More precisely, we prove that
the non--abelian Reidemeister is a sort of ``differential coefficient''
associated to the polynomial torsion.

We review the definition of the non--abelian Reidemeister torsion (for
more details, we refer to~\cite[Chap.~3]{Porti:1997}).
\begin{definition}\label{def:torsion}
  Let $M$ be a compact hyperbolic three--dimensional manifold whose
  boundary is the disjoint union of $b$ tori $\partial M = \cup_{\ell = 1}^b T^2_\ell$. Consider an
  $\SL$-representation $\rho \colon \pi_1(M) \to \SL$ which is
  $\bm{\lambda}$-regular for a set of closed loops $\bm{\lambda} =
  \{\lambda_\ell \subset T^2_\ell\,|\, 1 \myleq \ell \myleq b \}$.
  The non--abelian Reidemeister torsion
  $\RTors{M}{\smallbm{\lambda}}(\rho)$ is defined to be the sign--refined
  Reidemeister torsion for $C_*(M; \sllrho)$ and the basis
  $$\hbasis{*}_{\smallbm{\lambda}} = \big\{ 
    \bbrack{P^\rho_1 \otimes T^2_1},
      \ldots, 
    \bbrack{P^\rho_b \otimes T^2_b}, 
    \bbrack{P^\rho_1 \otimes \lambda_1},
      \ldots, 
    \bbrack{P^\rho_b \otimes \lambda_b}
                              \big\}$$ as
  \[
  \RTors{M}{\smallbm{\lambda}}(\rho) = \tau_0 \cdot \Tor{C_*(M;
    \sllrho)}{\cbasis{*}}{\hbasis{*}_{\smallbm{\lambda}}}.
  \]
\end{definition}
