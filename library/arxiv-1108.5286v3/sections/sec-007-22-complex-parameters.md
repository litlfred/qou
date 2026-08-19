---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of aﬃne Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen"
section_id: sec-007-22-complex-parameters
section_title: "Complex parameters"
section_number: 2.2
pages: 21-24
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
doc_brief: "Hochschild homology of affine Hecke algebras Maarten Solleveld Radboud Universiteit Nijmegen — Let H = H(R,q ) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not"
---
Everything we discussed in the previous subsection has a nat ural analogue for graded
Hecke algebras. The condition q positive translates to k real valued, but with the
scaling isomorphisms (7) we can also reach complex paramete rs.
In the graded setting we have to replace T P undT P
un by the vector spaces tP and
iaP . In the groupoid G we have to omit the parts KP , so we get a groupoid W′ with
W′
P Q = {g ∈ Γ ⋉W |g(P ) = Q} P,Q ⊂ ∆ .
Theorem 2.4. Suppose that kα ∈ R for all α ∈R. There exists a natural Q-linear
bijection
ζ∨ :GQ(H ⋊ Γ) →GQ(S(t∗) ⋊W′)
such that:
(1 ) ζ∨(π) is a tempered virtual S(t∗) ⋊W′-representation if and only if π is a tem-
pered virtual H ⋊ Γ -representation.
(2 ) ζ∨ commutes with parabolic induction, in the sense that for a su bgroup Γ′
P ⊂ Γ P ,
a tempered HP ⋊ Γ′
P -representationπ and λ ∈ tW (RP )⋊Γ ′
P we have
ζ∨(
IndH⋊Γ
HP ⋊Γ ′
P
(π ◦φλ)
)
= Ind S(t∗)⋊(W ⋊Γ)
S(t∗)⋊(W (RP )⋊Γ ′
P )(ζ∨(π) ◦φλ);
(3 ) if λ ∈ ia and π is a virtual representation with central character in W′λ + a,
then so is ζ∨(π);
(4 ) if π is tempered and admits a real central character, then ζ∨(π) = π ◦m0 with
m0 as in (7).
Proof. For H ⋊ Γ-representations which admit a central character whose co mpo-
nent in ia is small, this follows from Theorems 2.2 and 1.3. The extra co ndition (4)
is actually the starting point for the construction of ζ∨, see [Sol3, Section 2.3]. We
can generalize this to all H ⋊ Γ-representations via the scaling isomorphisms
mǫ : H( ˜R,ǫk ) ⋊ Γ → H( ˜R,k ) ⋊ Γ
for ǫ> 0. ✷
An induction datum for H is a triple ( P,δ,λ ) such that P ⊂ ∆ ,δ is a discrete
series representation of HP and λ ∈ tP . Suppose that µ ∈ iaP and that ρ is an
irreducible direct summand of the representation Ind
HP ⋊Γ (P,δ,µ)
HP (δ ◦φµ) (which is
completely reducible). We abbreviate Γ ρ = Γ (P,δ,µ) and tρ = (tP )Γ ρ . We say that
{
πρ(λ) := Ind H⋊Γ
HP ⋊Γ ρ
(ρ ◦φλ) |λ ∈ tρ}
(43)
is an analytic family of H ⋊ Γ-representations. Notice that
±µ ∈ tρ (44)
21
and that the central character of πρ(−µ) equals the central character of πΓ (P,δ, 0) =
IndH⋊Γ
HP δ. Moreover the weights satisfy an integrality property with respect to
Zk := Z{kα |α ∈R}.
By [Opd, Theorem A.7] every S(t∗
P )-weightν of δ is a residual point for ( ˜RP,k P ).
The classiﬁcation of such distinguished points in [HeOp, Se ction 4] shows thatα(ν) ∈
ZkP for all α ∈ RP . By [BaMo, Theorem 6.4] this property is preserved under
induction, that is, α(ν) ∈ Zk for every α ∈R and every S(t∗)-weightν of Ind H⋊Γ
HP δ.
We conclude that all S(t∗)-weights of πρ(λ) lie in
W′(λ +µ) + Hom(ZR, Zk), (45)
where we consider Hom( ZR, Zk) as a lattice in aR ⊂ t.
To the analytic family πρ we associate the group
W′
ρ =
{
g ∈ W′ |g(P ) = P,δ ◦ψ−1
g ∼
=δ,g stabilizes {πρ(λ) |λ ∈iaρ}
}
.
Correction (2022): The new comments on pages 16, 18 and 19 also apply to the
below construction and to Corollary 2.5. If we can instead us e one of the good cases
listed on page 19, the remainder of the paper holds for those f amilies of H ⋊ Γ-
representations. Otherwise, there is still a satisfactory substitute for Corollary 2.5
in terms of families of virtual H ⋊ Γ-representations, worked out in [Sol5].
Our discussion of C[X] ⋊W′ = O(T ) ⋊W′ before Theorem 2.2 applies just as well
to H( ˜R, 0) ⋊ Γ = S(t∗) ⋊W′. The considerations that lead to Lemma 2.3 also show:
Corollary 2.5. There exist analytic families of H ⋊ Γ -representationsπρw for w ∈
⟨W′⟩, such that:
(a) The parameter space tρw/W′
ρw is isomorphic to tw/ZW ′(w), as orbifolds.
(b) πρw (λ) and πρw (λ′) have the same trace if and only if λ and λ′ lie in the same
W′
ρw -orbit.
(c) The family of representations
{πρw (λ) |w ∈ ⟨W′⟩,λ ∈ tρw/W′
ρw }
contains no repetitions and forms a basis of GQ(H ⋊ Γ) .
The scaling isomorphisms mǫ for ǫ ∈ C× from (7) provide an immediate gener-
alization of Theorem 2.4 and Corollary 2.5 to graded Hecke al gebras H( ˜R,ǫk ) ⋊ Γ
such that k is real valued and ǫ ∈ C. To retain the formulation of Theorem 2.4 one
must modify the notions tempered and discrete series, in the sense that everywhere
in Section 1.5 one must use ǫa− instead of a−. Let us call this ǫ-tempered and
ǫ-discrete series. We can also consider the family of algebra s
{
H( ˜R,ǫk ) ⋊ Γ |ǫ ∈ C
}
.
22
For every ǫ ∈ C the analytic families of H( ˜R,ǫk ) ⋊ Γ-representations
{πm∗
ǫ (ρw)(λ) |w ∈ ⟨W′⟩,λ ∈ tρw/W′
ρw }
fulﬁll Corollary 2.5. We note that the matrix coeﬃcients of πm∗
ǫ (ρw)(λ) depend
algebraically onǫ andλ. More speciﬁcally, by (45) the S(t∗)-weights ofπm∗
ǫ (ρw)(−ǫµ)
lie in Hom( ZR, Zkǫ) ⊂ tR and depend linearly on ǫ.
Next we generalize Section 2.1 to certain complex parameter functionsq. As the
analogue of a line ǫR we use a one-parameter subgroup of C×. We consider qǫ for a
positive parameter function q and ǫ ∈ C. Then (23) becomes
ku,ǫ,α =
(
logqα∨/2 + (1 +α(u)) logqα∨
)
ǫ/2 α ∈Ru.
Notice that ǫ = 0 corresponds to the algebra H(R,q 0) ⋊ Γ = C[X] ⋊W′, which we
understand very well. On the other hand, for ǫ ∈iR \ {0} the parameter qα∨ can be
a root of unity (unequal to 1), in which case the aﬃne Hecke alg ebra H(R,q ) can
diﬀer substiantially from those with positive parameters. T herefore we assume that
ℜ(ǫ) ⁄= 0.
Theorem 2.6. Theorem 2.2 and Lemma 2.3 also hold for parameter functions qǫ
with q positive and ǫ ∈ C \iR. For the interpretation of Theorem 2.2 we have to
replace a− by ǫa−, Trs by exp(ǫa) and tempered by ǫ-tempered.
Moreover we can choose the required analytic families of H(R,q ǫ)⋊Γ -representations
such that the matrix coeﬃcients of the representations depe nd analytically on ǫ and
all A-weights depend polynomially on the variables
{
q±ǫ/2
α∨ |α∨ ∈R∨
nr
}
.
Proof. Every t ∈ T can be written uniquely as t = uc with u ∈ Tun and
c ∈ exp(ǫa), since ℜ(ǫ) ⁄= 0. In this setting Theorem 1.2 remains valid. Moreover
ku,ǫ,,α ∈ǫR and ⟨α,λ ⟩ ∈ǫR for all α ∈R and λ ∈ǫa, so ⟨α,ǫ a⟩ and ⟨α,ǫ a⟩ +ku,ǫ,α
have positive distance toπiZ\{0}. This ensures that Theorem 1.3 applies to all λ in a
suitable tubular neighborhood of ǫa in t. Its part (b) tells us that ˆH(R,q ǫ)W ′u exp(λ)⋊
Γ is Morita equivalent to ˆH( ˜RP (u),ǫk P (u))W ′
ZP (u)λ ⋊W′
P (u), while H( ˜RP (u),ǫk P (u)) is
isomorphic to a graded Hecke algebra with real parameter fun ctionkP (u) by means
of mǫ. To H( ˜RP (u),k P (u)) we can apply Theorem 2.4, which gives us Theorem 2.2
for H ⋊ Γ-representations with central character in W′u exp(ǫa). Combining these
results for all u ∈Tun yields the map
ζ∨ :G(H(R,q ǫ) ⋊ Γ) →G(X ⋊W′).
It makes Theorem 2.2 true for qǫ, because it does so on all sets u exp(ǫa).
Let us construct the required analytic families of H(R,q ǫ) ⋊ Γ-representations.
We start with (42) and let σ be any of the σw,i. With Theorem 1.3 we transfer
the HP ⋊ Γ σ-representation to a tempered representation ˜ σ of HP (u) ⋊ ˜Γ, for a
suitable subgroup ˜Γ ⊂ W′. Taking for u the unitary part of an A-weight of σ,
we can achieve that ˜ σ has real central character. Then m∗
ǫ (˜σ) is an ǫ-tempered
representation of H( ˜RP (u),ǫk P (u)) ⋊ ˜Γ. Now Theorem 1.3 in the opposite direction
23
yields an ǫ-tempered representation of H(RP, (qP )ǫ) ⋊ Γ σ, which we call m∗
ǫ (σ). We
claim that the analytic families of H(R,q ǫ) ⋊ Γ-representations
{πm∗
ǫ (σw,i)(t) |w ∈ ⟨W′⟩, 1 ≤i ≤c(w),t ∈T σw,i/Gσw,i }
fulﬁll Lemma 2.3. By construction ζ∨(πm∗
ǫ (σw,i)(t)) equals ζ∨(σw,i)(t). In view of
Lemma 2.3 and since Theorem 2.2 holds for q and qǫ, this implies the claim.
In view of [Sol3, (4.6)], m∗
ǫ (σ) is also the composition of σ with the algebra
homomorphism ρǫ from [Sol3, Proposition 4.1.2]. Although in [Sol3] the auth or
assumed that ǫ ∈ [−1, 1], the relevant calculations remain valid for ǫ ∈ C \iR. This
shows that the matrix coeﬃcients of m∗
ǫ (σ) depend analytically on ǫ. More precisely,
for every v ∈ W e the operator πm∗
ǫ (σw,i)(t,N v) depends in a complex analytic way
on ǫ and t.
By (34) all A-weights of πσw,i (t) are of the form γ(tuc) where γ ∈W′ and uc is
a weight of σw,i with unitary part u ∈Tun and absolute value c ∈Y ⊗ZqZ/2. This
in turn implies that all A-weights of πm∗
ǫ (σw,i)(t) are of the form
γ(tucǫ) cǫ ∈qǫZ/2, (46)
and in particular that (for ﬁxed t) they depend polynomially on
{
q±ǫ/2
α∨ | α∨ ∈
R∨
nr
}
. ✷
Since the whole situation depends in complex analytic fashi on on ǫ, it is natural
to expect that Theorem 2.6 extends to all but ﬁnitely many ǫ ∈ C. Indeed this is
known when q is an equal parameter function [KaLu], but the methods of thi s paper
are insuﬃcient to prove it.
