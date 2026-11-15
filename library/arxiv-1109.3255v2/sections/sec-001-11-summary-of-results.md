---
doc_id: arxiv-1109.3255v2
doc_title: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE"
section_id: sec-001-11-summary-of-results
section_title: "Summary of results"
section_number: 1.1
pages: 2-5
source_pdf: 1109.3255v2.pdf
source_sha256: dd4579be8e9b7e25
toc_source: outline
text_source: latex
latex_prose_ratio: 0.972
latex_coverage_ratio: 0.986
doc_brief: "FLOER COHOMOLOGY IN THE MIRROR OF THE PROJECTIVE PLANE AND A BINODAL CUBIC CURVE — We construct a family of Lagrangian submanifolds in the Landau– Ginzburg mirror to the projective plane equipped"
---
[]{#sec:outline label="sec:outline"} The piece of symplectic geometry in the Landau--Ginzburg model $(X^\vee,W)$ we study is the Floer cohomology of Lagrangian submanifolds, while on the mirror side $\CP^2$ we consider the cohomology of the coherent sheaves $\cO_{\CP^2}(d)$. We construct a symplectic manifold $X(B)$, that serves as our symplectic model for $X^\vee$, and a collection of Lagrangian submanifolds $\{L(d)\}_{d\in
  \Z}$ in $X(B)$ that is mirror to the collection $\{\cO_{\CP^2}(d)\}_{d\in \Z}$. The constructions of $X(B)$ and $L(d)$ are based on the SYZ picture of mirror symmetry in terms of torus fibrations and affine manifolds, and also use the theory of Lefschetz fibrations. The manifold $X(B)$ carries two fibrations: one is a fibration over a singular affine manifold $B$ whose fibers are Lagrangian tori, while the other is a Lefschetz fibration whose fibers are symplectic submanifolds. See section [\[sec:main-construction\]](#sec:main-construction){reference-type="ref" reference="sec:main-construction"} for the definitions.

To state the main result, let $A_n = H^0(\CP^2,\cO_{\CP^2}(n))$, and choose a basis $x,y,z$ of $A_1$. Thus $A = \bigoplus_{n=0}^\infty A_n
\cong \C[x,y,z]$ is the homogeneous coordinate ring of $\CP^2$. The Floer cohomology of two Lagrangian submanifolds $L,L'$ is a $\Z$-graded $\C$-vector space denoted $HF^*(L,L')$.

::: theorem
[]{#thm:triangle-products label="thm:triangle-products"} For each $d \in \Z$ and $n \geq 0$, there is an isomorphism $$\psi_{d,n} : HF^0(L(d),L(d+n)) \to A_n$$ carrying the basis of intersection points $L(d) \cap L(d+n)$ to the basis of $A_n$ consisting of the polynomials of the form $$\{x^a(xz-y^2)^iy^{n-a-2i}\} \cup
    \{z^a(xz-y^2)^iy^{n-a-2i}\}$$ (where we require $a \geq 0, i \geq 0, n-a-2i \geq 0$). The system of isomorphisms $\psi_{d,n}$ intertwines the Floer triangle product $$\mu^2: HF^0(L(d+n),L(d+n+m)) \otimes HF^0(L(d),L(d+n)) \to HF^0(L(d),L(d+n+m))$$ and the product of polynomials $A_m \otimes A_n \to A_{n+m}$.
:::

Let us remark on the formulation of the theorem. From the construction of the Lagrangians $L(d)$ it is easy to count the number of intersection points and show that the map $\psi_{d,n}$ exists as an isomorphism of vector spaces. Such a map exists for any choice of basis of $A_n$. The last statement equating Floer triangle products and the products of polynomials is the nontrivial bit that ties the choices together and shows that we have chosen the right basis for $A_n$.

This basis we obtain is related to the choice of divisor $D = C\cup L$, as it consists of monomials in the defining section $p =xz-y^2$ of $C$, the defining section $y$ of $L$, and the homogeneous variables $x$ or $z$ (but not both $x$ and $z$ in the same monomial). Another point of view has to do with the fact that the ring of functions on $\CP^2\setminus D$ is a cluster algebra [@fomin-zelevinsky-I]. There are two triples of homogeneous forms on $\CP^2$, $(x,p,y)$ and $(z,p,y)$, which are related by the so-called exchange relation $xz = y^2 + p$, and our basis consists of sections that are monomials in either triple.

For the proof of this theorem, the majority of our technical efforts are aimed at computing the Floer triangle product. This occupies section [\[sec:degeneration\]](#sec:degeneration){reference-type="ref" reference="sec:degeneration"}. At this point in the argument, the picture of $X(B)$ as a Lefschetz fibration is the focus. The holomorphic triangles we need to find can be represented as sections of this Lefschetz fibration. The problem of counting sections of Lefschetz fibrations has a TQFT-type structure, developed by Seidel. This structure, where one breaks a given problem into simpler ones by degenerating the base of the Lefschetz fibration, provides the basis of our technique.

There are several variations on Theorem [\[thm:triangle-products\]](#thm:triangle-products){reference-type="ref" reference="thm:triangle-products"} that are accessible using the same holomorphic curve analysis. We consider the complement of (some components of) the anticanonical divisor in $\CP^2$, and on the Landau--Ginzburg side, we must change the superpotential $W$ and consider a certain form of wrapped Floer cohomology. Our techniques allow us to treat three cases:

1.  the mirror of $(\CP^2 \setminus L, C \setminus (C\cap L))$,

2.  the mirror of $(\CP^2 \setminus C, L \setminus (L\cap C))$, and

3.  the mirror of $(\CP^2 \setminus (C\cup L), \emptyset)$.

In each case the mirror space is the same manifold $X^\vee$, and the Lagrangians mirror to line bundles are the same $L(d)$, but in each case there is a different prescription for wrapping the Lagrangian submanifolds. The first two cases require "partially wrapped" Floer cohomology, while the third uses the more standard "fully wrapped" Floer cohomology. In each case we denote wrapped Floer cohomology by $HW^*(L_1,L_2)$. Let $U = \CP^2 \setminus L$, $\CP^2 \setminus C$, or $\CP^2 \setminus (C\cup L)$, and let $A_n(U) = H^0(U,\cO_U(n))$. The space $A_n(U)$ consists of rational functions in the variables $x,y,z$ that are regular on $U$ and have degree $n$. The wrapped version of Theorem [\[thm:triangle-products\]](#thm:triangle-products){reference-type="ref" reference="thm:triangle-products"} is as follows (see §[\[sec:complements\]](#sec:complements){reference-type="ref" reference="sec:complements"})

::: theorem
[]{#thm:wrapped-products label="thm:wrapped-products"}

For $d \in \Z$ and $n \geq 0$, there is an isomorphism $$\psi_{d,n} : HW^0(L(d),L(d+n)) \to A_n(U)$$ carrying a certain distinguished basis of $HW^0(L(d),L(d+n))$ to the basis of $A_n(U)$ consisting of rational functions of the form $$\{x^a(xz-y^2)^iy^{n-a-2i}\} \cup
    \{z^a(xz-y^2)^iy^{n-a-2i}\}$$ where the exponents $a$ and $i$ are restricted to those values which actually give elements of $A_n(U)$. The system of isomorphisms $\psi_{d,n}$ intertwines the Floer triangle product on wrapped Floer cohomology and the product of rational functions $A_m(U) \otimes A_n(U) \to
  A_{n+m}(U)$.
:::

While our holomorphic triangle counts use the structure of a Lefschetz fibration on $X(B)$, we can also study the geometry of the $X(B)$ as a Lagrangian torus fibration over the base affine manifold $B$. One of the expectations of SYZ philosophy is that much of the geometry of the space $X(B)$ can be seen tropically, in terms of the geometry of the affine base $B$.

In fact, this is how we arrive at the construction of the manifold $X(B)$. In section [\[sec:fiber-superpotential\]](#sec:fiber-superpotential){reference-type="ref" reference="sec:fiber-superpotential"}, we construct a tropicalization of the fiber of the superpotential $W^{-1}(c)$ over a large positive real value, with respect to a torus fibration on the manifold $X^\vee$ with a single singularity. This gives a tropical curve in the base of our torus fibration. It bounds a compact region $B$ in the base, which agrees with the affine base of the torus fibration on $\CP^2\setminus D$. The purpose of this section is to motivate the use of the singular affine manifold $B$ as the basis for our main symplectic constructions in section [\[sec:main-construction\]](#sec:main-construction){reference-type="ref" reference="sec:main-construction"}.

We also are able to verify a conjectural tropical description of Floer cohomology in the cases we study. This description comes from a recent proposal of Abouzaid, Gross and Siebert for a tropical Fukaya category associated to a singular affine manifold. The Lagrangian submanifolds are taken to be sections of the torus fibration, but all we see of them tropically are their intersection points, which map to fractional integral points of the affine manifold $B$. The Floer triangle product corresponds to a "tropical triangle product" counting certain tropical curves in $B$ joining the fractional integral points. Since we do not say anything about degenerating holomorphic polygons to tropical ones, we merely verify the equivalence by matching bases and computing on both sides. See section [\[sec:trop-fuk\]](#sec:trop-fuk){reference-type="ref" reference="sec:trop-fuk"} for the precise definitions of the terms.

::: theorem
[]{#thm:tropical-trangles label="thm:tropical-trangles"} There is a bijection between the basis of intersection points $L(d)\cap L(d+n)$ for $HF^0(L(d),L(d+n))$ and the set of $(\frac{1}{n})$-integral points of the affine manifold $B$. Under this bijection, the counts of pseudo-holomorphic triangles contributing to the Floer triangle product are equal to counts of tropical curves in $B$ joining $(\frac{1}{n})$-integral points.
:::

The techniques developed in this article apply to a larger but still restricted class of $2$--dimensional singular affine manifolds, where the main restriction is that all singularities have *parallel monodromy-invariant directions*. The generalization to these types of manifolds is discussed in [\[sec:other-manifolds\]](#sec:other-manifolds){reference-type="ref" reference="sec:other-manifolds"}.
