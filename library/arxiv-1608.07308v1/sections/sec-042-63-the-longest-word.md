---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-042-63-the-longest-word
section_title: "The longest word"
section_number: 6.3
pages: 50-52
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
text_source: latex
latex_prose_ratio: 0.925
latex_coverage_ratio: 0.772
---
[]{#sub:longest label="sub:longest"}

Let us describe the sheaf for the positive lift $\sigma_1\sigma_2\sigma_1$ of the longest word in $S_3$. Remark that the following equation holds for all $a$ and $b$: $$\label{eqn:conj for 121}
\mathop{\mathrm{Tr}}(\sigma_1\sigma_2\sigma_1\mathcal{L}_2^{a}\mathcal{L}_3^{b})=\mathop{\mathrm{Tr}}(\sigma_2\sigma_1\sigma_1\mathcal{L}_2^{a}\mathcal{L}_3^{b}),$$ since $\sigma_1$ commutes both with $\mathcal{L}_2$ and $\mathcal{L}_3$ and the trace satisfies $\mathop{\mathrm{Tr}}(\sigma \sigma') = \mathop{\mathrm{Tr}}(\sigma'\sigma)$. By Corollary [\[cor:trace twisted identity\]](#cor:trace twisted identity){reference-type="ref" reference="cor:trace twisted identity"}, these traces are isomorphic up to a twist by a permutation $(1\ 2)$. In particular, the left hand side of [\[eqn:conj for 121\]](#eqn:conj for 121){reference-type="eqref" reference="eqn:conj for 121"} is supported on $\{x_1=x_3\}$, while the right hand side is supported on $\{x_2=x_3\}$. Furthermore, $$\iota_*(\sigma_2\sigma_1\sigma_1) = L_2\otimes \iota_*(\sigma_2)=L_2\otimes \mathcal{O}_{\mathrm{FHilb}(2\sim 3)}.$$ Note that in the notations of Section [\[sec:n=3\]](#sec:n=3){reference-type="ref" reference="sec:n=3"}, $\mathrm{FHilb}(2\sim 3)=Z_2\cup Z_5$. There is a natural involution $j_{12}$ on $\mathrm{FHilb}_3$ which exchanges $x_1$ and $x_2$ in $Z_1$, acts trivially on $Z_2$ and $Z_3$ and permutes $Z_4$ and $Z_5$. We arrive at the following conjecture:

::: conjecture
One has $\iota_*(\sigma_1\sigma_2\sigma_1)=j_{12}^{*}(L_2\otimes \mathcal{O}_{Z_2\cup Z_5}).$
:::

## The figure eight knot {#sub:figure eight}

In this section we describe a sheaf for the braid $\beta=\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$ representing the figure eight knot. There is a skein exact sequence relating $B_{\beta}$ with the following objects in $\mathrm{SBim}_3$: $$\sigma_1\sigma_2\sigma_1\sigma_2^{-1}=\sigma_2\sigma_1, \sigma_1\sigma_1\sigma_2^{-1}=\mathcal{L}_2\sigma_2^{-1}.$$ More precisely, there is an exact sequence: $$\label{skein fig 8}
0\xleftarrow{}\sigma_2\sigma_1\xleftarrow{}\mathop{\mathrm{Cone}}\left[\mathcal{L}_2\sigma_2^{-1}\xleftarrow{x_1-x_2} \mathcal{L}_2\sigma_2^{-1}\right]\xleftarrow{}B_{\beta}\xleftarrow{} 0.$$

::: proposition
[]{#prop:cone label="prop:cone"} The following identity holds: $$\iota_*\mathop{\mathrm{Cone}}\left[\sigma_2^{-1}\xleftarrow{x_1-x_2} \sigma_2^{-1}\right]\simeq \left[\mathcal{L}_2\mathcal{L}_3^{-1}\oplus qt\mathcal{L}_3^{-1}\right]_{Z_2}.$$
:::

::: proof
*Proof.* By [\[eq:mf\]](#eq:mf){reference-type="eqref" reference="eq:mf"} one has: $$\mathcal{O}_{\mathrm{FHilb}(1\sim 2)}\simeq [\mathcal{O}_{\mathrm{FHilb}_3(\mathbb{C})}\xleftarrow{x_1-x_2}q\mathcal{O}_{\mathrm{FHilb}_3(\mathbb{C})}\xleftarrow{y_{21}}qt\mathcal{L}_2^{-1}|_{\mathrm{FHilb}(1\sim 2)}]$$ (note that this is also a skein exact sequence for $\sigma_1^{-1},\mathbf{1}, \sigma_1$) and $$\iota_*(\sigma_2^{-1})=\mathcal{L}_2\mathcal{L}_3^{-1}\otimes \mathcal{O}_{\mathrm{FHilb}(2\sim 3)}.$$ Since $\mathcal{O}_{\mathrm{FHilb}(2\sim 3)}\otimes \mathcal{O}_{\mathrm{FHilb}(1\sim 2)}=\mathcal{O}_{Z_2}$, one has an exact sequence: $$0\leftarrow{} \mathcal{L}_2\mathcal{L}_3^{-1}|_{Z_2}\xleftarrow{} \iota_*\mathop{\mathrm{Cone}}\left[\sigma_2^{-1}\xleftarrow{x_1-x_2} \sigma_2^{-1}\right] \xleftarrow{}qt\mathcal{L}_3^{-1}|_{Z_2}
\xleftarrow{} 0.$$ It remains to notice that $$\mathop{\mathrm{Ext}}_{Z_2}(\mathcal{L}_2\mathcal{L}_3^{-1},\mathcal{L}_3^{-1})=H^{*}(Z_2,L_2^{-1})=H^{*}(\mathbb{P}^1,\mathcal{O}(-1))=0.$$ ◻
:::

::: proposition
Consider the braid $\beta=\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$ representing the figure eight knot. Then, assuming Conjecture [\[conj:1\]](#conj:1){reference-type="ref" reference="conj:1"} and [\[conj:knots\]](#conj:knots){reference-type="ref" reference="conj:knots"}, one has $$\iota_*(\beta)=\mathcal{O}_{\mathbb{P}^1}\oplus qt\mathcal{L}_2\mathcal{L}_3^{-1}.$$
:::

::: proof
*Proof.* By [\[skein fig 8\]](#skein fig 8){reference-type="eqref" reference="skein fig 8"} and Proposition [\[prop:cone\]](#prop:cone){reference-type="ref" reference="prop:cone"} one has: $$0\xleftarrow{}\mathcal{O}_{Z_2}\xleftarrow{\alpha}\left[\mathcal{L}_2^2\mathcal{L}_3^{-1}\oplus qt\mathcal{L}_2\mathcal{L}_3^{-1}\right]_{Z_2}\xleftarrow{}qt(\iota_*B_{\beta})\xleftarrow{} 0.$$ Let us compute the map $\alpha$. Remark that: $$\mathop{\mathrm{Hom}}_{Z_2}(\mathcal{L}_2\mathcal{L}_3^{-1},\mathcal{O})=H^0(Z_2,\mathcal{L}_2^{-1}\mathcal{L}_3)=H^0(\mathbb{P}^1,\mathcal{O}(1)\oplus qt\mathcal{O}(-2)),$$ $$\mathop{\mathrm{Hom}}_{Z_2}(\mathcal{L}_2^2\mathcal{L}_3^{-1},\mathcal{O})=H^0(Z_2,\mathcal{L}_2^{-2}\mathcal{L}_3)=H^0(\mathbb{P}^1,\mathcal{O}\oplus qt\mathcal{O}(-3)).$$ Therefore $\alpha$ is the unique degree 1 map $\mathcal{L}_2^2\mathcal{L}_3^{-1}\to \mathcal{O}$ and vanishes on $\mathcal{L}_2\mathcal{L}_3^{-1}$, so $$\iota_*B_{\beta}\simeq \mathcal{L}_2\mathcal{L}_3^{-1}\oplus q^{-1}t^{-1}\mathop{\mathrm{Cone}}[\mathcal{O}\xleftarrow{\alpha} \mathcal{L}_2^2\mathcal{L}_3^{-1}]\simeq \mathcal{O}_{\mathbb{P}^1}\oplus \mathcal{L}_2\mathcal{L}_3^{-1}.$$ ◻
:::

Using this result, we can compute the reduced homology of $\beta\cdot \mathbf{FT}_2^{a}\mathbf{FT}_3^{b}$ by computing the homology of each summand individually. Since $\mathrm{FHilb}_3(\mathrm{point})$ is a blowup of the punctual Hilbert scheme of 3 points, and $\mathbb{P}^1$ is the exceptional divisor, the tautological bundle is trivial on $\mathbb{P}_1$: $\overline{\mathcal{T}}_3\otimes \mathcal{O}_{\mathbb{P}^1}\simeq (q+t)\mathcal{O}_{\mathbb{P}^1}$. Similarly, $\mathbf{FT}_3\otimes \mathcal{O}_{\mathbb{P}^1}\simeq qt\mathcal{O}_{\mathbb{P}^1}$. We get the following equation: $$\label{eq: 3 strand square}
\int_{\mathrm{FHilb}_3(\mathrm{point})}\mathcal{O}_{\mathbb{P}^1}\otimes \mathbf{FT}_2^{a}\mathbf{FT}_3^{b}\otimes \wedge^{\bullet}\overline{\mathcal{T}}_3^{\vee}=
(1+aq^{-1})(1+at^{-1})(qt)^{b}\int_{\mathbb{P}^1}\mathcal{O}(a).$$

Equations [\[eq: 3 strand square\]](#eq: 3 strand square){reference-type="eqref" reference="eq: 3 strand square"} and [\[eqn:3 strand torus\]](#eqn:3 strand torus){reference-type="eqref" reference="eqn:3 strand torus"} can be used to compute the homology of $\beta\cdot \mathcal{L}_2^{a}\mathcal{L}_3^{b}$ for all $a$ and $b$. In particular: $$H^*(\mathrm{FHilb}_3(\mathrm{point}),\mathcal{L}_2\mathcal{L}_3^{-1})=H^*(\mathrm{FHilb}_3(\mathrm{point}),\mathcal{L}_3^{-1})=0,$$ $$H^*(\mathrm{FHilb}_3(\mathrm{point}),\mathcal{L}_3^{-2})=H^{*+1}(\mathbb{P}^1,\mathcal{O}(-1))=0,$$ $$H^*(\mathrm{FHilb}_3(\mathrm{point}),\mathcal{L}_2\mathcal{L}_3^{-2})=H^{*+1}(\mathbb{P}^1,\mathcal{O})=\mathbb{C}[1],$$ so $$\int_{\mathrm{FHilb}_3(\mathrm{point})}\mathcal{L}_2\mathcal{L}_3^{-1}\otimes \wedge^{\bullet}\overline{\mathcal{T}}_3^{\vee}=a\mathbb{C}[1],$$ and $$\mathop{\mathrm{HHH}}(\beta)=(1+aq^{-1})(1+at^{-1})+a\sqrt{qt}.$$ One can compare this with [@DGR Table 5.7].

# Categorical idempotents and equivariant localization {#sec:equiv}
