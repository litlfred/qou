---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-023-6-application-to-the-analytic-isoformal-classifi
section_title: "Application to the analytic isoformal classification"
section_number: 6
pages: 27-28
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.956
latex_coverage_ratio: 0.822
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:analyticisoformalclassification label="section:analyticisoformalclassification"}

The formal classification of analytic $q$-difference modules is equivalent to the classification of pure modules: the formal class of $M$ is equal to the formal class of ${\text{gr}}M$, and the latter is essentially the same thing as the analytic class of ${\text{gr}}M$. The classification of pure modules has been described in paragraph [\[subsection:puremodules\]](#subsection:puremodules){reference-type="ref" reference="subsection:puremodules"}.\
Let us fix a formal class, that is, a pure module: $$M_{0} := P_{1} \oplus \cdots \oplus P_{k}.$$ Here, each $P_{i}$ is pure isoclinic of slope $\mu_{i} \in {\mathbf Q}$ and rank $r_{i} \in {\mathbf N}^{*}$ and we assume that $\mu_{1} < \cdots < \mu_{k}$. All modules $M$ such that ${\text{gr}}M \simeq M_{0}$ have the same Newton polygon $N(M) = N(M_{0})$. They constitute a formal class and we want to classify them analytically. The following definition is inspired by [@BV].

[]{#not24 label="not24"}

::: defi
[]{#defi:analyticisoformalclass label="defi:analyticisoformalclass"} We write ${\mathcal{F}}(M_{0})$ or ${\mathcal{F}}(P_{1},\ldots,P_{k})$ for the set of equivalence classes of pairs $(M,g)$ of an analytic $q$-difference module $M$ and an isomorphism $g: {\text{gr}}(M) \rightarrow M_{0}$, where $(M,g)$ is said to be equivalent to $(M',g')$ if there exists a morphism $f: M \rightarrow M'$ such that $g = g' \circ {\text{gr}}(f)$.
:::

Note that $f$ is automatically an isomorphism. The goal of this paper is to describe precisely ${\mathcal{F}}(P_{1},\ldots,P_{k})$. This definition obviously admits a purely algebraic generalization, which is related to some interesting problems in homological algebra. In the appendix, we shall describe in some detail the necessary formalism and results in that direction; this will give us an adequate frame to formulate and prove our first structure theorems for the space ${\mathcal{F}}(M_{0})$ of isoformal analytic classes (theorems [\[theo:schemadesmodules\]](#theo:schemadesmodules){reference-type="ref" reference="theo:schemadesmodules"} and [\[theo:kintegralslopesspace\]](#theo:kintegralslopesspace){reference-type="ref" reference="theo:kintegralslopesspace"}).

::: rema
[]{#rema:badquotient1 label="rema:badquotient1"} The group $\prod\limits_{1 \leq i \leq k} \text{Aut}(P_{i})$ naturally operates on ${\mathcal{F}}(P_{1},\ldots,P_{k})$ in the following way: if $(\phi_{i})$ is an element of the group, thus defining $\phi \in \text{Aut}(M_{0})$, then send the class of the isomorphism $g: {\text{gr}}(M) \rightarrow M_{0}$ to the class of $\phi \circ g$. The quotient of ${\mathcal{F}}(P_{1},\ldots,P_{k})$ by this action is the set of analytic classes within the formal class of $M_{0}$, but it is not naturally made into a space of moduli. An example is given at the end of the next paragraph (remark [\[rema:badquotient2\]](#rema:badquotient2){reference-type="ref" reference="rema:badquotient2"}).
:::
