---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-024-83-the-maximum-of-the-growth-rate-of-the-r-matri
section_title: "The maximum of the growth rate of the R-matrix"
section_number: 8.3
pages: 21-22
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
of r±(α, β, κ).
Proposition 8.6. (a) With α, β, κ satisfying ( 33), r+(α, β, κ) achieves maximum when α = 3 /4, β = 1 /4,
and κ = 1/2. Moreover
r+(3/4, 1/4, 1/2) = v8
2π ,
where
v8 = 8Λ( π/4) ≈ 3.6638623767088760602 . . .
is the volume of the regular hyperbolic ideal octahedron.
(b) Similarly, r−(α, β, κ) reaches maximum when α = 1/4, β = 3/4, and k = 1/2; and its maximum value is
the same as that of r+(α, β, κ).
Thus, asymptotically, the winning conﬁguration is given by:
3n/4 n/4
n/2
3n/4 n/4
22 STA VROS GAROUF ALIDIS AND THANG TQ L ˆE
Proof. It is enough to consider the case of r+. The result for r− follows from ( 37). Let δ = α − κ, we have
r+(α, β, κ) = −Λ( π(β + κ)) + Λ( πβ) + Λ( πκ) − Λ( π(δ + κ)) + Λ( π(δ)),
with domain 0 ≤ β, δ, κ, and β + κ ≤ 1, δ + κ ≤ 1. Note the symmetry between β and δ.
Using Λ ′(x) = − log(2 sin x) for 0 < x < π , one can easily show that the function −Λ( π(β + κ)) + Λ( πβ),
for a ﬁxed κ ∈ [0, 1], achieves maximum at β = (1 − κ)/2. It follows that the maximum of r+(α, β, κ) is the
same as the maximum of
g(κ) := 2( −Λ( π(β + κ)) + Λ( πβ)) + Λ( πκ),
with β = (1 − κ)/2. The domain for g is κ ∈ [0, 1]. Using the derivative of g it is easy to show that g achieves
maximum when κ = 1/2. In this case α = 3/4, β = 1/4. □
Remark 8.7. Another proof is to use part (b) of Proposition 8.5 and the fact that the volume of an ideal
octahedron is maximized at a regular ideal octahedron; see [ Rat06].
Lemma 8.8. If z, w are complex numbers that satisfy |z| = |w| = 1 and |1 − z| = |1 − w|, then z = w±1.
Proof. Let us deﬁne
Cu0,r := {u ∈ C | | u − u0| = r > 0}.
Then Cu0,r is a circle with center u0 and radius r. Fixing w, it follows that z ∈ C0, 1 ∩ C1, |1−w|. The
intersection of two circles is two points, and since w and w−1 = ¯w both lie in the intersection, the result
follows. □
