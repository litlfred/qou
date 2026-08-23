---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-060-3-on-which-ℑfir-has-a-minimum-not-a-maximum-but
section_title: "(on which ℑf+|iR has a minimum, not a maximum), but we will not use"
section_number: 3
pages: 40-41
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INVARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI) of"
---
this.
We deform the contour i[s−
N, 2π −s+
N ]. Let x be a large negative real number, and deﬁne
C ∞ as the path from is−
N to 2iπ −is+
N formed by the concatenation of the open oriented
intervalsCs−
N
:= i(s−
N, 0), C ∞
0 := (0,x ) ⊂ R−, C ∞
x := x +i(0, 2π), C ∞
2π := (x, 0) +i2π, and
C ′
s+
N
:= (2iπ, 2iπ −is+
N ) (see Figure 3). Since C ∞ andi[s−
N, 2π −s+
N ] are homotopic relatively
to their endpoints we have
(113) In,+ =
∫
C∞
e
N
2πi L+(z;−2πi,πi)dz.
·x
·
x + 2iπ
·0
·is−
N
· 2iπ −is+
N
·2iπ
C ∞
0
ℑ(f+)< 0
C ∞
2π
ℑ(f+)< 0
C ∞
x
ℑ(f+)< 0
C ′
s+
N
Cs−
N
Figure 3. The deformed contour C ∞ =Cs−
N
∪C ∞
0 ∪C ∞
x ∪C ∞
2π ∪C ′
s+
N
(blue
parts are where ℑ(f+) < 0 and the red part is where ℑ(f+) is positive but
very small)
From the formula f+(z) = L+(z; −2πi,πi ) = Li 2(ez) +z2 +πiz we compute
ℑ(f+(z)) = ℑ(Li2(ez)) + 2ℜ(z)ℑ(z) +πℜ(z).
VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS 41
Forz ∈C ∞
0 ⊂ R− we thus have ℑ(f+(z)) = ℑ(Li2(ez)) +πℜ(z) = πℜ(z)< 0 since ℜ(z)< 0
and the dilogarithm of a real number < 1 is real.
Forz ∈C ∞
2π ⊂ R− +i2π we have ℑ(f+(z)) = ℑ(Li2(ez)) + 5πℜ(z) = 5πℜ(z)< 0 since again
ℜ(z)< 0 and the dilogarithm of ez ∈ exp(] − ∞; 0[+2iπ) ⊂ R\]1; +∞[ is real.
Forz =x +it ∈C ∞
x we have ℑ(f+(x +it)) = ℑ(Li2(ex+it)) + 2xt +πx. Moreover Li2(y) ∼y
as y → 0 in C, and therefore there exists x0 < 0 such that for every t ∈ [0, 2π] and x ≤ x0
we have |Li2(ex+it)|< 1
2 . Hence, taking for instance x ⩽ x0 − 1, for every t ∈ [0, 2π] we have
ℑ(f+(x +it)) = ℑ(Li2(ex+it)) + 2xt +πx ⩽ 1
2 +π(−1)< 0.
We conclude that for |x| large enough, ℑ(f+)< 0 on the contour C ∞
x .
Now we remark that, having ﬁxed for example x =x0 − 1< 0, and denoting by γ : [0, 1] → C
a parametrization of the path C ∞
0 ∪C ∞
x ∪C ∞
2π, we have
⏐
⏐
⏐
⏐
∫
C∞
e
N
2πif+(z)dz
⏐
⏐
⏐
⏐ ⩽
∫ 1
0
|e
N
2πif+(γ(t))γ′(t)|dt
⩽
∫ 1
0
e
N
2π ℑf+(γ(t))|γ′(t)|dt
⩽
∫ 1
0
e
N
2π 0|γ′(t)|dt = 2|x| + 2π =ON →∞(1).
Finally, the remaining two integrals on the small vertical c ontoursCs−
N
,C ′
s+
N
are alsoON →∞(1)
from the conclusions of Section 4.3. Hence In,+ =ON →∞(1).
