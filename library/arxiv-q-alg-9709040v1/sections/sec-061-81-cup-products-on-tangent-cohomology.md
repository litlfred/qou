---
doc_id: arxiv-q-alg-9709040v1
doc_title: "Deformation quantization of Poisson manifolds"
section_id: sec-061-81-cup-products-on-tangent-cohomology
section_title: "Cup-products on tangent cohomology"
section_number: 8.1
pages: 36-37
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
toc_source: inferred
doc_brief: "Deformation quantization of Poisson manifolds — 75 sections: Front matter; Plans; Star-products"
---
Diﬀerential graded Lie algebras Tpoly, Dpoly and (more generally) shifted by [1] Hochschild complexes of
arbitrary associative algebras, all carry an additional structure. We do not know at the moment a deﬁnition,
it should be something close to so called homotopy Gerstenhaber algebras (see [GV], [GJ]), although deﬁnitely
not precisely this. At least, a visible part of this structure is a commutative associative product of degree
+2 on cohomology of the tangent space to any solution of the Maurer-Cartan equation. Namely, if g is
one of diﬀerential graded Lie algebras listed above and γ ∈(g ⊗m)1 satisﬁes dγ + 1
2[γ, γ] = 0 where m
is a ﬁnite-dimensional nilpotent non-unital diﬀerential graded commutative associative algebra, the tangent
space Tγ is deﬁned as complex γ ⊗m[1] endowed with the diﬀerential d+[γ, ·]. Cohomology space Hγ of this
diﬀerential is a graded module over graded algebra H(m) (the cohomology space of m as a complex). If γ1
and γ2 are two gauge equivalent solutions, then Hγ1 and Hγ2 are (non-canonically) equivalent m-modules.
We deﬁne now cup-products for all three diﬀerential graded Lie algebras listed at the beginning of this
section. For Tpoly(X) the cup-product is deﬁned as the usual cup-product of polyvector ﬁelds (see 4.6.1).
One can check directly that this cup-product is compatible with the diﬀerential d + [γ, ·], and is a graded
commutative associative product. For the Hochschild complex of an associative algebra A the cup-product
on Hγ is deﬁned in a more tricky way. It is deﬁned on the complex by the formula
(t1 ∪t2)(a0 ⊗. . . ⊗an) :=
X
0≤k1≤k2≤k3≤k4≤n
±γn−(k2−k1+k4−k3)(a0 ⊗. . . ⊗t1(ak1 ⊗. . .) ⊗ak2 ⊗. . . ⊗t2(ak3 ⊗. . .) ⊗ak4 ⊗. . .)
36
where γl ∈(k[0] · 1 ⊕m)1−l ⊗Hom(A⊗(l+1), A) is homogeneous component of (γ + 1 ⊗mA).
It is not a trivial check that the cup-product on the Hochschild complex is compatible with diﬀerentials,
and also is commutative, associative and gauge-equivariant on the level of cohomology. Formally, we will
not use this fact. The proof is a direct calculation with Hochschild cochains. Even if one replaces formulas
by appropriate pictures the calculation is still quite long, about 4-5 pages of tiny drawings. Alternatively,
there is a simple abstract explanation using the interpretation of the deformation theory related with the
shifted Hochschild complex as a deformation theory of triangulated categories (or, better, A∞-categories,
see [Ko4]). We will discuss it in more details in the sequel to the present paper.
We deﬁne the cup-product for Dpoly(X) by the restriction of formulas for the cup-product in C•(A, A).
