---
doc_id: arxiv-1110.6212v2
doc_title: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗"
section_id: sec-005-24-characters
section_title: "Characters"
section_number: 2.4
pages: 14-16
source_pdf: 1110.6212v2.pdf
source_sha256: 1923b6a0bfdc810f
doc_brief: "On calibrated representations and the Plancherel Theorem f or affine Hecke algebras James Parkinson ∗ — This paper has two main purposes."
---
with tα∨
1 = q−1
1 and tα∨
2 = q2, speciﬁcally tω1 = q−1
1 q2 and tω2 = ±q−1/2
1 q2. The corresponding
matrices for xω1 and xω2 are
π(xω1) = diag( q−1
1 q2, q−1
2 , q−1
2 ) π(xω2) = ±diag(q−1/2
1 , q−1/2
1 , q1/2
1 q−1
2 ).
In the cases q1 = q2 or q1 = q2
2 an analogous computation to that in Example 2 can be used to
construct (non-calibrated) irreducible representations of H (q, q) and H (q, q2).
2.4 Characters
We conclude this section with some observations about chara cters that will be used for the
Plancherel Theorems. Let ft(h) be as in (1.11).
Lemma 2.8. Let π be an irreducible representation of HL with central character t, and suppose
that the character χ of π satisﬁes
χ(τwxλ) = δw,1
∑
v∈W0
kv(vt)λ for all w ∈ W0 and λ ∈ L,
for some numbers kv ∈ C. Then, with ft as in (1.11), if t is regular we have
χ(h) =
∑
v∈W0
kvfvt(h) for all h ∈ HL.
Proof. Since t is regular each fvt(h) with v ∈ W0 and h ∈ HL is deﬁned. From Remark 1.2
and the hypothesis we have χ(h) =∑
v∈W0 kvfvt(h) for all h ∈ H ′
L, where H ′
L is the subalgebra
of HL with basis {τwxλ | w ∈ W0, λ ∈ L}. Let ∆( x) = ∏
α∈R0(1 − x−α∨
) = d(x)d(x−1). An
induction using the formula (1 − x−α∨
i )Ti = τi + ai(x) shows that ∆( x)ℓ(w)Tw ∈ H ′
L for all
w ∈ W0. Thus ∆( x)ℓ(w)Twxλ ∈ H ′
L for all w ∈ W0 and λ ∈ L. Since ∆( x) ∈ C[L]W0 is central
and χ is irreducible we have
∆( t)ℓ(w)χ(Twxλ) = χ(∆( x)ℓ(w)Twxλ) =
∑
v∈W0
kvfvt(∆( x)ℓ(w)Twxλ) = ∆( t)ℓ(w) ∑
v∈W0
kvfvt(Twxλ).
We can divide through by ∆( t)ℓ(w) since t is regular.
Proposition 2.9. Let χt be the character of the principal series representation M (t) of HL
with central character t. Then
χt(h) =
∑
w∈W0
fwt(h) for all h ∈ HL (2.5)
where the right hand side has an analytic continuation (for ﬁ xed h ∈ HL) to all t ∈ Hom(L, C×).
Proof. Suppose ﬁrst that D(t) = ∅ and that M (t) is irreducible (see Theorem 2.2). Since
D(t) = ∅ the module M (t) has basis {τw ⊗ vt | w ∈ W0}. To see this note that if w = si1 · · ·siℓ
is reduced then the Bernstein relation gives
τw ⊗ vt =
[ ∏
α∈R(w−1)
(1 − tα∨
)
]
(Tw ⊗ vt) + lower terms ,
14
where ‘lower terms’ is a linear combination of terms Tv ⊗ vt with v < w in Bruhat order. Thus
if D(t) = ∅ then each basis element Tw ⊗ vt of M (t) can be written in terms of the elements
{τw ⊗ vt | w ∈ W0}.
From (1.7) we see that the diagonal entries of the matrix for τw are all 0. The matrix for xλ
is diagonal with entries ( wt)λ (w ∈ W0) on the diagonal. Therefore
χt(τwxλ) = δw,1
∑
v∈W0
(vt)λ for all w ∈ W0 and λ ∈ L.
Hence Lemma 2.8 gives (2.5).
The cases where D(t) ⁄= ∅ or M (t) is not irreducible are obtained as follows. For ﬁxed
h ∈ H the the character χt(h) is, by construction, a linear combination of {tλ | λ ∈ L} and is
deﬁned for all t ∈ Hom(L, C×). The right hand side of (2.5) is a rational function in t. Thus the
singularities of this rational function are removable sing ularities (even though each individual
summand may have singularities).
Proposition 2.10. Suppose that t is a regular character. Let J ⊆ N (t), and let MJ (t) be the
module constructed in Theorem 2.6. Then
χ(h) =
∑
w∈FJ (t)
fwt(h) for all h ∈ H .
Proof. Since τi · ewt = q1/2
i ni(t) esiwt we see that the diagonal entries of the matrix for τw are 0.
Since the matrix representing xλ is diagonal it follows that
χ(τvxλ) = δv,1
∑
w∈FJ (t)
(wt)λ for all v ∈ W0 and λ ∈ L,
and the result follows from Lemma 2.8.
Lemma 2.11. Let π be a 1-dimensional representation of HL with regular central character t.
Then
χ(h) = ft(h) for all h ∈ HL,
unless HL is of type ˜Cn with π(xα∨
n ) = −1. In this case there is a 1-dimensional representation
π′ deﬁned by π′(xλ) = π(xλ) for all λ ∈ L, π′(Ti) = π(Ti) for all i ⁄= n, and π′(Tn) = q1/2
n
(respectively −q−1/2
n ) if π(Tn) = −q−1/2
n (respectively q1/2
n ). Then
χ(h) + χ′(h)
2 = ft(h) for all h ∈ HL.
Proof. By direct analysis of the deﬁning relations (1.2)-(1.5) one sees that the central character t
of a 1-dimensional representation necessarily has ni(t)ni(t−1) = 0, except in the ˜Cn case with
π(xα∨
n ) = −1. Excluding this case for the moment, it follows from (1.7) t hat π(τi) = 0 and
hence π(τwxλ) = δw,1tλ for all w ∈ W0 and λ ∈ L. Since t is assumed to be regular, Lemma 2.8
gives χ(h) = ft(h) for all h ∈ HL.
Now consider the ˜C2 case with π(xα∨
n ) = −1. Let π′ be the companion representation deﬁned
in the statement of the lemma. The proof of Lemma 2.8 applied t o the representation π ⊕ π′
proves the result. The fact that π ⊕ π′ is not irreducible does not eﬀect the proof of Lemma 2.8
because the centre C[L]W0 of HL acts by the same scalar on each of π and π′.
15
Remark 2.12. In Proposition 2.10 and Lemma 2.11 we assumed that t is a regular central
character. In general these results are false for non-regul ar central characters, even if each term
ft(h) is deﬁned. For example consider the ˜G2 case with t ∈ Hom(Q, C×) given by tα∨
1 = q1,
tα∨
2 = q−1
2 . If q1 ⁄= q2 and q1 ⁄= q2
2 and q2
1 ⁄= q3
2 and q1 ⁄= q3
2 then this central character is
regular, and by Lemma 2.11 we have ft(h) = χ4(h) for all h ∈ H , where χ4 is the 1-dimensional
representation of H listed in Section 3.6. Suppose that q1 = q2 = q. A calculation similar
to Remark 1.2 shows that ft(h) is deﬁned for all h ∈ H , and that ft(T1T2T1) = q1/2. But
χ4(T1T2T1) = −q1/2.
