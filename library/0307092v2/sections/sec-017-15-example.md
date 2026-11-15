---
doc_id: 0307092v2
doc_title: "Extended Bloch group and the Cheeger–Chern–Simons class"
section_id: sec-017-15-example
section_title: "Example"
section_number: 15
pages: 58-60
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
toc_source: outline
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class — We deﬁne an extended Bloch group and show it is naturally isomorphic to H3(PSL(2, C)δ; Z)."
---
Example
We return to the ﬁgure 8 knot complement m004 of Example 14.4 to illustrate
the above formulae. Denote the cross-ratio parameters of the two simplices in
Figure 8 by z and y, and choose ﬂattenings [z; p, q] and [y, r, s]. The consis-
tency condition about each edge can be read oﬀfrom the ﬁgure. The condition
for the edge labeled with a single arrow is:
2 log z + log z′ −log y′ −2 log y′′ = 2πi
(18)
and the condition for the other edge turns out to be equivalent to this. The
log-parameters for the ﬂattenings are
(log z + pπi, log z′ + qπi, log z′′ + (−1 −p −q)πi),
(log y + rπi, log y′ + sπi, log y′′ + (1 −r −s)πi) .
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
471
z
z
z´
z´´
z´
z´´
z´
z
z´
z´´
z´´
z
z´
z´
z´
z
z
z´
z´
z
y
y
m
(y´)
y
y
(y´)
(y´)
y
(y´´)
(y´´)
(y´)
−1
−1
−1
−1
−1
−1
−1
−1
−1
−1
−1
−1
−1
−1
−1
l
z
z
z´´
z´´
(y´´)
(y´´)
(y´´)
(y´´)
Figure 9: Fundamental domain of the cusp torus, triangulated as the link of the 0–
simplex of the ideal triangulation of m004.
Thus the ﬂattening condition about the edge is
2p + q −s −2(1 −r −s) = −2 .
(19)
The log holonomy for a meridian and longitude can be read oﬀfrom the fun-
damental domain of the cusp torus illustrated in Figure 9 (taken from [16]
but modiﬁed since orientation conventions diﬀer; in particular, w, w′, w′′ there
are our (y′′)−1, (y′)−1, y−1 because of diﬀerent vertex-ordering for the second
simplex). They are:
u := log z′′ + log y′′
v := 2 log z −2 log z′′ .
(20)
Their vanishing thus gives ﬂattening conditions
(1 −r −s) + (−1 −p −q) = 0
2p −2(−1 −p −q) = 0
which simplify to
−p −q −r −s = 0
(21)
2 + 4p + 2q = 0 .
(22)
Solving equations (19), (21), (22) gives
q = −1 −2p,
(r, s) = −(p, q).
(23)
Simultaneously solving the consistency condition (18) and the cusp conditions
u = v = 0 (see (20)) gives z = ω, y = ω−1. Thus, as promised earlier, we see
Geometry & Topology, Volume 8 (2004)
472
Walter D Neumann
that ˆβ(m005) = [ω; p, q] −[ω−1; −p, −q] with q = −1 −2p. Choosing p = 0,
we get:
ˆβ(m005) = [ω; 0, −1] −[ω−1; 0, 1].
Now suppose we deform our parameters to perform hyperbolic (α, β) Dehn
ﬁlling on this manifold. Let z, y now denote the deformed values of the simplex
cross-ratios (they simultaneously satisfy the consistency condition (18) and the
Dehn ﬁlling condition αu + βv = 2πi). Choose γ, δ ∈Z so

α
β
γ
δ

 = 1.
As described in [16], the complex length of the added geodesic is λ := −(γu +
δv), so Theorem 14.5 gives the formulae
ˆβ(m004(α, β)) = −χ(e−γu−δv) + [z; 0, −1] −[y; 0, 1]
(vol +i cs)(m004(α, β)) = π
2 (γu + δv) −i(R(z; 0, −1) −R(y; 0, 1)) ,
(24)
with u, v given by (20).
On the other hand, if we use Theorem 14.7, the Dehn ﬁlling condition αu+βv =
2πi gives the ﬂattening condition
α(−p −q −r −s) + β(2 + 4p + 2q) = −2
while the parity condition says p + q + r + s must be even. A simultaneous
solution of these and equation (19) is:
q = γ −1 −2p,
r = −2δ −p,
s = −γ + 4δ + 1 + 2p .
Choosing, eg, p = 0, we get
ˆβ(m004(α, β)) = [z; 0, γ −1] −[y; −2δ, −γ + 4δ + 1] ,
(vol +i cs)(m004(α, β)) = −i(R(z; 0, γ −1) −R(y; −2δ, −γ + 4δ + 1)) .
(25)
It is not hard to verify directly the equivalence of (24) and (25).
