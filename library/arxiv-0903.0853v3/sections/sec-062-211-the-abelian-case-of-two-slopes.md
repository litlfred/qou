---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-062-211-the-abelian-case-of-two-slopes
section_title: "The abelian case of two slopes"
section_number: 21.1
pages: 110-111
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.978
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:abeliancase label="subsection:abeliancase"}

When the Newton polygon of $M_{0}$ has only two slopes $\mu < \nu$ with multiplicities $r,s$, so that we can write: $$A_{0} = \begin{pmatrix} z^{\mu} B & 0 \\ 0 & z^{\nu} C \end{pmatrix},
\quad B \in {\text{GL}}_{r}({\mathbf C}), \; C \in {\text{GL}}_{s}({\mathbf C}),$$ then the unipotent group ${\mathfrak{G}}_{A_{0}}$ is isomorphic to the vector space ${\text{Mat}}_{r,s}$ through the isomorphism: $$F \mapsto \begin{pmatrix} I_{r} & F \\ 0 & I_{s} \end{pmatrix}$$ from the latter to the former. Accordingly, the sheaf of unipotent groups $\Lambda_I(M_0)$ can be identified with the abelian sheaf $\Lambda$ on ${\mathbf{E}_{q}}$ defined by: $$\Lambda(U) := \{F \in {\text{Mat}}_{r,s}\bigl({\mathcal{O}}(p^{-1}(U))\bigr) ~ | ~
(\sigma_qF) (z^{\nu} C) = (z^{\mu} B) F \}.$$ This is actually a locally free sheaf, hence the sheaf of sections of a holomorphic vector bundle on ${\mathbf{E}_{q}}$, which we also write $\Lambda$ (more on this in section [\[section:vectorbundles\]](#section:vectorbundles){reference-type="ref" reference="section:vectorbundles"}). This bundle can be described geometrically as the quotient of the trivial bundle ${\mathbf C}^{*} \times {\text{Mat}}_{r,s}({\mathbf C})$ over ${\mathbf C}^{*}$ by the equivariant action of $q^{{\mathbf Z}}$ determined by the action $(z,F) \mapsto \bigl(q z,(z^{\mu} B) F (z^{\nu} C)^{-1}\bigr)$ of the generator $q$: $$\Lambda = \dfrac{{\mathbf C}^{*} \times {\text{Mat}}_{r,s}({\mathbf C})}
{(z,F) \sim \bigl(q z,(z^{\mu} B) F (z^{\nu} C)^{-1}\bigr)} 
\longrightarrow 
\dfrac{{\mathbf C}^{*}}{z \sim q z} = {\mathbf{E}_{q}}.$$ For details, see [@JSStokes; @JSfvqde]. This bundle is the tensor product of a line bundle of degree $\mu - \nu$ (corresponding to the "theta" factor $\sigma_qf = z^{\mu - \nu} f$) and of a flat bundle (corresponding to the "fuchsian" factor $\sigma_qF = B F C^{-1}$); we shall say that it is *pure (isoclinic)*. Now, the first cohomology group of such a vector bundle is a finite dimensional vector space whose dimension can be easily computed from its rank $r s$ and degree $\mu - \nu$: it is $r s (\nu - \mu)$. Actually, using Serre duality and an explicit frame of the dual bundle (made up of theta functions), one can provide an explicit coordinate system on $H^{1}({\mathbf{E}_{q}},\Lambda)$: this is done in [@JSfvqde], where the relation to the $q$-Borel transform is shown. In this section, we shall see how, in general, the non-abelian cohomology set $H^{1}({\mathbf{E}_{q}},\Lambda)$ can be described from successive extensions from the abelian situation.
