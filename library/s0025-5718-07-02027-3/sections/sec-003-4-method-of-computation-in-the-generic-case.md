---
doc_id: s0025-5718-07-02027-3
doc_title: "Li(p)-service? An algorithm for computing p-adic polylogarithms"
section_id: sec-003-4-method-of-computation-in-the-generic-case
section_title: "Method of computation in the generic case"
section_number: 4
pages: 6-11
source_pdf: S0025-5718-07-02027-3.pdf
source_sha256: 080b5ac8542ff19c
doc_brief: "Li(p)-service? An algorithm for computing p-adic polylogarithms — We describe an algorithm for computing Coleman’s p-adic poly- logarithms up to a given precision."
---
In this section we explain how to compute Lin(z) on all residue discs except U0,
U1 and U∞. The residue discs U0 and U∞ were discussed in the previous section,
and U1 will be dealt with in Section 5.
We begin with a well known observation.
Proposition 4.1. Every residue disc other than U0 and U∞ is Uζ for a unique
root of unity ζ of order dividing pf − 1 for some f> 0,k n o w na st h eTeichm¨uller
representative of this residue disc.
Proof. For the residue disc Ub the reduction ¯b satisﬁes ¯bpf −1 =1f o rs o m ef> 0
because Ub ⁄= U0 or U∞.S i n c eCp is complete we can apply Hensel’s lemma to lift
¯b to a unique solution of xpf −1 =1i n Ub,w h i c hi sζ. □
The key observation for the computation of Lin(z) is the following.
Proposition 4.2. Suppose that ζ ⁄=1 is a (pf − 1)-th root of unity. Then
Lin(ζ)=
(
pnf − 1
)−1 (
pnf Li(p)
n (ζ)+ pn(f −1)Li(p)
n (ζp)+ ··· + pnLi(p)
n (ζpf −1
)
)
.
Proof. This formula is derived in [3] as part of the proof of Corollary 2.2 there. For
completeness, we recall the easy proof. For any z in Cp with zpk
⁄=1w eh a v e
k−1∑
r=0
p−rnLi(p)
n (zpr
)=
k−1∑
r=0
p−rn(Lin(zpr
) − p−nLin(zpr+1
)) = Lin(z) − p−nkLin(zpk
)
since the second sum is telescopic. Setting z = ζ and k = f we have ζpf
= ζ; hence
f −1∑
r=0
p−rnLi(p)
n (ζpr
)=( 1 − p−nf )Lin(ζ)= p−nf (pnf − 1)Lin(ζ),
so
Lin(ζ)=( pnf − 1)−1
f −1∑
r=0
pn(f −r)Li(p)
n (ζpr
),
as required. □
Proposition 4.2 implies that if we are able to compute Li(p)
n (z), then we can ﬁnd
Lin(z)a tl e a s tf o rz = ζ. For this calculation we use a power series expansion of
Li(p)
n (z) around ∞ as in the next result (but see also Remark 8.5). Then Proposi-
tion 4.4 below will show how to use the value of Lin(ζ) in order to compute Lin(z)
for z in Uζ.
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1111
Proposition 4.3. We have Li(p)
n (z)= gn(1/(1 − z)) f o rap o w e rs e r i e sgn(v) in
Q[[v]], convergent for v in Cp with |v| <p 1/(p−1). It is determined inductively by
g0(v)= v − 1 − (v − 1)p
vp − (v − 1)p ,
g′
n+1(v)= − gn(v)
v − v2 = −gn(v)
v (1 +v + v2 + ··· )( n ≥ 0) ,
and
gn(0) = 0 ( n ≥ 1) .
Proof. By Theorem 2.7 we can write Li (p)
n (z)= gn(1/(1 − z)) with gn(v)ap o w e r
series that converges when |v| <p 1/(p−1). To determine the relations satisﬁed by
the gn(v) we ﬁrst writeu =1 −z and let fn(u)=L i (p)
n (1 −u)f o rn ≥ 0. Using (2.5)
the equations in (2.6) become
f0(u)= 1 − u
u − (1 − u)p
1 − (1 − u)p and f ′
n+1(u)= −fn(u)
1 − u .
Next we set v =1 /u and let gn(v)= fn(1/v) to ﬁnd
g0(v)= v−1− (v − 1)p
vp − (v − 1)p and g′
n+1(v)= − gn(v)
v − v2 = −gn(v)
v (1+v+v2+··· )
as required. We then have gn(0) = Li(p)
n (∞) = 0 for all n ≥ 0 by Theorem 2.7(3).
Clearly, these relations determine gn(v) inductively by integration. Because the
denominator vp −(v −1)p of g0(v)i sau n i ti nZ[[v]] we see thatg0(v)i si n Z[[v]] and
hence that gn(v)i si n Q[[v]] for n ≥ 1. Finally, we observe that v =1 /(1 − z). □
Proposition 4.4. Let ζ ⁄=1 be a (pf − 1)-th root of unity. For z in Uζ we have
that Lin(z)= Fn,ζ(z − ζ) f o rap o w e rs e r i e sFn,ζ(t) with coeﬃcients in Qp(ζ).I t
converges for |t| < 1 and can be found inductively by the formulae
F0,ζ(t)= ζ + t
(1 − ζ) − t =( 1 − ζ)−1
(
ζ + t
1 − ζ + t2
(1 − ζ)2 + ···
)
(4.5)
and, for n ≥ 0,
F ′
n+1,ζ(t)= Fn,ζ(t)
ζ + t = ζ−1Fn,ζ(t)(1 − ζ−1t + ζ−2t2 −··· )(4.6)
as well as
Fn+1,ζ(0) = Lin+1(ζ) .(4.7)
Proof. The fact that Lin(z) is rigid analytic on Uζ and therefore has a power series
expansion as above was stated in Theorem 2.7(1). The ﬁrst two formulae are
immediate consequences of (2.4). Integration then determines Fn+1,ζ(t)f o r n ≥
0, except for its constant term, which is given by the last equation. Since by
Proposition 4.3 Li (p)
n (ζ)i si n Qp(ζ) the same holds for Li n(ζ) by Proposition 4.2.
The claim about the coeﬃcients is then clear from the inductive formulae. □
For use in some of the estimates in the following sections we also prove a few
results about the absolute values of Li(p)
n (z)a n dL in(z) (cf. [3]). Note that if|z| < 1,
then |Li(p)
n (z)| = |z| by (3.3).
1112 AMNON BESSER AND ROB DE JEU
Proposition 4.8. If z in Cp satisﬁes |z − 1| =1 ,t h e n|Li(p)
n (z)|≤ 1.
Proof. This is a slight generalization of [3, Proposition 2.1], with the same proof.
We use a formula found by Coleman [7, Lemma 7.2],
Li(p)
n (z)=
∫
Z∗
p
x−ndµz(x) ,
where µz is the measure on Zp such that µz(a + pkZp)= za
1−zpk for a =1 ,...,p k.
Since for the speciﬁed values of z this measure takes values with absolute value at
most 1, the same holds for Li(p)
n (z). □
Corollary 4.9 ([3, Corollary 2.2]). If ζ ⁄=1 is a root of unity of order prime top,
then Lin(ζ) is in pnZp[ζ].
Proof. We have that Li(p)
n (ζ)i si n Qp(ζ) by Proposition 4.3, and by Proposition 4.8
we have |Li(p)
n (ζ)|≤ 1s ot h a tL i(p)
n (ζ)i si n Zp[ζ]. The result is now immediate from
Proposition 4.2. □
Corollary 4.10. If ζ is a root of unity of order pkm with m> 1 not divisible by
p,t h e n|Lin(ζ)|≤ p(k−1)n.
Proof. For k = 0 this is part of Corollary 4.9. Fork> 0 it then follows by induction
since Lin(ζ)= p−nLin(ζp)+L i (p)
n (ζ)a n d|Li(p)
n (ζ)|≤ 1 by Proposition 4.8. □
5. Method of computation on U1
To compute Lin(z)f o rz ⁄=1i n U1 we use the following result.
Proposition 5.1 ([7, Proposition 7.1]). For n ≥ 2 the function
(5.2) En(z)=L i n(z) − 1
n − 1 log(z)Lin−1(z)
extends to a rigid analytic function on U1.
It is then clear that En(z) is deﬁned for z ⁄= 0. Moreover, Proposition 2.10(1)
together with the identities log(zm)= m log(z)a n dl o g (ζz)=l o g (z)f o rar o o to f
unity ζ implies that we have a distribution relation
(5.3) En(zm)= mn−1 ∑
ζm=1
En(ζz)
for m ≥ 1a n dz in C∗
p.I np a r t i c u l a r
(5.4) En(z2)=2 n−1(En(z)+ En(−z)) .
Proposition 5.5. On U1 the functions En(z) are independent of the branch of the
logarithm.
Proof. It is easy to check that forn ≥ 3w eh a v e(n −1)E′
n(z)=( n −2)En−1(z)/z.
Since En(z) is rigid analytic onU1 as stated above, the statement follows by induc-
tion provided that En(1) is independent of the branch. Taking m = p − 1 in (5.3)
we see that En(1) is determined by the En(ζ)w h e r eζp−1 =1a n d ζ ⁄=1 . B u t
En(ζ)=L i n(ζ)f o rs u c hζ by (5.2), and from Proposition 4.2 and Theorem 2.7 we
ﬁnd that those values are independent of the branch of the logarithm. □
The Em(z)f o rz in U1 are much easier to deal with than the Li m(z), and we
express Lin(z)i nt e r m so ft h eEm(z) and logarithms.
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1113
Proposition 5.6. We have, for z ⁄=1 in U1 and n ≥ 2,
Lin(z)= 1
(n − 1)! logn−1(z)Li1(z)+
n∑
j=2
(j − 1)!
(n − 1)! logn−j(z)Ej(z) .
Proof. For n ≥ 2w eg e tf r o m( 5 . 2 )t h a t
(n − 1)! En(z)=( n − 1)! Lin(z) − (n − 2)! log(z)Lin−1(z) .
Setting E1(z)=L i 1(z) we have an equality of generating power series in T,
∑
n≥1
(n − 1)! En(z)Tn =( 1 − log(z)T)
(∑
n≥1
(n − 1)! Lin(z)Tn
)
,
so that
∑
n≥1
(n − 1)! Lin(z)Tn =
(∑
n≥1
(n − 1)! En(z)Tn
)
(1 + log(z)T +l o g2(z)T 2 + ··· ),
and the result follows easily. □
Remark 5.7. Because log(z)a n dEn(z) are rigid analytic onU1 the second summand
of Lin(z) in Proposition 5.6 is rigid analytic there. But Li1(z)= − log(1 −z)i sn o t
rigid analytic around 1, hence neither are the ﬁrst summand and Lin(z)i t s e l f .
However, for n ≥ 2w ec a ne x t e n dL in(z)t ot h ew h o l eo fCp by putting Lin(1) =
En(1) (which is independent of the branch of the logarithm by Proposition 5.5).
If F ⊂ Cp is any ﬁeld that is ﬁnitely ramiﬁed over Qp,t h e nl o g (z) is bounded on
F ∗ by the formulae in Remark 2.2 (see Remark 8.1), so by Proposition 5.6 this
extended Lin(z) is continuous onF. It follows from this continuity that part (1) of
Proposition 2.10 holds for all z in Cp (cf. [7, Corollary 7.1a]) and part (2) for all
z ⁄=0i n Cp.
We deal with the two summands in the expression for Lin(z) in Proposition 5.6
separately. Computing the logarithms is standard, and we develop the other func-
tion as a power series around 1 using iterated integration as described in the next
proposition. The constant of integration is expressed in terms of Li n(−1), which
we can compute using Propositions 4.2 and 4.3 if p ⁄=2 . B u ti fp =2 ,t h e n−1i s
outside of the set in Proposition 2.7(3) and we give a diﬀerent formula that we can
c a l c u l a t ea sw eg oa l o n g .
Proposition 5.8. For n ≥ 1 set Gn(t)=l o gn(1 +t)/n!,a n df o rn ≥ 2 let
Hn(t)=
n∑
j=2
(j − 1)!
(n − 1)! logn−j(1 +t)Ej(1 +t) .
Then Gn(t) and Hn(t) for |t| < 1 are given by power series in Qp[[t]],w i t hHn(t)
satisfying
H′
2(t)=1 − t/2+ t2/3 −··· ,(5.9)
H′
n(t)= Hn−1(t)
1+ t + Gn−1(t)
t (n ≥ 3)(5.10)
as well as
Hn(0) = 2n−1Lin(−1)/(1 − 2n−1) .
1114 AMNON BESSER AND ROB DE JEU
If p =2 ,t h e na l s o
Hn(0) = 2n−1
1 − 2n (Hn(−2) − Hn(0)) .(5.11)
Proof. That the Gn(t)f o r |t| < 1 are given by power series in Q[[t]] ⊂ Qp[[t]] is
well-known. By Proposition 5.1 we know that the Em(t +1 )f o rm =2 ,...,n are
given by power series in Cp[[t]] that converge for |t| < 1 so that the same holds for
Hn(t). We shall now ﬁrst prove the inductive formulae and then conclude that the
power series are actually in Qp[[t]].
F r o m( 2 . 3 )w eh a v et h a tE′
2(z)= − log(z)/(1 − z)s ot h a tH′
2(t)= E′
2(t +1 )=
log(1 + t)/t which gives the ﬁrst formula. For m ≥ 3w eh a v e(m − 1)E′
m(z)=
(m − 2)Em−1(z)/z so that H′
n(t)f o rn ≥ 3i sg i v e nb y
n−1∑
j=3
(j − 1)!
(n − 1)!
[
(n − j)logn−j−1(1 +t)
1+ t Ej(1 +t)+ j − 2
j − 1 logn−j(1 +t)Ej−1(1 +t)
1+ t
]
+ logn−1(1 +t)
(n − 1)! t +( n − 2) logn−3(1 +t)
(n − 1)! (1 +t)E2(1 +t)+ n − 2
n − 1En−1(1 +t)
and collecting powers of log(1 +t) this becomes
n−1∑
j=2
(j − 1)!
(n − 1)! [(n − j)+( j − 1)]logn−j−1(1 +t)
1+ t Ej(1 +t)+ logn−1(1 +t)
(n − 1)! t ,
proving the second formula.
As for the constant terms, we see from (5.4) thatEn(1) = 2n−1(En(1)+En(−1)).
Therefore Hn(0) = En(1) = 2n−1En(−1)/(1 − 2n−1), and En(−1) = Lin(−1) since
log(−1) = 0. If p =2 ,t h e n −1i si n U1 so that the deﬁnition of Hn(t)g i v e s
Hn(−2) = En(−1) = Lin(−1) and this leads immediately to the alternative formula
for Hn(0).
Finally, we prove that the coeﬃcients of theHn(t)a r ei nQp.F o rp ⁄= 2 it follows
from Proposition 4.3 that Li(p)
n (−1) is in Qp for n ≥ 0. Then Proposition 4.2 (with
f =1 )s h o w st h a tL in(−1) is in Qp, so the same holds forHn( 0 )b yw h a tw ep r o v e d
in the previous paragraph. Therefore, since H′
2(t)i si n Qp[[t]] by (5.9), H2(t)i si n
Qp[[t]]. For n> 2 we conclude by induction on n using (5.10) since Gn−1(t)/t is
in Qp[[t]] for such n.I f p = 2, then we prove by induction on n that H′
n(t)i si n
Q2[[t]] and Hn(0) is in Q2.F o rn = 2 it is clear from (5.9) that we can ﬁnd ~H2(t)
in Q2[[t]] with ~H′
2(t)= H′
2(t)a n d ~H2(0) = 0, so H2(t)= H2(0) + ~H2(t). Then
H2(0) is in Q2 by (5.11) since H2(−2) − H2(0) = ~H2(−2) is in Q2. Hence H2(t)i s
in Q2[[t]]. For n> 2 the proof proceeds similarly, writing Hn(t)= Hn(0) + ~Hn(t)
with, inductively, ~Hn(t)i n Q2[[t]] by (5.10). □
Remark 5.12. (1) It follows from the deﬁnition of Em(z) and Proposition 2.10(2)
that En(z)+( −1)nEn(1/z)=l o g n(z)/(n!( n − 1)). Therefore En(1), En(−1),
Lin(1), Lin(−1) and Hn(0) are all 0 when n ≥ 2i se v e n .
(2) Forp ⁄= 2 Proposition 4.2 withζ = −1 simpliﬁes to Lin(−1) = pn
pn −1 Li(p)
n (−1)
so that Hn(0) = 2n−1pn
(1−2n−1 )(pn−1) Li(p)
n (−1).
Li(p) -SER VICE? AN ALGORITHM FOR p-ADIC POLYLOGARITHMS 1115
