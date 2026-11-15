---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-015-92-case-2-rrll
section_title: "Case 2: RR|LL"
section_number: 9.2
pages: 24-25
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Case 2: RR|LL
Ω
R
R
|
L
L
i
0
1
2
3
4
wi
u
A + λε
0 + ε
A
v
xi
ξ −A −λε
−u + 2A + 2λε −ε
(1 −λ)ε
ε + v
A + ξ′
yi
η + A + λε
u + ε
(1 + λ)ε
−ε + 2A −v
−A + η′
zi
π −2u
π −2A −2λε
π −2ε
π −2A
π −2v
First consider the value of A. Since there can be no vertical bars immediately before or
after RR|LL, the tetrahedra ∆0, ∆1, ∆3, ∆4 have positive angles, so the parameter A
Geometry & Topology 10 (2006)
Canonical triangulations
1263
(which does not contribute to the angles of any other tetrahedra) can vary freely in an
open interval when ε = 0. So A must be critical giving
1 = exp −∂V
∂A

ε=0 = sin y0 sin2 x1
sin x0 sin2 z1
|
{z
}
P/T
sin2 y3 sin x4
sin2 z3 sin y4
|
{z
}
P′/T′
.
Hence P/T = T′/P′. Therefore, with the right choice of λ,
exp −∂V
∂ε

ε=0
=
1 −λ2
4
U
z
}|
{
sin y1
sin x1
| {z }
Q/P
sin x3
sin y3
| {z }
Q′/P′





1 + λ
1 −λ
sin y0 sin2 x1
sin x0 sin2 z1
|
{z
}
P/T=T′/P′=:V





λ
=
Q/P · Q′/P′
(1 + T/P)(1 + T′/P′) =
Q
P + T
Q′
P′ + T′ < 1
by Lemma 8.2; see Figure 10 (right).
We conclude with two remarks. First, up to replacing the monodromy ϕ with ϕ2 (thus
doubling the period m of Ω), we can always assume Ωhas at least 6 letters: that
way, all columns of the tables above are neatly distinct, and to recover the original Vϕ
we just quotient out by the extra symmetry (which the volume maximizer (wi)i∈Z/mZ
must respect, by concavity of the volume functional V ). Compare with the remark that
closes Section 5. Second, the choice of λ ∈(−1, 1), which may seem “magical” at ﬁrst
glance, is essentially our only degree of freedom in Section 9.1–Section 9.2: the volume
is already assumed critical with respect to most parameters (including A, the common
value of w1 and w3); therefore, only deformations of w1, w2, w3 need to be considered,
and if we assume ∂w2
∂ε = 1, then only the value of the difference ∂w1
∂ε −∂w3
∂ε ∈(−1, 1)
matters.
Theorem 1.1 is proved.
