---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-068-42-links-in-s2s1-and-rozanskys-proposal
section_title: "Links in S2×S1 and Rozansky’s proposal"
section_number: 4.2
pages: 60-63
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
ForM3 = S2×S1, the theory T [M3] is a particular case of ( 3.120) with p = 0 and g = 0,
that is the theory of 3d N = 2 vector multiplet with gauge group G = G = SU (2). In this
47This aspect is a surprising exception to the rule that knot homology is easier than 3-manifold homology.
– 59 –
case TorH1(M3, Z) = 0 and the only independent Wilson loop in T [M3] is the trivial Wilson
loop. Also, there is only one homological block ˆZ0. Therefore, for an arbitrary representation
λ of SU (2), the decomposition ( 4.13) allows to write the Wilson loop Wλ as (4.10):
Wλ = W0⊗H 0;i,j;𝓁
λ . (4.20)
In other words, in this case we expect a factorization
Ha[S2×S1;Kλ,Rλ] =
⨁
i,j,𝓁∈Z
H0;i,j;𝓁
λ ⊗Ha[S2×S1] (4.21)
where the ﬁrst factor on the right-hand side is theS2×S1 analogue of the Khovanov-Rozansky
homology of the corresponding link Kλ colored byRλ. What is Kλ? And, what is Rλ?
As we shall see below, already in this relatively simple case of M3 = S1×S2 the map
between colored knots and links in M3 and the UV line operators Wλ in T [M3] is rather
non-trivial. Since Wilson loops in T [M3] come from M2-branes wrapping the S1 circle of
S1×S2, we expect that the precise dictionary Wλ↔ (Kλ,Rλ) maps λ to a certain link in
M3 that winds around S1, and the total winding number (counted with multiplicities given
byRλ) is equal to |λ|. Regarding M3 = S1×S2 as a special case of the Hopf ﬁbration
(namely, the trivial ﬁbration), in the rest of this section we present evidence for the following
identiﬁcation48
Wλ ↔ (Kλ,Rλ) = “ λ-cable” of the unknot along the Hopf ﬁber (4.22)
Speciﬁcally,λ =□⊗2n corresponds to a link L2n made of 2n copies of the unknot along the
Hopf ﬁber, all colored by the fundamental representation ofSU (2). And (Kλ,Rλ) for general
λ is a linear combination of L2n’s that replicates the decomposition of λ into□⊗2n’s. Such
decomposition is usually referred to as the “cabling formula” (see Appendix B).
Curiously, a similar problem was already considered by Rozansky from a purely math-
ematical point of view in [82]. Speciﬁcally, the Conjecture 6.10 in [82] gives a concrete
description for the homological invariant of the link L2n. We shall verify that Rozansky’s
proposal49 matches exactly with the quantum ﬁeld theory computation if the generators ai
and θi are assigned ﬂavor charges i, that is
degtai = degtθi =i. (4.25)
48Note, in the unreﬁned / decategoriﬁed setting, Kλ is simply the unknot colored byRλ =λ. Although this
is no longer the case in homological world, there is still a close relation between “cabling” and “color” [80,81].
49The Conjecture 6.10 in [82] contains a typo in the description of the ideal Irel. Namely,
aipi(x) =θipi(x) = 0 (4.23)
should be replaced by
aipn−i+1(x) =θipn−i+1(x) = 0. (4.24)
– 60 –
Using the decomposition of tensor products of SU (2) representations, we can write the
expectation value of 2n Wilson loops in T [M3] as a sum over expectation values of Wilson
loops labeled by irreducible representations. Only even representations with highest weight
2l = 0, 2,..., 2n appear in this decomposition:
⟨W□⊗2n⟩ =
n∑
l=0
[( 2n
n−l
)
−
( 2n
n−l− 1
)]
⟨W2l⟩. (4.26)
The expectation value of the Wilson loop W2l in T [M3], which gives the graded Euler char-
acteristic ofHλ,50
∑
i,j,𝓁
(−1)jqit𝓁 dimH0;i,j,𝓁
λ ≡χq,t(Hλ) =⟨W2l⟩≡
ˆZ0(q,t ;W2l)
ˆZ0(q,t )
(4.28)
can be computed using ( 4.17), with T [S1×S2,SU (2)] now being the 3d N = 4 super-Yang-
Mills theory. We obtain
⟨W2l⟩ = (qt)l(1/t;q)l
(q2t;q)l
, (4.29)
and the expectation values of W2l+1 all vanish.
On the other hand, as a vector space, the homological invariantH•(S1×S2,L 2n) proposed
in Conjecture 6.10 of [82] admits a similar decomposition into subspaces of pure x-degree51
H•
Rozansky(L2n) =
n⨁
l=0
Vl⊗ Q[a1,θ 1,a 2,θ 2,...,a l,θl]. (4.30)
Here, Vl is a quotient of the vector space spanned by monomials of x1,...,x 2n, with degree
n−l, by the relations
x2
i = 0 and
2n∑
i=1
xi = 0. (4.31)
It is easy to check that 52
dimVl =
( 2n
n−l
)
−
( 2n
n−l− 1
)
(4.32)
are exactly the coeﬃcients in (4.26). In particular, Vj withj <0 is empty, and the dimension
of V0 is given by the n-th Catalan number. Then
χt(H•) =
n∑
j=0
dimVl· q2n−2j· (t;tq−2)j
(tq−4;tq−2)j
, (4.33)
50In this normalization, we have
⟨W0⟩ = 1, (4.27)
enabling us to directly extract the information about the space Hi,j;𝓁
λ .
51This decomposition doesn’t respect the ring structure as each subspace is not closed under multiplication.
52Basically, there are
( 2n
n−l
)
non-vanishing degree (n−l) monomials, and they are subject to
( 2n
n−l−1
)
inde-
pendent relations, obtained by multiplying ∑
ixi with degree (n−l− 1) monomials.
– 61 –
where we have used the q-degree of the generators,
degqxi = 2 , (4.34)
degqai =− 2i− 2, (4.35)
degqθi =− 2i + 2. (4.36)
If we shift the overall q-degree of H• by−2n units to remove the q2n factor in ( 4.33), what
remains is in perfect agreement with the expectation value of Wilson loops in 3d theory
T [M3]:
⟨W2l⟩ = (qt)j· (1/t;q)j
(tq2;q)j
= q−2j· (t,t q−2)j
(tq−4;tq−2)j
, (4.37)
with a typical relation between q and q [43]:
q2 = qt. (4.38)
So, we have veriﬁed the conjecture by Rozansky at the level of equivariant Euler characteristics
for this link L2n,
χq,t(HBPS) = χq,t(HRozansky) (4.39)
presenting some evidence for the isomorphism between H•
Rozansky(S1×S2,L 2n){−2n} and
Hλ := ⨁
i,j,𝓁∈ZH0;i,j;𝓁
λ with λ =□⊗2n.
As a side remark, positivity also features in the invariantsˆZa(M3;KR) of three manifolds
with knots, in a way similar to the case without knot ( 3.87). For example, in our case of
M3 =S2×S1,
− ˆZ0(q,−t;W6) =
(
2t3 + 2t2)
q3 +
(
2t4 + 4t3 + 4t2 + 2t
)
q4+
(
2t5 + 6t4 + 10t3 + 10t2 + 4t
)
q5 +
(
2t6 + 8t5 + 16t4 + 22t3 + 18t2 + 8t + 2
)
q6+
(
2t7 + 8t6 + 20t5 + 36t4 + 44t3 + 34t2 + 14t + 2
)
q7 +O
(
q8)
(4.40)
has only positive coeﬃcients.
