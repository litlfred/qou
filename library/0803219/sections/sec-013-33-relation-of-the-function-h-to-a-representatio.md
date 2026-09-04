---
doc_id: 0803219
doc_title: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS"
section_id: sec-013-33-relation-of-the-function-h-to-a-representatio
section_title: "Relation of the function H to a representation. Now we want to relate"
section_number: 3.3
pages: 17-20
source_pdf: 0803219.pdf
source_sha256: 8e37e11b8c8953c8
doc_brief: "ACTA MATHEMATICA VIETNAMICA 219 AN INTRODUCTION TO THE VOLUME CONJECTURE AND ITS GENERALIZATIONS — In this paper we give an introduction to the volume conjectur e and its generalizations."
---
the function H to a representation. It is convenient to put u := θ − 2π √ − 1 so
that the complete hyperbolic structure corresponds to u = 0.
(i) When θ is close to 2 π √ − 1, that is, when u is close to 0.
We put
(3.10) H(u) := Li 2
(
e−ϕ (u)−u
)
− Li2
(
eϕ (u)−u
)
+ uϕ (u).
236 HITOSHI MURAKAMI
Let us calculate the derivative d H(u)/d u . We have
d H(u)
d u
= − log
(
1 − e−ϕ (u)−u)
e−ϕ (u)−u × e−ϕ (u)−u ×
(
− d ϕ (u)
d u − 1
)
+ log
(
1 − eϕ (u)−u)
eϕ (u)−u × eϕ (u)−u ×
(d ϕ (u)
d u − 1
)
+ ϕ (u) + u × d ϕ (u)
d u
= d ϕ (u)
d u
{
log
(
1 − e−ϕ (u)−u
)
+ log
(
1 − eϕ (u)−u
)
+ u
}
+ log
(
1 − e−ϕ (u)−u
)
− log
(
1 − eϕ (u)−u
)
+ ϕ (u).
Since ϕ (u) satisﬁes cosh
(
ϕ (u)
)
= cosh(u) − 1/ 2, we have
eϕ (u) + eϕ (−u) = eu + e−u − 1
and so(
1 − e−ϕ (u)−u
)(
1 − eϕ (u)−u
)
= e−u
(
eu − e−ϕ (u) − eϕ (u) + e−u
)
= e−u.
Therefore we have
d H(u)
d u = 2 log
(
1 − e−ϕ (u)−u
)
+ ϕ (u) + u.(3.11)
If we put
v(u) : = 2 d H(u)
d u − 2π
√
− 1
= 4 log
(
1 − e−ϕ (u)−u
)
+ 2ϕ (u) + 2u − 2π
√
− 1,
(3.12)
we have
exp
(v(u)
2
)
= − exp
(
log
(
eϕ (u)+u − 2 + e−ϕ (u)−u
))
= − eϕ (u)+u + 2 − e−ϕ (u)−u.
We also put m := exp(u). Then since
e±ϕ (u) = cosh(u) − 1
2 ∓
√
− 1
√
1 −
(
cosh(u) − 1
2
)2
= 1
2
(
m + m−1 − 1
)
∓
√ − 1
2
√
(m + 1 + m−1)(3 − m − m−1),
we have
exp
(v(u)
2
)
= 1
2
(
− m2 + m + 2 + m−1 − m−2)
−
√ − 1
(
m − m−1)
2
√
(m + 1 + m−1)(3 − m − m−1)
= − 𝓁(m).
THE VOLUME CONJECTURE AND ITS GENERALIZATIONS 237
Therefore the representation ρ m± sends the longitude λ to
(
− e±v(u)/ 2 ∗
0 − e∓v(u)/ 2
)
.
(ii) When θ is real and |θ |/greaterorequalslantarccosh(3/ 2), that is, Im u = − 2π √ − 1 and |Re u|/greaterorequalslant
arccosh(3/ 2). In this case we put
˜H(u) := Li 2
(
e− ˜ϕ (u)−u
)
− Li2
(
e ˜ϕ (u)−u
)
+ (u + 2π
√
− 1) ˜ϕ (u).
If we deﬁne v(u) as in the previous case by using ˜H instead of H, then we see
that u deﬁnes the same representations as (i).
(iii) When θ is close to 0, that is u is close to − 2π √ − 1.
In this case we may say that θ deﬁnes the abelian representation α exp(θ/ 2) that
sends the meridian element to the matrix
(
eθ/ 2 0
0 e−θ/ 2
)
.
This is because the complex value ∆( E; exp(θ )) is the determinant of the Fox
matrix corresponding to the map π 1(S3 \ E) → H1(S3; Z) ∼= Z → C∗, where the
ﬁrst map is the abelianization, and the second map sends k to exp( kθ ). See for
example [39, Chapter 11].
(iv) When θ = ± arccosh(3/ 2), that is, u = ± arccosh(3/ 2) − 2π √ − 1. Note
that when u = ± arccosh(3/ 2) − 2π √ − 1, the corresponding representation is
non-abelian from (ii), but ‘attached’ to an abelian one from (iii).
Let us study ρ m± deﬁned in Subsection 3.1 more carefully when
m = exp
(
± arccosh(3/ 2)
)
= (3 ±
√
5)/ 2.
First note that d = 0, and so ρ m+ and ρ m− coincide. Moreover the images of
both x and y are upper triangle. Therefore these representations are re ducible.
By the linear fractional transformation, the Lie group SL(2; C) acts on C by(
p q
r s
)
·z := ( pz + q)/ (rz + s). For an upper triangle matrix this becomes
an aﬃne transformation. Therefore if θ = ± arccosh(3/ 2) the corresponding
representations can be regarded as aﬃne.
It is known that each aﬃne representation of a knot group corr esponds to a
zero of the Alexander polynomial of the knot ([4, 8]). See als o [27, Exercise 11.2].
Note also that tr
(
ρ m±
)
= tr
(
α m± 1/ 2
)
in this case.
238 HITOSHI MURAKAMI
