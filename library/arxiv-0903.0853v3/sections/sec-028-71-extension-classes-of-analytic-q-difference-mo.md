---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-028-71-extension-classes-of-analytic-q-difference-mo
section_title: "Extension classes of analytic $q$-difference modules"
section_number: 7.1
pages: 35-38
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.909
latex_coverage_ratio: 0.932
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#subsection:extensionsofqdifferencemodules label="subsection:extensionsofqdifferencemodules"}

From here on, we consider only analytic $q$-difference modules and the base field is ${{\mathbf C}(\{z\})}$ (except for brief indications about the formal case).

::: theo
[]{#theo:dimensiondeuxpentes label="theo:dimensiondeuxpentes"} Let $M,N$ be pure modules of ranks $r,s \in {\mathbf N}^{*}$ and slopes $\mu < \nu \in {\mathbf Q}$. Then $\dim_{{\mathbf C}} {\mathcal{F}}(M,N) = r s(\nu - \mu)$.
:::

::: proof
*Proof.* Since ${\mathcal{F}}(M,N) \simeq \text{Ext}^{1}(N,M) \simeq \Gamma^{1}(N^{\vee} \otimes M)$ (proposition [\[prop:GammaetExt\]](#prop:GammaetExt){reference-type="ref" reference="prop:GammaetExt"}) and since $N^{\vee} \otimes M$ is pure isoclinic of rank $r s$ and slope $\mu - \nu < 0$, the theorem is an immediate consequence of the following lemma. ◻
:::

::: lemm
[]{#lemm:dimensiondeuxpentes label="lemm:dimensiondeuxpentes"} Let $M$ be a pure module of ranks $r$ and slope $\mu < 0$. Then $\dim_{{\mathbf C}} \Gamma^{1}(M) = - r \mu$.
:::

::: proof
*Proof.* We give four different proofs, of which two require that $\mu \in {\mathbf Z}$.

1\) Write $d := - r \mu \in {\mathbf N}^{*}$. If $M = {{\mathcal{D}}_{q}}/{{\mathcal{D}}_{q}}P$, the module $M^{\vee}$ is pure of rank $r$ and slope $- \mu$, and can be written as ${{\mathcal{D}}_{q}}/{{\mathcal{D}}_{q}}P^{\vee}$ for some dual $P^{\vee} = a_{0} + \cdots + a_{r} \sigma_q^{r}$ of $P$, such that $v_{0}(a_{0}) = 0$, $v_{0}(a_{r}) = d$ and $v_{0}(a_{i}) \geq i d/r$ for all $i$ (lemma [\[lemm:puremodules\]](#lemm:puremodules){reference-type="ref" reference="lemm:puremodules"}). We want to apply proposition 2.5 of [@Bezivin], but the latter assumes $\left |q \right |< 1$, so we consider $L := P^{\vee} \sigma_q^{-r} = b_{0} + \cdots + b_{r} \sigma^{r}$, where $\sigma := \sigma_q^{-1}$ and $b_{i} := a_{r-i}$. After *loc.cit*, the operator $L: {{\mathbf C}\{z\}}\rightarrow {{\mathbf C}\{z\}}$ has index $d$. More generally, for all $m \in {\mathbf N}^{*}$, the operator $L: z^{-m} {{\mathbf C}\{z\}}\rightarrow z^{-m} {{\mathbf C}\{z\}}$ is conjugate to $z^{m} L z^{-m} = \sum q^{i m} b_{i} \sigma^{i}: {{\mathbf C}\{z\}}\rightarrow {{\mathbf C}\{z\}}$, which also has index $d$. Hence $L: {{\mathbf C}(\{z\})}\rightarrow {{\mathbf C}(\{z\})}$ has index $d$, and so has $P^{\vee}$. After corollary [\[coro:complexedessolutionsbis\]](#coro:complexedessolutionsbis){reference-type="ref" reference="coro:complexedessolutionsbis"}, this index is $\dim_{{\mathbf C}} \Gamma^{1}(M) - \dim_{{\mathbf C}} \Gamma(M)$. But, $M$ being pure isoclinic of non null slope, $\Gamma(M) = 0$, which ends the first proof.

2\) In the following proof, we assume $\mu \in {\mathbf Z}$. From theorem 1.2.3 of [@JSAIF], we know that we may choose the dual operator such that: $$P^{\vee} = (z^{-\mu} \sigma_q- c_{1}) u_{1} \cdots (z^{-\mu} \sigma_q- c_{r}) u_{r},$$ where $c_{1},\ldots,c_{r} \in {\mathbf C}^{*}$ and $u_{1},\ldots,u_{r} \in {{\mathbf C}\{z\}}$, $u_{1}(0) = \cdots = u_{r}(0) = 1$. We are thus left to prove that each $z^{-\mu} \sigma_q- c_{1}$ has index $-\mu$: the indexes add up and the sum will be $- r \mu = d$. Since the kernels are trivial, we must compute the cokernel of an operator $z^{m} \sigma_q- c$, $m \in {\mathbf N}^{*}$. But it follows from lemma [\[lemm:supplementairedeuxpentes\]](#lemm:supplementairedeuxpentes){reference-type="ref" reference="lemm:supplementairedeuxpentes"} that the image of $z^{m} \sigma_q- c: {{\mathbf C}(\{z\})}\rightarrow {{\mathbf C}(\{z\})}$ admits the supplementary space ${\mathbf C}\oplus \cdots \oplus {\mathbf C}z^{m-1}$.

3\) In the following proof, we assume again $\mu \in {\mathbf Z}$. After lemma [\[lemm:puremodules\]](#lemm:puremodules){reference-type="ref" reference="lemm:puremodules"}, we can write $M = ({{\mathbf C}(\{z\})}^{r},\Phi_{z^{\mu} A})$, $A \in {\text{GL}}_{r}({\mathbf C})$. After corollary [\[coro:complexedessolutions\]](#coro:complexedessolutions){reference-type="ref" reference="coro:complexedessolutions"}, we must consider the cokernel of ${{\mathbf C}(\{z\})}^{r} \overset{\Phi_{z^{\mu} A} - \text{Id}}{\longrightarrow} {{\mathbf C}(\{z\})}^{r}$. But, after lemma [\[lemm:supplementairedeuxpentes\]](#lemm:supplementairedeuxpentes){reference-type="ref" reference="lemm:supplementairedeuxpentes"}, the image of $\Phi_{z^{\mu} A} - \text{Id}$ admits the supplementary space $({\mathbf C}\oplus \cdots \oplus {\mathbf C}
z^{-\mu-1})^{r}$.

4\) A similar proof, but for arbitrary $\mu$, can be deduced from [@vdPR]. It follows indeed from this paper that each isoclinic module of slope $\mu$ can be obtained by successive extensions of modules admitting a dual of the form ${{\mathcal{D}}_{q}}/{{\mathcal{D}}_{q}}(z^{a} \sigma_q^{b} - c)$, where $b/a = - \mu$ and $c \in {\mathbf C}^{*}$. ◻
:::

::: lemm
[]{#lemm:supplementairedeuxpentes label="lemm:supplementairedeuxpentes"} Let $d,r \in {\mathbf N}^{*}$ and $A \in {\text{GL}}_{r}({\mathbf C})$. Let $D \subset {\mathbf Z}$ be any set of representatives modulo $d$, for instance $\{a,a+1,\ldots,a+d-1\}$ for some $a \in {\mathbf Z}$. Then, the image of the ${\mathbf C}$-linear map $F: X \mapsto z^{d} A \sigma_qX - X$ from ${{\mathbf C}(\{z\})}^{r}$ to itself admits as a supplementary $\left(\sum\limits_{i \in D} {\mathbf C}z^{i}\right)^{r}$.
:::

::: proof
*Proof.* For all $i \in {\mathbf Z}$, write $K_{i} := z^{i} {\mathbf C}(\{z^{d}\})$, so that ${{\mathbf C}(\{z\})}= \bigoplus_{i \in D} K_{i}$. Each of the $K_{i}^{r}$ is stable under $F$. We write $w := z^{d}$, $L := {\mathbf C}(\{w\})$, $\rho := q^{d}$ and define $\sigma$ on $L$ by $\sigma f(w) = f(\rho w)$. Multiplication by $z^{i}$ sends $L^{r}$ to $K_{i}^{r}$ and conjugates the restriction of $F$ to $K_{i}^{r}$ to the mapping $G_{i}: Y \mapsto w q^{i} A \sigma Y - Y$ from $L^{r}$ to itself. We are left to check that the image of $G_{i}$ admits ${\mathbf C}^{r}$ as a supplementary. But this is just the case $d = 1$, $D = \{0\}$ of the lemma. So we tackle this case under these assumptions with the notations of the lemma.

So write $F_{A}: X \mapsto z A \sigma_qX - X$ from ${{\mathbf C}(\{z\})}^{r}$ to itself. Also write $X = \sum X_{n} z^{n}$ and $Y = F_{A}(X) = \sum Y_{n} z^{n}$ (all sums here have at most a finite number of negative indices), so that $Y_{n} = q^{n-1} A X_{n-1} - X_{n}$. Putting $\tilde{X} := \sum A^{-n} X_{n} z^{n}$ and $\tilde{Y} := \sum A^{-n} Y_{n} z^{n}$, from the relation $A^{-n} Y_{n} = q^{n-1} A^{-(n-1)} X_{n-1} - A^{-n} X_{n}$, we draw $\tilde{Y} = z \sigma_q\tilde{X} - X$. Of course, $X \mapsto \tilde{X}$ is an automorphism of ${{\mathbf C}(\{z\})}^{r}$ and we just saw that it conjugates $F_{A}$ to the map $F: X \mapsto z \sigma_qX - X$ from ${{\mathbf C}(\{z\})}^{r}$ to itself. Moreover, the same automorphism leaves invariant the subspace ${\mathbf C}^{r} \subset {{\mathbf C}(\{z\})}^{r}$, so the question boils down to prove that the image of $F$ has supplementary ${\mathbf C}^{r}$. And this, in turn, splits into $r$ times the same problem for $r = 1$.

So we are left with the case of the map $\Psi: f \mapsto z \sigma_qf - f$ from ${{\mathbf C}(\{z\})}$ to itself, which is the very heart of the theory ! (See for instance example [\[exem:archetypal\]](#exem:archetypal){reference-type="ref" reference="exem:archetypal"} page and section [\[section:qEuler\]](#section:qEuler){reference-type="ref" reference="section:qEuler"} of chapter [\[chapter:examplesStokes\]](#chapter:examplesStokes){reference-type="ref" reference="chapter:examplesStokes"}.) This case has been studied in detail in paragraph [\[subsection:prototypal\]](#subsection:prototypal){reference-type="ref" reference="subsection:prototypal"}. We saw there that $\Psi$ is injective and that its image is in direct sum with ${\mathbf C}\subset {{\mathbf C}(\{z\})}$. More precisely, for any $u \in {{\mathbf C}(\{z\})}$, the unique $u_0 \in {\mathbf C}$ such that $u - u_0 \in \text{Im~} \Psi$ is $u_0 := {\mathcal{B}_{q,1}}\, u(1)$ (the $q$-Borel transform ${\mathcal{B}_{q,1}}\, u$ was defined in paragraph [\[subsection:prototypal\]](#subsection:prototypal){reference-type="ref" reference="subsection:prototypal"}). This achieves the proof. ◻
:::

Note that from the proof, one draws explicit projection maps from ${{\mathbf C}(\{z\})}^{r}$ to the image of $F_{A}$ and its supplementary ${\mathbf C}^{r}$: these are the maps $Y \mapsto Y - {\mathcal{B}_{q,1}}Y(A^{-1})$ and $Y \mapsto {\mathcal{B}_{q,1}}Y(A^{-1})$, where: $${\mathcal{B}_{q,1}}Y(A^{-1}) := \sum q^{-n(n-1)/2} A^{-n} Y_{n}.$$

## The affine scheme ${\mathcal{F}}(P_{1},\ldots,P_{k})$ {#subsection:theaffineschemeF(M0)}

Now let $P_{1},\ldots,P_{k}$ be pure isoclinic $q$-difference modules over ${{\mathbf C}(\{z\})}$, of ranks $r_{1},\ldots,r_{k} \in {\mathbf N}^{*}$ and slopes $\mu_{1} < \cdots < \mu_{k}$. From section [\[section:modulispace\]](#section:modulispace){reference-type="ref" reference="section:modulispace"} of the appendix [\[chapter:ISOGRAD\]](#chapter:ISOGRAD){reference-type="ref" reference="chapter:ISOGRAD"}, we have a functor from commutative ${\mathbf C}$-algebras to sets: $$C \leadsto F(C) := {\mathcal{F}}(C \otimes_{{\mathbf C}} P_{1},\ldots,C \otimes_{{\mathbf C}} P_{k}).$$ Here, the base change $C \otimes_{{\mathbf C}} -$ means that we extend the scalars of $q$-difference modules from ${{\mathbf C}(\{z\})}$ to $C \otimes_{{\mathbf C}} {{\mathbf C}(\{z\})}$.

::: theo
[]{#theo:schemadesmodules label="theo:schemadesmodules"} The functor $F$ is representable and the corresponding affine scheme is an affine space over ${\mathbf C}$ with dimension: $$\dim {\mathcal{F}}(P_{1},\ldots,P_{k}) =
\sum\limits_{1 \leq i < j \leq k} r_{i} r_{j} (\mu_{j} - \mu_{i}).$$
:::

::: proof
*Proof.* We apply theorem [\[theo:themodulispaceabstract\]](#theo:themodulispaceabstract){reference-type="ref" reference="theo:themodulispaceabstract"}. We need two check the assumptions: $$\forall i,j, \text{~~s.t.~~} 1 \leq i < j \leq k ~,~
\text{Hom}(P_{j},P_{i}) = 0 \text{~~and~~}
\dim_{{\mathbf C}}\text{Ext}(P_{j},P_{i}) = r_{i} r_{j} (\mu_{j} - \mu_{i}).$$ The first fact comes from theorem [\[theo:slopefiltration\]](#theo:slopefiltration){reference-type="ref" reference="theo:slopefiltration"} and the second fact from theorem [\[theo:dimensiondeuxpentes\]](#theo:dimensiondeuxpentes){reference-type="ref" reference="theo:dimensiondeuxpentes"}; the fact that the extension modules are free is here obvious since ${\mathbf C}$ is a field. ◻
:::

::: rema
The use of base changes $C \otimes_{{\mathbf C}} {{\mathbf C}(\{z\})}$ is too restrictive to consider this as a true space of moduli, as was done for differential equations in [@BV chap. III]: we would like to consider families of modules the coefficients of which are arbitrary analytic functions of some parameter. This will be done in [@JSmoduli].
:::

Now, to get coordinates on our affine scheme, we just have to find bases of the extension modules $\text{Ext}(P_{j},P_{i})$ for $1 \leq i < j \leq k$: this follows indeed from corollary [\[coro:themodulispaceabstract\]](#coro:themodulispaceabstract){reference-type="ref" reference="coro:themodulispaceabstract"}. An example will be given by corollary [\[coro:schemadesmodules\]](#coro:schemadesmodules){reference-type="ref" reference="coro:schemadesmodules"}.
