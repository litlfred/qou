---
doc_id: s0025-5718-07-02027-3
doc_title: "Li(p)-service? An algorithm for computing p-adic polylogarithms"
section_id: sec-005-5-method-of-computation-on-u1
section_title: "Method of computation on U1"
section_number: 5
pages: 8-11
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
toc_source: outline
doc_brief: "Li(p)-service? An algorithm for computing p-adic polylogarithms — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
To compute Lin(z) for z̸ = 1 in U1 we use the following result.
Proposition 5.1 ([7, Proposition 7.1]). For n ≥2 the function
(5.2)
En(z) = Lin(z) −
1
n −1 log(z)Lin−1(z)
extends to a rigid analytic function on U1.
(5.3)
En(zm) = mn−1 
for m ≥1 and z in C∗
p. In particular
(5.4)
En(z2) = 2n−1(En(z) + En(−z)) .
Proposition 5.5. On U1 the functions En(z) are independent of the branch of the
logarithm.
Proof. It is easy to check that for n ≥3 we have (n −1)E′
n (z)| ≤1.
Proof. This is a slight generalization of [3, Proposition 2.1], with the same proof.
We use a formula found by Coleman [7, Lemma 7.2],
x−ndµz(x) ,
p
1−zpk for a = 1, . . . , pk.
Since for the speciﬁed values of z this measure takes values with absolute value at
most 1, the same holds for Li(p)
n (z).
□
Corollary 4.9 ([3, Corollary 2.2]). If ζ̸ = 1 is a root of unity of order prime to p,
then Lin(ζ) is in pnZp[ζ].
n (ζ) is in Qp(ζ) by Proposition 4.3, and by Proposition 4.8
we have |Li(p)
n (ζ) is in Zp[ζ]. The result is now immediate from
Proposition 4.2.
□
Proof. For k = 0 this is part of Corollary 4.9. For k > 0 it then follows by induction
since Lin(ζ) = p−nLin(ζp) + Li(p)
n (ζ)| ≤1 by Proposition 4.8.
□
It is then clear that En(z) is deﬁned for z̸ = 0. Moreover, Proposition 2.10(1)
together with the identities log(zm) = m log(z) and log(ζz) = log(z) for a root of
unity ζ implies that we have a distribution relation
En(ζz)
ζm=1
n(z) = (n −2)En−1(z)/z.
Since En(z) is rigid analytic on U1 as stated above, the statement follows by induc-
tion provided that En(1) is independent of the branch. Taking m = p −1 in (5.3)
we see that En(1) is determined by the En(ζ) where ζp−1 = 1 and ζ̸ = 1. But
En(ζ) = Lin(ζ) for such ζ by (5.2), and from Proposition 4.2 and Theorem 2.7 we
ﬁnd that those values are independent of the branch of the logarithm.
□
The Em(z) for z in U1 are much easier to deal with than the Lim(z), and we
express Lin(z) in terms of the Em(z) and logarithms.
Li(p)-SERVICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS
1113
Proposition 5.6. We have, for z̸ = 1 in U1 and n ≥2,
Lin(z) =
1
(n −1)! logn−1(z)Li1(z) +
n

j=2
(j −1)!
(n −1)! logn−j(z)Ej(z) .
Proof. For n ≥2 we get from (5.2) that
(n −1)! En(z) = (n −1)! Lin(z) −(n −2)! log(z)Lin−1(z) .
Setting E1(z) = Li1(z) we have an equality of generating power series in T,

n≥1
(n −1)! En(z)T n = (1 −log(z)T)

n≥1
(n −1)! Lin(z)T n
,
so that

n≥1
(n −1)! Lin(z)T n =

n≥1
(n −1)! En(z)T n
(1 + log(z)T + log2(z)T 2 + · · · ),
and the result follows easily.
□
Remark 5.7. Because log(z) and En(z) are rigid analytic on U1 the second summand
of Lin(z) in Proposition 5.6 is rigid analytic there. But Li1(z) = −log(1 −z) is not
rigid analytic around 1, hence neither are the ﬁrst summand and Lin(z) itself.
However, for n ≥2 we can extend Lin(z) to the whole of Cp by putting Lin(1) =
En(1) (which is independent of the branch of the logarithm by Proposition 5.5).
If F ⊂Cp is any ﬁeld that is ﬁnitely ramiﬁed over Qp, then log(z) is bounded on
F ∗by the formulae in Remark 2.2 (see Remark 8.1), so by Proposition 5.6 this
extended Lin(z) is continuous on F. It follows from this continuity that part (1) of
Proposition 2.10 holds for all z in Cp (cf. [7, Corollary 7.1a]) and part (2) for all
z̸ = 0 in Cp.
We deal with the two summands in the expression for Lin(z) in Proposition 5.6
separately. Computing the logarithms is standard, and we develop the other func-
tion as a power series around 1 using iterated integration as described in the next
proposition. The constant of integration is expressed in terms of Lin(−1), which
we can compute using Propositions 4.2 and 4.3 if p̸ = 2. But if p = 2, then −1 is
outside of the set in Proposition 2.7(3) and we give a diﬀerent formula that we can
calculate as we go along.
Proposition 5.8. For n ≥1 set Gn(t) = logn(1 + t)/n!, and for n ≥2 let
Hn(t) =
n

j=2
(j −1)!
(n −1)! logn−j(1 + t)Ej(1 + t) .
Then Gn(t) and Hn(t) for |t| < 1 are given by power series in Qp[[t]], with Hn(t)
satisfying
H′
2(t) = 1 −t/2 + t2/3 −· · · ,
(5.9)
H′
n(t) = Hn−1(t)
1 + t
+ Gn−1(t)
t
(n ≥3)
(5.10)
as well as
Hn(0) = 2n−1Lin(−1)/(1 −2n−1) .
1114
AMNON BESSER AND ROB DE JEU
If p = 2, then also
Hn(0) = 2n−1
1 −2n (Hn(−2) −Hn(0)) .
(5.11)
Proof. That the Gn(t) for |t| < 1 are given by power series in Q[[t]] ⊂Qp[[t]] is
well-known. By Proposition 5.1 we know that the Em(t + 1) for m = 2, . . . , n are
given by power series in Cp[[t]] that converge for |t| < 1 so that the same holds for
Hn(t). We shall now ﬁrst prove the inductive formulae and then conclude that the
power series are actually in Qp[[t]].
From (2.3) we have that E′
2(z) = −log(z)/(1 −z) so that H′
2(t) = E′
2(t + 1) =
log(1 + t)/t which gives the ﬁrst formula. For m ≥3 we have (m −1)E′
m(z) =
(m −2)Em−1(z)/z so that H′
n(t) for n ≥3 is given by
n−1

j=3
(j −1)!
(n −1)!

(n −j)logn−j−1(1 + t)
1 + t
Ej(1 + t) + j −2
j −1 logn−j(1 + t)Ej−1(1 + t)
1 + t

+ logn−1(1 + t)
(n −1)! t
+ (n −2) logn−3(1 + t)
(n −1)! (1 + t)E2(1 + t) + n −2
n −1En−1(1 + t)
and collecting powers of log(1 + t) this becomes
n−1

j=2
(j −1)!
(n −1)! [(n −j) + (j −1)]logn−j−1(1 + t)
1 + t
Ej(1 + t) + logn−1(1 + t)
(n −1)! t
,
proving the second formula.
As for the constant terms, we see from (5.4) that En(1) = 2n−1(En(1)+En(−1)).
Therefore Hn(0) = En(1) = 2n−1En(−1)/(1 −2n−1), and En(−1) = Lin(−1) since
log(−1) = 0.
If p = 2, then −1 is in U1 so that the deﬁnition of Hn(t) gives
Hn(−2) = En(−1) = Lin(−1) and this leads immediately to the alternative formula
for Hn(0).
Finally, we prove that the coeﬃcients of the Hn(t) are in Qp. For p̸ = 2 it follows
from Proposition 4.3 that Li(p)
n (−1) is in Qp for n ≥0. Then Proposition 4.2 (with
f = 1) shows that Lin(−1) is in Qp, so the same holds for Hn(0) by what we proved
in the previous paragraph. Therefore, since H′
2(t) is in Qp[[t]] by (5.9), H2(t) is in
Qp[[t]]. For n > 2 we conclude by induction on n using (5.10) since Gn−1(t)/t is
in Qp[[t]] for such n. If p = 2, then we prove by induction on n that H′
n(t) is in
Q2[[t]] and Hn(0) is in Q2. For n = 2 it is clear from (5.9) that we can ﬁnd 
H2(t)
in Q2[[t]] with 
H′
2(t) = H′
2(t) and 
H2(0) = 0, so H2(t) = H2(0) + 
H2(t). Then
H2(0) is in Q2 by (5.11) since H2(−2) −H2(0) = 
H2(−2) is in Q2. Hence H2(t) is
in Q2[[t]]. For n > 2 the proof proceeds similarly, writing Hn(t) = Hn(0) + 
Hn(t)
with, inductively, 
Hn(t) in Q2[[t]] by (5.10).
□
Remark 5.12. (1) It follows from the deﬁnition of Em(z) and Proposition 2.10(2)
that En(z) + (−1)nEn(1/z) = logn(z)/(n! (n −1)).
Therefore En(1), En(−1),
Lin(1), Lin(−1) and Hn(0) are all 0 when n ≥2 is even.
(2) For p̸ = 2 Proposition 4.2 with ζ = −1 simpliﬁes to Lin(−1) =
pn
pn−1Li(p)
n (−1)
so that Hn(0) =
2n−1pn
(1−2n−1)(pn−1)Li(p)
n (−1).
Li(p)-SERVICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS
1115
