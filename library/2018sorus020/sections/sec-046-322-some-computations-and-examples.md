---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-046-322-some-computations-and-examples
section_title: "Some computations and examples"
section_number: 3.2.2
pages: 88-91
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
Some computations and examples
We compute the torsion function on a series of examples of twist knots, and deter-
mine its zeros on the character variety. A presentation of the fundamental group of
87
a
b
λ
µ
Figure 3.1 – A diagram of the Whitehead link. a, b and λ are depicted generators
of the fundamental group, and µ is a counter-clockwise oriented longitude of the
circle component.
the Whitehead link can be computed to be
π1(L52
1) = ⟨a, b, λ| b = λaλ−1, [λ−1, a−1][λ−1, a][λ, a][λ, a−1] = 1⟩
The J(2, 2n)-twists knots, n ∈Z, are obtained as
1
n Dehn ﬁlling along the circle
component. The additional relation is thus µn = λ, where µ = ba−1b−1a. Notice
that the second relation in the presentation above is [λ, µ] = 1, hence is redondant
whence µn = λ. Figure 3.2 shows positive and negative twist knots, for n = ±1.
Hence we obtain the following presentation of twist knot group π1(J(2, 2n)) =
⟨a, b|(ba−1b−1a)na = b(ba−1b−1a)n⟩, or ⟨a, λ|µn = λ⟩where the curve µ is the curve
ba−1b−1a = [λ, a][λ, a−1].
We deﬁne a tautological representation of the character variety X(2, 2n) of the twist
knots J(2, 2n) by
ρ(a) =
 
s
1
0
s−1
!
, ρ(b) =
 
s
0
y −s2 −s−2
s−1
!
88
a
b
a
b
Figure 3.2 – The diagram above if J(2, 2), the trefoil knot. The one below is
J(2, −2), the ﬁgure-eight knot.
89
We will use the variable x = s + s−1. A direct computation shows (see [Kit96], for
instance) that tor(M, ρ) =
det(ρ( ∂r
∂λ))
det(ρ(a)−1) =
det(ρ( ∂r
∂λ))
(2−x)
, where ρ is extended linearly to the
ring Z[π1].
— If n > 0, we obtain tor(M, ρ) = det((1+ρ(µ)+...+ρ(µ)n−1)(1−ρ(b)+ρ(ba−1)−ρ(ba−1b−1))−1)
2−x
— If n < 0, we obtain tor(M, ρ) = det((ρ(µ)−1+...+ρ(µ)n)(1−ρ(b)+ρ(ba−1)−ρ(ba−1b−1)))
2−x
The trefoil knot J(2,2)
The character variety equation is given by X(2, 2) = {(x2 −y −2)(y −1) = 0}.
The component of irreducible type X is thus {y −1 = 0}. We compute the torsion
function in C[x, y]/(y −1), it is tor(M, ρ) = y−2x+3
2−x
= 2, the torsion is constant.
The ﬁgure-eight knot J(2,-2)
Let X = {2x2 +y2 −x2y−y−1 = 0} the component of irreducible type of X(2, −2).
We have tor(M, ρ) = (4x2 −x2y + y2 −y −6x + 3)/(2 −x) = 2x −2 in C[X], hence
there is a zero at the point {x = 1, y = 1}, with multiplicity 2.
The knot 52 : J(2,4)
Here X = {−x2(y −1)(y −2) + y3 −y2 −2y + 1 = 0}, and tor(M, ρ) has two double
zeros when x = y are roots of x2 −3x + 1.
The knot 61 : J(2,-4)
Here X = {x4(y −2)2 −x2(y + 1)(y −2)(2y −3) + (y3 −3y −1)(y −1) = 0}, and
tor(M, ρ) has three double zeros when x = y are roots of x3 −4x2 + 3x + 1.
Remark 3.2.2. We observe that each time we have found a zero for the torsion, it
had multiplicity 2 and {tor(M, ρ) = 0} ⊂X ∩{x = y}. We have checked that this
inclusion is strict. We have no precise interpretation of those phenomenon, we think
that it comes from the computation of the torsion on the character variety of the
Whitehead link .
