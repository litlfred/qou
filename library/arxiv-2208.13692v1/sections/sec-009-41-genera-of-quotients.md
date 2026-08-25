---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-009-41-genera-of-quotients
section_title: "Genera of Quotients"
section_number: 4.1
pages: 18-20
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "Bring's curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
going to ﬁnd. To this end, we give the following result.
Proposition 4.1. The data of the quotients of B by subgroups⟨σ⟩≤ S5 is summarised by
the following table:
BRING’S CUR VE: OLD AND NEW 19
σ Example |cl(σ)| |Fix(σ)| Fixed Points NS5(⟨σ⟩)/⟨σ⟩ g (B/⟨σ⟩)
(12) - 10 6 Edges S3 1
(123) RS 20 0 - V4 2
(12)(34) R 15 2 Vertices V4 2
(1234) U 30 2 Vertices C2 1
(123)(45) - 20 0 - C2 0
(12345) S 24 4 Face-centres C4 0
Herecl(σ) is the conjugacy class of σ, Fix(σ) ={P∈B| σ(P ) =P}.
Proof. As conjugate elements yield isomorphic quotients we need only to give one σ per
conjugacy class. The ﬁrst three columns follow from the group theory we have previously
shown in §2.3, the fourth and ﬁfth follow from §3 and the sixth is elementary group theory.
The ﬁnal column remaining is then a Riemann-Hurwitz argument for genus, which will we
demonstrate for the quotient by (2345) as in [RR92].
For generalσ, denoting by π the projectionB→B /⟨σ⟩ :=H, Riemann-Hurwitz says
gB− 1 = (degπ)(gH− 1) + 1
2B,
whereB is the degree of ramiﬁcation of π, which in the case of a quotient by a group action
corresponds to the ﬁxed point structure of σ.
Consider (24)(35). A ﬁxed point of B under this, given by projective coordinates xi,i =
1,..., 5, must have
(x1,x 4,x 5,x 2,x 3) = (λx1,λx 2,λx 3,λx 4,λx 5).
From this we can see λ =±1. Taking λ = 1 gives no solutions, but taking λ =−1 one ﬁnds
the equations
x1 = 0, x 2
1 + 2x2
2 + 2x2
3 = 0, x 3
1 = 0,
which gives the 2 ﬁxed points [0 : 1 : ±i :−1 :∓i]. Hence we have
4− 1 = 2(gH− 1) + 1
2(1 + 1)⇒gH = 2.
Moving now to (2345), thinking about the possible branching structure we get from Riemann-
Hurwitz
3 = 4(gH− 1) + 1
2

 ∑
P∈Fix(σ)
3 +
∑
P∈Fix(σ2)\Fix(σ)
1

.
Fixed points of (2345) will correspond to points such that
(x1,x 3,x 4,x 5,x 2) = (λx1,λx 2,λx 3,λx 4,λx 5),
and we get the constraint λ4 = 1. The equations of the curve become
x1 +x2(1 +λ +λ2 +λ3) = 0,
x2
1 +x2
2(1 +λ2 + 1 +λ2) = 0,
x3
1 +x3
2(1 +λ3 +λ2 +λ) = 0,
20 H. W. BRADEN AND LINDEN DISNEY-HOGG
and checking the possible cases one ﬁnds that the only ﬁxed points of (2345) are [0 : 1 : ±i :
−1 :∓i]. These are also the only ﬁxed points of (24)(35) = (2345) 2 and so the second sum
vanishes, hence we ﬁnd gH = 1. □
R&R [RR92] provides a nice visual interpretation of the quotient by a 4-cycle, namely
think of a sphere with 4 handles attached around an equator, then (2345) is the cycle
rotating these handles to each other by a quarter turn about the axis through the center of
the equator. The ﬁxed points are then where this axis intersects the sphere. Edge [Edg78],
citing Wiman, says that Bring’s curve “is, in ten diﬀerent ways, in (2 , 1) correspondence
with a plane curve of genus 1”. The 10 (2 , 1) correspondences noted by Edge are exactly
the 10 quotients by a transposition giving a 2 : 1 map B→E , whereE is an elliptic curve.
Such a map is called a bielliptic structure, and Bring’s curve is the unique genus-4 curve to
have 10 such structures [CDC05]. This table also lets us reconstruct the results about the
gonality of Bring’s curve from [GWW10].
