---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-018-532-hawking-page-transition-for-toroidal-black-h
section_title: "Hawking-Page Transition for Toroidal Black Holes"
section_number: 5.3.2
pages: 48-50
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
For spherical black holes in AdS with metric (5.10), it is well known [83, 84] that for
small enough values ofα the black hole is unstable to decay by Hawking radiation. The
crossover point is when the temperature is of order R−1.37 This phenomenon provides
a natural endpoint for the type of decay we discussed in the previous section; the black
hole will very slowly radiate energy up the throat and into Minkowski space until it
reaches the critical temperature, after which it will decay essentially immediately into
low energy quanta in the AdS-region of the throat. Does something similar occur for
our toroidal black hole as well? The answer is yes, but as we now describe the analysis
has a few details that diﬀer from the spherical case. This transition has been previously
discussed by [85].
36For an asymptotically ﬂat geometry, in coordinates where the metric is ηµν +hµν withhµν small,
the ADM energy is deﬁned [82] as lim r→∞ 1
16πG
∫
dAni
(
∂jhij−∂ihj
j
)
. Here the integral is over the
S5× T3 at inﬁnity.
37More carefully this is the temperature below which the black hole no longer dominates the thermal
ensemble. In the microcanonical ensemble the energy below which a single black hole is actually
unstable is lower by some power of R/𝓁p, but this distinction will not be important for us for reasons
we explain below. We thank Juan Maldacena for explaining this distinction to us.
– 47 –
Far down the throat, our geometry becomes a compactiﬁed version of a general
solution called a black AdS brane. In AdSd the metric for this solution is 38
ds2 =r2(
−f(r)dt2 +d⃗ x2)
+ dr2
r2f(r), (5.29)
with
f(r) = 1− α
rd−1. (5.30)
In the spherical case the action of the Euclidean version of the solution (5.10) can
be compared to the action of another Euclidean solution which has the form (5.10)
again but with α = 0. In both cases the Euclidean time τ = it is compactiﬁed. The
competition between these two solutions is the source of the Hawking-Page transition.
In the toroidal setting there is an analogous construction of a second solution, where
we set α = 0, but it turns out always be subdominant to the black brane solution
(5.29). There is another solution however with the same boundary conditions; we can
take the “emblackening factor” f(r) and move it from in front of −dt2 to one of the
planar coordinates:39
ds2 =r2(
−dt2 +f(r)dx2 + (d⃗ x⊥)2)
+ dr2
r2f(r). (5.31)
This geometry is sometimes called the AdS Soliton. It has no region behind the “hori-
zon” at r =r0, instead it caps oﬀ smoothly provided that we choose the correct value
of r0 as a function of the periodicity L. When we continue to Euclidean time we can
set the τ periodicity of the AdS soliton (5.31) freely, but for the black brane (5.29) we
must choose r0 to be consistent with the τ periodicity for the Euclidean geometry to
be smooth. An important subtlety is that for a given periodicity of the circle at the
boundary, the correct value of r0 and also the coordinate periodicity of τ are diﬀerent
in the two solutions. 40 The Euclidean action is
S =− 1
16πG
(∫
ddx√−g (R + (d− 1)(d− 2)) + 2
∫
dd−1x√γK
)
, (5.32)
where γ is the determinant of the induced metric at the boundary and K is the trace
of the extrinsic curvature. Making the action ﬁnite involves cutting oﬀ the geometry at
some larger =rc, and then carefully matching the boundary geometry on the regulator
38In this section we set the AdS radius R to one.
39Had we chosen supersymmetric boundary conditions in the spatial directions this solution would
not exist.
40Actually in Euclidean signature they are really just the same solution with diﬀerent parameters,
so the calculation only needs to be done once.
– 48 –
surface in the two cases. We will not present the details explicitly here since they are
fairly standard in the literature. (See [84, 86] for examples.) The result is that the
ﬁnite parts of the actions are
−SBB = 1
16πG
( 4π
d− 1
)d−1
(LT )d−2 (5.33)
for the black brane and
−Ssol = 1
16πG
( 4π
d− 1
)d−1
(LT )−1 (5.34)
for the AdS soliton. Thus at high temperatures compared to L−1 the black brane wins
while at low temperatures the AdS soliton wins. This then is the eﬀect that we want;
as the black hole radiates it will eventually undergo a transition to some other type
of geometry with no horizon and Alice will no longer be able to test AMPS. The dual
ﬁeld theory interpretation of this is clear; it is the same large N phase transition as in
the spherical case, just studied with diﬀerent spatial topology. 41
