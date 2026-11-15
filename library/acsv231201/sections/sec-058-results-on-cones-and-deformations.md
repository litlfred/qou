---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-058-results-on-cones-and-deformations
section_title: "Results on cones and deformations"
section_number: null
pages: 359-365
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
341
the fortress generating function, and the GKZ symmetric rational function,
whose coeﬃcients exhibit a lacuna phenomenon.
11.1 Results on cones and deformations
Let Q be a Laurent polynomial in d variables deﬁning a variety V and set
M = Cd
∗\ V. In order to work with polynomial amoebas, it is convenient to
deﬁne and manipulate cones in logarithmic space. To that end, deﬁne the ﬂat
torus Tﬂat = (R/(2πR))d, let q(x) = (Q ◦exp)(x) = Q(ex1, . . . , exd), and recall
the notation Te(x) = {exp(x + iy) : y ∈Tﬂat} for any x ∈Rd.
Exercise 11.2. Is the map exp : Rd + i Tﬂat →Cd
∗a diﬀeomorphism?
Let B be a component of the complement of amoeba(Q), ﬁx a direction
ˆr∗, and suppose that −ˆr∗· x is minimized on B at a unique point x∗, nec-
essarily on the boundary ∂B. Recall from Deﬁnition 6.26 and Exercise 6.8
the open geometric tangent cone tanx(B) to B at a point x, with closed dual
cone normalx(B) = (−tanx(B))∗. These cones are projective: they are cones
over the origin, closed under multiplication by positive real constants. The fol-
lowing result is a combination of [BP11, Corollary 2.15 (i), Corollary 2.16,
Proposition 2.22, Theorem 5.4].
Theorem 11.1. Under the setup above, there exists a bundle Z of convex pro-
jective cones {Z(y) : y ∈Tﬂat} with the following properties.
(i) For all y ∈Tﬂat the cone Z(y) contains tanx∗(B).
(ii) Let⃗V be a smooth non-vanishing section of Z, so that⃗V : Tﬂat →Rd \{0}
is smooth and⃗V(y) ∈Z(y) for all y. If x ∈B then there exists an ε > 0
such that the set
n
exp

x∗+ δt⃗V(y) + (1 −t)(x −x∗) + iy

: y ∈Tﬂat, 0 ≤t ≤1, 0 < δ < ε
o
(11.1)
is disjoint from V.
(iii) For each y ∈Tﬂat let N(y) = (−Z(y))∗be the outward dual cone to
Z(y), and let ˆr be any real unit vector. If ˆr ∈N(y) then exp(x∗+ iy) is
a stratiﬁed critical point for h ˆr. If ˆr < N(y) then there is some vector
v ∈Z(y) such that ˆr · v = 1.
(iv) The cones Z(y) vary lower-semicontinuously in y. In particular, if yn →
y in Tﬂat then Z(y) ⊆lim inf Z(yn).
Remark 11.2. The cones Z(y) will typically be open cones, such as inter-
sections of open halfspaces. We will see below that we can choose Z(y) to
342
Cone point asymptotics
be cones of hyperbolicity of the homogenization of q at x + iy, picking the
one that contains tanx(B). While the theorem does not rule out other choices,
choosing smaller cones would be wasteful because then N(y) would be larger
and the last part of conclusion (iii) would apply less often, while choosing
larger cones turns out to make conclusion (ii) impossible to satisfy. The hy-
pothesis that x∗∈∂B is important: for a counterexample when this fails, see
Exercise 11.10.
The cones N(y) allow us to deﬁne a set of points that locally look like min-
imal critical points, except that they “don’t see” points of Q.
Deﬁnition 11.3. The set local( ˆr) of locally minimal points of Q with respect
to x∗in the direction ˆr consists of the points z = exp(x∗+ iy) ∈Te(x∗),
where Q vanishes and ˆr ∈N(y). We also deﬁne the set of logarithmic locally
minimal arguments localarg( ˆr) = {y ∈Tﬂat : exp(x + iy) ∈local( ˆr)}.
Locally minimal points are the only points that can cause an obstruction
when trying to deform the Cauchy domain of integration to lower height.
Theorem 11.4. Assume the hypotheses of Theorem 11.1 and let T = Te(x)
for any x ∈∂B. If local( ˆr) is empty then T is homotopic in M to a cycle C∗
whose maximum height is less than h∗= −ˆr · x∗.
Proof of Theorem 11.4 from Theorem 11.1
Fix x ∈∂B and for each y ∈Tﬂat
let v(y) denote a vector v as in conclusion (iii) of Theorem 11.1. By semicon-
tinuity, for each y ∈Tﬂat there is a neighborhood N(y) of y in Tﬂat such that
v(y) ∈Z(y′) when y′ ∈N(y). Cover Tﬂat with ﬁnitely many of the neigh-
borhoods {N(y j) : 1 ≤j ≤m} by compactness, let {ψ j : 1 ≤j ≤m} be a
partition of unity subordinate to this ﬁnite cover, and for y ∈Tﬂat deﬁne⃗
V(y) =
m
X
j=1
ψ(y)v(y j) .
(11.2)
For each j such that y ∈N(y j), the vector v(y j) lies in the cone Z(y). The vec-
tor⃗V(y) is a convex combination of these vectors and therefore, by convexity
of the cone Z(y), we see that⃗V(y) ∈Z(y). By linearity of the dot product with
ˆr∗, we also have that⃗V(y) · ˆr∗> 0. In particular,⃗V is a smooth non-vanishing
section of Z. Let ε > 0 be as in conclusion (ii) of Theorem 11.1. Again using
convexity of Z(y) and the fact that Z(y) ⊇tanx∗(B) ⊇B −x (the set B with
x∗translated to the origin), we see that the line segment between and⃗V(y) and
any x ∈B is contained in Z(y).
Deﬁne the map φ : Tﬂat ×[0, 1] by
φt(y) = exp
n
iy + x∗+ δ
h
(1 −t)(x −x∗) + t⃗V(y)
i o
.
(11.3)
11.1 Results on cones and deformations
343
By construction φ is continuous with φ0(Tﬂat) being the chain Te(u) for u =
x∗+ δ(x −x∗) ∈B. Because each line segment from u to⃗V(y) is in Z(y), and
exp(iy +x∗+v) < V for any v in any Z(y), we see that the homotopy φ avoids
V. The homotopy φ deforms Te(u) to the cycle φ1(Tﬂat), with the height of a
point φ1(y) given by −ˆr∗· Re{x∗+⃗V(y)}. Because⃗V(y) was picked according
to conclusion (iii) of Theorem 11.1, we see that ˆr∗·⃗V(y) is strictly positive,
and therefore that h ˆr∗(φ1(y)) < −ˆr∗· x∗, ﬁnishing the proof.
□
Theorem 11.5. Assume the hypotheses of Theorem 11.1 and let T = Te(x) for
any x ∈∂B. If local( ˆr) is ﬁnite and nonempty then for any δ > 0 the torus T
is homotopic in M to a cycle whose maximum height is less than h∗= −ˆr · x∗
outside of balls of radius δ around the points of W = local( ˆr).
Proof of Theorem 11.5 from Theorem 11.1
Repeat the proof of Theorem 11.4,
with the following modiﬁcations. For y < W, choose a smaller N(y) if neces-
sary so that W ∩N(y) = ∅. For y ∈W, deﬁne N(y) to be the preimage under
the exponential map of the ball of radius δ centered at exp(x∗+ iy) and set
v(y) = 0. Choose again a ﬁnite open subcover N(y j : 1 ≤j ≤m} of Tﬂat and
construct⃗V by (11.2) and φt by (11.3) as before. The cycle Cδ = φ1(Tﬂat) is
homotopic in M to T(u) and satisﬁes the conclusion of the theorem.
□
Corollary 11.6. The conclusions of Theorems 11.4 and 11.5 can be strength-
ened to hold simultaneously for all ˆr in some neighborhood.
Proof
This follows from the ﬁniteness of the open cover in each case and the
fact that the strict inequality over each N(y) actually bounds ˆr∗·⃗V(y) away
from zero.
□
A simpliﬁed argument for smooth points
It will take a lot of work to prove Theorem 11.1 below, so we ﬁrst illuminate
the argument by proving a special case that does not need the full theory of
cones of hyperbolicity. Assume for the remainder of this section that
T(x∗) ∩V consists only of smooth points of V.
(∗)
It turns out that cones of hyperbolicity at smooth points are always halfspaces:
Theorem 6.44 in Chapter 6 implies that for a minimal point z ∈V the vector
∇log Q(z) is a complex scalar multiple of a real unit vector λ, and this real
vector, with proper orientation, deﬁnes the correct cone.
Deﬁnition 11.7. For y ∈Tﬂat with q(x∗+ iy) , 0 deﬁne Z(y) = Rd. For
y ∈Tﬂat with q(x∗+ iy) = 0 and z = exp(x∗+ iy) a smooth point of V, let
Z(y) = {x ∈Rd : x · λ(z) < 0} .
(11.4)
344
Cone point asymptotics
Lemma 11.8. Assume the hypotheses of Theorem 11.1 as well as the smooth
point assumption (*). Then the family {Z(y) : y ∈Tﬂat} in Deﬁnition 11.7
satisﬁes conclusions (i), (iii), and (iv) of Theorem 11.1.
Note that we do not require conclusion (ii) of Theorem 11.1 for our special
arguments about deformations in the smooth case below.
Proof
Conclusion (i) follows from part (b) of Theorem 6.44. For conclu-
sion (iii), note that N(y) is by deﬁnition empty if q(x∗+ iy) , 0, in which
case Z(y) is all of Rd and the conclusion is trivial. Assume therefore that
q(x∗+ iy) = 0 and let λ = λ(y) denote the vector (∇log Q)(exp(x∗+ iy))
after normalizing to a unit vector and orienting to point away from B, so that
N(y) is the ray parallel to λ. The point exp(x∗+ iy) is critical in directions
precisely ±λ, because smooth points are critical precisely for directions paral-
lel to the logarithmic gradient; this veriﬁes that ˆr ∈N(y) implies ˆr is a critical
direction. If ˆr , ±λ then the dot product with ˆr is unbounded both above
and below on the halfspace Z(y) with outward normal λ, so we can choose
v ∈Z(y) with ˆr · v = 1. If ˆr = −λ then ˆr ∈tanx(B) = Z(y) and we can
choose v = c ˆr, where c = || ˆr||−1
2
> 0. Conclusion (iv) follows from the fact
that S = T(x∗) ∩V is closed and ∇log Q is continuous and non-vanishing on
S .
□
Theorem 11.9 (Theorem 11.4 for smooth points, self-contained). Assume the
hypotheses of Theorem 11.4 as well as the smooth point assumption (*). Then
for x ∈B, the torus T(x) is homotopic in M to a cycle C∗with maximum
height less than h∗= −ˆr∗· x∗.
Proof
Fix x ∈B and mimic the proof of Theorem 11.4 up through (11.2).
That is, for each y ∈Tﬂat choose vectors v(y) ∈Z(y) and neighborhoods N(y)
with v(y) ∈Z(y′) when y′ ∈N(y); then deﬁne⃗V(y) via (11.2). We claim,
picking N′(y) smaller if necessary, that over each N′(y) there is a suﬃciently
small δ > 0 such that for all 0 ≤t ≤1,
q

x∗+ iy′ + δ[t⃗V(y) + (1 −t)(x −x∗)]

, 0 .
(11.5)
If q(x∗+ iy) , 0 then we can pick N′ and δ to keep q from vanishing
by continuity, so we assume that q(x∗+ iy) = 0. Nonvanishing of (11.5) for
suﬃciently small δ follows from the Taylor expansion of the left-hand side in
δ. Speciﬁcally, because the gradient of q is a multiple of λ, we have
q

x∗+ iy + δ[t⃗V(y) + (1 −t)(x −x∗)]

= 0 + δ λ(y) · (t⃗V(y) + (1 −t)(x −x∗))
|                                    {z                                    }
g(t)
+O(δ2).
11.1 Results on cones and deformations
345
Lemma 11.8 implies that g(t) has modulus bounded away from zero over 0 ≤
t ≤1 for ﬁxed x and choice of⃗V(y), because both⃗V(y) and x −x∗are in the
interior of the negative halfspace for λ.
We have now shown that δ can be chosen so that (11.5) holds with y in place
of y′. Choosing N′ small enough completes the claim for the actual (11.5).
This implies that the homotopy deﬁned by (11.3) remains in M, completing
the proof of Theorem 11.9.
□
The same argument gives the following version of Theorem 11.5 for smooth
points.
Corollary 11.10. Assume the hypotheses of Theorem 11.5 as well as the smooth
point assumption (*). Then for x ∈B and any δ > 0 the torus T(x) is homo-
topic in M to a cycle C∗with maximum height less than h∗= −ˆr∗· x∗except
in a δ-neighborhood of W.
□
Exercise 11.3. Let Q(x, y) = 5 −x −x−1 −y −y−1, whose amoeba is displayed
below with the boundary points p = (−log 2, −log 2) and q = (log 2, log 2)
speciﬁed. For x = p and x = q ﬁnd T(x)∩VQ, ﬁnd Z(y) for each x+iy with
exp(x + iy) ∈V, and determine whether or not local( ˆr) is empty.
Example 11.11. Consider the bivariate rational function
F(x, y) =
1
(1 + 2x)(1 −x −y)
in the main diagonal direction ˆr = (1/2, 1/2). The singular variety of F has
one non-smooth point (x, y) = (−1/2, 3/2), which is not minimal as it has
strictly greater coordinate-wise modulus than the minimal critical point σ =
(1/2, 1/2). The point σ is not ﬁnitely minimal because
V ∩T(σ) = {(1/2, 1/2)}
∪
{(−1/2, eiθ2/2) : θ2 ∈(−π, π)} ,
but it does satisfy ﬁnite criticality. Let us construct the homotopy Φt(y) for
346
Cone point asymptotics
this example. For (θ1, θ2) ∈Tﬂat we have Q(e−ln(2)+iθ1, e−ln(2)+iθ2) = 0 only
when θ1 = θ2 = 0 or θ1 = π. Since
(∇log Q)(1/2, 1/2) = −(1, 1)
and
(∇log Q)(−1/2, y) = (y −3/2) × (1, 0) ,
we have
Z(θ1, θ2) =

{z : z · (1, 1) < 0}
if θ1 = θ2 = 0
{z : z · (1, 0) < 0}
if θ1 = π
R2
otherwise.
Figure 11.1 Left: The elements of Tﬂat, drawn in [−π, π]2, for which
Q(e−ln(2)+iθ1, e−ln(2)+iθ2) = 0, together with the real vectors equal to (∇log Q)(x, y)
at these points, up to a non-zero scalar multiple. Right: The open sets N1 and
N2 consist of the small circle of radius ε and the rectangular strips on either side
(identiﬁed as one large strip since −π = π in Tﬂat). The open set N3 consists of the
remaining points and some small overlap with N1 and N2 to make N1 ∪N2 ∪N3
an open cover. The vectors vj are drawn in each region.
Fix ε > 0 suﬃciently small, let
N1 = {−π < θ1, θ2 ≤π : θ2
1 + θ2
2 < ε} ⊂R2 ,
let
N2 = (π −ε, π + ε) × (−π, π] ⊂R2,
and let N3 be an open set containing Tﬂat \(N1 ∪N2) having arbitrarily small
intersection with N1 ∪N2. We identify N1, N2, and N3 with their cosets in
Tﬂat = (R/2πZ)2; Figure 11.1 gives a picture of the situation. If
v1 = (−1, −1),
v2 = (−1, 2),
and
v3 = (1/2, 1/2)
then vj ∈K(y) for y ∈N j, and v2 · r = v3 · r = 1 as desired (in this case
