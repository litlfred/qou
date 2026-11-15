---
doc_id: arxiv-2601.07042v1
doc_title: "A Tannakian description of the local Kaletha gerbe"
section_id: sec-006-22-limits-of-gerbes
section_title: "Limits of gerbes"
section_number: 2.2
pages: 6-7
source_pdf: 2601.07042v1.pdf
source_sha256: c2f3e302624e7abb
toc_source: outline
text_source: latex
latex_prose_ratio: 0.973
latex_coverage_ratio: 0.96
doc_brief: "A Tannakian description of the local Kaletha gerbe — We construct, for a p-adic field F, an explicit semisimple Tannakian category RigIsocF whose category of fiber functors recovers Kaletha’s Galois"
---
For $s \mid s'$, we have a fully faithful embedding of categories from $\iota_{s,s'} \colon P_{E/F,s}$ to $P_{E/F,s'}$, which sends the triple $(V, \Phi, \mathcal{D})$ to the triple $(V, \Phi, \mathcal{D}_{s'/s})$, where $\mathcal{D}_{s'/s}$ is the ${\prod_{\Gamma_{E/F}}\frac{1}{s'}\mathbb{Z}}$-grading of $V$ given by $V_{(b_{\sigma}/s')} = V_{([b_{\sigma}/(s'/s)]/s)}$ if $s'/s$ divides $b_{\sigma}$ for all $\sigma$, and is zero otherwise.

We define the category $P_{E/F}$ to be the direct limit $\varinjlim_{s} P_{E/F,s}$ over all positive integers $s$ (direct limit of categories in the obvious sense). Explicitly, a morphism between the objects $(V, \Phi, \mathcal{D}, s)$ and $(V', \Phi', \mathcal{D}', s')$ can be identified with a morphism between $\iota_{s, ss'}(V, \Phi, \mathcal{D}, s)$ and $\iota_{s', ss'}(V', \Phi', \mathcal{D}', s')$ in the category $P_{E/F,ss'}$.

Note that if one looks at a subspace $V_{(b_{\sigma}c/sc)}$, viewed as an object of $P_{E/F,sc}$, then although a priori it only has a basis on which $\mathfrak{f}_{E}^{sc}$ acts by $\prod_{\sigma \in \Gamma_{E/F}} \sigma(\varpi_{E})^{b_{\sigma}c}$, one can say even more: It has an $L_{E}$-basis on which $\mathfrak{f}_{E}^{s}$ acts by $\prod_{\sigma \in \Gamma_{E/F}} \sigma(\varpi_{E})^{ b_{\sigma}}$, as follows from the general theory of $\Phi$-$L_{E}$ spaces (cf. [@Kottwitzisoci p.11]). This shows that the embedding $\iota_{s,s'}(P_{E/F,s})$ may be described as all tuples whose only non-zero graded components have indices which may be written as $(\frac{b_{\sigma}(s'/s)}{s(s'/s)})_{\sigma}$. The identification of the gerbe corresponding to $P_{E/F,s}$ with $\mathcal{E}_{(c_{\sigma})_{\sigma}}$ is compatible for varying $s$, provided that we choose the sections compatibly (which is always possible), and hence we see that the Tannakian category $P_{E/F}$ is banded by $\prod_{\Gamma_{E/F}} \mathbb{D}(L_{E})$ (where $\mathbb{D}$ is the pro-torus with character group $\mathbb{Q}$), and corresponds to the anti-canonical class in $H^{2}(\Gamma_{L_{E}/E}, \prod_{\Gamma_{E/F}} \mathbb{D}(L_{E}))$ given by the inverse limit of the finite anti-canonical classes (these transition maps are given for $s \mid s'$ by the multiplication-by-$s'/s$ map $\frac{1}{s'}\mathbb{Z}/\mathbb{Z}\to \frac{1}{s}\mathbb{Z}/\mathbb{Z}$).

For $s \mid s'$, it is worth investigating the transition maps on bands corresponding to the map of extensions $p_{s',s} \colon \mathcal{E}_{P_{E/F,s'}} \to \mathcal{E}_{P_{E/F,s}}$. First, we need to say what this map of extensions is: Note that, by base-changing to the gerbe $\mathcal{E}_{(c_{\sigma})_{\sigma}}$ to $\overline{F}$, we get the extension $$1 \to \prod_{\Gamma_{E/F}} \mathbb{G}_{m}(\overline{F}) \to \mathcal{E}_{(c'_{\sigma})_{\sigma}} \to \Gamma_{\overline{F}/E} \to 1,$$ where each $c_{\sigma}'$ denotes the inflated anti-canonical class $\Gamma_{\overline{F}/E}^{2} \to \Gamma_{E_{s}/E}^{2} \xrightarrow{c_{\sigma,s}} \prod_{\Gamma_{\overline{F}/E}} E_{s}^{\times}$---we can do the identical thing for $s'$. We then get a morphism of group extensions $$\begin{tikzcd}
1 \arrow{r} & \prod_{\Gamma_{E/F}} \mathbb{G}_{m}(\overline{F}) \arrow{r} \arrow["s'/s"]{d} & \mathcal{E}_{(c_{\sigma,s'}')_{\sigma}} \arrow{d} \arrow{r} & \Gamma_{\overline{F}/E} \arrow[equals]{d} \to 1 \\
1 \arrow{r} & \prod_{\Gamma_{E/F}} \mathbb{G}_{m}(\overline{F}) \arrow{r} & \mathcal{E}_{(c_{\sigma,s}')_{\sigma}} \arrow{r} & \Gamma_{\overline{F}/E} \to 1,
\end{tikzcd}$$ and we get a commutative square of Tannakian categories $$\begin{tikzcd}
P_{E/F,s',\overline{L}} \arrow{r} & \text{Rep}_{\overline{L}}(\mathcal{E}_{(c_{\sigma,s'}')_{\sigma}}) \\
P_{E/F,s,\overline{L}} \arrow{r} \arrow{u} & \text{Rep}_{\overline{L}}(\mathcal{E}_{(c_{\sigma,s}')_{\sigma}}), \arrow{u}
\end{tikzcd}$$ where the left-hand map is the transition map described above, the right-hand map is the one induced by the above morphism of extensions, and the horizontal ones are induced by the equivalence of Tannakian categories described above.

By $P_{E/F,s,\overline{L}}$ we mean the category of $\prod_{\Gamma_{E/F}} \frac{1}{s}\mathbb{Z}$-graded finite-dimensional $\overline{L}$-vector spaces $V$ with a $W_{E}$-semilinear action, such that each $V_{(a_{\sigma}/s)}$ is $W_{E}$-stable and $(V_{(a_{\sigma}/s)})^{\Gamma_{\overline{L}/L_{E}}}$ has an $L_{E}$-basis (which implies that it is an $\overline{L}$-basis of $V_{(a_{\sigma}/s)}$) on which $\mathfrak{f}_{E}^{s}$ acts by the scalar $\prod_{\Gamma_{E/F}} \sigma(\varpi_{E})^{a_{\sigma}}$. By $\text{Rep}_{\overline{L}}(\mathcal{E}_{(c_{\sigma,s}')})$, we mean the Tannakian category of representations $(V, \rho)$ (over $\overline{L}$) of $\mathcal{E}_{(c_{\sigma,s}')}$. The equivalence of the previous subsection goes through for these two categories after some elementary modifications. We check that, starting with an object $(V, \Phi, \mathcal{D})$, going right and then up gives the representation $(V, \rho)$, where $\rho$ sends $\mathfrak{f}_{E}$ to $\Phi$, and the corresponding $E$-morphism $\prod \mathbb{G}_{m} \to \mathrm{GL}_{V}$ is determined by acting on the subspace $V_{(h_{\sigma}/s)} \subseteq V$ via $$(a_{\sigma}) \cdot v = \prod a_{\sigma}^{h_{\sigma}(s'/s)}v.$$

On the other hand, going up and then right gives the representation $(V, \rho')$, where $\rho'$ sends $\mathfrak{f}_{E}$ to $\Phi$ with $E$-morphism determined by acting on $V_{(h'_{\sigma}/s')}$ by $$(a_{\sigma}) \cdot v= \prod a_{\sigma}^{h'_{\sigma}}v.$$ Now the result follows from the fact that $h'_{\sigma} = h_{\sigma}(s'/s)$ for all $\sigma$, by construction of our transition functor.

::: cor
The transition morphism of Tannakian categories $P_{E/F,s} \to P_{E/F,s'}$ gives the $s'/s$-power morphism on bands (via the identifications of the above Corollary [\[productgerbe\]](#productgerbe){reference-type="ref" reference="productgerbe"}, using compatible sections).
:::
