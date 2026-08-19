---
doc_id: arxiv-math-0506456v1
doc_title: "Journal of Knot Theory and Its Ramiﬁcations c© W orld Scientiﬁc Publishing Company ASYMPTOTICS OF THE QUANTUM INV ARIANTS FOR SURGERIES ON THE FIGURE 8 KNOT JØRGEN ELLEGAARD ANDERS"
section_id: sec-012-14-asymptotics-of-the-quantum-invariants-for-the
section_title: "Asymptotics of the quantum invariants for the ﬁgure 8 knot"
section_number: 14
pages: 13-15
source_pdf: 0506456v1.pdf
source_sha256: ce11210245a29eec
doc_brief: "Asymptotics of the quantum invariants for surgeries on the figure-8 knot (Andersen–Hansen, JKTR) — asymptotic expansion of the SU(2) Reshetikhin–Turaev invariants for surgeries on 4₁."
---
From now on we ﬁx γ =π/r (so r> 3). By Lemma 1 we get that
Sγ(ζ) = Sγ(ζ + 2π)
r−1∏
j=0
(
1 +e
√−1(ζ+(2j+1)π/r)
)
.
If we write ζ = −π + 2πx we get that
r−1∏
j=0
(
1 +e
√−1(ζ+(2j+1)π/r)
)
=
r−1∏
j=0
(
1 −wje2π√−1(x+ 1
2r )
)
,
where w =e2π√−1/r. Using 1 −zr =∏ r−1
j=0(1 −wjz) we get that
Sγ(−π + 2πx) =
(
1 +e2π√−1xr
)
Sγ(−π + 2π(x + 1)) (3.18)
for x ∈ C. Let
xn = n
r + 1
2r, n ∈ Z.
Thenx ↦→Sγ(−π + 2πx) is analytic on C \ {xn|n =r,r + 1,... }. If m is a positive
integer then {xn|n =mr,mr + 1,..., (m + 1)r − 1 } are poles of order m, while the
points {xn|n = −mr, −mr + 1,..., −mr +r − 1 } are zeros of order m.
Let us use the function Sγ to give another expression for τr(Mp/q). By Lemma 1
we have that m∏
l=0
(1 −ξk±l) =
m∏
l=0
Sγ(−π + 2γ(k ±l) −γ)
Sγ(−π + 2γ(k ±l) +γ).
Therefore
m∏
l=0
(1 −ξk−l) = Sγ(−π + 2γ(k −m) −γ)
Sγ(−π + 2γk +γ) ,
m∏
l=0
(1 −ξk+l) = Sγ(−π + 2γk −γ)
Sγ(−π + 2γ(k +m) +γ).
So m∏
l=0
(1 −ξk−l)(1 −ξk+l) = (1 −ξk)Sγ(−π + 2γ(k −m) −γ)
Sγ(−π + 2γ(k +m) +γ),
and then by (2.17)
τr(Mp/q) = β(r)
∑
n∈Z/|q|Z
r−1∑
k=1
r−1∑
m=0
fn,r
(k
r,m + 1/2
r
)
,
where
fn,r(x,y ) = sin
(π
q (x − 2nd)
)
e
2πir
(
dn2
q + p
4qx2− n
qx−xy
)
Sγ(−π + 2π(x −y))
Sγ(−π + 2π(x +y))
14 Asymptotics of the quantum invariants for the ﬁgure 8 knot
and
β(r) = − ia(r)
2 sin(π/r)
= isign(q)
r
√
|q|
e− 3πi
4 sign(pq) exp
(πi
2r
[
3sign(pq) − p
q + S
(p
q
)])
. (3.19)
Note that d is equal to the inverse of p modq and that the functions fn,r are
independent of the choice of this inverse. By the remarks following L emma 1 the
functions fn,r are holomorphic on Ω r × Ωr, where
Ωs =
{
w ∈ C | − 1
4s < Re(w)< 1 + 1
4s
}
(3.20)
for s ∈]0, ∞]. By the residue theorem we therefore end up with
Lemma 2. The quantum invariants of Mp/q are given by
τr(Mp/q) = β(r)r2
4
∑
n∈Z/|q|Z
∫
C 1r
cot(πrx)
(∫
C 2r
tan(πry)fn,r(x,y )dy
)
dx,
where β(r) is given by (3.19) and
fn,r(x,y ) = sin
(π
q (x − 2nd)
)
e2πir
(
dn2
q + p
4qx2− n
qx−xy
)
Sγ(−π + 2π(x −y))
Sγ(−π + 2π(x +y)),
and where C1
r is a closed curve in Ω r such that the poles {k/r |k = 1, 2,...,r − 1 }
for x ↦→cot(πrx) lies inside C1
r and the poles 0 and 1 lies outside C1
r , and C2
r
is a closed curve in Ω r such that the poles {(m + 1/2)/r | m = 0, 1,...,r − 1 }
for y ↦→tan(πry) lies inside C2
r . Both curves are oriented in the anti-clockwise
direction.
Using the function Sγ we can also express J ′
K(r) as a contour integral. By
Lemma 1 we get that
J ′
K (r) = r
r−1∑
m=0
Sγ(π − (2m + 1)γ)
Sγ(−π + (2m + 1)γ).
We have here used that
Sγ(−π +γ)
Sγ(π −γ) =
r−1∏
j=1
Sγ(π − (2j + 1)γ)
Sγ(−π + (2j + 1)γ) =
r−1∏
j=1
(
1 −e−2π√−1 j
r
)
=r.
If we put
gr(x) = Sγ(π − 2πx)
Sγ(−π + 2πx)
