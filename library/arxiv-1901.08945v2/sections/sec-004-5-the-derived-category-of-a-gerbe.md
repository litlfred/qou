---
doc_id: arxiv-1901.08945v2
doc_title: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties"
section_id: sec-004-5-the-derived-category-of-a-gerbe
section_title: "The derived category of a gerbe"
section_number: 5
pages: 20-24
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.963
doc_brief: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group"
---
[]{#sec:decomp-deriv-categ label="sec:decomp-deriv-categ"} In this section we generalize some of the results by Căldăraru [@caldararu2000 Chapter 2] and Lieblich [@lieblich2004 Section 2.2.4] on the basic structure of derived categories of gerbes and twisted sheaves. Throughout the section, we let $\alpha\colon X \to S$ be a gerbe banded by a diagonalizable group $\Delta$ with character group $A$.

::: definition
[]{#def:derived-twisted label="def:derived-twisted"} Given a character $\chi \colon \Delta_S \to {\ensuremath{\mathbb{G}_{\operatorname{m},S}}}$, we say that an object $\mathcal{F}$ in ${\operatorname{D}}_{\operatorname{qc}}(X)$ is *$\chi$-homogeneous* if it has $\chi$-homogeneous cohomology. We denote the full subcategory of $\chi$-homogeneous objects in ${\operatorname{D}}_{\operatorname{qc}}(X)$ by ${\operatorname{D}}_{{\operatorname{qc}}, \chi}(X)$.

Consider the special case $\Delta = {\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ and let ${\operatorname{id}}\colon {\ensuremath{\mathbb{G}_{\operatorname{m}}}}\to {\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ be the identity character. An object in ${\operatorname{D}}_{{\operatorname{qc}}, {\operatorname{id}}}(X)$ is called an *$\alpha$-twisted complex on $S$*. We often use the notation ${\operatorname{D}}_{{\operatorname{qc}}, \alpha}(S)$ instead of ${\operatorname{D}}_{{\operatorname{qc}}, {\operatorname{id}}}(X)$ employing a similar abuse of notation as in Remark [\[rem-twisted-abuse\]](#rem-twisted-abuse){reference-type="ref" reference="rem-twisted-abuse"} if $\alpha$ is just a cohomology class in $\mathop{\mathrm{H}}^2(S_{\operatorname{fppf}}, {\ensuremath{\mathbb{G}_{\operatorname{m}}}})$.
:::

We state the following lemma for convenient reference. See Remark [\[rem-trivial-case\]](#rem-trivial-case){reference-type="ref" reference="rem-trivial-case"} for sharper results.

::: lemma
[]{#lem:affine-derived-decomp label="lem:affine-derived-decomp"} Let $S$ be an affine scheme and let $\alpha\colon X \to S$ be a trivial $\Delta$-gerbe, where $\Delta$ is a diagonalizable group. Then the obvious functor $$\label{eq-equiv-qcoh}
{\operatorname{D}}({\ensuremath{\operatorname{Qcoh}}}(X)) \xrightarrow{\sim} {\operatorname{D}}_{\operatorname{qc}}(X)$$ is a monoidal equivalence and induces equivalences $$\label{eq-equiv-qcoh-chi}
{\operatorname{D}}({\ensuremath{\operatorname{Qcoh}}}_\chi(X)) \xrightarrow{\sim} {\operatorname{D}}_{{\operatorname{qc}}, \chi}(X)$$ for each character $\chi$ of $\Delta$. Moreover, let $T$ be an affine scheme and let $\beta\colon X' \to T$ be a trivial $\Delta'$-gerbe, where $\Delta'$ is a diagonalizable group. Assume that we have a morphism $\rho\colon X \to X'$ of algebraic stacks. Then the squares $$\label{eq-commute-derived}
\xymatrix{
{\operatorname{D}}({\ensuremath{\operatorname{Qcoh}}}(X')) \ar[r]^-{\sim}\ar[d]_{\mathsf{L}\rho^*} & {\operatorname{D}}_{\operatorname{qc}}(X') \ar[d]^{\rho^*}\\
{\operatorname{D}}({\ensuremath{\operatorname{Qcoh}}}(X)) \ar[r]^-{\sim}& {\operatorname{D}}_{\operatorname{qc}}(X), \\
}\qquad
\xymatrix{
{\operatorname{D}}({\ensuremath{\operatorname{Qcoh}}}(X')) \ar[r]^-{\sim} & {\operatorname{D}}_{\operatorname{qc}}(X') \\
{\operatorname{D}}({\ensuremath{\operatorname{Qcoh}}}(X)) \ar[r]^-{\sim}\ar[u]^{\mathsf{R}\rho_*}& {\operatorname{D}}_{\operatorname{qc}}(X)\ar[u]_{\rho_*} \\
}$$ commute up to natural equivalence.
:::

::: proof
*Proof.* The equivalence [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is a special case of [@lieblich2004 Proposition 2.2.4.6], and the equivalences [\[eq-equiv-qcoh-chi\]](#eq-equiv-qcoh-chi){reference-type="eqref" reference="eq-equiv-qcoh-chi"} are then immediate from Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}. The fact that the equivalence [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is monoidal follows from the fact that any complex in ${\ensuremath{\operatorname{Qcoh}}}(X)$ admits a resolution by an h-flat complex in ${\ensuremath{\operatorname{Qcoh}}}(X)$ which is also h-flat as a complex in ${\ensuremath{\operatorname{Mod}}}(X_{\operatorname{lis-\acute{e}t}}, \mathcal{O}_X)$. This can be seen by using a homotopy limit argument (see [@stacks-project [Tag 06XX](http://stacks.math.columbia.edu/tag/06XX)]), using that any object in ${\ensuremath{\operatorname{Qcoh}}}(X)$ is a quotient of a locally free sheaf and the fact that coproducts in ${\ensuremath{\operatorname{Mod}}}(X_{\operatorname{lis-\acute{e}t}}, \mathcal{O}_X)$ are exact and preserve ${\ensuremath{\operatorname{Qcoh}}}(X)$.

The functor $\alpha_*\colon {\ensuremath{\operatorname{Qcoh}}}(X) \to {\ensuremath{\operatorname{Qcoh}}}(S)$ is exact, since this operation corresponds to taking invariants and $\Delta$ is diagonalizable. This well-known fact also easily follows from the last sentence of Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"} together with the decomposition in Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}. Hence the equivalence [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} shows that $X$ has cohomological dimension zero.

Note that $\rho$ induces a morphism $S \to T$ on the coarse spaces, so $\rho$ factors as $X \to X'\times_T S \to X'$ where the first morphism is a morphism of gerbes over $S$, and the second morphism is affine. Furthermore, the first morphism factors as an affine morphism followed by a $\Delta$-gerbe by Remark [\[rem-gerbe-ff\]](#rem-gerbe-ff){reference-type="ref" reference="rem-gerbe-ff"}. Hence also $\rho$ has cohomological dimension zero, as this property is stable under composition and can be checked after a faithfully flat base change by [@hr2017 Lemma 2.2]). In particular, $\rho$ is concentrated, so it follows from [@hnr2018 Corollary 2.2] that the right hand square [\[eq-commute-derived\]](#eq-commute-derived){reference-type="eqref" reference="eq-commute-derived"} commutes. Hence also the left hand square commutes by adjunction. ◻
:::

::: remark
[]{#rem-gerbe-concentrated label="rem-gerbe-concentrated"} Let $\rho\colon X \to Y$ be a morphism of gerbes banded by diagonalizable groups over an algebraic stack $S$ as in Remark [\[rem-gerbe-ff\]](#rem-gerbe-ff){reference-type="ref" reference="rem-gerbe-ff"}. Then the last part of the proof shows that $\rho$ is concentrated of cohomological dimension zero, as these properties can be checked locally on $S$ (see [@hr2017 Lemma 2.2 and Lemma 2.5]).
:::

The next theorem is the main structure theorem for the derived category of a $\Delta$-gerbe and the derived analog of Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}. It is a generalization of the observation in [@lieblich2004 Section 2.2.4] that the derived category splits according to characters in certain situations.

::: theorem
[]{#t:chi-splitting-D-qc-X label="t:chi-splitting-D-qc-X"} Let $S$ be an algebraic stack and $\alpha\colon X \to S$ a gerbe banded by a diagonalizable group $\Delta$. Then ${\operatorname{D}}_{{\operatorname{qc}}, \chi}(X)$ is a triangulated subcategory of ${\operatorname{D}}_{{\operatorname{qc}}}(X)$ for each $\Delta_S$-character $\chi$, and taking the coproduct gives an equivalence $$\label{eq-equivalence-derived}
\prod_{\chi \in A} {\operatorname{D}}_{{\operatorname{qc}}, \chi}(X) \xrightarrow[{}]{\sim}{\operatorname{D}}_{\operatorname{qc}}(X),
\qquad
 (\mathcal{F}_\chi)_{\chi \in A} 
\mapsto 
\bigoplus_{\chi \in A} \mathcal{F}_\chi,$$ of triangulated categories, where $A$ denotes the character group of $\Delta$.

Furthermore, assume that $\mathcal{F}_\chi$ and $\mathcal{G}_\psi$ are objects in ${\operatorname{D}}_{\operatorname{qc}}(X)$ which are homogeneous for $\Delta_S$-characters $\chi$ and $\psi$, respectively. Then the objects $$\label{eq-der-monoidal}
\mathcal{F}_\chi \otimes \mathcal{G}_\psi, \qquad
{\mathcal{H}{om}}(\mathcal{G}_\psi, \mathcal{F}_\chi)$$ are $\chi\psi$- and $\chi\psi^{-1}$-homogeneous, respectively.
:::

::: proof
*Proof.* By Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}, the category ${\ensuremath{\operatorname{Qcoh}}}_\chi(X)$ is a Serre subcategory of ${\ensuremath{\operatorname{Qcoh}}}(X)$. It follows that ${\operatorname{D}}_{{\operatorname{qc}}, \chi}(X)$ is a strictly full triangulated subcategory of ${\operatorname{D}}_{\operatorname{qc}}(X)$ by [@stacks-project [Tag 07B4](http://stacks.math.columbia.edu/tag/07B4), [Tag 06UQ](http://stacks.math.columbia.edu/tag/06UQ)].

Recall that we work with sheaves on the lisse--étale sites over $X$ and $S$. Note that we get a morphism $X_{{\operatorname{lis-\acute{e}t}}} \to S_{{\operatorname{lis-\acute{e}t}}}$ of topoi, by [@stacks-project [Tag 07AT](http://stacks.math.columbia.edu/tag/07AT)], since $\alpha$ is smooth (see Remark [\[rem-gerbe-ff\]](#rem-gerbe-ff){reference-type="ref" reference="rem-gerbe-ff"}). In particular, there is no need to work with hypercoverings to define pull-backs as in [@olsson2007].

Let $E$ be a subset of the set $A$ of characters of $\Delta$, and let ${\ensuremath{\operatorname{Qcoh}}}_E(X)$ denote the full subcategory of ${\ensuremath{\operatorname{Qcoh}}}(X)$ of objects which are direct sums of $\chi$-homogeneous objects for $\chi \in E$. Let $F$ be the complement of $E$ in $A$. It follows from Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"} that $({\ensuremath{\operatorname{Qcoh}}}_E(X), {\ensuremath{\operatorname{Qcoh}}}_F(X))$ is a torsion pair in ${\ensuremath{\operatorname{Qcoh}}}(X)$ and that both ${\ensuremath{\operatorname{Qcoh}}}_E(X)$ and ${\ensuremath{\operatorname{Qcoh}}}_F(X)$ are abelian subcategories of ${\ensuremath{\operatorname{Qcoh}}}(X)$.

Let $\mathcal{E}$ and $\mathcal{F}$ be objects of ${\ensuremath{\operatorname{Qcoh}}}_E(X)$ and ${\ensuremath{\operatorname{Qcoh}}}_F(X)$, respectively. We will show that $$\label{eq-ext-vanishing}
\mathop{\mathrm{Ext}}^n_{\mathcal{O}_X}(\mathcal{E}, \mathcal{F})
\cong \mathop{\mathrm{H}}^n(\mathsf{R}\Gamma\mathsf{R}{\mathcal{H}{om}}_{\mathcal{O}_X}(\mathcal{E}, \mathcal{F}))$$ vanishes for each $n$. Since $\mathsf{R}\Gamma\mathsf{R}{\mathcal{H}{om}}_{\mathcal{O}_X}(\mathcal{E}, \mathcal{F})
\cong
\mathsf{R}\Gamma\mathsf{R}\alpha_\ast\mathsf{R}{\mathcal{H}{om}}_{\mathcal{O}_X}(\mathcal{E}, \mathcal{F}),$ this follows if we prove that $\mathsf{R}\alpha_\ast\mathsf{R}{\mathcal{H}{om}}_{\mathcal{O}_X}(\mathcal{E}, \mathcal{F})$ vanishes. The $n$-th cohomology sheaf of $\mathsf{R}\alpha_\ast\mathsf{R}{\mathcal{H}{om}}_{\mathcal{O}_X}(\mathcal{E}, \mathcal{F})$ is easily seen to be the sheaf of $\mathcal{O}_S$-modules associated to the presheaf $$(U \to S) \mapsto
\mathop{\mathrm{Ext}}^n_{\mathcal{O}_{X_U}}(\mathcal{E}|_{X_U}, 
\mathcal{F}|_{X_U})$$ where $U$ is a scheme and $U \rightarrow S$ is smooth. It is therefore enough to verify the vanishing of [\[eq-ext-vanishing\]](#eq-ext-vanishing){reference-type="eqref" reference="eq-ext-vanishing"} when $S$ is affine and the gerbe $\alpha\colon X \to S$ is trivial. But in this situation the functor [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is an equivalence by Lemma [\[lem:affine-derived-decomp\]](#lem:affine-derived-decomp){reference-type="ref" reference="lem:affine-derived-decomp"}, so we get the desired vanishing from Lemma [\[p:abelian-torsion-pair\]](#p:abelian-torsion-pair){reference-type="ref" reference="p:abelian-torsion-pair"}.[\[enum:Ext-TF\]](#enum:Ext-TF){reference-type="ref" reference="enum:Ext-TF"} or, more easily, from Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}.

All direct and inverse truncation systems in ${\operatorname{D}}_{\operatorname{qc}}(X)$ are effective by Propositions [\[p:ab4-trunc\]](#p:ab4-trunc){reference-type="ref" reference="p:ab4-trunc"} and [\[p:Dqc-truncation-complete\]](#p:Dqc-truncation-complete){reference-type="ref" reference="p:Dqc-truncation-complete"}. Hence the hypotheses of Theorem [\[t:sod-DBA\]](#t:sod-DBA){reference-type="ref" reference="t:sod-DBA"} are satisfied, so we get a semi-orthogonal decomposition $$\label{eq-so-decomp}
{\operatorname{D}}_{\operatorname{qc}}(X) = \langle {\operatorname{D}}_{{\operatorname{qc}}, F}(X), {\operatorname{D}}_{{\operatorname{qc}}, E}(X)\rangle,$$ where ${\operatorname{D}}_{{\operatorname{qc}}, E}$ denotes the full subcategory of ${\operatorname{D}}_{\operatorname{qc}}(X)$ of objects with cohomology in ${\ensuremath{\operatorname{Qcoh}}}_E(X)$ and similarly for ${\operatorname{D}}_{{\operatorname{qc}}, F}(X)$.

We are now ready to prove that the functor [\[eq-equivalence-derived\]](#eq-equivalence-derived){reference-type="eqref" reference="eq-equivalence-derived"} is an equivalence. First note that it is well defined since ${\operatorname{D}}_{\operatorname{qc}}(X)$ has arbitrary coproducts. Let $\chi \in A$ and set $E = \{\chi\}$, $F = A -\{\chi\}$. Then $\mathop{\mathrm{Hom}}_{{\operatorname{D}}_{\operatorname{qc}}(X)}(\mathcal{F}_\chi, \mathcal{G})$ vanishes whenever $\mathcal{F}_\chi \in {\operatorname{D}}_{{\operatorname{qc}}, \chi}(X)$ and $\mathcal{G} \in {\operatorname{D}}_{{\operatorname{qc}}, F}$ by the semi-orthogonal decomposition [\[eq-so-decomp\]](#eq-so-decomp){reference-type="eqref" reference="eq-so-decomp"}. Since ${\operatorname{D}}_{{\operatorname{qc}}, \chi}(X)$ is a full subcategory of ${\operatorname{D}}_{\operatorname{qc}}(X)$, it follows that the functor [\[eq-equivalence-derived\]](#eq-equivalence-derived){reference-type="eqref" reference="eq-equivalence-derived"} is fully faithful.

Now let $\mathcal{F}$ be any object of ${\operatorname{D}}_{\operatorname{qc}}(X)$. Then the semi-orthogonal decomposition [\[eq-so-decomp\]](#eq-so-decomp){reference-type="eqref" reference="eq-so-decomp"} gives a triangle $$\mathcal{F}_\chi \to \mathcal{F} \to \mathcal{F}_F \to \Sigma\mathcal{F}_\chi$$ with $\mathcal{F}_\chi \in {\operatorname{D}}_{{\operatorname{qc}}, \chi}(X)$ and $\mathcal{F}_F
\in {\operatorname{D}}_{{\operatorname{qc}}, F}(X)$, respectively. By Remark [\[rem:cohomology-split\]](#rem:cohomology-split){reference-type="ref" reference="rem:cohomology-split"} and Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}, the morphism $\mathcal{F}_\chi \to \mathcal{F}$ induces an isomorphism $\mathop{\mathrm{H}}^n(\mathcal{F}_\chi) \to \mathop{\mathrm{H}}^n(\mathcal{F})_\chi$ for each $n$. It follows that the canonical map $\bigoplus_{\chi \in A} \mathcal{F}_\chi \to \mathcal{F}$ induces an isomorphism on cohomology and therefore is an isomorphism in ${\operatorname{D}}_{\operatorname{qc}}(X)$. Hence the functor [\[eq-equivalence-derived\]](#eq-equivalence-derived){reference-type="eqref" reference="eq-equivalence-derived"} is essentially surjective and therefore an equivalence.

Finally, we prove the statements about the monoidal structure. It is enough to prove the statement about the tensor product, since the statement about the internal hom follows formally from the adjointness property. The question whether $\mathcal{F}_\chi \otimes_\mathcal{O_X}^\mathsf{L}\mathcal{G}_\psi$ is $\chi\psi$-homogeneous can be verified locally on $S$. Indeed, this follows from Proposition [\[p:pull-back-grading\]](#p:pull-back-grading){reference-type="ref" reference="p:pull-back-grading"}, since cohomology of a complex commutes with pull-back along a flat map (see [@hr2017 Equation 1.9]), and the pull-back functor along a faithfully flat map is conservative. Hence we may assume that $S$ is affine and that the gerbe $\alpha\colon X \to S$ is trivial. Now the statement follows from the underived case described in Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"} by the monoidal decomposition preserving equivalence [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} in Lemma [\[lem:affine-derived-decomp\]](#lem:affine-derived-decomp){reference-type="ref" reference="lem:affine-derived-decomp"}. ◻
:::

::: remark
Similarly as in Remark [\[rem-coprod-prod\]](#rem-coprod-prod){reference-type="ref" reference="rem-coprod-prod"}, the canonical morphism $\bigoplus_{\chi\in A} \mathcal{F}_\chi
\to
\prod_{\chi\in A} \mathcal{F}_\chi$ is an isomorphism even if the character group $A$ is not finite.
:::

The following two propositions are the derived analogs of Proposition [\[p:pull-back-grading\]](#p:pull-back-grading){reference-type="ref" reference="p:pull-back-grading"} and [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"}.

::: proposition
[]{#p:pull-back-grading-derived label="p:pull-back-grading-derived"} Let $S$ be an algebraic stack and $\alpha\colon X \to S$ a gerbe banded by a diagonalizable group $\Delta$. Let $f\colon T \to S$ be a morphism of algebraic stacks, and let $g\colon Y \to X$ denote the canonical morphism from the pull-back $Y$ of $X$ along $f$. Then the functors $$g^*\colon {\operatorname{D}}_{\operatorname{qc}}(X) \to {\operatorname{D}}_{\operatorname{qc}}(Y), \qquad
g_*\colon {\operatorname{D}}_{\operatorname{qc}}(Y) \to {\operatorname{D}}_{\operatorname{qc}}(X)$$ respect the decompositions of ${\operatorname{D}}_{\operatorname{qc}}(X)$ and ${\operatorname{D}}_{\operatorname{qc}}(Y)$ into homogeneous components given in Theorem [\[t:chi-splitting-D-qc-X\]](#t:chi-splitting-D-qc-X){reference-type="ref" reference="t:chi-splitting-D-qc-X"}.
:::

::: proof
*Proof.* As a formal consequence of adjunction, it is enough to verify that the pull-back $g^*$ respects the decomposition. By a similar reduction argument as in the last paragraph of the proof of Theorem [\[t:chi-splitting-D-qc-X\]](#t:chi-splitting-D-qc-X){reference-type="ref" reference="t:chi-splitting-D-qc-X"}, we reduce to the case when $S$ and $T$ are affine and the gerbes are trivial. Now the result follows from the underived setting in Proposition [\[p:pull-back-grading\]](#p:pull-back-grading){reference-type="ref" reference="p:pull-back-grading"} and the commutative diagram [\[eq-commute-derived\]](#eq-commute-derived){reference-type="eqref" reference="eq-commute-derived"} in Lemma [\[lem:affine-derived-decomp\]](#lem:affine-derived-decomp){reference-type="ref" reference="lem:affine-derived-decomp"}. ◻
:::

::: proposition
[]{#t:equivalence-epi-derived label="t:equivalence-epi-derived"} Let $X$ and $X'$ be gerbes over $S$ banded by diagonalizable groups $\Delta$ and $\Delta'$, respectively, and let $\rho\colon X \to X'$ be a morphism over $S$ with induced morphism $\varphi\colon \Delta_S \to \Delta'_S$ on the bands. Fix a character $\chi'\colon \Delta'_S \to {\ensuremath{\mathbb{G}_{\operatorname{m},S}}}$, and let $\chi =
  \chi' \circ \varphi$. Then the pull-back functor $\rho^*$ takes $\chi'$-homogeneous objects to $\chi$-homogeneous objects and induces an equivalence $$\label{eq:restricted-pb-derived}
    \rho^*\colon {\operatorname{D}}_{{\operatorname{qc}},\chi'}(X') \xrightarrow[{}]{\sim}{\operatorname{D}}_{{\operatorname{qc}},\chi}(X)$$ of triangulated categories. In particular, if $X' = S$ then $\rho^*\colon {\operatorname{D}}_{\operatorname{qc}}(S) \to {\operatorname{D}}_{\operatorname{qc}}(X)$ is fully faithful with essential image consisting of those objects that are homogeneous for the trivial character.
:::

::: proof
*Proof.* Since $\rho$ is flat (see Remark [\[rem-gerbe-ff\]](#rem-gerbe-ff){reference-type="ref" reference="rem-gerbe-ff"}), the pull-back $\rho^*$ commutes with taking cohomology (see [@hr2017 Equation (1.9)]). In particular, the first statement follows from the underived case, which is given by Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"}.

Let us first consider the special case $X' = S$. By Remark [\[rem-gerbe-concentrated\]](#rem-gerbe-concentrated){reference-type="ref" reference="rem-gerbe-concentrated"}, the morphism $\rho$ is concentrated, so the push-forward $\rho_*$ respects flat base change by [@hr2017 Theorem 2.6(4)]. Hence the statement can be verified locally. In particular, we may assume that the gerbes are trivial and that $S$ is affine. Hence we may use the equivalences in Lemma [\[lem:affine-derived-decomp\]](#lem:affine-derived-decomp){reference-type="ref" reference="lem:affine-derived-decomp"}. Since $\rho^*$ and $\rho_*$ are exact, the statement follows from the underived case, which is Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"}.

For the general case, we proceed exactly as in the proof of Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"} on the level of derived categories. ◻
:::

Similarly as in the underived case, we get the following corollaries.

::: corollary
[]{#cor:twisted-power-derived label="cor:twisted-power-derived"} Let $S$ be an algebraic stacks and let $\alpha\colon X \to S$ be a gerbe banded by $\Delta$, and choose a character $\chi\colon \Delta_S \to {\ensuremath{\mathbb{G}_{\operatorname{m},S}}}$. Then we have an equivalence $${\operatorname{D}}_{{\operatorname{qc}},\chi_*\alpha}(S)\cong {\operatorname{D}}_{{\operatorname{qc}}, \chi}(X)$$ of categories, where $\chi_*\alpha$ is defined as in Construction [\[cons-gerbe-pf\]](#cons-gerbe-pf){reference-type="ref" reference="cons-gerbe-pf"}. In the particular case when $\Delta = {\ensuremath{\mathbb{G}_{\operatorname{m}}}}$, this gives the equivalence $${\operatorname{D}}_{{\operatorname{qc}},\alpha^d}(S)\cong {\operatorname{D}}_{{\operatorname{qc}},d}(X)$$ for any $d \in \mathbb{Z}$, where $\alpha^d$ is defined as in Construction [\[cons-gerbe-operations\]](#cons-gerbe-operations){reference-type="ref" reference="cons-gerbe-operations"}.
:::

::: proof
*Proof.* This is proven similarly as Corollary [\[cor:twisted-power\]](#cor:twisted-power){reference-type="ref" reference="cor:twisted-power"} by using Proposition [\[t:equivalence-epi-derived\]](#t:equivalence-epi-derived){reference-type="ref" reference="t:equivalence-epi-derived"} instead of Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"}. ◻
:::

::: corollary
[]{#cor:twisted-tensor-derived label="cor:twisted-tensor-derived"} Let $S$ be an algebraic stack and let $\alpha\colon X \to S$ and $\beta\colon Y \to S$ be ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$-gerbes. Then the tensor product and the internal Hom-functor on ${\operatorname{D}}_{\operatorname{qc}}(X\times_S Y)$ induce triangulated functors $$\begin{aligned}
\otimes & \colon {\operatorname{D}}_{{\operatorname{qc}}, \alpha}(S) \times {\operatorname{D}}_{{\operatorname{qc}}, \beta}(S)
\to {\operatorname{D}}_{{\operatorname{qc}}, \alpha\beta}(S),\\
{\mathcal{H}{om}}& \colon {\operatorname{D}}_{{\operatorname{qc}}, \alpha}(S)^{\operatorname{op}}\times {\operatorname{D}}_{{\operatorname{qc}}, \beta}(S)
\to {\operatorname{D}}_{{\operatorname{qc}}, \alpha^{-1}\beta}(S).
\end{aligned}$$ Furthermore, if $f\colon T \to S$ is an arbitrary morphism of algebraic stacks, then we get an induced pair of adjoint functors $$f^* \colon {\operatorname{D}}_{{\operatorname{qc}}, \alpha}(S) \to {\operatorname{D}}_{{\operatorname{qc}}, f^*\alpha}(T),
  \qquad
  f_* \colon {\operatorname{D}}_{{\operatorname{qc}}, f^*\alpha}(T) \to {\operatorname{D}}_{{\operatorname{qc}}, \alpha}(S).$$
:::

::: proof
*Proof.* This is proven similarly as Corollary [\[cor:twisted-tensor\]](#cor:twisted-tensor){reference-type="ref" reference="cor:twisted-tensor"} by using Theorem [\[t:chi-splitting-D-qc-X\]](#t:chi-splitting-D-qc-X){reference-type="ref" reference="t:chi-splitting-D-qc-X"}, Proposition [\[p:pull-back-grading-derived\]](#p:pull-back-grading-derived){reference-type="ref" reference="p:pull-back-grading-derived"} and Proposition [\[t:equivalence-epi-derived\]](#t:equivalence-epi-derived){reference-type="ref" reference="t:equivalence-epi-derived"} instead of Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}, Proposition [\[p:pull-back-grading\]](#p:pull-back-grading){reference-type="ref" reference="p:pull-back-grading"} and Proposition [\[t:equivalence-epi\]](#t:equivalence-epi){reference-type="ref" reference="t:equivalence-epi"}. ◻
:::

We conclude the section with two remarks regarding alternative approaches for proving Theorem [\[t:chi-splitting-D-qc-X\]](#t:chi-splitting-D-qc-X){reference-type="ref" reference="t:chi-splitting-D-qc-X"}.

::: remark
[]{#rem-trivial-case label="rem-trivial-case"} Note that Theorem [\[t:chi-splitting-D-qc-X\]](#t:chi-splitting-D-qc-X){reference-type="ref" reference="t:chi-splitting-D-qc-X"} is trivial whenever the functor [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is a monoidal equivalence. By Lieblich [@lieblich2004 Proposition 2.2.4.6], the functor [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is an equivalence whenever $S$ is a quasi-compact, separated scheme. More generally, it follows from the work by Hall, Neeman and Rydh [@hnr2018 Theorem 1.2] that [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is an equivalence whenever $S$ is an algebraic space which is either noetherian or quasi-compact with affine diagonal. The aforementioned theorem applies since in this case, the category ${\operatorname{D}}_{\operatorname{qc}}(X)$ is compactly generated by $|A|$ objects by [@hr2017 Theorem 6.9] applied to the presheaf $(T \to S) \mapsto {\operatorname{D}}_{\operatorname{qc}}(X_T)$ of triangulated categories. Since we are not going to use this result, we leave the details of verifying the hypotheses of the cited theorem to the reader (cf. [@hr2017 Example 9.2]). We do not know whether the equivalence [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is monoidal in this generality.

Finally, it should be emphasized that there certainly are interesting cases when [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is not an equivalence. For instance, consider the ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$-gerbe in Example [\[ex-gerbes\]](#ex-gerbes){reference-type="ref" reference="ex-gerbes"}.[\[it-universal-projective\]](#it-universal-projective){reference-type="ref" reference="it-universal-projective"}. The functor [\[eq-equiv-qcoh\]](#eq-equiv-qcoh){reference-type="eqref" reference="eq-equiv-qcoh"} is not an equivalence for $X = \mathop{\mathrm{B}}\mathop{\mathrm{GL}}_n$ if $n \geq 2$ by [@hnr2018 Theorem 1.3], so Theorem [\[t:chi-splitting-D-qc-X\]](#t:chi-splitting-D-qc-X){reference-type="ref" reference="t:chi-splitting-D-qc-X"} seems to be non-trivial even in this basic case.
:::

::: remark
[]{#rem:decomposition-O-modules label="rem:decomposition-O-modules"} Theorem [\[t:chi-splitting-D-qc-X\]](#t:chi-splitting-D-qc-X){reference-type="ref" reference="t:chi-splitting-D-qc-X"} would be trivial if the category ${\ensuremath{\operatorname{Mod}}}(X_{\operatorname{lis-\acute{e}t}}, \mathcal{O}_X)$ admitted a decomposition similar to the one for ${\ensuremath{\operatorname{Qcoh}}}(X)$ described in Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}. We do not know whether this is the case, but we suspect it is not.

In [@sga-3-1-2011 Exposé 1, Proposition 4.7.2], it is stated that the category of (not necessarily quasi-coherent) sheaves of $G-\mathcal{O}_S$-modules on the small Zariski site is equivalent to the category of sheaves of $\mathcal{A}$-comodules for any affine group scheme $G = \mathop{\mathrm{Spec}}_S \mathcal{A}$ over a scheme $S$. If this were true, then it should be possible to adapt the proof to our situation and to get a decomposition of ${\ensuremath{\operatorname{Mod}}}(X_{\operatorname{lis-\acute{e}t}}, \mathcal{O}_X)$. However, we suspect that the previously cited proposition might be wrong, since it uses [@sga-3-1-2011 Exposé 1, Proposition 4.6.4] which in turn uses the fact that the canonical morphism $$\label{eq:qcoh-push-pull}
  \mathcal{F}\otimes_S \mathcal{A} \to \alpha_\ast\alpha^\ast\mathcal{F}$$ is an isomorphism whenever $\mathcal{F}$ is quasi-coherent and $\alpha\colon X = \mathop{\mathrm{Spec}}_S \mathcal{A} \to S$ is affine. But this is certainly not true in general if we drop the condition that $\mathcal{F}$ be quasi-coherent.

Let for example $S$ be a scheme with an open subscheme $U$ such that the inclusion $j \colon U \rightarrow S$ is affine and quasi-compact and $\mathcal{F}=j_! \mathcal{O}_U$ is not quasi-coherent. Then the canonical morphism $j_!
\mathcal{O}_U \cong \mathcal{F} \otimes j_*\mathcal{O}_U \rightarrow
j_*j^* \mathcal{F} \cong j_*\mathcal{O}_U$ is not an isomorphism because $j_*\mathcal{O}_U$ is quasi-coherent. Let $G:=S \sqcup U$ be the disjoint union. Then $\alpha \colon G \rightarrow S$ is in the obvious way an affine étale group scheme over $S$. In this case $\mathcal{A}=\alpha_*\mathcal{O}_G=
\mathcal{O}_S \oplus
j_*\mathcal{O}_U$ and the morphism [\[eq:qcoh-push-pull\]](#eq:qcoh-push-pull){reference-type="eqref" reference="eq:qcoh-push-pull"} is not an isomorphism for $\mathcal{F}=j_! \mathcal{O}_U$.
:::
