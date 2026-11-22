---
doc_id: arxiv-math-0408210v3
doc_title: "A simple algebraic proof of the algebraic index theorem"
section_id: sec-004-23-fedosov-deformation-quantization-with-twisted
section_title: "Fedosov deformation quantization with twisted coefficients."
section_number: 2.3
pages: 6-11
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.981
latex_coverage_ratio: 0.973
doc_brief: "A simple algebraic proof of the algebraic index theorem — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
Let ${\cal M}$ be a symplectic manifold of dimension $2n$. We denote by ${\omega}={\omega}_{ij}(x)dx^i dx^j$ the corresponding symplectic form and by $$\overline{\omega}= {\omega}^{ij}(x)\frac{{\partial}}{{\partial}x^i}\wedge \frac{{\partial}}{{\partial}x^j}$$ the corresponding Poisson tensor. Here $x^i$ denote local coordinates and the indices $i,j$ run from $1$ from $2n$ . For a vector bundle $V$ of rank $N$ over ${\cal M}$ we will denote by $End(V)$ the bundle of endomorphisms of $V$ and by $End_V= {\Gamma}({\cal M}, End(V))$ the algebra of global sections of $End(V)$ .

If the vector bundle $V$ is endowed with a connection ${\partial}^V$ then

::: defi
By quantization of the algebra $End_V$ we mean a construction of an associative ${\Bbb C}((h))$-linear product in $End_V(({\hbar}))$ given by the formal power series $$\label{star}
a *b = a b + \sum_{k\ge 1} {\hbar}^k B_k(a,b)\,,
\qquad a,\, b \in End_V$$ of bidifferential operators $B_k\,:\, End_V\otimes End_V\mapsto End_V$ such that $$B_1(a,b) - B_1(b,a) = {\omega}^{ij}(x) {\partial}^V_i(a) {\partial}^V_j(b)\,.$$
:::

In [@F1] B. Fedosov proposed a simple procedure for the deformation quantization of the algebra of endomorphisms of a vector bundle $V$ over a symplectic manifold ${\cal M}$. The main ingredient of the construction is the *Weyl algebra bundle* $W(End_V)$ whose sections are the following formal power series $$a=a(x,y,h)=\sum_{k,l}{\hbar}^k a_{k; i_1 i_2\dots i_l}(x)y^{i_1}\dots
y^{i_l}\,,$$ where $y=(y^1\dots y^{2n})$ are fiber coordinates of the tangent bundle $T{\cal M}$, $a_{k; i_1 i_2 \dots i_l}$ represent sections of $End(V)\otimes S^l(T^{*}M)$ and the summation over $k$ is bounded below.

Multiplication of two sections of $W(End_V)$ is given by the Weyl formula $$\label{circ1}
a \circ b(x,y,{\hbar})=\exp\left(\frac{{\hbar}}{2}\,
{\omega}^{ij}\frac{{\partial}}{{\partial}y^i}\frac{{\partial}}{{\partial}z^j}\right)a(x,y,{\hbar})b(x,z,{\hbar})|_{y=z}.$$ Notice that in the right hand side of ([\[circ1\]](#circ1){reference-type="ref" reference="circ1"}) the sections of $W(End_V)$ are multiplied via the product induced from the algebra $End_V$ .

For any point $p\in {\cal M}$ the fiber $W_p(End_V)$ of the Weyl algebra bundle at $p$ is isomorphic to the algebra ${\mathfrak{gl}}_N({\cal W})$ of $N \times N$-matrices of the Weyl algebra ${\cal W}$ associated with the cotangent space $T^*_p({\cal M})$ at the point $p$ with the symplectic form $\overline{\omega}_p$ . The transition functions are realized by the adjoint action of the group $GL_N$ .

The filtration ([\[filtr\]](#filtr){reference-type="ref" reference="filtr"}) of the Weyl algebra gives us a natural filtration of the bundle $W(End_V)$ $$\label{filtr-bun}
\begin{array}{c}
\displaystyle
\dots \subset W^1(End_V)  \subset W^0(End_V)  \subset
W^{-1}(End_V) \dots \subset W(End_V)\,, \\[0.3cm]
\displaystyle
{\Gamma}(W^m(End_V)) = \{ a = \sum_{2k+p\ge m}
{\hbar}^k a_{k;i_1 \dots i_p}(x)y^{i_1} \dots y^{i_p}\}\,.
\end{array}$$ This filtration defines the $2[{\hbar}]+[y]$-adic topology in the algebra ${\Gamma}(W(End_V))$ of sections of $W(End_V)$ .

The vector space ${\Omega}^{{\bullet}}(W(End_V))$ of smooth exterior forms with values in $W(End_V)$ is naturally a graded associative algebra with the product induced by ([\[circ1\]](#circ1){reference-type="ref" reference="circ1"}) and the following graded commutator $$[a,b]= a \circ b - (-)^{q_a q_b} b\circ a\,,$$ where $q_a$ and $q_b$ are exterior degrees of $a$ and $b$ , respectively. The filtration of $W(End_V)$ ([\[filtr-bun\]](#filtr-bun){reference-type="ref" reference="filtr-bun"}) gives us a filtration of the algebra ${\Omega}^{{\bullet}}(W(End_V))$ $$\begin{array}{c}
\dots \subset {\Omega}^{{\bullet}}(W^1(End_V))
\subset{\Omega}^{{\bullet}}(W^0(End_V))\subset  \phantom{aaaaaaa}  \\[0.3cm]
 \phantom{aaaaaaa} \subset{\Omega}^{{\bullet}}(W^{-1}(End_V)) \subset
\dots \subset {\Omega}^{{\bullet}}(W(End_V))\,.
\end{array}$$ In what follows we refer to the algebra ${\Omega}^{{\bullet}}({\cal M})$ of exterior forms on ${\cal M}$ as an algebra embedded into ${\Omega}^{{\bullet}}(W(End_V))$ via the natural map $\iota\,:\,{\Omega}^{{\bullet}}({\cal M}) \mapsto {\Omega}^{{\bullet}}(W(End_V))\,,$ which sends an exterior form $\eta\in {\Omega}^{{\bullet}}({\cal M})$ to the scalar matrix $\eta I_{N}\in {\Omega}^{{\bullet}}(W(End_V))$ .

Let ${\partial}^s$ be a torsion free connection on $T{\cal M}$ compatible with the symplectic structure ${\omega}$. Using the connection ${\partial}^s$ and the connection ${\partial}^V$ on $V$ we define the following linear operator $${\nabla}\,:\,{\Omega}^{{\bullet}}(W(End_V)) \mapsto
{\Omega}^{{\bullet}+1}(W(End_V))\,,$$ $$\label{nabla}
{\nabla}=dx^i\frac{{\partial}}{{\partial}x^i}-
dx^i{\Gamma}^{k}_{ij}(x)y^j\frac {{\partial}}{{\partial}y^k}+[{\Gamma}_V,\,\cdot\,]\,,$$ where ${\Gamma}^k_{ij}(x)$ are Christoffel symbols of ${\partial}^s$ and ${\Gamma}^V$ is the connection form of ${\partial}^V$ .

Thanks to the compatibility of ${\partial}^s$ with the symplectic structure ${\omega}$ the operator ([\[nabla\]](#nabla){reference-type="ref" reference="nabla"}) is a derivation of the graded algebra ${\Omega}^{{\bullet}}(W(End_V))$ . Furthermore, a simple computation shows that $${\nabla}^2 a = \frac1{2}[R+R^V,a]\,, \qquad
\forall~ a\in {\Omega}(W(End_V))\,,$$ where $R^V\in {\Omega}^2(End_V)$ is the curvature form of ${\partial}^V$, $$R= \frac1{2{\hbar}} {\omega}_{km}(R_{ij})^m_l(x) y^k y^l dx^i dx^j,$$ and $(R_{ij})^m_l(x)$ is the Riemann curvature tensor of ${\partial}^s$ .

::: defi
The  Fedosov  connection  is  a  nilpotent derivation of the graded algebra ${\Omega}^{{\bullet}}(W(End_V))$ of the following form $$\label{F-conn}
D= {\nabla}+ \frac1{{\hbar}}[A, \cdot\,]\,,
\qquad
A= - dx^i {\omega}_{ij}(x)y^j + r\,,$$ where $r$ is an element in ${\Omega}^1(W^2(End_V))$
:::

The flatness of $D$ is equivalent to the fact that the Fedosov-Weyl curvature $$\label{Weyl-c}
C^W= {\hbar}(R+ R^V) + 2 {\nabla}A + \frac1{{\hbar}} [A, A]$$ of $D$ belongs to the subspace ${\Omega}^2({\cal M})(({\hbar}))\subset {\Omega}^2(W(End_V))$ . A simple analysis of degrees in ${\hbar}$ and $y$ shows that $C^W$ is of the form $$\label{nado}
C^W = -{\omega}+ {\Omega}_{{\hbar}}\,,
\qquad {\Omega}_h \in {\hbar}{\Omega}^2(M)[[{\hbar}]]$$ whereas the Bianchi identity $D (C^W)=0$ implies that ${\Omega}_h$ is a series of two-forms closed with respect to the De Rham differential.

One can observe that the definition of the Fedosov connection depends on the choice of the symplectic connection ${\partial}^s$ and the connection ${\partial}^V$ on $V$. The following proposition shows how this problem can be remedied

::: pred
[]{#absor label="absor"} If ${\nabla}$ and $\widetilde{\nabla}$ are two operator ([\[nabla\]](#nabla){reference-type="ref" reference="nabla"}) corresponding to the symplectic connections ${\partial}^s$, $\widetilde{\partial}^s$ and the connections ${\partial}^V$, $\widetilde{\partial}^V$ on $V$, respectively, then the difference $\widetilde{D}-D$ between two Fedosov connections $$\label{tD}
\widetilde{D}= \widetilde{\nabla}+ \frac1{{\hbar}} [- dx^i {\omega}_{ij}(x)y^j + \widetilde{r}, \cdot\,]\,,
\qquad
D= {\nabla}+ \frac1{{\hbar}} [- dx^i {\omega}_{ij}(x)y^j + r, \cdot\,]\,,$$ takes the form of the commutator $$\widetilde{D}- D = \frac1{{\hbar}} [{\Delta}r, \cdot\,]\,,$$ where ${\Delta}r\in {\Omega}^1(W^2(End_V))$ . In other words any deviations of the connections ${\partial}^s$ and ${\partial}^V$ can be absorbed into the form $r\in {\Omega}^1(W^2(End_V))$ .
:::

**Proof.** See page $151$ in [@F1] . $\Box$

Let us consider the affine subspace $I_N\oplus {\Gamma}(W^1(End_V))$ in ${\Gamma}(W(End_V))$ consisting of the sums $U=I_N + U_1\,,$ where $I_N$ is the identity endomorphism of $V$ and $U_1$ is an arbitrary element in ${\Gamma}(W^1(End_V))$. It is straightforward that

::: pred
The affine subspace $I_N\oplus {\Gamma}(W^1(End_V)) \subset {\Gamma}(W(End_V))$ is a subgroup in the group of invertible elements of ${\Gamma}(W(End_V))$ . $\Box$
:::

We are now ready to give the following

::: defi
[]{#equiv label="equiv"} Two Fedosov connections $$D = {\nabla}+ \frac1{{\hbar}}[A, \cdot\,]\,, \qquad
\widetilde{D}= {\nabla}+ \frac1{{\hbar}}[\widetilde{A}, \cdot\,]$$ are called equivalent if there exists an element $U\in I_N\oplus {\Gamma}(W^1(End_V))$ such that $$\label{equiv1}
\widetilde{D}= D + [U^{-1}\circ DU,\cdot\,]$$ or equivalently $\widetilde{A}= U^{-1}\circ A \circ U + {\hbar}U^{-1}\circ {\nabla}U\,.$
:::

Let us remark that the Fedosov connection ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) can be rewritten as $$\label{DDD}
D = {\nabla}-{\delta}+ \frac1{{\hbar}}[r, \cdot\,]\,,$$ where $$\label{de}
{\delta}= \frac1{{\hbar}}[dx^i{\omega}_{ij}(x)y^j, \cdot\,]=
dx^i \frac{{\partial}}{{\partial}y^i}$$ is the Koszul derivation of the algebra ${\Omega}^{{\bullet}}(W(End_V))$ .

For our purposes we will need the homotopy operator for the Koszul differential ${\delta}$ $$\delta^{-1}a=y^k i\left( \frac \partial {\partial x^k}\right)
\int\limits_0^1 a(x,{\hbar}, ty,tdx)\frac{dt}t,  \label{del-1}$$ where $i(\partial /\partial x^k)$ denotes the contraction of an exterior form with the vector field $\partial /\partial x^k$ , and $\delta ^{-1}$ is extended to ${\Gamma}(W(End_V))$ by zero.

Simple calculations show that ${\delta}^{-1}$ is indeed the homotopy operator for ${\delta}$, namely $$a=\sigma(a) +\delta \delta ^{-1}a + \delta ^{-1}\delta a\,,
\qquad \forall~a\in{\Omega}(W(End_V))
 \label{Hodge}$$ where ${\sigma}$ is the natural projection $$\label{sigma}
{\sigma}(a)= a \Big |_{y=0,~dx=0}\,, \qquad
a\in {\Omega}^{{\bullet}}(W(End_V))$$ from ${\Omega}^{{\bullet}}(W(End_V))$ onto the algebra of endomorphisms $End_V(({\hbar}))$ .

The proof of the following theorem is contained in section $5.3$ of [@F1]. (More precisely, see theorem $5.3.3$ and remarks at the end of section $5.3$)

::: teo
[]{#F label="F"} If ${\partial}^s$ is a symplectic connection on ${\cal M}$, ${\partial}^V$ is a connection on $V$ and ${\Omega}_{{\hbar}}$ is a series of closed two-forms in ${\hbar}{\Omega}^2(M)[[{\hbar}]]$ then

1.  One can construct a nilpotent derivation $D={\nabla}+ {\hbar}^{-1}[r-dx^i{\omega}_{ij}(x)y^j, \cdot\,]$ whose Fedosov-Weyl curvature ([\[Weyl-c\]](#Weyl-c){reference-type="ref" reference="Weyl-c"}) is equal to $C^W= -{\omega}+ {\Omega}_{{\hbar}}$ and the element $r\in {\Omega}^1(W^2(End_V))$ satisfies the normalization condition $$\label{norm}
    {\delta}^{-1} r = 0\,.$$

2.  Given a Fedosov connection ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) one can construct a vector space isomorphism ${\lambda}$ $$\label{la}
    {\lambda}\,:\, End_V(({\hbar}))~ \widetilde{\rightarrow}~ {\Gamma}_D(W(End_V))$$ from $End_V(({\hbar}))$ to the algebra ${\Gamma}_D(W(End_V))$ of flat sections of $W(End_V)$ with respect to $D$. The product in $End_V(({\hbar}))$ induced via the isomorphism ${\lambda}$ is the desired star-product ([\[star\]](#star){reference-type="ref" reference="star"})

3.  Two Fedosov connections $D$ and $\widetilde{D}$ whose Fedosov-Weyl curvatures represent the same De Rham cohomology class in $H^2_{DR}({\cal M})[[{\hbar}]]$ are equivalent in the sense of definition [\[equiv\]](#equiv){reference-type="ref" reference="equiv"}. If the equivalence between $D$ and $\widetilde{D}$ is established by an element $U \in I_N \oplus
    {\Gamma}(W^1(End_V))$ then the map $$a \mapsto U \circ a \circ U^{-1}$$ gives an isomorphism from the algebra ${\Gamma}_{\widetilde{D}}(W(End_V))$ of flat sections of $\widetilde{D}$ to the algebra ${\Gamma}_{D}(W(End_V))$ of flat sections of $D$ .
:::

**Remark 1.** The construction of the Fedosov connection is functorial in the sense that if $u$ is an isomorphism from $V$ to $\widetilde{V}$ then $$\widetilde{D}= D + [u D(u^{-1}),\cdot\,]$$ is a Fedosov connection in ${\Omega}^{{\bullet}}(W(End_{\widetilde{V}}))$ . Moreover, the corresponding isomorphisms $${\lambda}\,:\, End_V(({\hbar})) ~\widetilde{\rightarrow}~
{\Gamma}_{D}(W(End_V))\,, \qquad
\widetilde{\lambda}\,:\,End_{\widetilde{V}}(({\hbar})) ~\widetilde{\rightarrow}~
{\Gamma}_{\widetilde{D}}(W(End_{\widetilde{V}}))$$ are related by the formula $$\widetilde{\lambda}(a) = u {\lambda}(u^{-1} a u) u^{-1}\,, \qquad a\in  End_{\widetilde{V}}\,.$$ **Remark 2.** If $V$ is a trivial vector bundle $L_1$ of rank $N=1$ then the isomorphism ${\lambda}$ ([\[la\]](#la){reference-type="ref" reference="la"}) gives a star-product $*$ in the algebra of functions $C({\cal M})(({\hbar}))$ . Due to the result of P. Xu [@Xu], any star-product in $C({\cal M})(({\hbar}))$ is equivalent to the one obtained via Fedosov's procedure[^1]. In particular, the cohomology class of the Fedosov-Weyl curvature ([\[Weyl-c\]](#Weyl-c){reference-type="ref" reference="Weyl-c"}) is a well-defined characteristic class of a star-product in $C({\cal M})(({\hbar}))$. This characteristic class is referred to as *the Deligne-Fedosov class*.

Let us prove here an important technical lemma which might as well have an independent interest

::: lem
[]{#Tech label="Tech"} Let $V$ be a vector bundle over the symplectic manifold ${\cal M}$ and $D$ be a Fedosov connection ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) with the form $r = A + dx^i {\omega}_{ij}(x)y^j$ satisfying the normalization condition ([\[norm\]](#norm){reference-type="ref" reference="norm"}). If $q\in End_V$ is an endomorphism of $V$ then $${\partial}^V q =0 \quad \Rightarrow \quad D q=0\,.$$ In other words, if $q$ is ${\partial}^V$-flat then the isomorphism ${\lambda}$ ([\[la\]](#la){reference-type="ref" reference="la"}) sends the $q$ to itself.
:::

**Proof.** Since $q$ does not depend on $y's$ and ${\partial}^V q=0$ we have that ${\nabla}q={\delta}q=0\,.$ Hence, $D q= {\hbar}^{-1} [r,q]$ and it suffices to show that the commutator $[r,q]$ is vanishing. Since $D$ is nilpotent $D [r,q] = 0$.

The operator ${\delta}^{-1}$ ([\[del-1\]](#del-1){reference-type="ref" reference="del-1"}) is not a derivation of algebra ${\Omega}^{{\bullet}}(W(End_V))$. However, since $q$ does not depend on $y's$ and ${\delta}^{-1}r=0$, $${\delta}^{-1} [r,q]=0\,.$$ Thus if $\eta =[r,q]\in {\Omega}^1(W(End_V))$ we have $${\delta}\eta = {\nabla}\eta + \frac1{{\hbar}}[r,\eta]\,, \qquad
{\delta}^{-1} \eta=0\,.$$ Therefore, applying ([\[Hodge\]](#Hodge){reference-type="ref" reference="Hodge"}) to $\eta$ we get $$\eta = {\delta}^{-1} ({\nabla}\eta + \frac1{{\hbar}}[r,\eta])\,.$$ The latter equation has the unique vanishing solution since ${\delta}^{-1}$ raises the degree in $y$ . Thus the lemma is proven. $\Box$

[^1]: See paper [@D], in which this result was extended to any smooth affine algebraic symplectic variety.
