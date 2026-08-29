---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-052-2-detλn
section_title: "(detΛ)N"
section_number: 2
pages: 66-67
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
N
{λδ} = Z{dˆν}
N
detγδ ˆQN+γ−1(λδ)
∆(λ)(detΛ)N
,
where dˆνh,¯h ≡e−ˆV (¯h)dνh,¯h and ˆQk are the corresponding orthogonal polino-
mials. In other words, we reduced the model with potential U(h) to another
model with potential, −ˆV (h), and expressed the diﬀerence in terms of or-
thogonal polinomials ˆQk:
Z{dµ}
N
Z{dˆν}
N
=
1
(detΛ)N · detγδ ˆQN+γ−1(λδ)
∆(λ)
.
(3.67)
If ˆV (h) is adjusted to give rise to some simple orthogonal polinomials, (i.e.
if the new model Z{dˆν}
N
is easy to solve), this representation can considerably
simplify the original model.
Another interpretation of this formula is that we obtained a GKM-like
representation of the from of (3.19) for the discrete scalar-product model.
The only diﬀerence is that ϕ{V }
γ
in (3.19) are changed for ˆQγ−1 in (3.67).
This is an important diﬀerence, because ϕ{V }
γ
in GKM are deﬁned to by
integral formulas like (3.15), ϕ{V }
γ
= ⟨⟨xγ−1⟩⟩or, alternatively, satisfy the
recursive relations like (3.21).
Moreover, generic ϕ{V }
γ
are inﬁnite formal
series in λ−1, while Qγ−1 are orthogonal polinomials. This discreapancy is one
of important stimuli for further developement of the concept of Generalized
Kontsevich model, as well as for search for convenient integral representations
for orthogonal polinomials.
There is, however, at least one interesting situation when the two formulas
indeed coincide. This is the case of Gaussian potentials V and ˆV , when both
ϕ{V }
γ
and Qγ−1 are represented by orthogonal Hermite polinomials, which
possess integral representation, exactly adequate in the context of GKM.
This is the subject of our consideration in the next subsection.
3.8
Equivalence of the discrete 1-matrix and Gaussian
Kontsevich models
Let us take the ordinary 1-matrix model with the local measure dµh =
eU(h)dh to be the scalar-product model, considered in the previous subsection
63
and take Miwa parametrization with upper signs and with rk = −1
2δk,2 (as
we did in the section 2.6). Then ˆV (h) =
P
k rkhk = −h2
2 = (ih)2
2 . The rel-
evant orthogonal polinomials ˆQ are just Hermite polinomials of imaginary
argument:23 Q
{−h2
2 dh}
k
= i−kHek(ih) = hk + . . .. These polinomials possess
an integral representation (3.50):
i1−kHek−1(ih) =
1
√
2πe−h2
2
Z
xk−1e−x2
2 +xhdx
(3.20)
=
ϕ
{ x2
2 }
k
(h).
(3.68)
Using (3.67) and (3.19) we obtain a remarkable relation between the two
matrix models:
ZN{t0 = 0; tk = −1
ktrΛ−k + 1
2δk,2}
ZN{tk = 1
2δk,2}
=
R
N×N dHe
P∞
k=0 tkTrHk
R
N×N dHe
1
2H2
=
=
e−tr Λ2
2
(2π)
n2
2 (detΛ)N
Z
n×n dX(detX)Ne−tr X2
2 +ΛX = Z X2
2 {N, t},
(3.69)
where ZN{tk = 1
2δk,2} = (−2π)
N2
2 cN. This relation can be also regarded as
an identity
R
N×N dHe
1
