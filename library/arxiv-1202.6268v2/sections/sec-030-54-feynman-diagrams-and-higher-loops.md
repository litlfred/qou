---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-030-54-feynman-diagrams-and-higher-loops
section_title: "Feynman diagrams and higher loops"
section_number: 5.4
pages: 33-35
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
obtained by continuing the saddle-point (stationary phase) expan sion of the state integral
to higher order. The calculation can be systematically organized into a set of Feynman
rules ( cf. [HKK+03, Ch.9], [ BIZ80, Pol05]). The resulting formulas — summarized in the
Introduction — are explicit algebraic functions of the exponentiate d shape parameters zi,
and belong to the invariant trace ﬁeld EM .
34 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
To proceed, we should ﬁrst re-center the integration around a cr itical point. Thus, we
replace Z → Z +ζ and integrate over ζ, assuming Z to be a solution to ( 5.8). Using
[DGLZ09, Eqn.3.26], we expand as follows:
ZT (ℏ) =
√
8π3
ℏ3 det B
∫ dNζ
(2πℏ)N/ 2
N∏
i=1
ψℏ(Zi +ζi)
×e
1
ℏ
[ 1
2
(
iπ + ℏ
2
) 2
f ·B−1ν−
(
iπ + ℏ
2
)
(Z+ζ)·B−1ν+ 1
2 (Z+ζ)·B−1A(Z+ζ)
]
∼
√
8π3
ℏ3 det BeΓ (0)(Z)
∫ dNζ
(2πℏ)N/ 2 exp
[
− 1
2ℏζ·H (Z)·ζ +
∞∑
k=1
N∑
i=1
Γ (k)
i (Z)
k! ζ k
i
]
.(5.17)
In this form, the ﬁrst coeﬃcient Γ (0)(Z) can be identiﬁed with an overall vacuum energy ,
while the rest of the Γ (k)
i (Z) are vertex factors .
Every Γ (k)(Z) here is a series in ℏ, in general starting with a 1 /ℏ term. However, Γ (1)
i must
vanish at leading order ℏ−1 precisely becauseZ is a solution to the leading-order critical point
equations; and we have also already extracted the leading ℏ−1 piece of Γ (2)
i as the Gaussian
integration measure− 1
2ℏζHζ. Typically, 1-vertices and 2-vertices are absent from a Feynman
calculus. Here, however, they appear because our critical point e quation and the Hessian
(respectively) are only accurate at leading order, and incur ℏ-corrections. (Note that the
1-vertices and 2-vertices are counted separately in ( 5.19) below.)
The vacuum energy Γ (0) contributes to every ST ,n , n≥ 0. Its leading-order ℏ−1 term is
just the complex volume ( 5.10), while the ℏ0 piece contains the corrections ( 5.13)–(5.14) to
the torsion. At higher order in ℏ, we have
(5.18) Γ (0)(Z) = 1
ℏS0 + ℏ0(...) + ℏ
8f· B−1Af +
∞∑
n=2
ℏn−1Bn
n!
N∑
i=1
Li2−n(z−1
i )
(
mod ℏ
24
)
.
Each Sn, n≥ 2, is calculated by taking the ℏn−1 part of Γ (0), and adding to it an ap-
propriate sum of Feynman diagrams. The rules for the diagrams are derived from ( 5.17) as
follows. There are vertices of all valencies k = 1, 2,... , with a vertex factor given by Γ (k)
i .
One draws all connected diagrams (graphs) with
(5.19)
# loops + # 1-vertices + # 2-vertices ≤n.
Eachk-vertex is assigned a factor Γ (k)
i , and each edge is assigned a propagator
(5.20) propagator : Π ij := ℏH−1
ij = ℏ(−B−1A + ∆ z′)−1
ij .
The diagrams are then evaluated by contracting the vertex facto rs with propagators, and
multiplying by a standard symmetry factor . In each diagram, one should restrict to the ℏn−1
term in its evaluation.
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 35
Explicitly, using the asymptotic expansion ( 5.7) of the quantum dilogarithm, we ﬁnd that
the vertices are
1-vertex: Γ (1)
i =−1
2 (B−1ν)i−
∞∑
n=1
ℏn−1Bn
n! Li1−n(z−1
i ) =−1
2 (B−1ν)i + z′
i
2 +... ,(5.21a)
2-vertex: Γ (2)
i =
∞∑
n=1
ℏn−1Bn
n! Li−n(z−1
i ) = ziz′2
i
2 − ℏ
12zi(1 +zi)z′3
i +...(5.21b)
k-vertex: Γ (k)
i = (−1)k
∞∑
n=0
ℏn−1Bn
n! Li2−n−k(z−1
i ) ( k≥ 3)(5.21c)
Note that in Γ (1)
i we could also write B−1ν = B−1Af +f ′′. When the inequality (
5.19)
is saturated, only the leading-order ( ℏ−1 or ℏ0) terms of the vertex factors ( 5.21) need be
considered. Otherwise, subleading ℏ-corrections may be necessary.
Examples of 2-loop and 3-loop Feynman diagrams were given in Figures 1–3 of the Intro-
duction, along with the entire evaluated expression for ST , 2.
