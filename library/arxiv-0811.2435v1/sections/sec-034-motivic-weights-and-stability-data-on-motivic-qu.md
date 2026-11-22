---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-034-motivic-weights-and-stability-data-on-motivic-qu
section_title: "Motivic weights and stability data on motivic quantum tori"
section_number: null
pages: 92-95
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.977
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
Let $\CC$ be a $3$-dimensional ind-constructible Calabi-Yau category over a field of characteristic zero (see Section 3.3). In this section we are going to define motivic Donaldson-Thomas invariants associated with a constructible stability condition and an orientation data on $\CC$.

*Step 1*.

Let us define the ring $${D}^{\mu}={\cal M}^{\mu}(Spec(\k))[{\mathbb L}^{-1}, {\mathbb L}^{1/2},  ([GL(n)]^{-1})_{n\geqslant 1}]\,\,,$$ where the ring ${\cal M}^{\mu}(Spec(\k))$ was defined in 4.3, and ${\mathbb L}=[{\bf A}^1_{\k}]$ is the motive of the affine line. The element ${\mathbb L}^{1/2}$ is a formal symbol satisfying the equation $({\mathbb L}^{1/2})^2={\mathbb L}$. Instead of inverting motives $$[GL(n)]=({\mathbb L}^n-1)({\mathbb L}^n-{\mathbb L})\dots({\mathbb L}^n-{\mathbb L}^{n-1})$$ of all general linear groups we can invert motives of all projective spaces $$[{\bf P}^n]={{\mathbb L}^{n+1}-1\over {\mathbb L}-1}\,\,.$$ We also will consider the ring $\overline{D^{\mu}}$ of equivalence classes of functions from $D^{\mu}$ by the equivalence relation defined in Section 4.5. The ring $\overline{D^{\mu}}$ will play the role of the universal coefficient ring where motivic Donaldson-Thomas invariants take value.

*Step 2*.

We define an algebra $\overline{{\cal M}^{\mu}}(Ob(\CC))$ associated with $\CC$ which will contain certain canonical element called the motivic weight. First, we define $${\cal M}^{\mu}(Ob(\CC)):=\prod_i{\cal M}^{GL(N_i),\mu}(Y_i)[{\mathbb L}^{-1}, {\mathbb L}^{1/2}]\,\,,$$ where $(Y_i, GL(N_i))_{i\in I}$ is a decomposition of the stack of objects of $\CC$ as at the end of 3.2. Algebra $\overline{{\cal M}^{\mu}}(Ob(\CC))$ is obtained from it by passing to the equivalence classes in the sense of Section 4.5.

For any $GL(N_i)$-invariant constructible set $Z\subset Y_i$ for some $i\in I$, we have a ${\cal M}^\mu(Spec(\k))[{\mathbb L}^{-1}, {\mathbb L}^{1/2}]$-linear map $$\int_Z: {\cal M}^{\mu}(Ob(\CC))\to {D}^{\mu}$$ which is the $\mu$-equivariant version of integral over stack $(Z,GL(N_i))$ (see 4.2) of the restriction to $Z$. Explicitly, if $f_{|Y_i}$ is represented by a $\mu\times GL(N_i)$-equivariant map $X\to Y_i$ then $$\int_Z f=[X\times_{Y_i} Z]/[GL(N_i)] \in D^\mu$$ where $[X\times_{Y_i} Z]$ is interpreted a constructible set with $\mu$-action. By additivity we extend the integral to the case when $Z$ is a finite union of $GL(N_i)$-invariant constructible set $Z_i\subset Y_i$ for different $i\in I$.

*Step 3*.

Now we are going to define the motivic weight. Recall that for any $E\in Ob(\CC)(\kk)$ we have defined the potential $W_E^{min}$ which is a formal power series in $\alpha\in \op{Ext}^1(E,E)$ which starts with cubic terms. We denote by $$MF(E):=MF_0(W_E^{min})$$ the motivic Milnor fiber of $W_E^{min}$ at $0\in \op{Ext}^1(E,E)$. Then the assignment $E\mapsto MF(E)$ can be interpreted as the value of some function $MF\in {\cal M}^{\mu}(Ob(\CC))$.

Let us choose an orientation data $\sqrt{\cal D}$ for $\CC$. Recall that in Section 5.2 we defined the element $h\in J_2(\CC)$ represented by the equivariant super line bundle $\sqrt{\cal D}\otimes {\cal D}_{\le 1}^{-1}$ with trivialized tensor square. For a representative of $h$ given by a pair $(V,Q)$ we have $\overline{I}(h)=(1-MF_0(Q)){\mathbb L}^{-{1\over{2}}\op{rk} Q}$. Let us choose such a representative.

::: defn
The motivic weight $w\in {\cal M}^{\mu}(Ob(\CC))$ is the function defined on objects by the formula $$w(E)={\mathbb L}^{{1\over{2}}\sum_{i\le 1}(-1)^i \dim \op{Ext}^i(E,E)}(1-MF(E))(1-MF_0(Q_E)){\mathbb L}^{{-{1\over{2}}\op{rk}Q_E}}\,\,.$$
:::

The image $\overline{w}\in \overline{{\cal M}^{\mu}}(Ob(\CC))$ does not depend on the choice of a representative of $h$ and is equal to $$\overline{w}(E)={\mathbb L}^{{1\over{2}}\sum_{i\le 1}(-1)^i \dim \op{Ext}^i(E,E)}(1-MF(E))\overline{I}(h(E))\,\,,$$ where $h(E)$ is the value of the obstruction $h$ at the point $E$.

*Step 4*.

Let us now fix the following data:

-   a triple $(\Gamma, \langle\bullet,\bullet \rangle, Q)$ consisting of a free abelian group $\Gamma$ of finite rank endowed with a skew-symmetric bilinear form $\langle\bullet,\bullet \rangle: \Gamma\otimes \Gamma\to \Z$, and a quadratic form $Q$ on $\Gamma_{\R}=\Gamma\otimes \R$;

-   an ind-constructible, $\op{Gal}({\overline{\k}}/\k)$-equivariant homomorphism $$\op{cl}_{\kk}: K_0(\CC(\kk))\to \Gamma$$ compatible with the Euler form and the skew-symmetric bilinear form;

-   a constructible stability structure $\sigma\in Stab(\CC,\op{cl})$ compatible with the quadratic form $Q$ in the sense that $Q_{|\op{Ker}Z}<0$ and $Q(\op{cl}_{\kk}(E))\geqslant 0$ for $E\in \CC^{ss}(\overline{\k})$.

In the next section we are going to define a homomorphism from the motivic Hall algebra to the associative unital algebra called motivic quantum torus. The latter is defined in the following way.

For any commutative unital ring $C$ which contains an invertible symbol ${\mathbb L}^{1/2}$ we introduce a $C$-linear associative algebra $${\cal R}_{\Gamma,C}:=\oplus_{\gamma\in \Gamma}C\cdot \hat{e}_{\gamma}$$ where the generators $\hat{e}_{\gamma}, \gamma\in \Gamma$ satisfy the relations $$\hat{e}_{\gamma_1}\hat{e}_{\gamma_2}={\mathbb L}^{{1\over{2}}\langle \gamma_1,\gamma_2\rangle}\hat{e}_{\gamma_1+\gamma_2}, \,\,\,\hat{e}_0=1\,\,.$$ We will call it the *quantum torus* associated with $\Gamma$ and $C$.

For any strict sector $V\subset \R^2$ we define $${\cal R}_{V,C}:=\prod_{\gamma \in \Gamma\cap \,C_0(V,Z,Q)}C\cdot \hat{e}_{\gamma}$$ and call it the quantum torus associated with $V$. Here we introduce a notation which will be used later: $$C_0(V,Z,Q):=C(V,Z,Q)\cup \{0\}$$ where the cone $C(V,Z,Q)$ was defined in 2.2. Algebra ${\cal R}_{V,C}$ is the natural completion of the subalgebra ${\cal R}_{V,C}\cap {\cal R}_{\Gamma,C}\subset{\cal R}_{\Gamma,C}$.

Let us choose as $C$ the ring $\overline{D^{\mu}}$. We denote ${\cal R}_{\Gamma}:={\cal R}_{\Gamma, \overline{D^{\mu}}}$ the corresponding quantum torus and call it the *motivic quantum torus* associated with $\Gamma$. Similarly, we have motivic quantum tori $R_V$ associated with strict sectors $V$.

*Step 5*.

We define an element $A_V^{mot}\in {\cal R}_V:={\cal R}_{V,\overline{D^{\mu}}}$ in the following way. First, we fix a branch of the function $\op{Log}z$, where $z\in V$ (the result will not depend on the choice of the branch). Recall the category $\CC_{V,\op{Log}}\subset \CC$ (see Section 3.4). It follows from our assumptions that for any $\gamma\in \Gamma$ the set $\CC_{V,\gamma}=\{E\in Ob(\CC_{V,\op{Log}})|\op{cl}(E)=\gamma\}$ is constructible.

Finally, we define the desired element $$A_V^{mot}=\sum_{\gamma}\left(\int_{\CC_{V,\gamma}}w \right)\cdot \hat{e}_{\gamma}\,\,.$$ The element $A_V^{mot}$ in fact depends only on $\overline{w}$.

Informally, one can write $$A_V^{mot}=\sum_{E\in Iso(\CC_{V,\op{Log}})}{w(E)\over {[\op{Aut}(E)]}}\hat{e}_{\op{cl}(E)}=1+\dots\in {\cal R}_V,$$ where $Iso(\CC_{V,\op{Log}})$ denotes the set of isomorphism classes of objects of the category $\CC_{V,\op{Log}}$.

::: thm
Assuming the integral identity, the collection of elements $(A_V^{mot})$ satisfies the Factorization Property: if a strict sector $V$ is decomposed into a disjoint union $V=V_1\sqcup V_2$ (in the clockwise order) then $$A_V^{mot}=A_{V_1}^{mot}A_{V_2}^{mot}\,\,.$$ Moreover we have a local homeomorphism $Stab(\CC)\to Stab\left({\cal R}_{\Gamma,\overline{D^{\mu}}}\right)$.
:::

This theorem follows immediately from the statement of Proposition 11 (see 6.1) about the elements $A_V^{\op{Hall}}$, and the Theorem 8 from the next section.
