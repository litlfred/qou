---
doc_id: arxiv-math-0408210v3
doc_title: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM"
section_id: sec-005-22-the-chern-weil-homomorphism
section_title: "The Chern-Weil homomorphism"
section_number: 2.2
pages: 5-9
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
doc_brief: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM — In math.QA/0311303 B. Feigin, G. Felder, and B."
text_source: latex
latex_prose_ratio: 0.748
latex_coverage_ratio: 0.968
---
Let ${\mathfrak{g}}$ be a Lie algebra and ${\mathfrak{h}}\subset{\mathfrak{g}}$ be a subalgebra of ${\mathfrak{g}}$. Suppose that there is an ${\mathfrak{h}}$-equivariant projection $pr\,:\,{\mathfrak{g}}\mapsto {\mathfrak{h}}$, that is a map commuting with the adjoint action of ${\mathfrak{h}}$ and satisfying the property $\displaystyle pr\, |_{{\mathfrak{h}}} = Id_{{\mathfrak{h}}}\,.$ The amount by which $pr$ fails to be a Lie algebra homomorphism is measured by the "curvature" $C\in Hom(\wedge^2 {\mathfrak{g}}, {\mathfrak{h}})$ $$\label{curvature}
C(v,w)= [pr(v), pr(w)]- pr ([v,w])\,,
\qquad v,w \in {\mathfrak{g}}\,.$$

Given the "curvature" ([\[curvature\]](#curvature){reference-type="ref" reference="curvature"}) of the ${\mathfrak{h}}$-equivariant projection $pr$, it is not hard to see that for any adjoint invariant form $Q\in ((S^j{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ the formula $$\label{Ch-W}
\chi(Q)(v_1, \dots, v_{2j}) =
\frac1{(2j)!} \sum_{\nu\in S_{2j}}
(-)^{\nu} Q(C(v_{\nu(1)}, v_{\nu(2)}), \dots,
C(v_{\nu(2j-1)}, v_{\nu(2j)}))$$ defines a relative Lie algebra cocycle $\chi(Q)\in C^{2j}({\mathfrak{g}},{\mathfrak{h}})$. The standard argument of the theory of characteristic classes shows that the cohomology class $[\chi(Q)]$ of the cocycle $\chi(Q)$ does not depend on the choice of the projection $pr$. Thus ([\[Ch-W\]](#Ch-W){reference-type="ref" reference="Ch-W"}) induces a map from the vector space $((S^j{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ to $H^{2j}({\mathfrak{g}}, {\mathfrak{h}})$. The latter map is called the *Chern-Weil homomorphism*.

In our case we set ${\mathfrak{g}}={\mathfrak{gl}}_N({\cal W})$, ${\mathfrak{h}}={\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$ and define the projection $pr$ from ${\mathfrak{g}}$ to ${\mathfrak{h}}$ by the formula $$\label{pr}
pr(v)= pr_0(v) + pr_2 (v)\,,$$ $$pr_0(v)= v\Big|_{y=0}\,, \qquad
pr_2(v)= \frac1{N}{\sigma}_2(tr (v)) I_{N}\,,$$ where ${\sigma}_2$ denotes the projection onto the monomials of the second degree in $y$'s, $tr$ is the ordinary matrix trace, $I_N$ is the identity matrix of size $N\times N$, and the Lie algebra ${\mathfrak{sp}}_{2n}$ is realized as a subalgebra of scalar matrices in ${\mathfrak{gl}}_N({\cal W})$ with values in quadratic monomials in ${\cal W}$ .

Due to [@FFS] we have the following

::: teo
The Lie algebra cocycle $\Theta^N_{2n}\in
C^{2n}({\mathfrak{g}},{\mathfrak{g}}^*)$ is relative with respect to the subalgebra ${\mathfrak{h}}={\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$. The evaluation of ([\[Te\]](#Te){reference-type="ref" reference="Te"}) on the identity matrix $I_N\in {\mathfrak{g}}$ gives a relative Lie algebra cocycle $${\varphi}\in C^{2n}({\mathfrak{g}}, {\mathfrak{h}})$$ $${\varphi}= \Theta^N_{2n}(\cdot ,\dots, \cdot, I_N)\,:\,
\wedge^{2n}({\mathfrak{g}}) \mapsto {\Bbb C}(({\hbar}))$$ whose cohomology class $$\label{FFS}
[{\varphi}\,]=[\chi (Q_n)]\,,$$ coincides with the image of the $n$-th component $Q_n\in ((S^n{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ of the adjoint invariant form $Q\in ((S{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ $$\label{Qn}
Q(X,\dots, X)= \det\Big( \frac{X_1/2{\hbar}}{sinh\,(X_1/2{\hbar})}
\Big)^{1/2} tr\, \exp\left(\frac{X_2}{{\hbar}}\right)\,,$$ $$X= X_1\oplus X_2 \in {\mathfrak{sp}}_{2n} \oplus {\mathfrak{gl}}_N$$ under the Chern-Weil homomorphism ([\[Ch-W\]](#Ch-W){reference-type="ref" reference="Ch-W"}).
:::

## Fedosov deformation quantization with twisted coefficients.

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

## The Feigin-Felder-Shoikhet trace density map.

Let as above $V$ be a vector bundle of rank $N$ over the symplectic manifold ${\cal M}$ and $*$ be a star-product ([\[star\]](#star){reference-type="ref" reference="star"}) in the algebra $End_V(({\hbar}))$ . Then,

::: defi
A trace density map $trd$ is a ${\Bbb C}(({\hbar}))$-linear map $$trd\,:\, End_V(({\hbar})) \mapsto H^{2n}({\cal M})(({\hbar}))$$ vanishing on commutators $$trd(a * b - b * a)=0\,,
\qquad a,b \in End_V(({\hbar}))\,.$$
:::

We will show that if the star-product $*$ in $End_V(({\hbar}))$ is obtained via the Fedosov procedure [@F1] then the Feigin-Felder-Shoikhet cocycle ([\[Te\]](#Te){reference-type="ref" reference="Te"}) provides us with a natural trace density map.

Let as above $D$ be the Fedosov connection ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) and ${\lambda}$ be the isomorphism ([\[la\]](#la){reference-type="ref" reference="la"}). Since $\Theta_{2n}^N$ ([\[Te\]](#Te){reference-type="ref" reference="Te"}) is a cocycle of ${\mathfrak{g}}= {\mathfrak{gl}}_N({\cal W})$ relative to ${\mathfrak{h}}= {\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$ , we have the following well-defined map $$\label{Psi}
\Psi_{D}\,:\, End_V(({\hbar})) \mapsto {\Omega}^{2n}({\cal M})(({\hbar}))\,,
\qquad
\Psi_{D}(a)= \frac1{{\hbar}^n}\Theta^N_{2n} (A,\dots, A,{\lambda}(a))\,,$$ where $A\in {\Omega}^1(W(End_V))$ is the one-form entering the definition of the Fedosov connection $D$ ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) .

We assemble the required properties of the map $\Psi_D$ in the following

::: teo
[]{#main label="main"} With the above notations the following statements hold:\
**i)** If $V_1$ and $V_2$ are two vector bundles over ${\cal M}$ and $D_1,~ D_2$ are Fedosov connections on $W(End_{V_1})$ and $W(End_{V_2})$, respectively, then for any $a\in End_{V_1}$ $$\Psi_{D_1\oplus D_2} (a \oplus 0) = \Psi_{D_1}(a)\,,$$ where $0$ stands for the trivial endomorphism of $V_2$ .\
**ii)** For any pair of endomorphisms $a,b \in End_V(({\hbar}))$ $$\Psi_D(a * b - b * a)\in d {\Omega}^{2n-1}({\cal M})(({\hbar}))\,,$$ where $d$ is the De Rham differential.\
**iii)** Let $D$ and $\widetilde{D}$ be two equivalent Fedosov connections and $U\in I_N \oplus {\Gamma}(W^1(End_V))$ be the element establishing their equivalence in the sense of ([\[equiv1\]](#equiv1){reference-type="ref" reference="equiv1"}). Then for any $a\in End_V(({\hbar}))$ $$\Psi_{\widetilde{D}}({\sigma}(U^{-1}\circ {\lambda}(a)\circ U))
- \Psi_D (a)
\in d {\Omega}^{2n-1}({\cal M})(({\hbar}))\,,$$ where ${\sigma}$ is the projection ([\[sigma\]](#sigma){reference-type="ref" reference="sigma"}) and ${\lambda}$ is the isomorphism ([\[la\]](#la){reference-type="ref" reference="la"}).\
**iv)** For the identity endomorphism $I_N\in End_V$ $$\Psi_D(I_N) - \frac1{{\hbar}^n}Q_n(C(A,A), \dots, C(A,A))
\in d {\Omega}^{2n-1}({\cal M})(({\hbar}))\,,$$ where $Q_n\in ((S^n{\mathfrak{h}})^*)^{{\mathfrak{h}}}$ is the $n$-th component of the adjoint invariant form ([\[Qn\]](#Qn){reference-type="ref" reference="Qn"}), $A\in {\Omega}^1(W(End_V))$ is the one-form entering the definition of the Fedosov connection $D$ ([\[F-conn\]](#F-conn){reference-type="ref" reference="F-conn"}) and $C$ is the fiberwise "curvature" ([\[curvature\]](#curvature){reference-type="ref" reference="curvature"}) of the projection ([\[pr\]](#pr){reference-type="ref" reference="pr"}) .
:::

**Proof.** Statement $i)$ is obvious from the construction of the cocycle $\Theta^N_{2n}$ ([\[phi\]](#phi){reference-type="ref" reference="phi"}), ([\[tau\]](#tau){reference-type="ref" reference="tau"}), ([\[Te\]](#Te){reference-type="ref" reference="Te"}). Statements $ii)$, $iii)$, and $iv)$ are proven in [@FFS] for the case when the bundle $V$ is trivial. Statements $ii)$ and $iii)$ follow from the fact $\Theta^N_{2n}$ is a cocycle relative to ${\mathfrak{h}}= {\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$ and statement $iv)$ is a consequence of ([\[FFS\]](#FFS){reference-type="ref" reference="FFS"}) . These results of [@FFS] are generalized to the non-trivial bundle $V$ in a straightforward manner since we always deal with the Lie algebra cochains relative to ${\mathfrak{h}}= {\mathfrak{gl}}_N\oplus {\mathfrak{sp}}_{2n}$ . $\Box$

As an immediate consequence of this theorem we get that

::: cor
If $*$ is the star-product in $End_V(({\hbar}))$ obtained via the isomorphism ${\lambda}$ ([\[la\]](#la){reference-type="ref" reference="la"}) then $$\label{trd}
trd(a) = [\Psi_D(a)] \,:\,
End_V(({\hbar})) \mapsto H^{2n}({\cal M})(({\hbar}))$$ is a trace density map.
:::

In what follows we refer to ([\[trd\]](#trd){reference-type="ref" reference="trd"}) as the Feigin-Felder-Shoikhet (FFS) trace density map.

[^1]: See paper [@D], in which this result was extended to any smooth affine algebraic symplectic variety.
