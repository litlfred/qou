---
doc_id: arxiv-2203.17029v1
doc_title: "MODULAR q-HOLONOMIC MODULES"
section_id: sec-027-58-an-analytic-lift-of-the-colored-jones-polynom
section_title: "An analytic lift of the colored Jones polynomial"
section_number: 5.8
pages: 62-62
source_pdf: 2203.17029v1.pdf
source_sha256: 5557f7f272cb8a43
doc_brief: "MODULAR q-HOLONOMIC MODULES — We introduce the notion of modular q-holonomic modules whose fundamental matrices deﬁne a cocycle with improved analyticity properties and show that the generalised"
duplicate_of: "modularqholonomicmodules"
---
a proof of Theorem
1.10. The main observation is that when x = qN , the series ˆf (0)(t, qN , q)
terminates to a polynomial of t, in which case the q-Borel transfrom, followed by a q-Laplace
transfrom is the identity. Explicitly, when x = qN for N ∈ /CI
≥1 we have
ˆf (0)(t, qN , q) =
∞∑
k=0
(−1)kq−k(k+1)/2(q1+N ; q)k(q1−N ; q)ktk
=
N −1∑
k=0
(−1)kq−k(k+1)/2(qN +1; q)k(q1−N ; q)ktk .
(330)
The theorem then follows from Equation ( 58). □
5.9. Specialisation t = qm. In this short subsection, included for completeness, we brieﬂy
comment how our analytic functions of t, specialised to t = qm, become the known sequences
of q-series and ( x, q)-series that have appeared in the literature. In [ 32] and [ 22, 23, 24] the
q-holonomic modules are discrete versions of what we have considere d in Section 5. Here
we describe how the solutions can be constructed from the ones pr esented here. Consider a
solution f (t, q) of a q-diﬀerence equation
ar(t, q)f (qrt, q) + ar−1(t, q)f (qr−1t, q) + · · · + a0(t, q)f (t, q) = 0
corresponding to an edge of slope κ on the Newton polygon, and let
fm(q) = ( −1)κmq−κm(m+1)/2Resz=0θ(qme(z), q)−κf (qme(z), q) dz
2πiz . (331)
Then we ﬁnd that fm(q) satisﬁes the linear q-diﬀerence equation
ar(qm, q)fr+m(q) + ar−1(qm, q)fr+m−1(q) + · · · + a0(qm, q)fm(q) = 0 .
This follows from
0 =Resz=0
(
ar(qme(z), q )f (qr+me(z), q ) + ar−1(qme(z), q )f (qr+m−1e(z), q ) + . . .
+a0(qme(z), q )f (qme(z), q )) e(κz )dz
θ(e(z); q)κ2πiz
=ar(qm, q )fr+m(q) + ar−1(qm, q )fr+m−1(q) + · · · + a0(qm, q )fm(q)
(332)
where the equality follows from holomorphicity of θ−κf or the higher order of vanishing of
the indicial polynomial.
For example, for the Equation ( 28), and its solution solution g(0,1) deﬁned in Equa-
tion ( 206), we obtain that
Resz=0g(0,1)(qme(z), q) dz
2πiz =
∞∑
k=0
(
k + 1
2 − m − 2E(k)
1 (q)
)
(−1)k qk(k+1)/2−km−m
(q; q)2
k
, (333)
a q-series that appears in [
23, Equ.13b] and [ 24, Equ.6].
