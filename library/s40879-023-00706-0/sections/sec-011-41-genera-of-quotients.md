---
doc_id: s40879-023-00706-0
doc_title: "Bring’s curve: old and new"
section_id: sec-011-41-genera-of-quotients
section_title: "Genera of quotients"
section_number: 4.1
pages: 24-25
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
toc_source: outline
doc_brief: "Bring’s curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
Our ﬁrst step is to know the topology of the quotients we are going to ﬁnd. To this
end, we give the following result.
Proposition 4.1 The data of the quotients of B by subgroups ⟨σ⟩⩽S5 is summarised
by the following table:
σ
Example
|cl(σ)|
|Fix(σ)|
Fixed Points
NS5(⟨σ⟩)/⟨σ⟩
g(B/⟨σ⟩)
(12)
–
10
6
Edges
S3
1
(123)
RS
20
0
–
V4
2
(12)(34)
R
15
2
Vertices
V4
2
(1234)
U
30
2
Vertices
C2
1
(123)(45)
–
20
0
–
C2
0
(12345)
S
24
4
Face-centres
C4
0
Here cl(σ) is the conjugacy class of σ, Fix(σ) = {P ∈B | σ(P) = P}.
Proof As conjugate elements yield isomorphic quotients we need only to give one σ
per conjugacy class. The ﬁrst three columns follow from the group theory we have
previously shown in Sect.2.3, the fourth and ﬁfth follow from Sect.3 and the sixth
is elementary group theory. The ﬁnal column remaining is then a Riemann–Hurwitz
argument for genus, which will we demonstrate for the quotient by (2345) as in [54].
For general σ, denoting by π the projection B →B/⟨σ⟩..= C, Riemann–Hurwitz
says
gB −1 = (deg π)(gC −1) + 1
2 B,
where B is the degree of ramiﬁcation of π, which in the case of a quotient by a group
action corresponds to the ﬁxed point structure of σ.
Consider (24)(35). A ﬁxed point of B under this, given by projective coordinates
xi, i = 1, . . . , 5, must have
(x1, x4, x5, x2, x3) = (λx1, λx2, λx3, λx4, λx5).
From this we can see λ = ±1. Taking λ = 1 gives no solutions, but taking λ = −1
one ﬁnds the equations
x1 = 0,
x2
1 + 2x2
2 + 2x2
3 = 0,
x3
1 = 0,
which gives the two ﬁxed points [0 : 1 : ± i : −1 : ∓i]. Hence we have
4 −1 = 2(gC −1) + 1
2 (1 + 1) ⇒gC = 2.
Bring’s curve: old and new
Page 25 of 46
3
Moving now to (2345), thinking about the possible branching structure we get from
Riemann–Hurwitz
3 = 4(gC −1) + 1
2


P∈Fix(σ)
3 +

P∈Fix(σ 2)\Fix(σ)
1

.
Fixed points of (2345) will correspond to points such that
(x1, x3, x4, x5, x2) = (λx1, λx2, λx3, λx4, λx5),
and we get the constraint λ4 = 1. The equations of the curve become
x1 + x2(1 + λ + λ2 + λ3) = 0,
x2
1 + x2
2(1 + λ2 + 1 + λ2) = 0,
x3
1 + x3
2(1 + λ3 + λ2 + λ) = 0,
and checking the possible cases one ﬁnds that the only ﬁxed points of (2345) are
[0 : 1 : ± i : −1 : ∓i]. These are also the only ﬁxed points of (24)(35) = (2345)2 and
so the second sum vanishes, hence we ﬁnd gC = 1.
R&R [54] provides a nice visual interpretation of the quotient by a 4-cycle, namely
think of a sphere with four handles attached around an equator, then (2345) is the
cycle rotating these handles to each other by a quarter turn about the axis through the
centre of the equator. The ﬁxed points are then where this axis intersects the sphere.
Edge [24], citing Wiman, says that Bring’s curve “is, in ten different ways, in (2, 1)
correspondence with a plane curve of genus 1". The ten (2, 1) correspondences noted
by Edge are exactly the ten quotients by a transposition giving a 2 : 1 map B →E,
where E is an elliptic curve. Such a map is called a bielliptic structure, and Bring’s
curve is the unique genus 4 curve to have ten such structures [12]. This table also lets
us reconstruct the results about the gonality of Bring’s curve from [31].
