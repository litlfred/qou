---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-007-32-estimate-of-the-range-of
section_title: "Estimate of the range of ∆′"
section_number: 3.2
pages: 16-18
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Estimate of the range of ∆′
In this section, we calculate the concrete values of the bounds of the inequalities in (31)
so that they satisfy that ∆−∆′ ⊂(30).
Putting Λ as in Section 2.2, we have that
Re ˆV (t, s, u) = 2 Λ(t) + Λ(s) + Λ(u).
We consider the domain
{
(t, s, u) ∈∆

 2 Λ(t) + Λ(s) + Λ(u) ≥ςR
}
,
(34)
where we put ςR = 0.5035603... as in (41). We note that this domain is symmetric with
respect to the exchange of s and u. The aim of this section is to show that this domain
is included in the interior of the domain ∆′ of (31). For this purpose, we estimate ranges
of t, s, u and t+s+u in the domain (34).
We calculate the minimal value tmin and the maximal value tmax of t. Since Λ( · ) ≤
Λ(1
6),
2 Λ(t) ≥ςR −2 Λ
(1
6
)
= 0.180494... .
The minimal and maximal values of t are solutions of the following equation,
2 Λ(t) = ςR −2 Λ
(1
6
)
.
(35)
Noting that the behavior of Λ(t) is as shown in Section 2.2, this equation has exactly
two solutions in 0 < t < 0.5. By calculating a solution of this equation by Newton’s
method from t = 0.01, we obtain tmin = 0.0364809... , and from t = 0.4, we obtain
tmax = 0.363674... . Therefore, we obtain an estimate of t in ∆′ as
0.03 ≤t ≤0.4.
Remark 3.1. To be precise, the above argument is not partially rigorous, since we do
not estimate the error terms of the numerical solutions of Newton’s method, though the
above argument is practically useful, since we can guess that such error terms would be
suﬃciently small for the above purpose. In order to complete the above argument, we
give a rigorous proof of estimates of solutions of (35) in Lemma A.1.
We calculate the minimal value smin and the maximal value smax of s. Since Λ( · ) ≤
Λ(1
6),
Λ(s) ≥ςR −3 Λ
(1
6
)
= 0.0189614... .
The minimal and maximal values of s are solutions of the following equation,
Λ(s) = ςR −3 Λ
(1
6
)
.
Similarly as above, we note that this equation has exactly two solutions in 0 < s < 0.5.
By calculating a solution of the equation by Newton’s method from s = 0.001, we obtain
16
smin = 0.00406176... , and from s = 0.5, we obtain smax = 0.472596... . Therefore, we
obtain an estimate of s in ∆′ as
0.001 ≤s ≤0.5.
To be precise (see Remark 3.1), we can rigorously verify the above estimate of the solutions
of the above equation in a similar way as in Section A.1.
We obtain the estimate of u in ∆′ from the above formula by the symmetry with
respect to the exchange of s and u.
Before calculating t+s+u, we show that the domain (34) is convex, as follows. As
mentioned in Section 2.2, the function Λ(t) is a concave function for 0 < t < 0.5, whose
second derivative is negative. Hence, the function 2Λ(t) + Λ(s) + Λ(u) is concave on
{
(t, s, u)

 0 < t, s, u < 0.5
}
, whose Hesse matrix is negative deﬁnite. Therefore, the
domain (34) is convex. Further, we note that its boundary is a smooth closed surface
in
{
(t, s, u)

 0 < t, s, u < 0.5
}
, whose Gaussian curvature is positive everywhere (see
Lemma B.2).
We calculate the maximal value (t+s+u)max of t+s+u. We consider the plane t+s+u = c
for a constant c. The range of t+s+u is given as the range of c such that this plane and
the domain (34) has non-empty intersection. Since the domain (34) is a compact convex
domain whose boundary is a smooth closed surface, the maximal and minimal values are
given by the planes tangent to this domain. Putting w = t+s+u, the tangent points of
such planes are given by solutions of the following equations,









2 Λ(w −s −u) + Λ(s) + Λ(u) = ςR ,
∂
∂s
(
2 Λ(w −s −u) + Λ(s) + Λ(u)
)
= 0,
∂
∂u
(
2 Λ(w −s −u) + Λ(s) + Λ(u)
)
= 0.
These equations are rewritten





2 Λ(w −s −u) + Λ(s) + Λ(u) = ςR ,
−2 Λ′(w −s −u) + Λ′(s) = 0,
−2 Λ′(w −s −u) + Λ′(u) = 0.
Since the boundary of the domain (34) is a smooth closed surface whose Gaussian curva-
ture is positive everywhere (see Lemma B.2), there are exactly two such tangent points,
and the above system of equations has exactly two solutions, corresponding to the maxi-
mal and minimal values of t+s+u; we put the maximal value to be wmax. Since the above
system of equations is symmetric with respect to the exchange of s and u, the (unique)
solution of the form (wmax, s, u) satisﬁes that s = u. Hence, we can rewrite the above
system of equations as
{
2 Λ(w −2s) + 2 Λ(s) = ςR ,
−2 Λ′(w −2s) + Λ′(s) = 0.
(36)
17
By calculating a solution of these equations by Newton’s method from (w, s) = (1, 0.3),
we obtain (t+s+u)max = 0.925048... . Therefore, we obtain an estimate of t + s + u in ∆′
as
t + s + u ≤0.94.
Remark 3.2. To be precise, the above argument is not partially rigorous, since we do
not estimate the error term of the numerical solution of Newton’s method, though the
above argument is practically useful, since we can guess that such an error term would
be suﬃciently small for the above purpose. In order to complete the above argument, we
give a rigorous proof of an estimate of a solution of (36) in Lemma A.2.
