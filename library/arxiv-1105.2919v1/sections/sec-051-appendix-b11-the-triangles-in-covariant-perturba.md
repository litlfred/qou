---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-051-appendix-b11-the-triangles-in-covariant-perturba
section_title: "Appendix B.1.1 The triangles in covariant perturbation theory"
section_number: null
pages: 63-66
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The triangle diagrams are shown in Fig. B.1. The contributions from diagram (a) and (b) will be denoted
by Va and Vb, respectively. According to relativistic Feynman rules, one obtains
Va
=
i g2
A
16f 4π
Z
d4l
(2π)4 (2lµ + qµ)ϵabcτ c
1 ¯u1(⃗p ′)γµu1(⃗p)
i
(l + q)2 −m2π + iϵ ×
×
i
l2 −m2π + iϵ ¯u2(−⃗p ′)(−lν)τ b
2γνγ5
i(k/N + MN)
k2
N −M 2
N + iϵ(lρ + qρ)τ a
2 γργ5u2(−⃗p) ,
(B.1)
Vb
=
i g2
A
16f 4π
Z
d4l
(2π)4 (2lµ + qµ)ϵabcτ c
2 ¯u2(−⃗p ′)γµu2(−⃗p)
i
(l + q)2 −m2π + iϵ ×
×
i
l2 −m2π + iϵ ¯u1(⃗p ′)(−lν −qν)τ b
1γνγ5
i(¯k/N + MN)
¯k2
N −M 2
N + iϵ(lρ)τ a
1 γργ5u1(⃗p) ,
(B.2)
where the momenta are deﬁned in Fig. B.1 and q = (0,⃗p ′ −⃗p). The sum over the isospin operators is
ϵabcτ c
i τ b
j τ a
j = −i 2τ i ·τ j and, for the intermediate nucleon, we have γνγ5(k/N +MN)γργ5 = γν(k/N −MN)γρ.
63
(a)
(b)
kN =

Ep −l0 , −⃗p ′ −⃗l

¯kN =

Ep −l0 ,⃗p −⃗l

l
l + q
b
a
kN
µ
ν
ρ
(Ep ,⃗p)
(Ep , −⃗p)
(Ep ,⃗p ′)
(Ep , −⃗p ′)
l + q
b
a
l
¯kN
µ
ν
ρ
(Ep ,⃗p)
(Ep , −⃗p)
(Ep ,⃗p ′)
(Ep , −⃗p ′)
Figure B.1: Two-pion exchange triangle diagrams at NLO.
Thus,
Va
=
−i τ 1 · τ 2
g2
A
8f 4π
Z
d4l
(2π)4 (2lµ + qµ)¯u1(⃗p ′)γµu1(⃗p)
1
(l + q)2 −m2π + iϵ ×
×
1
l2 −m2π + iϵ ¯u2(−⃗p ′)(−lν)γν
(k/N −MN)
k2
N −M 2
N + iϵ(lρ + qρ)γρu2(−⃗p) ,
(B.3)
Vb
=
−i τ 1 · τ 2
g2
A
8f 4π
Z
d4l
(2π)4 (2lµ + qµ)¯u2(−⃗p ′)γµu2(−⃗p)
1
(l + q)2 −m2π + iϵ ×
×
1
l2 −m2π + iϵ ¯u1(⃗p ′)(−lν −qν)γν
(¯k/N −MN)
¯k2
N −M 2
N + iϵ(lρ)γρu1(⃗p) .
(B.4)
At NLO, only the lowest order in the 1/MN expansion is included. The nucleon mass dependence comes
from the Dirac spinors and the nucleon propagator and performing such an expansion, we ﬁnd at lowest
order
¯uiγµui
≈
δµ0
(B.5)
¯uiγν(k/N −MN)γρui
≈
δνjδρm2MN(δjm + iϵjmnσn
i )
(B.6)
1
k2
N −M 2
N + iϵ
≈
1
2MN
1
−l0 + iϵ
(B.7)
In this approximation, the amplitudes are
Va
=
−i τ 1 · τ 2
g2
A
4f 4π
Z
d4l
(2π)4
1
(l + q)2 −m2π + iϵ
1
l2 −m2π + iϵ ×
× (δjm + iϵjmnσn
2 )(lj)(lm + qm)
(B.8)
Vb
=
−i τ 1 · τ 2
g2
A
4f 4π
Z
d4l
(2π)4
1
(l + q)2 −m2π + iϵ
1
l2 −m2π + iϵ ×
× (δjm + iϵjmnσn
1 )(lj + qj)(lm)
(B.9)
where we used q0 = 0.
64
Alternatively, one can derive the NLO triangle diagram contributions by using the HB formalism from
the outset. Using the Feynman rules for the HB Lagrangians and propagators yields
V HB
a
=
i g2
A
16f 4π
Z
d4l
(2π)4 (2l0)ϵabcτ c
1
i
(l + q)2 −m2π + iϵ
i
l2 −m2π + iϵ ×
× τ b
2(⃗σ2 ·⃗l)
i
−l0 + iϵτ a
2 (−⃗σ2 · (⃗l +⃗q)) ,
(B.10)
V HB
b
=
i g2
A
16f 4π
Z
d4l
(2π)4 (2l0)ϵabcτ c
2
i
(l + q)2 −m2π + iϵ
i
l2 −m2π + iϵ ×
× τ b
1(⃗σ1 · (⃗l +⃗q))
i
−l0 + iϵτ a
1 (−⃗σ1 ·⃗l) .
(B.11)
Performing the isospin sums and using the identity (⃗σ ·⃗a)(⃗σ ·⃗b) =⃗a ·⃗b + i⃗σ · (⃗a ×⃗b), we obtain
V HB
a
=
−i τ 1 · τ 2
g2
A
4f 4π
Z
d4l
(2π)4
1
(l + q)2 −m2π + iϵ
1
l2 −m2π + iϵ ×
×
h⃗
l · (⃗l +⃗q) + i⃗σ2 · (⃗l × (⃗l +⃗q))
i
,
(B.12)
V HB
b
=
−i τ 1 · τ 2
g2
A
4f 4π
Z
d4l
(2π)4
1
(l + q)2 −m2π + iϵ
1
l2 −m2π + iϵ ×
×
h
(⃗l +⃗q) ·⃗l + i⃗σ1 · ((⃗l +⃗q) ×⃗l)
i
.
(B.13)
The two sets of Eqs. (B.8), (B.9) and (B.12), (B.13) obviously agree—as they should.
Since (⃗l +⃗q) ×⃗l =⃗q ×⃗l and since the integral over a term proportional to⃗l will yield a result ∝⃗q, the
spin dependent terms vanish and the sum of both triangles is given by
V = Va + Vb
=
−i τ 1 · τ 2
g2
A
2f 4π
Z
d4l
(2π)4
1
(l + q)2 −m2π + iϵ⃗
l2 +⃗l ·⃗q
l2 −m2π + iϵ .
(B.14)
At this point, it might be of interest to compare with what other authors obtain for the NLO triangle
diagrams. In the work of Ref. [54], time-ordered perturbation theory (TOPT) (also known as old-fashioned
PT) is used in which loop integrals extend only over the three space-dimensions.
Thus, we will perform the integration over the time component in Eq. (B.14) to make a comparison with
TOPT possible. For convenience, we ﬁrst apply the transformation l = 1
2(l′ −q), which yields
V
=
−i τ 1 · τ 2
g2
A
8f 4π
Z
d4l′
(2π)4
1
(l′ + q)2 −4m2π + iϵ⃗
l′2 −⃗q2
(l′ −q)2 −4m2π + iϵ .
(B.15)
The poles in the lower half plane are at l′0 = ω± −iϵ with
ω±
=
q
(⃗l′ ±⃗q)2 + 4m2π
(B.16)
and, so, we can write the amplitude as
V
=
−i τ 1 · τ 2
g2
A
8f 4π
Z
d4l′
(2π)4
1
(l′0)2 −ω2
+ + iϵ⃗
l′2 −⃗q2
(l′0)2 −ω2
−+ iϵ .
(B.17)
Now we perform the integration over l′0 using the residue theorem
V
=
−τ 1 · τ 2
g2
A
8f 4π
Z
d3l′
(2π)3 (⃗l′2 −⃗q2)
 1
2ω+
1
ω2
+ −ω2
−
+
1
ω2
−−ω2
+
1
2ω−

=
−τ 1 · τ 2
g2
A
8f 4π
Z
d3l′
(2π)3 (⃗l′2 −⃗q2)

1
ω2
+ −ω2
−
ω−−ω+
2ω+ω−

=
τ 1 · τ 2
g2
A
16f 4π
Z
d3l′
(2π)3⃗
l′2 −⃗q2
ω+ω−(ω+ + ω−) .
(B.18)
65
Except for a typo in Ref. [54] and diﬀerences in notation, this agrees with the second term of Eq. (20) of
Ref. [54] as well as the ﬁrst term of Eq. (4.30) of Ref. [64], which both represent the triangle diagrams.
