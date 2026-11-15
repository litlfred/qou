---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-015-the-spectral-curves
section_title: "The spectral curves"
section_number: null
pages: 24-26
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
reducible).
Our system can be described rather explicitly. The moduli space of degree 0,
rank n vector bundles on E can be identiﬁed with the symmetric product SnE:
each equivalence class contains a unique decomposable bundle V = ⊕n
i=1Li, with
Li = OE(qi −∞) ∈Pic0E. The moduli of SL(n)-bundles is the ﬁber over 0 of the
Abel-Jacobi map SnE →E. It is a projective space
{q1 + · · · + qn|
X
qi = n∞} = PH0(E, O(n∞)) ≈Pn−1.
In terms of the decomposition V = ⊕Li, any Higgs ﬁeld ϕ on V can be written as
a matrix with entries
ϕij ∈Γ(Lj ⊗L−1
i (∞)).
Let A := Res∞ϕ. Its diagonal elements are all zeroes, and A −m · Id has rank
≤1, so A is conjugate, via a diagonal matrix, to m times e = Σi̸=jeij. This means
that each (V, ϕ) in our system is equivalent to a pair (V, ϕ) with Res∞(ϕij) = m
for i̸ = j. For a given V , this condition uniquely determines the ϕij (as long as
Li̸ = Li). The remaining free parameters are the coordinates qi of V = ⊕O(qi −∞)
and the diagonal entries pi = ϕii. Away from the diagonals qi = qj, these (qi, pi)
can be identiﬁed with the canonical coordinates on T ∗M.
The spectral curves
The family of spectral curves Cb, for the fundamental, n-dimensional repre-
sentation of SL(n), can be described as a linear system on the compactiﬁcation
S = P(ωE(∞) ⊕OE) of the surface S, or on various birationally equivalent sur-
faces. More precisely, it forms an aﬃne open subspace of this linear system, the
complement consisting of curves which contain the section at inﬁnity, Z∞:= S −S,
with some multiplicity k > 0. By removing this multiple component, we recover
the spectral curves for the analogous problem with n replaced by n −k. (If A is an
endomorphism of a vector space V , and W is an invariant subspace, then
rankW (A −m · Id) ≤rankV (A −m · Id),
so the conjugacy class restricts correctly.)
SEIBERG-WITTEN INTEGRABLE SYSTEMS
25
We can write down an explicit equation
pn(t) = tn + Σn
k=2fktn−k = 0
for the spectral curves. Here t is a coordinate on the ﬁbers of ωE(∞), and fk ∈
Γ(OE(k∞)). (We identify OE ≈ωE). Once we have such a pn for each n, the
previous remark and the tracelessness condition imply that the general spectral
curve has equation
Cu : pn + Σn−2
ℓ=0 uℓpℓ= 0,
with arbitrary constants uℓwhich can therefore be interpreted as coordinates on
the quantum moduli-space, the base of the integrable system.
The condition on pn which speciﬁes the right conjugacy class at inﬁnity is that
when we substitute t = t′ + ξ−1, where ξ is a local coordinate on E at ∞, we get a
function of t′ and ξ with at most ﬁrst order poles in ξ. Write the equation of E in
Weierstrass form,
E : y2 = x3 + bx −c.
The local coordinate ξ determines a sequence xk, k = 2, 3, . . ., of rational functions
on E which are regular on E −∞and such that near ∞,
xk −ξ−k = O(ξ−1).
We may as well use the local coordinate ξ = x−1/2, and then the xk can be read
oﬀthe Taylor expansions:
y = ξ−3(1 + bξ4 −cξ6)1/2 = ξ−3(1 + b
2ξ4 −c
2ξ6 −b2
8 ξ8 + bc
4 ξ10 −2c2 −b3
16
ξ12 + . . . )
and
y−1 = ξ3(1+bξ4−cξ6)−1/2 = ξ3(1−b
2ξ4+ c
2ξ6+ 3b2
8 ξ8−3bc
4 ξ10+ 6c2 −5b3
16
ξ12+. . .).
Explicitly, we get:
x2 = x
x3 = y
x4 = x2
x5 = xy
x6 = x3
x7 = x2y −b
2y
x8 = x4
x9 = x3y −b
2xy + c
2y
x10 = x5
x11 = x4y −b
2x2y + c
2xy + 3b2
8 y
x12 = x6,
26
RON Y. DONAGI
and so on. In terms of this basis, one checks by an easy induction argument that
pn = tn −Σn
k=2(−1)k(k −1)

n
k

xktn−k,
so the ﬁrst few polynomials are:
1
t
t2 −x
t3 −3xt + 2y
t4 −6xt2 + 8yt −3x2
t5 −10xt3 + 20yt2 −15x2t + 4xy
t6 −15xt4 + 40yt3 −45x2t2 + 24xyt −5x3
t7 −21xt5 + 70yt4 −105x2t3 + 84xyt2 −35x3t + 6(x2y −b
2y).
This is a bit cleaner than the formulas in [DW], mostly because we set the sum of
the roots in the Weierstrass equation of E to 0. A more-or-less equivalent solution
was given already in [T], where the generating function for the pn was written in
terms of theta functions and exponentials on E. A slightly diﬀerent (but equivalent)
set of polynomials was given in [IM1].
