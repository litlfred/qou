---
doc_id: arxiv-1801.04409v4
doc_title: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES"
section_id: sec-008-33-compatibility-of-negligible-morphisms-with-su
section_title: "Compatibility of negligible morphisms with surjective tensor functors"
section_number: 3.3
pages: 14-15
source_pdf: 1801.04409v4.pdf
source_sha256: db61d011e3775aca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.978
doc_brief: "ON SEMISIMPLIFICATION OF TENSOR CATEGORIES — We develop the theory of semisimpliﬁcations of ten- sor categories deﬁned by Barrett and Westbury."
---
Let $\mathcal{C},\mathcal{D}$ be finite spherical tensor categories ([@EGNO], Section 6), and $F: \mathcal{C}\to \mathcal{D}$ a surjective tensor functor ([@EGNO], Subsection 6.3). Let $I: \mathcal{D}\to \mathcal{C}$ be the right adjoint of $F$. Note that $I$ is exact since $F$ maps projectives to projectives, ([@EGNO], Theorem 6.1.16).

::: definition
The *index* of $F$ is $d:=\dim I(\bold 1)$.
:::

::: definition
Let us say that $I$ is *dimension-scaling* if $\dim I(V)=d\dim V$ for all $V\in \mathcal{D}$.
:::

::: proposition
[]{#negli label="negli"} If $F$ has a nonzero index and $I$ is dimension-scaling then

\(i\) $\dim F(Y)=\dim Y$ for all $Y\in \mathcal{C}$;

\(ii\) for any negligible morphism $f$ in $\mathcal{C}$, the morphism $F(f)$ is negligible in $\mathcal{D}$.
:::

::: proof
*Proof.* We have a functorial isomorphism $\varepsilon_Y: I(F(Y))\to I(\bold 1)\otimes Y$. Indeed, $$\mathrm{Hom}(X,I(F(Y)))=\mathrm{Hom}(F(X),F(Y))=\mathrm{Hom}(F(X)\otimes F(Y)^*,\bold 1)=$$ $$\mathrm{Hom}(F(X\otimes Y^*),\bold 1)=
\mathrm{Hom}(X\otimes Y^*,I(\bold 1))=
\mathrm{Hom}(X,I(\bold 1)\otimes Y).$$ Since $I$ is dimension-scaling, we have $$d\dim F(Y)=\dim I(F(Y))=\dim (I(\bold 1)\otimes Y)=d \dim Y.$$ Since $d\ne 0$, this implies (i).

Now let us prove (ii). For this, note that if $f: X\to Y$ is a morphism in $\mathcal{C}$ then $\varepsilon_Y\circ I(F(f))\circ \varepsilon_X^{-1}={\rm Id}_{I(\bold 1)}\otimes f$. Hence the morphism $I(F(f))$ is negligible.

::: lemma
[]{#scaletrace label="scaletrace"} If $h: V\to V$ is a morphism in $\mathcal{D}$ then one has $\text{Tr}(I(h))=d\text{Tr}(h)$.
:::

::: proof
*Proof.* By decomposing $V$ into generalized eigenobjects of $h$, we may assume that $h$ has a single eigenvalue $\lambda$. Then $h=\lambda{\rm Id}+h_0$, where $h_0$ is nilpotent, so $I(h)=\lambda {\rm Id}+I(h_0)$. Since $I(h_0)$ is nilpotent, the desired statement reduces to the identity $\dim I(V)=d\dim V$ for all $V\in \mathcal{D}$, which holds since $I$ is dimension-scaling. ◻
:::

Now let $g: F(Y)\to F(X)$ be a morphism. Then by Lemma [\[scaletrace\]](#scaletrace){reference-type="ref" reference="scaletrace"}, $$d\text{Tr}(F(f)\circ g)=\text{Tr}(I(F(f)\circ g))=\text{Tr}(I(F(f))\circ I(g)).$$ But this is zero, since $I(F(f))$ is negligible. Since $d\ne 0$, this implies that $\text{Tr}(F(f)\circ g)=0$, i.e., $F(f)$ is negligible, yielding (ii). ◻
:::

Proposition [\[negli\]](#negli){reference-type="ref" reference="negli"} immediately implies

::: corollary
[]{#desc label="desc"} If $F$ has a nonzero index and $I$ is dimension-scaling then $F$ descends to a tensor functor $\overline{F}: \overline{\mathcal{C}}\to \overline{\mathcal{D}}$.
:::

Now let $H$ be an involutive finite dimensional Hopf algebra over any algebraically closed field $\mathbf{k}$ (i.e., $S^2=\text{Id}$, where $S$ is the antipode of $H$), and $K$ be a Hopf subalgebra in $H$; for example, $H$ is cocommutative (e.g., a group algebra). Then $\mathcal{C}=\mathop{\mathrm{Rep}}\nolimits H$ and $\mathcal{D}=\mathop{\mathrm{Rep}}\nolimits K$ are finite spherical tensor categories, where dimensions are the usual dimensions (projected to $\mathbf{k}$). Restriction from $H$ to $K$ defines a surjective tensor functor $F: \mathcal{C}\to \mathcal{D}$. Let $I: \mathop{\mathrm{Rep}}\nolimits(K)\to \mathop{\mathrm{Rep}}\nolimits(H)$ be the right adjoint to this functor, i.e., the induction functor, $I(V)=\mathrm{Hom}_K(H,V)$.

Recall that by the Nichols-Zoeller theorem [@NZ], $H$ is a free $K$-module, of some rank $d$.

::: corollary
[]{#invo label="invo"} Assume that $d\ne 0$ in $\mathbf{k}$. Then any negligible morphism $f: X\to Y$ of $H$-modules is also negligible as a morphism of $K$-modules. Thus, $F$ defines a tensor functor: $\overline{\mathop{\mathrm{Rep}}\nolimits H}\to \overline{\mathop{\mathrm{Rep}}\nolimits K}$.
:::

::: proof
*Proof.* We have $\dim I(V)=d\dim V$, i.e., $I$ is dimension-scaling. Thus, the result follows from Proposition [\[negli\]](#negli){reference-type="ref" reference="negli"}. ◻
:::
