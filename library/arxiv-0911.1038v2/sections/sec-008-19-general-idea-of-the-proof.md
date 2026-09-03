---
doc_id: arxiv-0911.1038v2
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS"
section_id: sec-008-19-general-idea-of-the-proof
section_title: "General idea of the proof"
section_number: 1.9
pages: 7-12
source_pdf: 0911.1038v2.pdf
source_sha256: 3bc566efaefd44c6
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS: STRUCTURE OF KEROV CHARACTER POLYNOMIALS — We study asymptotics of characters of the symmetric groups on a ﬁxed conjugacy class."
---
symmetric functionk(µ) := |µ| + 2g − 1 = p1(µ) + 2g − 1, therefore for
a given symmetric functions fg andhg we can deﬁne symmetric functions
˜fg(µ) := k(µ)
( k(µ )+1
3
)
fg(µ) and ˜hg(µ) := k(µ)
( k(µ )+1
3
)
hg(µ). We notice
that in equations (4) and (5) we sum over all partitions µ which satisfy
k(µ) = k. Therefore the following proposition is an immediate conse -
quence of Theorem 1.1.
Proposition 1.2. For anyg ≥ 1 there exist inhomogeneous symmetric func-
tions ˜fg and ˜hg, having maximal degree 4g, such that
kK k,k +1−2g =
∑
|µ |=k+1−2g
(
l(µ) + 2g − 2
)
! ˜fg(µ)Rµ
=
∑
|µ |=k+1−2g
(2g − 1)l(µ ) ˜hg(µ)Qµ,
where ˜fg(µ) = ˜fg(µ1,µ 2,... ) and ˜hg(µ) = ˜hg(µ1,µ 2,... ). These symmet-
ric functions are independent ofk.
In fact, the opposite implication holds true as well and Theo rem 1.1 is
a consequence of Proposition 1.2: roughly speaking we will s how that the
symmetric functions ˜fg and ˜hg are divisible by the polynomialk
( k+1
3
)
. One
can notice that Proposition 1.2 stated that ˜fg and ˜hg are independent ofk, so
the divisibility which we will show is a divisibility of symm etric functions
˜fg and ˜hg by the symmetric function K which has a property that for any
partitionµ such that |µ| =k+1 −2g we have thatK(µ) = k
( k+1
3
)
. We shall
explain precisely what this divisibility means and show in S ection 3 that it
8 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
holds indeed by studying the arithmetic properties of Kerov polynomials
and their divisibility by prime numbers.
The remaining difﬁculty is to prove Proposition 1.2. We shal l do it in
Section 2 by analysis of the Goulden-Rattan formula.
Section 4 is a presentation of technical and complicated proofs of lemmas
which are used in the previous sections.
2. G OULDEN -RATTAN FORMULA AND EXISTENCE OF SYMMETRIC
POLYNOMIALS
2.1. Power seriesPλ. Following Goulden and Rattan [GR07] we deﬁne
(6) C(t) = 1
1 −∑
i≥2 Riti =
∑
µ
t|µ |l(µ)! Rµ.
LetD =t d
dt and deﬁne form ≥ 1
Pm(t) = − 1
m!C(t)
(
D +m − 2
)
C(t) · · ·
(
D + 1
)
C(t)DC (t).
For example, we have
P1(t) = −C(t),
P2(t) = −1
2C(t)DC (t),
P3(t) = −1
6C(t)(D + 1)C(t)DC (t)
= −1
6
[
C(t)DC (t)DC (t) +C(t)2DC (t)
]
= −1
6
[
C(t)D
(
C(t) ·DC (t)
)
+C(t)2DC (t)
]
= −1
6
[
C(t)
(
DC (t)
) 2
+C(t)2D2C(t) +C(t)2DC (t)
]
.
Finally, for a partitionλ, we writePλ (t) =∏ l(λ )
j=1Pλ j (t).
Forp = (p0,...,p l) ∈ Nl+1 we deﬁne
E(p) := C(t)p0DC (t)p1 · · ·DC (t)pl.
Lemma 2.1.
(a) Let p ∈ Nl+1,q ∈ Nm+1 and denote by |p| := p0 + · · · +pl (|q| =
q0 + · · ·qm respectively). Then
E(p) ·E(q) =
∑
r∈Nl+m+1,
|r|=|p|+|q|
cp,q
r E(r),
wherecp,q
r ∈ Z.
STRUCTURE OF KEROV CHARACTER POLYNOMIALS 9
(b) For any partition λ the fraction Pλ (t)
C(t) is a linear combination of
termsE(p) wherep ∈ Nk such that |p| = |λ| − 1 andk ≤ |λ| −
l(λ) + 1.
Proof. Let p = (p0,...,p l) ∈ Nl+1, q = (q0,...,q m) ∈ Nm+1. We will
show part (a) by induction onl. It is obvious forl = 0. Forl = 1 we have:
E(p) ·E(q) = E(p0,p 1 +q0,q 1,q 2,...,q m) −E(p0 +p1,q 0,q 1,...,q m)
by the Leibniz rule. Let us assume, that the inductive assert ion holds for
somel ≥ 1 and let p = (p0,...,p l+1). Then by the Leibniz rule we have
that
(7) E(p) ·E(q) = C(t)p0D [E(p′) ·E(q)] −C(t)p0+p1 [E(p′′) ·E(q′)],
wherep′ = (p1,...,p l+1),p′′ = (0,p 2,...,p l+1),q′ = (0,q 0,...,q m). By
the inductive assertion, the right hand side of (7) is equal to
∑
α ∈Nl+m+1,
|α |=|p|+|q|−p0
cαC(t)p0DE(α) −
∑
β ∈Nl+m+2,
|β |=|p|+|q|
cβE(β),
wherecα,c β ∈ Z. But it means that
E(p) ·E(q) =
∑
r∈Nl+m+2,
|r|=|p|+|q|
cp,q
r E(r),
wherecp,q
r ∈ Z which ﬁnishes the proof of part (a).
For part (b) we notice that each functionPm(t) is a linear combination of
E(p), wherep ∈ Nk, |p| =m andk ≤m − 1 and we apply part (a). □
2.2. Polynomial structure of coefﬁcients ofPλ .
Deﬁnition 2.2. Iff is a symmetric function of degree d and 2g ≥ 2 is an
integer then the formal power series
(8) F (t) =
∑
µ
t|µ |(
l(µ) + 2g − 2
)
!f (µ) Rµ
will be called a power-sum of the ﬁrst kind with degree d and genusg and
the formal power series
(9) F (t) =
∑
µ
t|µ |(2g − 1)l(µ )f (µ) Qµ
will be called a power-sum of the second kind with degreed and genusg.
Lemma 2.3.
(a) C(t) is a power-sum of the ﬁrst (respectively, second) kind with de-
gree 0 and genus 1.
10 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
(b) If F (t) is a power-sum of the ﬁrst (respectively, second) kind with
degreed and genus g then DF (t) is a power-sum of the ﬁrst (re-
spectively, second) kind with degreed + 1 and genusg.
(c) If F (t) is a power-sum of the ﬁrst (respectively, second) kind with
degree d and genus g then C(t)F (t) is a power-sum of the ﬁrst
(respectively, second) kind with degreed and genusg + 1
2.
Proof. In order to prove point (a) it sufﬁces to notice that
C(t) =
∑
µ
t|µ |l(µ)! Rµ =
∑
µ
t|µ |Qµ.
In order to prove point (b) letF (t) be in the form (8). Then
DF (t) =
∑
µ
t|µ |(
l(µ) + 2g − 2
)
!
[
(p1(µ)f (µ)
]
Rµ
is again of the form (8).
IfF (t) is of the form (9), then
DF (t) =
∑
µ
t|µ |(2g − 1)l(µ )[
(p1(µ)f (µ)
]
Qµ
is again of the form (9) which shows part (b).
For part (c) we can assume that the symmetric function f is equal to
monomial symmetric functionmλ for some partitionλ.
We deﬁne
Cn =
∑
|µ |=n
l(µ)! Rµ =
∑
|µ |=n
Qµ,
Cµ =
∏
i≥2
C mi(µ )
i
mi(µ)!.
The correspondence between these three families (Q,R andC) is given by
Qn =
∑
|µ |=n
(−1)l(µ )(l(µ) − 1)! Cµ,
−Rn =
∑
|µ |=n
(−1)l(µ ) Qµ =
∑
|µ |=n
(−1)l(µ )l(µ)! Cµ.
Following Lassalle, [Las08] we deﬁne the (formal) alphabet A by
Ri = −hi(A), Q i = −pi(A)/i, C i = (−1)iei(A).
Writing
uµ =l(µ)!/
∏
i≥1
mi(µ), ǫ µ = (−1)n−l(µ ), z µ =
∏
i≥1
imi(µ )mi(µ)!,
STRUCTURE OF KEROV CHARACTER POLYNOMIALS 11
the previous relations can be understood in a frame of symmetric functions
theory, and they are merely the classical properties [Mac95, pp. 25 and 33]
pn = −n
∑
|µ |=n
(−1)l(µ )uµhµ/l(µ) = −n
∑
|µ |=n
ǫµuµeµ/l(µ),
en =
∑
|µ |=n
ǫµuµhµ =
∑
|µ |=n
ǫµz−1
µ pµ,
hn =
∑
|µ |=n
z−1
µ pµ =
∑
|µ |=n
ǫµuµeµ.
Using this notation, it sufﬁces to show that for any monomial symmetric
functionmλ and anyg we have
(10)( ∑
µ
t|µ |mλ (µ) (l(µ) + 2g − 2)!
l(µ)! (−1)l(µ )uµhµ
)( ∑
ρ
t|ρ|(−1)l(ρ)uρhρ
)
=
( ∑
ν
t|ν| mλ (ν)
l(λ) + 2g − 1
(l(ν) + 2g − 1)!
l(ν)! (−1)l(ν)uνhν
)
,
because the right hand side is a power-sum of the ﬁrst kind wit h degree |λ|
and genusg + 1
2, and it sufﬁces to show, that for any monomial symmetric
functionmλ and anyg we have
(11)( ∑
µ
t|µ |mλ (µ)(2g − 1)l(µ )(−1)l(µ )z−1
µ pµ
)( ∑
ρ
t|ρ|(−1)l(ρ)z−1
ρ pρ
)
=
( ∑
ν
t|ν|
( 2g − 1
2g
) l(λ )
mλ (ν)(2g)l(ν)(−1)l(ν)z−1
ν pν
)
,
because the right hand side is a power-sum of the second kind w ith degree
|λ| and genus g + 1
2. In order to prove (10) and (11) it is enough to use
Lemma 4.1. □
The main result of this subsection is the following proposition.
Proposition 2.4. Pλ (t)
C(t) is a linear combination of power-sums of the ﬁrst
(respectively, second) kind of genus |λ |
2 and degree at most |λ| −l(λ).
Proof. It is enough to apply Lemma 2.1 and Lemma 2.3. □
12 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
