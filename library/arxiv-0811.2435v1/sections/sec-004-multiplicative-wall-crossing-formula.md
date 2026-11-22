---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-004-multiplicative-wall-crossing-formula
section_title: "Multiplicative wall-crossing formula"
section_number: null
pages: 10-15
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 0.985
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 51 sections: Front matter; Introduction; Counting problems for 3-dimensiona"
---
The wall-crossing formulas for the numerical Donaldson-Thomas invariants do not depend on their origin and can be expressed in terms of graded Lie algebras. This is explained in Section 2. Our main application is the case of $3d$ Calabi-Yau categories. Let us recall that if ${\cal C}$ is an $Ext$-finite Calabi-Yau category of the odd dimension $d$ (e.g. $d=3$) then the Euler form

$$\chi:K_0(\CC)\otimes K_0(\CC)\to \Z,\,\,\,\,\chi(E,F):=\sum_{n\in \Z} (-1)^n \dim \, \op{Ext}^n(E,F)$$ is skew-symmetric. In this case we also assume that if $\CC$ is endowed with polarization, then a skew-symmetric bilinear form $\langle\bullet,\bullet\rangle: \Gamma\otimes \Gamma\to \Z$ is given and satisfies $$\langle \op{cl}(E),\op{cl}(F)\rangle=\chi(E,F)\,\,\,\,\,\forall E,F\in Ob(\CC)\,.$$

In general, having a free abelian group $\Gamma$ of finite rank endowed with an integer-valued skew-symmetric form $\langle\bullet,\bullet\rangle$, we define a Lie algebra over $\Q$ $\g_{\Gamma}:=\g_{(\Gamma,\langle\bullet,\bullet\rangle)}$, with the basis $(e_\gamma)_{\gamma\in \Gamma}$ and the Lie bracket

$$[ e_{\gamma_1}, e_{\gamma_2}]=(-1)^{\langle \gamma_1,\gamma_2\rangle}\langle
\gamma_1,\gamma_2\rangle\,e_{\gamma_1+\gamma_2}\,\,.$$

This Lie algebra is isomorphic (non-canonically) to the Lie algebra of regular functions on the algebraic Poisson torus ${ \op{Hom}}(\Gamma, {{\bf G}}_m)$ endowed with the natural translation-invariant Poisson bracket.[^1]

An additive map $Z:\Gamma\to \C$ is called *generic* if there are no two $\Q$-independent elements of the lattice $\Gamma$ which are mapped by $Z$ into the same straight line in $\R^2=\C$. The set of non-generic maps is a countable union of real hypersurfaces in $\C^n=\op{Hom}(\Gamma, \C)$. These hypersurfaces are called *walls*.

Let us choose such an additive map $Z$ and an arbitrary norm $\parallel \bullet \parallel$ on the real vector space $\Gamma_{\R}=\Gamma\otimes \R$. We will keep the same notation for the $\R$-linear extension of $Z$ to $\Gamma_{\R}$. Finally, assume that we are given an even map $\Omega:\Gamma\setminus \{0\}\to \Z$ supported on the set of $\gamma\in \Gamma$ such that $\parallel \gamma \parallel\le C|Z(\gamma) |$ for some given constant $C>0$.

Let $(Z_t)_{t\in [0,1]}$ be a generic piece-wise smooth path in $\C^n=\op{Hom}(\Gamma, \C)$ such that $Z_0$ and $Z_1$ are generic. The wall-crossing formula calculates the function $\Omega_1$ corresponding to $Z_1$ in terms of the function $\Omega=\Omega_0$ corresponding to $Z_0$. This is analogous to the analytic continuation of a holomorphic function expressed in terms of its Taylor coefficients. The continuation is unique if it exists, and is not changed under a small deformation of the path with the fixed endpoints.

Let us call *strict* a sector in $\R^2$ with the vertex at the origin $(0,0)$ which is less than $180^\circ$. With a strict sector $V\subset \R^2$ we associate a group element $A_V$ given by the infinite product $$A_V:=\prod_{\gamma\in Z^{-1}(V )\cap \Gamma}^{\longrightarrow}
    \exp\left(- \Omega(\gamma)\sum_{n=1}^\infty \frac{e_{n\gamma}}{n^2}\right).$$

The product takes value in a certain pro-nilpotent Lie group $G_V:=G_{V,\Gamma, \langle \bullet,\bullet,\rangle}$, which we will describe below. The right arrow in the product sign means that the product is taken in the *clockwise* order on the set of rays $\R_+\cdot Z(\gamma)\subset V\subset \C$. For the product in the anti-clockwise order we will use the left arrow.

Let us describe the Lie algebra $\g_V=Lie(G_V)$ of the pro-nilpotent Lie group $G_V$. We denote by $C(V)$ a convex cone in $\Gamma_{\R}$ which is the convex hull of the set of points $v \in Z^{-1}(V)$ such that $\parallel v \parallel\le C|Z(v)|$. The Lie algebra $Lie(G_V)$ is the infinite product $\prod_{\gamma \in \Gamma \cap  C(V)} \Q\cdot e_\gamma$ equipped with the above Lie bracket.

Now we can formulate the wall-crossing formula. It says (roughly) that $A_V$ does not change as long as no lattice point $\gamma\in  \Gamma$ with $\Omega_t(\gamma)\ne 0$ crosses the boundary of the cone $Z^{-1}_t(V)$ (here $\Omega_t$ corresponds to the point $t\in [0,1]$). By our assumptions, if $t=t_0$ corresponds to a non-generic central charge $Z_{t_0}$ then there exists a $2$-dimensional lattice $\Gamma_0\subset \Gamma$ such that $Z_{t_0}(\Gamma_0)$ belongs to a real line ${\R}e^{i\alpha}$ for some $\alpha\in [0,\pi]$.

The wall-crossing formula describes the change of values $\Omega(\gamma)$ for $\gamma \in \Gamma_0$ and depends only on the restriction $\Omega_{|\Gamma_0}$ of $\Omega$ to the lattice $\Gamma_0$. Values $\Omega(\gamma)$ for $\gamma\notin \Gamma_0$ do not change at $t=t_0$. Denote by $k\in \Z$ the value of the form $\langle\bullet,\bullet\rangle$ on a fixed basis $\gamma_1,\gamma_2$ of $\Gamma_0\simeq \Z^2$ such that $C(V)\cap \Gamma_0\subset \Z_{\geqslant 0}\cdot\gamma_1\oplus \Z_{\geqslant 0}\cdot\gamma_2$. We assume that $k\ne 0$, otherwise there will be no jump in values of $\Omega$ on $\Gamma_0$. The group elements which we are interested in can be identified with products of the following automorphisms[^2] of $\Q[[x,y]]$ preserving the symplectic form $k^{-1}(xy)^{-1} dx\wedge dy$: $$T_{a,b}^{(k)}:(x,y)\mapsto$$ $$\mapsto \left( x\cdot (1-(-1)^{kab} x^a y^b)^{-kb}, y\cdot(1-(-1)^{kab} x^a y^b)^{ka}\right),\medskip a,b\geqslant 0, a+b\geqslant 1\,.$$ For $\gamma=a\gamma_1+b\gamma_2$ we have $$T_{a,b}^{(k)}=\exp\left(-\sum_{n\geqslant 1}\frac{e_{n\gamma}}{n^2}\right)$$ in the above notation. Any exact symplectomorphism $\phi$ of $\Q[[x,y]]$ can be decomposed uniquely into a clockwise and an anti-clockwise product: $$\phi=\prod_{a,b}^{\longrightarrow} \left(T_{a,b}^{(k)}\right)^{c_{a,b}}=\prod_{a,b}^{\longleftarrow} \left(T_{a,b}^{(k)}\right)^{{d}_{a,b}}$$ with certain exponents $c_{a,b},d_{a,b}\in \Q$. These exponents should be interpreted as the limiting values of the functions $\Omega_{t_0}^{\pm}=\lim_{t\to t_0\pm 0}\Omega_t$ restricted to $\Gamma_0$. The passage from the clockwise order (when the slope $a/b \in [0,+\infty]\cap {\mathbb P}^1(\Q)$ decreases) to the anti-clockwise order (when the slope increases) gives the change of $\Omega_{|\Gamma_0}$ as we cross the wall. It will be convenient to denote $T_{a,b}^{(1)}$ simply by $T_{a,b}$. The pro-nilpotent group generated by transformations $T_{a,b}^{(k)}$ coincides with the one generated by transformations $T_{a,|k|b}$.

The compatibility of the wall-crossing formula with the *integrality* of the numbers $\Omega(\gamma)$ is not obvious but follows from:

::: conj
If for $k>0$ one decomposes the product $T_{1,0}\cdot T_{0,k}$ in the opposite order: $$T_{1,0}\cdot T_{0,k}= \prod_{a/b \text{ increases}}  (T_{a,kb})^{d(a,b,k)},$$ then $d(a,b,k)\in \Z$ for all $a,b,k$.
:::

An equivalent form of this conjecture says that if one decomposes $T_{1,0}^k \cdot T_{0,1}^k$ in the opposite order then all exponents will belong to $k\Z$.

Here are decompositions for $k=1,2$ $$T_{1,0} \cdot T_{0,1} =T_{0,1}\cdot T_{1,1}\cdot T_{1,0}\,\,,$$ $$T_{1,0}^{(2)} \cdot T_{0,1}^{(2)}= T_{0,1}^{(2)}\cdot T_{1,2}^{(2)}\cdot T_{2,3}^{(2)}\cdot\dots
    \cdot (T_{1,1}^{(2)})^{-2} \cdot \dots\cdot T_{3,2}^{(2)} \cdot T_{2,1}^{(2)}
\cdot T_{1,0}^{(2)}\,\,,$$ or equivalently $$T_{1,0} \cdot T_{0,2}= T_{0,2}\cdot T_{1,4}\cdot T_{2,6}\cdot\dots
    \cdot T_{1,2}^{-2} \cdot \dots\cdot T_{3,4} \cdot T_{2,2}
\cdot T_{1,0}\,\,.$$ Greg Moore and Frederik Denef pointed out that the factors in the last formula correspond to the BPS spectrum of $N=2, d=4$ super Yang-Mills model studied by Seiberg and Witten in [@SeibW]. A "physical\" explanation of our formulas in this context was given in [@GaMNeit], see also our Section 2.7.

For $k\geqslant 3$ or $k\le -1$ the decomposition of $T_{1,0}^{(k)}\cdot T_{0,1}^{(k)}$ is not yet known completely. Computer experiments give a conjectural formula for the diagonal term with the slope $a/b=1$. The corresponding symplectomorphism is given by the map $$(x,y)\mapsto (x \cdot F_k(xy)^{-k}, y \cdot F_k(xy)^{k}),$$ where the series $F_k=F_k(t)\in 1+ t\Z[[t]]$ is an algebraic hypergeometric series given for $k\geqslant 3$ by the formulas: $$\sum_{n=0}^\infty \binom {(k-1)^2n +k-1}{n}\frac {t^n}{(k-2)n+1}=
        \exp\left(\sum_{n=1}^\infty \binom{(k-1)^2n}{n}
\frac{k}{(k-1)^2}\frac{t^n}{n}\right).$$

The function $F_k$ satisfies the equation $$F_k(t)\left(1-t F^{k-2}_k(t)\right)^k-1=0\,\,.$$

::: rmk
The above example for $k=1$ is compatible with the expected behavior of Donaldson-Thomas invariants when we have two spherical objects $E_1,E_2\in \CC$ (sphericity means that ${\op{Ext}}^{\bullet}(E_i,E_i)=H^{\bullet}(S^3)$) such that

$${\op{Ext}}^1 (E_2,E_1)=\k, \,\,\, {\op{Ext}}^n(E_2,E_1)=0 \text{ for } n\ne 1\,\,.$$ In this case on the one side of the wall we have two semistable objects $E_1,E_2$, and on the other side we have three semistable objects $E_1,E_2, E_{12}$ where $E_{12}$ is the extension of $E_2$ by $E_1$. In the case of the derived of the Fukaya category the objects $E_i, i=1,2$ can correspond to embedded special Lagrangian spheres intersecting transversally at one point. Then $E_{12}$ corresponds to their Lagrangian connected sum.
:::

The automorphisms $T_{a,b}$ are a special case of the more general ones. Namely, we can consider the following rational automorphisms of $\g_{\Gamma}$ (considered as a Poisson algebra):

$$T_{\gamma}: e_{\mu}\mapsto (1-e_{\gamma})^{\langle \gamma, \mu\rangle}e_{\mu},\,\,\,\,\, \gamma,\mu \in \Gamma\,\,.$$ The group element $A_V$ in the above notation has the form $$A_V=\prod_{\gamma\in Z^{-1}(V )\cap \Gamma}^{\longrightarrow} T_\gamma^{\,\Omega(\gamma)}$$ and acts on a completion of $\g_\Gamma$. It is easy to quantize this Poisson algebra. The corresponding algebra (quantum torus) is additively generated by quantum generators $\hat{e}_{\gamma}, \gamma\in \Gamma$ subject to the relations $$\hat{e}_{\gamma}\hat{e}_{\mu}=q^{{1\over{2}}\langle \gamma,\mu\rangle}\hat{e}_{\gamma+\mu}\,\,,$$ where $q$ is a parameter (with the classical limit $q^{1\over{2}}\to -1$). Then one has formulas similar to the above for the "quantum\" analogs of automorphisms $T_{\gamma}, \gamma \in \Gamma$ (see Sections 6.4 and 7.1).

For general $k\ge 2$ the decomposition of the product $T_{1,0}\cdot T_{0,k}$ as in Conjecture 1, describes numerical DT-invariants of the Calabi-Yau category associated with the Kronecker quiver consisting of two vertices and $k$ parallel arrows (see Section 8 for a general theory). Recent paper [@Re1] gives an explicit formula for $d(a,b,k)$ in terms of the Euler characteristic of the framed moduli space of semistable representations of the quiver. Moreover, a weak form of the integrality Conjecture 1 is proved in [@Re1].

[^1]: Later we will use the multiplication as well. It is given explicitly by $e_{\gamma_1}e_{\gamma_2}=(-1)^{\langle \gamma_1,\gamma_2\rangle}\,e_{\gamma_1+\gamma_2}.$

[^2]: Here we write an automorphism as acting on elements of the algebra of functions. The corresponding automorphism on *points* is given by the inverse formula.
