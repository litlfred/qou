---
doc_id: arxiv-2601.07906v2
doc_title: "March 2026 A universal sum over topologies in 3d gravity"
section_id: sec-011-handlebodies-are-not-sufficient
section_title: "Handlebodies are not sufficient"
section_number: null
pages: 41-46
source_pdf: 2601.07906v2.pdf
source_sha256: e69b1bf37f2c75b0
doc_brief: "March 2026 A universal sum over topologies in 3d gravity — We explore the sum over topologies in AdS 3 quantum gravity and its relationship with the statistical interpretation of the boundary theory."
---
Before introducing the gravitational machine in its full generality, we will just point
out two examples of conditions imposed in section 2 that fail to be satisfied by the
handlebody sum alone, showing that the handlebody sum is indeed insufficient.
Consistency between higher and lower genus.In section 3.4 we have seen
that the handlebody sum at genusgcontains information about the handlebody
sum at lower genus. For example, at genus 2 the sum over handlebodies (in the
sunset channel) contains as a subsum the elements of the formγ p1,q1◦γp2,q2◦F, recall
(3.50). Hereγ p,q is a modular transformation at genus 1, labeled by a pair of co-prime
integers that uniquely specify the PSL(2,Z)/Zelement. The sum over this subclass
of crossing transformations contributes as:
ρ1ρ2ρ3C123C∗
123⊃ρ MWK(h1, ¯h1)ρMWK(h2, ¯h2)

ρ0(h3)C0(h1,h 2,h 3)

2
.(4.1)
Hereρ MWK is the genus-1 handlebody sum (3.51), which is the full sum over on-shell
topologies contributing to the mean spectral density ¯ρ. As discussed in section 2.4,
– 41 –
if we ignore spectral correlations (associated to off-shell topologies in the bulk), the
above statistical moment should factorize as:
ρ1ρ2ρ3C123C∗
123 =ρ1ρ2ρ3C123C∗
123.(4.2)
Comparing to eq. (4.1), we see that the handlebody (sub-)sum correctly reproduces
the means ¯ρ1 =ρ MWK(h1, ¯h1) and ¯ρ2 =ρ MWK(h2, ¯h2), but fails to reproduce the
third mean spectral density ¯ρ3, giving only the leading Cardy densityρ 0(h3)ρ0(¯h3).
Intuitively, the reason is that the genus-2 mapping class group is too small to ac-
commodate three commuting copies of PSL(2,Z).
The set of topologies thatdoesfactorize into lower moments as in (4.2) is rather
easy to describe, and it necessarily includes non-handlebodies. We describe this set
using Dehn surgery: given a VTQFT diagram Γ (i.e. a network of Wilson lines), and
a regular neighborhoodN(Γ) embedded in a closed 3-manifoldM E, take an edge dual
to a non-contractible cycle inM E\N(Γ). Then carve out a solid torus enclosing this
edge and re-glue the solid torus after a modular transformationγ p,q. Pictorially:
P −→ P ∪ .(4.3)
The elementγ p,q maps the blue meridian on the right torus to a curve on the left
which winds around the meridianptimes and around the longitudeqtimes (in the
picturep= 3 andq= 1). For a curve with no self-intersectionspandqare coprime
integers, and the ordered pair written asp/qis in one-to-one correspondence with
the elements of PSL(2,Z)/Z.
In Virasoro TQFT, the above Dehn surgery procedure is described by the Ver-
linde loop operator [12, 14], as follows:
ZVir

 Pi
p/q

≡
Z ∞
0
dPK (p,q)
1P ZVir

 Pi
P

 (4.4)
=
Z ∞
0
dPK (p,q)
1P
SPPi[1]
S1Pi[1] ZVir
"
Pi
#
(4.5)
= 1
ρ0(Pi) K(−q,p)
1Pi ZVir
"
Pi
#
.(4.6)
HereK (p,q)
1P is the modular kernel forγp,q, implementing the Dehn surgery with surgery
coefficientp/q. In the second line we used the formula (C.31) for removing the
– 42 –
Verlinde loop, and in the third line we used the fact thatγ p,q◦S=γ −q,p under the
modular S-transform. The above manipulations can be done locally on any edge of
Γ, indicated as before by the dotted line.
To obtain the gravitational partition function from the above VTQFT compu-
tation, we multiply the fixed-Ppartition function (4.6) by the normalization factor
ρC
g (P)—which in particular contains a factorρ 0(Pi) for thei th edge—and then we
multiply by the right-moving counterpart. Finally, we sum over the co-primesp,q.
The net effect of this sum over Dehn surgeries is that the Cardy densityρ 0 gets
modular completed to the MWK spectral density:
ρ0(Pi)ρ0( ¯Pi)

 Pi
p/q

2
sum over
−−−−−−−→
co-primesp,q
ρ′
MWK(Pi, ¯Pi)

Pi

2
.(4.7)
Hereρ ′
MWK is the MWK handlebody sum (3.51) without the vacuum contribution,
i.e.ρ MWK =δ(h)δ( ¯h) +ρ′
MWK. In other words, we excluded the Dehn surgery with
(p,q) = (0,1), which projectsP i to the identity1. This corresponds to the case that
the surgery implements the action of the Ω-loop. In this way, the sum over Dehn
surgeries upgrades the heavy Cardy density to the heavy part of the MWK density,
leaving the identity contributions that are already part of the genus-ghandlebody
sum. Importantly, for complicated enough Dehn surgery coefficients, the manifolds
constructed by our procedure (4.6) can be non-handlebodies.
Let us see how this works in the genus-2 example discussed above. Dehn surgery
on the three internal lines of the sunset channel gives: 23
ρC
g=2(P)Z Vir


p2
q2
p1
q1
p3
q3
P2
P1 P3

 =K (−q1,p1)
1P1 K(−q2,p2)
1P2 K(−q3,p3)
1P3 C0(P1,P 2,P 3).
(4.8)
In section 5, we will identify the topology of the filling ( p1
q1
, p2
q2
, p3
q3
) = (2,2,2) with a
non-handlebody known as the twistedI-bundle [31], and ( p1
q1
, p2
q2
, p3
q3
) = (2,2,3) with
another non-handlebody called the5 2 handlebody-knot. In total, the sum over all
the surgery coefficients (pi,qi) contributes as:
ρ1ρ2ρ3C123C∗
123⊃ρ MWK(h1, ¯h1)ρMWK(h2, ¯h2)ρMWK(h3, ¯h3)

C0(h1,h 2,h 3)

2
,(4.9)
which is indeed of the factorized form (4.2). Although compatible with genus-1
modular invariance, the sum over Dehn surgeries itself still has to be completed by a
sum over the genus-2 mapping class group, which acts via crossing transformations on
the sunset diagram. The non-trivial interplay between crossing and the factorization
(4.2) into lower moments will be explained in more depth in section 4.2.
23Here we used the sunset normalization factorρ C
g=2(P) =ρ 0(P1)ρ0(P2)ρ0(P3)C0(P1,P 2,P 3)2,
as well as (3.22) for evaluating the sunset diagram in VTQFT.
– 43 –
Typicality.As a second constraint that is not satisfied by the handlebody sum, we
give an example of a violation of the typicality condition discussed in section 2.3. As
explained there, typicality predicts extra terms contributing to statistical moments
with repeated pairs of indices, such as C113C113. On the level of distributions, this
means there are delta-function contributions such as:
ρ1ρ2ρ3C123C∗
123⊃
δ2(h1−h 2)ρ1ρ3

(1 + (−1)J3)GS

1 1 3

+GD

1
3
1

.(4.10)
This is an example of a term for the index contractionδ 12, which, since we are
integrating over densities, has been represented by the Dirac deltaδ 2(h1−h 2)≡
δ(h1−h 2)δ(¯h1− ¯h2). In some cases, these delta-function contributions may be ac-
counted for in the bulk by handlebodies, but in general we require non-handlebodies
to account for all index contractions.
For example, (4.10) receives a contribution from the following handlebody:
1
2
3
′
.(4.11)
Here we drew the linked dumbbell from the previous section (with the opposite over-
under crossing), where one of the bells is in the S-dual channel as indicated by the
prime. We can check that this indeed produces the desired delta function by using
the Ω-loop defined in (3.60) to implement the S-transform:
ZVir


1
2
3
′

 =Z Vir


1
2
3Ω

 = δ(P1−P 2)
ρ0(P2) ZVir

 1 1 3

.(4.12)
Here we used the VTQFT identity (C.38) for the Ω-loop encircling two Wilson lines.
We can also directly use the VTQFT partition function for the linked dumbbell
computed in (3.30), together with the fact thatSis unitary:
Z ∞
0
dPS P1P [P3]ZVir


P
2
3

 =
Z ∞
0
dPS P1P [P3] SPP 2[P3]∗
ρ0(P2)C0(P2,P 2,P 3) (4.13)
= δ(P1−P 2)
ρ0(P2)C0(P2,P 2,P 3).(4.14)
Multiplying by the normalization factorρ g=2(P) and the anti-holomorphic counter-
part, we see that this handlebody contributes in the following way:
ρ1ρ2ρ3C123C∗
123⊃δ 2(h1−h 2)|ρ 0(h1)ρ0(h3)C0(h1,h 1,h 3)|2.(4.15)
– 44 –
There is also the handlebody with the opposite over-under crossing of the linked
handles, which gives an extra phase factor e −πih3, as already remarked in (3.33).
This accounts for the (−1)J3 contribution to the moment (4.10).
Even though handlebodies account for some of the contractions predicted by
typicality, not all of the contractions can be explained by the handlebody sum alone.
For example, the enhancement in (4.10) by the dumbbell termsG D consists of non-
handlebody contributions, as we will see in section 5. A simpler example is given by
the double contractionδ 12δ23, recall (2.24), which contributes to the second moment
when all indices coincide, CiiiCiii. Whenh i ̸=1, the only contributions to this
moment come from non-handlebodies. In fact, the simplest contribution comes from
a so-calledhandlebody-knot, whose VTQFT diagram can be drawn as:
′ ′
2
31 .(4.16)
If we take this knotted graph and embed it in S3, its complement is a non-handlebody
with genus-2 boundary. It is the handlebody-knot with the least number of over-
under crossings, called the4 1 handlebody-knot in the classification of [90]. The
primes indicate that we additionally perform an S-transform on the two bells. Let
us check that this manifold produces the desired delta functions for the double con-
traction:
ZVir


′ ′
2
31

 =Z Vir

 Ω Ω
2
1
3

 (4.17)
= δ(P1−P 2)
ρ0(P2)
δ(P2−P 3)
ρ0(P3) ZVir

 1 1 1

.(4.18)
Multiplying by the normalization factor and the anti-holomorphic counterpart, we
confirm that this non-handlebody is the leading contribution to the double index
contractionδ 12δ23 at genus two:
ρ1ρ2ρ3C123C∗
123⊃δ 2(h1−h 2)δ 2(h2−h 3)|ρ 0(h1)C0(h1,h 1,h 1)|2.(4.19)
This example shows that non-handlebodies like4 1 are needed for consistency with
typicality. Since a non-handlebody always remains a non-handlebody after crossing
transformations, all of the mapping class group images of (4.16) (which are needed
to complete (4.19) into a crossing symmetric density) are also non-handlebodies.
Moreover, it may be further modified by Dehn surgery to upgradeρ 0 toρ MWK.
In the next subsection, we will take the two examples studied above as the basis
for an algorithm for generating 3-manifolds, which we call the ‘gravitational machine’.
– 45 –
