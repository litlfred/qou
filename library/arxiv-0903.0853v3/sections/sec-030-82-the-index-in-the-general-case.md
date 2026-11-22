---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-030-82-the-index-in-the-general-case
section_title: "The index in the general case"
section_number: 8.2
pages: 40-42
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.939
latex_coverage_ratio: 0.938
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
Generally speaking, there is no simple formula for the dimensions of the kernel and cokernel of a $q$-difference operator $P$. However, if $P$ has integral slopes[^1], we can factor it into operators of degree $1$, and then use proposition [\[prop:indices\]](#prop:indices){reference-type="ref" reference="prop:indices"} and linear algebra to deduce:

1.  The ${\mathbf C}$-linear map $P: f \mapsto P.f$ from $K$ to itself has an index, that is finite dimensional kernel and cokernel.

2.  The index of $P$, that is the integer $\chi(P) := \dim \text{Ker~}P - \dim \text{Coker~} P$ is the sum of indices of factors of $P$.

Note that $\chi(P)$ is the Euler-Poincaré characteristic of the complex of solutions of $P$.

::: coro
Let $P$ be an operator of order $n$ and pure of slope $\mu \neq 0$.\
(i) In the formal case, $\dim \text{Ker~}P = \dim \text{Coker~} P = 0$.\
(ii) In the convergent case $\dim \text{Ker~}P = 0$ and $\dim \text{Coker~} P = n \max(0,\mu)$.
:::

::: proof
*Proof.* If $\mu \in {\mathbf Z}$, all the factors of $P$ have the form $(z^{\mu} \sigma_q-c).u$. If $\mu \neq 0$, they are all bijective in the formal case, whence the first statement. They are also all injective in the convergent case, and onto if $\mu < 0$, whence the second statement in this case. If $\mu > 0$, they all have index $\mu$ (in the convergent case), whence the second statement in this case by additivity of the index.\
The case of an arbitrary slope is easily reduced to this case by ramification. ◻
:::

By similar arguments:

::: coro
Let $P$ be an operator pure of slope $0$. Then, the index of $P$ (in the formal or convergent case) is $0$.
:::

Now, using the additivity of the index:

::: coro
The index of an arbitrary operator $P$ is $0$ in the formal case and $- \sum\limits_{\mu > 0} r_{P}(\mu) \mu$ in the convergent case.
:::

::: coro
Let $P \in {{\mathcal{D}}_{q}}$ be an analytic $q$-difference operator. The index of $P$ acting as a ${\mathbf C}$-linear endomorphism of ${{\mathbf C}((z))}/{{\mathbf C}(\{z\})}$ is equal to $\sum\limits_{\mu > 0} r_{P}(\mu) \mu$.
:::

Of course, $r_{P}$ denotes here the Newton function of $P$ introduced in subsection [\[subsection:Newtonpolygon\]](#subsection:Newtonpolygon){reference-type="ref" reference="subsection:Newtonpolygon"}.

## Irregularity and the dimension of ${\mathcal{F}}(P_{1},\ldots,P_{k})$ {#subsection:algebraicirregularity}

The following definition is inspired by that of [@Ma3].

::: defi
[]{#defi:irregularity label="defi:irregularity"} The *irregularity* of a $q$-difference operator $P$, resp. of $q$-difference module $M$, is defined by the formulas: []{#not33 label="not33"} $$\text{Irr~}(P) := \sum\limits_{\mu > 0} r_{P}(\mu) \mu, \quad
\text{Irr~}(M) := \sum\limits_{\mu > 0} r_{M}(\mu) \mu.$$
:::

Graphically, this is the height of the right part of the Newton polygon, from the bottom to the upper right end. It is clearly a formal invariant. From its interpretation as an index in ${{\mathbf C}((z))}/{{\mathbf C}(\{z\})}$, the irregularity of operators is additive with respect to the product. From theorem [\[theo:Newtonpolygon\]](#theo:Newtonpolygon){reference-type="ref" reference="theo:Newtonpolygon"}, the irregularity of modules is additive with respect to exact sequences. Moreover, with the notations of [\[theo:slopefiltration\]](#theo:slopefiltration){reference-type="ref" reference="theo:slopefiltration"}, writing $$M^{>0} := M/M_{\leq 0}$$ the "positive part" of $M$, one has: $$\text{Irr~}(M) = \text{Irr~}(M^{>0}).$$

[]{#not34 label="not34"} Write $M_{0} := P_{1} \oplus \cdots \oplus P_{k}$. Then the "internal End" $E := \underline{\text{End}}(M_{0}) = M_{0}^{\vee} \otimes M_{0}$ of this module (subsection [\[subsection:generalitiesdiffmods\]](#subsection:generalitiesdiffmods){reference-type="ref" reference="subsection:generalitiesdiffmods"}) has as Newton function: $$r_{E}(\mu) = \sum_{\mu_{j} - \mu_{i} = \mu} r_{i} r_{j}.$$ (This follows from theorem [\[theo:Newtonpolygon\]](#theo:Newtonpolygon){reference-type="ref" reference="theo:Newtonpolygon"}.) From theorem [\[theo:schemadesmodules\]](#theo:schemadesmodules){reference-type="ref" reference="theo:schemadesmodules"} and definition [\[defi:irregularity\]](#defi:irregularity){reference-type="ref" reference="defi:irregularity"}, we therefore get the equality: $$\dim {\mathcal{F}}(P_{1},\ldots,P_{k}) = 
\text{Irr~} \left(\underline{\text{End}}(M_{0})\right).$$ In subsection [\[subsection:sheaftheoreticirregularity\]](#subsection:sheaftheoreticirregularity){reference-type="ref" reference="subsection:sheaftheoreticirregularity"}, we shall give a sheaf theoretical interpretation of this formula.

[^1]: This assumption will be dropped in the four next corollaries.
