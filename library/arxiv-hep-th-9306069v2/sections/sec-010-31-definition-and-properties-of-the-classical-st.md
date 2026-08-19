---
doc_id: arxiv-hep-th-9306069v2
doc_title: "Department of Physics"
section_id: sec-010-31-definition-and-properties-of-the-classical-st
section_title: "Definition and properties of the classical stretched ho rizon"
section_number: 3.1
pages: 18-22
source_pdf: 9306069v2.pdf
source_sha256: a140d10424f73233
doc_brief: "Department of Physics — Three postulates asserting the validity of conventional qu antum theory, semi-classical general relativity and the statistical basis for thermodyn amics are introduced as a"
---
We deﬁne the classical stretched horizon as follows. Consid er the classical area function
(2.2) along the global event horizon. For a black hole formed by gravitational collapse,
depicted in Figure 3, this area increases with y+ until the black hole has settled to its ﬁnal
size. We deﬁne the stretched horizon by mapping each point m on the event horizon back
along a past-directed null line (away from the event horizon itself) to a point p at which
A(p) = A(m) +δ, (3. 1)
where δ is an arbitrary small constant. This results in a timelike cu rve as indicated in
Figure 5.
18
singularity
ι+
R
ι−
L ι−
R
event horizon
black hole
m
stretched horizon
p
ι+
L
FIGURE 5. Construction of the classical stretched horizon.
Note that our deﬁnition diﬀers from that given in [9]. There t he shift in the area
between the global event horizon and the stretched horizon s cales like the horizon area
itself. For a massive black hole our stretched horizon is thu s much closer to the event
horizon. Our deﬁnition is better suited for the semi-classi cal theory of two-dimensional
gravity considered here, and may also be appropriate for the quantum description of black
holes in four spacetime dimensions. For the classical black hole solutions (2.17) one ﬁnds
the remarkably simple result that in Kruskal coordinates th e stretched horizon curve is
independent of the incoming energy ﬂux, T++(y+), and the curve is given by
−y+y− =δ. (3. 2)
The simplicity of the stretched horizon becomes even more ap parent in the tortoise
coordinates (2.20). While the event horizon lies at t = ∞ and σ = −∞, the stretched
horizon is at ﬁxed spatial position
σ S = 1
2 logδ. (3. 3)
Thus the stretched horizon can receive and emit signals. Fur thermore, to distant observers,
19
clocks at the event horizon appear inﬁnitely slowed while th ey appear to run at a ﬁnite rate
at the stretched horizon. For an eternal black hole of mass M0, proper time τ along HS is
related to coordinate time t by
dτ =
√
δ
M0+δ dt. (3. 4)
Finally, one can consider the Hawking temperature of a massi ve two-dimensional dilaton
black hole,T = 1
2π , which is independent of the mass. Since temperature has uni ts of energy,
then in proper time units at the stretched horizon the temper ature is
TS = 1
2π
dt
dτ = 1
2π
√
M0+δ
δ . (3. 5)
From (3.5) it appears that the local temperature at the stret ched horizon increases with
M0. This is a bit misleading, because the analogue of the Planck length in two-dimensional
dilaton gravity depends on the local value of the dilaton ﬁel d, according to lpl ∼eφ. At the
stretched horizon, the dilaton ﬁeld satisﬁes e−φ = √M0+δ , so (3.5) implies that, measured
in Planck units, the temperature at the stretched horizon is independent of the mass. This
result also holds for four-dimensional black holes as we wil l see in section 5.1.
Let us continue examining the classical behavior of the stre tched horizon. Consider the
evolution of the area A onHS. Parametrizing HS byy+ and substituting the deﬁnition (3.2)
of HS into the gravitational collapse solution (2.17) we ﬁnd
AS(y+) = M(y+) +δ −y+(P+(y+) −P∞) (3 . 6)
which, when diﬀerentiated twice, gives
d2AS
(dy+)2 = −T++(y+). (3. 7)
Transforming to tortoise coordinates, one can parametrize HS by the tortoise time t =
logy+ − 1
2 logδ . Equation (3.7) then becomes
d2AS
dt2 −dAS
dt = −
( dy+
dt
) 2
T++(y+) ≡ −T++(σ +) (3 . 8)
where the quantity T++(σ +) is the incoming physical ﬂux of energy as seen by a distant
observer. There are two interesting features of (3.8). The ﬁ rst has to do with the nature of
20
the boundary conditions on the solutions of the equation. In general, the stretched horizon
will begin to grow even before any energy crosses it. From (3. 8) we see that before T++
becomes nonzero, AS has the solution
AS(t) = Cet. (3. 9)
The choice of the constant C is dictated by ﬁnal conditions. As t → ∞ , a black hole is
present with mass M∞. The area of the stretched horizon of such a black hole is
lim
t→∞
AS(t) = M∞ +δ, (3. 10)
and thus (3.10) is the boundary condition one must impose on t he solution of (3.8). This
means that the initial state of the stretched horizon must be tuned in conjunction with
the incoming matter distribution so that (3.10) is satisﬁed . This strange feature has been
referred to in the membrane paradigm literature as the “tele ological boundary condition”
[9]. We will show in section 3.4 how the equations can, in fact , be given a more conventional
and causal interpretation.
The second interesting feature of (3.8) is the dissipative t erm dAS
dt . It breaks time reversal
symmetry much like a friction term in ordinary mechanics. Th e presence of dissipative terms
in mechanics is generally associated with the production of heat and the increase of thermal
entropy. In the classical case, the temperature of the black hole is zero, but in the semi-
classical case the temperature increases when the black hol e is formed, and the stretched
horizon appears to radiate like a thermally excited black bo dy.
In the limit of large black holes, we can also consider the the ory of a massless matter
ﬁeld f propagating in the black hole background. We ﬁnd that the equ ations governing
the matter ﬁelds interacting with the stretched horizon als o exhibit dissipation. In the case
of a four-dimensional black hole interacting with electrom agnetic ﬁelds, the phenomenon
of dissipation is described by attributing an ohmic resista nce to the membrane. A similar
description can be given for two-dimensional dilaton black holes. Indeed, the theory of a
massless ﬁeld f bears a useful resemblance to ordinary classical electrody namics, with f
playing the role of the vector potential. We work in the torto ise coordinates (2.20) and
21
deﬁne the “electric” and “magnetic” ﬁelds E and B by
E = −∇tf, B = ∇σf . (3. 11)
The equation of motion for the f ﬁeld is
∇2f = −4πJ (3. 12)
where we have introduced a source j. Writing this equation in terms of the ﬁelds E and B,
we obtain an inhomogeneous “Maxwell” equation
∇tE + ∇σB = −4πJ . (3. 13)
We can also obtain the homogeneous “Maxwell” equation ∇σE + ∇tB = 0.
Now we consider the interaction of the f ﬁeld with the stretched horizon, which, from
the point of view of an external observer, is a boundary absor bing all incoming waves. This
behavior can be modeled by attributing a resistance to the st retched horizon,
∇tE + ∇σB = −4πρ −1
S δ (σ −σ S)E. (3. 14)
An incoming f wave will be completely absorbed if and only if ρ = 4π . This is the analogue
of the surface electrical resistivity of a four-dimensiona l black hole. The power absorbed
by the stretched horizon is ρ −1
S (∂ tf )2, which can be thought of as ohmic heating. When
quantum corrections are included, the heat is radiated back as Hawking radiation.
