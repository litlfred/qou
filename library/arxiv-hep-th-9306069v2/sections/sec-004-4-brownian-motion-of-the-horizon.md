---
doc_id: arxiv-hep-th-9306069v2
doc_title: "The stretched horizon and black hole complementarity"
section_id: sec-004-4-brownian-motion-of-the-horizon
section_title: "Brownian motion of the horizon⋆"
section_number: 4
pages: 34-37
source_pdf: 9306069v2.pdf
source_sha256: a140d10424f73233
toc_source: inferred
doc_brief: "The stretched horizon and black hole complementarity — Three postulates asserting the validity of conventional quantum theory, semi-classical general relativity and the statistical basis for"
---
Lagrangian mechanics and thermodynamics are quite diﬀerent descriptions of a system.
According to the usual principles of lagrangian mechanics, the motion of any system is
reversible and the concepts of heat and entropy have no place. Thermodynamics, on the
other hand, is the theory of the irreversible dissipation of organized energy into heat. The
thermodynamic description arises from the coarse graining of the mechanical description, in
which conﬁgurations which are macroscopically similar are considered identical.
The equations of semi-classical gravity are peculiarly thermodynamic near the stretched
horizon. In this section, we will see that they include another eﬀect that generally occurs
in thermodynamic systems, namely, random ﬂuctuation and diﬀusion. That such an eﬀect
should occur was pointed out to us by N. Seiberg and S. Shenker [29].
Speciﬁcally, we
shall see that the area of a two-dimensional dilaton black hole undergoes brownian motion
and diﬀuses away from its semi-classical value.
This phenomenon can be independently
understood from thermodynamics and quantum ﬁeld theory.
We begin by recalling the Einstein relation between speciﬁc heat and energy ﬂuctuations.
The average energy and squared energy of a system in thermal equilibrium with a heat bath
are
⟨E⟩= −1
Z
∂Z
∂β ,
(4.1)

E2

= 1
Z
∂2Z
∂β2
(4.2)
where Z is the partition function and β is the inverse temperature. From (4.1) and (4.2) it
follows that
∂⟨E⟩
∂β
=

⟨E⟩2 −

E2

= −Var(E) ,
(4.3)
where Var(X) =

(X−⟨X⟩)2

denotes the variance of the quantity X. This can be expressed
⋆The material in this section is based on work done in collaboration with N. Seiberg, S. Shenker, and
J. Tuttle [28].
34
in terms of the speciﬁc heat C, deﬁned by
C = ∂⟨E⟩
∂T
= −1
T 2
∂⟨E⟩
∂β
,
(4.4)
so that
T 2C = Var(E) .
(4.5)
In particular, since the variance of any quantity is positive-deﬁnite, the speciﬁc heat is also
positive deﬁnite. When applied to a four-dimensional Schwarzschild black hole, (4.4) gives
nonsense because the speciﬁc heat is negative. This is a sign of instability.
In section 3.2, we obtained a dynamical equation (3.28) for the time dependence of the
horizon area A. In thermal equilibrium, the incoming and outgoing average energy ﬂuxes are
both equal to κ
4. In this case (3.28) has a static solution for each value of the average area.
Since the Hawking temperature of two-dimensional black holes is independent of the mass
in the semi-classical approximation, the speciﬁc heat of a black hole is inﬁnite. By (4.5),
the root-mean-square ﬂuctuations of the mass, and therefore the area, are also inﬁnite. This
means that the thermal ﬂuctuations will so smear the horizon that the diﬀerent mass static
black hole solutions should be replaced by a single ensemble for all masses and areas.
More generally, a time-dependent semi-classical black hole will have a brownian motion
superimposed on the semi-classical solution. Among other eﬀects, this will cause a statistical
ﬂuctuation in the elapsed time before the black hole ceases to radiate. The ﬂuctuation will
be of order
√
M, where M is the initial black hole mass.
Physically, we can understand this as follows: ﬂuctuations in the thermal ﬂux of energy
at the horizon cause the black hole mass to randomly increase and decrease with time.
For an ordinary system, with positive speciﬁc heat, such ﬂuctuations are self-regulating. A
momentary increase (decrease) in the energy of the system causes an increase (decrease) in
its temperature, which in turn causes heat to ﬂow back to (from) the reservoir, thus restoring
equilibrium. In the present case, the temperature does not respond to the energy ﬂuctuation.
Therefore, there is no tendency to return to the original energy balance. The mass and area
just random walk away from their original values.
If a black hole of area A0 is created at time t = 0 and is subsequently illuminated with
thermal radiation at the Hawking temperature T =
1
2π, then at time t > 0 the mass of the
35
black hole will have random walked:

(A(t) −A0)2

∝t .
(4.6)
The exact coeﬃcient in (4.6) can be computed from a knowledge of ﬂuctuations in the
thermal energy of the matter ﬁelds in the surrounding bath. For the case of N massless
ﬁelds, the result is

(A(t) −A0)2

=
N
24π2t .
(4.7)
A rough translation of this result into Kruskal coordinates can be made by observing that y±
are exponentials of tortoise coordinates. Equation (4.7) suggests that in terms of an infrared
cutoﬀin Kruskal coordinates log R ≈t, the ﬂuctuations in the horizon area satisfy
Var(A) ≈
N
24π2 log R .
(4.8)
Now let us consider the semi-classical ﬁeld equations (2.33). In particular, the scalar
ﬁeld Ωsatisﬁes an inhomogeneous free ﬁeld equation in Kruskal coordinates given by
∂+∂−Ω= −1 .
(4.9)
The static black hole solutions to (4.9) have the form
ΩM = M −y+y−
(4.10)
and the semi-classical area of the event horizon of a massive black hole is given by
A ≈ΩM(0) = M .
(4.11)
The area of the stretched horizon is a bit larger but this diﬀerence will not be important in
this section.
36
Now let us consider the quantum ﬂuctuations about (4.10). Deﬁne ∆= Ω−ΩM. The
ﬂuctuation ∆satisﬁes a free wave equation,
∂+∂−∆= 0 .
(4.12)
This suggests that ∆is a canonical, massless free ﬁeld. As such it has ﬂuctuations which
are logarithmically infrared divergent,

∆2(0)

≈
κ
2π2 log R ,
(4.13)
where R is the Kruskal coordinate infrared cutoﬀ. This estimate of the ﬂuctuations in the
horizon area precisely agrees with the thermodynamic result (4.7). It should be pointed out
that there are technical subtleties involved in the quantization of this model, and the above
result has not been rigorously established. However, the agreement with thermodynamics
strongly suggests that ∆behaves like a canonical ﬁeld [28].
