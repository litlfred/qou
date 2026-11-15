---
doc_id: arxiv-1608.07308v1
doc_title: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology"
section_id: sec-072-94-differentials-in-affine-charts
section_title: "Differentials in affine charts"
section_number: 9.4
pages: 70-71
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.923
doc_brief: "Flag Hilbert schemes, colored projectors and Khovanov–Rozansky homology — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
[]{#sub:affine diff label="sub:affine diff"}

Recall the affine charts $\mathrm{FHilb}_T \subset \mathrm{FHilb}_n$ defined in Subsection [\[sub:defcharts\]](#sub:defcharts){reference-type="ref" reference="sub:defcharts"}. In each of these, the vector space $\mathbb{C}^n$ is endowed with a preferred basis $e_1,...,e_n$, which more abstractly means that the tautological bundle is trivialized: $$\mathcal{T}_n|_{\mathrm{FHilb}_T} \cong \mathcal{O}\cdot e_1 \oplus...\oplus \mathcal{O}\cdot e_n$$ The basis vectors are indexed by boxes $\square$ in the Young diagram of $T$, and the torus $\mathbb{C}^{*} \times \mathbb{C}^*$ acts on the basis vector $e^\square$ by the character $z_\square= q^at^b$ for any box $\square= (a,b)$. We conclude that: $$\wedge^{\bullet}\mathcal{T}_n^{\vee}|_{\mathrm{FHilb}_T} \cong \wedge(\xi_1,\ldots,\xi_n)$$ where the equivariant weights of the symbols $\xi_\square$ are given by $z_\square^{-1} = q^{-a}t^{-b}$. Recall from Subsection [\[sub:sections schemes\]](#sub:sections schemes){reference-type="ref" reference="sub:sections schemes"} that to any polynomial $f\in \mathbb{C}[x,y]$, we may associate a section of the tautological bundle given by: $$\label{eqn:diff chart}
s_f|_{(X,Y,v)} = f(X,Y)v \in \mathcal{T}_n|_{(X,Y,v)}$$ We may dualize the above section to obtain $s_f:\mathcal{T}_n^\vee \rightarrow \mathcal{O}$, and in local coordinates this takes the form: $$\label{eqn:dual diff chart}
s_f(\xi_i)=[f(X,Y)v]_{i} = f(X,Y)_{i1}$$ The local rings of the dg scheme $\mathrm{Tot}_{\mathrm{FHilb}_n^\emph{dg}} (\mathcal{T}_n[1],s_f)$ is then given by the Koszul complex associated with the first column of the matrix $f(X,Y)$.

::: lemma
Suppose that $f=x^Ny^M$ and the diagram of $T$ contains the box with coordinates $(N,M)$. Then the dg algebra $\wedge_{\mathrm{FHilb}_n^\emph{dg}} (\mathcal{T}_n^\vee,s_f)$ is contractible in the local chart $\mathring{\mathrm{FHilb}}_T$.
:::

::: proof
*Proof.* Suppose that $\square= (N,M)$in $T$. Using [\[eqn:chartx\]](#eqn:chartx){reference-type="eqref" reference="eqn:chartx"}--[\[eqn:charty\]](#eqn:charty){reference-type="eqref" reference="eqn:charty"}, one can prove that $(X^NY^M)(v)\in e_\square+ \mathfrak{m}_T$, where $\mathfrak{m}_T$ is the maximal ideal in the local ring $\mathring{\mathcal{A}}_T = \mathbb{C}[\mathring{\mathrm{FHilb}}_T]$. Therefore, $s_f(\xi_\square)=1$ is invertible in [\[eqn:dual diff chart\]](#eqn:dual diff chart){reference-type="eqref" reference="eqn:dual diff chart"}, and this implies that the Koszul complex of $s_f$ is contractible. ◻
:::

::: corollary
[]{#cor: kill projectors label="cor: kill projectors"} Suppose that the diagram of $T$ has more than $N$ columns. Then the homology of the categorified projector $\mathcal{P}_T$ with respect to $d_N$ vanishes.
:::

::: remark
In [@Becker Theorem 4] it is proved that $(B_w,d_N)\cong 0$, if the Robinson-Shensted tableau of $w$ has more than $N$ columns. One can prove that Soergel bimodules $B_w$ with this property generate a tensor subcategory of $\mathrm{SBim}_n$, and all categorified projectors $\mathcal{P}_T$ belong to this subcategory, provided that $T$ has more than $N$ columns. Therefore $(\mathcal{P}_T,d_N)\cong 0$ in agreement with Corollary [\[cor: kill projectors\]](#cor: kill projectors){reference-type="ref" reference="cor: kill projectors"}.
:::

For $T=(1,\ldots,1)$, the differential corresponding to $x^N$ can be written very explicitly.

::: proposition
In the chart $\mathring{\mathrm{FHilb}}_{(1,\ldots,1)}$ the differential $d_N$ is given by the equation $$\label{eqn:dN}
d_N(\xi_1+z\xi_2+\ldots+z^{n-1}\xi_{n-1})=(u_1+zu_2+\ldots+z^{n-1}u_{n})^{N}\ \mod z^n,$$ where $u_1,\ldots,u_n$ are local coordinates and $z$ is a formal parameter.
:::

::: proof
*Proof.* Indeed, in the chart $\mathring{\mathrm{FHilb}}_{(1,\ldots,1)}$ one has $X=u_1+Bu_2+\ldots+B^{n-1}u_n$, where $B$ is the $n\times n$ Jordan block. Clearly, $B^n=0$ and the first column of $X^N$ contains first $n$ coefficients of the polynomial $(u_1+zu_2+\ldots+z^{n-1}u_{n})^{N}$. ◻
:::

As a corollary, we get the following result.

::: proposition
Assuming Conjecture [\[conj:differentials\]](#conj:differentials){reference-type="ref" reference="conj:differentials"}, the $\mathfrak{sl}_N$ homology of the $n$-th symmetric categorified Jones-Wenzl projector is isomorphic to the Koszul homology of the differential [\[eqn:dN\]](#eqn:dN){reference-type="eqref" reference="eqn:dN"}.
:::

This description of $d_N$ indeed agrees with the ones in [@GL; @GOR; @GORS], and the homology is quite involved. Indeed, its Poincaré series for $n\to\infty$ deforms the character of the $(2,2N+1)$ minimal model for the Virasoro algebra. Extensive computer experiments [@GL; @GOR] support this conjecture for $N=2$ and $N=3$. See also [@Hog2] for recent developments for $N=2$.

The homology of all projectors on two and three strands with respect to $d_N$ were described in [@GL]. One can check that they agree with the general framework of this paper.
