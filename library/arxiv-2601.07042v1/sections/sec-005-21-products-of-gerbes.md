---
doc_id: arxiv-2601.07042v1
doc_title: "A Tannakian description of the local Kaletha gerbe"
section_id: sec-005-21-products-of-gerbes
section_title: "Products of gerbes"
section_number: 2.1
pages: 4-6
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.906
doc_brief: "A Tannakian description of the local Kaletha gerbe — We construct, for a p-adic field F, an explicit semisimple Tannakian category RigIsocF whose category of fiber functors recovers Kaletha’s Galois"
---
[]{#sec:prod label="sec:prod"}

::: defn
Fix $s \in \mathbb{N}$. Then we define the category $P_{E/F, s}$ as follows.

-   Objects are triples $(V, \Phi, \mathcal{D})$, where $V$ is a finite-dimensional $L_{E}$-vector space, $\Phi \colon V \to V$ is an $\mathfrak{f}_{E}$-semilinear automorphism, and $\mathcal{D}$ is a $\prod\limits_{\Gamma_{E/F}} \frac{1}{s}\mathbb{Z}$-grading on $V$ such that the subspace $V_{(b_{\sigma}/s)_{\sigma}}$ has an $L_{E}$-basis on which $\Phi^{s}$ acts by the scalar $\prod\limits_{\gamma \in \Gamma_{E/F}} \gamma(\varpi_{E})^{b_{\gamma}}$.

-   Morphisms in $P_{E/F,s}$ will be $\Phi$-equivariant morphisms of $L_{E}$-spaces which preserve the gradings.
:::

::: lem
The category $P_{E/F, s}$ can be equipped with the structure of a Tannakian category over $E$ in a natural way. The forgetful functor $\omega_{P_{E/F, s}}: P_{E/F, s} \to \mathrm{Vect}_{L_E}$ is a fiber functor defined over $L_E$.
:::

::: proof
*Proof.* There is a natural functor $\otimes \colon P_{E/F,s} \times P_{E/F,s} \to P_{E/F,s}$ which sends $(V, \Phi, \mathcal{D}) \times (V', \Phi', \mathcal{D}')$ to the triple $(V \otimes_{L_{E}} V', \Phi \otimes \Phi', \mathcal{D} \otimes \mathcal{D}')$, where the first two terms are clear and the grading $\mathcal{D} \otimes \mathcal{D}'$ is given by $$(V \otimes V')_{(b_{\sigma}/s)_{\sigma}} = \bigoplus_{(c_{\sigma}/s)_{\sigma} \in \prod\limits_{\Gamma_{E/F}} \frac{1}{s}\mathbb{Z}} V_{(c_{\sigma}/s)_{\sigma}} \otimes_{L_{E}} V'_{(\frac{b_{\sigma} - c_{\sigma}}{s})_{\sigma}}.$$

The above construction gives a well-defined tensor functor on $P_{E/F,s}$. Denote by $\textbf{1}_{P_{E/F,s}}$ the object given by the vector space $L_{E}$ with the usual $\mathfrak{f}_{E}$-action concentrated in the $(0)_{\sigma}$-graded piece. Then $P_{E/F,s}$ is a rigid abelian tensor category with identity object $\textbf{1}_{P_{E/F,s}}$. Moreover, the endomorphism algebra of $\textbf{1}_{P_{E/F,s}}$ is identified with $E$. Finally, we note that the functor $\omega_{P_{E/F,s}} \colon P_{E/F,s} \to \text{Vect}_{L_{E}}$ is an $E$-linear exact tensor functor, making $P_{E/F,s}$ a Tannakian category over $E$ which is neutralized by the extension $L_{E}$. ◻
:::

If $\Gamma$ is a profinite group acting continuously on an abelian group $A$ and we fix $c \in Z^{2}(\Gamma,A)$, there is a standard way to construct a group extension of $\Gamma$ by $A$ which we use throughout this paper. Namely, one defines $\mathcal{E}$ as a set by $A \times \Gamma$, with group multiplication given by $(a,g) \cdot (b,h) = (a \cdot \prescript{g}{}b \cdot c(g,h), gh)$. Observe that there is a natural set-theoretic section $\Gamma \to \mathcal{E}$ sending $g$ to $(1,g)$.

We now identify the gerbe corresponding to the category $P_{E/F, s}$. For each $\sigma \in \Gamma_{E/F}$, the element $\sigma(\varpi_{E})$ determines a cocycle of $\Gamma_{E_{s}/E}$ representing the anti-canonical class in $H^{2}(\Gamma_{E_{s}/E}, E_{s}^{\times})$, given explicitly by $c_{\sigma}(\mathfrak{f}_{E}^{i}, \mathfrak{f}_{E}^{j}) = 1$ if $i+j < s$, and $\sigma(\varpi_{E})$ otherwise. We will consider a group extension corresponding to the 2-cocycle $(c_{\sigma})_{\sigma}$ of $\Gamma_{E_{s}/E}$ valued in $\prod_{\Gamma_{E/F}} \mathbb{G}_{m}(E_{s})$, given by $$1 \to  \prod_{\Gamma_{E/F}} \mathbb{G}_{m}(E_{s}) \to  \widetilde{\prod}_{\Gamma_{E/F}} \mathcal{E}_{c_{\sigma}} \to \Gamma_{E_{s}/E} \to 1,$$ where by "$\widetilde{\prod}$" we mean that the product is fibered with respect to the projection of each $\mathcal{E}_{c_{\sigma}}$ to $\Gamma_{E_{s}/E}$. Denote this Galois gerbe by $\mathcal{E}_{(c_{\sigma})_{\sigma}}$.

We now make the following claim:

::: claim
The category $P_{E/F, s}$ is isomorphic as Tannakian categories over $E$ to $\text{Rep}_{E_{s}}(\mathcal{E}_{(c_{\sigma})_{\sigma}})$.
:::

Before proving the claim, we first investigate the latter Tannakian category. Let $\rho \colon \mathcal{E}_{(c_{\sigma})_{\sigma}} \to \text{Aut}(V)$ be a representation of $\mathcal{E}_{(c_{\sigma})_{\sigma}}$, for a finite-dimensional $E_{s}$-vector space $V$ . The Galois gerbe $\mathcal{E}_{(c_{\sigma})_{\sigma}}$ comes, by construction, equipped with a section $\Gamma_{E_{s}/F} \to \mathcal{E}_{(c_{\sigma})_{\sigma}}$, which allows us to identify it with pairs $((a_{\sigma}), x)$ for $a_{\sigma} \in E_{s}^{\times}$ for each $\sigma \in \Gamma_{E/F}$ and $x \in \Gamma_{E_{s}/E}$, where the group operation is $$((a_{\sigma})_{\sigma}, x)((b_{\sigma})_{\sigma},y) = ((a_{\sigma}x(b_{\sigma})c_{\sigma}(x,y))_{\sigma}, xy).$$

Our fixed representation $\rho$ gives an $\mathfrak{f}_{E}$-semilinear automorphism $\Phi := \rho((1_{\sigma}), \mathfrak{f}_{E})$ of $V$, which is such that $\Phi^{s}$ acts by $\rho((\sigma(\varpi_{E})), 1)$; note also that $\rho \colon \prod_{\Gamma_{E/F}} \mathbb{G}_{m}(E_{s}) \to \mathrm{GL}_{V}$ must be an algebraic homomorphism. Via simultaneous diagonalization, we may decompose $V$ into a direct sum $V = \bigoplus\limits_{\prod_{\Gamma_{E/F}} \mathbb{Z}} V_{(h_{\sigma})_{\sigma}}$, where $(\mathbb{G}_{m})_{\tau}$ acts on $V_{(h_{\sigma})_{\sigma}}$ via $x \cdot v = x^{h_{\tau}}v$ for each $x \in (\mathbb{G}_{m})_{\tau}(E_{s})$. Note that each subspace $V_{(h_{\sigma})}$ is $\Phi$-stable, and also that $\Phi^{s}$ must act on $V_{(h_{\sigma})}$ by the scalar $\prod_{\Gamma_{E/F}} \sigma(\varpi_{E})^{h_{\sigma}}$. A morphism of $\mathcal{E}_{(c_{\sigma})}$-representations from $V$ to $W$ sends $V_{(h_{\sigma})}$ to $W_{(h_{\sigma})}$ for all tuples $(h_{\sigma})$ and is $\Phi$-equivariant.

We now prove the claim.

::: proof
*Proof.* We first define a functor from $\text{Rep}_{E_{s}}(\mathcal{E}_{(c_{\sigma})})$ to $P_{E/F,s}$; for a representation $(V, \rho)$, we send it to $(V \otimes_{E_{s}} L_{E}, \Phi \otimes \text{id}_{L_{E}}, \mathcal{D})$, where $\mathcal{D}$ is the grading induced by tensoring the $\prod_{\Gamma_{E/F}} \frac{1}{s} \mathbb{Z}$-grading $V_{(h_{\sigma}/s)} := V_{(h_{\sigma})}$ with $L_{E}$ over $E_{s}$. A morphism from $(V, \rho)$ to $(W, \rho')$ will go to the morphism given by applying the functor $- \otimes \text{id}_{L_{E}}$; this construction evidently defines a morphism of Tannakian categories over $E$. There is also an inverse functor, given by sending the tuple $(V, \Phi, \mathcal{D})$ to the representation given as a vector space $V'$ by the $E_{s}$-span of any choice of $L_{E}$-bases of $V_{(h_{\sigma}/s)}$ (for all tuples) such that $\Phi^{s}$ acts by $\prod_{\Gamma_{E/F}} \sigma(\varpi_{E})^{h_{\sigma}}$. Note that this vector space does not depend on the choice of basis: Indeed, given any $v$ on which $\Phi^{s}$ acts by $\lambda := \prod \sigma(\varpi_{E})^{h_{\sigma}}$ and choice of basis $(e_{i})$ for the corresponding graded piece, writing $v = \sum a_{i}e_{i}$ for $a_{i} \in L_{E}$ gives that $$\sum (a_{i} \lambda)e_{i} = \sum (\mathfrak{f}_{E}^{s}(a_{i})\lambda) e_{i},$$ which means that $\mathfrak{f}_{E}^{s}(a_{i}) = a_{i}$ for all $i$, so that $a_{i} \in E_{s}$.

The map $\rho$ is defined by sending $((1_{\sigma}), \rho)$ to $\Phi$ and $(\mathbb{G}_{m})_{\tau}$ to the linear operator on $V'$ determined by $x \cdot v = x^{h_{\sigma}}v$ for any $v$ in the $E_{s}$-span of a basis of the graded component $V_{(h_{\sigma}/s)}$. This is a well-defined representation, since for any $(a_{\sigma})\in \prod_{\Gamma_{E/F}} \mathbb{G}_{m}(E_{s})$, we have that the maps $\Phi \circ (a_{\sigma}) \circ \Phi^{-1}$ and $\mathfrak{f}_{E} (a_{\sigma}) \mathfrak{f}_{E}^{-1}$ are $L_{E}$-linear and act on a vector element $v$ in $V'_{(h_{\sigma}/s)}$ as follows: $$\mathfrak{f}_{E} (a_{\sigma}) \mathfrak{f}_{E}^{-1}v = ((\mathfrak{f}_{E}(a_{\sigma})),1) \cdot v = (\prod_{\Gamma_{E/F}} \mathfrak{f}_{E}(a_{\sigma})^{h_{\sigma}})v,$$ and we also have (using the $\Phi$-stability of $V'_{(h_{\sigma})}$) that $$(\Phi \circ (a_{\sigma}) \circ \Phi^{-1})v = \Phi( (a_{\sigma}) \cdot (\Phi^{-1}(v))) = \Phi(\prod a_{\sigma}^{h_{\sigma}}\Phi^{-1}(v)) = (\prod \mathfrak{f}_{E}(a_{\sigma})^{h_{\sigma}})v,$$ as desired. These define mutually-inverse functors, giving the desired equivalence. ◻
:::

::: cor
[]{#productgerbe label="productgerbe"} The gerbe over $\text{Spec}(E)_{\text{fpqc}}$ corresponding to the Tannakian category $P_{E/F,s}$ is isomorphic to the product of the gerbes (as fibered categories over $\text{Spec}(E)_{\text{fpqc}}$) $\prod_{\sigma \in \Gamma_{E/F}} \mathcal{E}_{c_{\sigma}}$. In particular, it is banded by the $E$-group scheme $\prod_{\Gamma_{E/F}} \mathbb{G}_{m}$ and corresponds to the anti-canonical class in $H^{2}(\Gamma_{L_{E}/E}, \prod_{\Gamma_{E/F}} L_{E}^{\times})$ corresponding to the element $(-1/s)_{\sigma} \in \prod_{\Gamma_{E/F}} \mathbb{Q}/\mathbb{Z}$.
:::

What the above construction does is give an isomorphism of $\prod_{\Gamma_{E/F}}\mathbb{G}_{m}$-gerbes from $\mathcal{E}_{P_{E/F,s}}$ to $\mathcal{E}_{(c_{\sigma})_{\sigma}}$; note that since $H^{1}(\Gamma_{L_{E}/E}, \prod_{\Gamma_{E/F}} L_{E}^{\times})$ vanishes, this isomorphism is unique up to conjugation by an element of $\prod_{\Gamma_{E/F}} L_{E}^{\times}$, which we will see later does not affect cohomology.
