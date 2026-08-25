---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-071-2-f-n-f-m
section_title: "(f (N ) +f (M )) +"
section_number: 2
pages: 80-82
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
n∑
k=1
B2k
(2k)!
{
f (2k−1)(N )−f (2k−1)(M )
}
−
∫ N
M
B2n(t)
(2n)! f (2n)(t)dt. (2.55)
HereBk are the Bernoulli numbers and Bk(t) are the Bernoulli polynomials which are
deﬁned by
zetz
ez− 1 =
∑
k≥0
Bk(t)
k! zk, B k :=Bk(0).
Bn(t) is the so-called modiﬁed Bernoulli polynomial: Bn(t) = Bn({t}), where{t} :=t− [t]
is the fractional part of a real number t.
As a simple corollary of the Euler-Maclauren summation form ula, one can obtain
Corollary 10. If q = e−ǫ and ǫ → 0, then the function eq(x) has the following
asymptotic expansion ( 0<x< 1)
eq(x) = (1−x)− 1
2 exp(Li2(x)
ǫ + xǫ
12(1−x) )(1 +O(ǫ3)).
Indeed, it follows from (2.55) that (cf. [Mo], [UN]) if 0 < x <1 and q =e−ǫ, then as
ǫ→ 0,
log((x;q)∞)∼− Li2(x)
ǫ + 1
2 log(1−x)−
∞∑
k=1
B2k
(2k)!
P2k−1(x)ǫ2k−1
(1−x)2k−1 ,
where Pn(x) is a polynomial of degree n satisfying
Pn(x) = (x−x2)P ′
n−1(x) +nxPn−1(x), P 0 = 1, n = 1, 2, 3,....
Moreover, the error in terminating the series is less in abso lute value than that of the ﬁrst
term neglected and has the same sign.
The most important and fundamental property of Euler’s dilo garithm is the ﬁve-term
relation (in Rogers’ form, [Ro]) Li2(x) +Li2(y)−Li2(xy) =
=Li2
(x(1−y)
1−xy
)
+Li2
(y(1−x)
1−xy
)
+ log
( 1−x
1−xy
)
log
( 1−y
1−xy
)
. (2.56)
Before discussing the (quantum) analog of the ﬁve-term rela tion for the quantum dilog-
arithmLi2(x;q) (see also [FK]), let us consider in more detail the properti es of q-exponent
eq(x).
Dilogarithm identities 81
Lemma 9. Assume that variables a and b satisfy the Weyl relation ab = qab. Then
we have
i) eq(b)eq(a) = eq(a +b), (2.57)
ii) eq(a)eq(b) = eq(b−ba)eq(a) (2.58)
=eq(a +b−ba) (2.59)
=eq(b)eq(−ba)eq(a) (2.60)
=eq(b)eq(a−ba) (2.61)
Proof. The ﬁrst relation (2.57) is well-known and follows fr om the following result due
to M.-P. Sch¨ utzenberger (the middle of 50’s)
if ab =qab, then ( a +b)n =
n∑
k=0
akbn−k
[
n
k
]
q
.
As for the identities of part ii), the crucial relation is (2.58). Both (2.59) and (2.60) fol low
from (2.58) and (2.57) (hint: a(b−ba) = q(b−ba)a, bab = qb2a). Now let us prove the
identity (2.58). We give two proofs.
First proof. Let us check that the both sides of (2.58) as the functions on b satisfy the
same functional equation. Indeed, ( e(·) := eq(·))
e(a)e(qb)e−1(b)e−1(a) = e(a)(1−b)e−1(a) = 1−e(a)be−1(a)
= 1−be(qa)e−1(a) = 1−b(1−a) = 1−b +ba;
e(q(b−ba))e(a)e−1(a)e−1(b−ba) = 1−b +ba.
Second proof (A. Volkov). We have
e(a)e(b)e−1(a) = e(e(a)be(a−1)) = e(be(qa)e−1(a)) = e(b(1−a)).
In a similar manner, the identity (2.61) may be derived from ( 2.54).
It is very surprising that (2.57) and (2.59) have the polynom ial analogs.
Lemma 10. Under the assumptions of Lemma 9, we have
i) ( a;q)n· (b;q)n = (a +b−qnba;q)n, (2.62)
ii) ( b;q)n· (a;q)n = (a +b−ba;q)n. (2.63)
Proof. Let us prove (2.62) by induction. The case n = 1 is clear. Further,
LHS(2.62) = (1−qn−1a)(a)n−1(1−b)(qb)n−1
= (1−a)(qa)n−1(qb)n−1− (1−qn−1a)b(qa)n−1(qb)n−1
= (1−a−b +qn−1ab)(qa)n−1(qb)n−1
induction
= (1 −a−b +qnba)(qa +qb−qn+1ba)n−1 = (a +b−qnba)n.
82 Anatol N. Kirillov
Analogously, LHS(2.63) = (1 −b)(qb)n−1(1−qn−1a)(a)n−1
= (1−qn−1b)(b)n−1(a)n−1−qn−1(1−b)(qb)n−1a(a)n−1
= (1−qn−1b)(b)n−1(a)n−1−qn−1(1−b)a(b)n−1(a)n−1
= (1−qn−1b−qn−1a +qn−1ba)(b)n−1(a)n−1
induction
= ( a +b−ba)n.
Now we are ready to give the quantum analog of the ﬁve-term rel ation (1.4) for the
quantum dilogarithm Li2(x;q).
Theorem I (L.D. Faddeev and R.M. Kashaev, [FK]). The ﬁve term or ”pentagon”
relation (ab =qba)
eq(a)eq(b) = eq(b)eq(−ba)eq(a) (2 .60)
is a quantum analog of the Rogers ﬁve-term relation (1.4) or ( 2.56), i.e. an appropriate
limit q→ 1 in (2.60) reduces the last to the relation (2.56).
Let us rewrite the relations (2.57), (2.59) and (2.60) using the quantum dilogarithm.
For this purpose we need the Baker-Campbell-Hausdorﬀ serie s. Namely, for any Lie algebra
with Lie bracket [·,·], let us denote by H(x,y ) its Campbell-Hausdorﬀ series, i.e.
ex·ey =eH(x,y),
H(x,y ) = x +y + 1
2 [x,y ] + 1
12{[x, [x,y ]] + [y, [y,x ]]} + 1
24 [xyyx]
+ 1
144{9[xxyyx] + 9[yyxxy ] + 4[xyyyx ]− 2[xxxxy]− 2[yyyyx ]} +...,
where [a1a2...a n] is the multiple commutator [ a1, [a2,..., [an−1,a n]··· ].
Proposition 2 (Functional equations for quantum dilogarithm). We have (ab =qba)
i) H(Li2(a;q),Li 2(b;q)) = Li2(a +b−ab;q),
(2.64)
ii) H(Li2(b;q),Li 2(a;q)) = Li2(a +b;q).
Corollary 11 (Five term relation for quantum dilogarithm).
H(Li2(a;q),Li 2(b;q)) = H(Li2(b;q),H (Li2(−ba;q),Li 2(a;q))) (2 .65)
=H(H(Li2(b;q),Li 2(−ba;q)),Li 2(a;q)).
Exercises to Section 2.5.
A (Weyl algebra and q-exponential a function).
