---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-007-32-compatibility-of-semisimplification-with-equi
section_title: "Compatibility of semisimplification with equivariantization"
section_number: 3.2
pages: 13-14
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.979
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
Now let $\mathcal{C}$ be a tensor category and $L$ be a finite group acting on $\mathcal{C}$. Let $\mathcal{C}^L$ be the $L$-equivariantization of $\mathcal{C}$ ([@EGNO], Subsection 4.15). The following lemma is easy ([@EGNO], Exercise 4.15.3).

::: lemma
[]{#equivar label="equivar"} If $$1\to N\to G\to L\to 1$$ is an exact sequence of groups then $L$ acts naturally on $\mathop{\mathrm{Rep}}\nolimits_{\bold k} N$, and $(\mathop{\mathrm{Rep}}\nolimits_{\bold k} N)^L\cong \mathop{\mathrm{Rep}}\nolimits_{\bold k} G$.
:::

Clearly, any action of $L$ on $\mathcal{C}$ descends to its action on the semisimplification $\overline{\mathcal{C}}$.

::: proposition
[]{#commu label="commu"} If $|L|\ne 0$ in $\mathbf{k}$ and $L$ preserves the spherical structure of $\mathcal{C}$ then $L$-eqiuvariantization commutes with semisimplification. In other words, we have a natural equivalence of tensor categories $\overline{\mathcal{C}^L}\cong \overline{\mathcal{C}}^L$.
:::

::: proof
*Proof.* We have a natural forgetful functor $F: \mathcal{C}^L\to \mathcal{C}$. We claim that if $X,Y\in \mathcal{C}^L$ and $f: X\to Y$ is negligible, then $F(f)$ is negligible. Indeed, recall that $\mathrm{Hom}(F(X),F(Y))$ carries a natural action of $L$, and that $F$ defines an isomorphism $\mathrm{Hom}(X,Y)\cong \mathrm{Hom}(F(X),F(Y))^L$. Now let $h\in \mathrm{Hom}(F(Y),F(X))$, and let us show that $\text{Tr}(F(f)\circ h)=0$. Let $\overline{h}=|L|^{-1}\sum_{\gamma\in L}\gamma(h)$. Then $\overline{h}=F(g)$ for a unique $g\in \mathrm{Hom}(X,Y)$. Thus, since $F(f)$ commutes with $L$ and the action of $L$ preserves traces, we have $$\text{Tr}(F(f)\circ h)=\text{Tr}(F(f)\circ \overline{h})=\text{Tr}(F(f)\circ F(g))=0,$$ as desired. Thus, the functor $F$ descends to a tensor functor $\overline{F}: \overline{\mathcal{C}^L}\to \overline{\mathcal{C}}$. Moreover, for any $T\in \overline{\mathcal{C}^L}$ the object $\overline{F}(T)$ has a natural structure of an $L$-equivariant object (coming from that of $T$), so the functor $\overline{F}$ factors naturally through a tensor functor $E:  \overline{\mathcal{C}^L}\to \overline{\mathcal{C}}^L$.

Suppose $T\in \overline{\mathcal{C}^L}$ is simple. Then $T=\overline{X}$, where $X\in \mathcal{C}^L$ is an indecomposable object of nonzero dimension. Thus $X=\text{Ind}_{L_Z}^L(\rho\otimes Z)$, where $Z$ is an indecomposable object of $\mathcal{C}$ of nonzero dimension, $L_Z$ is the stabilizer of $Z$ in $L$, and $\rho$ is an irreducible representation of $L_Z$ over $\mathbf{k}$. Then $E(T)=\text{Ind}_{L_Z}^L(\rho\otimes \overline{Z})$. Thus, $E(T)$ is simple (since so is $\overline{Z}$, and $L_{\overline{Z}}=L_Z$).

It remains to show that $E$ is essentially surjective, i.e. every simple object of $\overline{\mathcal{C}}^L$ is of the form $E(T)$. To this end, note that every simple object of $\overline{\mathcal{C}}^L$ has the form $W=\text{Ind}_{L_V}^L(\rho\otimes V)$, where $V=\overline{X}$ is a simple object of $\overline{\mathcal{C}}$ and $\rho$ is an irreducible representation of $L_V$. Since $|L_V|\ne 0$ in $\mathbf{k}$, we have $\dim \rho\ne 0$ in $\mathbf{k}$. Hence, $W=E(T)$, where $T=\text{Ind}_{L_V}^L(\rho\otimes X)$ is a simple object of $\overline{\mathcal{C}^L}$ (as $L_V=L_X$). The proposition is proved. ◻
:::

::: corollary
[]{#commu2 label="commu2"} In the setup of Lemma [\[equivar\]](#equivar){reference-type="ref" reference="equivar"} assume that $|L|\ne 0$ in $\mathbf{k}$. Then $\overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}G}\cong \overline{\mathop{\mathrm{Rep}}\nolimits_\mathbf{k}N}^L$.
:::

::: proof
*Proof.* This follows from Proposition [\[commu\]](#commu){reference-type="ref" reference="commu"} and Lemma [\[equivar\]](#equivar){reference-type="ref" reference="equivar"}. ◻
:::

::: remark
Similarly to Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"}, Proposition [\[commu\]](#commu){reference-type="ref" reference="commu"} and its proof generalizes to Karoubian pivotal categories satisfying the assumptions of Theorem [\[karpiv\]](#karpiv){reference-type="ref" reference="karpiv"}.
:::
