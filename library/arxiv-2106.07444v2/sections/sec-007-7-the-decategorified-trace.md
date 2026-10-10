---
doc_id: arxiv-2106.07444v2
doc_title: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS"
section_id: sec-007-7-the-decategorified-trace
section_title: "The Decategorified Trace"
section_number: 7
pages: 45-52
source_pdf: 2106.07444v2.pdf
source_sha256: 5acca39c07bcdddd
doc_brief: "FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS — Let W be the W eyl group of a split semisimple group G. Its Hecke category HW can be built from pure perverse sheaves on the double ﬂag variety of G."
---
7.1. To state the main deﬁnition of this section, let W denote an arbitrary ﬁnite
Coxeter group.
As before, HW is the Iwahori–Hecke algebra of W . Moreover, we will draw freely
upon the notation introduced in Appendix A:
• R(W ) is the representation ring of W .
• QW ⊆ ¯Q is the splitting ﬁeld of W .
• (−, −)W :R(W ) ×R(W ) → Z be the multiplicity pairing.
• We write
[Sym(V)]q =
∑
i
qi Symi(V).
• If φ :W → QW is an irreducible character, then φq :HW (q
1
2 ) → QW (q
1
2 )
is the corresponding Z[q± 1
2 ]-linear trace.
• {−, −} : ˆW × ˆW → QW is the symmetric pairing (derived from) Lusztig’s
exotic Fourier transform.
Deﬁnition 7.1.1. For any ﬁnite Coxeter groupW , theR(W ) trace on its Iwahori–
Hecke algebra is the Z[q± 1
2 ]-linear trace
⟨−⟩ q :HW →R(W ) ⊗ QW (q
1
2 )
deﬁned by
⟨β⟩ q =
∑
φ,ψ∈ ˆW
{φ,ψ }φq(β)ψ
for all β ∈HW .
In the next two subsections, we assume that W is still a Weyl group and prove
Theorem 5, which relates the R(W ) trace to the decategoriﬁcation of the AW trace.
In the remainder of the section, we allow W to be an arbitrary ﬁnite Coxeter group
and relate the R(W ) trace to the Markov trace studied by Ocneanu and Gomi.
We conclude by proving Propositions 7.5.1 and 7.5.5, which roughly generalize
rationality and symmetry properties of the Markov trace.
7.2. Recall that an object of Modb
2( ¯Qℓ[W ]) is a ¯Qℓ[W ]-module equipped with a
W -invariant bigrading where the ﬁrst grading is bounded belo w and the second is
bounded. We have an additive map
AH :HW
∼
− →[HW ]△ → [Modb
2( ¯Qℓ[W ])]⊕
induced by the composition
Hop
W
AH
− − →Modb
2(AW ) → Modb
2( ¯Qℓ[W ]),
where the second arrow is the forgetful functor. Note that Modb
2( ¯Qℓ[W ]) is semisim-
ple, since ¯Qℓ[W ] is.
For any ring R, such as R =R(W ), we write R( (q
1
2 ) ) =R[ [q
1
2 ] ][1
q ]. Let
[−]q : [Mod1,1( ¯Qℓ[W ])]⊕ →R(W )( (q
1
2 ) )
46 MINH-TÂM QUANG TRINH
be the additive map deﬁned by
[M ]q =
∑
i,j
(−1)i−jq
j
2Mi,j.
We say that [M ]q is the q-graded character of M . For all i,j , let
(AH∨)i,j(−) = Hom ¯Qℓ (AHi,j(−), ¯Qℓ).
Then the composition
[AH∨]q := [−]q ◦ AH∨ :HW →R(W )( (q
1
2 ) )
is Z[q± 1
2 ]-linear.
7.3. Recall from Section 2 that {γw}w denotes the Kazhdan–Lusztig basis of the
Iwahori–Hecke algebra. Then Theorem 5 reduces to the claim that:
[AH∨(ICw)]q = ⟨γw⟩ q · [Sym(V)]q
for all w ∈ W . To prove it, we use a multiplicity formula for unipotent cha racter
sheaves, derived from [ L85-III, Cor. 14.11] and [ L85-V, Thm. 23.1].
As in § 2.5, let [ C(G0)]⊕ be endowed with the action of Z[q
1
2 ] in which q
1
2 acts
by ⟨− 1⟩ . The following version of the formula is the one quoted in [ WW08, 413],
ﬁxed to incorporate semisimpliﬁcation.
Theorem 7.3.1 (Lusztig). For all w ∈W , we have
[CH(ICw)ss] =
∑
φ,ψ∈ ˆW
{φ,ψ }φq(γw)[Gψ] + cuspidal terms
in [C(G0)]⊕, where “cuspidal terms” refers to the contribution of simpl e objects
not of the form Gψ for some ψ ∈ ˆW , and “ ss” refers to the semisimpliﬁcation of
(shifted) perverse summands.
Proof of Theorem 5. By an argument similar to the proof of the second equivalence
in Lemma 6.3.1, Theorem 3.3.1 implies that for all i,j ∈ Z, we have
grw
j Homi(Sψ, S) ≃
{
Vψ ⊗ Sym
i
2 (V) i =j
0 i ⁄=j
as representations of W . So Theorem 7.3.1 yields
[AH∨(ICw)]q =
∑
i,j
(−1)i−jq
j
2 grw
j Homi(i∗CH(ICw)⟨−r⟩, S)∨
=
∑
i,j
(−1)i−jq
j
2
∑
φ,ψ∈ ˆW
{φ,ψ }φq(γw) grw
j Homi(Sψ, S)∨
=
∑
φ,ψ∈ ˆW
{φ,ψ }φq(γw)
∑
i
q
i
2 (ψ ⊗ Sym
i
2 (V))∨.
Every representation of W is self-dual because QW = Q ⊆ R, so the inner sum in
the last expression simpliﬁes to ψ · [Sym(V)]q. □
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 47
7.4. We now relate ⟨−⟩ q to Markov traces.
The HOMFL Y series of a link λ ⊆ R3 is one of the predecessors of the isotopy
invariant mentioned in Remark 6.1.1. We will denote it by
[λ]a,q ∈ Z[(q
1
2 − q− 1
2 )±1,a ±1].
We have [λ]a,q = P(λ)|t=−1, where P is the invariant in the remark. With this
normalization, the HOMFLY series of the unknot equals 1.
There are many diﬀerent constructions of the HOMFLY invaria nt [ HOMFLY].
Ocneanu’s approach relies on Alexander’s theorem, stating that every link in R3 is
the closure of a braid. Namely, one constructs for each n ≥ 1 a certain function on
the Iwahori–Hecke algebra of Sn, now known as a Markov trace [ J]. If Brn denotes
the braid group of Sn, i.e., the group of topological braids on n strands, and λ is
the closure of β ∈ Brn, then the HOMFLY series of λ is the Markov trace of β,
multiplied by a factor depending only on |β| and n.
Y. Gomi generalized Ocneanu’s Markov traces in a uniform way beyond type
A, extending work of Geck–Lambropoulou in type BC [G]. We follow Gomi’s
conventions here.
Let (W,S ) be any ﬁnite Coxeter system. Recall from § A.4 that if S′ ⊆ S and
W ′ ⊆W is theS-parabolic subgroup generated byS′, thenHW ′ ⊆HW . A Markov
trace on HW is a Z[q± 1
2 ]-linear function
tr :HW → Z[q± 1
2 ](a)
such that:
(1) tr(1) = 1.
(2) For all β,γ ∈HW , we have tr(βγ ) = tr(γβ ).
(3) For all s ∈ S and γ ∈ HW ′ , where W ′ is the S-parabolic subgroup of W
generated by S \s, we have
tr(σ±1
s γ) = −a∓1
(
q
1
2 − q− 1
2
a −a−1
)
tr(γ).
Axioms (2) and (3) are respectively known as the ﬁrst and seco nd Markov moves.
Theorem 7.4.1 (Ocneanu). The axioms above uniquely deﬁne a Markov trace on
the Iwahori–Hecke algebra of Sn for all n ≥ 1. For all β ∈ Brn, we have
[ ˆβ]a,q = (−a)|β|
( a −a−1
q
1
2 − q− 1
2
)n−1
tr(β),
where ˆβ is the link closure of β.
Suppose that a Markov trace on HW exists. After base change from Z[q± 1
2 ] to
QW (q
1
2 ), we can view it as a trace on HW (q
1
2 ) (see § A.7). Then
tr =
∑
φ∈ ˆW
trφφq
for some weights trφ ∈ QW (q
1
2,a ).
48 MINH-TÂM QUANG TRINH
Axioms (1)-(3) show that tr|a−2=0 is the symmetrizing trace τq : HW (q
1
2 ) →
Z[q± 1
2 ]. Proposition A.9.3 then suggests that the weights trφ should involve bivari-
ate Molien series. These observations motivate the form of G omi’s Markov weights.
Below, let V be a realization of W such that VW = 0, and for all ψ ∈ ˆW , let
mψ(q,x ) =
∑
i,j
(−x)iqj (ψ, Λi(V) ⊗ Symj(V))W.
By construction, mψ(q, 0) = mψ(q), the usual Molien series of ψ.
Theorem 7.4.2 (Gomi). The weights
trφ =
( 1 − q
1 −a−2
)r ∑
ψ∈ ˆW
{φ,ψ }mψ(q,a −2)
deﬁne a Markov trace on HW for any ﬁnite Coxeter group W of rank r.
This is a bivariate reﬁnement of Proposition A.9.3.
Henceforth, tr denotes Gomi’s Markov trace. To relate it to the R(W ) trace, we
introduce the normalization
⟨β⟩ 0
q = (−q
1
2 )|β|⟨β⟩ q ·ε[Sym(V)]q,
where ε denotes the sign character of W (see § A.5). We emphasize that whenever
we use ⟨−⟩ 0
q, we always assume that VW = 0. For Weyl groups, the result below
follows from Theorems 6.2.1 and 5.
Proposition 7.4.3. Under the hypotheses of Theorem 7.4.2, we have
tr(β) = ( −q− 1
2 )|β|
( 1 − q
1 −a2
)r∑
i
(−a2)i(Λi(V), ⟨β⟩ 0
q)W
for all β ∈ BrW .
Lemma 7.4.4. We have
1
(1 −x−1)r
∑
i
(−x−1)i Λi(V) = ε
(1 −x)r
∑
i
(−x)i Λi(V)
in R(W )(x).
Proof. Use the identity Λ r−i(V) = ε Λi(V). □
Proof of Proposition 7.4.3. By Lemma 7.4.4 and the self-duality of Sym( V),
trφ =
( 1 − q
1 −a2
)r ∑
ψ∈ ˆW
{φ,ψ }
∑
i,j
(−a2)iqj(Λi(V),εψ · Symj(V))W.
Comparing with the terms that make up ⟨−⟩ 0
q, we get the result. □
Corollary 7.4.5. Under the hypotheses of Theorem 7.4.2, we have
τq = (−q− 1
2 )|β|(1 − q)r(ε, ⟨β⟩ 0
q)W
as Z[q± 1
2 ]-linear traces on HW .
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 49
Corollary 7.4.6. Under the hypotheses of Theorem 7.4.1, we have
[ ˆβ]a,q = (aq− 1
2 )|β|−n+1 ∑
0≤i≤n−1
(−a2)i(Λi(V), ⟨β⟩ 0
q)W
for all β ∈ Brn.
7.5. To conclude this section, we prove:
(1) Proposition 7.5.1, a rationality result that will simplify the proof of Theo-
rem 9 in Section 8.
(2) Proposition 7.5.5, a symmetry result. Together with (1) and Theorem 9, it
implies Theorem 6, as we will also explain.
These results about the R(W ) trace respectively generalize, and are inspired by,
the following facts about the HOMFLY series:
(1′) HOMFLY has integer coeﬃcients. Moreover, it is a q
1
2 -monomial shift of
an element of Z[ [q] ][a±1], not just of Z[ [q
1
2 ] ][a±1].
(2′) HOMFLY is invariant under q
1
2 ↦→ −q− 1
2 .
Note that the second claim of (1 ′) can be proved via the Markov trace, while (2 ′) is
a consequence of the HOMFLY skein relation (see [ DGR, §2.4], noting that their q
is our q
1
2 ). By contrast, the proofs below are representation-theore tic. Throughout,
we assume that the realization V satisﬁes VW = 0.
7.5.1. Let d1,...,d r be the invariant degrees of the W -action on V. Let:
q0 =
{
q
1
2 W has a factor of type E7 or E8
q else
(20)
The reason we make an exception for E7 andE8 is the existence of so-called excep-
tional characters in these types. See [ GP, §9.5] and the references therein.
Proposition 7.5.1. For all β ∈ BrW , we have
⟨β⟩ q ∈ (q− 1
2 )|β|R(W )[q0],
⟨β⟩ 0
q ∈ 1
(1 − qd1) · · · (1 − qdr )R(W )[q0],
(1, ⟨β⟩ 0
q)W ∈ 1
(1 − qd1) · · · (1 − qdr ) (1 + q0Z[q0]).
Proof. Let ˜β = q
|β|
2 β. To prove the ﬁrst statement, we must show that
(ψ, ⟨ ˜β⟩ q)W =
∑
φ∈ ˆW
{φ,ψ }φq( ˜β) ∈ QW (q
1
2 )
actually belongs to Z[q0] for all ψ ∈ ˆW . We make a series of reductions:
By Lemma-Postulate A.9.1(1), we can assume that W is irreducible.
We can expand ˜β as a Z[q]-linear combination of the elements ˜σw = q
|σw |
2 σw for
w ∈W . So we can assume that ˜β = ˜σw for some w.
We can now check the non-crystallographic types case by case , using [ GP, §8.3]
and [ L94] for the dihedral types, [ GP, Table 9.1] and [ BM93, §7] for type H3 (but
see Remark 7.5.4, below), and [ AL, M] for type H4. So we can assume that W is
crystallographic.
50 MINH-TÂM QUANG TRINH
Theorem 5 implies that ( ψ, ⟨ ˜β⟩ q)W ∈ Z[q± 1
2 ]. So it remains to show that
(ψ, ⟨ ˜β⟩ q)W ∈ Q[q0]. Since {−, −} takes values in QW = Q, it is enough to get
φq(˜σw) ∈ Q[q0] for all φ. For crystallographic irreducible W , this is a theorem of
Benson–Curtis [ BC] (joint with Springer in the case of E7 and E8).
The remaining two statements follow from the ﬁrst statement , once we establish
the following two lemmas. □
Lemma 7.5.2. We have
[Sym(V)]q ∈ 1
(1 − qd1 ) · · ·(1 − qdr )R(W )[q].
Proof. In the notation of § A.6 and § A.8, we have
[Sym(V)]q = m1(q)
∑
φ∈ ˆW
Fegφ(q)φ,
where m1(q) =∏
i (1 − qdi )−1 and Fegφ(q) ∈ Z[q] for each φ. □
Lemma 7.5.3. For all β ∈ BrW , we have (ε, ⟨β⟩ q)W =εq(β) = ( −q− 1
2 )|β|.
Proof. By [ GP, 252], we have εq(σs) = −q− 1
2 for all s ∈S. (Note that Ts = q
1
2σs
in the notation of ibid..) But εq is the character of a 1-dimensional QW (q
1
2 )-vector
space, so it is multiplicative on BrW . We deduce that εq(β) = ( −q− 1
2 )|β| for all
β ∈ BrW .
As for the other equality: By [ L84-1, Ch. 4], we have {φ,ε } = 0 for all φ ⁄= ε.
This implies (ε, ⟨β⟩ q)W =εq(β). □
Remark 7.5.4. The proof of Proposition 7.5.1 uses the explicit description of the
exotic Fourier transform in type H3. For this group, there are three nontrivial
families (see § A.10), one of which is exceptional. The 4 × 4 matrix in [ BM93, §7]
represents the block of the Fourier matrix for the non-excep tional families. I learned
from George Lusztig that by contrast, the data for the except ional family matches
that of the exceptional family in type E7. The assertion in [ GM, 189] that all three
families have the same Fourier data is incorrect.
7.5.2. Turning to the symmetry result:
Proposition 7.5.5. For all β ∈ BrW , we have
⟨β⟩ q ∈R(W )[q
1
2 −εq− 1
2 ],
⟨β⟩ 0
q ∈ (q
1
2 )|β|−rR(W )[(q
1
2 − q− 1
2 )±1].
By Proposition 7.5.1, ⟨−⟩ q takes values in R(W )[q± 1
2 ], so the proof amounts to
the following lemmas:
Lemma 7.5.6. For all β ∈ BrW , we have ⟨β⟩ q ↦→ε⟨β⟩ q under q
1
2 ↦→ −q− 1
2 .
FROM THE HECKE CATEGORY TO THE UNIPOTENT LOCUS 51
Proof. Recall that for all β ∈ HW , we have ( ψ, ⟨β⟩ q)W = ∑
φ∈ ˆW {φ,ψ }φq(β).
Using Lemma-Postulate A.9.1(3), we compute
(ψ,ε ⟨β⟩ q)W = (εψ, ⟨β⟩ q)W
=
∑
φ
{φ,εψ }φq(β)
=
∑
φ
{εφ,εψ }(εφ)q(β)
=
∑
φ
{φ,ψ }(εφ)q(β).
It remains to show that if β is in the image of BrW , then
φq(β) ↦→(εφ)q(β) under q
1
2 ↦→ −q− 1
2.
This follows implicitly from the proof of [ GP, Prop. 9.4.1(a)]. □
Lemma 7.5.7. We have q
r
2 [Sym(V)]q ↦→εq
r
2 [Sym(V)]q under q
1
2 ↦→ −q− 1
2 .
Proof. Observe that∑
i (−q)i Λi(V) is the multiplicative inverse of [Sym( V)]q. So
the claim follows from Lemma 7.4.4 with x = q. □
7.5.3. We show that Proposition 7.5.1, Proposition 7.5.5, and Theorem 9 together
imply Theorem 6.
Proof of Theorem 6. Proposition 7.5.1 shows that if W has no factors of type E7
or E8, then ⟨β⟩ 0
q and (1, ⟨β⟩ 0
q)W are indeed rational functions in q, not just power
series in q
1
2 . Theorem 9 extends this result to all W . These results, combined with
Proposition 7.5.5, establish
⟨β⟩ q ∈ q− |β|
2 R(W )[q] ∩R(W )[q
1
2 −εq− 1
2 ],
⟨β⟩ 0
q ∈R(W )[ [q] ]∩R(W )(q) ∩ (q
1
2 )|β|−rR(W )[(q
1
2 − q− 1
2 )±1].
In particular, the q-degrees of ⟨β⟩ 0
q and (1, ⟨β⟩ 0
q)W are well-deﬁned. The following
observations show that their degrees must be |β| −r:
• Proposition 7.5.1 shows that ⟨β⟩ 0
q, and hence (1 , ⟨β⟩ 0
q)W , belong to Z[ [q] ],
i.e., their lowest-order term in q is the constant term.
• By Proposition 7.5.5, we have
⟨β⟩ 0
q ↦→(−q)r−|β|⟨β⟩ 0
q under q0 ↦→q−1
0 .
• Proposition 7.5.1 also shows that (1, ⟨β⟩ 0
q)W , and hence ⟨β⟩ 0
q, have nonzero
constant term. □
52 MINH-TÂM QUANG TRINH
