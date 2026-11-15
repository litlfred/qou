---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-013-016-quasitriangular-quantum-groupoids
section_title: "Quasitriangular quantum groupoids"
section_number: 0.16
pages: 16-19
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.992
latex_coverage_ratio: 0.937
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
::: definition
[]{#QT WHA label="QT WHA"} A quasitriangular quantum groupoid is a pair ($H,\, {\mathcal R}$) where $H$ is a quantum groupoid and ${\mathcal R}\in \Delta^{op}(1)(H\otimes_k H)\Delta(1)$ satisfying the following conditions : $$\Delta^{op}(h){\mathcal R}= {\mathcal R}\Delta(h),$$ for all $h\in H$, where $\Delta^{op}$ denotes the comultiplication opposite to $\Delta$, $$\begin{aligned}
(\mbox{id}\otimes \Delta){\mathcal R}&=& {\mathcal R}_{13}{\mathcal R}_{12}, \label{DR1}\\
(\Delta \otimes \mbox{id}){\mathcal R}&=& {\mathcal R}_{13}{\mathcal R}_{23}, \label{DR2}
\end{aligned}$$ where ${\mathcal R}_{12} = {\mathcal R}\otimes 1$, ${\mathcal R}_{23} = 1\otimes {\mathcal R}$, etc. as usual, and such that there exists ${\bar {\mathcal R}}\in \Delta(1)(H\otimes_k H)\Delta^{op}(1)$ with $${\mathcal R}{\bar {\mathcal R}}= \Delta^{op}(1), \qquad {\bar {\mathcal R}}{\mathcal R}= \Delta(1).$$
:::

Note that ${\bar {\mathcal R}}$ is uniquely determined by ${\mathcal R}$: if ${\bar {\mathcal R}}$ and ${\bar {\mathcal R}}'$ are two elements of $\Delta(1)(H\otimes_k H)\Delta^{op}(1)$ satisfying the previous equation, then $${\bar {\mathcal R}}={\bar {\mathcal R}}\Delta^{op}(1)={\bar {\mathcal R}}{\mathcal R}{\bar {\mathcal R}}'=\Delta(1){\bar {\mathcal R}}'={\bar {\mathcal R}}'.$$ For any two objects $V$ and $W$ of $\mbox{Rep}(H)$ define $c_{V,W}: V\otimes W \to W\otimes V$ as the action of $R_{21}$ : $$c_{V,W}(x) = R^{(2)}\cdot x^{(2)}\otimes R^{(1)}\cdot x^{(1)},$$ where $x =x^{(1)}\otimes x^{(2)}\in V\otimes W$ and ${\mathcal R}={\mathcal R}^{(1)}\otimes {\mathcal R}^{(2)}$.

::: proposition
[]{#braiding label="braiding"} The family of homomorphisms $\{c_{V,W}\}_{V,W}$ defines a braiding in $\mbox{Rep}(H)$. Conversely, if $\mbox{Rep}(H)$ is braided, then there exists ${\mathcal R}$, satisfying the properties of Definition [\[QT WHA\]](#QT WHA){reference-type="ref" reference="QT WHA"} and inducing the given braiding.
:::

::: proof
*Proof.* Note that $c_{V,W}$ is well-defined, since ${\mathcal R}_{21}= \Delta(1){\mathcal R}_{21}$. To prove the $H$-linearity of $c_{V,W}$ we observe that

$$\begin{aligned}
c_{V,W}(h\cdot x)
&=& {\mathcal R}^{(2)}h_{(2)}\cdot x^{(2)}\otimes {\mathcal R}^{(1)}h_{(1)}\cdot x^{(1)}\\
&=& h_{(1)} {\mathcal R}^{(2)}\cdot x^{(2)}\otimes h_{(2)} {\mathcal R}^{(1)}\cdot x^{(1)}=h\cdot (c_{V,W}(x)).
\end{aligned}$$ The inverse of $c_{V,W}$ is given by $$c_{V,W}^{-1}(y) = {\bar {\mathcal R}}^{(1)}\cdot y^{(2)}\otimes {\bar {\mathcal R}}^{(2)}\cdot y^{(1)},
\qquad \mbox{ where } y =y^{(1)}\otimes y^{(2)}\in W\otimes V,$$ therefore $c_{V,W}$ is is an isomorphism. Finally, we check the braiding identities. Let $x =x^{(1)}\otimes x^{(2)}\otimes x^{(3)}\in U\otimes V\otimes W$, then $$\begin{aligned}
\lefteqn{(\mbox{id}_V \otimes c_{U,W})(c_{U,V}\otimes \mbox{id}_W)(x) = } \\
&=& (\mbox{id}_V \otimes c_{U,W})
    ({\mathcal R}^{(2)}\cdot x^{(2)}\otimes {\mathcal R}^{(1)}\cdot x^{(1)}\otimes x^{(3)}\\
&=& {\mathcal R}^{(2)}\cdot x^{(2)}\otimes {{\mathcal R}'}^{(2)}\cdot x^{(3)}\otimes {{\mathcal R}'}^{(1)}{\mathcal R}^{(1)}\cdot x^{(1)}\\
&=& {\mathcal R}^{(2)}_{(1)}\cdot x^{(2)}\otimes {\mathcal R}^{(2)}_{(2)}\cdot x^{(3)}\otimes {\mathcal R}^{(1)}\cdot x^{(1)}
    = c_{U, V\otimes W}(x).
\end{aligned}$$ Similarly, we have $(c_{U,W}\otimes\mbox{id}_V)(\mbox{id}_U\otimes c_{V,W}) = c_{U\otimes V,W}$.

The third equality of this computation shows that the relations of Definition [\[QT WHA\]](#QT WHA){reference-type="ref" reference="QT WHA"} are equivalent to the braiding identities. ◻
:::

::: lemma
[]{#QYBE label="QYBE"} Let $(H,{\mathcal R})$ be a quasitriangular quantum groupoid. Then ${\mathcal R}$ satisfies the quantum Yang-Baxter equation : $${\mathcal R}_{12}{\mathcal R}_{13}{\mathcal R}_{23} = {\mathcal R}_{23}{\mathcal R}_{13}{\mathcal R}_{12}.$$
:::

::: proof
*Proof.* It follows from the first two relations of Definition [\[QT WHA\]](#QT WHA){reference-type="ref" reference="QT WHA"}, that $$\begin{aligned}
{\mathcal R}_{12}{\mathcal R}_{13}{\mathcal R}_{23}=(\mbox{id}\otimes \Delta^{op})({\mathcal R}) {\mathcal R}_{23}=
{\mathcal R}_{23} (\mbox{id}\otimes \Delta)({\mathcal R})={\mathcal R}_{23}{\mathcal R}_{13}{\mathcal R}_{12}.
\end{aligned}$$ ◻
:::

::: remark
Let us define two linear maps ${\mathcal R}_1, {\mathcal R}_2 : \widehat H \to H$ by $${\mathcal R}_1(\phi) =(\mbox{id}\otimes \phi)({\mathcal R}), \quad
{\mathcal R}_2(\phi) =(\phi\otimes \mbox{id})({\mathcal R}), \quad\mbox{for all } \phi\in \widehat H.$$ Then condition ([\[DR1\]](#DR1){reference-type="ref" reference="DR1"}) of Definition [\[QT WHA\]](#QT WHA){reference-type="ref" reference="QT WHA"} is equivalent to ${\mathcal R}_1$ being a coalgebra homomorphism and algebra anti-homomorphism and condition ([\[DR2\]](#DR2){reference-type="ref" reference="DR2"}) is equivalent to ${\mathcal R}_2$ being an algebra homomorphism and coalgebra anti-homomorphism. In other words, ${\mathcal R}_1:\widehat H \to H^{op}$ and ${\mathcal R}_2:\widehat H \to H^{cop}$ are homomorphisms of quantum groupoids.
:::

::: proposition
[]{#properties of R label="properties of R"} For any quasitriangular quantum groupoid $(H,{\mathcal R})$, we have: $$\begin{aligned}
(\varepsilon_s\otimes \mbox{id})({\mathcal R}) &=& \Delta(1), \qquad
(\mbox{id}\otimes \varepsilon_s)({\mathcal R}) = (S\otimes \mbox{id})\Delta^{op}(1), \\
(\varepsilon_t\otimes \mbox{id})({\mathcal R}) &=& \Delta^{op}(1),\qquad
(\mbox{id}\otimes \varepsilon_t)({\mathcal R}) = (S\otimes \mbox{id})\Delta(1), \\
(S\otimes \mbox{id})({\mathcal R}) &=& (\mbox{id}\otimes S^{-1})({\mathcal R}) = {\bar {\mathcal R}},
\qquad (S\otimes S)({\mathcal R})= {\mathcal R}. 
\end{aligned}$$
:::

::: proof
*Proof.* The proof is essentially the same as ([@Ma], 2.1.5). ◻
:::

::: proposition
[]{#elements u and v label="elements u and v"} Let $(H,{\mathcal R})$ be a quasitriangular quantum groupoid. Then $$S^2(h) = uhu^{-1}$$ for all $h\in H$, where $u=S({\mathcal R}^{(2)}){\mathcal R}^{(1)}$ is an invertible element of $H$ such that $$u^{-1} = {\mathcal R}^{(2)}S^2({\mathcal R}^{(1)}), \quad \Delta(u) = {\bar {\mathcal R}}{\bar {\mathcal R}}_{21} (u\otimes u).$$ Likewise, $v = S(u) = {\mathcal R}^{(1)}S({\mathcal R}^{(2)})$ obeys $S^{-2}(h) = vhv^{-1}$ and $$v^{-1} = S^2({\mathcal R}^{(1)}){\mathcal R}^{(2)}, \quad \Delta(v) = {\bar {\mathcal R}}{\bar {\mathcal R}}_{21} (v\otimes v).$$
:::

::: proof
*Proof.* Note that $S({\mathcal R}^{(2)})y{\mathcal R}^{(1)}= S(y)u$ for all $y\in H_s$. Hence, we have $$\begin{aligned}
S(h_{(2)})uh_{(1)}
&=& S(h_{(2)}) S({\mathcal R}^{(2)}){\mathcal R}^{(1)}h_{(1)} = S({\mathcal R}^{(2)}h_{(2)}){\mathcal R}^{(1)}h_{(1)} \\
&=& S(h_{(1)} {\mathcal R}^{(2)}) h_{(2)} {\mathcal R}^{(1)}= S({\mathcal R}^{(2)}) \varepsilon_s(h) {\mathcal R}^{(1)}\\
&=& S(\varepsilon_s(h))u,
\end{aligned}$$ for all $h\in H$. Therefore, $$\begin{aligned}
uh
&=& S(1_{(2)})u1_{(2)}h = S(\varepsilon_t(h_{(2)})u h_{(1)} \\
&=& S(h_{(2)} S(h_{(3)}))u h_{(1)} = S^2(h_{(3)}) S(h_{(2)})u h_{(1)} \\
&=&  S^2(h_{(2)}) S(\varepsilon_s(h_{(1)})) u = S(\varepsilon_s(h_{(1)})S(h_{(2)}))u = S^2(h)u.
\end{aligned}$$ The remaining part of the proof follows the lines of ([@Ma], 2.1.8). The results for $v$ can be obtained by applying the results for $u$ to the quasitriangular quantum groupoid $(H^{op/cop}, {\mathcal R})$. ◻
:::

::: definition
[]{#Drinfeld element label="Drinfeld element"} The element $u$ defined in Proposition [\[elements u and v\]](#elements u and v){reference-type="ref" reference="elements u and v"} is called *the Drinfeld element* of $H$.
:::

::: corollary
[]{#uv is central label="uv is central"} The element $uv=vu$ is central and obeys $$\Delta(uv) =({\bar {\mathcal R}}{\bar {\mathcal R}}_{21})^2(uv\otimes uv).$$ The element $uv^{-1} =vu^{-1}$ is group-like and implements $S^4$ by conjugation.
:::

::: proposition
[]{#range of F label="range of F"} Given a quasitriangular quantum groupoid $(H, {\mathcal R})$, consider a linear map $F:\widehat H\to H$ given by

$$\label{map F}
F: \phi \mapsto (\phi\otimes \mbox{id})({\mathcal R}_{21}{\mathcal R}),\qquad \phi\in \widehat H.$$ Then the range of $F$ belongs to $C_H(H_s)$, the centralizer of $H_s$.
:::

::: proof
*Proof.* Take $y\in H_s$. Then we have : $$\phi({\mathcal R}^{(2)}{{\mathcal R}'}^{(1)}) {\mathcal R}^{(1)}{{\mathcal R}'}^{(2)}y =
\phi({\mathcal R}^{(2)}y {{\mathcal R}'}^{(1)}) {\mathcal R}^{(1)}{{\mathcal R}'}^{(2)}= \phi({\mathcal R}^{(2)}{{\mathcal R}'}^{(1)}) y {\mathcal R}^{(1)}{{\mathcal R}'}^{(2)},$$ therefore $F(\phi)\in C_H(H_s)$, as required. ◻
:::

::: definition
[]{#factorizability label="factorizability"} A quasitriangular quantum groupoid is *factorizable* if the above map $F: \widehat H \to C_H(H_s)$ is surjective.
:::

The factorizability of $H$ means that ${\mathcal R}$ is as non-trivial as possible, in contrast to *triangular* quantum groupoids, for which ${\mathcal R}_{21} = {\bar {\mathcal R}}$ and the range of $F$ is equal to $H_t$.
