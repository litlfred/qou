---
doc_id: arxiv-hep-th-9306069v2
doc_title: "The stretched horizon and black hole complementarity"
section_id: sec-005-5-consequences-of-the-postulates
section_title: "Consequences of the postulates"
section_number: 5
pages: 37-47
source_pdf: 9306069v2.pdf
source_sha256: a140d10424f73233
toc_source: inferred
doc_brief: "The stretched horizon and black hole complementarity — Three postulates asserting the validity of conventional quantum theory, semi-classical general relativity and the statistical basis for"
---
5.1. Microstructure of the stretched horizon
Consider a quantum ﬁeld theory in a two-dimensional spacetime with a strictly time-like
boundary. Suppose the boundary is stationary at σ = 0, except for a brief time interval
[ta, tb], during which it moves toward negative σ (left) and then returns.
The ﬁelds are
deﬁned to the right of the boundary. The boundary may have additional degrees of freedom.
Without loss of generality we can pretend that the boundary is permanently at σ = 0
by assigning it extra degrees of freedom during the interval [ta, tb]. During this period the
system has ﬁeld degrees of freedom on the negative σ axis. Nothing prevents us from formally
considering these degrees of freedom to belong to the boundary at σ = 0.
In the case of subcritical ﬂux, where the boundary is always time-like and in causal
contact with distant observers, we can perform a similar formal trick, regardless of the
nature of the boundary degrees of freedom. They, as well as the ﬁelds behind the stretched
horizon, can be formally assigned to the stretched horizon. We gain nothing from this except
the assurance that a set of stretched horizon degrees of freedom can be deﬁned. Note that
this procedure in no way inﬂuences the experiences of an observer crossing the stretched
horizon.
37
Up to now we have assumed nothing radical. The fact that outside observers see an
apparently real stretched horizon is surprising but derivable from conventional semi-classical
assumptions. At this point we will make a radical departure from traditional thought about
black holes, which is required by our three postulates. We propose that, for the purposes of
a distant observer,
A consistent set of quantum mechanical degrees of freedom continue to describe the
stretched horizon even when the critical ﬂux is exceeded.
We postulate no details about these degrees of freedom, but some general properties are
required by Postulate 3. According to standard thermodynamic reasoning, the entropy of
a large system is the negative of the logarithm of the density of states. For both two- and
four-dimensional black holes, the entropy is proportional to the area. We therefore require
that the dimension of the Hilbert space of a stretched horizon with area A is of order exp(A).
For a four-dimensional black hole, this suggests that the number of degrees of freedom per
unit area is a universal, intensive property, independent of the total mass of the black hole.
This universality of stretched horizon properties is general. Deﬁne the stretched horizon
of a four-dimensional Schwarzschild black hole to have an area one Planck unit greater than
the global event horizon. The local rate of clocks at the stretched horizon is easy to compute.
The analogue of (3.4) has the form
dτ
dt ∼MP
M
(5.1)
where MP is the Planck mass and M is the mass of the black hole.
The local proper
temperature at the stretched horizon, TS, is related to the asymptotically measured Hawking
temperature TH by
TS = M
MP
TH .
(5.2)
Using the standard Hawking temperature TH ∼M 2
P
M gives the universal value
TS ∼MP .
(5.3)
The total energy of the black hole, measured in proper units at the stretched horizon, is
MS = M dt
dτ ∼M2
MP
.
(5.4)
38
Dividing this by the area of the stretched horizon we ﬁnd the surface energy density to be
MS
A ∼M3
P .
(5.5)
In the semi-classical theory deﬁned in Section 3, the temperature of a black hole is
completely independent of its mass. Thus, as a black hole evaporates, its energy ﬂux is
exactly constant, until the instant it disappears. An immediate consequence of Postulate 3
is that the temperature of a two-dimensional dilaton black hole cannot be strictly constant
when the mass tends to zero. However, there can be a maximum temperature, which is
quickly saturated as energy increases. Suppose there are discrete energy levels with a density
ρ(E) which behaves asymptotically as
ρ(E) ∼exp(2πE)
as
E →∞.
(5.6)
The partition function
Z(β) =
X
states
e−βE
(5.7)
converges for all β > 2π. For large β, Z can be approximated by the ﬁrst few terms:
Z ≈1 + e−βE1 + . . . ,
(5.8)
and the average energy is given by
⟨E⟩= −∂log(Z)
∂β
≈E1 e−βE1 + . . . .
(5.9)
As the ⟨E⟩tends to inﬁnity, the temperature tends to the value T =
1
2π in agreement with
the semi-classical limit. As the energy tends to zero, the temperature T = 1
β also tends to
zero.
In the semi-classical approximation, the black hole radiates a bit more energy than the
system originally had [23]. This was compensated by a ﬁnal “thunderpop” of negative energy.
From the present point of view, a more plausible behavior is that as the black hole nears the
endpoint of the evaporation process, its temperature and luminosity tend to zero and do not
overshoot. Note that this is precisely the behavior exhibited by solutions of (3.53).
39
Another unphysical consequence of the semi-classical theory concerns static solutions,
corresponding to a uniform sub-critical energy ﬂux, as the limit of critical ﬂux is approached.
According to the semi-classical theory a static solution exists for every value of the energy
ﬂux, T++ = T−−= T < κ
4. The semi-classical area (2.35), evaluated at the stretched horizon
(3.16), is given by
AS = T + (κ
4 −T)

log (κ
4 −T) −log κ
4

.
(5.10)
As T goes to κ
4 the area approaches A = κ
4. On the other hand, the statistical theory of
the previous section requires the mean square value of the area to diverge in this limit. The
model in section 3.4, based on the thermodynamics of the stretched horizon, does exhibit
that behavior. In general, thermodynamic boundary conditions at the stretched horizon,
as in section 3.4, yield a more consistent physical description than semi-classical boundary
conditions imposed at the critical curve, γcr.
The large horizon ﬂuctuations as the temperature approaches T =
1
2π are reminiscent of
critical behavior.⋆As the critical temperature is approached the area of the stretched horizon
ﬂuctuates more and more, until the horizon swallows up all of space. In the case of a second
order phase transition, correlated domains ﬂuctuate and grow until one domain swallows up
the whole sample. The failure of semi-classical theory to correctly account for the horizon
ﬂuctuations is analogous to the failure of mean ﬁeld theory in critical phenomena.
5.2. Thermal entropy vs. entropy of entanglement
Given our assumptions about the microstructure of the stretched horizon, it is evident
that no real loss of information takes place during black hole evaporation. Nevertheless,
it is far from clear how the large amount of initial data is stored in outgoing thermalized
radiation. Our discussion of this subject will follow the very illuminating study by Don Page
[27].
Let us begin by distinguishing two kinds of entropy. The ﬁrst, which is of purely quantum
origin, we call entropy of entanglement. Consider a quantum system composed of two parts,
A and B. In what follows, B will refer to the stretched horizon and A to the radiation
ﬁeld outside the stretched horizon. Assume the Hilbert space of state vectors H is a tensor
⋆R. Laughlin has also suggested similarities between black hole behavior and phase transitions [30].
40
product space: H = HA ⊗HB. If {|a⟩} is an orthonormal basis for HA and {|b⟩} is an
orthonormal basis for HB, then a general ket |ψ⟩in H may be written
|ψ⟩=
X
a, b
ψ(a, b) |a⟩⊗|b⟩.
(5.11)
The density matrix of the subsystem A, in the basis {|a⟩}, is
ρA(a, a′) =
X
b
ψ(a, b)ψ∗(a′, b) ,
(5.12)
and that of B is
ρB(b, b′) =
X
a
ψ(a, b)ψ∗(a, b′) .
(5.13)
Note that the composite system A ∪B is in a pure state.
The entropies of entanglement of subsystems A and B are deﬁned by
SE(A) = −Tr
 ρALOG(ρA)

,
SE(B) = −Tr
 ρBLOG(ρB)

.
(5.14)
It is easy to prove that SE(A) = SE(B) if the composite system is in a pure state. The
entropy of entanglement of a subsystem is only zero if |ψ⟩is an uncorrelated product state.
The entropy of entanglement is not the entropy with which the second law of thermodynamics
is concerned; SE can increase or decrease with time. A ﬁnal point is that if the dimension
of HB is DB, then the maximum value of SE(B) (and therefore of SE(A)) is
SE(B)max = −log(DB) .
(5.15)
We have assumed in (5.15) that DB ≤DA.
The second kind of entropy is entropy of ignorance.
Sometimes we assign a density
matrix to a system, not because it is quantum entangled with a second system, but because
we are ignorant about its state, and we assign a probability to each state. For example, if we
know nothing about a system, we assign it a density matrix proportional to the unit matrix.
If we know only its energy, we assign a density matrix which is vanishing everywhere except
41
the allowed energy eigenspace. Thermal entropy is of this type: it arises because of practical
inability to follow the ﬁne grained details of a system. For a system in thermal equilibrium
with a reservoir, we assign a Maxwell-Boltzmann density matrix
ρMB = Z−1EXP(−βH) ,
(5.16)
and deﬁne the thermal entropy by
ST = −Tr
 ρMB LOG(ρMB)

.
(5.17)
Now let us consider the evolution of both kinds of entropy during the formation and
evaporation of a two-dimensional black hole. Let us begin with the thermal entropy of the
stretched horizon, which we assume is equal to its area. As we have seen, the area begins to
increase exponentially with t before the infalling matter arrives, reaching its maximum at the
arrival time. The area then decreases linearly with t until the black hole disappears. This
is illustrated in Figure 8. The thermal entropy of the outgoing radiation begins to increase
due to the emission from the excited stretched horizon. Shortly after the radiation begins,
the temperature approaches T =
1
2π, so that the rate of change of the thermal entropy of
the radiation is constant throughout most of the process. This is also shown in Figure 8.
ST
HS
t
radiation
FIGURE 8. Thermal entropy of stretched horizon and radiation ﬁeld as a function of time.
Now consider the entropy of entanglement. Initially, the stretched horizon is in its ground
state, with minimal area, and the radiation ﬁeld is described by a pure state. The entropy
42
of entanglement starts at zero. As soon as the stretched horizon area begins to increase,
f−quanta are emitted. Typically, the state of the f−quanta will be correlated to the state
of the stretched horizon, so that SE will start to increase. However, SE will generally be
bounded by the logarithm of the dimension of the Hilbert space describing the stretched
horizon, which we have assumed is proportional to the area. In other words, at any time,
SE(HS) ≤ST(HS) = A(t) .
(5.18)
Thus, the entropy of entanglement is bounded and must return to zero as the area of the
stretched horizon returns to its vacuum value. Page has argued that in the beginning the
entropy of entanglement is likely to approximately follow the thermal entropy of the radiation
ﬁeld, so that the history of SE should look like Figure 9.
SE
t
FIGURE 9. Entanglement entropy of radiation and stretched horizon.
The dashed curves indicate the thermal entropies of Figure 8.
Evidently, as time elapses, subtle diﬀerences develop between the coarse grained thermal
density matrix of the radiation and the exact description. Postulates 1 and 3 dictate that
the entropy of entanglement return to zero in a more or less deﬁnite way as the black hole
evaporates. In particular, there is no room for a stable or very long-lived remnant storing
the incident information.
To understand the diﬀerence between the thermal and exact density matrices of the ﬁnal
outgoing radiation, consider a time about half-way through the evaporation process, when
43
the thermal entropy and the entropy of entanglement are still not too diﬀerent. The total
ﬁne grained entropy of the combined system of stretched horizon and radiation is zero, but
the radiation is correlated to the degrees of freedom of the stretched horizon. More time
elapses, and the stretched horizon emits more quanta. The previous correlations between the
stretched horizon and the radiation ﬁeld are now replaced by correlations between the early
part of the radiation and the newly emitted quanta. In other words, the features of the exact
radiation state which allow SE to return to zero are long time correlations spread over the
entire time occupied by the outgoing ﬂux of energy. The local properties of the radiation are
expected to be thermal. For example, the average energy density, short time radiation ﬁeld
correlations, and similar quantities that play an imporant role in the semi-classical dynamics
should be thermal. The long time correlations which restore the entropy to zero are not
important to average coarse grained behavior, and are just the features which are not found
unless a suitable microphysical description is provided for the stretched horizon.
5.3. Discussion
We will conclude with some speculation about the nature of the stretched horizon mi-
crostructure for four-dimensional black holes. If we consider nearly spherical black holes, a
stretched horizon can be deﬁned as follows. Consider a radial incoming null geodesic which
crosses the global horizon where its area is A. Proceed backward along such geodesics until
the surface with area one Planck unit larger is encountered. By using such ingoing geodesics,
we can map every point of the global horizon to a point on the stretched horizon.
The global horizon is composed of a bundle of light rays which can be thought of as a
two dimensional ﬂuid on the global horizon [9]. The points of this ﬂuid can be mapped to
the stretched horizon, thereby deﬁning a ﬂuid ﬂow on that surface. Classically, the ﬂuid
behaves as a continuous, viscous ﬂuid with conventional shear viscosity and negative bulk
viscosity. A natural candidate for the microphysics of the stretched horizon is to replace the
continuous classical ﬂuid with a ﬂuid of discrete “atoms”.
As we have seen, the intensive thermodynamic variables of the stretched horizon are
universal and do not depend on the size or mass of the black hole. This demands that the
surface density of atoms also is independent of the area. When incoming energy ﬂux or
outgoing Hawking radiation causes the area of a patch of the stretched horizon to change,
points of the ﬂuid will pop into and out of existence in order to keep the density constant.
44
Finally we would like to point to a feature of 3+1-dimensional black holes which is
not shared by the 1+1-dimensional theory. This feature adds plausibility to the claim that
the stretched horizon is in thermal equilibrium during most of the evaporation. Consider
an observer at the stretched horizon who counts the number of particles emitted per unit
proper time. Since the stretched horizon is always at the Planck temperature the number
of particles emitted per unit area per unit proper time is of order one in Planck units. If all
these particles made it out to inﬁnity, then a distant observer would estimate a number of
particles emitted per unit time, which is obtained by multiplying by the black hole area and
the time dilation factor,
dN
dt ∼M2dτ
dt ∼M .
(5.19)
On the other hand, the number per unit time of particles that actually emerge to inﬁnity is
obtained by multiplying the black hole luminosity L ∼
1
M 2 by the inverse energy of a typical
thermal particle at the Hawking temperature. The result is
dN
dt ∼1
M .
(5.20)
Therefore it seems that most of the particles emitted from the stretched horizon do not
get to inﬁnity. In fact, only those particles which are emitted with essentially zero angular
momentum can overcome the gravitational attraction of the black hole, and the rest fall
back [9]. This gives rise to a thermal atmosphere above the stretched horizon which only
slowly evaporates and whose repeated interaction with the stretched horizon insures thermal
equilibrium. Such a thermal atmosphere can be obtained in 1 + 1 dimensions by including
massive degrees of freedom in the model, and this may indeed be necessary for a fully
consistent description of two-dimensional black hole evaporation.
If the considerations of this paper are correct then black holes catalyze a very diﬀerent
phenomenon than that envisioned by Hawking [16]. To begin with an incoming pure state of
matter composed of low-energy particles falls into its own gravitational well. The matter is
blue-shifted relative to stationary observers so that when it arrives at the stretched horizon it
has planckian wavelengths. Thereupon it interacts with the “atoms” of the stretched horizon
leading to an approximately thermal state. The subsequent evaporation yields approximately
thermal radiation but with non-thermal long time correlations. These non-thermal eﬀects
depend not only on the incoming pure state but also on the precise nature of the Planck-scale
45
“atoms” and their interaction with the blue-shifted matter. The evaporation products then
climb out of the gravitational well and are red-shifted to low energy. The result is remarkable.
The very low-energy Hawking radiation from a massive black hole has non-thermal correla-
tions, which contain detailed information about Planck-scale physics [3,4]. The phenomenon
is reminiscent of the imprinting of planckian ﬂuctuations onto the microwave background
radiation by inﬂation.
The view of black holes that we have presented is, of course, incomplete. As we have
emphasized, the reality of the membrane can not be an invariant which all observers agree
upon. Furthermore, although conventional quantum ﬁeld theory in an evaporating black
hole background seems to lead to a description in which a single state vector describes the
interior and exterior of the black hole, this description must be wrong if our postulates are
correct. Precisely what is wrong is not clear to us, but we wish to emphasize that the event
space for an experiment should only contain physically measurable results.
In many respects, the situation seems comparable to that of the early part of the century.
The contradictions between the wave and particle theories of light seemed irreconcilable, but
careful thought could not reveal any logical contradiction. Experiments of one kind or the
other revealed either particle or wave behavior, but not both. We suspect that the present
situation is similar. An experiment of one kind will detect a quantum membrane, while
an experiment of another kind will not. However, no possibility exists for any observer to
know the results of both. Information involving the results of these two kinds of experiments
should be viewed as complementary in the sense of Bohr.
Acknowledgements: We are very grateful to a number of our friends for collaboration, ad-
vice and encouragement. In particular we have beneﬁtted from many conversations with
T. Banks, A. Bilal, C. Callan, S. de Alwis, S. Giddings, S. Hawking, R. Laughlin, D. Page,
J. Preskill, A. Strominger, E. Verlinde, and H. Verlinde. Section 4 of the paper is based on
work done in collaboration with N. Seiberg, S. Shenker and J. Tuttle. Much of the remainder
of the paper reﬂects our previous close collaboration with J. Russo. Finally, we are especially
thankful to G. ’t Hooft for inspiration and for reinforcing our own belief in the inviolability
of the principles of quantum theory in black hole evaporation. This work is supported in
part by National Science Foundation grant PHY89-17438. J. U. is supported in part by a
National Science Foundation Graduate Fellowship.
46
