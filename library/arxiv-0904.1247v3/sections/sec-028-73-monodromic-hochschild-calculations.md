---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-028-73-monodromic-hochschild-calculations
section_title: "Monodromic Hochschild calculations"
section_number: 7.3
pages: 41-42
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.953
latex_coverage_ratio: 1.0
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
We continue with the setup and constructions of the previous section, in particular Theorem [\[monodromic Hecke\]](#monodromic Hecke){reference-type="ref" reference="monodromic Hecke"}. Thus suppose $X$ is a stack with smooth diagonal, $Y$ is a stack, and $X\to Y$ is a proper representable map. Suppose $\mathcal A_X\in {\mathcal D}(X)$ is a commutative algebra object whose underlying object is compact and hence dualizable with dual denoted by $\mathcal A_X^\vee\in {\mathcal D}(X)$.

Return to the fundamental correspondence $$\xymatrix{
 \mathcal LY  = Y\times_{Y\times Y} Y & \mathcal LY \times_Y X =X \times_{X \times Y} X \ar[l]_-{q} \ar[r]^-{\epsilon} & X\times_Y X.\\
}$$ where $q$ is a base change of $p$, and $\epsilon$ is a base change $\delta$.

Define the functor $$\xymatrix{
\tilde F: {\mathcal D}_{\mathcal A^{(2)}_X}(X\times_Y X) \ar[r]^-{\tilde \epsilon^!} & {\mathcal D}_{\mathcal A_X}(\mathcal LY \times_Y X) 
 \ar[r]^-{\tilde q_*}& {\mathcal D}(\mathcal LY) \\
}$$ where $\tilde \epsilon^!$ is the composition of the pullback $\epsilon^!$ and then tensoring with the diagonal $\mathcal A_X$-module, and $\tilde q_*$ is the composition of forgetting $\mathcal A_{X}$-module structure and then the pushforward $q_*$.

For simplicity, we will also assume given an equivalence of $\mathcal A_X$-modules of the form $\mathcal A_X^\vee \simeq \mathcal A_X[k]$, for some fixed $k$. This provides an identification of the right adjoint of the pushforward $\tilde q_*$ with a shift of the pullback $\tilde q^!$. Thus we have the explicit continuous right adjoint $$\xymatrix{
\tilde F^r:{\mathcal D}(\mathcal LY)   \ar[r]^-{\tilde q^![k]}&{\mathcal D}_{\mathcal A_X}(\mathcal LY \times_Y X)  \ar[rr]^-{\tilde \epsilon_*[-2\dim X]} && {\mathcal D}_{\mathcal A^{(2)}_X}(X\times_Y X)\\
}$$ where $\tilde q^!$ is the composition of the pullback $q^!$ and then tensoring with $\mathcal A_X$, and $\tilde \epsilon_*$ is the composition of forgetting to an $\mathcal A^{(2)}_X$-module structure and then the pushforward $\epsilon_*$.

Let $\mathcal I(\tilde F) \subset {\mathcal D}(\mathcal LY)$ denote the cocompletion of the image of $\tilde F$. It is naturally equivalent to the left orthogonal ${}^\perp \mathcal K(\tilde F^r) \subset {\mathcal D}(\mathcal LY)$ to the kernel of $\tilde F^r$.

Suppose in addition that tensoring with $\mathcal A_X^\vee$ is conservative so that $\tilde q^!$ satisfies descent. Then both of the above categories are naturally equivalent to the full subcategory of ${\mathcal D}(\mathcal LY)$ of objects whose image under $\tilde q^!$ is in the cocompletion of the image of $\tilde \epsilon^!$.

Now repeating the arguments of Theorem [\[thm center\]](#thm center){reference-type="ref" reference="thm center"} and Corollary [\[cor trace\]](#cor trace){reference-type="ref" reference="cor trace"} gives the following extension.

::: theorem
There are natural adjoint commutative diagrams $$\xymatrix{
&  \tilde \mathcal H\ar[dl]_-\mathfrak {tr}\ar[d]<-1ex>_-{F}&\\
 \operatorname{Tr}(\tilde \mathcal H) \ar[r]^-\sim & \ar[u]<-1ex>_-{\tilde F^r} {}^\perp \mathcal K(\tilde F^r) \simeq \mathcal I(\tilde F) \ar[r]^-\sim
 &  \ar[ul]_-\mathfrak z\operatorname{Z}(\tilde \mathcal H)
   }$$
:::

::: proof
*Proof.* For notational convenience, set $\tilde \mathcal A= {\mathcal D}_{\mathcal A_{X \times_Y X}}(X \times_Y X)$ and $\tilde \mathcal B= {\mathcal D}_{\mathcal A_X}(X)$, so that the center is the totalization of the cosimplicial object $$\tilde \mathcal C^\bullet =  \mathop{\mathrm{Hom}}_{\tilde \mathcal B\otimes \tilde\mathcal B^{op}} (\tilde\mathcal A^{\otimes_{\tilde\mathcal B\bullet}},  \tilde\mathcal A)$$

Using Proposition [\[prop int trans adjoint\]](#prop int trans adjoint){reference-type="ref" reference="prop int trans adjoint"} as in the proof of of Theorem [\[thm center\]](#thm center){reference-type="ref" reference="thm center"}, we have a level-wise fully faithful map of cosimplicial diagrams $$\xymatrix{
\tilde \mathcal C^\bullet \ar[r] &  
 {\mathcal D}_{\mathcal A^{(\bullet + 1)}_{X}}(X^{\times_Y (\bullet+1)} \times_Y \mathcal LY)
 }$$ where the cosimplicial structure maps on the latter are given by the composition of $!$-pullbacks together with tensoring up with tensor powers of $\mathcal A_X^\vee$.

Thus the center $\operatorname{Z}(\mathcal A)$ is equivalent to the full subcategory of ${\mathcal D}(\mathcal LY)$ of objects whose image under $\tilde q^!$ is in the cocompletion of the image of $\tilde \epsilon^!$. ◻
:::

Finally, there is a Morita-invariance between the original and now monodromic calculations.

::: prop
The full subcategories $\mathcal K(F^r), \mathcal K(\tilde  F^r)\subset  {\mathcal D}(\mathcal LY)$ defined by the original and monodromic fundamental correspondences coincide.
:::

::: proof
*Proof.* On underlying objects, we calculate via composition identities and the projection formula that $\tilde F^r(\mathfrak M) \simeq F(\mathfrak M) \otimes \mathcal A'_{X \times_Y X}$. Since tensoring with $\mathcal A_X^\vee$ is conservative, so is tensoring with $\mathcal A'_{X \times_Y X}$, and hence $\mathcal K(F^r) = \mathcal K(\tilde F^r) \subset {\mathcal D}(\mathcal LY)$. ◻
:::
