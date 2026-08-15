---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-062-451-case-b-integral-in-let-us-study-the-asymptot
section_title: "Case (b), integral In,+. Let us study the asymptotics of In,+ ="
section_number: 4.5.1
pages: 41-45
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
∫
i[s−
N,2π−s+
N ]
e
N
2iπf+(z)dz.
42 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
From the formula f+(z) = L+(z; −2πi, 2πi) = Li 2(ez) +z2 we compute
ℑ(f+(z)) = ℑ(Li2(ez)) + 2ℜ(z)ℑ(z),
(f+)′(z) = 2z − Log(1 −ez),
(f+)′′(z) = 2 + ez
1 −ez = 1 + 1
1 −ez,
f+(x +it) = Li 2(ex+it) + (x +it)2,
∂
∂x ℑ(f+(x +it)) = ℑ
( ∂
∂xf+(x +it)
)
= 2t − ℑ
(
Log(1 −ex+it)
)
= 2t − arg
(
1 −ex+it)
,
∂
∂t ℑ(f+(x +it)) = ℑ
(∂
∂tf+(x +it)
)
= 2x − ℜ
(
Log(1 −ex+it)
)
= 2x − Log|1 −ex+it|.
One can easily compute that ( f+)′(z0) = 0 if and only if
z0 =a := Log((−1 +
√
5)/2) ≈ −0.48.
We will deform the contour i[s−
N, 2π −s+
N ] (in blue in Figure 4) to a new contour C ′ (in
dotted blue in Figure 4) on which ℑ(f+) is negative everywhere but in the point a where
ℑ(f+)(a) = 0 and on the small subcontour [0 ,isN ] where it is nonnegative. Let us prove this
is possible.
We construct C ′ in six parts:
• C ′
1 is vertical, going from is−
N to 0.
• C ′
2 is vertical, going from 0 to −iη.
• C ′
3 is almost horizontal, going from −iη to a.
• C ′
4 is vertical, going from a to a + 2iπ −iη′.
• C ′
5 is horizontal, going from a + 2iπ −iη′ to 2iπ −iη′.
• C ′
6 is vertical, going from 2 iπ −iη′ to 2iπ −is+
N .
ℑf+> 0
ℑf+< 0ℑf+> 0
ℑf+< 0
Cut
Cut
a
a + 2iπ −iη′
0
is−
N
iπ
2iπ −is+
N
2iπ −iη′
2iπ
−iη
Figure 4. The deformed contour (in dashed blue) through zones where
ℑf+< 0 and the point a (in red) where ℑf+ = 0.
First, ℑ(f+) is zero on the half-line ( −∞, 0] since Li 2 takes real values on [0 , 1]. Moreover,
ℑ(f+)(z) vanishes at z = 2iπ (and also at z =iπ but we will not use this). The set of points
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 43
where ℑ(f+) vanishes is drawn in red in Figure 4; the red dotted line’s ge neral form was
computed via Mathematica, but we will not use its exact position in our arguments.
Deﬁning C ′
1, and asymptotics: We deﬁne C ′
1 := [0,is −
N ] oriented downwards. Recall that for
all t ∈ R and z := it we have ℑ(Li2(ez)) = Cl 2(t), thus ℑ(f+(it)) = Cl 2(t). From Section
4.3.2 we have:
∫
C′
1
e
N
2iπf+(z)dz =
∫ s−
N
0
e
N
2π ℑ(f+(it))dt =
∫ s−
N
0
e
N
2π Cl2(t)dt =ON →∞
( 1
N 1− α
2
)
=oN →∞
( 1√
N
)
.
Deﬁning C ′
2, and asymptotics: We deﬁne C ′
2 := [ −iη, 0] oriented downwards. From Section
4.3.1, since [ −η, 0] ⊂ [−π, 0] we have:
⏐
⏐
⏐
⏐
⏐
∫
C′
2
e
N
2iπf+(z)dz
⏐
⏐
⏐
⏐
⏐ ⩽
∫ 0
−η
e
N
2π ℑ(f+(it))dt =
∫ 0
−η
e
N
2π Cl2(t)dt =oN →∞
( 1√
N
)
.
Deﬁning C ′
3: The critical point z = a of f+ is simple, since ( f+)′′(z) only vanishes at z =
Log(2). Thus, by standard complex analysis, there is a disk n eighbourhood Da of a (drawn
as a grey disk) split into four zones by two transverse level l ines where ℑ(f+) = 0, and ℑ(f+)
is alternatively positive and negative in these four zones b y circling around a. We already
know that one level line is the horizontal line (drawn in full red), thus the other level line
(part of the dotted red curve) crosses transversely this hor izontal line.
Now, for any point x ∈ (a, 0] we have
∂
∂t ℑ(f+(x +it))|t=0 = 2x − Log|1 −ex| = 2x − Log(1 −ex)> 0,
by deﬁnition of a and the fact that 2 x − Log|1 −ex|> 0 ⇔ (ex)2 + (ex) − 1> 0. Hence, ℑ(f+)
is increasing on every small enough vertical line (oriented upwards) above every x ∈ (a, 0].
This conﬁrms that a negative zone for ℑ(f+) is below the red horizontal line and a positive
zone is above it.
We can now deﬁne the part C ′
3 of the new contour C ′ (in Figure 4 this is the part which is
between −iη and a, oriented from right to left, where the value of η >0 will be decided in
what follows). For any x ∈ (a, 0], deﬁne a small enough disk Dx aroundx so that the real line
cutsDx into two half-disks, where ℑ(f+) is negative on the bottom half-disk and positive on
the upper half-disk. Such a small disk exists since ∂
∂t ℑ(f+(x +it))|t=0 > 0.
The union Da ∪⋃
a<x⩽ 0Dx covers the compact set [ a, 0], so there is a ﬁnite family of points
x0 = a < x1 < x2 < ... < xp = 0 such that Da ∪⋃
1⩽i⩽pDxi covers [a, 0]. Take η > 0
small enough to be smaller than the radius of Dxp = D0. We can now deﬁne the part C ′
3
as a smooth curve going from −iη to a while remaining in all bottom half-disks; it can even
be chosen outside of Da as an horizontal line of imaginary part −η (thus higher than the
opposite of half the minimum of all radii of Dxi), and smoothed out afterwards.
Deﬁning C ′
4: We deﬁneC ′
4 := [a,a +2iπ −iη′], oriented upwards. Let us prove that ℑ(f+)< 0
on the vertical line ( a,a + 2iπ]. To do this we look for all t ∈ (0, 2π) at the real derivative
∂
∂t ℑ(f+(a +it)) = 2a − Log|1 −ea+it| = Log(1 −ea) − Log|1 −ea+it|.
We remark that this quantity is negative for all t ∈ (0, 2π), by a simple geometric argument:
1 −ea is the distance between 1 and ea ∈ (0, 1), which is smaller than the distance |1 −ea+it|
between 1 and any other point ea+it of the circle of center 0 and radius ea (since 1 lives
outside of the closed disk ¯D(0,ea)). Hence, ℑ(f+) decreases on [a,a + 2iπ] oriented upwards,
and thus ℑ(f+)< 0 on the vertical line ( a,a + 2iπ].
44 ST ´EPHANE BASEILHAC 1, F ATHI BEN ARIBI2
Asymptotics on C ′
3 ∪C ′
4: From what precedes, we have all the tools to apply the saddle p oint
method (see Section 4.2) on the contour λ =C ′
3 ∪C ′
4 for g(z) = 1,f (z) = f+(z) and z0 =a.
Since N = 2πn, we obtain:
∫
C′
3∪C′
4
e
N
2iπf+(z)dz = 2π√
N
eiθ · 1 · 1√
|f ′′
+(a)|e
N
2iπf+(a) (1 +oN →∞(1)).
For the curious reader, we remark that ([63])
Li2(ea) = Li 2
(√
5 − 1
2
)
= π2
10 − Log2
(√
5 + 1
2
)
,
and thus f+(a) = Li 2(ea) +a2 has the unexpectedly simple expression f+(a) = π2
10 . For our
purposes, we only need to know that this is a real number, i.e. ℑ(f+(a)) = 0 which we knew
already.
Moreover, (f+)′′(a) = 1 + 1
1 −ea = 5 +
√
5
2 . Hence we have
∫
C′
3∪C′
4
e
N
2iπf+(z)dz = Constant+√
N
(eir+N +oN →∞(1)),
where Constant + ∈ C∗ has modulus 2π
(
5 +
√
5
2
) − 1
2
= 3.303... and r+ = −π
20 ∈ R.
Deﬁning C ′
5, and asymptotics: We deﬁne C ′
5 := [a + 2iπ −iη′, 2iπ −iη′] oriented from left to
right. Since ∂xℑ(f+(x +it)) = 2t − arg
(
1 −ex+it)
for all x +it in the domain of deﬁnition
of f+, and since arg lies in ( −π,π ], we deduce that for any ﬁxed t > π/2 the function
(x ↦→ ℑ(f+(x +it))) is strictly increasing on the horizontal line of altitud e t oriented from
left to right.
In particular for t = 2π −η′, ℑ(f+) is maximal on C ′
5 at its right endpoint 2 iπ −iη′ where it
takes the value Cl 2(2π −η′)< 0. Hence
⏐
⏐
⏐
⏐
⏐
∫
C′
5
e
N
2iπf+(z)dz
⏐
⏐
⏐
⏐
⏐ ⩽ |a|e
N
2π Cl2(2π−η′) =oN →∞
( 1√
N
)
.
Deﬁning C ′
6, and asymptotics: We deﬁne C ′
6 := i[2π −η′, 2π −s+
N ] oriented upwards. From
Section 4.3, since [2 π −η′, 2π −s+
N ] ⊂ [π, 2π] we have:
⏐
⏐
⏐
⏐
⏐
∫
C′
6
e
N
2iπf+(z)dz
⏐
⏐
⏐
⏐
⏐ ⩽
∫ 2π−s+
N
2π−η′
e
N
2π ℑ(f+(it))dt =
∫ 2π−s+
N
2π−η′
e
N
2π Cl2(t)dt =oN →∞
( 1√
N
)
.
This concludes the construction of the new contour C ′, and by summing the integrals on each
part, we obtain
In,+ =
∫
C′
e
N
2iπf+(z)dz = Constant+√
N
(eir+N +oN →∞(1)),
where
(117) |Constant+| = 2π
(
5 +
√
5
2
) − 1
2
= 3.303..., r+ = −π
20 ∈ R.
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 45
