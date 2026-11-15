---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-041-13-the-fundamental-isomorphism
section_title: "The fundamental isomorphism"
section_number: 13
pages: 62-65
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.936
latex_coverage_ratio: 0.929
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:fundamentalisomorphism label="section:fundamentalisomorphism"}

[]{#not48 label="not48"} We write $\Lambda_I := I_n + {\text{Mat}}_n({\mathscr{A}}_0)$ for the subsheaf of groups of ${\text{GL}}_n({\mathscr{A}})$ made up of matrices infinitely tangent to the identity and, if $G$ is an algebraic subgroup of ${\text{GL}}_n({\mathbf C})$, we put $\Lambda_I^G := \Lambda_I \cap G({\mathscr{A}})$. In particular $\Lambda_I^{{\mathfrak{G}}}$ is a sheaf of triangular matrices of the form [\[eqn:isoplat\]](#eqn:isoplat){reference-type="eqref" reference="eqn:isoplat"} with all the $F_{i,j}$ infinitely flat.\
For a $q$-difference module $M = ({{\mathbf C}(\{z\})}^n,\Phi_A)$ (section [\[subsection:generalitiesdiffmods\]](#subsection:generalitiesdiffmods){reference-type="ref" reference="subsection:generalitiesdiffmods"}), we consider the set of *automorphisms of $M$ infinitely tangent to the identity*: this is the subsheaf $\Lambda_I(M)$ of $\Lambda_I$ whose sections satisfy the equality: $F[A] = A$ (recall that by definition $F[A] = (\sigma_qF) A F^{-1}$); this is also called the *Stokes sheaf* of the module $M$.\
If the matrix $A$ has the form [\[eqn:formestandardtriangulaire\]](#eqn:formestandardtriangulaire){reference-type="eqref" reference="eqn:formestandardtriangulaire"} (see paragraph [\[subsection:matricialdescriptionofF(P1,\...,Pk)\]](#subsection:matricialdescriptionofF(P1,...,Pk)){reference-type="ref" reference="subsection:matricialdescriptionofF(P1,...,Pk)"}) then $\Lambda_I(M)$ is a subsheaf of $\Lambda_I^{{\mathfrak{G}}}$. Up to an analytic gauge transformation, we can assume that we are in this case. As a consequence, $\Lambda_I(M)$ is a sheaf of *unipotent* (and even triangular) groups.

## Study of $H^1({\mathbf{E}_{q}};\Lambda_I)$ {#subsection:glue}

[]{#not49 label="not49"}

We choose $\tau \in {\mathbf C}$, $\Im(\tau) > 0$, such that $q = e^{-2 {\text{i}}\pi\tau}$. Since $(1,\tau)$ is a basis of the ${\mathbf R}$-vector space ${\mathbf C}$, the group morphism: $$p_0: (u,v) \mapsto e^{2 {\text{i}}\pi (u+v\tau)}$$ from ${\mathbf R}^2$ to ${\mathbf C}^*$ is onto with kernel ${\mathbf Z}\times \{0\}$, and the preimage of $q^{{\mathbf Z}}$ is $$\label{not50}
p_0^{-1}(q^{{\mathbf Z}}) = {\mathbf Z}\times {\mathbf Z}.$$ Therefore, the composition $p \circ p_0$ of $p_0$ with the natural projection $p: {\mathbf C}^* \rightarrow {\mathbf{E}_{q}}= {\mathbf C}^{*}/q^{{\mathbf Z}}$ is a group epimorphism with discrete kernel ${\mathbf Z}^2$; it is clearly a local diffeomorphism.

::: rema
The morphism $p_0$ induces an isomorphism between ${\mathbf R}^2/{\mathbf Z}^2$ and ${\mathbf{E}_{q}}= {\mathbf C}^{*}/q^{{\mathbf Z}}$. Through this isomorphism, the natural splitting of ${\mathbf R}^2/{\mathbf Z}^2$ is carried to the splitting: $${\mathbf C}^* = {\mathbf{U}}\times q^{{\mathbf R}},$$ where ${\mathbf{U}}$ denotes the unit circle in ${\mathbf C}^*$ and, for $v \in {\mathbf R}$, we denote $q^v = e^{-2 {\text{i}}\pi\tau v}$
:::

We will call *open parallelogram* of ${\mathbf{E}_{q}}$ the image by the map $p \circ p_0: {\mathbf R}^2 \rightarrow {\mathbf{E}_{q}}$ of an open parallelogram $\left]u_1,u_2\right[ \times \left]v_1,v_2\right[ \subset {\mathbf R}^2$ where $u_2 - u_1 \leq 1, v_2 - v_1 \leq 1$. This is the same as the image by $x \mapsto e^{2 {\text{i}}\pi x}$ of: $$\{u + v\tau \in {\mathbf C}~ | ~u_1 < u < u_2, v_1 < v< v_2\},$$ We will call *closed parallelogram* of ${\mathbf{E}_{q}}$ the closure of an open parallelogram such that $u_2 - u_1 < 1,v_2 - v_1 < 1$. We will say that a parallelogram is *small* if $u_2 - u_1 < 1/4$ and $v_2 - v_1 < 1/4$.\
For every open covering ${\mathfrak{V}}$ of ${\mathbf{E}_{q}}$, there exists a finite open covering ${\mathfrak{U}}= (U_i)_{i\in I}$, finer than ${\mathfrak{V}}$, such that:

1.  the $U_i$ are open parallelograms,

2.  the open sets $U_i$ are four by four disjoint.

We will call *good* such a covering. There is a similar definition for closed coverings. It is then clear that:

-   Every element of $H^j({\mathbf{E}_{q}};{\text{GL}}_n({\mathscr{A}})),j=0,1$ can be represented by an element of $H^j({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}}))$, where ${\mathfrak{U}}$ is a good covering.

-   The natural map $H^j({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}})) \rightarrow H^j({\mathbf{E}_{q}};{\text{GL}}_n({\mathscr{A}}))$ is always injective.

[]{#not51 label="not51"} Let ${\mathfrak{U}}$ be a good open covering of ${\mathbf{E}_{q}}$; we denote by ${\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}}))$ the subspace of the space of $0$-cochains $(g_i) \in C^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}}))$ whose coboundary $(g_{ij} := g_i g_j^{-1})$ belongs to $C^1({\mathfrak{U}};\Lambda_I)$. Thus, a cochain $C^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}}))$ is any family $(g_i)$ such that $g_i \in {\mathscr{A}}(U_i)$, and it belongs to ${\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}}))$ if, and only if, the $g_i$ ($i\in I$) admit the same asymptotic expansion $\hat g \in {\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)$. It is also equivalent to say that the natural image of the cochain $(g_i)$ in $C^0({\mathfrak{U}}; {\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr))$ is a cocycle.

::: lemm
-   Let ${\mathfrak{U}}$ be a good open covering of ${\mathbf{E}_{q}}$. The coboundary map $\partial$ induces an injection on the double quotient: []{#not52 label="not52"} $$C^0({\mathfrak{U}};\Lambda_I) \backslash
    {\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}}))
    /H^0\bigl({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}})\bigr)
    \rightarrow H^1({\mathfrak{U}};\Lambda_I).$$

-   We have a canonical injection: $${\lim_{\longrightarrow}}_{{\mathfrak{U}}}~C^0({\mathfrak{U}};\Lambda_I)
    \backslash {\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}}))
    /{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)
    \rightarrow H^1({\mathbf{E}_{q}};\Lambda_I),$$ where the direct limit is indexed by the good coverings.
:::

::: proof
*Proof.* We have two natural maps: $${\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}})) \rightarrow Z^1({\mathfrak{U}};\Lambda_I),$$ which sends the family $(g_i)$ to the family $(g_{ij})$ and $${\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}})) \rightarrow {\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr),$$ which sends the family $(g_i)$ to $\hat g \in {\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)$, the common asymptotic expansion of all the $g_i$.

Two cochains $(g_i),(g'_i)\in {\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}}))$ define the same element of $H^1({\mathfrak{U}};\Lambda_I)$ if and only if: $$g'_i{g'}_j^{-1}=h_ig_ig_j^{-1}h_j^{-1}, \ \text{with} \
(h_i)\in C^0({\mathfrak{U}};\Lambda_I).$$ This is equivalent to ${g'}_j^{-1} h_j g_j = {g'}_i^{-1} h_i g_i$, which thus defines an element $f \in H^0\bigl({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}})\bigr)$ and we have $g' = h g f^{-1}$. ◻
:::

::: prop
For every good open covering ${\mathfrak{U}}$ of ${\mathbf{E}_{q}}$ we have a natural isomorphism: $$C^0({\mathfrak{U}}:\Lambda_I)
\backslash {\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}}))
/H^0\bigl({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}})\bigr)
\rightarrow
{\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr).$$ (Note that the double quotient on the left hand side is the same as the double quotient on the left hand side of assertion (i) in the lemma above.)
:::

::: proof
*Proof.* Let ${\mathfrak{U}}$ be a good open covering of ${\mathbf{E}_{q}}$. Let $\hat g \in {\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)$. Using the $q$-analog of Borel-Ritt (theorem [\[theo:BorelRittfaible\]](#theo:BorelRittfaible){reference-type="ref" reference="theo:BorelRittfaible"}), we can represent it by an element $g_i$ on each open set $U_i$ such that $g_i$ admits $\hat g$ as asymptotic expansion, therefore the natural map: $${\tilde{C}}^0({\mathfrak{U}};{\text{GL}}_n({\mathscr{A}})) \rightarrow {\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)$$ is onto. The proposition follows. ◻
:::

::: coro
For every good open covering ${\mathfrak{U}}$ of ${\mathbf{E}_{q}}$, we have natural injections: $${\text{GL}}_n\bigl({{\mathbf C}[[z]]}\bigr)/{\text{GL}}_n\bigl({{\mathbf C}\{z\}}\bigr)
\rightarrow
H^1({\mathfrak{U}};\Lambda_I) \rightarrow H^1({\mathbf{E}_{q}};\Lambda_I).$$
:::

We will see later (subsection [\[subsection:theformaltrivialisation\]](#subsection:theformaltrivialisation){reference-type="ref" reference="subsection:theformaltrivialisation"}) that these maps are bijections.
