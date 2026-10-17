---
doc_id: arxiv-2412.04241v2
doc_title: "The Habiro ring of a number field"
section_id: sec-012-22-admissible-series
section_title: "Admissible series"
section_number: 2.2
pages: 20-22
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
toc_source: outline
doc_brief: "The Habiro ring of a number field — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
arise as generating series of Poincar´e polynomials of Cohomological Hall Algebras. The latter
are algebra structures that one can define on the homology of a moduli stack parametrising
objects in abelian categories satisfying appropriate conditions.
By their very definition, the product of two admissible series is admissible, and since the
choice of the integers cn,i in (28) is arbitrary (as long as they have finite support for each n),
it follows that admissible series belong to an uncountable group of formal power series. In
contrast with q-series with integer coefficients, which are typically defined only for |q| < 1,
F(t, q)
is admissible if and only if
F(t, q−1)
is admissible .
(61)
Another property of admissible series F(t, q) is that the ratio (which is often considered
in the literature) and the symmetrisation (which is less common, but useful for us)
G(t, q) = F(qt, q)/F(t, q),
F sym(t, q) = F(t, q)F(t, q−1)
(62)
are integral i.e., both lie in Z[q±1][[t]]. This follows easily from equation (28) combined with
the two identities
(1 −t)(qt; q)∞= (t; q)∞,
(t; q−1)∞=
1
(qt; q)∞
(63)
in Q(q)[[t]], which follow from the known t-series expansions of both sides or from the fact that
they satisfy the same first order linear q-difference equation. More precisely, equation (28)
implies that
G(t, q) =
Y
0̸=n∈(Z≥0)N
Y
i∈Z
(qitn; q)
−cn,i
n1+···+nN,
F sym(t, q) =
Y
0̸=n∈(Z≥0)N
Y
i∈Z
(q1−itn; q)
−cn,i
2i−1 . (64)
Admissible series initially appear to treat q near 0 or infinity. As already mentioned, we
can also consider q near 1, or better yet, near a primitive m-th root of unity ζm. Doing
so, we are led to associate to an admissible series F(t, q) a collection of completed series
f(t, q) = (fm(t, x))m≥1 defined for q = ζm + x via the very short definition (30).
The
next lemma unravels this definition. Its proof follows directly from the definition of the
admissibility (27), and among other things explains the necessity for the rescaling t1/m of
the t (multi-)variable. To state it, recall Ln(q) from equation (27) and set
V (t) =
X
0̸=n∈(Z≥0)N
Ln(1)Li2(tn) ∈Q[[t]] ,
(65)
δ(t) = exp

X
0̸=n∈(Z≥0)N
Ln(1)Li1(tn) −2
X
0̸=n∈(Z≥0)N
L′
n(1)Li1(tn)

∈Q[[t]] ,
(66)
THE HABIRO RING OF A NUMBER FIELD
21
with constant terms V (0) = 0 and δ(0) = 1. Furthermore, for every integer m ≥1, we let
Um(t) = eum(t), where
um(t) = −m −1
2m
X
0̸=n∈(Z≥0)N
Ln(1)Li1(tn) + 1 −m
m
X
0̸=n∈(Z≥0)N
L′
n(1)Li1(tn)
−
m−1
X
j=1
X
0̸=n∈(Z≥0)N
Ln(ζj
m)
1 −ζj
m
X
k∈Z/mZ
ζ−kj
m
m Li1(ζk
mtn/m)
∈t Q[[t]] .
(67)
Lemma 2.3. For every m, we have
fm(t, x) ∈e
V (t)
m2 log(1+x/ζm)
1
p
δ(t)
Um(t)(1 + x t1/m Q[ζm][[t1/m]][[x]]),
fm(0, x) = 1 .
(68)
When F(t, q) = FA(t, q) is given by (31), we will denote the corresponding series fA(t, q),
VA(t), δA(t) and UA,m(t), respectively.
Proof. To simplify the notation, we assume N = 1. Fix m, and observe that the right hand
side of (27) has a simple pole at q = ζm coming from the terms with ℓdivisible by m, for
which
Res
q=ζm
Ln(qℓ)
ℓ(1 −qℓ) = −Ln(1) ζm
ℓ2
.
(69)
Setting ℓ= mr with r ≥1, we see that the residue of the right hand side of (27) is given by
X
n,r≥1
Ln(1) ζm
m2r2
tnmr =
1
m2
X
n≥1
Ln(1) Li2(tnm) =
1
m2V (tm) .
(70)
This explains the need for the rescaling t 7→t1/m in order to match with equation (68). The
remaining terms of (27) can be expanded into power series in t1/m with coefficients in Q[ζm].
When we compute the constant term of the x-series expansion of fm(t, x) there are two
contributions to um(t) from log F(t, q) in (27), depending whether or not m divides ℓ. When
m divides ℓ, with q = ζm + x, we have
−Ln(qℓ)
ℓ(1 −qℓ) = ζm
Ln(1)
ℓ2
1
x +
Ln(1)
2ℓ2
−Ln(1)
2ℓ
+ L′
n(1)
ℓ

+ O(x)
(71)
Setting m = rℓand summing over n ≥1, r ≥1 and rescaling t to t1/m gives the volume term
V (t)/(2m2) and the first two terms in equation (67).
When m does not divide ℓ, then ℓ= rm + j for some r ≥0 and 1 ≤j ≤m −1. Then,
again with q = ζm + x, we have
−Ln(qℓ)
ℓ(1 −qℓ) = −
Ln(ζj
m)
(mr + j)(1 −ζj
m)
+ O(x)
(72)
and after rescaling t, we find that this contribution is
−
m−1
X
j=1
X
n≥1, r≥0
Ln(ζj
m)
(mr + j)(1 −ζj
m)
tn(mr+j)/m = −
m−1
X
j=1
X
n≥1
Ln(ζj
m)
1 −ζj
m
X
k∈Z/mZ
ζ−kj
m
m Li1(ζk
mtn/m) ,
(73)
22
STAVROS GAROUFALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
which is the last term of equation (67). The lemma follows.
□
Equations (65) and (67) imply the following corollary, which in a sense is a gluing property
of the collection of power series f(t, q).
Corollary 2.4. Let F (1) and F (2) be admissible series with the same number of variables t,
and L(i)
n , V (i)(t), δ(i)(t), and U (i)
m (t) (i = 1, 2) be as defined before Lemma 2.3. Then
(a) V (1) = V (2) if and only if L(1)
n (1) = L(2)
n (1) for all n ≥1.
(b) F (1) = F (2) if and only if V (1) = V (2), δ(1) = δ(2) and U (1)
m = U (2)
m for all m ≥1.
(c) F (1) = F (2) if and only f (1)
m = f (2)
m for some (and hence for every) m ≥1.
Proof. Only the if direction of (b) is not obvious. To show it, we note that equation (67) and
the fact that Lis(t) = t+O(t2) imply that V (t) and δ(t) determine Ln(1) and L′
n(1) for all n,
and hence with Um(t) determine sm(t) := Pm−1
j=1
P
n≥1
Ln(ζj
m)
1−ζj
m
P
k∈Z/mZ
ζ−kj
m
m Li1(ζk
mtn/m). Now
use P
k∈Z/mZ
ζ−kj
m
m Li1(ζk
mtn/m) = tjn/m/j + · · · to deduce that the coefficient of t1/m in sm(t)
is L1(ζm)/(1 −ζm) for all m. Thus sm(t) determines L1(q) ∈Z[q±1]. Subtracting this first
contribution from sm(t), we find that the coefficient of t2/m is now L2(ζm)/(2(1 −ζm)) and
hence is again determined by sm(t). Continuing by induction on n, we deduce that sm(t)
determines Ln(q) for all n ≥1.
□
We next discuss a Dwork-type quotient of admissible series for a prime p. The product
formula (28) and equation (27) for admissible series lead immediately to the equality
log
F(tp, qp)
F(t, q)p

= p
X
0̸=n∈(Z≥0)N
X
ℓ>0
(p,ℓ)=1
Ln(qℓ)
ℓ(1 −qℓ)tℓn .
(74)
Expanding near q = ζm + x as in (30) with (m, p) = 1, we see that the left-hand side, even
after division by p, is p-integral. (This strong integrality property will be important.) This
proves:
Lemma 2.5. If F(t, q) is admissible, then for all primes p and positive integers m not
divisible by p we have
log(F(tp/m, qp)) −p log(F(t1/m, q)) ∈p
xZ(p)[t1/m, ζm][[t, x]] ,
q = ζm + x .
(75)
