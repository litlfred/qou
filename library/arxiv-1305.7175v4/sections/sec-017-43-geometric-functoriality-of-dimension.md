---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-017-43-geometric-functoriality-of-dimension
section_title: "Geometric functoriality of dimension"
section_number: 4.3
pages: 27-29
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 0.949
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
::: prop
[]{#geometric adjunction label="geometric adjunction"} The graph $X\leftarrow \Gamma_f \to Y$ of any proper morphism $f: X\to Y$ gives a continuous morphism $F:X\to Y$ in $\ul{Corr}^{prop}_k$, with right adjoint $F^r:Y\to X$ identified with the opposite correspondence $Y\leftarrow \Gamma_f \to X$.
:::

::: proof
*Proof.* We construct the unit and counit of the adjunction as follows. Consider the composition $F^r F:X\to X$ of correspondences $$\xymatrix{&&X \times_Y X \ar[ld]\ar[rd]&&\\
&\Gamma_f\ar[ld]\ar[rd]&&\Gamma_f\ar[ld]\ar[rd]& \\
X&&Y &&X}$$ The unit $\eta_f: \id_X=X \to F^rF\simeq X\times_Y X$ is given by the relative diagonal map.

Consider the opposite composition of correspondences $$\xymatrix{&&X \times_X X \ar[ld]\ar[rd]&&\\
&\Gamma_f\ar[ld]\ar[rd]&&\Gamma_f\ar[ld]\ar[rd]& \\
Y&&X &&Y}$$ The counit $\epsilon_f:  FF^r\simeq X\to \id_Y=Y$ is given by $f$ itself.

The standard identities are easily verified by identifying the resulting composite map $$\xymatrix{\Gamma_f\ar[r] & \Gamma_f\times_Y \Gamma_f \times_X \Gamma_f \ar[r] & \Gamma_f}$$ of correspondences with the identity. ◻
:::

::: lemma
[]{#geometric cyclic trace label="geometric cyclic trace"} Let $F_Z:X\to Y$ and $F_W:Y\to X$ be morphisms in $Corr_k$ given by respective correspondences $X\leftarrow Z \to Y$ and $Y \leftarrow W \to X$. Then the canonical equivalence $$\xymatrix{
m(F_W, F_Z):\Tr(F_W\circ F_Z) \ar[r]^-\sim & \Tr(F_Z\circ F_W)
}$$ is given by the composition of evident geometric identifications $$\xymatrix{
  (Z \times_Y W) \times_{X \times X} X \ar[r]^-\sim &  W \times_{X\times Y} Z \ar[r]^-\sim & Z \times_{Y\times X} W
  \ar[r]^-\sim &  (W \times_X Z) \times_{Y \times Y} Y 
}$$
:::

::: proof
*Proof.* Returning to the definition and using our previous identifications, observe that $m(F_Z, F_W)$ is calculated by commutativity of the diagram of correspondences $$\xymatrix{ & X\times X\ar[r]^-{Z \times X}     \ar[ddr]^-{X \times W}      & Y\times X
 \ar[r]^-{W\times X} \ar[ddr]^-{Y \times W}  & X\times X
\ar[dr]^-{X} &\\
pt\ar[ur]^-{X} \ar[dr]_-{Y} & &  && pt\\
& Y\times Y   \ar[r]_-{W\times Y}    & X\times Y \ar[r]_-{X \times Y} &
Y\times Y  \ar[ur]_-{Y} & }$$

Following the top edge, we see $\Tr(F_W\circ F_Z) \simeq  (Z \times_Y W) \times_{X \times X} X$. Following the bottom edge, we see $\Tr(F_Z\circ F_W) \simeq  (W \times_X Z) \times_{Y \times Y} Y$. Moving from the top to bottom edge via the successive equivalences of the three commuting squares, one finds the three successive equivalences in the assertion of the lemma. ◻
:::

::: prop
[]{#geometric dims label="geometric dims"} Suppose $f:X\to Y$ is a proper morphism, and $F:X\to Y$ denotes the induced morphism in $\ul{Corr}^{prop}_k$ given by the graph $X\leftarrow \Gamma_f \to Y$. Then $\dim(F):\dim(X)\to\dim(Y)$ is canonically identified with the $S^1$-equivariant morphism $\cL f:\cL X\to \cL Y$.
:::

::: proof
*Proof.* Denote by $F^r:Y\to X$ the right adjoint to $F$. We must calculate $$\xymatrix{
\dim(X) \ar[r] & \Tr(F^r F) \ar[rr]^-{m(F^r, F)} && \Tr(F F^r) \ar[r] & \dim(Y)
}$$ We have seen that the first and third morphisms correspond to the natural geometric maps $$\xymatrix{
\cL X \simeq X\times_{X \times X} X \ar[r] & (X \times_Y X) \times_{X \times X} X &
X \times_{Y \times Y} Y \ar[r] & Y \times_{Y \times Y} Y \simeq \cL Y
}$$ induced by the relative diagonal $X\to X\times_Y X$ and given map $f:X\to Y$ respectively. Furthermore, by Lemma [\[geometric cyclic trace\]](#geometric cyclic trace){reference-type="ref" reference="geometric cyclic trace"}, the middle map is the natural geometric identification $$\xymatrix{
(X \times_Y X) \times_{X \times X} X \ar[r]^-\sim & 

X \times_{Y \times Y} Y}$$

Altogether, the composition

is easily identified with the loop map $\cL f:\cL X \to \cL Y$. ◻
:::

::: remark
It follows from the proposition that the loop map $\cL f:\cL X \to \cL Y$ must be proper when the given map $f:X\to Y$ is proper. Let us note why this is true geometrically from the factorization $\cL X \to \cL_X Y \to \cL Y$ appearing in the proof.

First, the natural morphism $\cL X\to \cL_X Y$ is the restriction along the diagonal $X\to X\times X$ of the relative diagonal $X\to \XYX$. The relative diagonal is a closed embedding since $f$ is proper, and hence the natural morphism $\cL X\to \cL_X Y$ is as well. Second, the natural morphism $\cL_X Y
\to \cL Y$ is the restriction along the diagonal $Y\to Y\times Y$ of the proper morphism $f:X\to Y$ and thus is proper as well. Altogether, we see that $\cL f:\cL X\to \cL Y$ is itself proper.
:::

::: remark
One can invoke the cobordism hypothesis with singularities to endow the morphism $\dim(F):\dim(X)\to \dim(Y)$ with a canonical $S^1$-equivariant structure, and it will agree with the canonical geometric $S^1$-equivariant structure on the map $\cL f:\cL X\to \cL Y$ under the identification of the proposition.
:::
