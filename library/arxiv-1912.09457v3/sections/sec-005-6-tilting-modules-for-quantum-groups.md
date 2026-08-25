---
doc_id: arxiv-1912.09457v3
doc_title: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS"
section_id: sec-005-6-tilting-modules-for-quantum-groups
section_title: "Tilting modules for quantum groups"
section_number: 6
pages: 16-17
source_pdf: 1912.09457v3.pdf
source_sha256: c00b3801060fc3cc
doc_brief: "GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS — We introduce a generalization of the notion of a negligible morphism and study the associated tensor ideals and thick id eals."
---
We review some results about quantized tilting modules whic h are needed
to show that the category of tilting modules can be obtained a s a mod m
evaluation.
6.1. Lusztig’s integral form. We denote by A = Z[v,v −1] the Laurent
polynomial ring in an indeterminate v and byU =UA Lusztig’s integral form
(with divided powers) of the Drinfeld quantized enveloping algebra Uv over
Q(v) [
L93]. Any commutative ring R with 1 and a ﬁxed invertible element
v can be regarded as a commutative A-algebra via the homomorphism φ :
A → R such that φ(vn) = vn for all n ∈ Z. For any A-algebraR we denote
UR = UA ⊗A R. We apply this for R = Q(q) and specialize the generic
parameterv to a primitive ℓ-th root of unity q withℓ odd, and assume that
ℓ is not divisible by 3 if g ∼
= g2. We also assume ℓ>h , the Coxeter number
of g. Then we denote by Rep(Uq(g)) the category of ﬁnite dimensional
representations of Uq(g) of type 1 as in [
APW91].
6.2. Quantized tilting modules over Q(q). InRep(Uq(g)) we have analogs
of Weyl and induced modules (where the latter can be deﬁned by means of
the triangular decomposition of Uq(g)) which we denote again by V (λ) and
H 0(λ), λ ∈ X +. These satisfy exactly the same Ext-vanishing conditions
as in the modular case. In particular
Exti(V (λ),H 0(λ)) = 0
for i > 0, λ ∈ X + (see [ An92] and the references therein). This uses the
quantum variant of Kempf’s vanishing theorem. We can then de ﬁne modules
with a good ﬁltration and a Weyl ﬁltration and deﬁne tilting m odules as in
the modular case. The main statement (proposition 5.1) about indecompos-
able tilting modules still holds and we denote by T (λ) the indecomposable
tilting module attached to λ ∈X +.
GENERALIZED NEGLIGIBLE MORPHISMS AND THEIR TENSOR IDEALS 1 7
6.3. Quantized tilting modules over R. As in the modular case, the
entire theory of tilting modules can be developed over a (com plete) dis-
crete valuation ring. The crucial ingredient here is that Ke mpf’s vanishing
theorem holds over the ground ring A as well. This follows from work of
Ryom-Hansen [RH03] and Kaneda [ Ka00] [ Ka98-2]. For an A-algebraR we
denote by H 0
R(λ) and VR(λ) the corresponding induced module and Weyl
module. For any base change A → R we have
H 0
A(λ) ⊗AR =H 0
R(λ) ∀λ ∈X +
and likewise for VR(λ). Again by Kempf’s vanishing theorem over A and
standard facts about H i we get the vanishing of Exti
UA(A,H 0
A(λ) ⊗H 0
A(µ))
for allλ,µ ∈X + andi> 0 (see also [
Ka98-2]). The remaining arguments are
the same as in the modular case. In particular for each λ ∈X + there is an
indecomposable tilting module TR(λ),λ ∈X +, such that its λ-weight space
is free of rank 1 [ Ka98-2, Theorem 7.6] and every tilting module decomposes
uniquely into a direct sum of the TR(λ).
Since the λ-weight space is free of rank 1, the arguments of Jantzen [ J03,
E.20] go through and we obtain
Corollary 6.1. LetR be a complete discrete valuation ring with residue
ﬁeld R/m = Q(q) (or C) of characteristic 0. Then
TR(λ) ⊗R/m ∼
=TR/m(λ)
End(TR(λ)) ⊗RR/m) ∼
=End(TR(λ)) ⊗RR/m.
