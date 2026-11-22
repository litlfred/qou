---
doc_id: arxiv-hep-th-9306069v2
doc_title: "The stretched horizon and black hole complementarity"
section_id: sec-003-3-the-stretched-horizon
section_title: "The stretched horizon"
section_number: 3
pages: 18-34
source_pdf: 9306069v2.pdf
source_sha256: a140d10424f73233
toc_source: inferred
doc_brief: "The stretched horizon and black hole complementarity — Three postulates asserting the validity of conventional quantum theory, semi-classical general relativity and the statistical basis for"
---
Our postulates require us to build a theory in which a distant observer makes no reference
to events inside a black hole. For this purpose it is very useful to introduce the idea of a
stretched horizon, HS, which is a visible timelike curve, in front of the global event horizon of
the black hole. Each point on HS is identiﬁed with a point on HG, so the stretched horizon
can act as a “surrogate” for the global horizon in a phenomenological description of black
hole evolution.
3.1. Definition and properties of the classical stretched horizon
We deﬁne the classical stretched horizon as follows. Consider the classical area function
(2.2) along the global event horizon.
For a black hole formed by gravitational collapse,
depicted in Figure 3, this area increases with y+ until the black hole has settled to its ﬁnal
size. We deﬁne the stretched horizon by mapping each point m on the event horizon back
along a past-directed null line (away from the event horizon itself) to a point p at which
A(p) = A(m) + δ ,
(3.1)
where δ is an arbitrary small constant.
This results in a timelike curve as indicated in
Figure 5.
18
singularity
ι+
R
ι−
L
ι−
R
event horizon
black hole
m
stretched horizon
p
ι+
L
FIGURE 5. Construction of the classical stretched horizon.
Note that our deﬁnition diﬀers from that given in [9].
There the shift in the area
between the global event horizon and the stretched horizon scales like the horizon area
itself.
For a massive black hole our stretched horizon is thus much closer to the event
horizon.
Our deﬁnition is better suited for the semi-classical theory of two-dimensional
gravity considered here, and may also be appropriate for the quantum description of black
holes in four spacetime dimensions. For the classical black hole solutions (2.17) one ﬁnds
the remarkably simple result that in Kruskal coordinates the stretched horizon curve is
independent of the incoming energy ﬂux, T++(y+), and the curve is given by
−y+y−= δ .
(3.2)
The simplicity of the stretched horizon becomes even more apparent in the tortoise
coordinates (2.20). While the event horizon lies at t = ∞and σ = −∞, the stretched
horizon is at ﬁxed spatial position
σS = 1
2 log δ .
(3.3)
Thus the stretched horizon can receive and emit signals. Furthermore, to distant observers,
19
clocks at the event horizon appear inﬁnitely slowed while they appear to run at a ﬁnite rate
at the stretched horizon. For an eternal black hole of mass M0, proper time τ along HS is
related to coordinate time t by
dτ =
r
δ
M0+δ dt .
(3.4)
Finally, one can consider the Hawking temperature of a massive two-dimensional dilaton
black hole, T =
1
2π, which is independent of the mass. Since temperature has units of energy,
then in proper time units at the stretched horizon the temperature is
TS = 1
2π
dt
dτ = 1
2π
r
M0+δ
δ
.
(3.5)
From (3.5) it appears that the local temperature at the stretched horizon increases with
M0. This is a bit misleading, because the analogue of the Planck length in two-dimensional
dilaton gravity depends on the local value of the dilaton ﬁeld, according to lpl ∼eφ. At the
stretched horizon, the dilaton ﬁeld satisﬁes e−φ = √M0+δ, so (3.5) implies that, measured
in Planck units, the temperature at the stretched horizon is independent of the mass. This
result also holds for four-dimensional black holes as we will see in section 5.1.
Let us continue examining the classical behavior of the stretched horizon. Consider the
evolution of the area A on HS. Parametrizing HS by y+ and substituting the deﬁnition (3.2)
of HS into the gravitational collapse solution (2.17) we ﬁnd
AS(y+) = M(y+) + δ −y+(P+(y+) −P∞)
(3.6)
which, when diﬀerentiated twice, gives
d2AS
(dy+)2 = −T++(y+) .
(3.7)
Transforming to tortoise coordinates, one can parametrize HS by the tortoise time t =
log y+ −1
2 log δ. Equation (3.7) then becomes
d2AS
dt2
−dAS
dt
= −
dy+
dt
2
T++(y+) ≡−T++(σ+)
(3.8)
where the quantity T++(σ+) is the incoming physical ﬂux of energy as seen by a distant
observer. There are two interesting features of (3.8). The ﬁrst has to do with the nature of
20
the boundary conditions on the solutions of the equation. In general, the stretched horizon
will begin to grow even before any energy crosses it. From (3.8) we see that before T++
becomes nonzero, AS has the solution
AS(t) = Cet .
(3.9)
The choice of the constant C is dictated by ﬁnal conditions. As t →∞, a black hole is
present with mass M∞. The area of the stretched horizon of such a black hole is
lim
t→∞AS(t) = M∞+ δ ,
(3.10)
and thus (3.10) is the boundary condition one must impose on the solution of (3.8). This
means that the initial state of the stretched horizon must be tuned in conjunction with
the incoming matter distribution so that (3.10) is satisﬁed. This strange feature has been
referred to in the membrane paradigm literature as the “teleological boundary condition”
[9]. We will show in section 3.4 how the equations can, in fact, be given a more conventional
and causal interpretation.
The second interesting feature of (3.8) is the dissipative term dAS
dt . It breaks time reversal
symmetry much like a friction term in ordinary mechanics. The presence of dissipative terms
in mechanics is generally associated with the production of heat and the increase of thermal
entropy. In the classical case, the temperature of the black hole is zero, but in the semi-
classical case the temperature increases when the black hole is formed, and the stretched
horizon appears to radiate like a thermally excited black body.
In the limit of large black holes, we can also consider the theory of a massless matter
ﬁeld f propagating in the black hole background. We ﬁnd that the equations governing
the matter ﬁelds interacting with the stretched horizon also exhibit dissipation. In the case
of a four-dimensional black hole interacting with electromagnetic ﬁelds, the phenomenon
of dissipation is described by attributing an ohmic resistance to the membrane. A similar
description can be given for two-dimensional dilaton black holes. Indeed, the theory of a
massless ﬁeld f bears a useful resemblance to ordinary classical electrodynamics, with f
playing the role of the vector potential. We work in the tortoise coordinates (2.20) and
21
deﬁne the “electric” and “magnetic” ﬁelds E and B by
E = −∇tf,
B = ∇σf .
(3.11)
The equation of motion for the f ﬁeld is
∇2f = −4πJ
(3.12)
where we have introduced a source j. Writing this equation in terms of the ﬁelds E and B,
we obtain an inhomogeneous “Maxwell” equation
∇tE + ∇σB = −4πJ .
(3.13)
We can also obtain the homogeneous “Maxwell” equation ∇σE + ∇tB = 0.
Now we consider the interaction of the f ﬁeld with the stretched horizon, which, from
the point of view of an external observer, is a boundary absorbing all incoming waves. This
behavior can be modeled by attributing a resistance to the stretched horizon,
∇tE + ∇σB = −4πρ−1
S δ(σ−σS) E .
(3.14)
An incoming f wave will be completely absorbed if and only if ρ = 4π. This is the analogue
of the surface electrical resistivity of a four-dimensional black hole. The power absorbed
by the stretched horizon is ρ−1
S (∂tf)2, which can be thought of as ohmic heating. When
quantum corrections are included, the heat is radiated back as Hawking radiation.
3.2. The semi-classical stretched horizon
In deﬁning the stretched horizon of a semi-classical black hole, we ﬁnd it more convenient
to refer to the ultimate horizon at y−= 0 than the event horizon (2.41). For a large black
hole, the diﬀerence is negligible. We also replace the classical area function (2.2) by its semi-
classical counterpart (2.35). This leads to the following condition for points on the stretched
horizon:
−y+y−−κ
4 log

1 −y−
P∞

= δ ,
(3.15)
where we have used the black hole solution (2.39). If the incoming energy is large, then y−
P∞
will be very small on HS, except in the extremely early stages of its evolution. Thus, we will
22
drop the log term in the deﬁnition. In the classical case, δ is an arbitrary small number. In
the semi-classical theory, there is a natural choice, δ = κ
4, for which the area of the stretched
horizon vanishes in the asymptotic past and future when there is no black hole. This implies
that the stretched horizon will coincide with the boundary curve γcr in these limits. Thus,
we deﬁne the stretched horizon to be the set of points satisfying the condition
−y+y−= κ
4 .
(3.16)
In tortoise coordinates, the stretched horizon is given by the curve
ˆσS(t) = 1
2 log
κ
4

= σS .
(3.17)
Let us now consider the black hole evolution in tortoise coordinates as shown in Figure 6.
The incoming ﬂux is assumed to be vanishing outside the interval 0 < σ+ < τ. For y+ < 1,
i.e. σ+ < 0, we have the initial linear dilaton vacuum and the boundary curve is given by
ˆσcr(t) = log
P∞et
2
hs
1 + κe−2t
P 2∞
−1
i
.
(3.18)
In the remote past, this curve tends to
ˆσcr(t) →σS −P∞
√κet .
(3.19)
We see that the boundary begins to separate from the stretched horizon at a time
t∗= −log P∞+ 1
2 log κ .
(3.20)
The incoming matter arrives at the stretched horizon at a time t0 = −σS. Consequently,
we see a period of time ∼log P∞during which the boundary moves in anticipation of the
infalling matter. It continues to move toward σ = −∞with a velocity which approaches
that of light.
23
A second boundary curve passes through the naked singularity at the endpoint of the
black hole evaporation. Behind the stretched horizon the second boundary curve is space-like
and coincides with the curvature singularity. This is shown in Figure 6. The semi-classical
viewpoint is that the infalling matter becomes trapped between these boundary lines and
disappears into a spatially disconnected region. However, our postulates do not require us
to pay any attention to this region, as it lies behind the stretched horizon.
incoming
  matter
γcr
σ=σS
HS
Hawking
radiation
γcr
HG
E
t0+τ
t0
t*
FIGURE 6. Black hole evolution in tortoise coordinates.
Now let us turn to the outgoing Hawking radiation. Using the (−−) constraint equation
(2.34), one ﬁnds the outgoing Hawking ﬂux
T−−(t, σ) = κ
4
h
1 −
1
(1 −P∞e(t−σ))2
i
Θ(tE −t + σ −σS) ,
(3.21)
where
24
tE = log (e
4
κM∞−1) −log P∞+ σS
≈4
κM∞−log P∞+ σS .
(3.22)
The outgoing ﬂux has its leading, albeit somewhat fuzzy, edge along the null curve
σ −t ≈log(P∞) .
(3.23)
Tracing this line back to the stretched horizon we ﬁnd that it intersects the stretched horizon
at the time
t∗= t0 −log P∞.
(3.24)
If we interpret the outgoing thermal radiation as originating on the stretched horizon, it
begins at a time well before the incoming matter arrives. For early times, the semiclassical
area of the stretched horizon is approximately
AS ≈1
2P 2
∞e2t .
(3.25)
The radiation begins just as the area of the stretched horizon begins to increase. The radiation
has turned on by the time the area (and entropy) of the stretched horizon have increased to
their values at t∗, given by A∗≈κ
8.
The correspondence between the onset of Hawking radiation and the excitation of the
stretched horizon is unexpected.
From a strictly local point of view, nothing special is
happening at this point.
It is straightforward to generalize the equation (3.8) governing the evolution of the area
of the stretched horizon. Using (2.39) and (3.16) and parametrizing HS by y+, we ﬁnd
AS(y+) = M(y+) −y+[P+(y+) −P∞] + κ
4(1 −log(κ
4 + y+P∞)) .
(3.26)
Diﬀerentiating twice with respect to y+ and transforming to tortoise coordinates gives
d2AS
dt2
−dAS
dt
= −T++(t, σS) + κ
4
h
1
(1 +
κ
4P∞exp[−(σS−t)])2
i
.
(3.27)
Once the stretched horizon area is signiﬁcantly greater than κ
4, the second term on the right
25
hand side can be simpliﬁed to κ
4, giving
d2AS
dt2
−dAS
dt
= −T++(t, σS) + κ
4 .
(3.28)
The second term on the right hand side of (3.28) represents the eﬀects of the outgoing
Hawking radiation on the evolution of AS. For example, we see that a stationary solution
is possible if T++(σ+) = κ
4. In this case, the incident energy ﬂux is just suﬃcient to balance
the outgoing thermal radiation. In section 4, we will see that things are somewhat more
complicated, and that AS has a brownian motion superimposed on its average motion.
Let us now review the process of formation and evaporation as seen by a distant observer
using tortoise coordinates. The infalling matter is scheduled to begin passing the stretched
horizon at time t0. However, well before this, at time t0 −log P∞, the stretched horizon
begins to separate from the boundary, and its area increases by an amount of order κ
8.
Assuming the standard connection between entropy and area, this is the point at which the
stretched horizon becomes thermally excited. The distant observer sees the onset of Hawking
radiation originating from this point. At the time t0, the infalling matter is swallowed behind
the stretched horizon, which continues to radiate. If we assume that there are microphysical
degrees of freedom which underlie the thermodynamic description, t0 is the ﬁrst opportunity
for them to feel the infalling matter. Therefore, at least for the initial time of order log P∞,
no information can be stored in the Hawking radiation [4].
After the infalling matter is absorbed, the area begins to decrease. The acceleration
term in (3.28) goes to zero, and AS satisﬁes
dAS
dt
= −κ
4 .
(3.29)
The area, entropy, and mass of the black hole tend linearly to zero. The entire process from
t0 to the endpoint at which AS returns to its initial value takes a time t ≈4M
κ , during
which a constant ﬂux of Hawking radiation is emitted by the stretched horizon.
As we
shall see in section 4, the entire semi-classical evolution is accompanied by random brownian
ﬂuctuations, which introduce an uncertainty of order
√
M to the lifetime of the process.
26
3.3. Incident flux below the black hole threshold
We now consider the case in which the incident energy ﬂux remains below the critical
value κ
4 for all time. The resulting geometry and outgoing ﬂux of radiation was obtained in
[24]. Here we will transcribe some of those results into tortoise coordinates. Assume that
the incoming energy ﬂux T++(σ+) vanishes outside the interval 0<σ+<τ. The time-like
boundary curve γcr is obtained by solving the equations of motion (2.33) subject to the RST
boundary conditions (2.42). In tortoise coordinates, γcr satisﬁes the following equation:
eˆσcr(t) −κ
4e−ˆσcr(t) = −
∞
Z
ˆσcr(t)
dse−sT++(t + s) .
(3.30)
incoming  matter
γcr
σ=σS
t*
tf
FIGURE 7. Sub-critical ﬂux of incident matter.
As in the black hole case, in the remote past the boundary curve tends to a ﬁxed spatial
position,
σS = 1
2 log
κ
4

,
(3.31)
27
which we will continue to call the location of the stretched horizon, even though no black
hole is formed. The boundary begins to move exponentially in anticipation of the incoming
matter, as it did in the black hole case, but this time γcr remains time-like throughout the
evolution, and eventually returns to the stretched horizon at the time tf = τ −σS. This is
shown in Figure 7.
The outgoing ﬂux is obtained by applying the following reﬂection conditions [24]:
T−−(σ−) −κ
4 =
 dˆσ+
cr
dσ−
2 
T++(ˆσ+
cr) −κ
4

,
(3.32)
where ˆσ+
cr(σ−) denotes the boundary curve γcr parametrized by σ−. Note that this prescrip-
tion for reﬂecting energy ﬂux does not involve boundary conditions imposed directly on the
matter ﬁelds.
It is instructive to consider a constant incoming energy ﬂux, T++(σ+) = T, of duration
τ. The early time behavior of the boundary curve is given by
ˆσcr(t) = σS −P∞
√κ et .
(3.33)
The boundary curve continues to recede from the stretched horizon until the incoming ﬂux
intersects γcr, as shown in Figure 7. If T is much smaller than κ
4, the boundary curve never
moves appreciably away from the stretched horizon, but if T is close to κ
4, γcr moves deep
into the region of negative σ. The maximum coordinate distance between γcr and HS is
σmax = 1
2 log
 κ
4 −T(1−e−τ)

,
(3.34)
which occurs at time tmax = −σmax. After that the boundary curve begins to return to the
stretched horizon. How fast it returns depends on the parameters T and τ. In the limit of
very long duration of the incoming energy ﬂux, τ ≫1, the boundary remains practically
stationary for a long time at its maximum distance, but eventually it returns and arrives
back at the stretched horizon at time tf = τ −σS. If, on the other hand, the duration of the
incoming energy ﬂux is relatively short the boundary curve rapidly returns and approaches
HS with a velocity
v ≈
T
κ
2 −T .
(3.35)
When the incoming energy ﬂux goes to the critical value, κ
4, this velocity approaches the
speed of light.
28
In [24], it was speculated that the critical boundary might behave like a moving mirror
reﬂecting the fi ﬁelds. We can now see that this can only be consistent in the limit of small
incoming energy ﬂux, T ≪κ
4. For if T ≈κ
4, the incoming radiation would be met by a
very relativistic mirror, which would greatly blueshift the reﬂected radiation. In addition,
accelerated mirrors create incoherent quantum radiation of net positive energy. The result
would be far more energy output than the total incoming energy. It is therefore clear that
only a tiny fraction of the incident energy can be coherently reﬂected by the boundary when
T ≈κ
4.
The outgoing ﬂux of energy can be calculated from (3.32) and one ﬁnds that almost all
the energy is radiated back before the incoming signal could have been reﬂected from the
boundary curve γcr. The following odd rule gives a better account of the energy output
as determined by the RST boundary conditions in the case T ≈κ
4: assume that at time
t∗= −log P∞
√κ, when the boundary curve γcr separates from HS, the stretched horizon
becomes thermally excited to a temperature T ≈
1
2π. Assume that the hot horizon emits
thermal radiation at a ﬁxed rate until time tf. The total radiated energy will be
Eout ≈κ
4(tf −t∗) ,
(3.36)
which accounts for about the right amount of energy output. We will provide further moti-
vation for this alternate viewpoint in the following subsection.
Another interesting point concerns the fate of the conserved charges associated with the
global O(N) symmetry of the matter ﬁelds. Only when the energy ﬂux T is much less than κ
4
can the boundary curve consistently behave like a mirror, reﬂecting both the energy and the
conserved charges. When T ≈κ
4, almost all the energy is radiated before the charges have
an opportunity to reﬂect. If a large total charge of order (tf−t∗) came in and was reﬂected,
it would have to be carried by a small energy, of order κ. In other words, it would have to
be carried out in the form of quanta with energy of order
κ
(tf−t∗) which would take a very
long time. It is easy to see, however, that as T approaches κ
4, the reﬂected region does not
spread out as it would have to if it were composed of quanta of ever lower energy. Therefore,
only a small amount of conserved charge can be reﬂected. In addition to thermalizing the
incident energy, the process must also destroy the conservation of quantum numbers.
Another failure of the boundary to behave like a mirror can be illustrated by considering
an interruption in an otherwise uniform incoming ﬂux – a glitch. If the boundary behaved
29
like a mirror, a brief, sharp interruption would be expected in T−−where the glitch reﬂects
oﬀthe boundary, but an explicit calculation shows that this is not the case.
3.4. A causal description of the stretched horizon
Our aim is a self-contained description of black hole evolution as seen by a distant
observer in which no reference need be made to events behind the stretched horizon. It will
also become clear that such a formulation has signiﬁcant advantages in the low energy sector,
compared to a semi-classical description which focuses on boundary conditions imposed at
the boundary curve γcr. In particular, the stretched horizon oﬀers a uniﬁed view, in which
it is no longer necessary to treat the cases of large and small incident energy ﬂux separately.
We saw earlier that the stretched horizon begins to expand in what appears to be a
teleological manner before the incoming matter arrives. One might be concerned that this
would preclude a conventional causal Hamiltonian description of the quantum stretched
horizon. We do not believe this to be the case. From a formal point of view, the cause of the
horizon expansion is a gravitational dressing which is attached to the incoming energy ﬂux.
Consider the initial state description in tortoise coordinates. Suppose an incoming ﬂux of
energy is described by T++(σ+). The functions P+ and M are given in tortoise coordinates
by
P+(σ+) =
σ+
Z
−∞
du e−u T++(u) ,
M(σ+) =
σ+
Z
−∞
du T++(u) ,
(3.37)
and the ﬁeld Ωis given by
Ω= e2σ +

P∞−P+(σ+)

eσ+ + M(σ+) −κ
4

σ+ + log(P∞+ e−σ−)

(3.38)
Let us subtract from Ωthe functional form Ωwhich it would have in the absence of any
incoming matter,
Ω= e2σ −κ
2σ .
(3.39)
30
We obtain
ω ≡Ω−Ω= ωin(σ+) + ωout(σ−) ,
(3.40)
where
ωin(σ+) =
 P∞−P+(σ+)

eσ+ + M(σ+) ,
ωout(σ−) = −κ
4 log
 1 + P∞eσ−
.
(3.41)
We see that the free ﬁeld ω consists of an incoming part and an outgoing part. We can use
the outgoing ω ﬁeld to determine the outgoing energy-momentum ﬂux.
Since the incoming part is completely determined by the incoming energy ﬂux, we will
consider it to be a “dressing” of the incoming matter. It can be written
ωin(σ+) =
Z
du T++(u) W(σ+ −u) ,
(3.42)
where
W(σ+ −u) = Θ(u −σ+)e(σ+−u) + Θ(σ+ −u) .
(3.43)
In other words, a bit of energy δM arriving along the curve σ+ = u must be accompanied
by an ω dressing which has the value W(σ+ −u) δM. The ω dressing precedes the incoming
fi ﬂux, and is the ﬁrst thing that strikes the stretched horizon. By time reversal symmetry,
a bit of outgoing energy δM departing along the curve σ−= v also has an ω dressing given
by W(v −σ−) δM.
In a complete quantum theory, the outgoing state would be described by a vector in
the physical state space of fi-particles, from which it would be possible to compute the
expectation value of T−−. This would not be feasible, however, even if we knew the exact
nature of the microstructure of the stretched horizon. As we shall now see, thermodynamic
arguments can give information about ωout, which is suﬃcient to compute T−−.
The ω dressing of the incoming matter satisﬁes
(∂+ −∂2
+) ωin(σ+) = T++ .
(3.44)
By time reversal we obtain a relation between ωout and T−−:
(∂−+ ∂2
−) ωout(σ−) = −T−−.
(3.45)
31
This can be written as a condition at the stretched horizon,
dωout
dt
= −T−−
 t, ˆσS(t)

−d2ωout
dt2
(3.46)
The outgoing thermal ﬂux T−−is assumed to originate at the thermally excited stretched
horizon. The entropy of the stretched horizon is given by ω = ωin+ωout, since at the stretched
horizon, ω = A.
In thermal equilibrium, T−−should be a well-deﬁned function of the thermodynamic
state of the stretched horizon, and thus of the entropy ωS.
More generally, for non-
equilibrium processes such as the onset and end of Hawking evaporation, the ﬂux may
depend on the detailed time history. Nevertheless, we will consider a simpliﬁed model in
which T−−depends only on the instantaneous value of ωS, and the sign of its time derivative.
In other words, we shall allow for the possibility that T−−(ω) has diﬀerent functional forms
at the beginning and end of the evaporation. Thus, we assume the radiated ﬂux is a function
of ω,
T−−= T−−(ω) = T−−(ωin + ωout) .
(3.47)
Substituting this into (3.46) gives
˙ωout + ¨ωout = −T−−(ωout + ωin) .
(3.48)
Since ωin(t) is known in terms of T++, we have obtained a diﬀerential equation for ωout.
To obtain agreement with the semi-classical theory for large black holes, we assume that
T−−(ω) approaches the value κ
4 for ω ≫κ. Of course, T−−(ω) should be zero for ω = 0,
which is the ground state of the stretched horizon. Furthermore, if one requires that the
onset of the Hawking radiation, for a massive black hole, agrees with the semi-classical result
(3.21), then one is led to a speciﬁc form for T−−(ω) during the heating phase at early times.
This can be constructed as follows. Deﬁne a function z(ω) by
ω = z(ω) −κ
4 log

1 + 4
κz(ω)

,
(3.49)
then choose
T−−(ω) = κ
4
h
1 −
1
(1 + 4
κz(ω))2
i
.
(3.50)
For massive black holes, it can be shown that ω(t) as given by (3.40) solves (3.48) until near
32
the end of the evaporation.
We can now see an important advantage of the stretched horizon formulation, concerning
the endpoint of Hawking evaporation. In the semi-classical RST model [23], overall energy
conservation could only be achieved by having a negative energy “thunderpop” at the end
of the evaporation process. The negative energy was bounded and small, but nevertheless
an embarrassment [25]. In contrast, consider the sum of (3.44) and (3.45), evaluated at the
stretched horizon,
˙ωin −¨ωin + ˙ωout + ¨ωout = T++ −T−−.
(3.51)
Integrating both sides of (3.51) over time reveals that energy is conserved, i.e.,
Z
dt T++ =
Z
dt T−−
(3.52)
as long as ω begins and ends at zero. This is assured in the remote past, when the stretched
horizon coincides with the boundary curve. For the late time evolution of ω, we return to
(3.48). From (3.41) we see that the late value of ωin is the total infalling mass, so ωin →M∞.
Inserting this into (3.48) leads to the following diﬀerential equation for ωout at late time:
¨ωout + ˙ωout + T−−(ωout + M∞) = 0 .
(3.53)
This is the equation for the damped motion of a particle subject to a restoring force, with
equilibrium position at ωout + M∞= 0. Provided the motion is overdamped, we ﬁnd that ω,
and therefore T−−, tend smoothly to zero at late times. This places a condition on T−−(ω),
namely that it goes to zero no slower than ω
4 . Comparing with (3.49) and (3.50) we see that
T−−must depend diﬀerently on ω during the cooling and heating phases.
33
