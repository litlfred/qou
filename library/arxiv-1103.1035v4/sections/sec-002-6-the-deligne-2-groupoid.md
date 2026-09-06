---
doc_id: arxiv-1103.1035v4
doc_title: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI"
section_id: sec-002-6-the-deligne-2-groupoid
section_title: "The Deligne 2-Groupoid"
section_number: 6
pages: 23-31
source_pdf: 1103.1035v4.pdf
source_sha256: dd5c4660e1d08ea1
doc_brief: "MC ELEMENTS IN PRONILPOTENT DGLIE ALGEBRAS AMNON YEKUTIELI — Consider a pronilpotent DG (differential graded) Lie algebra over a ﬁeld of characteristic 0."
---
5.3 and Proposition 5.5) associated to the action of the group exp (mˆ⊗ g0) on the
collection of groups {Nω}ω∈MC(mˆ⊗ g). The feedback D ω and the twisting Ψ(g)
are speciﬁed in Corollary 6.9.
Proposition 6.12. Consider pairs (g, R) such that Deligne 2-groupoid Del2(g, R) is
deﬁned, i.e. either of the two conditions in Deﬁnition 6.11 holds.
(1) The Deligne 2-groupoid Del2(g, R) depends functorially on g and R.
(2) The reduced Deligne groupoid satisﬁes
Delr(g, R) = π1(Del2(g, R)).
24 AMNON YEKUTIELI
Proof. This is immediate from the constructions. □
Theorem 6.13. Let R be a parameter algebra, let g and h be DG Lie algebras, and let
φ : g→ h be a DG Lie algebra quasi-isomorphism. Assume either of these two conditions
holds:
(i) R is artinian.
(ii) g and h are of quasi quantum type.
Then the morphism of 2-groupoids
Del2(φ, R) : Del2(g, R)→ Del2(h, R)
is a weak equivalence.
Proof. Since
π0(Del2(φ, R)) = π0(Delr(φ, R))
and
π1(Del2(φ, R), ω) = π1(Delr(φ, R), ω)
for all ω∈ MC(mˆ⊗ g), these are bijections by Theorem 4.2.
Next, there is a functorial bijection
(6.14)
exp : H−1(mˆ⊗ g)ω
≃− →
Ker
(
Dω : Nω→ exp(mˆ⊗ g0)
)
= π2(Del2(g, R), ω);
cf. the commutative diagram in the proof of Proposition 6.7. So
π2(Del2(φ, R), ω) = H−1(1mˆ⊗ φ)
is bijective. □
Remark 6.15. It is possible to deﬁne a Deligne 2-groupoid Del2(g, R) even when
both conditions in Deﬁnition 6.11 fail, by taking Nω := exp(ˆaω). However the
function exp in (6.14) might fail to be bijective. Hence, in the situation of Theorem
6.13, the homomorphism π2(Del2(φ, R), ω) might fail to be bijective.
7. L ∞ Morphisms and Coalgebras
We shall use the coalgebra approach to L ∞ morphisms, following [Qu], [Ko2,
Section 4], [Hi2], [CKTB, Section 3.7] and [Ye2, Section 3].
Let us denote by DGLie(K) the category of DG Lie algebras over K, and by
DGCog(K) the category of DG unital cocommutative coalgebras over K. Note
that commutativity here is in the graded (or super) sense. Recall that a unital
coalgebra C has a comultiplication ∆ : C→ C⊗ C, a counit ϵ : C→ K and a unit
1∈ C. The differential d has to be a coderivation of degree 1. The conditions
on the unit are ∆(1) = 1⊗ 1, d (1) = 0 and ϵ(1) = 1 in K. Morphisms in
DGCog(K) are K-linear homomorphisms C→ D respecting ∆, ϵ and 1. We write
C+ := Ker(ϵ).
Let V =⨁
i∈Z Vi be a graded K-module. The symmetric algebra over K of the
graded module V is
Sym(V) =
⨁
i∈N
Symj(V).
Note that we are in the super-commutative setting, so Sym j(V) = ⋀j(V[1])[−j].
We view Sym (V) as a Hopf algebra over K, which is commutative and co-
commutative. The unit is 1 ∈ K = Sym0(V), and the counit is the projection
ϵ : Sym(V)→ K.
MC ELEMENTS 25
The Hopf algebra Sym (V) is bigraded, with one grading coming from the
grading of V, which we call degree. The second grading is called order; by
deﬁnition the j-th order component of Sym (V) is Symj(V). Let us write
Sym+(V) :=
⨁
i≥1
Symj(V) = Ker(ϵ).
The projection Sym (V)→ Sym1(V) is denoted by ln. So for an element c∈
Sym(V), its ﬁrst order term is ln (c). Recall that giving a homomorphism of unital
graded coalgebras Ψ : Sym(V)→ Sym(W) is the same as giving its sequence of
Taylor coefﬁcients{∂jΨ}j≥1, where the j-th Taylor coefﬁcient of Ψ is the K-linear
function
∂jΨ := (ln◦Ψ)|Symj(V) : Symj(V)→ W
of degree 0.
The free graded Lie algebra over the graded K-module V is denoted by
FrLie(V).
There is a functor
C : DGLie(K)→ DGCog(K)
called the bar construction. Given a DG Lie algebra g, the corresponding DG coal-
gebra is C(g) := Sym(g[1]), with a coderivation that encodes both the differential
of g and its Lie bracket. There is another functor
L : DGCog(K)→ DGLie(K)
called the cobar construction. Given a DG coalgebra C, the corresponding DG Lie
algebra is FrLie (C+[−1]), with a derivation that encodes both the differential of
C and its comultiplication. If g∈ DGLie(K) and C∈ DGCog(K), then the set of
graded K-linear homomorphisms Homgr(C, g) is a DG Lie algebra, and there are
functorial bijections
(7.1) Hom DGLie(K)(L(C), g)∼= HomDGCog(K)(C, C(g))∼= MC(Homgr(C, g)).
Thus the functors C and L are adjoint. We denote the adjunction morphisms by
ζg : (L◦ C)(g)→ g
and
θC : C→ (C◦ L)(C).
It is known that the functor C is faithful. Let g and h be DG Lie algebras. By
deﬁnition, an L ∞ morphism Φ : g→ h is a morphism C (g)→ C(h) in DGCog(K).
Let us deﬁne DGLie∞(K) to be the category whose objects are the DG Lie algebras,
and the morphisms are the L ∞ morphisms between them. Composition of L ∞
morphisms is that of DGCog(K). Thus we get a full and faithful functor
C∞ : DGLie∞(K)→ DGCog(K)
whose restriction to DGLie(K) is C.
Take an L∞ morphism Φ : g→ h. Its i-th Taylor coefﬁcient ∂iΦ := ∂i(C∞(Φ))
is a K-linear function
∂iΦ :⋀ig→ h
26 AMNON YEKUTIELI
of degree 1 − i. Writing φi := ∂iΦ, the sequence of functions {φi}i≥1 satisﬁes
these equations:
d
(
φi(γ1∧···∧ γi)
)
−
i
∑
k=1
±φi
(
γ1∧···∧ d(γk)∧···∧ γi
)
=
1
2 ∑
k,l≥1
k+l=i
1
k! l! ∑
σ∈Si
±
[
φk(γσ(1)∧···∧ γσ(k)), φl(γσ(k+1)∧···∧ γσ(i))
]
+ ∑
k<l
±φi−1
(
[γk, γl]∧ γ1∧··· γk
··· γl
···∧ γi
)
.
Here γk∈ g are homogeneous elements, Si is the permutation group of{1, . . . ,i},
and the signs depend only on the indices, the permutations and the degrees of the
elements γk. The signs are written explicitly in [CKTB, Section 3.6]. Conversely,
any sequence{φi}i≥1 of homomorphisms satisfying these equations determines
an L∞ morphism.
Let Φ : g→ h be an L ∞ morphism. The ﬁrst Taylor coefﬁcient ∂1Φ : g→ h
is a homomorphism of complexes of K-modules (forgetting the Lie brackets). If
∂iΦ = 0 for all i≥ 2, then ∂1Φ is a DG Lie algebra homomorphism. If ∂1Φ is a
quasi-isomorphism, then Φ is called an L ∞ quasi-isomorphism.
Lemma 7.2. Let g∈ DGLie(K), and deﬁne C := C(g), ˜g := L(C) and ˜C := C( ˜g).
Consider the coalgebra homomorphisms θC : C→ ˜C and C(ζg) : ˜C→ C. Then
C(ζg)◦ θC = 1C,
the identity automorphism of C.
Proof. This is true for any pair of adjoint functors; see [Ma, Section IV .1 Theorem
1]. □
Lemma 7.3. Let Φ : g→ h be an L∞ quasi-isomorphism. Then
(L◦ C∞)(Φ) : (L◦ C)(g)→ (L◦ C)(h)
is a DG Lie algebra quasi-isomorphism.
Proof. Let us write C := C(g), D := C(h) and Ψ := C∞(Φ). Put on C the
ascending ﬁltration FjC := ⨁j
k=0 Symk(g[1]); so that {FjC}j≥0 is an admissible
coalgebra ﬁltration, in the sense of [Hi2, Deﬁnition 4.4.1]. Likewise there is an
admissible coalgebra ﬁltration {FjD}j≥0 on D. According to step 2 of the proof
of [Hi2, Proposition 4.4.3], the coalgebra homomorphism Ψ is a ﬁltered quasi-
isomorphism. Hence by [Hi2, Proposition 4.4.4] the DG Lie algebra homomor-
phism (L◦ C∞)(Φ) = L(Ψ) is a quasi-isomorphism. □
8. L ∞ Quasi-isomorphisms between Pronilpotent Algebras
Let (R, m) be a parameter K-algebra, and let Φ : g→ h be an L ∞ morphism
between DG Lie algebras. Then Φ extends uniquely to an R-multilinear L∞ mor-
phism
ΦR : Rˆ⊗ g→ Rˆ⊗ h,
whose i-th Taylor coefﬁcient
∂iΦR : (Rˆ⊗ g)×···× (Rˆ⊗ g)| {z }
i
→ Rˆ⊗ h
is the R-multilinear homogeneous extension of ∂iΦ. See [Ye2, Section 3] for more
details.
MC ELEMENTS 27
Deﬁnition 8.1. Let Φ : g→ h be an L ∞ morphism, and let (R, m) be a parameter
algebra. For an element ω∈ mˆ⊗ g1 we deﬁne
MC(Φ, R)(ω) := ∑
i≥1
1
i! (∂iΦR)(ω, . . . ,ω| {z }
i
)∈ mˆ⊗ h1.
Note that the sum above converges in the m-adic topology of mˆ⊗ h1, since
(∂iΦR)(ω, . . . ,ω)∈ miˆ⊗ h1 = mi−1· (mˆ⊗ h1).
Proposition 8.2. Let ω∈ MC(g, R) = MC(mˆ⊗ g). Then the element MC(Φ, R)(ω)
belongs to MC(h, R). Thus we get a function
MC(Φ, R) : MC(g, R)→ MC(h, R).
Proof. Let Rj := R/mj+1, and let pj : R→ Rj be the projection. According to [Ye2,
Theorem 3.21], which refers to the artinian case, we have
MC(Φ, Rj)(pj(ω))∈ MC(h, Rj)
for every j. And by Lemma 4.1(2) we know that
MC(h, R)∼= lim
←j
MC(h, Rj).
□
Let ΩK[t] = K[t]⊕ Ω1
K[t] be the algebra of polynomial differential forms in the
variable t (relative to K). This is a commutative DG algebra. For λ∈ K there is a
DG algebra homomorphism σλ : ΩK[t]→ K, namely t↦→ λ. There is an induced
homomorphism of DG Lie algebras
(8.3) σλ : mˆ⊗ ΩK[t]ˆ⊗ g→ mˆ⊗ g,
and an induced function
(8.4) MC(σλ) : MC(mˆ⊗ ΩK[t]ˆ⊗ g)→ MC(mˆ⊗ g)
We shall often think of elements of ΩK[t] as “functions of t”, as in Section 1.
Given elements f (t)∈ ΩK[t] and λ∈ K, we shall use the substitution notation
f (λ) := σλ( f (t))∈ K.
Lemma 8.5. Here λ = 0, 1.
(1) The homomorphisms σ0, σ1 in formula (8.3) are quasi-isomorphisms.
(2) The functions MC(σ0) and MC(σ1) in formula (8.4) are bijections.
(3) The bijections MC(σ0) and MC(σ1) are equal.
Proof. (1) This is because the homomorphisms σi : ΩK[t] → K are homotopy
equivalences (of complexes of K-modules).
(2) This is by item (1) and Theorem 4.2.
(3) Note that the inclusion
φ : mˆ⊗ g→ mˆ⊗ ΩK[t]ˆ⊗ g
is also a quasi-isomorphism, and that σ0◦ φ = σ1◦ φ is the identity automorphism
of mˆ⊗ g. Hence
MC(σ0)◦ MC(φ) = MC(σ1)◦ MC(φ),
and canceling the bijection MC(φ) we obtain our result. □
Lemma 8.6. Let ω0, ω1∈ MC(mˆ⊗ g). The following two conditions are equivalent:
28 AMNON YEKUTIELI
(i) There exists an element g∈ exp(mˆ⊗ g0) such that
Af(g)(ω0) = ω1.
(ii) There exists an element
ω(t)∈ MC(mˆ⊗ ΩK[t]ˆ⊗ g)
such that ω(0) = ω0 and ω(1) = ω1.
Proof. (i)⇒ (ii): Consider the elements γ := log(g)∈ mˆ⊗ g0,
g(t) := exp(tγ)∈ exp(mˆ⊗ (ΩK[t]⊗ g)0)
and
ω(t) := Af(g(t))(ω0)∈ MC(mˆ⊗ ΩK[t]ˆ⊗ g).
Then
ω(0) = Af(g(0))(ω0) = Af(1)(ω0) = ω0
and
ω(1) = Af(g(1))(ω0) = Af(g)(ω0) = ω1.
(ii)⇒ (i): Let us write [ωi] for the classes in MC(mˆ⊗ g). We know that
MC(σi)([ω(t)]) = [ ωi]
for i = 0, 1. By Lemma 8.5(3) we know that MC(σ0) = MC(σ1). Therefore
[ω0] = [ ω1]; and by deﬁnition this says that Af (g)(ω0) = ω1 for some g. □
Proposition 8.7. Let Φ : g→ h be an L∞ morphism. The function
MC(Φ, R) : MC(g, R)→ MC(h, R)
respects gauge equivalences. Therefore there is an induced function
MC(Φ, R) : MC(g, R)→ MC(h, R).
Proof. Let A := Rˆ⊗ ΩK[t], which is a commutative DG algebra. There are in-
duced homomorphisms σi : A→ R. And there is an induced A-multilinear L ∞
morphism
ΦA : mˆ⊗ ΩK[t]ˆ⊗ g→ mˆ⊗ ΩK[t]ˆ⊗ h
(cf. [Ye2, Section 3]). Let us write MC (g, A) := MC(mˆ⊗ ΩK[t]ˆ⊗ g) etc. There
is a function MC (Φ, A) whose formula is like in Deﬁnition 8.1. Since the L ∞
morphisms ΦR and ΦA are induced from Φ, the diagram of functions
MC(g, A)
MC(Φ,A) //
MC(σi,R)

MC(h, A)
MC(σi,R)

MC(g, R)
MC(Φ,R) // MC(h, R)
is commutative, for i = 0, 1. Now suppose ω0, ω1∈ MC(g, R) are gauge equiv-
alent. By Lemma 8.6 there is an element ω(t)∈ MC(g, A) such that ω(i) = ωi.
Deﬁne χi := MC(Φ, R)(ωi) and χ(t) := MC(Φ, A)(ω(t)). Because the diagram
above is commutative, we have χ(i) = χi. Using Lemma 8.6 again we conclude
that χ0 and χ1 are gauge equivalent. □
MC ELEMENTS 29
Let Ψ : C→ D be the morphism in DGCog(K) gotten by applying the functor
C∞ to the L ∞ morphism Φ : g→ h. And let ˜Ψ : ˜C→ ˜D be the morphism gotten
by applying the functor C◦ L to Ψ : C→ D. Since θ− is a natural transformation,
we get a commutative diagram
(8.8) C Ψ //
θC

D
θD

˜C
˜Ψ // ˜D
in DGCog(K). There is a corresponding commutative diagram
(8.9) g Φ //
θg

h
θh

˜g
˜Φ // ˜h
in DGLie∞(K). Namely ˜g = ( L◦ C)(g), ˜h = ( L◦ C)(h), and the full faithful
functor C∞ sends the diagram (8.9) to the diagram (8.8). Note that by the proof of
Lemma 7.2, the Taylor coefﬁcients ∂jθC are nonzero for all j; so the corresponding
morphism θg : g→ ˜g in DGLie∞(K) is not a DG Lie algebra homomorphism. The
same for θh.
Lemma 8.10. The diagram of functions
(8.11) MC (g, R)
MC(Φ,R) //
MC(θg,R)

MC(h, R)
MC(θh,R)

MC(˜g, R)
MC( ˜Φ,R) // MC(˜h, R)
is commutative.
Proof. Because of Lemma 4.1(2) we can assume that R is artinian. Consider the
commutative diagram of DG coalgebras over R
(8.12) R⊗ C
ΨR //
θC,R

R⊗ D
θD,R

R⊗ ˜C
˜ΨR // R⊗ ˜D
induced from (8.8) by tensoring with R.
Take any ω∈ m⊗ g1⊂ R⊗ C, and deﬁne
e := exp(ω) = ∑
i≥0
1
i! ωi∈ R⊗ C.
According to [Ye2, Lemma 3.18] we have
(
MC(θh, R)◦ MC(Φ, R)
)
(ω) = log
(
(θD,R◦ ΨR)(e)
)
=
log
(
( ˜ΨR◦ θC,R)(e)
)
=
(
MC( ˜Φ, R)◦ MC(θg, R)
)
(ω).
This proves commutativity of the diagram. □
30 AMNON YEKUTIELI
Theorem 8.13. Let g and h be DG Lie algebras, let Φ : g → h be an L∞ quasi-
isomorphism, and let R be a parameter algebra, all over the ﬁeld K. Then the function
MC(Φ, R) : MC(g, R)→ MC(h, R)
(see Proposition 8.7) is bijective.
The idea for the proof was suggested to us by Van den Bergh.
Proof. By Lemma 7.3 the DG Lie algebra homomorphism ˜Ψ : ˜g→ ˜h is a quasi-
isomorphism. Therefore by Theorem 4.2 the function
MC( ˜Φ, R) : MC(˜g, R)→ MC(˜h, R)
is bijective.
Next, by [Hi2, Proposition 4.4.3(1)] the DG Lie algebra homomorphism ζg :
˜g→ g is a quasi-isomorphism. Again using Theorem 4.2 we conclude that the
function
MC(ζg, R) : MC(˜g, R)→ MC(g, R)
is bijective. On the other hand, by Lemma 7.2, with the arguments in the proof of
Lemma 8.10, we see that
MC(ζg, R)◦ MC(θg, R) = 1MC(g,R).
Therefore
MC(ζg, R)◦ MC(θg, R) = 1MC(g,R).
Because MC(ζg, R) is a bijection, the same is true for the function MC(θg, R). The
same line of reasoning says that MC(θh, R) is bijective.
Finally consider the commutative diagram of functions
MC(g, R)
MC(Φ,R) //
MC(θg,R)

MC(h, R)
MC(θh,R)

MC(˜g, R)
MC( ˜Φ,R) // MC(˜h, R)
induced from (8.11). We know that three of the arrows are bijective; so the fourth
arrow, namely MC(Φ, R), is also bijective. □
Remark 8.14. Lemma 3.5 in our earlier paper [Ye1] says that the canonical func-
tion
MC(g, R)→ lim
←j
MC(g, R/mj)
is bijective. The proof of this Lemma (which is actually omitted from the paper)
is incorrect. Moreover, we suspect that statement itself is false. The hidden as-
sumption was that the gauge group G (g, R) acts on the set MC (g, R) with closed
orbits.
This lemma is used to deduce [Ye1, Corollary 3.10] (incorrectly) from the nilpo-
tent case. The correction is to replace [Ye1, Corollary 3.10] with Theorem 8.13
above. The same correction pertains also to [Ye4, formula (12.2)].
Remark 8.15. This is a good place to correct a typographical error (repeated
several times) in [Ye2, Section 3]. In Lemmas 3.14 and 3.18 of op. cit., instead of
“mg[1]” the correct expression should be “ mg1” or “(mg[1])0”.
Let us also mention that a “colocal coalgebra homomorphism”, in the sense of
[Ye2, Deﬁnition 3.3], is the same as a “unital coalgebra homomorphism”.
MC ELEMENTS 31
