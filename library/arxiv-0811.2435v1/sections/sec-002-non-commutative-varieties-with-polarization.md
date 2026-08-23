---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations"
section_id: sec-002-non-commutative-varieties-with-polarization
section_title: "Non-commutative varieties with polarization"
section_number: null
pages: 5-9
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic Donaldson-Thomas invariants and cluster transformations — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
AllA∞-categories in this paper will be ind-constructible. This r oughly means
that their spaces of objects are countable inductive limits of constructible
sets (for more details see Section 3). We deﬁne a non-commutative proper
algebraic variety over a base ﬁeld k as an Ext-ﬁnite ind-constructible k-
linear triangulated A∞-categoryC. For two objects E and F we denote by
Hom•(E,F ) the complex of morphisms and by Ext •(E,F ) its cohomology.
Here are few examples of such categories.
Example 1 a) A∞-version of Db(X), the bounded derived category of the
category of coherent sheaves on a smooth projective algebra ic variety X/k. In
this case Db(X) coincides with the triangulated category Perf (X) of perfect
complexes on X.
b) More generally, for a (not necessarily proper) smooth var iety X en-
dowed with a closed proper subset X0⊂ X, the corresponding triangulated
category is the full subcategory of Perf (X) consisting of complexes of sheaves
with cohomology supported on X0.
c) Also for a (not necessarily proper) smooth variety X we can consider
the the full subcategory of Perf (X) consisting of complexes of sheaves with
compactly supported cohomology.
d) The A∞-version of the category Perf (X) of perfect complexes on a
proper, not necessarily smooth scheme X over k.
e) If A is an A∞-algebra with ﬁnite-dimensional cohomology then C =
Perf (A) is the category of perfect A-modules.
f ) If k is the ﬁeld of characteristic zero and A is ﬁnitely generated in the
sense of [71], (in particular it is homologically smooth, se e [42]) then C is the
category of A-modules of ﬁnite dimension over k.
g) If the category C is ind-constructible and E∈Ob(C) then left and right
orthogonal to the minimal triangulated subcategory genera ted by E are also
ind-constructible (since the conditions Ext•(X,E ) = 0 and Ext•(E,X ) = 0
are “constructible”).
Let us make few comments on the list. Example a) is a particula r case of
examples b),c),d). Using the results of [7] we can reduce geo metric examples
b),d) to the algebraic example e), and also the example c) to t he example
f). Let us discuss a typical (and most important) example e) a t the level
of objects of the category. We claim that the set of isomorphi sm classes
of objects of C can be covered by an inductive limit of constructible sets.
5
First, replacing A by its minimal model we may assume that A is ﬁnite-
dimensional. Basic examples of perfect A-modules are direct sums of shifts
of A, i.e. modules of the type
M =A[n1]⊕A[n2]⊕···⊕ A[nr], r /greaterorequalslant0
and their “upper-triangular deformations” (a.k.a. twiste d complexes). The
latter are described by solutions to the Maurer-Cartan equa tions
∑
1≤l≤r−1
ml(α,...,α ) = 0
where α = (aij)i<j is an upper-triangular r×r matrix with coeﬃcients in A
and degaij =ni−nj + 1.
This gives a closed scheme. For a point x of this scheme we have the
corresponding A∞-module Mx overA. In order to describe all other objects
ofPerf (A) we need to take direct summands (up to homotopy) of such mod-
ulesMx. The set of such summands is parametrized by all A∞-morphisms of
the non-unital algebra P = k·p with the product given by p2 =p (and with
the trivial diﬀerential) to End •(Mx). Every such morphism is described by
a collection of linear maps fn : P⊗n→ End1−n(Mx) satisfying a system of
polynomial equations. Notice that if n is large then fn = 0 because the cor-
responding negative graded components of End •(Mx) are trivial. Therefore
we again have a ﬁnite system of polynomial equations.
For givenN =∑
1≤j≤r(|nj| + 1) we obtain a scheme of ﬁnite type ModN
parametrizing some objects of Perf (A). Clearly Ob(Perf (A)) =∪N /greaterorequalslant1ModN .
Each isomorphism class of an object appears in the union for i nﬁnitely many
values of N. In order to avoid the “overcounting” we deﬁne a subscheme of
ﬁnite type Mod 0
N ⊂ ModN consisting of objects not isomorphic to objects
from ModN ′ for N′ < N. We conclude that objects of Perf (A) form an
ind-constructible set (more precisely, an ind-constructi ble stack). One can
take care about morphisms in the category in a similar way. Th is explains
the example e).
We deﬁne a polarization on a non-commutative proper algebraic variety
over k (a version of Bridgeland stability condition, see [9]) by th e following
data and axioms:
• an ind-constructible homomorphism cl : K0(C)→ Γ, where Γ ≃ Zn
is a free abelian group of ﬁnite rank endowed with a bilinear f orm3
3 In physics literature Γ is called the charge lattice.
6
⟨•,•⟩: Γ ⊗ Γ → Z such that for any two objects E,F ∈Ob(C) we have
⟨cl(E), cl(F )⟩=χ(E,F ) :=
∑
i
(−1)i dim Exti(E,F ) ,
• an additive map Z : Γ → C, called the central charge,
• a collectionCss of (isomorphism classes of) non-zero objects in C called
the semistable ones, such that Z(E)⁄= 0 for any E∈C ss, where we
write Z(E) for Z(cl(E)),
• a choice Log Z(E)∈ C of the logarithm of Z(E) deﬁned for any E∈
Css.
Making a connection with [9] we say that the last three items d eﬁne a
stability structure (or stability condition) on the category C.
ForE∈C ss we denote by Arg( E)∈ R the imaginary part of Log Z(E).
The above data satisfy the following axioms:
• for all E∈C ss and for all n∈ Z we have E[n]∈C ss and
ArgZ(E[n]) = Arg Z(E) +πn ,
• for all E1,E 2∈C ss with Arg(E1)> Arg(E2) we have
ExtC
≤0 (E1,E 2) = 0 ,
• for any object E∈Ob(C) there exist n /greaterorequalslant0 and a chain of morphisms
0 = E0→E1→···→ En =E (an analog of ﬁltration) such that the
corresponding “quotients” Fi := Cone(Ei−1→ Ei), i = 1,...,n are
semistable and Arg(F1)> Arg(F2)>··· > Arg(Fn),
• for each γ∈ Γ \{ 0} the set of isomorphism classes of a Css
γ ⊂Ob(C)γ
consisting of semistable objects E such that cl(E) = γ and Arg(E) is
ﬁxed, is a constructible set,
• (Support Property) Pick a norm‖·‖on Γ⊗R, then there exists C >0
such that for all E∈C ss one has‖E‖≤C|Z(E)|.
7
In the above deﬁnition one can allow Γ to have a torsion. In geo metric
examples a), d) for k = C one can take Γ = K 0
top(X(C)) where K 0
top denotes
the topological K 0-group. Similarly, in examples b),c) one should take the
K 0-groups with appropriate supports. Another choice for Γ is t he image of
the algebraic K 0-group under the Chern character. Yet another choice is
Γ = Knum
0 (C), which is the quotient of the group K0(C) by the intersection
of the left and right kernels of the Euler form χ(E,F ). Finally one can pick
a ﬁnite collection of ind-constructible functors Φ i :C→ Perf (k), 1≤i≤n
and deﬁne
cl(E) = (χ(Φ 1(E)),...,χ (Φ n(E)))∈ Zn =: Γ ,
whereχ :K0(Perf (k))→ Z is the isomorphism of groups given by the Euler
characteristic.
Remark 1 The origin of the Support Property is geometric and can be ex-
plained in the case of the category of A-branes (the derived Fukaya category
Db(F (X))) of a compact 3-dimensional Calabi-Yau manifold X. Let us ﬁx
a Calabi-Yau metric g0 on X. Asymptotically, in the large volume limit (as
the rescaled symplectic form approaches inﬁnity) it gives r ise to the stability
condition on Db(F (X)) such that stable objects are special Lagrangian sub-
manifolds, and |Z(L)| is the volume of L with respect to g0. Then for any
harmonic form η one has |
∫
Lη|≤ C|Z(L)|. It follows that the norm of the
cohomology class of L is bounded (up to a scalar factor) by the norm of the
linear functional Z.
The Support Property implies that the set {Z(E)∈ C|E∈C ss} is a
discrete subset of C with at most polynomially growing density at inﬁnity.
It also implies that the stability condition is locally ﬁnit e in the sense of
Bridgeland (see [9]). Any stability condition gives a bound ed t-structure
onC with the corresponding heart consisting of semistable obje cts E with
Arg(E)∈ (0,π ] and their extensions.
Remark 2 The case of the classical Mumford notion of stability with re spect
to an ample line bundle (and its reﬁnement for coherent sheav es deﬁned by
Simpson) is not an example of the Bridgeland stability condi tion, it is rather
a limiting degenerate case of it (see [1], [73] and Remark at t he end of Section
2.1).
8
For givenC and a homomorphism cl : K0(C)→ Γ as above, let us denote
byStab(C) := Stab(C, cl) the set of stability conditions (Z,Css, (LogZ(E))E∈Css).
Space Stab(C) can be endowed with a Hausdorﬀ topology, which we discuss
in detail in Section 3.4. Then we have an ind-constructible v ersion of the
following fundamental result of Bridgeland (see [9]).
Theorem 1 The forgetting map Stab(C) → Cn ≃ Hom(Γ, C) given by
(Z,Css, (LogZ(E))E∈Css)↦→Z, is a local homeomorphism.
Hence, Stab(C) is a complex manifold, not necessarily connected. Under
appropriate assumptions one can show also that the group of a utoequiva-
lences Aut(C) acts properly and discontinuously on Stab(C). On the quo-
tient orbifold Stab(C)/ Aut(C) there is a natural non-holomorphic action of
the group GL+(2, R) of orientation-preserving R-linear automorphisms of
R2≃ C.
