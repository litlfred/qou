---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-010-12-artin-schelter-gorenstein-algebras
section_title: "Artin-Schelter Gorenstein algebras"
section_number: 1.2
pages: 4-5
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.971
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec1.2 label="xxsec1.2"}

While our main interest is in Hopf algebras of various sorts, some of our results apply in fact to any algebra possessing a natural augmentation $\epsilon$ to the base field $k$, such as, for example, the connected $\mathbb{N}$-graded $k$-algebras, where $\epsilon$ is the graded map $A\to
A/A_{\geq 1}(=k)$. Accordingly, we give the following definitions in this more general context.

::: definition
Let $A$ be a noetherian algebra.

1.  We shall say $A$ has *finite injective dimension* if the injective dimensions of $_AA$ and $A_A$, $\mathop{\mathrm{injdim}}_AA$ and $\mathop{\mathrm{injdim}}A_A$, are both finite. In this case these integers are equal by [@Za], and we write $d$ for the common value. We say $A$ is *regular* if it has finite global dimension, $\mathop{\mathrm{gldim}}_AA < \infty$. Right global dimension always equals left global dimension [@We Exercise 4.1.1]; and, when finite, the global dimension equals the injective dimension.

2.  Suppose now that $A$ has a fixed augmentation $\epsilon: A\to k$. Let $k$ also denote the trivial $A$-module $A/\ker \epsilon$. Then $A$ is *Artin-Schelter Gorenstein*, which we usually abbreviate to *AS-Gorenstein*, if

    1.  $\mathop{\mathrm{injdim}}{_AA}=d<\infty$,

    2.  $\dim_k \mathop{\mathrm{Ext}}^d_A({_Ak},{_AA})=1$ and $\mathop{\mathrm{Ext}}^i_A({_Ak},{_AA})=0$ for all $i\neq d$,

    3.  the right $A$-module versions of (AS1,AS2) hold.

3.  If, further, $\mathop{\mathrm{gldim}}A=d$, then $A$ is called *Artin-Schelter regular*, usually shortened to *AS-regular*.
:::

We recall that the following question, first posed in [@BG1 1.15], and repeated in [@Br1], remains open:

::: question
Is every noetherian affine Hopf algebra AS-Gorenstein?
:::

We shall note in Section 6 many of the classes of algebra for which a positive answer to this question is known.

::: remark
The Artin-Schelter Gorenstein condition (AS2) given in the above definition is slightly different from the definition given in [@BG1 1.14]. When $A$ is a Hopf algebra, the two definitions are equivalent, as we record in Lemma [\[xxsec3.2\]](#xxsec3.2){reference-type="ref" reference="xxsec3.2"}.
:::
