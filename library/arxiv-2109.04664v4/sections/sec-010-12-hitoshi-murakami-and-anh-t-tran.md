---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-010-12-hitoshi-murakami-and-anh-t-tran
section_title: "HITOSHI MURAKAMI AND ANH T. TRAN"
section_number: 12
pages: 12-14
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
Re 
Im 
1− ϕ (ξ)/ξ − ϕ (ξ)/ξ 
(1 − ϕ (ξ)/ξ ) tan θ√− 1
− (1 + ϕ (ξ)/ξ ) tan θ√− 1
Ob− b+
tan θ√− 1
− tan θ√− 1
− 2 tan θ√− 1
Figure 1. The parallelogram is the boundary of P , the circle is
the boundary of Nδ0, the red region is D−, and the green region is
D+. The cyan rectangle indicates the boundary of R+ ∪R−
(see below).
(iv). Condition (3) in Proposition 4.2 is satisﬁed.
Proof.
(i). The distances to the upper side, the lower side, the left side, an d the
right side of P from the origin O is (1 −ϕ (ξ)/ξ ) sinθ, (1 + ϕ (ξ)/ξ ) sinθ,
ϕ (ξ)/ξ and 1 −ϕ (ξ)/ξ , respectively. Since (1 − ϕ (ξ)/ξ ) sinθ < ϕ(ξ)/ξ
from the assumption sin θ < ϕ
ξ−ϕ (ξ) , δ0 is less than these distances.
So Nδ0 is contained in the parallelogram P . Moreover since ψ ′′(0) =
F ′′(ϕ (ξ)/ξ ) = −ξ
√
(2 cosh(ξ) − 1)2 − 4< 0, ψ (z) is of the form (4.3) with
a := −ξ
2
√
(2 cosh(ξ) − 1)2 − 4.
(ii). We ﬁrst show that b± ∈ D± ∩P . It is clear that b− < 0, b+ > 0, and
b± ∈P . The inequality Re ψ (b±)< 0 follows from Lemma 4.1. So, we can
choose ε0> 0 so that Re ψ (b±)< −ε0.
Next, we will show that for each x ⁄= 0 with −ϕ (ξ)/ξ <x< 1 −ϕ (ξ)/ξ ,
the set {y ∈ R | Reψ (x +y√−1)< 0} ∩P is an open interval containing 0.
Then, we can see that D± ∩P is connected.
If we put
g(x,y ) := eξ +e−ξ −eξ(x+y√−1)+ϕ (ξ) −e−ξ(x+y√−1)−ϕ (ξ),
then we have
(4.6) d
dy Reψ (x +y
√
−1) = − argg(x,y )
from (4.2). Now we have
Reg(x,y ) = 2 coshξ − 2 cosh
(
ξ
(
x + ϕ (ξ)
ξ
))
cos(ξy),
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 13
and
Img(x,y ) = − sinh
(
ξ
(
x + ϕ (ξ)
ξ
))
sin(ξy).
We can see that Re g(x,y ) is positive since 0 <x +ϕ (ξ)/ξ < 1. We will
show that Im g(x,y )< 0 (Img(x,y )> 0) if y >0 (y <0, respectively). If
x +y√−1 ∈ P , then −2 tanθ < y <tanθ (see Figure 1). Together with
the assumption tan θ < π
2ξ , we conlude that |y| ≤ 2 tanθ < π/ξ , and so
|ξy|<π . This implies that sin( ξy)> 0 (sin(ξy)< 0, respectively) if y >0
(y < 0, respectively). Since x +ϕ (ξ)/ξ > 0, we see that Im g(x,y ) < 0
(Img(x,y )> 0) if y >0 (y <0, respectively).
Therefore argg(x,y ) is positive (negative, respectively) when y< 0 (y >
0, respectively). It follows that if y > 0 (y < 0, respectively), Re ψ (x +
y√−1) is monotonically increasing (decreasing, respectively) with respe ct
to y. Since Re ψ (x) < 0 from Lemma 4.1, we see that {y ∈ R | Reψ (x +
y√−1)< 0} ∩P is an open interval containing 0.
Therefore, we conclude that D± ∩P is connected.
(iii). We will show that the region R+ := [b−,b +] × [0,δ 0] \ {O} is contained in
the region {x +y√−1 ∈ C | Reψ (x +y√−1) < 2πy }, which means that
the region (4.4) equals R+. Then we can ﬁnd a path connecting b− andb+
in R+, proving Condition (2).
In fact, we can show if b− ≤ x ≤ b+ and 0 ≤ y ≤ δ0 ((x,y ) ⁄= (0, 0)),
then Reψ (x +y√−1) − 2πy< 0 as follows.
Wheny> 0, then Img(x,y )< 0 from the argument in (ii), and so g(x,y )
is in the fourth quadrant in the complex plane because Re g(x,y ) > 0.
Therefore we have 0 > argg(x,y )> −π/ 2. This shows that d
dy
(
Reψ (x +
y√−1)−2πy
)
< 0 wheny> 0 from (4.6), and so we conclude that Re ψ (x+
y√−1) − 2πy <0 since Re ψ (x) ≤ 0 from Lemma 4.1.
(iv). We will show that the region R− := [b−,b +] × [−δ0, 0] \ {O} is in the region
{x +y√−1 ∈ C | Reψ (x +y√−1)< −2πy }, which means that the region
(4.5) equals R− ∪ {O}. Then we can ﬁnd a path connecting b− and b+ in
R−, proving Condition (3).
We will show if b− ≤ x ≤ b+ and −δ0 ≤ y ≤ 0 ((x,y ) ⁄= (0, 0)), then
Reψ (x +y√−1) + 2πy <0.
When y < 0, then Im g(x,y ) > 0 from the argument in (ii), and so
g(x,y ) is in the ﬁrst quadrant because Re g(x,y ) > 0. Therefore we have
0 < argg(x,y ) < π/ 2. This shows that d
dy
(
Reψ (x +y√−1) + 2πy
)
> 0
when y < 0, and so we conclude that Re ψ (x +y√−1) + 2πy < 0 since
Reψ (x) ≤ 0 from Lemma 4.1.
□
Now we can prove Theorem 1.5.
Proof of Theorem 1.5. From Proposition 4.2, there exists ε> 0 such that
1
N
∑
−ϕ (ξ)/ (2ξ)≤k/N ≤(1−ϕ (ξ)/ξ )/ 2
eNψ (k/N ) =
∫ (1−ϕ (ξ)/ξ )/ 2
−ϕ (ξ)/ (2ξ)
eNψ (z)dz +O
(
e−Nε)
.
Since fN (z +ϕ (ξ)/ξ + 1/ (2N )) −S(ξ)/ξ uniformly converges to ψ (z), we have
1
N
∑
−ϕ (ξ)/ (2ξ)≤k/N ≤(1−ϕ (ξ)/ξ )/ 2
eN (fN (k/N +ϕ (ξ)/ξ +1/ (2N ))−S(ξ)/ξ )
