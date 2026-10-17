---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-012-43-the-case-of-sylow-subgroup-of-prime-order
section_title: "The case of Sylow subgroup of prime order"
section_number: 4.3
pages: 17-18
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.988
latex_coverage_ratio: 0.965
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
Let us now consider the simplest nontrivial special case of Theorem [\[equiv\]](#equiv){reference-type="ref" reference="equiv"}, when the $p$-Sylow subgroup of $G$ has order $p$.

::: corollary
[]{#cyc label="cyc"} If $P=\Bbb Z/p$ then $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}G}=({\rm Ver}_p)^L$, where ${\rm Ver}_p$ is the Verlinde category (see Example [\[ex1\]](#ex1){reference-type="ref" reference="ex1"}(2)).
:::

Note that if $p=2$ then ${\rm Ver}_p=\mathrm{Vec}$. Thus, if $P=\Bbb Z/2$ then Corollary [\[cyc\]](#cyc){reference-type="ref" reference="cyc"} says that $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}G}=\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}L$.

So let us consider the case $p>2$ and compute the category $({\rm Ver}_p)^L$ more explicitly. Note that ${\rm Ver}_p={\rm Ver}_p^+\boxtimes {\rm Supervec}$, and ${\rm Ver}_p$ has no nontrivial symmetric tensor autoequivalences ([@O]), while ${\rm Ver}_p^+$ has no nontrivial tensor automorphisms of the identity functor. Thus, from Corollary [\[cyc\]](#cyc){reference-type="ref" reference="cyc"} we get $$\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}G}={\rm Ver}_p^+\boxtimes {\rm Supervec}^L.$$

The group of tensor automorphisms of the identity functor of ${\rm Supervec}$ is $\Bbb Z/2$. Hence, actions of $L$ on ${\rm Supervec}$ correspond to elements $H^2(L,\Bbb Z/2)$. Let $c\in H^2(L,\Bbb Z/2)$ be the element corresponding to the action as above, and let us compute $c$. Since the action of $L$ on $\Bbb Z/p$ factors through an action of $\Bbb Z/(p-1)$, the element $c$ is pulled back from a canonical element $\bar c\in H^2(\Bbb Z/(p-1),\Bbb Z/2)=\Bbb Z/2$.

::: proposition
[]{#nontri label="nontri"} The element $\bar c$ is nontrivial.
:::

::: proof
*Proof.* It suffices to show that the pullback of $\bar c$ to $\Bbb Z/2\subset \Bbb Z/(p-1)$ is nontrivial. For this purpose, it suffices to consider the semisimplification of $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}D_p$, where $D_p:=\Bbb Z/2\ltimes \Bbb Z/p$ is the dihedral group. In $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}D_p}$ we have an invertible object $X$ of vector space dimension $p-1$, which has composition series $\mathbf{k}_+,\mathbf{k}_-,...,\mathbf{k}_+,\mathbf{k}_-$, where $\mathbf{k}_+$ is the trivial representation of $\Bbb Z/2$ and $\mathbf{k}_-$ is the sign representation, and it suffices to show that $X$ has order $>2$. But we have $X=X^*\otimes \mathbf{k}_-$. Thus, $X$ cannot have order $2$, as desired. ◻
:::

Let $\widetilde L$ be the central extension of $L$ by $\Bbb Z/2$ defined by the cocycle $c$, and let $z$ be the generator of the central subgroup $\Bbb Z/2\subset \widetilde L$.

::: corollary
[]{#corro label="corro"} If $p$ is odd and $P=\Bbb Z/p$ then $$\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}G}\cong {\rm Ver}_p^+\boxtimes \mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(\widetilde L,z),$$ where $\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}(\widetilde L,z)$ is the category of representations of $\widetilde L$ on supervector spaces, so that $z$ acts by the parity operator.
:::
