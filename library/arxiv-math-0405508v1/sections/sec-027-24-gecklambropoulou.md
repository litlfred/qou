---
doc_id: arxiv-math-0405508v1
doc_title: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B"
section_id: sec-027-24-gecklambropoulou
section_title: "Geck–Lambropoulou"
section_number: 24
pages: 24-26
source_pdf: 0405508v1.pdf
source_sha256: ef2e41cf67f3a411
doc_brief: "Markov traces and knot invariants related to Iwahori-Hecke algebras of type B — 30 sections: Introductory remarks on knots, bra; Geck–Lambropoulou; Geck–Lambropoulou"
---
with d∗
i ∈ D ′
n, 0 and, secondly, that τ(d∗
1 · · ·d∗
n) = zayb where a is the number
of si’s and b is the number of conjugates of t in this element. This is the exact
counterpart of the purely algebraic argument given before in (4.4) .
Also, notice that the set of mixed links of the form ˆt′t′
1 · · · t′
k−1 form the
basis of the submodule of the 3rd skein module of the solid torus (as c alculated
by Turaev in [10] and by Hoste and Kidwell in [4]), that is related to the
Iwahori-Hecke algebras of type B.
Finally, the deﬁning equation in Deﬁnition 5.3 already shows that Xˆα is
a polynomial in Q±, y 1, y 2, . . . . If we also perform the change of variables
x := √
qλ and r := √q − 1√q then the ﬁrst skein rule can be rewritten as
1
x XL+ − xXL− = rXL0.
As in [5], Proposition 6.2, this allows us to deduce that Xˆα also is a Laurent
polynomial in the variables x and r.
Examples 5.6 We shall now evaluate explicitly Xˆα for some special choices
of α as a Laurent polynomial in x, r, Q, y 1, y 2, . . . .
(a) If α is a product of generators si or their inverses (and does not involve t)
then Xˆα equals the known 2-variable invariant for oriented knots inside S3 (see
the remarks following Deﬁnition 5.3).
(b) Consider α = s1s−1
2 s1ts−1
1 s2 and α ′ = ts2 in B1, 3 (see Remarks 2.6(b)).
Using (4.4) we directly ﬁnd that τ ◦ π(α ) = τ ◦ π(α ′) = zy1. The exponent
sum e of the factors si equals 1 in both cases. Therefore, we also have
Xˆα = Xˆα ′ =
(
1 − λq
√
λ(1 − q)
) 2 √
λzy 1
= λq − 1√
λ(1 − q)
√
λy 1 (inserting z)
= 1 − x2
xr y1 (inserting x and r).
(c) For a general braid α ∈ B1,n , we ﬁrst have to consider its image in Hn and
express it as a linear combination in the standard basis of Hn:
h := π(α ) =
∑
w∈W
awgw with aw ∈ A.
Then we could compute the set I(h) deﬁned in Proposition 3.4 and ﬁnally use
the recipe given in (4.4) to evaluate the trace τ(h). Now the computation of
Markov traces and knot invariants 25
the set I(h) involves performing a base change from the standard basis of Hn
to the new basis consisting of the elements r′
1 · · · r′
n, with r′
i ∈ R ′
i (see (3.2)
and the proof of Proposition 3.4). In practice, however, this will be quite
cumbersome. A more economic way is by using the class polynomials of [3 ].
Recall from [ loc. cit. ] that for each w ∈ Wn there exist elements fw,C ∈
Z Z[q, Q ] such that ϕ (gw) =
∑
C fw,C ϕ (gwC ) (sum over all conjugacy classes C
of Wn), for all trace functions ϕ on Hn. In [ loc. cit. ], Section 1, there is also
given a recursive formula for computing fw,C . Assume then that we know (for
our given braid α ) the coeﬃcients aw ∈ A and the class polynomials fw,C for
all w such that aw ⁄= 0. Then we have
τ ◦ π(α ) =
∑
C

 ∑
w∈Wn
awfw,C

 τ(gwC ).
Thus, we are reduced to calculating, once and for all, the values of τ on basis
elements corresponding to representatives wC of minimal length in the conju-
gacy classes C of Wn. These classes are parametrized by pairs of partitions
(π1, π 2) such that the total sum of the parts of π1 and π2 equals n and where
each part of π1 (respectively π2) corresponds to a negative (respectively posi-
tive) block. The formulae become more complicated as the number of negative
blocks involved in wC gets larger. Below we give the trace values for n ≤ 4
and all wC which contain at most three negative blocks. (The only class C for
which we don’t give the value is the one with representative tt1t2t3; for each
n ≥ 2, we consider only those wC which are not already contained in B1,n −1.)
B1, 1 : τ(1) = 1 , τ (t) = y1.
B1, 2 : τ(g1) = z, τ (tg1) = zy1,
τ(tt1) = (( q − 1)(Q − 1)y1 + (q − 1)Q)z + qy2.
B1, 3 : τ(tg2) = zy1, τ (g1g2) = z2, τ (tg1g2) = z2y1,
τ(tt1g2) = zτ(tt1) (see B1, 2),
τ(tt1t2) = (( q − 1)(Q2 − Q + 1)y1 + Q(q − 1)(Q − 1))(q3 − 1)z2
+(Qy1 + (Q − 1)y2)(q3 − 1)qz + q3y3.
B1, 4 : τ(g1g3) = z2, τ (g1g2g3) = z3,
τ(tg1g3) = τ(tg2g3) = z2y1, τ (tg1g2g3) = z3y1,
τ(tt1g3) = zτ(tt1), τ (tt1g2g3) = z2τ(tt1) (see B1, 2),
τ(tg1t2g3) = (( Q − 1)y1 + Q)(q − 1)(q2 + 1)z3 + q(q2 − q + 1)y2z2,
τ(tt1t2g3) = zτ(tt1t2) (see B1, 3),
τ(tt1t2t3) (four negative blocks) .
