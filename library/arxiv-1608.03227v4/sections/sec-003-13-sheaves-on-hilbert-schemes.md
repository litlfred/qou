---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-003-13-sheaves-on-hilbert-schemes
section_title: "Sheaves on Hilbert schemes"
section_number: 1.3
pages: 5-6
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.991
latex_coverage_ratio: 0.939
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
The usual nested Hilbert scheme $\SymbolPrint{\Hilb^L_{1,n}}$

is a subvariety of $\Hilb_{1,n}^{free}$ defined by the commutativity constraint on $X,Y$: $$[X,Y]=0.$$ It turns out that the support of the homology of the complex $\bbS_\beta$ is contained in $\Hilb_{1,n}^L$. Hence the sheaf homology of the complex is the sheaf $$\SymbolPrint{\calS_\beta}=\SymbolPrint{\calS_\beta^{odd}}\oplus\SymbolPrint{\calS_\beta^{even}}:=\mathcal{H}^*(\Hilb_{1,n}^{free},\mathbb{S}_\beta)$$ on $\Hilb_{1,n}$ and we immediately have the following:

::: theorem
[]{#thm: spec seq label="thm: spec seq"} There is a spectral sequence with $E_2$ term being $$(\textup{H}^*(\Hilb^L_{1,n},\calS_\beta\otimes\wedge^k\calB),d)$$ $$d: \textup{H}^k(\Hilb^L_{1,n},\calS^{odd/even}_\beta\otimes\wedge^k\calB)\to
\textup{H}^{k-1}(\Hilb^L_{1,n},\calS^{even/odd}_\beta\otimes\wedge^k\calB),$$ that converges to $\mathbb{H}^k(\beta)$.
:::

We conjecture that one can extract the link invariant for $L(\beta)$ directly from the sheaf $\calS_\beta$ if $\beta$ is sufficiently positive

::: conjecture
For any $\beta\in\Brgr_n$ and sufficiently positive $k$ we have $$\textup{H}^{>0}(\Hilb^L_{1,n},\calS_{\beta\cdot Tw^k})=0.$$
:::

There is a natural projection from the nested Hilbert scheme to the usual Hilbert scheme $p: \Hilb_{1,n}\to\Hilb_n$ and it turns out that the push-forward $\SymbolPrint{p_*}(\mathcal{S}_\beta)\in
D_{T_{sc}}^{per}(\Hilb_n)$ has slightly better properties than $\calS_\beta$:

::: theorem
The element of $D_{T_{sc}}^{per}(\Hilb_n)$ $$\SymbolPrint{\calS_{[\beta]}}:=p_*(\calS_\beta)$$ depends only on the conjugacy class of $\beta$.
:::

In the sequel to this paper we compute the sheaf $\bbS_\beta$ for many elements of the braid group. That allows us to give a geometric description of the homology of a torus knot $T_{n,nk+1}$. More precisely, we study the positive braid $\beta_k\in \Brgrn$ such that $L(\beta_k)=T_{n,nk+1}$. We compute explicitly the sheaf corresponding to this braid. It is supported on the punctual Hilbert scheme: $\SymbolPrint{\Hilb_{1,n}^{0}}=\widetilde{\Hilb}^{0}_{1,n}/B$, $\widetilde{\Hilb}_{1,n}^{0}:=\widetilde{\Hilb}_{1,n}\cap \frn^2\times V$ and we show

::: theorem
[@OR][]{#thm:Tnk label="thm:Tnk"} For any $k\in \mathbb{Z}$ we have $$\calS_{\beta_k}=[\calO_{\Hilb_{1,n}^{0}}]^{vir}\otimes \det(\mathcal{B})^k,$$ where $[\calO_{\Hilb_{1,n}^0}]^{vir}$ is the Koszul complex defining the punctual Hilbert scheme $\widetilde{\Hilb}^0_{1,n}\subset \widetilde{\Hilb}_{1,n}^{free}$.
:::

The sheaf $\calO_{\Hilb_n^0(\CC^2)}\otimes \det(\mathcal{B})^k$ attracted a lot of attention in connection to combinatorics [@Hai], representation theory [@GS] and knot theory [@ORS; @GORS]. In particular, in [@ORS] it was conjectured that the global sections of this sheaf is a particular double-graded subspace of the space of Khovanov-Rozansky homology of the torus knot $T_{n,1+nk}$. We expect that the push forward of the complex $p_*([\calO_{\Hilb_{1,n}^0}]^{vir})$ is $\calO_{\Hilb_n^0(\CC^2)}$ and thus our theorem is consistent with this conjecture and its generalization in [@GORS].

In a forthcoming paper we explore this regular behavior to gain more insight into the behavior of our knot invariant on large classes of knots.
