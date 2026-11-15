---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-066-221-the-general-construction
section_title: "The general construction"
section_number: 22.1
pages: 114-115
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.967
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:vectorbundles label="subsection:vectorbundles"}

For details on the following, see [@JSfvqde]. To any $q$-difference module $M$ over ${{\mathbf C}(\{z\})}$, one can associate []{#not95 label="not95"} a holomorphic vector bundle ${\mathcal{F}}_{M}$ over ${\mathbf{E}_{q}}$ in such a way that the correspondence $M \leadsto {\mathcal{F}}_{M}$ is functorial and that the functor is faithful, exact and compatible with tensor products and duals. If one restricts to pure isoclinic modules with a fixed slope, the functor is moreover *fully* faithful (this follows immediately from the case of fuchsian modules, which is dealt with in [@JSGAL]); but this ceases to be true for arbitrary modules: for instance, if $M := ({{\mathbf C}(\{z\})},\sigma_q)$ and $N := ({{\mathbf C}(\{z\})},z^{-1}\sigma_q)$, then the function ${\theta_{q}}$ induces a morphism from ${\mathcal{F}}_{M}$ to ${\mathcal{F}}_{N}$, although $\text{Hom}(M,N) = 0$. This is one of the reasons why this functor is not very important in the present work (see however the remark further below).\
In order to describe ${\mathcal{F}}_{M}$, we shall assume for simplicity that the module $M$ is related to a $q$-difference system $\sigma_qX = A X$ such that $A$ and $A^{-1}$ are holomorphic all over ${\mathbf C}^{*}$, for instance, that $A$ is in Birkhoff-Guenther normal form. (In the general case, one just has to speak of germs at $0$ everywhere). The sheaf of holomorphic solutions over ${\mathbf{E}_{q}}$ is then defined by the relation: $$\label{not96}
{\mathcal{F}}_{M}(U) := \{X \in {\mathcal{O}}\bigl(p^{-1}(U)\bigr)^{n} ~ | ~\sigma_qX = A X\}.$$ This is a locally free sheaf, whence the sheaf of sections of a holomorphic vector bundle over ${\mathbf{E}_{q}}$ which we also write ${\mathcal{F}}_{M}$. The bundle ${\mathcal{F}}_{M}$ can be realized geometrically as the quotient of the trivial bundle ${\mathbf C}^{*} \times {\mathbf C}^{n}$ over ${\mathbf C}^{*}$ by an equivariant action of the subgroup $q^{{\mathbf Z}}$ of ${\mathbf C}^{*}$: $${\mathcal{F}}_{M} = \dfrac{{\mathbf C}^{*} \times {\mathbf C}^{n}}{(z,X) \sim \bigl(q z,A X)} 
\rightarrow \dfrac{{\mathbf C}^{*}}{z \sim q z} = {\mathbf{E}_{q}}.$$ The construction of the bundle $\Lambda$ in subsection [\[subsection:abeliancase\]](#subsection:abeliancase){reference-type="ref" reference="subsection:abeliancase"} corresponds to the $q$-difference system $(\sigma_qF) (z^{\nu} C) = (z^{\mu} B) F$, which is the "internal Hom" $\underline{\text{Hom}}(N,M)$ of the modules $M,N$ respectively associated to the $q$-difference systems with matrices $z^{\mu} B,z^{\nu} C$. From the compatibilities with tensor products and duals, one therefore draws: $$\Lambda = {\mathcal{F}}_{N}^{\vee} \otimes {\mathcal{F}}_{M}.$$

::: rema
From the exactness and the existence of slope filtrations, one deduces that the vector bundle associated to a $q$-difference module with integral slopes admits a flag of subbundles such that each quotient is "pure isoclinic", that is, isomorphic to the tensor product of a line bundle with a flat bundle. The functor sending the module $M$ to the vector bundle ${\mathcal{F}}_{M}$ *endowed with such a flag* is fully faithful.
:::
