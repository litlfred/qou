---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-024-estimate-of-a-solution-of-58
section_title: "Estimate of a solution of (58)"
section_number: null
pages: 58-59
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Estimate of a solution of (58)
In this section, we explain how to estimate a solution in 3-variable case. We explain it
for a solution of (58); we can estimate solutions in other 3-variable cases in similar ways.
As mentioned in Section 4.2, there are exactly two solutions of (58). These solutions
give the maximal and minimal values of 2s+u. We put the solution for the maximal value
to be (t1, s1, u1). Then, the maximal value of 2s + u is given by (2s + u)max = 2s1 + u1.
As we mentioned in Remark 4.1, we give a rigorous proof of an estimate of (2s + u)max in
the following lemma.
Lemma A.3. (2s + u)max ≤0.97.
Proof. The system of equations (58) is rewritten



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
+ Λ(u) −ςR = 0,
−2 Λ′(t) + Λ′(
t −w′ + 1
2u
)
= 0,
1
2Λ
(
t −w′ + 1
2u
)
−Λ
(
w′ −1
2u
)
+ Λ′(u) = 0,
where ςR = 0.700414248... . Putting s = w′ −1
2, they are rewritten





−2 Λ(t) + Λ(t −s) + 2 Λ(s) + Λ(u) −ςR = 0,
2 Λ′(t) = Λ′(t −s),
1
2 Λ′(t −s) −Λ′(s) + Λ′(u) = 0.
(94)
The second equation is rewritten
2 sin2 πt = sin π(t −s).
Hence,4
s = t −1
π arcsin
(
2 sin2 πt
)
.
We put the right-hand side of this formula to be f(t), that is, s = f(t). By the second
and third equations of (94), we obtain that
Λ′(u) = Λ′(s) −Λ′(t).
Hence,
u = 1
π arcsin
( sin πs
2 sin πt
)
.
Putting s = f(t), we put the right-hand side of this formula to be g(t), that is, u = g(t).
Further, putting
P(t) = −2 Λ(t) + Λ
(
t −f(t)
)
+ 2 Λ
(
f(t)
)
+ Λ
(
g(t)
)
−ςR ,
the system of equations (94) is rewritten as a single equation P(t) = 0.
4Here, we choose a branch of arcsin as −π/2 ≤arcsin(·) ≤π/2. By choosing another branch, we obtain an estimate of
the minimal value of 2s + u.
58
We estimate the solution (t1, s1, u1), as follows. Since
P(0.7586) = 0.000307098... > 0,
P(0.7587) = −0.000200034... < 0,
we have that
0.7586 < t1 < 0.7587.
In this range, arcsin
(
2 sin2 πt
)
is monotonically decreasing. Hence,
f(0.7586) < s1 < f(0.7587).
Further, since
f(0.7586) = 0.363692... > 0.3636,
f(0.7587) = 0.364407... < 0.3645,
we have that
0.3636 < s1 < 0.3645.
In these ranges,
sin πs
sin πt is monotonically increasing with respect to t and s respectively.
Hence,
1
π arcsin
( sin π 0.3636
2 sin π 0.7586
)
< u1 < 1
π arcsin
( sin π 0.3645
2 sin π 0.7587
)
.
Therefore, we obtain that
(2s + u)max = 2s1 + u1 < 2 · 0.3645 + 1
π arcsin
( sin π 0.3645
2 sin π 0.7587
)
= 0.959440... ≤0.97,
as required.
B
Curvature of the boundary of the domain {Re ˆV ≥ςR}
In Sections 3.2, 4.2 and 5.2, we estimated the maximal and minimal values of some linear
function L(t, s, u) on the domain
{
(t, s, u) | Re ˆV (t, s, u) ≥ςR
}
. This domain is a convex
domain whose boundary is a smooth closed surface. These maximal and minimal values
are obtained when the plane L(t, s, u) = c (where c is a constant) is tangent to this
domain. In order to show that there are exactly two such planes,5 we show that Gaussian
curvature of the boundary surface of this domain is positive in this section. We explain
2-, 3-variable cases in Sections B.1 and B.2 respectively.
