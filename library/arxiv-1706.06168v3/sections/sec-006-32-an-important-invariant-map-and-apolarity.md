---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-006-32-an-important-invariant-map-and-apolarity
section_title: "An Important Invariant Map, and Apolarity"
section_number: 3.2
pages: 8-9
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 1.0
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#inv_maps_subsect label="inv_maps_subsect"}

To aide in our investigation of inner tensor products of $\mathop{\mathrm{SL}}_2(\mathbb{C})$ representations, we now define an important $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariant linear map, denoted by $D$. This map has a long history in invariant theory, and we touch on this below.

::: proposition
[]{#Dmap_prop label="Dmap_prop"} The linear map $D := (\partial_x \otimes \partial_y - \partial_y \otimes \partial_x): V(n+1) \otimes V(m+1) \rightarrow V(n) \otimes V(m)$ is $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariant.
:::

::: proof
*Proof.* It suffices to check this on simple tensors. Fix $\phi = \left[\begin{smallmatrix} a & b \\ c & d \end{smallmatrix}\right] \in \mathop{\mathrm{SL}}_2(\mathbb{C})$, $p \in V(n+1)$, and $q \in V(m+1)$. We compute: $$\begin{split}
            (\phi^{-1} \circ D \circ \phi) (p \otimes q) &= (\phi^{-1} \circ D) (p(dx-by, -cx+ay) \otimes q(dx-by, -cx+ay)) \\
                &= (d\partial_x-c\partial_y)p \otimes (-b\partial_x+a\partial_y)q - (-b\partial_x+a\partial_y)p \otimes (d\partial_x-c\partial_y)q \\
                &= (ad-bc)(\partial_x p \otimes \partial_y q - \partial_y p \otimes \partial_x q) \\
                &= D (p \otimes q)
        \end{split}$$ That is, $D \circ \phi = \phi \circ D$. ◻
:::

::: proposition
The multiplication map $V(n) \otimes V(m) \xrightarrow{\times} V(n+m)$ is $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariant.
:::

::: proof
*Proof.* Trivial. ◻
:::

Powers of the $D$ map actually appear in the literature under a few different names. The first comes from invariant theory, where the application of the map $$V(n) \otimes V(m) \xrightarrow{D^r} V(n-r) \otimes V(m-r) \xrightarrow{\times} V(n+m-2r)$$ to polynomials $p \in V(n)$ and $q \in V(m)$ is called the *$r^\text{th}$ transvectant* of $p$ and $q$. This map is also the result of the $r^\text{th}$ iteration of *Cayley's $\Omega$ process*. These notions are discussed, for example, in chapters 4 and 5 of [@olver1999invarianttheory], where they are used to explicitly compute invariants and covariants of forms. In particular, the invariance of the Jacobian ($1^\text{st}$ transvectant map applied to $p \otimes q$) and the Hessian ($2^\text{nd}$ transvectant map applied to $p \otimes p$) can be determined in this way.

Additionally, the $n^\text{th}$ transvectant of $p,q \in V(n)$ is used to define a notion of apolarity (see, e.g., [@rota1993apolarity] and [@brennan2007apolarity]), and this notion corresponds to the classical one used in Grace's theorem. In fact, one of the original formulations of Grace's theorem can be found in Grace and Young's 1903 book, *The Algebra of Invariants* [@grace1903invariants]. This suggests a connection between invariant theory and the analytic consequences of apolarity theory via the $D$ map, and we will indeed see this map play a crucial role in the proof of Grace's theorem (Theorem [\[graces_thm\]](#graces_thm){reference-type="ref" reference="graces_thm"}).

We are now ready to define the homogeneous apolarity form via the $D$ map. This form and its $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariance are then the next main step toward the definition of the symbol of an operator. In the next section, we will use this bilinear form to define an important construction called the dual of a representation. This will serve as the link to viewing spaces of linear operators as representations themselves.

::: definition
[]{#Uform_def label="Uform_def"} We call the $n^\text{th}$ transvectant $$V(n) \otimes V(n) \xrightarrow{D^n} V(0) \otimes V(0) \cong \mathbb{C}$$ the *apolarity form* of $V(n)$. This is the unique (up to scalar) nondegenerate $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariant bilinear form on $V(n)$, and therefore it is the homogenization of the classical apolarity form.
:::

We now want to extend this definition to act on $V(\lambda) \otimes V(\lambda)$ for $\lambda \in \mathbb{N}_0^m$. Note that for $p \in V(\lambda)$, we have $m$ pairs of variables given by $p(x_1,y_1,\ldots,x_m,y_m)$, which allows us to naturally define: $$D^\lambda := \prod_{i=1}^m (\partial_{x_i} \otimes \partial_{y_i} - \partial_{y_i} \otimes \partial_{x_i})^{\lambda_i}$$ With this, we can define the apolarity form for $V(\lambda)$ as follows.

::: definition
[]{#Mform_def label="Mform_def"} We call the map $$V(\lambda) \otimes V(\lambda) \xrightarrow{D^\lambda} V(0^m) \otimes V(0^m) \cong \mathbb{C}$$ the *apolarity form* of $V(\lambda)$. This is the unique (up to scalar) nondegenerate $(\mathop{\mathrm{SL}}_2(\mathbb{C}))^m$-invariant bilinear form on $V(\lambda)$, and therefore it is the homogenization of the multivariate apolarity form defined by Borcea and Brändén in [@bb2].
:::

Since $V(0) \otimes V(0) \cong \mathbb{C}$ and $V(0^m) \otimes V(0^m) \cong \mathbb{C}$, we will often consider the maps $D^n$ and $D^\lambda$ to output a element of $\mathbb{C}$. And as a final note, we do not justify here the claims of uniqueness and nondegeneracy stated above. Proving these claims involves decomposing $V(n) \otimes V(n)$ and $V(\lambda) \otimes V(\lambda)$ into their irreducible components, and we leave this work to Appendix [\[sl2_app\]](#sl2_app){reference-type="ref" reference="sl2_app"} for the interested reader (see Corollaries [\[Uunique_cor\]](#Uunique_cor){reference-type="ref" reference="Uunique_cor"} and [\[Munique_cor\]](#Munique_cor){reference-type="ref" reference="Munique_cor"} specifically).
