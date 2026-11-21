---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-017-52-estimate-of-the-range-of
section_title: "Estimate of the range of ∆′"
section_number: 5.2
pages: 48-50
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Estimate of the range of ∆′
In this section, we calculate the concrete values of the bounds of the inequalities in (79)
so that they satisfy that ∆−∆′ ⊂(78).
Putting Λ as in Section 2.2, we have that
Re ˆV (t, s, u) = 2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u).
We consider the domain
{
(t, s, u) ∈∆

 2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u) ≥ς
}
,
(82)
where we put ς = 0.906072... as in (86). We note that this domain is symmetric with
respect to the exchange of t and u. The aim of this section is to show that this domain
is included in the interior of the domain ∆′ of (79). We graphically show the set of (t, s)
satisfying that Re ˆV (t, s, u) ≥ς for some u in Figure 4.
0.20
0.25
0.30
0.55
0.60
0.65
0.18≤t
s−t ≤0.47
0.54 ≤s
0.3 ≤s−t
t ≤0.3
s ≤0.7
Figure 4: The set of (t, s) satisfying that Re ˆV (t, s, u) ≥ς for some u
We can show (see Lemma C.1) that the domain (82) is a compact convex domain and
its boundary is a smooth closed surface whose Gaussian curvature is positive everywhere.
We calculate the minimal value tmin and the maximal value tmax of t. We consider the
plane t = c for a constant c. The range of t is given as the range of c such that this plane
and the domain (82) has non-empty intersection. Since the domain (82) is a compact
convex domain whose boundary is a smooth closed surface, the maximal and minimal
values are given by the planes tangent to this domain. The tangent points of such planes
are given by solutions of the following equations,









2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u) = ς,
∂
∂s
(
2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u)
)
= 0,
∂
∂u
(
2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u)
)
= 0.
Since the boundary of the domain (82) is a smooth closed surface whose Gaussian cur-
vature is positive everywhere, there are exactly two such tangent points, and the above
48
system of equations has exactly two solutions, corresponding to the minimal and maximal
values of t. By calculating a solution by Newton’s method from (t, s, u) = (0.2, 0.6, 0.2),
we obtain tmin = 0.186629... , and from (t, s, u) = (0.3, 0.6, 0.3), we obtain tmax =
0.296109... . Therefore, we obtain an estimate of t in ∆′ as
0.18 ≤t ≤0.3.
To be precise (see Remark 4.1), we can rigorously verify the above estimate of the solutions
of the above system of equations in a similar way as in Section A.3.
We calculate the minimal value smin and the maximal value smax of s. They satisfy the
following equations,









2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u) = ς,
∂
∂t
(
2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u)
)
= 0,
∂
∂u
(
2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u)
)
= 0.
They are rewritten





2 Λ(t) + Λ(s −t) −2 Λ(s) + Λ(s −u) + 2 Λ(u) = ς,
2 Λ′(t) = Λ′(s −t),
2 Λ′(u) = Λ′(s −u).
We note that this system of equations has exactly two solutions. Since the above system
of equations is symmetric with respect to the exchange of t and u, the solutions of the
form (t, smin, u) and (t, smax, u) satisfy that t = u. Hence, the above system of equations
is rewritten
{
2 Λ(t) + Λ(s −t) −Λ(s) =
1
2ς,
2 Λ′(t) = Λ′(s −t).
We note again that this system of equations has exactly two solutions. By calculating
a solution of them by Newton’s method from (t, s) = (0.25, 0.55), we obtain smin =
0.547094... , and from (t, s) = (0.25, 0.7), we obtain smax = 0.688624... . Therefore, we
obtain an estimate of s in ∆′ as
0.54 ≤s ≤0.7.
To be precise (see Remark 3.2), we can rigorously verify the above estimate of the solutions
of the above system of equations in a similar way as in Section A.2.
We calculate the minimal value (s −t)min and the maximal value (s −t)max of s −t.
Putting w = s −t, they satisfy the following equations,









2 Λ(t) + Λ(w) −2 Λ(t + w) + Λ(t + w −u) + 2 Λ(u) = ς,
∂
∂t
(
2 Λ(t) + Λ(w) −2 Λ(t + w) + Λ(t + w −u) + 2 Λ(u)
)
= 0,
∂
∂u
(
2 Λ(t) + Λ(w) −2 Λ(t + w) + Λ(t + w −u) + 2 Λ(u)
)
= 0.
49
We note that this system of equations has exactly two solutions. By calculating a solution
by Newton’s method from (w, t, u) = (0.3, 0.25, 0.25), we obtain (s −t)min = 0.301964... ,
and from (w, t, u) = (0.5, 0.2, 0.2), we obtain (s −t)max = 0.462284... . Therefore, we
obtain an estimate of s −t in ∆′ as
0.3 ≤s −t ≤0.47.
To be precise (see Remark 4.1), we can rigorously verify the above estimate of the solutions
of the above system of equations in a similar way as in Section A.3.
We obtain the other bounds of ∆′ from the above bounds by the symmetry with respect
to the exchange of t and u.
