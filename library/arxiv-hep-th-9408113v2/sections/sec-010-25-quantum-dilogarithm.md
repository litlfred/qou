---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-010-25-quantum-dilogarithm
section_title: "Quantum dilogarithm."
section_number: 2.5
pages: 79-89
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
toc_source: inferred
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
2.5. Quantum dilogarithm.
Let us remind that the Euler dilogarithm Li2(x) is deﬁned for 0 ≤x ≤1 by
Li2(x) =
X
n≥1
xn
n2 .
Deﬁnition 9 (q-analog of Euler’s dilogarithm or quantum dilogarithm).
Quantum
dilogarithm Li2(x; q) is the following formal series
Li2(x; q) =
X
n≥1
xn
n(1 −qn).
(2.52)
Before stating the basic properties of the quantum dilogarithm, let us remind the
deﬁnition of the two q-exponential functions (see e.g. [GR], Appendix II)
eq(x) =
X
n≥0
xn
(q)n
=
1
(x)∞
,
(2.53)
Eq(x) =
X
n≥0
q
n(n−1)
2
xn
(q)n
= (−x)∞.
Here we use the standard q-analysis notation:
(x)∞:= (x; q)∞=
Y
n≥0
(1 −xqn),
(x)n :=
(x; q)∞
(xqn; q)∞
.
It is clear from the deﬁnition (2.53) that
(1 + x)Eq(qx) = Eq(x),
eq(qx) = (1 −x)eq(x),
eq−1(x) = Eq(−qx).
(2.54)
Lemma 8. We have
i) Li2(x; q) = log(eq(x)),
ii) Li2(x; q) + Li2(x; q−1) = −log(1 −x).
Proof. it is clear from (2.54) that
Li2(qx; q) = Li2(x; q) + log(1 −x).
Hence, if Li2(x; q) =
X
n≥1
anxn, then qnan = an −1
n.
80
Anatol N. Kirillov
Proposition H (Euler-Maclaurin’s summation formula). If f ∈C2n([M, N]), M and
N integers, then
N
X
m=M
f(m) =
Z N
M
f(t)dt + 1
2(f(N) + f(M)) +
n
X
k=1
B2k
(2k)!
n
f (2k−1)(N) −f (2k−1)(M)
o
−
Z N
M
B2n(t)
(2n)! f (2n)(t)dt.
(2.55)
Here Bk are the Bernoulli numbers and Bk(t) are the Bernoulli polynomials which are
deﬁned by
zetz
ez −1 =
X
k≥0
Bk(t)
k!
zk,
Bk := Bk(0).
Bn(t) is the so-called modiﬁed Bernoulli polynomial: Bn(t) = Bn({t}), where {t} := t−[t]
is the fractional part of a real number t.
As a simple corollary of the Euler-Maclauren summation formula, one can obtain
Corollary 10.
If q = e−ǫ and ǫ →0, then the function eq(x) has the following
asymptotic expansion
(0 < x < 1)
eq(x) = (1 −x)−1
2 exp(Li2(x)
ǫ
+
xǫ
12(1 −x))(1 + O(ǫ3)).
Indeed, it follows from (2.55) that (cf. [Mo], [UN]) if 0 < x < 1 and q = e−ǫ, then as
ǫ →0,
log((x; q)∞) ∼−Li2(x)
ǫ
+ 1
2 log(1 −x) −
∞
X
k=1
B2k
(2k)!
P2k−1(x)ǫ2k−1
(1 −x)2k−1 ,
where Pn(x) is a polynomial of degree n satisfying
Pn(x) = (x −x2)P ′
n−1(x) + nxPn−1(x),
P0 = 1,
n = 1, 2, 3, . . ..
Moreover, the error in terminating the series is less in absolute value than that of the ﬁrst
term neglected and has the same sign.
The most important and fundamental property of Euler’s dilogarithm is the ﬁve-term
relation (in Rogers’ form, [Ro]) Li2(x) + Li2(y) −Li2(xy) =
= Li2
x(1 −y)
1 −xy

+ Li2
y(1 −x)
1 −xy

+ log
 1 −x
1 −xy

log
 1 −y
1 −xy

.
(2.56)
Before discussing the (quantum) analog of the ﬁve-term relation for the quantum dilog-
arithm Li2(x; q) (see also [FK]), let us consider in more detail the properties of q-exponent
eq(x).
Dilogarithm identities
81
Lemma 9. Assume that variables a and b satisfy the Weyl relation ab = qab. Then
we have
i)
eq(b)eq(a) = eq(a + b),
(2.57)
ii)
eq(a)eq(b) = eq(b −ba)eq(a)
(2.58)
= eq(a + b −ba)
(2.59)
= eq(b)eq(−ba)eq(a)
(2.60)
= eq(b)eq(a −ba)
(2.61)
Proof. The ﬁrst relation (2.57) is well-known and follows from the following result due
to M.-P. Sch¨utzenberger (the middle of 50’s)
if ab = qab,
then (a + b)n =
n
X
k=0
akbn−k

n
k

q
.
As for the identities of part ii), the crucial relation is (2.58). Both (2.59) and (2.60) follow
from (2.58) and (2.57) (hint: a(b −ba) = q(b −ba)a, bab = qb2a). Now let us prove the
identity (2.58). We give two proofs.
First proof. Let us check that the both sides of (2.58) as the functions on b satisfy the
same functional equation. Indeed, (e(·) := eq(·))
e(a)e(qb)e−1(b)e−1(a) = e(a)(1 −b)e−1(a) = 1 −e(a)be−1(a)
= 1 −be(qa)e−1(a) = 1 −b(1 −a) = 1 −b + ba;
e(q(b −ba))e(a)e−1(a)e−1(b −ba) = 1 −b + ba.
Second proof (A. Volkov). We have
e(a)e(b)e−1(a) = e(e(a)be(a−1)) = e(be(qa)e−1(a)) = e(b(1 −a)).
In a similar manner, the identity (2.61) may be derived from (2.54).
It is very surprising that (2.57) and (2.59) have the polynomial analogs.
Lemma 10. Under the assumptions of Lemma 9, we have
i)
(a; q)n · (b; q)n = (a + b −qnba; q)n,
(2.62)
ii)
(b; q)n · (a; q)n = (a + b −ba; q)n.
(2.63)
Proof. Let us prove (2.62) by induction. The case n = 1 is clear. Further,
LHS(2.62) = (1 −qn−1a)(a)n−1(1 −b)(qb)n−1
= (1 −a)(qa)n−1(qb)n−1 −(1 −qn−1a)b(qa)n−1(qb)n−1
= (1 −a −b + qn−1ab)(qa)n−1(qb)n−1
induction
=
(1 −a −b + qnba)(qa + qb −qn+1ba)n−1 = (a + b −qnba)n.
82
Anatol N. Kirillov
Analogously,
LHS(2.63) = (1 −b)(qb)n−1(1 −qn−1a)(a)n−1
= (1 −qn−1b)(b)n−1(a)n−1 −qn−1(1 −b)(qb)n−1a(a)n−1
= (1 −qn−1b)(b)n−1(a)n−1 −qn−1(1 −b)a(b)n−1(a)n−1
= (1 −qn−1b −qn−1a + qn−1ba)(b)n−1(a)n−1
induction
=
(a + b −ba)n.
Now we are ready to give the quantum analog of the ﬁve-term relation (1.4) for the
quantum dilogarithm Li2(x; q).
Theorem I (L.D. Faddeev and R.M. Kashaev, [FK]). The ﬁve term or ”pentagon”
relation (ab = qba)
eq(a)eq(b) = eq(b)eq(−ba)eq(a)
(2.60)
is a quantum analog of the Rogers ﬁve-term relation (1.4) or (2.56), i.e. an appropriate
limit q →1 in (2.60) reduces the last to the relation (2.56).
Let us rewrite the relations (2.57), (2.59) and (2.60) using the quantum dilogarithm.
For this purpose we need the Baker-Campbell-Hausdorﬀseries. Namely, for any Lie algebra
with Lie bracket [·, ·], let us denote by H(x, y) its Campbell-Hausdorﬀseries, i.e.
ex · ey = eH(x,y),
H(x, y) = x + y + 1
2[x, y] + 1
12 {[x, [x, y]] + [y, [y, x]]} + 1
24[xyyx]
+
1
144 {9[xxyyx] + 9[yyxxy] + 4[xyyyx] −2[xxxxy] −2[yyyyx]} + . . . ,
where [a1a2 . . . an] is the multiple commutator [a1, [a2, . . ., [an−1, an] · · ·].
Proposition 2 (Functional equations for quantum dilogarithm). We have (ab = qba)
i) H(Li2(a; q), Li2(b; q)) = Li2(a + b −ab; q),
(2.64)
ii) H(Li2(b; q), Li2(a; q)) = Li2(a + b; q).
Corollary 11 (Five term relation for quantum dilogarithm).
H(Li2(a; q), Li2(b; q)) = H(Li2(b; q), H(Li2(−ba; q), Li2(a; q)))
(2.65)
= H(H(Li2(b; q), Li2(−ba; q)), Li2(a; q)).
Exercises to Section 2.5.
A (Weyl algebra and q-exponential a function).
1. Let us consider a function ϕ(a)
ϕ(a) := eq2(−qa) =
X
n≥0
(−qa)2
(q2; q2)n
=
1
j≥0
(1 + q2j+1a)
.
Dilogarithm identities
83
Show that
i) ϕ(qa) = (1 + a)ϕ(q−1a);
ii) If a and b satisfy the Weyl relation ab = q2ba, then
ϕ(b)ϕ(a) = ϕ(a + b),
(1)
ϕ(a)ϕ(b) = ϕ(b)ϕ(a + qb),
(2a)
= ϕ(a + b + qba),
(2b)
= ϕ(b)ϕ(qba)ϕ(a),
(2c)
Hint: use the relations (2.57)-(2.61).
2. Let us consider the theta-function
θ(a) := [ϕ(a)ϕ(a−1)]−1. Show that
i) θ(qa) = a−1θ(q−1a);
ii) θ(a) =
X
n∈Z
qn2an;
iii) (cf. [FV]) If ab = q2ba, then
θ(a)θ(b)θ(a) = θ(b)θ(a)θ(b).
(3)
Hint: use the following relation
θ(a)θ(b)a = bθ(a)θ(b).
3. Let us consider a function
f(a) := f(z, a) = ϕ(za)/ϕ(a). Show that
i)
f(qa)
f(q−1a) = 1 + za
1 + a ,
f(qz, a)
f(q−1z, a) = 1 + az;
ii) f(z, a) =
X
n≥0
anqn2(z; q−2)n
(q2; q2)n
;
iii) (Cf. [FV]) If ab = q2ba, then f(b)f(a) = f(a + b + qba).
Hint: use the relations
ϕ(za)ϕ(b) = ϕ(b)ϕ(za + zqba),
ϕ(zb)ϕ(za + zqba) = ϕ(za + zb + zqba).
4. Let us consider a function
π(a) := π(z, a) = ϕ(za)ϕ(za−1). Show that
i)
π(z, a) =
X
n≥0
(−qz)nHn(a)
(q2; q2)n
,
where Hn(a) := Hn(a; q2) is the so-called continuous
q-Hermite polynomial. Prove the recurrence relation for the continuous q-Hermite polyno-
mials:
Hn(a) = AHn−1(a) −(1 −q2n−2)Hn−2(a),
(4)
84
Anatol N. Kirillov
where A = a + a−1, H0(a) = 1, H1(a) = a + a−1.
It follows from (4), that
Hn(a; q2) = det

A
1
. . .
0
0
1 −q2
A
. . .
0
0
. . .
. . .
. . .
0
0
. . .
A
1
0
0
. . .
1 −q2n−2
A

n×n
.
Hint: use the functional equation:
π(qa)
π(q−1a) =
1 + za
1 + za−1 .
(5)
ii) (Modifyed Yang-Baxter equation). If ab = q2ba, then
π(z′, b)π(zz′, qba)π(z, a) = π(z, a)π(zz′, qab−1)π(z′, b).
(6)
Proof. Let us remark at ﬁrst that (ab = q2ba)
π(z, a)b(1 + zq−1a−1) = b(1 + zqa)π(z, a),
(7)
π(z, a)b−1(1 + zq−1a) = b−1(1 + zqa−1)π(z, a).
Indeed, using the functional equation (5), one can ﬁnd
π(z, a)b(1 + aq−1a−1) = bπ(z, q2a)(1 + zq−1a−1) = b(1 + zqa)π(z, a).
To go further, let us use the relations (1) and (2). One can check
Φ := π(z′, b)π(zz′, qba) = ϕ(z′b)ϕ(z′b−1)ϕ(zz′qba)ϕ(zz′qb−1a−1)
(2c)
= ϕ(z′b)ϕ(zz′qba)ϕ(z(z′)2a)ϕ(z′b−1)ϕ(zz′qb−1a−1)
(1)
= ϕ(z′b(1 + qza))ϕ(z(z′)2a)ϕ(z′b−1(1 + qza−1)).
Consequently (use the relation (7) !),
Φ · π(z, a) = π(z, a)ϕ(z′b(1 + zq−1a−1))ϕ(z(z′)2a)ϕ(z′b−1(1 + zq−1a))
= π(z, a)π(zz′, qab−1)π(z′, b),
as it was claimed.
5 (Commutation relations for the continuous q-Hermite polynomials).
Show that (ab = q2ba)
i) q[B1(a), Bn(b)] = (1 −q2n)

B1(qab−1)Bn−1(b) −Bn−1(b)B1(qba)
	
,
Dilogarithm identities
85
q[Bn(a), B1(b)] = (1 −q2n)

Bn−1(a)B1(qab−1) −B1(qba)Bn−1(a)
	
.
ii) More generally, in the Weyl algebra {a, b | ab = q2ba} there exist the following relations
(m, n = 1, 2, 3, . . .)
min(n,m)
X
k=0
(−q−1)k

n
k

q2

m
k

q2 (q2; q2)kBn−k(b)Bk(qba)Bm−k(a)
(8)
=
min(n,m)
X
k=0
(−q−1)k

n
k

q2

m
k

q2 (q2; q2)kBm−k(a)Bk(qab−1)Bn−k(b).
Hint: the relations (8) are equivalent to the modifyed Yang-Baxter equation (6).
6. Let us consider a function (cf. [FV])
r(z, a) = θ(a)π(z, a). Show that
i) (functional equations)
r(z, qa)
r(z, q−1a) = 1 + za
a + z ,
r(qz, a)
r(q−1z, a) = (1 + za)(1 + za−1).
ii) r(z, a) = 1 +
X
n≥1
qn(n−1) (z; q−2)n
(zq2; q2)n
(an + a−n).
iii) (Yang-Baxter equation, L.D. Faddeev and A.Yu. Volkov [FV], A.N. Kirillov).
If ab = q2ba and zz′ = z′z, then
r(z, a)r(zz′, b)r(z′, a) = r(z′, b)r(zz′, a)r(z, b).
(9)
Hint: using the commutation relations
θ(b)∓1g(a)θ(b)±1 = g(q±1ab∓1),
θ(a)∓1g(b)θ(a)±1 = g(q∓1a±1b),
to reduce a proof of (9) to that of (6).
iv) Using the functional equation
(z + a)r(z, qa) = (1 + za)r(z, q−1a),
check that
LHS(9)(az−1 + qba + z′b) = (z′a + qba + bz−1)LHS(9),
RHS(9)(az−1 + qba + z′b) = (z′a + qba + bz−1)RHS(9).
Deduce from these relations that
LHS(9) = RHS(9).
B. (Miscellany).
7. Let Wq be the algebra over the ﬁeld of rational functions C(q) generated by a and
b subject to the relation ab = q2ba.
Prove that the maps
∆(e∆) : Wq →Wq ⊗Wq
∆(a) = 1 ⊗a + a ⊗b,
(e∆(a) = a ⊗a),
∆(b) = b ⊗b,
(e∆(b) = 1 ⊗b + b ⊗a)
deﬁne the comultiplications in Wq.
86
Anatol N. Kirillov
8. Consider an element f(a, b) =
X
n,m
cn,m(q)bnam from the Weyl algebra Wq
1
2 and
assume that there exists the limit
lim
q→1(1 −q)f(a, b) = ef(ea,eb),
where ea and eb commutes.
Prove that
i)
lim
q→1(1 −q) [L(a), f(a, b)] = log(1 −ea)

eb ∂
∂eb

ef(ea,eb),
lim
q→1(1 −q) [f(a, b), L(b)] = log(1 −eb)

ea ∂
∂ea

ef(ea,eb).
ii)
lim
q→1(1 −q)
X
n≥0
1
n!adn
L(a) (f(a, b)) = ef(ea,eb −eaeb),
where
ad0
y(x) = x and
adn+1
y
(x) = [y, adn
y(x)], n ≥0.
Hint: use the Taylor formula
(xy = yx)
exp(

yx ∂
∂x

f(x) = f (x exp(y)) .
9 (Quantum polylogarithm). Let us deﬁne the quantum polylogarithm as the following
formal series (k ≥1)
Lik(x; q) :=
X
n≥1
xn
n(1 −qn)k−1 .
(10)
• Prove that (k ≥2)
exp (Lik(x; q)) =
Y
m=(m1,...,mk−2)∈Zk−2
+
eq(q|m|x),
(11)
where |m| := m1 + . . . + mk−2.
Hint: it is clear that Lik(x; q) −Lik(qx; q) = Lik−1(x; q). Consequently,
Lik(x; q) =
X
m≥0
Lik−1(qmx; q),
exp (Lik(x; q)) =
Y
m≥0
exp (Lik−1(qmx; q)) .
• (Functional equation for quantum trilogarithm). Prove that if x and y satisfy the
Weyl relation xy = qyx, then
exp (Li3(x; q)) exp (Li3(y; q)) = exp (Li3(y; q)) exp (Li3((y)∞x; q))
(12)
= exp (Li3(y(x)∞; q)) exp (Li3(x; q)) .
Dilogarithm identities
87
It is a very intertesting task to study the asymptotic behavior of the quantum polyloga-
rithm functional equations (see e.g. (2.64), (2.65) and (9), (11), (12)) when q = ζe−ǫ →1,
ǫ →0, where ζ = exp
2πi
l

. We intended to consider this interesting subject in [Kir10].
Appendix.
Proof of Proposition E, n = 2, A = 1. We have the following series of relations coming
from the functional equation (1.4):
• L(β1/α2) + L(α2x1) −L(β1x1) −L
β1(1 −α2x1)
α2(1 −β1x1)

−L
(α2 −β1)x1
1 −β1x1

= 0,
• L(β1/α1) + L(α1x2) −L(β1x2) −L
β1(1 −α1x2)
α1(1 −β1x2)

−L
(α1 −β1)x2
1 −β1x2

= 0,
• L(β2/α1) + L(α1x1) −L(β2x1) −L
β2(1 −α1x1)
α1(1 −β2x1)

−L
(α1 −β2)x1
1 −β2x1

= 0,
• L(β2/α2) + L(α2x2) −L(β2x2) −L
β2(1 −α2x2)
α2(1 −β2x2)

−L
(α2 −β2)x2
1 −β2x2

= 0,
• L
(α1 −β1)x2
1 −β1x2

+ L
(α2 −β1)x1
1 −β1x1

−L(t) −L
x1(α2 −β1)(1 −β2x2)
(1 −β1x1)(1 −α2x2)

−L
x2(α1 −β1)(1 −β2x1)
(1 −β1x2)(1 −α1x1)

= 0,
• L
(α1 −β2)x1
1 −β2x1

+ L
(α2 −β2)x2
1 −β2x2

−L(t) −L
x1(α1 −β2)(1 −β1x2)
(1 −β2x1)(1 −α1x2)

−L
x2(α2 −β2)(1 −β1x1)
(1 −β2x2)(1 −α2x1)

= 0,
• L
β1(1 −α2x1)
α2(1 −β1x1)

+ L
β2(1 −α1x1)
α1(1 −β2x1)

−L
β1β2(1 −t)
α1α2

−L
β1(1 −α2x1)(1 −β2x2)
(1 −β1x1)(α2 −β2)

−L
β2(1 −α1x1)(1 −β1x2)
(1 −β2x1)(α1 −β1)

= 0,
• L
β1(1 −α1x2)
α1(1 −β1x2)

+ L
β2(1 −α2x2)
α2(1 −β2x2)

−L
β1β2(1 −t)
α1α2

−L
β1(1 −α1x2)(1 −β2x1)
(1 −β1x2)(α1 −β2)

−L
β2(1 −α2x2)(1 −β1x1)
(1 −β2x2)(α2 −β1)

= 0,
• L
(α2 −β2)x2(1 −β1x1)
(1 −α2x1)(1 −β2x2)

+ L
β1(1 −α2x1)(1 −β2x2)
(α2 −β2)(1 −β1x1)

−L (x2β1)
−L
 −β1/α1
1 −β1/α1

−L
 −α1x2
1 −α1x2

= 0,
• L
(α1 −β1)x2(1 −β2x1)
(1 −α1x1)(1 −β1x2)

+ L
β2(1 −α1x1)(1 −β1x2)
(α1 −β1)(1 −β2x1)

−L (x2β2)
88
Anatol N. Kirillov
−L
 −β2/α2
1 −β2/α2

−L
 −α2x2
1 −α2x2

= 0,
• L
(α2 −β1)x1(1 −β2x2)
(1 −α2x2)(1 −β1x1)

+ L
β2(1 −α2x2)(1 −β1x1)
(α2 −β1)(1 −β2x2)

−L (x1β2)
−L
 −β2/α1
1 −β2/α1

−L
 −α1x1
1 −α1x1

= 0,
• L
(α1 −β2)x1(1 −β1x2)
(1 −α1x2)(1 −β2x1)

+ L
β1(1 −α1x2)(1 −β2x1)
(α1 −β2)(1 −β1x2)

−L (x1β1)
−L
 −β1/α2
1 −β1/α2

−L
 −α2x1
1 −α2x1

= 0.
Let us denote by S the LHS of the sum of all of these relations. Let D be a diﬀerence
between the LHS and the RHS of the identity from Proposition E. Then one can check
S = −2D −
X
i,j

L(αixj) + L
 −αixj
1 −αixj

−2L(αi/αj)

+ 2L(1) = 0.
But it follows from the integral representation (1.2) that a function
l(t) :=
X
i,j

L(αixj(t)) + L
 −αixj(t)
1 −αixj(t)

does not depend on t. Taking t = 1 one can ﬁnd this constant. The result is
l(t) = 2
X
L(αi/αj) + 2L(1),
consequently, D = 0.
Note that the next Lemma and identities (A1)-(A2) had played the key role in the
proving of Proposition E.
Lemma A1. Let r(x, t) be a polynomial as in Proposition E. Then we have
i)

1 −Aβ1 . . . βn
α1 . . . αn
(1 −t)
 n
Y
l=1
(1 −βxl) =
n
Y
l=1

1 −β
αl

, where β = βk for some k,
1 ≤k ≤n,
ii)

1 −Aβ1 . . .βn
α1 . . . αn
(1 −t)
 n
Y
l=1
(1 −αxl) = −(1 −t)
n
Y
l=1

1 −βl
α

, where α = αk for
some k, 1 ≤k ≤n.
Corollary (of Lemma A1, with n = 2). We have
1 −(α1 −β1)x2(1 −β2x1)
(1 −β1x2)(1 −α1x1) = −
(α1 −β1)(α1 −β2)
(1 −β1x2)(1 −α1x1)(α1α2 −β1β2(1 −t)),
(A1)
1 −β1(1 −β2x2)(1 −α2x1)
(α2 −β2)(1 −β1x1)
=
α1(α2 −β1)
(1 −β1x1)(α1α2 −β1β2(1 −t)).
(A2)
Dilogarithm identities
