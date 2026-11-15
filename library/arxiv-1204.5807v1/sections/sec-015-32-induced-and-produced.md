---
doc_id: arxiv-1204.5807v1
doc_title: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES"
section_id: sec-015-32-induced-and-produced
section_title: "Induced and produced"
section_number: 3.2
pages: 19-20
source_pdf: 1204.5807v1.pdf
source_sha256: 4bf4f73b0c152b19
toc_source: inferred
doc_brief: "FROM HOPF ALGEBRAS TO TENSOR CATEGORIES — This is a survey on spherical Hopf algebras. We give criteria to decide when a Hopf algebra is spherical and collect examples."
---
denote by ResA
B the restriction functor from the category A- Mod to B- Mod.
3.2.1. The induced and produced modules of T ∈B- Mod are
IndA
B T = A⊗BT,
ProA
B T = HomB(A, T).
(3.2)
These are equipped with morphisms of B-modules ι : T֒ →IndA
B T, given
by ι(t) = 1 ⊗t for t ∈T, and π : ProA
B T ։ T, given by π(f) = f(1) for
f ∈HomB(A, T). The following properties are well-known.
(a) HomB(T, ResA
B M) ≃HomA(IndA
B T, M); that is, induction is left
adjoint to restriction.
(b) For every S ∈Irr A there exists T ∈Irr B such that S is a quotient
of IndA
B T.
(c) HomB(ResA
B N, T) ≃HomA(N, ProA
B T); that is, production (also
called coinduction) is right adjoint to restriction.
(d) For every S ∈Irr A there exists T ∈Irr B such that S is a submodule
of ProA
B T.
3.2.2. Assume that A is a ﬁnite B-module. Then ResA
B, IndA
B and ProA
B re-
strict to functors (denoted by the same name) between the categories A- mod
and B- mod of ﬁnite-dimensional modules; mutatis mutandis, the preceding
points hold in this context. Assume also that there exists a contravariant
k-linear functor D : A- mod →A- mod such that D(B- mod) ⊆B- mod and
admits a quasi-inverse E : A- mod →A- mod, so that D is an equivalence of
categories. It follows at once from the universal properties that
IndA
B T ≃D(ProA
B ET) ≃E(ProA
B DT),
(3.3)
ProA
B T ≃D(IndA
B ET) ≃E(IndA
B DT).
(3.4)
Hence D(IndA
B T) ≃ProA
B DT, D(ProA
B T) ≃IndA
B DT, and so on.
In this setting, consider the following conditions:
For every S ∈Irr A, ∃a unique T ∈Irr B such that IndA
B T ։ S.
(3.5)
For every S ∈Irr A, ∃a unique U ∈Irr B such that S֒ →ProA
B U.
(3.6)
The head of IndA
B T is simple for every T ∈Irr B.
(3.7)
The socle of ProA
B U is simple for every U ∈Irr B.
(3.8)
Then (3.5) ⇐⇒(3.6) and (3.7) ⇐⇒(3.8). If all these conditions hold,
then for any T ∈Irr B, there exists a unique U ∈Irr B such that
IndA
B T ։ S֒ →ProA
B U,
where S is the head of IndA
B T and the socle of ProA
B U. We set U = w0(T).
20
ANDRUSKIEWITSCH, ANGIONO, GARCÍA IGLESIAS, TORRECILLAS, VAY
3.2.3. Let K be a Hopf subalgebra of a Hopf algebra H, with H ﬁnite over
K. Then
IndH
K T ≃(ProH
K
∗T)∗≃∗(ProH
K T ∗),
ProH
K T ≃(IndH
K
∗T)∗≃∗(IndH
K T ∗).
If H is pivotal, then these formulae are simpler because the left and right
duals coincide.
3.2.4. Let g be a simple Lie algebra, b a Borel subalgebra and q a root of unity
of odd order, relatively prime to 3 when g is of type G2. Let H = Uq(g) be
the Lusztig’s q-divided power quantized enveloping algebra and K = Uq(b).
Let C be the category of ﬁnite-dimensional H-modules of type 1, see [APW],
and Cb the analogous category of K-modules. Then there are induced and
produced functors IndH
K, ProH
K : Cb →C. Then the Weyl and dual Weyl
modules are the produced and induced modules of the simple objects in
Cb, parameterized conveniently by highest weights.
This allows to deﬁne
Weyl and dual Weyl ﬁltrations and tilting modules; instead of appealing to
Theorem 3.3, one establishes the semisimplicity of the category of tilting
modules by establishing crucial cohomological results, see [AP] for details.
