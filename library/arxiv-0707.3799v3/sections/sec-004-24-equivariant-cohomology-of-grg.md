---
doc_id: arxiv-0707.3799v3
doc_title: "Equivariant Satake category and Kostant-Whittaker reduction"
section_id: sec-004-24-equivariant-cohomology-of-grg
section_title: "Equivariant cohomology of GrG"
section_number: 2.4
pages: 5-5
source_pdf: 0707.3799v3.pdf
source_sha256: 0b29cbced7939f72
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.903
doc_brief: "Equivariant Satake category and Kostant-Whittaker reduction — 24 sections: Front matter; Introduction; Notation and statements of the res"
---
Note that $H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr_G)=
H^\bullet_{{{\mathbb G}_m}}({\bf G_O}\backslash{\bf G_F}/{\bf G_O})$, whence two morphisms $pr_1^*, pr_2^*:\ {\mathcal O}({\frak t}/W)=H^\bullet_{\bf G_O}(pt)\to
H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr_G)$. We also have a morphism $pr^*:\ \mathsf k[\hbar]=H^\bullet_{{\mathbb G}_m}(pt)\to
H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr_G)$.

::: thm
[]{#normocon label="normocon"} a) Assume $G$ is simply connected. We have a canonical isomorphism $H^\bullet_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr_G)\cong
{\mathcal O}(N_{\check{\mathfrak t}{}^*/W\times \check{\mathfrak t}{}^*/W}\Delta)$ where $\Delta \subset (\check{\mathfrak t}{}^*/W)^2$ is the diagonal. Here the projection $N_{ (\check{\mathfrak t}{}^*/W)^2}\Delta\to {\mathbb A}^1$ corresponds to the homomorphism $H_{{{\mathbb G}_m}}^\bullet(pt)\to H^\bullet_{{\bf G_O}
\rtimes {{\mathbb G}_m}} (\Gr_G)$; and the two projections $N_{ (\check{\mathfrak t}{}^*/W)^2}\Delta
\to \check{\mathfrak t}{}^*/W={\frak t}/W$ correspond to the two homomorphisms $H_{{\bf G_O}}^\bullet(pt)\to H^\bullet_{{\bf G_O}
\rtimes {{\mathbb G}_m}} (\Gr_G)$. The isomorphism is specified uniquely by these requirements.

b\) For arbitrary $G$ we have a canonical isomorphism $H^*_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr_G)\cong\bigoplus_{\pi_1(G)}{\mathcal O}(N_{\check{\mathfrak t}{}^*/W\times \check{\mathfrak t}{}^*/W}\Delta)$.
:::

::: Rem
To simplify the exposition we assume from now on that $G$ is simply connected.
:::

Cohomology of any complex of sheaves on a topological space carries an action of the cohomology algebra of the space; thus we have the functor of equivariant cohomology $$H_{{\bf G_O}\rtimes{{\mathbb G}_m}}^\bullet: D_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)\to 
H^\bullet_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)
-mod^{gr} = Coh^{{{\mathbb G}_m}}(N_{(\check{\mathfrak t}{}^*/W)^2}\Delta)$$ where $D_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr)$ denotes the bounded constructible equivariant derived category, and the grading on $H^*_{{\bf G_O}\rtimes{{\mathbb G}_m}}(\Gr,?)$ is the one by the cohomology degree.

::: thm
[]{#free_cohh label="free_cohh"} The functor $S: Rep({\check{G}})\to Perv_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)$ extends to a full imbedding $S_\hbar:\HC_\hbar^{fr}\to
D_{{\bf G_O}\rtimes {{\mathbb G}_m}}(\Gr)$, such that $$\label{cogokaph}
{\kappa_\hbar}\cong H_{{\bf G_O}\rtimes{{\mathbb G}_m}}^\bullet\circ S_\hbar.$$ Such an extension $S_\hbar$ (for a fixed isomorphism [\[cogokaph\]](#cogokaph){reference-type="eqref" reference="cogokaph"}) is unique.
:::
