---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-018-44-geometric-functoriality-of-trace
section_title: "Geometric functoriality of trace"
section_number: 4.4
pages: 29-29
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.944
doc_brief: "NONLINEAR TRACES — We combine the theory of traces in homotopical algebra with sheaf theory in de- rived algebraic geometry to deduce general ﬁxed point and character formulas."
---
Consider a proper morphism $f:X\to Y$ and endomorphisms $F_Z:X\to X$ and $F_W:Y\to Y$ in $Corr_k$ given by respective self-correspondences $X\leftarrow Z \to X$ and $Y \leftarrow W \to Y$.

By an $f$-morphism from the pair $(X,F_Z)$ to the pair $(Y,F_W)$, we mean an identification $$\xymatrix{
  s:Z  \ar[r]^-\sim &  X\times_Y W
  }$$ of correspondences from $X$ to $Y$. This in turn induces an identification of what might be called relative traces $$\xymatrix{
  Z\times_{Y\times Y} Y\ar[r]^-\sim &  X\times_{Y\times Y} W
  }$$ generalizing the relative loop space $\cL_X Y$ from the case of the identity correspondences $Z=X$, $W=Y$. We thus obtain a map of traces $$\xymatrix{
\tau(f, s):Z|_{\Delta_X}  =   Z\times_{X\times X} X \ar[r] &   Z \times_{Y\times Y} Y \ar[r]^-\sim &  X \times_{Y\times Y} W \ar[r] &  
  Y\times_{Y\times Y} W = W|_{\Delta_Y}
}$$

::: prop
[]{#geometric traces label="geometric traces"} With the preceding setup, the trace map $\Tr(f,s):\Tr(F_Z)\to\Tr(F_W)$ is canonically identified with the geometric map $$\xymatrix{
\tau(f, s): Z|_{\Delta_X} \ar[r] & W|_{\Delta_Y}
}$$
:::

::: proof
*Proof.* Denote by $F:X\to Y$ the morphism given by the graph $X\leftarrow \Gamma_f \to Y$, and by $F^r:Y\to X$ its right adjoint. We must calculate $$\xymatrix{
\Tr(F_Z) \ar[r] & \Tr(F^r F F_Z) \ar[r]^-{s } &  \Tr(F^r F_W F)   \ar[rr]^-{m(F^r, F_W F)} && \Tr(F_W F F^r) \ar[r] & \Tr(F_W)
}$$

We have seen that the first and fourth morphisms correspond to the natural geometric maps $$\xymatrix{
Z|_{\Delta_X} = Z\times_{X \times X} X \ar[r] & Z  \times_{X \times X} (X\times_Y X)  
}$$ $$\xymatrix{
X \times_{Y \times Y} W \ar[r] & Y \times_{Y \times Y} W = W|_{\Delta_Y}
}$$ induced by the relative diagonal $X\to X\times_Y X$ and given map $f:X\to Y$ respectively.

Using associativity, the second map, induced by $s$, is the natural geometric identification $$\xymatrix{
Z  \times_{X \times X} (X\times_Y X)  \simeq Z \times_{Y\times Y} Y\ar[r]^-\sim &  W \times_{Y \times Y} X 

}$$ By Lemma [\[geometric cyclic trace\]](#geometric cyclic trace){reference-type="ref" reference="geometric cyclic trace"}, the third map, given by the cyclic symmetry, is nothing more than the natural identification $$\xymatrix{
W \times_{Y \times Y} X  \ar[r]^-\sim &
X \times_{Y \times Y} W
}$$

Thus assembling the above maps we arrive at the composition defining $\tau(f, s)$. ◻
:::
