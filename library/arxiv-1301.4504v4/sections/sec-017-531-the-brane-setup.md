---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-017-531-the-brane-setup
section_title: "The Brane Setup"
section_number: 5.3.1
pages: 46-48
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
To quantitatively test the feasibility of using a throat to evade the computational hard-
ness of decoding, we need a speciﬁc example of this type of geometry. In string theory
there is a standard way of producing throat geometries with the desired properties
by stacking branes; for example D3 branes in type IIB string theory or M5 branes
in M-theory. To realize the geometry (5.10) explicitly we would need a conﬁguration
of branes which is spherically symmetric and stable. Spherical symmetry is a bit in-
convenient because branes in spherical conﬁgurations tend to collapse under their own
tension unless there is something else supporting them. A simple thing we could do
is start with the AdS3×S3×T 4 solution of IIB supergravity with RR ﬂux, itself the
near horizon limit of the D1−D5 system, and then wrap some D3 branes on the S3.
This throat would not be asymptotically Minkowski, but we could easily arrange for
the curvature radius of the AdS3 to be much larger than the curvature radius of the
AdS5 near the D3 branes. Rather than try to make this construction work in detail,
we will instead consider a simpler setup in which the black hole has planar symmetry
instead of spherical symmetry.
One of the best-known solutions of ten-dimensional IIB supergravity is the extremal
planar black 3-brane [80], with metric
ds2 =Z(r)−1/2(
−dt2 +d⃗ x2)
+Z(r)1/2(
dr2 +r2dΩ2
5
)
. (5.17)
Here
Z(r) = 1 +
(R
r
)4
, (5.18)
and R is a parameter of the solution. The string theory interpretation of this solution
is that it gives the backreacted geometry in the presence of N D3 branes, with
R4 = 4πgN𝓁 4
s∼N𝓁 4
p (5.19)
– 45 –
where g is the string coupling, 𝓁s is the string length, and 𝓁p is the ten-dimensional
Planck length. By looking at Z(r) we see that this geometry indeed has the property
that for r≪ R it behaves like AdS5 in Poincar´ e coordinates, times an extra S5 of
constant radius, while for r≫R it becomes ten dimensional Minkowski space.
To get something like a black hole down the throat we need to put this solution
at ﬁnite temperature, and to get the entropy to be ﬁnite we need to compactify the
spatial ⃗ xdirections. Although it will not be explicit in our equations, we will choose
anti-periodic boundary conditions for the fermions around the compact dimensions. 35
To add some temperature we just need to consider the non-extremal version of the
solution [81]:
ds2 =Z(r)−1/2(
−f(r)dt2 +d⃗ x2)
+Z(r)1/2
( dr2
f(r) +r2dΩ2
5
)
, (5.20)
where Z(r) is now
Z(r) = 1 +λ
(R
r
)4
, (5.21)
with
λ =
√
1 + 1
4
(r0
R
)8
− 1
2
(r0
R
)4
(5.22)
and
f(r) = 1−
(r0
r
)4
. (5.23)
To put the black hole far down the throat we clearly want r0
R≪ 1, and in this limit
the entropy of the black hole is
S = Ω5L3r3
0R2
4G ∼ L3r3
0R2
𝓁8
p
(5.24)
and the temperature is
T = 1
π
r0
R2. (5.25)
35The reason for this choice is that compactifying with periodic boundary conditions preserves
supersymmetry, which introduces an instability of the throat. Supersymmetry ensures there is no
potential energy cost for separating the D3 branes that make up the throat. In CFT language the
dual gauge theory is unable to pick a vacuum and its zero modes wander freely on its moduli space.
Antiperiodic boundary conditions break supersymmetry and generate a potential that keeps the branes
together. We thank Igor Klebanov and Juan Maldacena for discussions of this point.
– 46 –
Here Ω5 is the volume of a unit S5 and L is the periodicity of the ⃗ xdirections. In the
same limit the ADM energy 36 is
EADM = Ω5L3
4πG
(
R4 + 3
2r4
0
)
. (5.26)
One can check that when r0→ 0 this reproduces the correct D3-brane tension. The
energy above extremality is
E = 3Ω5L3r4
0
8πG ∼ L3r4
0
𝓁8
p
. (5.27)
It is straightforward to check that the instability encountered in Reissner-Nordstrom
does not happen here; in fact we have
E = 3
2ST, (5.28)
so the energy will be bigger than the temperature until the black hole has Planckian
area. We may then worry that the black hole evaporation time is independent of
the intial entropy, as we worried with Reissner-Nordstrom, but there is now a new
phenomenon which comes to the rescue.
