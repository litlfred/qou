---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-006-26-quasiclassical-limit
section_title: "Quasiclassical limit"
section_number: 2.6
pages: 6-7
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.95
latex_coverage_ratio: 0.951
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
[]{#quasic label="quasic"} Recall that the fiber of $N_XZ$ over $0\in{\mathbb A}^1$ is the normal cone to $Z$ in $X$. In particular, the fiber of $N_{(\check{\mathfrak t}{}^*/W)^2}\Delta$ over $0\in{\mathbb A}^1$ is the total space of the tangent bundle $\bT(\check{\mathfrak t}{}^*/W)$. Thus, Theorem [\[normocon\]](#normocon){reference-type="ref" reference="normocon"} implies the canonical isomorphism $H^\bullet_{\bf G_O}(\Gr)\simeq\CO(\bT(\check{\mathfrak t}{}^*/W))$. On the other hand, $H^\bullet_{\bf G_O}(\Gr)$ was computed by V. Ginzburg in [@G] in terms of the universal centralizer bundle of $\check{\mathfrak g}{}$. The two computations are related as follows.

The variety $(\check{\mathfrak g}{}^*)^{reg}$ of regular elements in $\check{\mathfrak g}{}^*$ carries a sheaf of commutative Lie algebras ${\frak z}\subset \check{\mathfrak g}{}\otimes
{\mathcal O}$ whose fiber at a point $\xi\in (\check{\mathfrak g}{}^*)^{reg}$ is the stabilizer of $\xi$. We claim a canonical isomorphism ${\frak z}\cong
pr^*({\mathcal T}^*)$ where $pr:(\check{\mathfrak g}{}^*)^{reg} \to \check{\mathfrak t}{}^*/W$ is the projection to the spectrum of invariant polynomials, and ${\mathcal T}^*$ stands for the cotangent sheaf. Indeed, the fiber of $pr^*({\mathcal T}^*)$ at a point $\xi\in \check{\mathfrak g}{}^*$ is dual to the cokernel of the map $\check{\mathfrak g}{}\to
\check{\mathfrak g}{}^*$, $x\mapsto coad(x)(\xi)$; thus it is canonically isomorphic to the kernel of the dual map (which happens to coincide with the original map), which is exactly the fiber of ${\frak z}$ at $\xi$.

In view of this identification, one should compare Lemma [\[MIt\]](#MIt){reference-type="ref" reference="MIt"} in subsection [\[secr\]](#secr){reference-type="ref" reference="secr"} below with Ginzburg's description in [@G] of ${\bf G_O}$-equivariant Intersection Cohomology of a ${\bf G_O}$-orbit in $\Gr$ as a ${\frak z}$-module.

We now proceed to define the *Kostant functor* $\kappa: Coh^{{\check{G}}\times{{\mathbb G}_m}}(\check{\mathfrak g}{}^*)\to Coh^{{\mathbb G}_m}
(\bT(\check{\mathfrak t}{}^*/W))$, ${{\mathbb G}_m}$-equivariant coherent sheaves on the tangent bundle to $\check{\mathfrak t}{}^*/W$.

If $\F \in Coh^{\check{G}}(\check{\mathfrak g}{}^*)$ is equipped with an equivariant structure, then $\F|_{(\check{\mathfrak g}{}^*)^{reg} }$ carries an action of ${\frak z}$; thus by the previous paragraph it defines a coherent sheaf on the total space of the pull-back of the tangent bundle under $pr$. Restricting this sheaf to the preimage of $\Sigma$ we get a coherent sheaf on the tangent bundle to $\Sigma=\check{\mathfrak t}{}^*/W$ which we denote by $\overline{\kappa}(\F)$. Notice that $\overline{\kappa}(\F)= (\F|_{\Upsilon})^{\check{N}{}_-}$ (where we do not distinguish between a coherent sheaf on an affine variety and the module of its global sections). An obvious modification of this definition yields a functor $\kappa: Coh^{{\check{G}}\times {{\mathbb G}_m}}(\check{\mathfrak g}{}^*)\to Coh^{{{\mathbb G}_m}}
(\bT(\check{\mathfrak t}{}^*/W))$ (where the action of ${{\mathbb G}_m}$ on $\check{\mathfrak t}{}^*/W$ is the natural one).

Define the full subcategory

$Coh_{fr}^{{\check{G}}\times {{\mathbb G}_m}}(\check{\mathfrak g}{}^*)\subset Coh^{{\check{G}}\times {{\mathbb G}_m}}(\check{\mathfrak g}{}^*)$ to consist of all objects of the form $V\otimes {\mathcal O}_{\check{\mathfrak g}{}^*}$, for $V\in Rep({\check{G}}\times {{\mathbb G}_m})$.

Recall that ${\tilde S}:\ Rep({\check{G}})\to Perv_{{\bf G_O}}(\Gr)$ is the composition of $S$ with the forgetful functor $Perv_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)\to Perv_{{\bf G_O}}(\Gr)$. We have the functor of ${\bf G_O}$-equivariant cohomology $$H_{\bf G_O}^\bullet: D_{{\bf G_O}}(\Gr)\to H^\bullet_{{\bf G_O}}(\Gr)
-mod^{gr} = Coh^{{{\mathbb G}_m}}(\bT(\check{\mathfrak t}{}^*/W))$$

::: thm
[]{#free_coh label="free_coh"} The functor ${\tilde S}$ extends to a full imbedding ${\tilde S}_{qc}:\ Coh_{fr}^{{\check{G}}\times {{\mathbb G}_m}}(\check{\mathfrak g}{}^*)\to
D_{{\bf G_O}}(\Gr)$, such that there exists an isomorphism $$\label{cogokap} 
\kappa \cong H_{\bf G_O}^\bullet\circ {\tilde S}_{qc}.$$ Such an extension ${\tilde S}_{qc}$ (for a fixed isomorphism [\[cogokap\]](#cogokap){reference-type="eqref" reference="cogokap"}) is unique.
:::
