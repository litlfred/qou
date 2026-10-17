---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-004-14-further-discussion
section_title: "Further discussion"
section_number: 1.4
pages: 12-13
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
text_source: latex
latex_prose_ratio: 0.965
latex_coverage_ratio: 0.99
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
[]{#families label="families"} We conclude the introduction with a brief discussion of twisted versions of our results and relations with supersymmetric gauge theory.

### Twisted ${\mathcal D}$-modules and families version

The results of this paper have natural analogues in which ${\mathcal D}$-modules on flag varieties are replaced by twisted ${\mathcal D}$-modules. The requisite arguments are formally identical, but we will only briefly summarize the picture here. We expect a more detailed account to appear in forthcoming work with Sam Gunningham.

The monodromic Hecke category $\widetilde \mathcal H_G$ fits into a family of twisted monodromic Hecke categories $\widetilde \mathcal H_{G,\lambda}$, indexed by characters $\lambda\in \mathfrak h^{\vee}$. Likewise, the dg category ${Ch}_G$ of unipotent character sheaves fits into a family of dg categories ${Ch}_{G, [\lambda]}$ of character sheaves with central character $[\lambda]\in H^\vee/W$.

::: expectation
Fix any $\lambda\in \mathfrak h^\vee$, with image $[\lambda]\in H^\vee/W$.

1\) The twisted monodromic Hecke category $\widetilde \mathcal H_{G, \lambda}$ is a semi-rigid Calabi-Yau monoidal category.

2\) The monoidal center and trace of $\widetilde \mathcal H_{G, \lambda}$ are both identified with character sheaves ${Ch}_{G, [\lambda]}$ with central character $[\lambda]\in H^\vee/W$.
:::

The Koszul duality of Hecke categories extends in an interesting way to other characters $\lambda\in\mathfrak h^\vee$. On the monodromic side, one has the twisted monodromic Hecke category $\widetilde \mathcal H_{G, \lambda}$. On the equivariant side, one introduces the centralizer $G^\vee_\lambda \subset G^\vee$ of a semi-simple representative of $\lambda$, a Borel subgroup $B^\vee_\lambda\subset
G^\vee_\lambda$, and the equivariant Hecke category $\mathcal H_{G^\vee_\lambda} = {\mathcal D}(B^\vee_\lambda\backslash
G^\vee_\lambda/B^\vee_\lambda)$. The results of [@BGS; @S; @BY] give an equivalence of monoidal categories $$\widetilde \mathcal H_{G, \lambda}^{per}\simeq \mathcal H_{G^\vee_\lambda}^{per}$$

Now if the above expectation is realized, then one can introduce a twisted 2-dimensional character theory $\widetilde{\chi}_{G,\lambda}$. It will satisfy a Langlands duality $$\widetilde{\chi}_{G,\lambda}^{per} \simeq \chi^{per}_{G^\vee_\lambda}$$ and in particular, its value on the circle will provide an equivalence $${Ch}_{G, [\lambda]}^{per} \simeq {Ch}_{G^\vee_\lambda}^{per}.$$ relating character sheaves on $G$ with central character $[\lambda]$ and unipotent character sheaves on the centralizer $G^\vee_\lambda$ in the dual group.

::: remark
At first encounter, the idea (derived from Koszul duality) to consider the Hecke categories $\mathcal H_{G^\vee_\lambda}$ as a family might seem bizarre. However, in [@reps] we establish (using the techniques developed in [@conns]) that the family of Hecke categories $\mathcal H_{G^\vee_\lambda}$ arises naturally by $S^1$-equivariant localization from an evident family of affine Hecke categories. One can then see its Koszul duality with $\widetilde \mathcal H_{G,
  \lambda}$ as a shadow of the Langlands duality for affine Hecke categories due to Bezrukavnikov [@Roma; @ICM].
:::

### Relation with gauge theory and geometric Langlands {#physics}

The character theory has an expected physical interpretation due to Witten [@Witten; @Atiyah Section 3.3], roughly coming from a topological twist of a certain maximally supersymmetric three-dimensional gauge theory. This relation is a dimensional reduction of the groundbreaking interpretation of the geometric Langlands correspondence as Montonen-Olive S-duality for maximally supersymmetric four-dimensional gauge theory due to Kapustin and Witten [@KW]. In particular, the Langlands duality for character theories should arise as a dimensionally reduced version of the geometric Langlands correspondence. Namely, Witten considers 4-dimensional ${\mathcal N=4}$ super-Yang-Mills in the "geometric Langlands" topological twist as studied in [@KW] (for any value of the twist and coupling parameter) reduced on 4-manifolds of the form $M^3\times S^1$. The supercharge in this theory has a perturbation which squares to rotation along the $S^1$-factor (this is closely related to the "$\Omega$-background" in the form studied in [@NW], or to the appearance of ${\mathcal D}$-modules from cyclic homology discovered in [@cyclic]). This supercharge still defines a differential when restricted to $S^1$-invariant modes, and can be used to define a $\mathbb Z/2$-graded 3-dimensional TFT (independent of parameters), which is the physical construction of the character theory. The parameter $\lambda\in \mathfrak h^\vee$ has the physical interpretation as a vacuum expectation value (vev) of a scalar field, so that $\mathfrak h^\vee/W$ appears as the moduli of vacua of the theory (much as the Hitchin base appears as the moduli of vacua or Seiberg-Witten base for supersymmetric gauge theories in four dimensions), with the unipotent version studied here arising at the conformal point.
