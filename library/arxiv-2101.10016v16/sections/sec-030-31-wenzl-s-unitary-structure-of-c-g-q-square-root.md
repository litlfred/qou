---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-030-31-wenzl-s-unitary-structure-of-c-g-q-square-root
section_title: "Wenzl’s unitary structure of C(g, q, ℓ), square root of the quantum Casimir"
section_number: 31
pages: 187-194
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
doc_brief: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem — We construct, for every complex simple Lie algebra g and every positive integer level k, a unitary modular"
---
31. Wenzl’s unitary structure of C(g, q, ℓ), square root of the quantum
Casimir
Recall that the algebra Uq(g) at complex roots of unity was introduced in Sect. 19,
and we assume the same setting as there. In particular, it becomes a (topological) ribbon
complex Hopf algebra with a ∗–involution.
For the reader convenience we recall two main results from [185] concerning the unitary
structure. They center on a continuity argument that plays an important role in our
paper in connecting structures from quantum groups at roots of unity to corresponding
structures from affine Lie algebras, developed in Sects. 26–33. To this aim, as we shall
see, it is important that the root of unity is minimal of large enough order in the sense of
Def. 19.1, 20.2.
Remark 31.1. Note that for non-minimal roots, the continuity argument may not be
applied, but the construction of this section possibly extend to these cases and lead to
Hermitian structure. This may have possible applications to the study of Hermitian ribbon
categories or applications to Chern-Simons theory, see Remark 8 in [161].
31.1. Unitary structure of irreducible modules. The first result describes unitarizability of a fixed specialized Weyl module Vλ(q) of the Hopf algebra Uq(g) when q varies
in an arc of the unit circle depending on λ. Recall that if q is any complex root of unity, ℓ
′
denotes the order of q, ℓ the order of q
2
, Λ+ the cone of dominant integral weights, Λ+(q)
the open Weyl alcove associated to q, Λ+(q) = {λ ∈ Λ
+ : ⟨λ + ρ, θ0⟩ < ℓ}, where θ0 is the
highest root θ if d divides ℓ and the highest short root θs otherwise. Forthermore, Λ+(q) is
contained in a fundamental domain for the action of the affine Weyl group Wℓ
′. To cover
the case where q ∈ T is not a root of unity, we set ℓ
′ = ∞, Λℓ
′=∞ = Λ+ and Wℓ′ is the
ordinary Weyl group.
Theorem 31.2. ([185] Proposition 2.4) Let λ be a dominant weight and
I = {q = e
iπt : |t| <
1
m − d
}
where m = ⟨λ + ρ, θ⟩. Then Vλ(q) is simple and the Hermitian form defined in Prop. 2.2
in [185] is positive definite for q ∈ I.

188 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Proof. We claim that λ ∈ Λ+(q) for q ∈ I, that is ⟨λ + ρ, θ0⟩ ≤ ℓ. We may assume that ℓ
′
is finite. Note that |t| <
1
m−d
implies ℓ > m − d as 2πr|t| < 2π for r ≤ m − d. We have
the following cases.
a) d = 1; In this case θ0 = θ, and the claim is m ≤ ℓ, but we already know this.
b) 1 < d and d divides ℓ; In this case θ0 = θ and we need to show m ≤ ℓ. As pointed out
in [185], ⟨µ, θ⟩ is divisible by d for any dominant weight µ, thus m − d < ℓ is equivalent to
m ≤ ℓ,
c) 2 = d and ℓ is not divisible by d; we have θ0 = θs and we need to show ⟨λ+ρ, θs⟩ < ℓ.
We have ⟨λ+ρ, θs⟩ = m− ⟨(λ+ρ, θ−θs⟩ < ℓ+d− ⟨λ+ρ, θ−θs⟩, but ⟨λ+ρ, θs⟩ < ⟨λ+ρ, θ⟩
are both integers thus ⟨λ + ρ, θs⟩ < ℓ + 1 in this case,
d) 3 = d and ℓ not divisible by d; we have θ0 = θs and we verify ⟨λ + ρ, θs⟩ ≤ ℓ. We also
have g = G2, ⟨λ + ρ, θ − θs⟩ = 4 and we conclude as in the previous case, and the claim is
proved. Assume that Vλ(q) is not simple. It follows it admits a submodule of highest weight
µ < λ, thus λ and µ lie in Λ+(q) that is a fundamental domain for the translated action of
Wℓ
′, thus these dominant weights can not be conjugate under this action, contradicting the
linkage principle. The Hermitian form (ξ, η) of Vλ,A′ as in the statement is Hermitian over
the Laurent polynomial ring A′ by Prop. 2.3 in [185] and thus it becomes an Hermitian form
for Vλ(q) specializing x to any complex number q with |q| = 1. Moreover it is not trivial as
(vλ(q), vλ(q) > 0 and it makes Vλ(q) into a ∗-representation, and it follows that the radical
of the Hermitian form is a ∗-subrepresentation, that vanishes by simplicity, and it follows
that the form is non-degenerate. Let vi(q) be the specialization of Kashiwara-Lusztig basis
at q and consider the matrix with entries (vi(q), vj (q)), which depend continuously on q,
and therefore the same holds for the eigenvalues. The ∗-involution of the Hopf algebra
U(g) for q = 1 (classical limit) corresponds to the compact real form gR of g, and the
Hermitian form of the Weyl module Vλ of U(g) is a unitary representation of the compact
Lie subgroup K of G, see Remark 19.2. Hence ((vi(q), vj (q))) is positive for all q ∈ I. □
Remark 31.3. Note that by the proof of Lemma 2.2 in [185], the Hermitian form of the
statement is the specialization at q of an Hermitian form on the Weyl module Vλ,A′ of
U
†
A′(g) satisfying the assumptions in b) of Prop. 14.2.
We summarize some of the results recalled in Sect. 19 and in proof of the previous
theorem in the following corollary that plays an important role in [185] and also in our
paper. Recall that minimal roots of large enough order have been defined in Def. 19.1,
20.2.
Corollary 31.4. Let q0 be a minimal root of unity of large enough order. Then for all
q varying on the arc Tq0,1 of the unit circle clockwise connecting q0 to 1, we have that
Λ+(q0) ⊂ Λ+(q) and the latter equals the whole Weyl chamber Λ
+ for q = 1; for λ ∈ Λ+(q0),
and q varying continuously in Tq0,1, the Kashiwara-Lusztig basis of Vλ,A′ specializes to a
basis of Vλ(q); the invariant Hermitian form of Vλ(q) is positive definite and is uniquely
determined by (vλ(q), vλ(q)) = 1 and is invariant with respect to the compact real form of
U(g) for q = 1.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 189
We next recall the unitary structure on certain tensor products of specialized Weyl
modules of Uq(g).
31.2. Square root of the quantum Casimir operator and compatible Hermitian
coboundary structure of Uq(g). Loosely speaking, the strategy of [185] is to define a
Hermitian structure on tensor products Vλ(q0) ⊗ Vµ(q0) for λ, µ ∈ Λ+(q0) via the action of
a coboundary matrix of Uq0(g) on the space. By [161], Uq0(g) is a ribbon Hopf algebra in
a topological sense. However the ribbon element v may not have a square root in Uq0(g)
arising as the specialization at q0 of an element in the integral form U
†
A′(g). This problem
is mentioned at the beginning of Sect. 3.6 in [185].
Indeed, if this were the case then following a central idea in [185], by our theorem 28.9
we would have an Hermitian form on the full tensor product obtained by specialization
of a nondegenerate A′-valued Hermitian form. Since it is obtained as a specialization,
the Hermitian form would be continuous in q, and thus positive since it reduces to the
usual inner product for q = 1. It would then follow that the tensor product is completely
reducible, but this is not always the case.
For our purposes we shall need an Hermitian form defined on every tensor product space
Vλ(q0) ⊗ Vµ(q0) for λ, µ ∈ Λ
+(q0), thus we look for a square root operator of the action
of R21R. Using the ribbon structure given by the specialized quantum Casimir v see Def.
19.5, Theorem 19.7, Sect. 19, 20, 31, we are reduced to construct a square root of the
action of v on a full tensor product.
Definition 31.5. For an invertible operator T on a finite dimensional vector space, we
define T
1/2 via Jordan decomposition, that is for a Jordan block J = c(I + N) of T with
c ∈ C, c ̸= 0 and N nilpotent we set J
1/2 = c1/2
(1 + N)
1/2
, where (1 + N)
1/2
is defined via
Taylor expansion (that is eventually constant since N is nilpotent) and for c = |c|e
2πit ∈ C,
t ∈ (−1, 1] we set c
1/2 = |c|1/2
e
πit
, |c|
1/2 > 0.
It follows from the inclusions (19.6), (19.7) that for any invertible elements T ∈ Uq0(g),
the square roots T
1/2 and ∆(T)1/2 are well defined as operators of ΠV (q0)End(V (q0)) and
ΠV (q0),W(q0)End(V (q0)) ⊗ End(W(q0)) respectively.
Definition 31.6. In particular, let v be the specialized quantum Casimir operator of
Uq0(g) as in Def. 19.5. Then v
1/2 and ∆(v)1/2 are well defined invertible operators of
ΠV (q0)End(V (q0)) and ΠV (q0),W(q0)End(V (q0)) ⊗ End(W(q0)) respectively.
Proposition 31.7. We have for λ, µ ∈ Λ+(q0),
a) for T ∈ Uq0
(g) invertible, R∆(T)
1/2 = ∆op(T)1/2R,
b) v
1/2 acts on Vλ(q0) as a scalar in T, given by wλ := q0
−
⟨λ,λ+2ρ⟩
2 ,
c) ((R21R)
−1
)
1/2 acts on Vλ(q0) ⊗ Vµ(q0) as ∆(v)1/2w
−1
λ ⊗ w
−1
µ
,
d) the operator Rλ,µ = R((R21R)
−1
)
1/2
is invertible selfadjoint on Vλ(q0)⊗Vµ(q0) w.r.t.
the product of Wenzl inner products and satisfies (Rµ,λ)21Rλ,µ = 1.

190 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Proof. The proof of a), b), c) follow easily from the definitions and Prop. 19.7. d)
Selfadjointess of Rλ,µ can be shown as in the proof of Theorem 28.9 with the following
modifications. In equations (28.3)–(28.5) we put E = I, replace ∆(w) with ∆(v)
1/2
,
∆op(w) with ∆op(v)
1/2
, ∆( ˜ w) with ∆( ˜ v)
1/2
, and in (28.4) we use a). In (28.6) we use
(∆( ˜ v)
1/2
)
∗ = (∆( ˜ v)∗
)
1/2
(the coefficients of the Taylor expansion are real), in (28.6) we
replace ∆(w
−1
) with ∆(v
−1
)
1/2
. The coboundary equation (Rµ,λ)21Rλ,µ = 1 can be shown
as in Prop. 28.8 with similar replacements of ∆(w) and ∆op(w) with ∆(v)
1/2 and ∆op(v)1/2
respectively.
□
Remark 31.8. Thus Rλ,µ defines a non-degenerate Hermitian form on the full tensor
product space Vλ(q0) ⊗ Vµ(q0) making the braided symmetry unitary, cf. the problem
mentioned at the beginning of Sect. 3.6 in [185]. On the other hand, not all the idempotents pγ : Vλ,A′ ⊗A′ Vµ,A′ → Vγ,A′ describing classical fusion specialize to corresponding
idempotents pγ(q) by non-semisimplicity. By [185], this is an obstruction in the proof of
positivity of the Hermitian form, in that when this is possible then the Hermitian form of
the specialized module Vλ(q0) ⊗ Vµ(q0) is positive on Vγ(q0) by a continuity argument that
links q0 to the classical limit 1 that comes from specialization (unlike the construction of
Prop. 31.7). Notably, there are sufficiently many modules for which this holds, and in a
nutshell from them we shall construct the wqh.
We next show that Uq0(g) satisfies the axioms of a Hermitian coboundary Hopf algebra.
With this we mean that we show that axioms a), b), c), d) of Def. 28.1 hold for the topological Hopf algebra Uq0
(g) defined by [161]. The result is motivating for the construction
of the unitary discrete coboundary weak Hopf algebras AW (g, q0, ℓ) of the next section.
Moreover, in Sect. 32, see Theorem 2.5, and more in detail Prop. 32.20 and in Sect. 33
we shall need the 2-cocycle property of the coboundary R = RU of Uq0(g) for the proof of
our analogue of KL-F theorem for affine vertex operator algebras 2.11.
We need at least to show that the square root v
1/2 of the ribbon element v lies in Uq0
(g)
and that ∆(v
1/2
) = ∆(v)
1/2
. We shall see that combining with the work in [185], this is
all is left to show. Note that the R-matrix R and the ribbon element v ∈ Uq0(g) depend
only on the choice of q
1/L
0
, see Sect. 1 in [161], Sect. 1.4 in [185].
Theorem 31.9. Let q
1/L
0
be a fixed L-th root of q0 and consider the associated ribbon
structure (R, v) on Uq0(g) defined as in Sect. 19, (i.e. following [161] for the algebraic
structure and [185] for the ∗-involution). Let v
1/2 and ∆(v)1/2
be defined as in Def. 31.6.
Then
a) v
1/2 ∈ Uq0
(g) and ∆(v)
1/2 ∈ Uq0
(g)⊗Uq0
(g), the completed tensor product defined
in [161], and ∆(v
1/2
) = ∆(v)
1/2
.
b) with w = v
1/2
, Uq0(g) becomes a (topological) Hermitian coboundary Hopf algebra
with compatible involution and antipode of Kac type.
c) In particular, R
U
:= RU∆(w)w
−1 ⊗ w−1
is a 2-cocycle for Uq0(g),
R
U
⊗ I∆ ⊗ 1(R
U
) = I ⊗ R
U
1 ⊗ ∆(R
U
).

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 191
Proof. The Kac-type property of the antipode follows from properties (19.2)–(19.3) that
still hold for Uq0(g). Axioms a) b), d) of Def. 28.1 are shown in Lemma 1.4.1 of [185]
in the case of the algebra over a formal variable x, and easily extend to the specialized
algebra Uq0(g) of [161]. For axiom c), we set w = v
1/2 defined on each full matrix algebra
M defining Uq0(g) as in Def. 31.6 via the Jordan form of v. If c(I + N) is a Jordan block
for v then c(I ⊗ I + ∆(N)) is a Jordan block for ∆(v), and this puts ∆(v) in Jordan
form. Thus v
1/2 and ∆(v)1/2 are eventually constant limit on the full matrix algebras
defining Uq0(g) and Uq0(g)⊗Uq0
(g) respectively. This shows that v
1/2 and ∆(v)1/2
lie in
Uq0(g) and Uq0(g)⊗Uq0(g) respectively. Since v is central, the nilpotent parts occurring
in v are central, thus v
1/2
is central. The equality ∆(v
1/2
) = ∆(v)
1/2
follows from the
homomorphism property of ∆. □
The previous result was implicitly used in [25] but no detailed proof was given. In that
paper two of us constructed weak Hopf algebras associated to Verlinde fusion categories in
the type A case with specific methods. In Sect. 32 we shall extend and expand the main
result of [25] to the other Lie types with general methods.
Proposition 31.10. The elements R
U
R
U
⊗ I∆ ⊗ 1(R
U
) = I ⊗ R
U
1 ⊗ ∆(R
U
) (31.1)
are selfadjoint in Uq0(g)⊗Uq0
(g) and Uq0(g)⊗Uq0(g)⊗Uq0(g) respectively.
Proof. Selfadjointness of R
U
follows from part d) of Prop. 31.7. Recall that R
U
twists ∆
to ∆op and that ∆(a)
∗ = ∆op(a∗
) for a ∈ Uq0(g). We have
(R
U
⊗ I∆ ⊗ 1(R
U
))∗ = ∆op ⊗ 1(R
U
)R
U
⊗ I = R
U
⊗ I∆ ⊗ 1(R
U
).
□
Remark 31.11. Note that the ribbon element of Uq0(g) defined in detail in [161] acts on
any irreducible Weyl module Vλ(q0) as q0
−⟨λ,λ+2ρ⟩
, but this may not suffice to determine an
expression of the ribbon element in Uq0(g). Moreover, there is no unitary square root of
the ribbon element in Uq0(g) which is continuous in q from 1 to q0 as otherwise by Theorem
28.9 this induces an Hermitian form on any full tensor product of Weyl modules and by
continuity in 1 by Wenzl argument it is positive definite. Thus the tensor product would
be completely reducible, but this is not always the case.
On the other hand, when a Wenzl idempotent pγ : Vλ(q0) ⊗ Vµ(q0) → Vγ(q0) onto an
irreducible Weyl module Vγ(q0) is well-defined, a unitary square root w of the action of
v can be defined as in part b) of Prop. 31.7 on Vγ(q0) and is a specialization at q0 of a
corresponding action in the formal variable x. In particular, this holds for λ, µ, γ in the
open Weyl alcove Λ+(q0).

192 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
31.3. Hermitian form on tensor product modules (following Wenzl). We next
recall a second main result in [185] on the construction of an Hermitian form on certain
tensor products of specialized Weyl modules. When we specialize x to a root of unity q,
not all the specialized Weyl modules Vλ(q) are irreducible, and not all the idempotents pγ :
Vλ,A′ ⊗A′ Vµ,A′ → Vγ,A′ describing classical fusion specialize to corresponding idempotents
pγ(q).
For example, when λ, µ ∈ Λ
+(q) then Vλ(q)⊗Vµ(q) is tilting and the decomposition into
indecomposable tilting modules depends in general on the affine Weyl group associated
to q and thus on the order of q
2
. When q0 is a minimal root of large enough order (Def.
20.2, 19.1) there are special cases where λ, µ, γ are fixed dominant weights of Λ+(q0) when
we let q varying continuously from q0 to 1 as in Corollary 31.4, and we regard λ, µ, γ as
elements of Λ+(q) (that contains Λ+(q0) by the same Corollary).
In these cases pγ(q) can be constructed as an idempotent onto the isotypic component
corresponding to γ arising from specialization in q of a corresponding idempotent between
modules of the integral form. Assume that we are in one of these cases. On the range of
pγ(q), ∆(v)
1/2
v
−1/2 ⊗ v−1/2 acts as as a square matrix with respect to the product of the
two Kashiwara-Lusztig bases with entries powers in the specified power q
1/L = e2πit/L (the
weights of the tensor product are congruent to λ + µ, and the action of v on each weight
space is given by the quantum Casimir, part d) of Theorem 19.4, thus ∆(v)
1/2
v
−1/2 ⊗v−1/2
acts diagonally on each weight space with eigenvalues integral powers of q
1/L). Note in
particular that this action is continuous.
Moreover, R(q) acts as a rectangular matrix, as R(q) may not leave the range of pγ(q)
invariant. It follows that Rλ,µ(q) defines a non-degenerate Hermitian form on the product
Hilbert space making the ranges pairwise orthogonal if we in addition know that Vλ(q) ⊗
Vµ(q) is completely reducible into irreducible Weyl modules as in the classical case. Thus
in this case pγ(q) is selfadjoint with respect to the Hermitian form of the domain, and it
follows that the form is nondegenerate on the range of pγ(q), and therefore positive by the
continuity argument. The selfadjointness property reads as
pγ(q)
†Rλ,µ(q) = Rλ,µ(q)pγ(q), (31.2)
where pγ(q)
†
is the adjoint of pγ(q) with respect to the tensor product Hilbert space structure.
More precisely, by Sect. 3.5 in [185], we choose a fundamental representation V of the
Lie algebra for each Lie type. Let κ be its highest weight. This representation can be
defined explicitly as follows (we follow [98] for notation of the fundamental weights here
below):
AN ) the vector module of slN+1, κ = λ1,
BN ) the spin module of o2N+1, κ = λN ,
CN ) the vector module of sp2N , κ = λ1,
DN ) the two spin modules of o2N , κ = λN−1, λN ,
E6) κ one among λ1 or λ6 the corresponding vertex in the Dynkin diagram is chosen
between the two farthest from the branching point,

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 193
E7, E8) κ = λ7, λ8 respectively,
F4) κ = λ4,
G2) κ = λ1.
We shall need the following properties of V . As anticipated in Subsect. 19.1 Wenzl [185]
notes the following useful fact.
Theorem 31.12. Suppose that κ lies in the open principal Weyl alcove Λ
+(q). Then a
U(g)-module is tilting if and only if it is a direct sum of direct summands of tensor powers
of V (q).
Recall that in Subsect. 19.5 we introduced the open Weyl alcove Λ+(q), and recalled
that it labels the irreducible objects of C(g, q, ℓ). We here recall that the Coxeter number
h and its dual h
∨ may are also computed as
h
∨ = ⟨ρ, θ∨
⟩ + 1, h = ⟨ρ, θ∨
s
⟩ + 1, (31.3)
with as before θ the highest root and θs the highest short root. Recall also from Def. 19.1
the level k associated to the order ℓ of q
2
. We introduce
h(λ) := ⟨λ, θ∨⟩ if d|ℓ, h(λ) = ⟨λ, θs⟩ otherwise.
The following result (mentioned in Subsect. 19.1) is simple but useful, especially for the
use of Theorem 31.12, to determine the minimum possible value of the level k for which
the above Theorem applies.
Proposition 31.13. The dominant weight λ lies in the Weyl alcove Λ
+(q) if and only if
h(λ) ≤ k. Moreover h(κ) = 1 for the classical Lie types, E6, E7, and h(κ) = 2 for E8. For
F4 and G2 then h(κ) = 1 if d|ℓ, and h(κ) = 2 otherwise.
The fundamental representation V is irreducible if g is not of type D, and is the sum of
the two half spin representations in the type D case; every irreducible of g is a subrepresentation of a power of V ; the dominant weight of V (or of each summand in type D) lies
in Λ+(q).
We consider the associated Weyl module of Uq(g) denoted in the same way. For λ ∈
Λ
+(q0), Vλ(q) ⊗ V (q) decomposes into a direct sum of indecomposable tilting modules Tγ
Vλ(q) ⊗ V (q) = ⊕γTγ ⊗ C
mγ
with the property that for g ̸= E8, the dominant weights γ appearing in the decomposition
at most lie in Λ+(q), and for g ̸= F4, E8 the decomposition is multiplicity-free in the
classical case. Thus Tγ = Vγ(q) for all γ and the decomposition is completely reducibile
and unique, thus pγ(q) is defined.
For g = F4 multiplicity may arise for γ = λ. In this case, pγ(q) is first defined for γ ̸= λ
then pλ(q) is defined as the complement idempotent.
For g = E8, the summand Tγ may not lie in Λ+(q) for γ = λ + κ with κ the dominant
weight of V . Multiplicity may arise for γ = λ in this case also. In Prop. 3.6 case 2 [185] it
is shown that a selfadjoint projection pγ(q) may be defined, and we shall comment more
on this in the next section, and more precisely in the proof of Lemma 32.18.

194 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
These constructions hold for any primitive root q such that the order ℓ of q
2
is large
enough (see Def 19.1) and under this assumption we shall construct the weak Hopf algebra
AW (g, q, ℓ) at an algebraic level in the first part of the following section.
For the unitary structure, Wenzl shows that the restriction to the minimal roots Def.
20.2 is essential. The requirement of having large enough order includes the fundamental
representations in the open Weyl alcove for all Lie types and positive integer levels, see
Prop. 2.4 in [185], also Theorem 31.2.
Definition 31.14. We refer to pγ (also denoted pλ,γ in the next section)
Vλ(q) ⊗ V (q) → Vγ(q) ⊗ C
mγ
, λ, γ ∈ Λ
+(q) (31.4)
as Wenzl idempotents.
Remark 31.15. For the unitarization result of [185], one only needs λ, γ ∈ Λ
+(q0) (but
to construct pγ for γ = λ in the F4 one also needs pν with ν ∈ Λ+(q0), see the proof of
the proposition at page 274 in [185]). On the other hand, for our purposes (a search of
strongly unitary structures), see Theorem 2.8, we need the stronger positivity results of
Lemma 3.6.2 (b) in [185] that involve positivity of the Hermitian form also on the range
of pγ for γ ∈ Λ(q0) for g ̸= E8.
