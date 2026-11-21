---
doc_id: arxiv-1002.0126v1
doc_title: "AN INTRODUCTION TO THE VOLUME CONJECTURE"
section_id: sec-015-51-complexification
section_title: "Complexification"
section_number: 5.1
pages: 29-29
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
toc_source: outline
text_source: latex
latex_prose_ratio: 0.791
latex_coverage_ratio: 1.0
doc_brief: "AN INTRODUCTION TO THE VOLUME CONJECTURE — This is an introduction to the Volume Conjecture and its gener- alizations for nonexperts."
---
In [@Thurston:BULAM31982] W. Thurston pointed out that the Chern--Simons invariant [@Chern/Simons:ANNMA21974] can be regarded as an imaginary part of the volume. Neumann and Zagier gave a precise conjecture [@Neumann/Zagier:TOPOL85 Conjecture, p. 309] which was proved to be true by Yoshida [@Yoshida:INVEM85]. For combinatorial approaches to the Chern--Simons invariant, see [@Neumann1992] and [@Zickert:DUKMJ2009].

So it would be natural to drop the absolute value sign of the left hand side of the Volume Conjecture and add the Chern--Simons invariant to the right hand side.

::: conjecture
[]{#conj:CVC label="conj:CVC"} If a knot $K$ is hyperbolic, that is, its complement possesses a complete hyperbolic structure, then $$\begin{gathered}
  2\pi\lim_{N\to\infty}\frac{\log J_N(K;\exp(2\pi\sqrt{-1}/N)) }{N}
  \equiv
  \operatorname{Vol}(S^3\setminus{K})+\sqrt{-1}\operatorname{CS}(S^3\setminus{K})
  \\
  \pmod{\pi^2\sqrt{-1}\mathbb{Z}},
\end{gathered}$$ where $\operatorname{CS}$ is the Chern--Simons invariant defined for a three-manifold with torus boundary by Meyerhoff [@Meyerhoff:density].
:::

::: remark
We may regard the left hand side as a definition of the Chern--Simons invariant for non-hyperbolic knots provided that the limit of Conjecture [\[conj:CVC\]](#conj:CVC){reference-type="ref" reference="conj:CVC"} exists.
:::
