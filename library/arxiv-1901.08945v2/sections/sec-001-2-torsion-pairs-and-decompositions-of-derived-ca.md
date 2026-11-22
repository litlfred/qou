---
doc_id: arxiv-1901.08945v2
doc_title: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties"
section_id: sec-001-2-torsion-pairs-and-decompositions-of-derived-ca
section_title: "Torsion pairs and decompositions of derived categories"
section_number: 2
pages: 5-13
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.974
doc_brief: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group"
---
[]{#sec:torsion-pairs-decomp label="sec:torsion-pairs-decomp"}

We give criteria ensuring that a torsion pair in an abelian category gives rise to a semi-orthogonal decomposition on the level of derived categories. Our main assumption on the torsion pair is that its two components are abelian subcategories of the ambient abelian category. For bounded derived categories this is straightforward (see Theorem [\[t:sod-DbBA\]](#t:sod-DbBA){reference-type="ref" reference="t:sod-DbBA"}) as soon as some foundational results for such torsion pairs are established (see Proposition [\[p:abelian-torsion-pair\]](#p:abelian-torsion-pair){reference-type="ref" reference="p:abelian-torsion-pair"}). Our result for unbounded derived categories (see Theorem [\[t:sod-DBA\]](#t:sod-DBA){reference-type="ref" reference="t:sod-DBA"}) needs some technical assumptions on effectiveness of inverse and direct truncation systems introduced in Section [0.3](#sec:notes-htpy-limits){reference-type="ref" reference="sec:notes-htpy-limits"}. Fortunately, these assumptions are satisfied for the derived category ${\operatorname{D}}_{\operatorname{qc}}(X)$ of an algebraic stack (see Example [\[ex:ringed-topos-effective\]](#ex:ringed-topos-effective){reference-type="ref" reference="ex:ringed-topos-effective"} and Proposition [\[p:Dqc-truncation-complete\]](#p:Dqc-truncation-complete){reference-type="ref" reference="p:Dqc-truncation-complete"}).

## Torsion pairs {#sec:torsion-pairs}

We remind the reader of the notion of a *torsion pair*. Sometimes the terminology *torsion theory* is used in the literature. Standard references are [@beligiannis-reiten-torsion-theories I.1], [@borceux-cat-2 1.12], [@dickson-torsion].

::: definition
[]{#d:torsion-pair label="d:torsion-pair"} A *torsion pair* in an abelian category $\mathcal{B}$ is a pair $(\mathcal{T}, \mathcal{F})$ of strictly full subcategories of $\mathcal{B}$ such that the following two conditions hold:

1.  []{#enum:TP-ses label="enum:TP-ses"} Any object $B \in \mathcal{B}$ fits into a short exact sequence $$0 \rightarrow T \rightarrow B \rightarrow F \rightarrow 0$$ with $T \in \mathcal{T}$ and $F \in \mathcal{F}$.

2.  []{#enum:TP-Hom-TF=0 label="enum:TP-Hom-TF=0"} We have $\mathop{\mathrm{Hom}}_\mathcal{B}(T, F)=0$ for all objects $T \in
        \mathcal{T}$ and $F \in \mathcal{F}$.
:::

::: remark
[]{#rem:adjoints-f-and-t label="rem:adjoints-f-and-t"} Let $(\mathcal{T}, \mathcal{F})$ be a torsion pair in an abelian category $\mathcal{B}$. The axioms of a torsion pair immediately imply that the short exact sequence in [\[enum:TP-ses\]](#enum:TP-ses){reference-type="ref" reference="enum:TP-ses"} is unique up to unique isomorphism and functorial in $B \in \mathcal{B}$. In particular, there are functors $t \colon \mathcal{B} \rightarrow\mathcal{T}$ and $f \colon
  \mathcal{B} \rightarrow\mathcal{F}$ together with natural transformations $t \rightarrow{\operatorname{id}}$ and ${\operatorname{id}}\rightarrow f$ giving rise to short exact sequences $$0 \rightarrow t(B) \rightarrow B \rightarrow f(B) \rightarrow 0,$$ for each object $B \in \mathcal{B}$. The object $B$ is in $\mathcal{T}$ (resp. $\mathcal{F})$ if and only if $f(B)=0$ (resp. $t(B)=0$). The functor $t$ is right adjoint to the inclusion functor $\mathcal{T} \rightarrow\mathcal{B}$, and the functor $f$ is left adjoint to the inclusion functor $\mathcal{F} \rightarrow\mathcal{B}$.
:::

Recall that an *abelian subcategory* of an abelian category is a strictly full subcategory which is abelian and whose inclusion functor is exact. A *weak Serre subcategory* is an abelian subcategory which is closed under extensions in the ambient category. If it is even closed under taking subobjects and quotients in the ambient category, it is called a *Serre subcategory*.

::: remark
In the following we are only interested in torsion pairs $(\mathcal{T}, \mathcal{F})$ where both $\mathcal{T}$ and $\mathcal{F}$ are abelian subcategories. These torsion pairs are traditionally called *hereditary* and *cohereditary*. We do not use this terminology.
:::

::: example
[]{#e:A2-reps label="e:A2-reps"} Let $\mathcal{B}$ be the category of representations of the $A_2$-quiver $1 \rightarrow 2$ over some ring. If $\mathcal{T}$ (resp. $\mathcal{F}$) denotes the subcategory of representations supported at the vertex $2$ (resp. $1$) then $(\mathcal{T}, \mathcal{F})$ is clearly a torsion pair in $\mathcal{B}$. Moreover, both $\mathcal{T}$ and $\mathcal{F}$ are abelian subcategories of $\mathcal{B}$.
:::

::: proposition
[]{#p:abelian-torsion-pair label="p:abelian-torsion-pair"} Let $(\mathcal{T}, \mathcal{F})$ be a torsion pair in an abelian category $\mathcal{B}$. If both $\mathcal{T}$ and $\mathcal{F}$ are abelian subcategories of $\mathcal{B}$, then the following statements are true.

1.  []{#enum:Hom-FT label="enum:Hom-FT"}

    $\mathop{\mathrm{Hom}}_\mathcal{B}(F, T)=0$ for all objects $F \in
        \mathcal{F}$ and $T \in 
        \mathcal{T}$.

2.  []{#enum:adjoints-exact label="enum:adjoints-exact"} Both the right adjoint to the inclusion functor $\mathcal{T} \rightarrow\mathcal{B}$ and the left adjoint to the inclusion functor $\mathcal{F} \rightarrow\mathcal{B}$ are exact, i.e., in the notation of Remark [\[rem:adjoints-f-and-t\]](#rem:adjoints-f-and-t){reference-type="ref" reference="rem:adjoints-f-and-t"}, both functors $t$ and $f$ are exact.

3.  []{#enum:serre-subcats label="enum:serre-subcats"} Both $\mathcal{T}$ and $\mathcal{F}$ are Serre subcategories of $\mathcal{B}$.

4.  []{#enum:Ext-TF label="enum:Ext-TF"} $\mathop{\mathrm{Ext}}^n_\mathcal{B}(T,F)=0$ for all objects $T \in \mathcal{T}$, $F \in \mathcal{F}$ and all integers $n
        \in {\mathbb{Z}}$.
:::

::: remark
The most interesting part of Proposition [\[p:abelian-torsion-pair\]](#p:abelian-torsion-pair){reference-type="ref" reference="p:abelian-torsion-pair"} is certainly the $\mathop{\mathrm{Ext}}$-vanishing result in part [\[enum:Ext-TF\]](#enum:Ext-TF){reference-type="ref" reference="enum:Ext-TF"}. After writing down its proof we learned that Brion has recently obtained the same result [@brion2018 Lemma 2.3]. For the convenience of the reader we give a full proof of Proposition [\[p:abelian-torsion-pair\]](#p:abelian-torsion-pair){reference-type="ref" reference="p:abelian-torsion-pair"} even though parts [\[enum:Hom-FT\]](#enum:Hom-FT){reference-type="ref" reference="enum:Hom-FT"}, [\[enum:adjoints-exact\]](#enum:adjoints-exact){reference-type="ref" reference="enum:adjoints-exact"}, [\[enum:serre-subcats\]](#enum:serre-subcats){reference-type="ref" reference="enum:serre-subcats"} are well-known or straightforward.
:::

::: proof
*Proof.* [\[enum:Hom-FT\]](#enum:Hom-FT){reference-type="ref" reference="enum:Hom-FT"} Let ${\varphi}\colon F \rightarrow T$ be a morphism from $F
  \in \mathcal{F}$ to $T \in \mathcal{T}$. By [\[enum:TP-ses\]](#enum:TP-ses){reference-type="ref" reference="enum:TP-ses"}, we may put $\mathop{\mathrm{Ker}}({\varphi})$ into a short exact sequence $0 \rightarrow T' \rightarrow\mathop{\mathrm{Ker}}({\varphi}) \rightarrow F' \rightarrow 0$ with $T' \in
  \mathcal{T}$ and $F' \in \mathcal{F}$. Since the composition of monomorphisms $T' \rightarrow\mathop{\mathrm{Ker}}({\varphi}) \rightarrow F$ is zero, by [\[enum:TP-Hom-TF=0\]](#enum:TP-Hom-TF=0){reference-type="ref" reference="enum:TP-Hom-TF=0"}, we have $T'=0$ and $\mathop{\mathrm{Ker}}({\varphi}) \in \mathcal{F}$. Similarly one shows $\mathop{\mathrm{Cok}}({\varphi}) \in
  \mathcal{T}$. But then $\mathop{\mathrm{Im}}({\varphi})$ is the cokernel of $\mathop{\mathrm{Ker}}({\varphi}) \rightarrow F$ and the kernel of $T \rightarrow\mathop{\mathrm{Cok}}({\varphi})$ and hence is in $\mathcal{F} \cap
  \mathcal{T}$ since both $\mathcal{F}$ and $\mathcal{T}$ are abelian subcategories, i.e., $\mathop{\mathrm{Im}}({\varphi})=0$ and ${\varphi}=0$.

[\[enum:adjoints-exact\]](#enum:adjoints-exact){reference-type="ref" reference="enum:adjoints-exact"} We use the notation of Remark [\[rem:adjoints-f-and-t\]](#rem:adjoints-f-and-t){reference-type="ref" reference="rem:adjoints-f-and-t"}. Clearly, $t$ and $f$ are additive. Let $0 \rightarrow B_1 \rightarrow B_2 \rightarrow B_3 \rightarrow 0$ be a short exact sequence in $\mathcal{B}$. Then we obtain a commutative diagram with exact rows $$\xymatrix{
      {0} \ar[r]
      &
      {t(B_3)} \ar[r]
      &
      {B_3} \ar[r]
      &
      {f(B_3)} \ar[r]
      &
      {0}
      \\
      {0} \ar[r]
      &
      {t(B_2)} \ar[r] \ar[u]
      &
      {B_2} \ar[r] \ar[u]
      &
      {f(B_2)} \ar[r] \ar[u]
      &
      {0}
      \\
      {0} \ar[r]
      &
      {t(B_1)} \ar[r] \ar[u]
      &
      {B_1} \ar[r] \ar[u]
      &
      {f(B_1)} \ar[r] \ar[u]
      &
      {0.}
    }$$ We view the columns as complexes in $\mathcal{B}$ by adding zeroes. Then the diagram is a short exact sequence of complexes and gives rise to a long exact sequence on cohomology. Since the middle column is exact, since the cohomology objects of the left (resp. right) column are in $\mathcal{T}$ (resp. $\mathcal{F})$, and since there are no nonzero morphisms from $\mathcal{F}$ to $\mathcal{T}$, by [\[enum:Hom-FT\]](#enum:Hom-FT){reference-type="ref" reference="enum:Hom-FT"}, the other two columns are also exact. This shows that $t$ and $f$ are exact.

[\[enum:serre-subcats\]](#enum:serre-subcats){reference-type="ref" reference="enum:serre-subcats"} Let $F \rightarrow B \rightarrow F'$ be an exact sequence in $\mathcal{B}$ where $F$ and $F'$ are objects of $\mathcal{F}$. To see that $\mathcal{F}$ is a Serre subcategory of $\mathcal{B}$ we need to see that $B \in \mathcal{F}$. The functor $t \colon \mathcal{B} \rightarrow
  \mathcal{T}$ is exact, by [\[enum:adjoints-exact\]](#enum:adjoints-exact){reference-type="ref" reference="enum:adjoints-exact"}, and hence yields the exact sequence $t(F) \rightarrow t(B) \rightarrow t(F')$ in $\mathcal{T}$. Since $t(F)=0=t(F')$ we obtain $t(B)=0$, i.e., $B \in
  \mathcal{F}$.

The same argument proves that $\mathcal{T}$ is a Serre subcategory of $\mathcal{B}$.

[\[enum:Ext-TF\]](#enum:Ext-TF){reference-type="ref" reference="enum:Ext-TF"} The claim is trivially true for $n<0$. For $n=0$ it is true by axiom [\[enum:TP-Hom-TF=0\]](#enum:TP-Hom-TF=0){reference-type="ref" reference="enum:TP-Hom-TF=0"} of a torsion pair.

For $n=1$ we need to prove that $\mathop{\mathrm{Ext}}^1_\mathcal{B}(T,F)=0$ for $T \in \mathcal{T}$ and $F \in \mathcal{F}$. Using Yoneda extensions (and [@stacks-project [Tag 06XU](http://stacks.math.columbia.edu/tag/06XU)]) it is enough to show that any short exact sequence $0 \rightarrow F \rightarrow B \rightarrow T \rightarrow 0$ in $\mathcal{B}$ splits. Since $t$ is exact, by [\[enum:adjoints-exact\]](#enum:adjoints-exact){reference-type="ref" reference="enum:adjoints-exact"}, and $t(F)=0$, we obtain a morphism of short exact sequences $$\xymatrix{
      {0} \ar[r] 
      &
      {0} \ar[r] \ar[d]
      &
      {t(B)} \ar[r]^-{\sim} \ar[d]
      &
      {t(T)} \ar[r] \ar[d]^-{\sim}
      &
      {0}
      \\
      {0} \ar[r] 
      &
      {F} \ar[r]
      &
      {B} \ar[r]
      &
      {T} \ar[r]
      &
      {0}
    }$$ in $\mathcal{B}$; the vertical arrow on the right is an isomorphism since $T \in \mathcal{T}$ and hence $f(T)=0$. This shows that our sequence splits. (Since $\mathop{\mathrm{Hom}}_\mathcal{B}(T,F)=0$, the splitting is in fact unique.)

Now let $n \geq 2$. Let $f \in \mathop{\mathrm{Ext}}_\mathcal{B}^n(T,F)$, i.e., $f \colon T \rightarrow
  \Sigma^n F$ is a morphism in ${\operatorname{D}}(\mathcal{B})$. The $n$-extension $f$ can be written as the composition of a 1-extension and an $(n-1)$-extension: this is easy to prove directly or follows alternatively using Yoneda extensions and [@stacks-project [Tag 06XU](http://stacks.math.columbia.edu/tag/06XU)]. Anyhow, there is an object $B \in \mathcal{B}$ such that $f$ is the composition $$f \colon T \xrightarrow[{}]{g} \Sigma^{n-1}B \xrightarrow[{}]{\Sigma^{n-1}h} \Sigma^n F,$$ where $g$ and $h \colon B \rightarrow\Sigma F$ are morphisms in ${\operatorname{D}}(\mathcal{B})$. The long exact $\mathop{\mathrm{Ext}}_\mathcal{B}(-,F)$-sequence obtained from the short exact sequence $0 \rightarrow t(B) \rightarrow B \xrightarrow[{}]{\pi} f(B) \rightarrow 0$ yields an isomorphism $$\pi^* \colon 
    \mathop{\mathrm{Ext}}^1_\mathcal{B}(f(B), F) \xrightarrow[{}]{\sim}
    \mathop{\mathrm{Ext}}^1_\mathcal{B}(B, F)$$ since we already know that $\mathop{\mathrm{Ext}}^1_\mathcal{B}(t(B), F)$ and $\mathop{\mathrm{Hom}}_\mathcal{B}(t(B), F)$ vanish. Hence $h$ has the form $h=h' \circ \pi$ for a (unique) morphism $h' \colon f(B) \rightarrow\Sigma F$ in ${\operatorname{D}}(\mathcal{B})$. Then $$f=(\Sigma^{n-1}h) \circ g = (\Sigma^{n-1}h') \circ
    (\Sigma^{n-1}\pi) \circ g.$$ By induction, the $(n-1)$-extension $(\Sigma^{n-1}\pi) \circ g
  \colon T 
  \rightarrow\Sigma^{n-1}f(B)$ vanishes. Hence $f=0$. ◻
:::

## Decompositions of bounded derived categories {#sec:decomp-bound-deriv}

If $\mathcal{S}$ is a weak Serre subcategory of an abelian category $\mathcal{B}$, the full subcategory of ${\operatorname{D}}(\mathcal{B})$ of objects with cohomology objects in $\mathcal{S}$ is denoted ${\operatorname{D}}_{\mathcal{S}}(\mathcal{B})$. Let ${\operatorname{D}}_{\mathcal{S}}^-(\mathcal{B})$, ${\operatorname{D}}_{\mathcal{S}}^+(\mathcal{B})$, and ${\operatorname{D}}_{\mathcal{S}}^{\operatorname{b}}(\mathcal{B})$ denote the full subcategories of ${\operatorname{D}}_{\mathcal{S}}(\mathcal{B})$ of objects whose cohomology is bounded above, bounded below, and bounded, respectively. All these categories are strictly full triangulated subcategories of ${\operatorname{D}}(\mathcal{B})$, see, e.g., [@stacks-project [Tag 06UQ](http://stacks.math.columbia.edu/tag/06UQ)]. We refer the reader to [@BS-conservative Subsection 5.1] for the notion of a semi-orthogonal decomposition.

::: theorem
[]{#t:sod-DbBA label="t:sod-DbBA"} Let $\mathcal{B}$ be a weak Serre subcategory of an abelian category $\mathcal{A}$. Let $\mathcal{T}$ and $\mathcal{F}$ be abelian subcategories of $\mathcal{B}$ forming a torsion pair $(\mathcal{T}, \mathcal{F})$ in $\mathcal{B}$. Assume that $$\label{eq:DA-T-F}
    \mathop{\mathrm{Ext}}^n_{\mathcal{A}}(T, F)=0$$ for all objects $T \in \mathcal{T}$, $F \in \mathcal{F}$ and all integers $n$. Then $${\operatorname{D}}_{\mathcal{B}}^{\operatorname{b}}(\mathcal{A})=
    \langle {\operatorname{D}}_{\mathcal{F}}^{\operatorname{b}}(\mathcal{A}), 
    {\operatorname{D}}_{\mathcal{T}}^{\operatorname{b}}(\mathcal{A})\rangle$$ is a semi-orthogonal decomposition.
:::

::: remark
Condition [\[eq:DA-T-F\]](#eq:DA-T-F){reference-type="eqref" reference="eq:DA-T-F"} is automatically satisfied in the special case when $\mathcal{B}=\mathcal{A}$, by Proposition [\[p:abelian-torsion-pair\]](#p:abelian-torsion-pair){reference-type="ref" reference="p:abelian-torsion-pair"}.[\[enum:Ext-TF\]](#enum:Ext-TF){reference-type="ref" reference="enum:Ext-TF"}. In general, the condition is automatically satisfied for $n \leq 1$ by the same proposition, since $\mathcal{B}$ is closed under extensions.
:::

::: proof
*Proof.* By Proposition [\[p:abelian-torsion-pair\]](#p:abelian-torsion-pair){reference-type="ref" reference="p:abelian-torsion-pair"}.[\[enum:serre-subcats\]](#enum:serre-subcats){reference-type="ref" reference="enum:serre-subcats"}, $\mathcal{F}$ and $\mathcal{T}$ are Serre subcategories of $\mathcal{B}$, hence weak Serre subcategories of $\mathcal{A}$, and ${\operatorname{D}}_{\mathcal{F}}^{\operatorname{b}}(\mathcal{A})$ and ${\operatorname{D}}_{\mathcal{T}}^{\operatorname{b}}(\mathcal{A})$ are strictly full triangulated subcategories of ${\operatorname{D}}_\mathcal{B}^{\operatorname{b}}(\mathcal{A})$.

Repeated use of truncation shows that ${\operatorname{D}}_{\mathcal{B}}^{\operatorname{b}}(\mathcal{A})$ coincides with its smallest strictly full triangulated subcategory containing $\mathcal{B}$. Axiom [\[enum:TP-ses\]](#enum:TP-ses){reference-type="ref" reference="enum:TP-ses"} shows that it is also its smallest such subcategory containing both $\mathcal{F}$ and $\mathcal{T}$. In particular, ${\operatorname{D}}_{\mathcal{B}}^{\operatorname{b}}(\mathcal{A})$ is generated, as a triangulated category, by its subcategories ${\operatorname{D}}_{\mathcal{F}}^{\operatorname{b}}(\mathcal{A})$ and ${\operatorname{D}}_{\mathcal{T}}^{\operatorname{b}}(\mathcal{A})$.

By truncation and condition [\[eq:DA-T-F\]](#eq:DA-T-F){reference-type="eqref" reference="eq:DA-T-F"}, there are no nonzero morphisms from ${\operatorname{D}}_{\mathcal{T}}^{\operatorname{b}}(\mathcal{A})$ to ${\operatorname{D}}_{\mathcal{F}}^{\operatorname{b}}(\mathcal{A})$. ◻
:::

## Some notes on homotopy limits of truncations {#sec:notes-htpy-limits}

Our aim is to state and prove Theorem [\[t:sod-DBA\]](#t:sod-DBA){reference-type="ref" reference="t:sod-DBA"} in the following subsection [0.4](#sec:decomp-unbo-deriv){reference-type="ref" reference="sec:decomp-unbo-deriv"} which is the analog of Theorem [\[t:sod-DbBA\]](#t:sod-DbBA){reference-type="ref" reference="t:sod-DbBA"} for unbounded derived categories. In order to to this, we need some terminology and some basic observations.

We refer the reader to [@neeman-tricat Definition 1.6.4] for the notion of a homotopy colimit. The definition of a homotopy limit is dual.

Let $\mathcal{A}$ be an abelian category. We propose the following terminology.

::: definition
[]{#d:truncation-system label="d:truncation-system"}

1.  An inverse system $$(F_n)_{n \in \mathbb{N}} = 
      (\dots \rightarrow F_{n+1} \rightarrow F_n \rightarrow\dots \rightarrow F_2 \rightarrow F_1 \rightarrow F_0)$$ in ${\operatorname{D}}(\mathcal{A})$ is an *inverse truncation system* if for each $n \in \mathbb{N}$ the object $F_n$ is in ${\operatorname{D}}^{\geq -n}(\mathcal{A})$ and the map $\tau_{\geq -n}F_{n+1} \to F_n$ induced by the transition morphism is an isomorphism (cf. Remark [\[rem:ITS-alternative\]](#rem:ITS-alternative){reference-type="ref" reference="rem:ITS-alternative"} for a reformulation).

2.  If ${\operatorname{D}}(\mathcal{A})$ has countable products, an inverse truncation system $(F_n)_{n \in \mathbb{N}}$ in ${\operatorname{D}}(\mathcal{A})$ is *effective* if the induced maps $\mathop{\mathrm{H}}^p(\mathop{\mathrm{holim}}_n F_n) \to
    \lim_n\mathop{\mathrm{H}}^p(F_n)$, are isomorphisms for all $p \in {\mathbb{Z}}$. Our assumption ensures the existence of homotopy limits, and all limits $\lim_n\mathop{\mathrm{H}}^p(F_n)$ exist by Remark [\[rem:ITS-alternative\]](#rem:ITS-alternative){reference-type="ref" reference="rem:ITS-alternative"} below.

Dually, we define a *direct truncation system* in the obvious way. If ${\operatorname{D}}(\mathcal{A})$ has countable coproducts we can talk about *effectiveness* of direct truncation systems.
:::

::: example
[]{#ex:ITS label="ex:ITS"} Given any object $F$ in ${\operatorname{D}}(\mathcal{A})$, we get an inverse truncation system $(\tau_{\geq-n}F)_{n \in \mathbb{N}}$ whose transition morphisms are the natural maps between the truncations. Similarly, we get a direct truncation system $(\tau_{\leq n}F)_{n \in \mathbb{N}}$.
:::

::: definition
[]{#d:standardITS label="d:standardITS"} An inverse (resp. direct) truncation system is called *standard* if it is isomorphic to an inverse (resp. direct) truncation system as in Example [\[ex:ITS\]](#ex:ITS){reference-type="ref" reference="ex:ITS"}.
:::

::: remark
Informally, one may think of an arbitrary inverse truncation system as obtained from a possibly non-existing object by truncation. Effectiveness says that the natural candidate for such an object, the homotopy limit, indeed does the job. We explain this in Remark [\[rem:effective\]](#rem:effective){reference-type="ref" reference="rem:effective"} below.
:::

::: remark
[]{#rem:ITS-alternative label="rem:ITS-alternative"} An inverse system $(F_n)_{n \in \mathbb{N}}$ in ${\operatorname{D}}(\mathcal{A})$ is an inverse truncation system if and only if $\mathop{\mathrm{H}}^p(F_n) = 0$ for all $p < -n$ and the maps $\mathop{\mathrm{H}}^p(F_{n+1}) \rightarrow\mathop{\mathrm{H}}^p(F_n)$ induced by the transition maps are isomorphisms for all $p \geq -n$. This just means that the induced inverse systems $(\mathop{\mathrm{H}}^p(F_{n}))_{n \in \mathbb{N}}$ look as follows. $$\xymatrix@R0em{
      {\ldots} \ar[r]^-{\sim} 
      & {\mathop{\mathrm{H}}^1(F_2)} \ar[r]^{\sim}
      & {\mathop{\mathrm{H}}^1(F_1)} \ar[r]^{\sim}
      & {\mathop{\mathrm{H}}^1(F_0)}
      \\
      {\ldots} \ar[r]^-{\sim} 
      & {\mathop{\mathrm{H}}^0(F_2)} \ar[r]^{\sim}
      & {\mathop{\mathrm{H}}^0(F_1)} \ar[r]^{\sim}
      & {\mathop{\mathrm{H}}^0(F_0)}
      \\
      {\ldots} \ar[r]^-{\sim} 
      & {\mathop{\mathrm{H}}^{-1}(F_2)} \ar[r]^{\sim}
      & {\mathop{\mathrm{H}}^{-1}(F_1)} \ar[r]
      & {0}
      \\
      {\ldots} \ar[r]^-{\sim} 
      & {\mathop{\mathrm{H}}^{-2}(F_2)} \ar[r]
      & {0} \ar[r]
      & {0}
     }$$ In particular, then all limits $\lim_n\mathop{\mathrm{H}}^p(F_n)$ exist in $\mathcal{A}$.
:::

::: remark
[]{#rem:effective label="rem:effective"} Assume that ${\operatorname{D}}(\mathcal{A})$ has countable products. Let $G:=\mathop{\mathrm{holim}}_n F_n$ be a homotopy limit of an inverse truncation system $(F_n)_{n \in {\mathbb{N}}}$. It comes together with morphisms $G \rightarrow F_n$, for all $n \in {\mathbb{Z}}$. Since $F_n \in {\operatorname{D}}^{\geq -n}(\mathcal{A})$ they come from unique morphisms $\tau_{\geq -n}G \rightarrow F_n$. Then, as a consequence of Remark [\[rem:ITS-alternative\]](#rem:ITS-alternative){reference-type="ref" reference="rem:ITS-alternative"}, the following conditions are equivalent.

1.  The inverse truncation system $(F_n)_{n \in {\mathbb{N}}}$ is effective.

2.  For all $p \in {\mathbb{Z}}$ there is an integer $n \geq -p$ such that $\mathop{\mathrm{H}}^p(G) \to
        \mathop{\mathrm{H}}^p(F_n)$ is an isomorphism; this condition is then automatically true for all integers $n \geq -p$.

3.  The morphism $(\tau_{\geq -n} G)_{n \in {\mathbb{N}}} \rightarrow(F_n)_{n \in
          {\mathbb{N}}}$ of inverse truncation systems is an isomorphism.

In particular, any effective inverse truncation system is standard in the sense of Definition [\[d:standardITS\]](#d:standardITS){reference-type="ref" reference="d:standardITS"}; more precisely, up to canonical isomorphism it is obtained by truncation from its homotopy limit.
:::

We address the natural question whether an object is the homotopy limit of its truncations.

::: lemma
[]{#l:holim-truncations label="l:holim-truncations"} Let $F$ be an object of ${\operatorname{D}}(\mathcal{A})$ and assume that ${\operatorname{D}}(\mathcal{A})$ has countable products. If the inverse truncation system $(\tau_{\geq -n}F)_{n \in {\mathbb{N}}}$ is effective there is a triangle $$F \rightarrow\prod_{n \in {\mathbb{N}}} \tau_{\geq -n} F \rightarrow\prod_{n \in
      {\mathbb{N}}} \tau_{\geq -n} F \rightarrow\Sigma F$$ in ${\operatorname{D}}(\mathcal{A})$ which exhibits $F$ as a homotopy limit of its truncations and whose first morphism is induced by the truncation maps $F \rightarrow\tau_{\geq -n}F$.
:::

::: proof
*Proof.* Let $G$ be a homotopy limit of the given inverse system with defining triangle $$G \rightarrow\prod \tau_{\geq -n}F \rightarrow\prod \tau_{\geq -n}F \rightarrow
    \Sigma G.$$ The obvious map from $F$ to the second term of this triangle comes from a (possibly non-unique) morphism $\gamma \colon F \rightarrow G$ to its first term which makes the upper left triangle in the following diagram commutative. Since the map $G \rightarrow\tau_{\geq -n}F$ factors through the truncation map $G \rightarrow\tau_{\geq -n}G$, we obtain the commutative diagram $$\xymatrix{
      {F} \ar[r] \ar[d]^-{\gamma} & {\tau_{\geq -n}F}\\
      {G} \ar[r] \ar[ur] & {\tau_{\geq -n} G.} \ar[u]
    }$$ Its right vertical arrow is an isomorphism since the inverse truncation system $(\tau_{\geq -n}F)_{n \in
    {\mathbb{N}}}$ is effective, by the equivalent statements in Remark [\[rem:effective\]](#rem:effective){reference-type="ref" reference="rem:effective"}. Hence the inverse of this arrow is the morphism $\tau_{\geq -n}(\gamma)$ which is therefore an isomorphism. Since $n \in {\mathbb{N}}$ was arbitrary, this implies that $\gamma$ is an isomorphism. The claim follows. ◻
:::

We now provide instances of inverse and direct truncation systems that are effective. The following proposition is essentially Remark 2.3 in [@neeman-homotopy-limits].

::: proposition
[]{#p:ab4-trunc label="p:ab4-trunc"} Let $\mathcal{A}$ be an abelian category. If $\mathcal{A}$ has countable products which are exact then any inverse truncation system in ${\operatorname{D}}(\mathcal{A})$ is effective. Dually, if $\mathcal{A}$ has exact countable coproducts then any direct truncation system in ${\operatorname{D}}(\mathcal{A})$ is effective.
:::

::: proof
*Proof.* Since the statements are dual, it is enough to prove one of them. We prove the first statement.

It is clear that ${\operatorname{D}}(\mathcal{A})$ has all countable products. Let $(F_n)_{n \in \mathbb{N}}$ be an inverse truncation system in ${\operatorname{D}}(\mathcal{A})$. Consider a homotopy limit $\mathop{\mathrm{holim}}_n F_n$ together with a defining triangle $$\mathop{\mathrm{holim}}_n F_n \to \prod_n F_n \xrightarrow{1 - \sigma}
    \prod_n F_n \to \Sigma \mathop{\mathrm{holim}}_n F_n,$$ where $\sigma$ is the shift map. Since $\mathcal{A}$ has exact countable products, the functor $\mathop{\mathrm{H}}^p(-)$ preserves countable products for all $p$. Hence, we get an exact sequence $$\dots
    \xrightarrow{\delta} 
    \mathop{\mathrm{H}}^p(\mathop{\mathrm{holim}}_n F_n) \to 
    \prod_n \mathop{\mathrm{H}}^p(F_n) \xrightarrow{1 - \sigma} 
    \prod_n \mathop{\mathrm{H}}^p(F_n) \xrightarrow{\delta} 
    \mathop{\mathrm{H}}^{p + 1}(\mathop{\mathrm{holim}}_n F_n)
    \rightarrow\dots$$ in $\mathcal{A}$ where $\sigma$ is again the shift map. Note that the inverse system $(\mathop{\mathrm{H}}^p(F_n))_{n \in \mathbb{N}}$ is zero for $n < -p$ and constant for $n \geq -p$ (cf. Remark [\[rem:ITS-alternative\]](#rem:ITS-alternative){reference-type="ref" reference="rem:ITS-alternative"}). Hence Remark [\[rem:1-shift-split-epi\]](#rem:1-shift-split-epi){reference-type="ref" reference="rem:1-shift-split-epi"} below shows that all morphisms $1- \sigma$ in our exact sequence are epimorphisms, i.e., all connecting morphisms $\delta$ vanish. Hence the canonical morphism $$\mathop{\mathrm{H}}^p(\mathop{\mathrm{holim}}_n F_n) \to \lim_n \mathop{\mathrm{H}}^p(F_n)$$ is an isomorphism, i.e., our inverse truncation system is effective. ◻
:::

::: remark
[]{#rem:1-shift-split-epi label="rem:1-shift-split-epi"} If an inverse system $(G_n)_{n \in {\mathbb{N}}}$ in an additive category with countable products is *eventually constant* in the sense that there is an $N \in {\mathbb{N}}$ such that all transition morphisms $G_{n+1} \rightarrow G_n$ for $n \geq N$ are isomorphisms, then the morphism "identity minus shift" $$1-\sigma \colon \prod_{n \in {\mathbb{N}}} G_n \rightarrow\prod_{n \in {\mathbb{N}}} G_n$$ is a split epimorphism: there is a morphism $f$ in the other direction such that $(1-\sigma) \circ f = {\operatorname{id}}$. We leave the easy proof of this fact to the reader.
:::

::: example
[]{#ex:modules-effective label="ex:modules-effective"} If $R$ is an arbitrary ring, then all inverse and direct truncation systems in the derived category ${\operatorname{D}}({\ensuremath{\operatorname{Mod}}}(R))$ of $R$-modules are effective, by Proposition [\[p:ab4-trunc\]](#p:ab4-trunc){reference-type="ref" reference="p:ab4-trunc"}.
:::

::: example
[]{#ex:ringed-topos-effective label="ex:ringed-topos-effective"} If $(X, \mathcal{O})$ is a ringed topos, then the category of $\mathcal{O}$-modules is Grothendieck abelian. In particular, it has arbitrary small products and coproducts and all coproducts are exact; in particular, any direct truncation system in ${\operatorname{D}}(X)$ is effective, by Proposition [\[p:ab4-trunc\]](#p:ab4-trunc){reference-type="ref" reference="p:ab4-trunc"}. Products, however, need not be exact. Nevertheless, certain inverse truncation systems may still be effective, see Proposition [\[p:Dqc-truncation-complete\]](#p:Dqc-truncation-complete){reference-type="ref" reference="p:Dqc-truncation-complete"} below.
:::

The following proposition follows from the proof of [@stacks-project [Tag 0D6M](http://stacks.math.columbia.edu/tag/0D6M)], which basically is an abstract version of a result by Bökstedt--Neeman [@neeman-homotopy-limits Lemma 5.3].

::: proposition
[]{#p:Dqc-truncation-complete label="p:Dqc-truncation-complete"} Let $X$ be an algebraic stack. Then any inverse truncation system in ${\operatorname{D}}(X)$ with terms in ${\operatorname{D}}_{\operatorname{qc}}(X)$ is effective.
:::

::: proof
*Proof.* It is clear that ${\operatorname{D}}(X)$ has all products. Let $(F_n)_{n \in \mathbb{N}}$ be an inverse truncation system in ${\operatorname{D}}(X)$ whose terms $F_n$ lie in ${\operatorname{D}}_{\operatorname{qc}}(X)$.

By the definition of an inverse truncation system, the transition morphism $F_{n+1} \rightarrow F_n$ factors as $F_{n+1} \rightarrow\tau_{\geq -n}F_{n+1} \xrightarrow[{}]{\sim}F_n$, and we obtain a triangle $$\Sigma^{n + 1}\mathop{\mathrm{H}}^{-n-1}(F_{n+1})
    \to F_{n+1}
    \to F_n
    \to \Sigma^{n + 2}\mathop{\mathrm{H}}^{-n-1}(F_{n+1})$$ for each $n \in \mathbb{N}$. Fix $p \in {\mathbb{Z}}$. Since the cohomology sheaves are assumed to be quasi-coherent, the functor $\mathop{\mathrm{H}}^p(U, -)$ vanishes on the first and fourth term of this triangle for all $n \geq -p$ and all affine schemes $U$ which are smooth over $X$. Hence $\mathop{\mathrm{H}}^p(U, F_{n+1}) \rightarrow\mathop{\mathrm{H}}^p(U, F_n)$ is an isomorphism for all $n \geq -p$, i.e., the inverse system $(\mathop{\mathrm{H}}^p(U, F_n))_{n \in {\mathbb{N}}}$ of abelian groups is eventually constant. By Remark [\[rem:1-shift-split-epi\]](#rem:1-shift-split-epi){reference-type="ref" reference="rem:1-shift-split-epi"}, the morphism "identity minus shift" $$1-\sigma \colon \prod_n\mathop{\mathrm{H}}^p(U,F_n)
    \rightarrow\prod_n \mathop{\mathrm{H}}^p(U,F_n)$$ is a (split) epimorphism. Its kernel is $\lim_n \mathop{\mathrm{H}}^p(U,F_n)$.

Note that the functors $\mathop{\mathrm{H}}^q(U, -) = \mathop{\mathrm{H}}^q(\mathsf{R}\Gamma(U, -|_U))$ commute with products since the functors restriction to $U$ and $\mathsf{R}
  \Gamma(U, -)$ are right adjoints and products are exact in the category of abelian groups. Hence applying $\mathop{\mathrm{H}}^p(U, -)$ to the defining triangle of the homotopy limit $\mathop{\mathrm{holim}}_n F_n$ yields an exact sequence $$\dots
    \rightarrow
    \mathop{\mathrm{H}}^p(U, \mathop{\mathrm{holim}}_n F_n) \to 
    \prod_n \mathop{\mathrm{H}}^p(U, F_n) \xrightarrow{1 - \sigma} 
    \prod_n \mathop{\mathrm{H}}^p(U, F_n)
    \rightarrow
    \dots$$ of abelian groups. Since all morphisms $1-\sigma$ are surjective, as observed above, this sequence splits into short exact sequences, and we get isomorphisms $$\mathop{\mathrm{H}}^p(U,\mathop{\mathrm{holim}}_n F_n) 
    \xrightarrow{\sim}
    \lim_n \mathop{\mathrm{H}}^p(U,F_n)
    \xrightarrow{\sim}
    \mathop{\mathrm{H}}^p(U,F_m)$$ for all $m \geq -p$. For an arbitrary object $G$ in ${\operatorname{D}}(X)$, the sheaf $\mathop{\mathrm{H}}^p(G)$ is the sheaf associated to the presheaf $U \mapsto \mathop{\mathrm{H}}^p(U, G)$. Hence the canonical map $\mathop{\mathrm{H}}^p(\mathop{\mathrm{holim}}_n F_n) \to
  \mathop{\mathrm{H}}^p(F_m)$ is an isomorphism for all $m \geq -p$. This means that our system is effective, by Remark [\[rem:effective\]](#rem:effective){reference-type="ref" reference="rem:effective"}. ◻
:::

## Decompositions of unbounded derived categories {#sec:decomp-unbo-deriv}

Now we can state and prove Theorem [\[t:sod-DBA\]](#t:sod-DBA){reference-type="ref" reference="t:sod-DBA"}.

::: remark
[]{#rem:cohomology-split label="rem:cohomology-split"} Let $\mathcal{B}$ be a weak Serre subcategory of an abelian category $\mathcal{A}$ and let $\mathcal{T}$ and $\mathcal{F}$ be abelian subcategories of $\mathcal{B}$ forming a torsion pair $(\mathcal{T}, \mathcal{F})$ in $\mathcal{B}$. Consider an arbitrary triangle $$B' \to B \to B'' \to \Sigma B'$$ in ${\operatorname{D}}_\mathcal{B}(\mathcal{A})$. Then we have $B'$ in ${\operatorname{D}}_\mathcal{T}(\mathcal{A})$ and $B''$ in ${\operatorname{D}}_\mathcal{F}(\mathcal{A})$ if and only if the long exact cohomology sequence splits up into short exact sequences $$0 \to \mathop{\mathrm{H}}^p(B')
  \to \mathop{\mathrm{H}}^p(B)
  \to \mathop{\mathrm{H}}^p(B'')
  \to 0$$ with first term $\mathop{\mathrm{H}}^p(B')$ in $\mathcal{T}$ and third term $\mathop{\mathrm{H}}^p(B'')$ in $\mathcal{F}$, for each $p \in {\mathbb{Z}}$. The "if"-part is trivial, and the "only if"-part is a simple consequence of the fact that $\mathop{\mathrm{Hom}}_\mathcal{B}(F, T)$ vanishes for each object $F$ in $\mathcal{F}$ and $T$ in $\mathcal{T}$, by Proposition [\[p:abelian-torsion-pair\]](#p:abelian-torsion-pair){reference-type="ref" reference="p:abelian-torsion-pair"}.[\[enum:Hom-FT\]](#enum:Hom-FT){reference-type="ref" reference="enum:Hom-FT"}.
:::

::: theorem
[]{#t:sod-DBA label="t:sod-DBA"} Let $\mathcal{B}$ be a weak Serre subcategory of an abelian category $\mathcal{A}$. Let $(\mathcal{T}, \mathcal{F})$ be a torsion pair in $\mathcal{B}$ where both $\mathcal{T}$ and $\mathcal{F}$ are abelian subcategories of $\mathcal{B}$. Assume that $$\mathop{\mathrm{Ext}}_\mathcal{A}^n(T, F)=0$$ for all objects $T \in \mathcal{T}$, $F \in \mathcal{F}$ and all integers $n \in {\mathbb{Z}}$. Assume that ${\operatorname{D}}(\mathcal{A})$ has countable products and coproducts. If every inverse and every direct truncation system in ${\operatorname{D}}(\mathcal{A})$ with terms in ${\operatorname{D}}_\mathcal{B}(\mathcal{A})$ is effective, in the sense of Definition [\[d:truncation-system\]](#d:truncation-system){reference-type="ref" reference="d:truncation-system"}, then $${\operatorname{D}}_{\mathcal{B}}(\mathcal{A})=
    \langle {\operatorname{D}}_{\mathcal{F}}(\mathcal{A}), 
    {\operatorname{D}}_{\mathcal{T}}(\mathcal{A})\rangle$$ is a semi-orthogonal decomposition.
:::

::: proof
*Proof.* **Semi-orthogonality**: We claim that $$\label{eq:Hom-vanishing-unbounded}
  \mathop{\mathrm{Hom}}_{{\operatorname{D}}(\mathcal{A})}(L, R)=0$$ for all objects $L \in {\operatorname{D}}_\mathcal{T}(\mathcal{A})$ and $R \in
{\operatorname{D}}_\mathcal{F}(\mathcal{A})$.

Our proof is a straightforward dévissage argument. Assume first that $L$ is in ${\operatorname{D}}^-_\mathcal{T}(\mathcal{A})$ and that $R$ is in ${\operatorname{D}}^+_\mathcal{F}(\mathcal{A})$. Then any morphism $L \to R$ factors as $L \to \tau_{\geq n} L \to
\tau_{\leq m} R \to R$ for sufficiently small $n$ and sufficiently large $m$. Hence the morphism vanishes by Theorem [\[t:sod-DbBA\]](#t:sod-DbBA){reference-type="ref" reference="t:sod-DbBA"}.

Keep the assumption on $L$ and assume that $R$ is an arbitrary object of ${\operatorname{D}}_\mathcal{F}(\mathcal{A})$. Effectiveness of inverse truncation systems with terms in ${\operatorname{D}}_\mathcal{B}(\mathcal{A})$ and Lemma [\[l:holim-truncations\]](#l:holim-truncations){reference-type="ref" reference="l:holim-truncations"} provide a triangle $$R \rightarrow
  \prod_{n \in {\mathbb{N}}} \tau_{\geq -n} R 
  \rightarrow
  \prod_{n \in {\mathbb{N}}} \tau_{\geq -n} R 
  \rightarrow
  \Sigma R$$ in ${\operatorname{D}}(\mathcal{A})$. The functor $\mathop{\mathrm{Hom}}_{{\operatorname{D}}(\mathcal{A})}(L,-)$ vanishes on the second and third term and their shifts by the universal property of products, boundedness from below of the truncations and the vanishing result already proven. Hence it vanishes also on the first term as desired.

Similarly, effectiveness of direct truncation systems with terms in ${\operatorname{D}}_\mathcal{B}(\mathcal{A})$ and the dual of Lemma [\[l:holim-truncations\]](#l:holim-truncations){reference-type="ref" reference="l:holim-truncations"} give [\[eq:Hom-vanishing-unbounded\]](#eq:Hom-vanishing-unbounded){reference-type="eqref" reference="eq:Hom-vanishing-unbounded"} for arbitrary objects $L$ in ${\operatorname{D}}_\mathcal{T}(\mathcal{A})$ and $R$ in ${\operatorname{D}}_\mathcal{F}(\mathcal{A})$.

**Completeness:** To finish the proof, we need to show that any object $B$ in ${\operatorname{D}}_{\mathcal{B}}(\mathcal{A})$ fits into a triangle $$\label{eq:tria-complete}
T \to B \to F \to \Sigma T$$ with $T$ in ${\operatorname{D}}_{\mathcal{T}}(\mathcal{A})$ and $F$ in ${\operatorname{D}}_{\mathcal{F}}(\mathcal{A})$.

Assume first that $B$ is an object in ${\operatorname{D}}^-_\mathcal{B}(\mathcal{A})$ and consider its associated standard inverse truncation system $(B_n)_{n \in \mathbb{N}}$ where $B_n = \tau_{\geq -n} B$ (see Example [\[ex:ITS\]](#ex:ITS){reference-type="ref" reference="ex:ITS"}). Since the cohomology of each $B_n$ is bounded, the semi-orthogonal decomposition in Theorem [\[t:sod-DbBA\]](#t:sod-DbBA){reference-type="ref" reference="t:sod-DbBA"} provides commutative squares $$\xymatrix{
    T_n \ar[r]\ar[d] & T_{n+1}\ar[d] \\
    B_n \ar[r] & {B_{n+1},} 
  }
  \qquad
  \xymatrix{
    \mathop{\mathrm{H}}^p(T_n) \ar[r]\ar[d] & \mathop{\mathrm{H}}^p(T_{n+1})\ar[d] \\
    \mathop{\mathrm{H}}^p(B_n) \ar[r] & \mathop{\mathrm{H}}^p(B_{n+1}), 
  }$$ where each $T_n$ is the projection of $B_n$ to ${\operatorname{D}}^{\operatorname{b}}_\mathcal{T}(\mathcal{A})$ along this semi-orthogonal decomposition. By Remark [\[rem:cohomology-split\]](#rem:cohomology-split){reference-type="ref" reference="rem:cohomology-split"}, the vertical maps in the right diagram are just the torsion subobjects with respect to the torsion pair $(\mathcal{T}, \mathcal{F})$. The characterization of inverse truncation systems in Remark [\[rem:ITS-alternative\]](#rem:ITS-alternative){reference-type="ref" reference="rem:ITS-alternative"} and the fact that $(B_n)_{n \in \mathbb{N}}$ is such a system make it clear that $(T_n)_{n \in \mathbb{N}}$ is such a system as well. By assumption, it is effective, and hence obtained from its homotopy limit $T$ in ${\operatorname{D}}(\mathcal{A})$ by truncation in a canonical way, see Remark [\[rem:effective\]](#rem:effective){reference-type="ref" reference="rem:effective"}. Without loss of generality we may hence assume that $T_n=\tau_{\geq -n}T$ for all $n \in {\mathbb{N}}$. It is clear that $T \in {\operatorname{D}}^-_\mathcal{T}(\mathcal{A})$. Note that $T$ and $B$ are the homotopy limits of the effective inverse truncation systems $(T_n)_{n \in \mathbb{N}}$ and $(B_n)_{n \in \mathbb{N}}$, by Lemma [\[l:holim-truncations\]](#l:holim-truncations){reference-type="ref" reference="l:holim-truncations"}. Hence the morphism $(T_n)_{n \in \mathbb{N}} \rightarrow(B_n)_{n \in \mathbb{N}}$ of inverse systems induces a morphism $T \rightarrow B$ which makes the following two squares commutative. $$\xymatrix{
    {T} \ar[r]\ar[d] & {T_{n}} \ar[d] \\
    {B} \ar[r] & {B_{n}} 
  }
  \qquad
  \xymatrix{
    {\mathop{\mathrm{H}}^p(T)} \ar[r]\ar[d] & {\mathop{\mathrm{H}}^p(T_{n})}\ar[d] \\
    {\mathop{\mathrm{H}}^p(B)} \ar[r] & {\mathop{\mathrm{H}}^p(B_{n})} 
  }$$ Obviously, the horizontal arrows in the right square are isomorphisms for all $n \geq -p$. Hence $\mathop{\mathrm{H}}^p(T) \to \mathop{\mathrm{H}}^p(B)$ is the torsion subobject with respect to the torsion pair $(\mathcal{T},
\mathcal{F})$, for each $p \in {\mathbb{Z}}$. Complete the morphism $T \to B$ to a triangle as in [\[eq:tria-complete\]](#eq:tria-complete){reference-type="eqref" reference="eq:tria-complete"}. Then the associated long exact sequence on cohomology splits up into short exact sequences with $\mathop{\mathrm{H}}^p(F)$ in $\mathcal{F}$. In particular, the object $F$ is in ${\operatorname{D}}^-_\mathcal{F}(\mathcal{A})$.

This establishes the semi-orthogonal decomposition ${\operatorname{D}}^-_{\mathcal{B}}(\mathcal{A}) =
\langle {\operatorname{D}}^-_{\mathcal{F}}(\mathcal{A}), 
{\operatorname{D}}^-_{\mathcal{T}}(\mathcal{A})\rangle.$ By the dual version of the argument above, starting with an object $B$ in ${\operatorname{D}}_\mathcal{B}(\mathcal{A})$ and using the fact that all direct truncation systems with terms in ${\operatorname{D}}_{\mathcal{B}}(\mathcal{A})$ are effective, we get the desired semi-orthogonal decomposition of ${\operatorname{D}}_\mathcal{B}(\mathcal{A})$. ◻
:::
