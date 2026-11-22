---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-011-27-ribbon-hopf-algebras
section_title: "Ribbon Hopf algebras"
section_number: 2.7
pages: 13-14
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.913
latex_coverage_ratio: 0.934
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect examples."
---
[]{#subsec:ribbon label="subsec:ribbon"} This is a distinguished class of spherical Hopf algebras. Let $(H, {\mathcal R})$ be a quasi-triangular Hopf algebra [@Dr1]. We denote the universal matrix as ${\mathcal R}= {\mathcal R}^{\left( 1 \right)} {\otimes}{\mathcal R}^{\left( 2 \right)}$. The *Drinfeld element* is $$\label{eqn:drinfeldelement}
{\mathbf u}= {\mathcal S}({\mathcal R}^{\left( 2 \right)}){\mathcal R}^{\left( 1 \right)}.$$ Let $Q = {\mathcal R}_{21}{\mathcal R}$. The Drinfeld element is invertible and satisfies $$\begin{aligned}
\label{eq:drinfeld-element1}
\Delta({\mathbf u}) = Q^{-1}({\mathbf u}{\otimes}{\mathbf u}) &= ({\mathbf u}{\otimes}{\mathbf u}) Q^{-1},  & {\mathbf u}^{-1} &=  {\mathcal R}^{\left( 2 \right)}{\mathcal S}^2({\mathcal R}^{\left( 1 \right)}),
\\\label{eq:drinfeld-element2}
g :={\mathbf u}{\mathcal S}({\mathbf u})^{-1} &= {\mathcal S}({\mathbf u})^{-1}{\mathbf u}\in G(H), & {\mathbf u}{\mathcal S}({\mathbf u}) &\in Z(H),
\\\label{eq:drinfeld-element3}
{\mathcal S}^2(h) &= {\mathbf u}h{\mathbf u}^{-1},  & {\mathcal S}^4(h) &= g h g^{-1},
\end{aligned}$$ for any $h\in H$.

::: definition
[]{#defi:ribbon label="defi:ribbon"}[@RT-cmp] A quasi-triangular Hopf algebra $(H, {\mathcal R})$ is *ribbon* if there exists ${\mathbf v}\in Z(H)$, called the *ribbon element*, such that $$\begin{aligned}
\label{eq:ribbon-element1}
{\mathbf v}^2 &= {\mathbf u}{\mathcal S}({\mathbf u}),  & {\mathcal S}({\mathbf v}) &= {\mathbf v}, & \Delta({\mathbf v}) &= Q^{-1}({\mathbf v}{\otimes}{\mathbf v}).
\end{aligned}$$ The ribbon element is not unique but it is determined up to multiplication by an element in $\{g\in G(H) \cap Z(H): g^2 = 1\}$.
:::

Let $H$ be a ribbon Hopf algebra. It follows easily that $\omega = {\mathbf u}{\mathbf v}^{-1}\in G(H)$ and ${\mathcal S}^2(h) = \omega h \omega^{-1}$ for all $h\in H$; that is, $\omega$ is a pivot. Actually, $H$ is spherical [@BaW-adv Example 3.2]. In fact, the concept of *quantum trace* is defined in any ribbon category using the braiding, see for example [@ka XIV.4.1]. By [@ka XIV.6.4], the *quantum trace* of $\operatorname{Rep}H$ coincides with $\operatorname{tr}_L$, cf. [\[eq:tr-sph-Ha\]](#eq:tr-sph-Ha){reference-type="eqref" reference="eq:tr-sph-Ha"}. Moreover, [@ka XIV.4.2 (c)] asserts that $\operatorname{tr}_L = \operatorname{tr}_R$.

There are quasi-triangular Hopf algebras that are not ribbon, but the failure is not difficult to remedy by adjoining a group-like element [@RT-cmp Theorem 3.4]. Namely, given a quasi-triangular Hopf algebra $(H, {\mathcal R})$, let $\widetilde H= H \oplus H{\mathbf v}$, where ${\mathbf v}$ is a formal element not in $H$. Then $\widetilde H$ is a Hopf algebra with product, coproduct, antipode and counit defined for $x,x',y,y' \in H$ by $$\begin{aligned}
\label{eq:ribbon-ext-producto}
(x + y{\mathbf v}) \cdot (x' + y' {\mathbf v}) &= (xx' + yy' {\mathbf u}{\mathcal S}({\mathbf u})) + (xy' + yx') {\mathbf v},
\\\label{eq:ribbon-ext-coproducto}
\Delta(x + y{\mathbf v}) &= \Delta(x) + \Delta(y)Q^{-1}({\mathbf v}{\otimes}{\mathbf v}),
\\\label{eq:ribbon-ext-antipoda}
{\mathcal S}(x + y{\mathbf v}) &= {\mathcal S}(x) + {\mathcal S}(y){\mathbf v}, \qquad  \varepsilon (x + y{\mathbf v}) = \varepsilon (x) + \varepsilon (y).
\end{aligned}$$ Clearly, $H$ becomes a Hopf subalgebra of $\widetilde H$; it can be shown then that ${\mathcal R}$ is a universal $R$-matrix for $\widetilde H$ and that ${\mathbf v}$ is a ribbon element for $(\widetilde H,{\mathcal R})$. See [@RT-cmp Theorem 3.4]. We shall say that $\widetilde H$ is the *ribbon extension* of $(H, {\mathcal R})$.

::: Rem
[]{#rem:ribbon-ext label="rem:ribbon-ext"} (Y. Sommerhäuser, private communication). The ribbon extension fits into an exact sequence of Hopf algebras $H \hookrightarrow\widetilde H\twoheadrightarrow \Bbbk[{\mathbb Z}/2]$, which is cleft. Namely, let $\xi$ be the generator of ${\mathbb Z}/2$ and define $$\begin{aligned}
\xi \rightharpoonup x &= {\mathcal S}^2(x), & x&\in H,& \sigma(\xi^i {\otimes}\xi^j)&= g^{ij},& i,j&\in \{0,1\}.
\end{aligned}$$ Then the crossed product defined by this action and cocycle together with the tensor product of coalgebras is a Hopf algebra $H \#_{\sigma}\Bbbk[{\mathbb Z}/2]$, see for instance [@AD]. Now the map $\psi: H \#_{\sigma}\Bbbk[{\mathbb Z}/2] \to \widetilde H$, $\psi(x\# \xi^i) = x ({\mathcal S}(u^{-1}){\mathbf v})^i$, is an isomorphism of Hopf algebras.
:::

In conclusion, any finite-dimensional Hopf algebra $H$ gives rise to a ribbon Hopf algebra, namely the ribbon extension of its Drinfeld double: $$\xymatrix{H \ar@{~>}[0,1]  & D(H) \ar@{~>}[0,1] & \widetilde{D(H)}.}$$

::: Rem
[]{#rem:ribbon-double label="rem:ribbon-double"} A natural question is whether the Drinfeld double itself is ribbon; this was addressed in [@KR], where the following results were obtained. Let $H$ be a finite-dimensional Hopf algebra, $g\in G(H)$ and $\alpha\in G(H^*)$ be the distinguished group-likes[^1]. The celebrated Radford's formula for the fourth power of the antipode [@radford-ajm] states that $$\begin{aligned}
\label{eq:radford-S4}
{\mathcal S}^4(h) &= g (\alpha \rightharpoonup h\leftharpoonup \alpha^{-1})g^{-1},  & h &\in H.
\end{aligned}$$ Here $\rightharpoonup$, $\leftharpoonup$ are the transposes of the regular actions.

1.  [@KR Theorem 2] Suppose that $(H, {\mathcal R})$ is quasi-triangular and that $G(H)$ has odd order. Then $(H, {\mathcal R})$ admits a (necessarily unique) ribbon element if and only if ${\mathcal S}^2$ has odd order.

2.  [@KR Theorem 3] $(D(H), {\mathcal R})$ admits a ribbon element if and only if there exist $\ell\in G(H)$ and $\beta\in G(H^*)$ such that $$\begin{aligned}
    \label{eq:kauffman-radford-S2}
    \ell^2 &= g, & \beta^2 &= \alpha, & {\mathcal S}^2(h) &= \ell (\beta \rightharpoonup h\leftharpoonup \beta^{-1})\ell^{-1},  & h &\in H.
    \end{aligned}$$
:::

[^1]: These control the passage from left to right integrals.
