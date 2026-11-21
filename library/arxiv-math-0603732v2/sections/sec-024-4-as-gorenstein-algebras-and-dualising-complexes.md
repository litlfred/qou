---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-024-4-as-gorenstein-algebras-and-dualising-complexes
section_title: "AS-Gorenstein algebras and dualising complexes"
section_number: 4
pages: 13-13
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.649
latex_coverage_ratio: 0.969
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
[]{#xxsec4 label="xxsec4"}

## Dualising Complexes {#xxsec4.1}

The noncommutative version of the dualising complex was introduced by Yekutieli in [@Ye1], and has now become one of the standard homological tools of noncommutative ring theory. We review in the next four paragraphs the small amount of this theory which we shall need to draw on. Most of the details, including some of the necessary facts about derived categories, can be found in [@Ye1; @VdB2; @YZ]. Let $A$ be an algebra and let $\mathop{\mathrm{{\sf D}}}^{\rm
b}(A$-$\mathop{\mathrm{{\sf Mod}}})$ denote the bounded derived category of left $A$-modules. A complex $X$ of left $A$-modules is called *homologically finite* if $\bigoplus_i H^i(X)$ is a finitely generated $A$-module.

::: definition
Let $A$ be a noetherian algebra. A complex $R\in \mathop{\mathrm{{\sf D}}}^{\rm
b}(A^e$-$\mathop{\mathrm{{\sf Mod}}})$ is called a *dualising complex* over $A$ if it satisfies the following conditions:

1.  $R$ has finite injective dimension over $A$ and over $A^{\sf
    op}$ respectively.

2.  $R$ is homologically finite over $A$ and over $A^{\sf op}$ respectively.

3.  The canonical morphisms $A\to \mathop{\mathrm{RHom}}_A(R,R)$ and $A\to \mathop{\mathrm{RHom}}_{A^{\sf op}}(R,R)$ are isomorphisms in $\mathop{\mathrm{{\sf D}}}(A^e$-$\mathop{\mathrm{{\sf Mod}}})$.

If $A$ is $\mathbb Z$-graded, a graded dualising complex is defined similarly.
:::

## Rigid dualising complexes {#xxsec4.2}

Let $R$ be a complex of $A^e$-modules, viewed as a complex of $A$-bimodules. Let $R^{\sf op}$ denote the "opposite complex" of $R$ which is defined as follows: as a complex of $k$-modules $R^{\sf op}= R,$ and the left and right $A^{\sf op}$-module actions on $R^{\sf op}$ are given by $$a \cdot r \cdot b \quad := \quad bra$$ for all $a, b\in A^{\sf op}$ and $r\in R^{\sf op}(=R)$. If $R\in \mathop{\mathrm{{\sf D}}}(A^e$-$\mathop{\mathrm{{\sf Mod}}})$ then $R^{\sf op}\in \mathop{\mathrm{{\sf D}}}^{\rm
b}((A^{\sf op})^e$-$\mathop{\mathrm{{\sf Mod}}})$. The flip map $$\tau : (A^{\sf op})^e = A^{\sf op} \otimes A \longrightarrow
A \otimes A^{\sf op} = A^e$$ is an algebra isomorphism, so $(A^{\sf op})^e$ is isomorphic to $A^e$. Hence there is a natural isomorphism $\mathop{\mathrm{{\sf D}}}^{\rm b}(A^e$-$\mathop{\mathrm{{\sf Mod}}}) \cong
\mathop{\mathrm{{\sf D}}}^{\rm b}((A^{\sf op})^e$-$\mathop{\mathrm{{\sf Mod}}})$.

An unfortunate failing of dualising complexes as defined in ([0.1](#xxsec4.1){reference-type="ref" reference="xxsec4.1"}) is their lack of uniqueness. To remedy this defect Van den Bergh [@VdB2] introduced the idea of a rigid complex:

::: definition
[@VdB2] Let $A$ be a noetherian algebra. A dualising complex $R$ over $A$ is called *rigid* if there is an isomorphism $$R \cong \mathop{\mathrm{RHom}}_{A^e}(A, R \otimes R^{\sf op})$$ in $\mathop{\mathrm{{\sf D}}}(A^e$-$\mathop{\mathrm{{\sf Mod}}})$. Here the left $A^e$-module structure of $R\otimes R^{\sf op}$ comes from the left $A$-module structure of $R$ and the left $A^{\sf op}$-module structure of $R^{\sf op}$.
:::

Earlier, Yekutieli [@Ye1] defined the concept of a *balanced* dualising complex over a graded algebra $A$; a balanced dualising complex over a connected graded algebra is rigid, [@VdB2 Proposition 8.2(2)]. If the algebra $A$ has a rigid dualising complex $R$, then $R$ is unique up to isomorphism, [@VdB2 Proposition 8.2].
