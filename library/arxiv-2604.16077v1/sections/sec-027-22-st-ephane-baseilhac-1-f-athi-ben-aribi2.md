---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-027-22-st-ephane-baseilhac-1-f-athi-ben-aribi2
section_title: "ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2"
section_number: 22
pages: 22-23
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
Lemma 3.1. For all y ∈ R +i(−π,π ) we have 1
2πi Li2(−ey) = 1
4
∫
R+i0
e−i yv
π dv
v2 sinh(v).
Proof. The integral above is a holomorphic function of y. Taking the derivative twice we get
∂2
y
(∫
R+i0
e−i yv
π dv
v2 sinh(v)
)
= − 1
π2
∫
R+i0
e−i yv
π dv
sinh(v) = − 1
π2(1 +ey)
(∫
R+i0
−
∫
R+i0+πi
) e−i yv
π dv
sinh(v)
where, using a simple change of variable, we note that
∫
R+i0+πi
e−i yv
π dv
sinh(v) = −ey
∫
R+i0
e−i yv
π dv
sinh(v) .
Now, let R > 0 and consider the contour Γ R formed by the concatenation of the oriented
segments [ −R,R ] +i0, R +iπ[0, 1], −([−R,R ] +i0) +iπ and −R −iπ[0, 1]. We have
lim
R→+∞
∫
±R+iπ[0,1]
e−i yv
π dv
sinh(v) = lim
R→+∞
∫ 1
0
e−i y
π (±R+πit)
sinh(±R +πit) dt = 0
and therefore
(∫
R+i0
−
∫
R+i0+πi
) e−i yv
π dv
sinh(v) = lim
R→+∞
(∫
ΓR
−
∫
R+iπ[0,1]
−
∫
−R−iπ[0,1]
) e−i yv
π dv
sinh(v)
= lim
R→+∞
∫
ΓR
e−i yv
π dv
sinh(v) .
This integral is constant in R, and equal to 2 πi.Res
(
e−i yv
π
sinh(v),v =iπ
)
= −2πiey by the residue
theorem. We deduce
∂2
y
(∫
R+i0
e−i yv
π dv
v2 sinh(v)
)
= 2iey
π(1 +ey).
Finally, we can integrate twice along a path running from −∞ along the real axis up to R(y),
and then along a straight segment up to y ∈ R +i(−π,π ), since the integrands are continuous
in this strip:
∂y
(∫
R+i0
e−i yv
π dv
v2 sinh(v)
)
= 2i
π
∫ y
−∞
es
1 +esds = 2i
π Log(1 +ey)
∫
R+i0
e−i yv
π dv
v2 sinh(v) = 2i
π
∫ y
−∞
Log(1 +es)ds = − 2i
π Li2(−ey).
The result follows. ✷
3.2. Asymptotics of ˆSN (z) and gN (z). Let us start with a straightforward lemma.
Lemma 3.2. For all δ ∈]0,π [, for all z ∈] − ∞,M ] +i([δ, 2π −δ] + 2πk), k ∈ Z, we have:
⏐
⏐
⏐
⏐
ez
1 −ez
⏐
⏐
⏐
⏐ ≤ eM/2
δ
√
1 − π2
24
.
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 23
Proof. It is enough to do the case k = 0. For δ ∈]0,π [ and z =x +iy ∈] − ∞,M ] +i[δ, 2π −δ],
we have
⏐
⏐
⏐
⏐
ez
1 −ez
⏐
⏐
⏐
⏐
2
= e2x
|1 −ez|2 = e2x
1 +e2x − 2ex cos(y) = ex
2 cosh(x) − 2 cos(y)
≤ eM
2 cosh(x) − 2 cos(y).
Fory ∈ [δ, 2π −δ] ﬁxed, 1
2 cosh(x) − 2 cos(y) is maximal at x = 0, where it is equal to
1
2 − 2 cos(y) = 1
2 − 2 + 4 sin(y/2)2 = 1
4 sin(y/2)2.
Moreover, for y ∈ [δ, 2π −δ] we have sin( y/2) ≥ sin(δ/2), and since 0 < δ/2 < π/2, a
Taylor-Lagrange expansion with remainder at order 4 gives s in(δ/2) ≥ δ/2 − 1
