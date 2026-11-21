---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-012-42-estimate-of-the-range-of
section_title: "Estimate of the range of ∆′"
section_number: 4.2
pages: 30-33
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Estimate of the range of ∆′
In this section, we calculate the concrete values of the bounds of the inequalities in (53)
so that they satisfy that ∆−∆′ ⊂(52).
Putting Λ as in Section 2.2, we have that
Re ˆV (t, s, u) = −2 Λ(t) + Λ(t −s) + 2 Λ(s) + Λ(u).
We consider the domain
{
(t, s, u) ∈∆

 −2 Λ(t) + Λ(t −s) + 2 Λ(s) + Λ(u) ≥ςR
}
.
(56)
We note that this domain is symmetric with respect to the exchange of (t, s, u) and
(1−s, 1−t, u). The aim of this section is to show that this domain is included in the
interior of the domain ∆′ of (53).
In order to estimate t and s, we consider the area of (t, s) such that (t, s, u) belongs to
the domain (56) for some u. Since Λ( · ) ≤Λ(1
6),
−2 Λ(t) ≥ςR −4 Λ
(1
6
)
= 0.054282... > 0,
and hence, 1
2 < t < 1. Similarly, we have that 0 < s < 1
2. Further, since Λ(u) ≤Λ(1
6),
−2 Λ(t) + Λ(t −s) + 2 Λ(s) ≥ςR −Λ
(1
6
)
= 0.538881... .
We consider the following domain
{
(t, s) | 0.5 < t < 1,
0 < s < 0.5,
−2 Λ(t) + Λ(t −s) + 2 Λ(s) ≥ςR −Λ
(1
6
)}
. (57)
We graphically show this domain in Figure 2.
Before calculating t and s, we show that the domain (57) is convex. We put F(t, s) =
−2 Λ(t) + Λ(t −s) + 2 Λ(s). Its diﬀerentials are given by
∂F
∂t
= −2 Λ′(t) + Λ′(t −s),
∂F
∂s
= 2 Λ′(s) −Λ′(t −s).
Hence,
∂2F
∂t2
= −2 Λ′′(t) + Λ′′(t −s) = 2π cot πt −π cot π(t −s),
30
0.7
0.8
0.9
0.1
0.2
0.3
0.4
0.5
0.6
0.6≤t
0.14 ≤s
t−s ≤0.67
t ≤0.86
s ≤0.4
0.3 ≤t−s
Figure 2: The domain (57)
∂2F
∂t ∂s = −Λ′′(t −s) = π cot π(t −s),
∂2F
∂s2
= 2 Λ′′(s) + Λ′′(t −s) = −2π cot πs −π cot π(t −s).
We put a = −cot πt and b = cot πs, noting that they are positive since 0.5 < t < 1 and
0 < s < 0.5. Further, noting that cot(α+β) = (cot α cot β −1)/(cot α + cot β), we have
that
1
π · ∂2F
∂t2
= −2a + ab −1
a + b ,
1
π · ∂2F
∂t ∂s = −ab −1
a + b ,
1
π · ∂2F
∂s2
= −2b + ab −1
a + b .
We put the Hesse matrix of F to be H. Then,
1
π ·trace H = −2a−2b+2·ab−1
a + b = −2
(
(a+b)2 −ab + 1
)
a + b
= −2
(
a2 + b2 + ab + 1
)
a + b
< 0.
Further,
1
π2 · det H = 4ab −(2a + 2b) · ab −1
a + b
= 2(ab + 1) > 0.
Hence, the two eigenvalues of H are nagative, and H is negative deﬁnite. Therefore, F
is a concave function on
{
(t, s)

 0.5 < t < 1, 0 < s < 0.5
}
, whose Hesse matrix is
negative deﬁnite. Hence, the domain (57) is a compact convex domain, and its boundary
is a smooth closed curve whose curvature is non-zero everywhere (see Lemma B.1).
We calculate the minimal value tmin and the maximal value tmax of t in the domain
(57). We consider the line t = c in the (t, s) plane for a constant c. The values tmin and
tmax are given when this line is tangent to the domain (57). The tangent points of such
lines are given by the following equations,



−2 Λ(t) + Λ(t −s) + 2 Λ(s) = ςR −Λ
(1
6
)
,
∂
∂s
(
−2 Λ(t) + Λ(t −s) + 2 Λ(s)
)
= 0.
31
Since the curvature of the boundary curve of the domain (57) is non-zero everywhere (see
Lemma B.1), there are exactly two such tangent points, and the above system of equations
has exactly two solutions tmin and tmax. By calculating a solution by Newton’s method
from (t, s) = (0.6, 0.25), we obtain tmin = 0.619717... , and from (t, s) = (0.85, 0.25), we
obtain tmax = 0.857766... . Therefore, we obtain an estimate of t in ∆′ as
0.6 ≤t ≤0.86.
To be precise (see Remark 3.2), we can rigorously verify the above estimate of the solutions
of the above system of equations in a similar way as in Section A.2.
We obtain an estimate of s in ∆′ from the above formula by using the symmetry
exchanging (t, s) and (1−s, 1−t), and hence, we obtain that
0.14 ≤s ≤0.4.
We calculate the minimal value umin and the maximal value umax of u. The maximal
point of −2 Λ(t) + Λ(t −s) + 2 Λ(s) is given by a solution of the following equations,





∂
∂t
(
−2 Λ(t) + Λ(t −s) + 2 Λ(s)
)
= 0,
∂
∂s
(
−2 Λ(t) + Λ(t −s) + 2 Λ(s)
)
= 0.
Their solution is (t, s) = ( 3
4, 1
4). Hence,
Λ(u) ≥ςR −4 Λ
(1
4
)
= 0.117292... .
By calculating solutions of the equality of the above formula by Newton’s method, we
obtain umin = 0.0586318... and umax = 0.315289... . Therefore, we obtain an estimate of
u in ∆′ as
0.05 ≤u ≤0.4.
To be precise (see Remark 3.1), we can rigorously verify the above estimate in a similar
way as in Section A.1.
We calculate the minimal value (t −s)min and the maximal value (t −s)max of t −s.
Putting w = t −s, they satisfy the following equations,



−2 Λ(t) + Λ(w) + 2 Λ(t −w) = ςR −Λ
( 1
6
)
,
∂
∂t
(
−2 Λ(t) + Λ(w) + 2 Λ(t −w)
)
= 0.
We note that this system of equations has exactly two solutions. By calculating a solution
of them by Newton’s method from (t, w) = (0.65, 0.3), we obtain (t −s)min = 0.334132...,
and from (t, w) = (0.85, 0.7), we obtain (t −s)max = 0.665868... . Therefore, we obtain an
estimate of t −s in ∆′ as
0.3 ≤t −s ≤0.67.
To be precise (see Remark 3.2), we can rigorously verify the above estimate of the solutions
of the above system of equations in a similar way as in Section A.2.
32
Before calculating 2s + u, we show that the domain (56) is convex. Since the function
−2Λ(t) + Λ(t −s) + 2Λ(s) and Λ(u) are concave functions whose Hesse matrices are
negative deﬁnite, the function −2Λ(t) + Λ(t−s) + 2Λ(s) + Λ(u) is also such a function
on
{
(t, s, u)

 0.5 < t < 1, 0 < s < 0.5, 0 < u < 0.5
}
. Hence, the domain is a convex
domain and its boundary is a smooth closed surface whose Gaussian curvature is positive
everywhere (see Lemma B.2).
We calculate the maximal value (2s+u)max of 2s+u. We consider the plane 2s+u = c
for a constant c. The maximal value (2s + u)max is obtained when this plane is tangent
to the domain (56); we note that there are exactly two such tangent points. Putting
2w′ = 2s + u, such tangent points are given by the following equations,









−2 Λ(t) + Λ
(
t −w′ + 1
2u
)
+ 2 Λ
(
w′ −1
2u
)
+ Λ(u) = ςR ,
∂
∂t
(
−2 Λ(t) + Λ
(
t −w′ + 1
2u
)
+ 2 Λ
(
w′ −1
2u
)
+ Λ(u)
)
= 0,
∂
∂u
(
−2 Λ(t) + Λ
(
t −w′ + 1
2u
)
+ 2 Λ
(
w′ −1
2u
)
+ Λ(u)
)
= 0.
(58)
We note that this system of equations has exactly two solutions. By calculating a solution
of them by Newton’s method from (t, w′, u) = (0.75, 0.5, 0.25), we obtain (2s + u)max =
0.958506... . Therefore, we obtain an estimate of 2s + u in ∆′ as
2s + u ≤0.97.
Remark 4.1. To be precise, the above argument is not partially rigorous, since we do
not estimate the error term of the numerical solution of Newton’s method, though the
above argument is practically useful, since we can guess that such an error term would
be suﬃciently small for the above purpose. In order to complete the above argument, we
give a rigorous proof of an estimate of a solution of (58) in Lemma A.3.
