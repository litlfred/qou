---
doc_id: 1-s20-s0166864101002632-main
doc_title: "PII: S0166-8641(01)00263-2"
section_id: sec-002-3-thick-knots-have-bounded-energy
section_title: "Thick knots have bounded energy"
section_number: 3
pages: 7-11
source_pdf: 1-s2.0-S0166864101002632-main.pdf
source_sha256: bc5aa8a7663b2a9f
toc_source: inferred
doc_brief: "PII: S0166-8641(01)00263-2 — The Möbius energy of a knot is an energy functional for smooth curves based on an idea of self- repelling."
---
In this section, we prove that the Möbius energy of a knot is bounded by the ropelength.
Our goal is partly the theorem itself and partly the paradigm: any “energy” deﬁned in terms
of inverse-square distances should have an analogous bound, with the proof following this
model.
Theorem 8. If K is a smooth knot in R3 then
EO4(K) < 4.57EL(K)4/3.
(3)
Theorem 9. If K is a smooth knot in R3 then
EO4(K) ⩽1
4EL(K)2.
(4)
Remark. For short knots, the quadratic bound is better than the 4/3 power bound.
Comparing (3) to (4), we see that one needs ropelengths over 79 before the advantage
of the lower exponent is evident. If one uses the actual bound (12) we obtain in the proof,
which is a complicated expression dominated by a 4/3 power term, then that bound is
lower than (4) for ropelengths > 41. Computer simulations suggest [23,35] the only knots
that can be realized with a ropelength ⩽41 are the unknot and the trefoil.
Proof of Theorems 8 and 9. We will obtain the quadratic bound en route to the 4/3 power
bound.
We follow an overall plan similar to [5,6], but introduce a limit process in the main
argument. Since EO4 and EL are both invariant under change of scale, we begin by
rescaling K to have thickness R(K) = 1, so that EL(K) is just the total arclength of K,
which we abbreviate L.
The energy EO4(K) is deﬁned as a double-integralover K ×K. We bound separately the
integral over the portion of K × K consisting of pairs (x,y) with arc(x,y) ⩽πR(K) = π,
and the integral over the rest of K × K.
Let
Eprox =

x∈K

arc(x,y)⩽π
1
|x −y|2 −
1
arc(x,y)2 ,
104
E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
Edist =

x∈K

arc(x,y)⩾π
1
|x −y|2 ,
and
Ereg =

x∈K

arc(x,y)⩾π
1
arc(x,y)2 .
So we have
EO4 = Eprox + Edist −Ereg.
By Lemma 5,
Eprox ⩽2
π L.
Also, by symmetry of the circle,
Ereg =

x∈K

2
L
2

π
1
t2 dt
	
dx = L

2
L
2

π
1
t2 dt
	
= 2
π L −4,
so
EO4 ⩽Edist + 4.
(5)
We now bound Edist. We shall bound the inner integral and then multiply by the length
of K to bound the energy. The inner integral, for each x, is
I x
dist =

arc(x,y)⩾π
1
|x −y|2 .
Here ﬁrst is the quadratic bound.
By Lemma 3, and our rescaling to R(K) = 1, we have for each point y ∈K,
arc(x,y) ⩾π ⇒|x −y| ⩾2.
Thus,
I x
dist ⩽1
22 (L −2π).
Multiplying by L, we get
Edist ⩽1
4L2 −π
2 L.
(6)
Combine (6) with (5) to complete a quadratic polynomial bound:
EO4(K) ⩽1
4L2 −π
2 L + 4.
(7)
Because K is a smooth closed curve with maximum curvature ⩽1 (by Lemma 2 and the
fact that we have normalized K to have thickness radius = 1), the total curvature of K is
E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
105
at most L. But by Fenchel’s theorem, the total curvature of a closed curve is at least 2π.
Thus L ⩾2π > 8/π, so the linear part of (7) is negative, and we have
EO4(K) ⩽1
4L2.
(8)
We now develop the 4/3 power bound. If L < 104
3 +2π ≈41, i.e., L−2π < 4
3

33 −13
,
then our proof stops here. The quadratic bound (4) is valid and certainly (4) < (3), so (3)
is valid as well. We continue under the assumption that EL(K) ⩾104
3 + 2π.
The ﬁrst observation is that for any ρ > 0, if |x −y| ⩾ρ, then the integrand
1
|x−y|2 ⩽1
ρ2 .
In obtaining the quadratic bound, we stopped here, allowing the idea that with respect
to each point x ∈K, the whole knot (except for the arc around x of length π in each
direction) lies just at distance 2 from x. But the knot is thick: a piece w of K of length ℓ(w)
carries along with it a solid tube W of volume πℓ(w) (we still are assuming R(K) = 1).
Furthermore, such a tube W cannot intersect any other part of K nor any of the rest of
the tube around K. This restricts how much length of K can be packed within any given
distance from x.
Fix x on K. Let Ydist denote the set on which we integrate to compute I x
dist, that is Ydist =
{y ∈K: arc(x,y) ⩾π}. The arclength of Ydist is just L −2π. Let S(ρ,σ] denote the half-
open spherical shell centered at x with radius from ρ to σ. Let Y(ρ,σ] = Ydist ∩S(ρ,σ],
a measurable set, and let ℓ(ρ,σ] denote its 1-dimensional measure, i.e., the measure of the
length of K lying in S(ρ,σ]. Let T (ρ,σ] be the solid tube with axis Y(ρ,σ], that is, the
portion of the unit radius tube about K consisting of disks centered at points y ∈Y(ρ,σ].
The 3-dimensional measure, i.e., volume, of T (ρ,σ] is πℓ(ρ,σ]. Deﬁne S[ρ,σ], Y[ρ,σ],
ℓ[ρ,σ], and T [ρ,σ] analogously. Note that Ydist ⊂S[2,L/2]. The subset of Ydist lying at
distance exactly 2 from x plays a special role in the analysis, so we also deﬁne S[2], Y[2],
ℓ[2], and T [2].
Let P = ( 3
4L −3π
2 + 1)1/3 −1. The constant P is the radius required so that a spherical
shell from r = 1 to r = P + 1 has the same volume as a tube of radius 1 about a set of
length L −2π.
We bound the total amount of length that can lie in each spherical shell by a function ℓ∗
(see (9) below). Let ℓ∗[2] = 4
3(33 −13) = 104
3 . For 2 ⩽a < b, let
ℓ∗(a,b] = 4
3
min{b,P} + 13 −min{a,P} + 13.
In particular, when 2 ⩽a < b ⩽P , this simpliﬁes to
ℓ∗(a,b] = 4
3

(b + 1)3 −(a + 1)3
.
Let
ℓ∗[2,b] = ℓ∗[2] + ℓ∗(2,b].
For b ⩽P , ℓ∗[2,b] = 4
3((b + 1)3 −13). For b > P , notice that ℓ∗(2,b] = ℓ∗(2,P] so
ℓ∗[2,b] = ℓ∗[2,P] = L −2π.
We now show that
ℓ[2,r] ⩽ℓ∗[2,r]
for all 2 ⩽r.
(9)
106
E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
The tube T [2,r] has volume πℓ[2,r]. But T [2,r] lies entirely within S[1,r + 1], whose
volume is 4
3π

(r + 1)3 −13
. Thus, when 2 ⩽r ⩽P ,
πℓ[2,r] ⩽4
3π(r + 1)3 −13 = πℓ∗[2,r].
If r > P , then ℓ∗[2,r] = ℓ∗[2,P] = L −2π ⩾ℓ[2,r]. Thus, we have (9).
We next partition Ydist into sets Wj whose distance to x is controlled, and express I x
dist
as the sum of the contributions from these sets.
Let n ∈N and δ = P−2
n . Then,
ℓ∗[2,P] = ℓ∗[2] + ℓ∗(2,2 + δ] + ℓ∗(2 + δ,2 + 2δ] + ··· + ℓ∗(P −δ,P]
= L −2π.
We deﬁne a sequence of sets {Wj} using Lemma 7 as follows. Let ν0 = ℓ∗[2] and
νj = ℓ∗(2 + (j −1)δ,2 + jδ] for 1 ⩽j ⩽n. Note that νn = ℓ∗(2 + (n −1)δ,2 + nδ] =
ℓ∗(P −δ,P]. Since ν0 + ν1 + ··· + νn = L −2π = µ(Ydist), by Lemma 7, there exists a
sequence 2 ⩽ρ0 ⩽ρ1 ⩽··· ⩽ρn and a partition of Ydist into measurable sets W0,...,Wn
such that: for 1 ⩽j ⩽n, we have µ(Wj) = νj and Wj ⊆Ydist ∩S[ρj−1,ρj]; for j = 0, we
have µ(W0) = ν0 and W0 ⊆Ydist ∩S[2,ρ0].
We want to know how far each Wj is from x, so we next bound the radii ρj (from below)
in terms of j and δ. If y ∈W0, then |x −y| ⩾2 by Lemma 3. For 1 ⩽j ⩽n, we claim
|x −y| > 2 + (j −1)δ for all y ∈Wj , except perhaps a set of measure 0. Suppose M
is a non-zero measure subset of W1 such that for all y ∈M, we have |x −y| ⩽2. Then
W0 ∪M ⊆Y[2] and ℓ[2] ⩾µ(W0) + µ(M) > µ(W0) = ℓ∗[2], which contradicts (9). We
continue using induction. Suppose for all 0 ⩽k < j ⩽n, we have |x −y| > 2 + (k −1)δ.
Suppose M is a non-zero measure subset of Wj such that for all y ∈M, we have
|x −y| ⩽2 + (j −1)δ. Then W0 ∪W1 ∪··· ∪Wj−1 ∪M ⊆Y[2,2 + (j −1)δ]. Thus,
πℓ

2,2 + (j −1)δ

⩾µ(W0) + µ(W1) + ··· + µ(Wj−1) + µ(M)
> µ(W0) + µ(W1) + ··· + µ(Wj−1)
= π

ℓ∗[2] + ℓ∗(2,2 + δ] + ···
+ ℓ∗2 + (j −2)δ,2 + (j −1)δ

= πℓ∗
2,2 + (j −1)δ
,
which contradicts (9).
Since Ydist = W0 ∪W1 ∪··· ∪Wn,
I x
dist =

y∈W0
1
|x −y|2 +

y∈W1
1
|x −y|2 + ··· +

y∈Wn
1
|x −y|2
< 1
22 ℓ∗[2] + 1
22 ℓ∗(2,2 + δ] + ··· +
1
(P −δ)2 ℓ∗(P −δ,P].
(10)
The ﬁrst term of (10) is 104
12 . The rest is
n

j=1
1
(2 + (j −1)δ)2 ℓ∗
2 + (j −1)δ,2 + jδ

,
which equals
E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
107
n

j=1
1
r2
j

4(rj + 1)2.r + 4(rj + 1).r2 + 4
3.r3

,
where rj = 2 + (j −1)δ and .r = δ. This is a Riemann sum for
 P
2
4(r+1)2
r2
dr plus terms
of higher order in .r whose contribution approaches 0 as .r →0. The bound (10) holds
for all choices of n, so as n →∞, we get
I x
dist ⩽104
12 +
P

2
4(r + 1)2
r2
dr = 8
3 + 4P −4
P + 8 ln(P) −8 ln(2).
We then multiply by L to get
Edist ⩽L

8
3 + 4P −4
P + 8 ln(P) −8 ln(2)

.
(11)
Combining (5) with (11) yields
EO4(K) ⩽L

8
3 + 4P −4
P + 8 ln(P) −8 ln(2)

+ 4.
(12)
We substitute P =  3
4L −3π
2 + 11/3 −1 to obtain our ﬁnal bound.
This bound is messy, but on the order of L4/3. We use a computer algebra system to plot
the bound divided by L4/3. The ratio achieves its maximum of ≈4.5626 near L = 1115.
Thus, for all L we have
EO4(K) ⩽4.57L4/3.
✷
For some values of L, in particular as L gets very large, the coefﬁcient 4.57 can be
further reduced. If 104
3 + 2π < L < 128 or L > 376,000, we have EO4(K) ⩽4L4/3. As L
tends to inﬁnity, the constant decreases to 3
1
3 4
2
3 ≈3.63.
