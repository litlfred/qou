---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-025-curvature-of-the-boundary-of-a-convex-domain-in
section_title: "Curvature of the boundary of a convex domain in a plane"
section_number: null
pages: 59-70
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Curvature of the boundary of a convex domain in a plane
In this section, we consider 2-variable case.
Let F(x, z) be a smooth concave function whose maximal value is positive. Then, the
domain
{
(x, z) ∈R2 

 F(x, z) ≥0
}
(95)
is a convex domain and its boundary is a smooth curve. The aim of this section is to
show the following lemma.
5We use this fact, when we show that the system of equations presenting such tangent points has exactly two solutions
in Sections 3.2, 4.2, 5.2 and Appendix A.
59
Lemma B.1. Let F(x, z) be a smooth concave function whose maximal value is positive
and Hesse matrix is negative deﬁnite. Then, the domain (95) is a convex domain and its
boundary is a smooth curve whose curvature is non-zero everywhere.
Proof. We choose any point on the boundary of the domain (95). It is suﬃcient to show
that the curvature of the boundary curve at this point is non-zero. By changing the
coordinate (x, z) by an aﬃne transformation appropriately, we can assume that this point
is the origin (0, 0), and the domain (95) is in the upper half plane and it is tangent to the
x-axis at the origin. Then, in a neighborhood of the origin, we can present the boundary
curve as z = f(x) with some smooth function f deﬁned in a neighborhood of 0. It is
suﬃcient to show that f ′′(0)̸ = 0.
We show that f ′′(0)̸ = 0, as follows. Since the boundary curve is given by F(x, z) = 0,
we have that F
(
x, f(x)
)
= 0. Its diﬀerential is given by
Fx(x, z) + Fz(x, z) f ′(x) = 0,
where the subscripts of x and z means
∂
∂x and
∂
∂z respectively. Since the domain (95) is
tangent to the x-axis at the origin, Fx(0, 0) = f ′(0) = 0. Further, the diﬀerential of the
above formula is given by
Fxx(x, z) + 2 Fxz(x, z) f ′(x) + Fzz(x, z)
(
f ′(x)
)2 + Fz(x, z) f ′′(x) = 0.
By putting x = z = 0, we have that
Fxx(0, 0) + Fz(0, 0) f ′′(0) = 0.
We obtain
(Fxx
)
from the Hesse matrix
(
Fxx
Fxz
Fxz
Fzz
)
by restricting R2 to R×{0}. Since the Hesse matrix is negative deﬁnite, we obtain that
Fxx(x, z) < 0 for any (x, z). Further, we consider the function g(z) = F(0, z). This is a
concave function such that g′′(z) < 0 and the maximal point z0 of g(z) is positive. Hence,
the function g′(z) is monotonically decreasing, and g′(z0) = 0 for z0 > 0. Therefore,
Fz(0, 0) = g′(0) > 0. Hence, we obtain that
f ′′(0) = −Fxx(0, 0)
Fz(0, 0)
> 0,
as required.
B.2
Curvature of the boundary of the domain {Re ˆV (t, s, u) ≥ςR}
In this section, we consider 3-variable case. Instead of the function Re ˆV (t, s, u) −ςR , we
consider a function F(x, y, z) in general.
Let F(x, y, z) be a smooth concave function whose maximal value is positive. Then,
the domain
{
(x, y, z) ∈R3 

 F(x, y, z) ≥0
}
(96)
60
is a convex domain and its boundary is a smooth surface. The aim of this section is to
show the following lemma.
Lemma B.2. Let F(x, y, z) be a smooth concave function whose maximal value is positive
and Hesse matrix is negative deﬁnite. Then, the domain (96) is a convex domain and its
boundary is a smooth surface whose Gaussian curvature is positive everywhere.
Proof. We choose any point on the boundary of the domain (96). Similarly as in the proof
of Lemma B.1, we can assume that this point is the origin (0, 0, 0), and the domain (96)
is in the upper half space and it is tangent to the (x, y)-plane at the origin. Then, in a
neighborhood of the origin, we can present the boundary curve as z = f(x, y) with some
smooth function f deﬁned in a neighborhood of 0. It is suﬃcient to show that the Hesse
matrix of f is positive deﬁnite at the origin.
We show that the Hesse matrix of f is positive deﬁnite at the origin, as follows. Since
the boundary curve is given by F(x, y, z) = 0, we have that F
(
x, y, f(x, y)
)
= 0. Its
diﬀerentials are given by
Fx(x, y, z) + Fz(x, y, z) fx(x, y) = 0,
Fy(x, y, z) + Fz(x, y, z) fy(x, y) = 0.
Since the domain (95) is tangent to the (x, y)-plane at the origin, fx(0, 0) = fy(0, 0) = 0.
Further, the diﬀerentials of the above formulas are given by
Fxx(x, y, z) + 2 Fxz(x, y, z) fx(x, y) + Fzz(x, y, z)
(
fx(x, y)
)2 + Fz(x, y, z) fxx(x, y) = 0,
Fxy(x, y, z) + Fxz(x, y, z) fy(x, y) + Fyz(x, y, z) fx(x, y)
+ Fzz(x, y, z) fx(x, y) fy(x, y) + Fz(x, y, z) fxy(x, y) = 0,
Fyy(x, y, z) + 2 Fyz(x, y, z) fy(x, y) + Fzz(x, y, z)
(
fx(x, y)
)2 + Fz(x, y, z) fyy(x, y) = 0.
By putting x = y = z = 0, we have that
Fxx(0, 0, 0) + Fz(0, 0, 0) fxx(0, 0) = 0,
Fxy(0, 0, 0) + Fz(0, 0, 0) fxy(0, 0) = 0,
Fyy(0, 0, 0) + Fz(0, 0, 0) fyy(0, 0) = 0.
Further, by considering the function g(z) = F(0, 0, z), we can show that Fz(0, 0, 0) =
g′(0) > 0, similarly as in the proof of Lemma B.1. Furthermore, we obtain the following
matrix
−Fz(0, 0, 0)
(
fxx(0, 0)
fxy(0, 0)
fxy(0, 0)
fyy(0, 0)
)
=
(
Fxx(0, 0, 0)
Fxy(0, 0, 0)
Fxy(0, 0, 0)
Fyy(0, 0, 0)
)
from the Hesse matrix of F by restricting R3 to R2×{0}. Therefore, the above matrix
is negative deﬁnite. Hence, the Hesse matrix of f is positive deﬁnite at the origin, as
required.
C
On the domain {Re ˆV (t, s, u) ≥ς} for the 63 knot
In Section 5.1, we put
∆=
{
(t, s, u) ∈R3 

 0 ≤t ≤s < 1,
0 ≤u ≤s
}
,
61
and consider the following domain in (82), which we put to be ˆ∆in this section,
ˆ∆=
{
(t, s, u) ∈∆

 2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u) −ς ≥0
}
.
We note that this domain is symmetric with respect to the exchange of t and u. The aim
of this section is to show the following lemma.
Lemma C.1. ˆ∆is a compact convex domain in the interior of ∆, and the boundary of
ˆ∆is a smooth closed surface whose Gaussian curvature is positive everywhere.
We show a proof of the lemma later in this section. Before showing it, we show some
lemmas.
Lemma C.2. The boundary of ∆is included in the complement of ˆ∆in ∆. That is, ˆ∆
is included in the interior of ∆.
Proof. We consider the deﬁning inequality of ˆ∆,
2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u) −ς ≥0.
(97)
It is suﬃcient to show that any boundary point of ∆does not satisfy this inequality. The
boundary of ∆consists of ﬁve faces: {t = 0}, {t = s}, {s = 1}, {u = 0} and {u = s}.
When t = 0, the left-hand side of (97) is rewritten
−Λ(s) + Λ(s −u) + 2 Λ(u) −ς ≤4 Λ
(1
6
)
−ς = −0.25994... < 0.
Hence, the face {t = 0} is included in the complement of ˆ∆.
When t = s, the left-hand side of (97) is rewritten
Λ(t −u) + 2 Λ(u) −ς ≤3 Λ
(1
6
)
−ς = −0.421473... < 0.
Hence, the face {t = s} is included in the complement of ˆ∆.
When s = 1, the left-hand side of (97) is rewritten
Λ(t) + Λ(u) −ς ≤2 Λ
(1
6
)
−ς = −0.583006... < 0.
Hence, the face {s = 1} is included in the complement of ˆ∆.
Further, it is shown that the other faces are included in the complement of ˆ∆from the
above results by the symmetry with respect to the exchange of t and u.
Therefore, we obtain the lemma.
Lemma C.3. Let (t, s, u) ∈ˆ∆. Then, s > 0.5.
Proof. We suppose that s was less than or equal to 0.5 (and show a contradiction). The
function of the deﬁning inequality of ˆ∆splits into the following two summands,
2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u) −ς
=
(
2 Λ(t) + Λ(s −t) −Λ(s) −1
2 ς
)
+
(
2 Λ(u) + Λ(s −u) −Λ(s) −1
2 ς
)
.
(98)
62
We show that, for such an arbitrarily ﬁxed s, the ﬁrst summand is negative,
2 Λ(t) + Λ(s −t) −Λ(s) −1
2 ς < 0
for 0 ≤t ≤s.
(99)
(Then, it is shown similarly that the second summand of (98) is also negative, and this
contradicts the deﬁning inequality of ˆ∆, which implies the assumption of the lemma.)
Hence, it is suﬃcient to show (99) for s ≤0.5.
We show (99), as follows. For a ﬁxed s ≤0.5, we put
f(t) = 2 Λ(t) + Λ(s −t) −Λ(s) −1
2 ς
for 0 ≤t ≤s. Then,
f ′(t) = 2 Λ′(t) −Λ′(s −t).
Since Λ(t) and Λ(s −t) are concave functions in 0 ≤t ≤s whose second derivatives are
negative, f(t) has a unique maximal point in 0 ≤t ≤s, noting that limt→+0 f ′(t) = ∞
and limt→s−0 f ′(t) = −∞. We put such a unique maximal point to be ˆt, that is, ˆt is a
unique solution of f ′(t) = 0 in 0 ≤t ≤s. Since f ′(ˆt) = 0,
2 Λ′(ˆt) = Λ′(s −ˆt).
Further, since Λ′(t) = −log 2 sin πt,
sin π(s −ˆt) = 2 sin2 πˆt.
Since 2 sin2 πˆt ≤1 and 0 ≤ˆt ≤0.5, we have that 0 ≤ˆt ≤0.25. Hence,
s = ˆt + 1
π arcsin
(
2 sin2 πˆt
)
.
We put the right-hand side of this formula to be g(ˆt), that is, s = g(ˆt). Since sin2 πˆt is
monotonically increasing in 0 ≤ˆt ≤0.25, g(ˆt) is also monotonically increasing. We note
that g(0) = 0 and g(0.25) = 0.75. So, in fact, we can deﬁne g(ˆt) for 0 ≤ˆt ≤0.25, but we
substantially consider the case where
0 ≤ˆt ≤g−1(0.5) = 0.2148... ≤0.22.
In order to show (99), it is suﬃcient to show that
2 Λ(ˆt) + Λ
(
g(ˆt) −ˆt
)
−Λ
(
g(ˆt)
)
−1
2 ς < 0
for 0 ≤ˆt ≤g−1(0.5). We put the left-hand side of the above formula to be P(ˆt). We
have that
P ′(ˆt) = 2 Λ′(ˆt) + Λ′(
g(ˆt) −ˆt
)(
g′(ˆt) −1
)
−Λ′(
g(ˆt)
)
g′(ˆt)
= Λ′(s −ˆt) + Λ′(s −ˆt)
(
g′(ˆt) −1
)
−Λ′(s) g′(ˆt)
=
(
Λ′(s −ˆt) −Λ′(s)
)
g′(ˆt),
63
where we obtain the second equality by 2 Λ′(ˆt) = Λ′(s−ˆt). Since g(ˆt) is monotonically
increasing, g′(ˆt) > 0. Further, since Λ′(v) is monotonically decreasing in 0 < v ≤0.5 and
0 ≤s−ˆt ≤s ≤0.5, we have that Λ′(s−ˆt) −Λ′(s) > 0 for 0 < ˆt ≤g−1(0.5). Therefore,
P ′(ˆt) > 0, and P(ˆt) is monotonically increasing. Since
P(0) = −0.453036... < 0
and
P(0.22) = −0.00453122... < 0,
we obtain that P(ˆt) < 0 for 0 ≤ˆt ≤g−1(0.5). This implies (99), completing the proof of
the lemma.
Lemma C.4. Let (t, s, u) ∈ˆ∆. Then, t < 0.5 or u < 0.5.
Proof. We suppose that 0.5 ≤t ≤1 and 0.5 ≤u ≤1. Then, the function of the deﬁning
inequality of ˆ∆is calculated as
2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u) −ς
≤Λ(s −t) −2 Λ(s) + Λ(s −u) −ς ≤4 Λ
(1
6
)
−ς = −0.25994... < 0,
and this contradicts the deﬁning inequality of ˆ∆, which implies the assumption of the
lemma.
Hence, t < 0.5 or u < 0.5, as required.
Lemma C.5. Let (t, s, u) ∈ˆ∆. Then, t < 0.5 and u < 0.5.
Proof. By Lemma C.4, we have that t < 0.5 or u < 0.5. We consider each of these two
cases in the following of this proof.
We suppose that t < 0.5. Then, we show that u < 0.5, as follows. We consider the
maximal value of 2Λ(t) + Λ(s −t) −2Λ(s) for 0 ≤t < 0.5 and 0.5 < s ≤1. As we showed
in Section 4.2 (exchanging t and s), when (t, s) = (1
4, 3
4), this maximal value is given by
4Λ(1
4). Hence, by the deﬁning inequality of ˆ∆,
0 ≤
(
2 Λ(t) + Λ(s −t) −2 Λ(s)
)
+ Λ(s −u) + 2 Λ(u) −ς
≤4 Λ
(1
4
)
+ Λ(s −u) + 2 Λ(u) −ς .
Therefore,
2 Λ(u) ≥ς −4 Λ
(1
4
)
−Λ(s −u) ≥ς −4 Λ
(1
4
)
−Λ
(1
6
)
= 0.161417... > 0.
Hence, u < 0.5, and we obtain the conclusion of the lemma in this case.
We suppose that u < 0.5. Then, it is shown that t < 0.5 from the above argument by
exchanging t and u. Hence, we also obtain the conclusion of the lemma in this case.
We now show a proof of Lemma C.1 by using above lemmas.
64
Proof of Lemma C.1. By Lemmas C.2, C.3 and C.5, the domain ˆ∆is included in
{
(t, s, u)

 0 < t < 0.5,
0.5 < s < 1,
0 < u < 0.5
}
.
We put H to be the Hesse matrix of the function
2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u) −ς,
which deﬁnes ˆ∆. By Lemma B.2, it is suﬃcient to show that H is negative deﬁnite.
We show that H is negative deﬁnite, as follows. We have that
H =


2 Λ′′(t) + Λ′′(s −t)
−Λ′′(s −t)
0
−Λ′′(s −t)
−2 Λ′′(s) + Λ′′(s −t) + Λ′′(s −u)
−Λ′′(s −u)
0
−Λ′′(s −u)
2 Λ′′(u) + Λ′′(s −u)


= −π


2 cot πt + cot π(s−t)
−cot π(s−t)
0
−cot π(s−t)
−2 cot πs + cot π(s−t) + cot π(s−u)
−cot π(s−u)
0
−cot π(s−u)
2 cot πu + cot π(s−u)

.
We put a = cot πt, b = −cot πs and c = cot πu, noting that they are positive. Further,
noting that cot(α+β) = (cot α cot β −1)/(cot α + cot β), we have that
−1
π H =


2a −ab−1
a+b
ab−1
a+b
0
ab−1
a+b
2b −ab−1
a+b −bc−1
b+c
bc−1
b+c
0
bc−1
b+c
2c −bc−1
b+c

.
It is suﬃcient to show that the above matrix is positive deﬁnite. By Lemma C.6 below,
it is suﬃcient to show that
(2a −ab−1
a+b
ab−1
a+b
ab−1
a+b
b −ab−1
a+b
)
and
(b −bc−1
b+c
bc−1
b+c
bc−1
b+c
2c −bc−1
b+c
)
are positive deﬁnite. Further, by Lemma C.7 below, they are positive deﬁnite. Therefore,
H is negative deﬁnite, as required.
The following two lemmas are used in the above proof of Lemma C.1.
Lemma C.6. Let αi and βi be real numbers. If
(
α1
α2
α2
α3
)
and
(
β3
β2
β2
β1
)
are positive
deﬁnite, then


α1
α2
0
α2
α3+β3
β2
0
β2
β1


is positive deﬁnite.
Proof. Since
(α1
)
is obtained from
(
α1
α2
α2
α3
)
by restricting R2 to R×{0},
(α1
)
is positive
deﬁnite, i.e., α1 > 0. Hence,
(
α1
α2
α2
α3
)
is related to
(
α1
0
0
α3 −α2
2/α1
)
by an elementary
65
transformation as a quadratic form. Therefore, α3 −α2
2/α1 > 0. In the same way, we
obtain that β1 > 0 and β3 −β2
2/β1 > 0. Further, the required matrix is related to the
following matrix by elementary transformations,


α1
0
0
0
α3 −α2
2
α1 + β3 −β2
2
β1
0
0
0
β3

.
Since the diagonal entries are positive, the required matrix is positive deﬁnite.
Lemma C.7. Let a, b and c be positive real numbers. Then, the following matrices are
positive deﬁnite,
(2a −ab−1
a+b
ab−1
a+b
ab−1
a+b
b −ab−1
a+b
)
,
(b −bc−1
b+c
bc−1
b+c
bc−1
b+c
2c −bc−1
b+c
)
.
Proof. We show the lemma for the ﬁrst matrix, as follows. Its trace is given by
2a + b −2 · ab −1
a + b
= (2a + b)(a + b) −2ab + 2
a + b
= 2a2 + b2 + ab + 2
a + b
> 0.
Further, its determinant is given by
2ab −(2a + b) · ab −1
a + b
= 2ab(a + b) −(2a + b)(ab −1)
a + b
= ab2 + 2a + b
a + b
> 0.
Hence, the two eigenvalues of this matrix are positive, and the ﬁrst matrix of the lemma
is positive deﬁnite.
It is shown that the second matrix is also positive deﬁnite from the above argument
replacing a with c.
D
Estimate of |(q)n| and restriction of ∆to ∆′
In this section, we give an estimate of
1
N log |(q)n| in Lemma D.2. By using this estimate,
we explain why we can restrict ∆to ∆′ in Sections 3.1, 4.1 and 5.1.
We explain the motivation to show Lemma D.2. By (6) and (11), we have that
log

(q)n

 = Re φ
( 1
2N
)
−Re φ
(2n + 1
2N
)
= 1
2 log N −Re φ
(2n + 1
2N
)
.
We arbitrarily ﬁx a suﬃciently small δ > 0. Then, we can show by Proposition 2.1 that
Re 1
N φ
(2n + 1
2N
)
= Re
1
2π√−1 Li2
(
e(2n+1)/(2N))
+ O
( 1
N 2
)
= Λ
(2n + 1
2N
)
+ O
( 1
N 2
)
,
for suﬃciently large N and any integer n such that δ ≤2n+1
2N ≤1−δ, where O( 1
N2) means
that the absolute value of the error term is bounded by C1/N 2 with some constant C1,
66
which is independent of N and n (but might be dependent on δ). Hence, there exists
C > 0 such that

 1
N log

(q)n

 + Λ
(2n + 1
2N
) 

 ≤C · log N
N
for suﬃciently large N and any integer n such that δ ≤2n+1
2N ≤1 −δ. The aim of Lemma
D.2 is to extend this estimate to the case where δ = 0.
Before we show Lemma D.2, we show the following lemma.
Lemma D.1. There exist C1, C2 > 0 such that

 Λ
( 1
N
) 

 ≤C1 · log N
N
,

 Λ
( 1
2N
) 

 ≤C2 · log N
N
,
for any suﬃciently large N. That is,
Λ
( 1
N
)
= O
(log N
N
)
,
Λ
( 1
2N
)
= O
(log N
N
)
.
Proof. Since Λ′(t) = −log 2 sin πt, we have that
Λ(t) =
∫t
0
(
−log 2 sin πs
)
ds.
Let t be suﬃciently small. Since sin x ≥x −1
6x3 = x(1 −1
6x2) for suﬃciently small x,
Λ(t) ≤
∫t
0
(
−log 2πs (1 −1
6 π2s2)
)
ds =
∫t
0
(
−log 2πs −log(1 −1
6 π2s2)
)
ds
≤
∫t
0
(
−log 2πs −2s2)
ds = −t log 2πt + t + 2
3 t3,
where we obtain the second inequality, since −log(1 −1
6π2s2) = 1
6π2s2 + O(s4) ≤2s2 for
suﬃciently small s. Hence,
Λ
( 1
N
)
≤−1
N log 2π
N + 1
N +
2
3N 3 = O
(log N
N
)
.
Since Λ(t) is non-negative for suﬃciently small t, we obtain the ﬁrst formula of the lemma.
We obtain the second formula of the lemma from the ﬁrst formula by replacing N with
2N.
Lemma D.2. There exists C > 0 such that

 1
N log

(q)n

 + Λ
(2n + 1
2N
) 

 ≤C · log N
N
for any suﬃciently large N and any integer n such that 0 ≤n < N. That is,
1
N log

(q)n

 = −Λ
(2n + 1
2N
)
+ O
(log N
N
)
as N →∞ﬁxing a value of n/N.
67
Proof. When n = 0, we can verify the lemma by Lemma D.1.
So, we assume that
1 ≤n ≤N −1, in the following of this proof. From the deﬁnition of (q)n , we have that
log

(q)n

 = log
∏
1≤j≤n

1 −qj

 =
∑
1≤j≤n
log 2 sin π j
N
= −
∑
1≤j≤n
Λ′( j
N
)
.
(100)
Further, we note that Λ′(t) is a convex function for 0 < t < 1, since Λ′′′(t) = π2/ sin2 πt ≥
π2 for 0 < t < 1.
We give a lower bound of “ 1
N log

(q)n

 + Λ
(2n+1
2N
)
”, as follows. Since Λ′(t) is a convex
function, the tangent line of the graph of Λ′(t) at t = N/j is located under the graph of
Λ′(t). Hence, by integrating them for 2j−1
2N ≤t ≤2j+1
2N , we obtain that
1
N Λ′( j
N
)
≤
∫(2j+1)/(2N)
(2j−1)/(2N)
Λ′(t) dt.
Further, by making the sum of the above formula over 1 ≤j ≤n, we have that
1
N
∑
1≤j≤n
Λ′( j
N
)
≤
∫(2n+1)/(2N)
1/(2N)
Λ′(t) dt = Λ
(2n + 1
2N
)
−Λ
( 1
2N
)
.
Therefore, by (100),
1
N log

(q)n

 + Λ
(2n + 1
2N
)
≥Λ
( 1
2N
)
= O
(log N
N
)
,
(101)
where we obtain the last equality by Lemma D.1.
We give an upper bound of “ 1
N log

(q)n

+Λ
( 2n+1
2N
)
”, as follows. Since Λ′(t) is a convex
function, the line connecting
( j
N , Λ′( j
N )
)
and
(j+1
N , Λ′(j+1
N )
)
is located over the graph of
Λ′(t). Hence, by integrating them for
j
N ≤t ≤j+1
N , we obtain that
∫(j+1)/N
j/N
Λ′(t) dt ≤
1
2N
(
Λ′( j
N
)
+ Λ′(j + 1
N
))
.
Further, by making the sum of the above formula over 1 ≤j ≤n, we have that
∫n/N
1/N
Λ′(t) dt ≤
1
N
∑
1≤j≤n
Λ′( j
N
)
−1
2N
(
Λ′( 1
N
)
+ Λ′( n
N
))
.
Furthermore, in a similar way as above, we have that
∫(2n+1)/(2N)
n/N
Λ′(t) dt ≤
1
4N
(
Λ′( n
N
)
+ Λ′(2n + 1
2N
))
.
Hence, as the sum of the above two formulas, we obtain the following inequality,
Λ
(2n+1
2N
)
−Λ
( 1
2N
)
=
∫(2n+1)/(2N)
1/(2N)
Λ′(t) dt
≤
1
N
∑
1≤j≤n
Λ′( j
N
)
−1
2N Λ′( 1
N
)
−1
4N Λ′( n
N
)
+ 1
4N Λ′(2n+1
N
)
.
68
Therefore, by (100),
1
N log

(q)n

 + Λ
(2n+1
2N
)
≤Λ
( 1
2N
)
−1
2N Λ′( 1
N
)
−1
4N Λ′( n
N
)
+ 1
4N Λ′(2n+1
N
)
= O
(log N
N
)
,
(102)
where we obtain the last equality by Lemma D.1 and from the fact that Λ′(t) = −log 2 sin πt,
noting that 1 ≤n ≤N −1.
Therefore, by (101) and (102), we obtain the required formula of the lemma.
Restriction of ∆to ∆′ for the 61 knot
We explain why we can restrict ∆to ∆′ in Section 3.1, that is, we show the equality
of (32).
Proof of the equality of (32). By Lemma D.2, we can show that
1
N log

the summand of (29)

 = Re ˆV
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
)
+ O
(log N
N
)
. (103)
We note that this convergence is uniform, i.e., the absolute value of the error term is
bounded by C · log N
N
, where C is a constant which is independent of i, j, k. We recall that
∆′ is a domain in ∆satisfying (30) for some ε > 0. Then, in order to show the equality
of (32), it is suﬃcient to show that the following sum is of the order O(e−Nε′) for some
ε′ > 0,

∑
i,j,k ∈Z
( 2i+1
2N , 2j+1
2N , 2k+1
2N )∈∆−∆′
exp
(
N · V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
)
−Nς
) 

≤
∑
i,j,k ∈Z
( 2i+1
2N , 2j+1
2N , 2k+1
2N )∈∆−∆′

 exp
(
N · V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
)
−Nς
) 

=
∑
i,j,k ∈Z
( 2i+1
2N , 2j+1
2N , 2k+1
2N )∈∆−∆′
exp
(
N · Re V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
)
−NςR
)
.
(104)
By (103), the convergence of Re V (·) to Re ˆV (·) is uniform. Hence, for any ε1 > 0,
Re V
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
)
≤Re ˆV
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
)
+ ε1
for suﬃciently large N. Therefore, by choosing suﬃciently small ε1, we have that
(104) ≤
∑
i,j,k ∈Z
( 2i+1
2N , 2j+1
2N , 2k+1
2N )∈∆−∆′
exp
(
N · Re ˆV
(2i + 1
2N , 2j + 1
2N
, 2k + 1
2N
)
−NςR + Nε1
)
= O
(
e−N ε2)
,
for some ε2 > 0. Hence, we obtain the equality of (32).
69
Restriction of ∆to ∆′ for the 62 knot and the 63 knot
In similar ways as above, we can restrict ∆to ∆′ for the sums of ⟨62 ⟩N and ⟨63 ⟩N.
That is, we can show (54) and (80) by using Lemma D.2 in similar ways as in the above
proof for the 61 knot.
