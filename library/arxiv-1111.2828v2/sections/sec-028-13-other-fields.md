---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-028-13-other-fields
section_title: "Other fields"
section_number: 13
pages: 42-42
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
toc_source: outline
text_source: latex
latex_prose_ratio: 0.906
latex_coverage_ratio: 1.0
doc_brief: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — For a compact 3-manifold M with arbitrary (possibly empty) boundary, we give a parametrization of the set of conjugacy classes of"
---
\lbl{otherfields}
The Ptolemy varieties $P_n(K)$ and $P_n^\sigma(K)$ may be defined over an arbitrary field $F$, and as in Section~\ref{proofsection}, a Ptolemy assignment determines a boundary-unipotent representation in $\SL(n,F)$, respectively, $p\SL(n,F)$. If $E$ is a primitive extension of $F^*$ by $\Z$, there are maps
\begin{equation}
V_n(K)_F\to\widehat\B_E(F),\qquad V_n^\sigma(K)_F\to\widehat\B_E(F)_{\PSL}
\end{equation}
defined as in~\eqref{defoflambda} using a set theoretic section of $E\to F^*$ instead of a logarithm. If $F$ is infinite, the chain complex of Ptolemy assignments computes relative homology (see Proposition~\ref{freeaction}) and we have maps
\begin{equation}
H_3(\SL(n,F))\to\widehat\B_E(F),\qquad H_3(p\SL(n,F))\to\widehat\B_E(F)_{\PSL}.
\end{equation}
It thus follows that every boundary-unipotent representation has an extended Bloch group element $[\rho]$. If $F$ is a number field, the extended Bloch groups are independent of the extension $E$.  

\begin{theorem}
Let $F$ be a number field, and let $\rho\colon\pi_1(M)\to\SL(n,F)$ be a boundary-unipotent representation. If $\rho$ is irreducible, $[\rho]$ lies in $\widehat\B(\Tr(\rho))$. 
\end{theorem}
\begin{proof}
Let $\sigma$ be an automorphism of $F$ over $\Tr(\rho)$ and let $\tau\colon F\to\C$ be an embedding. Then $\rho$ and $\sigma\circ\rho$ have the same traces, so $\tau\!\circ\!\rho$ and $\tau\!\circ\!\sigma\!\circ\!\rho$ are conjugate in $\SL(n,\C)$, and thus have the same extended Bloch group element in $\widehat\B(\C)$. By Corollary~\ref{injectivity}, it follows that $[\rho]=[\sigma\!\circ\!\rho]\in\widehat\B(F)$. Hence, $[\rho]$ is invariant under all automorphisms of $F$ over $\Tr(\rho)$, so $[\rho]\in\widehat\B(\Tr(\rho))$ by Galois descent.
\end{proof}
 





\bibliographystyle{plain}
