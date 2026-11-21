---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-027-72-monodromic-hecke-categories
section_title: "Monodromic Hecke categories"
section_number: 7.2
pages: 40-41
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.992
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
Let us return to the setup of a proper map $p:X\to Y$ of stacks where $X$ has smooth diagonal $\delta:X\to X\times X$. Suppose given $\mathcal A_X\in {\mathcal D}(X)$ a commutative algebra object.

Let $j:X \times_Y X\to X\times X$ be the natural map, introduce the commutative algebra object $$\mathcal A^{(2)}_X = j^! (\mathcal A_X \boxtimes \mathcal A_X) \in {\mathcal D}(X \times_Y X)$$ and the resulting Hecke category of bimonodromic ${\mathcal D}$-modules $${\mathcal D}_{\mathcal A^{(2)}_X}(X \times_Y X) = \mathop{\mathrm{Mod}}_{\mathcal A^{(2)}_X}({\mathcal D}(X \times_Y X))$$ More generally, we have similar constructions for repeated fiber products.

There is a natural monoidal structure on the bimonodromic Hecke category $\tilde\mathcal H= {\mathcal D}_{\mathcal A^{(2)}_X}(X \times_Y X)$ with product given by $$\mathfrak M\star_{\mathcal A_X} \mathfrak N= \tilde p_{13*}(\tilde p_{12}^!(\mathfrak M) \otimes_{\mathcal A^{(3)}_X} \tilde p_{23}^!(\mathfrak N))$$

Here the functors are the ringed-space variants of the usual pullback, tensor and pushforward functors. Namely, the $!$-pullbacks denote the composition of the usual $!$-pullbacks and then tensoring up with the free $\mathcal A_X$-module on the remaining factor. The tensor product denotes the tensor product of $\mathcal A^{(3)}_X$-modules. The $*$-pushforward denotes the composition of the usual $*$-pushforward and then forgetting the $\mathcal A_X$-module structure on the middle factor. The monoidal unit $1_{\tilde \mathcal H}$ is the diagonal bimodule $u_*\mathcal A_{X}$ arising from the map $u:X\to X \times_Y X$. Standard identities produce the higher constraints of the monoidal structure.

In the case where $\mathcal A_X = \pi_*\pi^*\omega_X  \in {\mathcal D}(X)$ for a smooth map $\pi:\tilde X\to X$ as discussed above, the monodromic Hecke category is a full subcategory $$\xymatrix{
\tilde\mathcal H={\mathcal D}_{\mathcal A^{(2)}_X}(X \times_Y X) 
\ar@{^(->}[r] &
{\mathcal D}(\tilde X\times_Y \tilde X)
}$$ Moreover, the latter category is naturally monoidal with respect to convolution and the above inclusion is monoidal.

::: example
If $\tilde X = B \to X = BB \to Y = BG$ are the natural projections of classifying stacks for a Borel subgroup $B\subset G$ and its unipotent radical $N\subset B$, then a bimonodromic ${\mathcal D}$-module in the above sense is equivalent to a traditional unipotent bimonodromic ${\mathcal D}$-module on $N\backslash G/N$.
:::

We have the following algebraic observation extending Theorems [\[perfect Hecke\]](#perfect Hecke){reference-type="ref" reference="perfect Hecke"}, [\[CY Hecke\]](#CY Hecke){reference-type="ref" reference="CY Hecke"}.

::: theorem
[]{#monodromic Hecke label="monodromic Hecke"} Suppose $X$ is a stack with smooth diagonal, $Y$ is a stack, and $X\to Y$ is a proper representable map. Suppose $\mathcal A_X\in {\mathcal D}(X)$ is a commutative algebra object whose underlying object is compact.

Then the monodromic Hecke category $\tilde \mathcal H={\mathcal D}_{\mathcal A^{(2)}_X}(X \times_Y X)$ is semi-rigid (hence 2-dualizable) with a canonical Calabi-Yau structure.
:::

::: proof
*Proof.* For compact objects $\mathfrak M\in \mathcal H$, objects of the form $\mathcal A^{(2)}_X\otimes \mathfrak M\in \tilde \mathcal H$ are compact and generate. Recall from the proof of Theorem [\[perfect Hecke\]](#perfect Hecke){reference-type="ref" reference="perfect Hecke"} that $\iota(\mathfrak M)\in \mathcal H$ is the left and right monoidal dual of such compact objects $\mathfrak M\in \mathcal H$.

Recall the natural map $j:X \times_Y X\to X\times X$, and introduce the $\mathcal A^{(2)}_X$-modules $$\xymatrix{
\mathcal A^{(2)}_X{}' = j^! (\mathcal A_X \boxtimes \mathcal A^\vee_X) \in {\mathcal D}(X \times_Y X)
&
{}'\hspace{-0.25em}\mathcal A^{(2)}_X = j^! (\mathcal A^\vee_X \boxtimes \mathcal A_X) \in {\mathcal D}(X \times_Y X)
}$$

It is simple to check that $\mathcal A^{(2)}_X{}' \otimes \iota(\mathfrak M)\in \tilde \mathcal H$ (respectively, ${}'\hspace{-0.25em}\mathcal A^{(2)}_X\otimes \iota(\mathfrak M)\in \tilde \mathcal H$) is the right (respectively, left) monoidal dual of $\mathcal A^{(2)}_X \otimes \mathfrak M\in \tilde \mathcal H$.

Finally, for the Calabi-Yau structure, one can directly repeat the proof of Theorem [\[CY Hecke\]](#CY Hecke){reference-type="ref" reference="CY Hecke"} with the functors $q_*$ and $p^!$ replaced by their respective monodromic versions $\tilde q_*$ and $\tilde p^!$ as in the construction of the monoidal structure on $\tilde \mathcal H$.

Namely, they are given by the ringed-space variants where $\tilde q_*$ is the composition of the usual $*$-pushforward and then forgetting the module structure, and $\tilde p^!$ is the composition of the usual $!$-pullback and then tensoring up with the free module. ◻
:::
