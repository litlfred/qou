---
doc_id: arxiv-hep-th-9306069v2
doc_title: "The stretched horizon and black hole complementarity"
section_id: sec-006-23-semi-classical-theory
section_title: "Semi-classical theory"
section_number: 2.3
pages: 13-15
source_pdf: 9306069v2.pdf
source_sha256: a140d10424f73233
doc_brief: "The stretched horizon and black hole complementarity — Three postulates asserting the validity of conventional qu antum theory, semi-classical general relativity and the statistical basis for"
---
Our second postulate assumes that a semi-classical approxi mation to gravitation theory
can be developed systematically. In the simpliﬁed world of t wo-dimensional dilaton gravity
this can be achieved by the addition of certain quantum corre ctions to the classical equa-
tions of motion, as ﬁrst described in the groundbreaking wor k of Callan et al. [11]. These
corrections arise from the conformal anomaly of the matter ﬁ elds in the theory, which takes
the form
⟨
T µ
µ
⟩
= N
24R. (2. 23)
The semi-classical CGHS model is obtained by adding to the cl assical action, (2.1), the
associated Liouville term,
SL = − N
96π
∫
d2x
√
−g(x)
∫
d2x′√
−g(x′)R(x)G(x;x′)R(x′), (2. 24)
whereG is a Green function for the operator ∇2. This incorporates the leading-order quan-
tum back-reaction on the geometry due to the matter ﬁelds. Th e original CGHS-equations
have not been solved in closed form (see [26] for results of nu merical studies) but subsequent
work led to a set of semi-classical equations which can be sol ved exactly [20-23]. In the
following we will use the model introduced by Russo, Susskin d and Thorlacius (RST) and
give a summary of the results of [23,24]. This model is obtain ed by including in the eﬀective
action a local covariant counterterm,
− N
48π
∫
d2x√−gφR, (2. 25)
in addition to the non-local Liouville term. This turns out t o simplify the analysis and
physical interpretation of the semi-classical solutions.
13
We work in conformal gauge and use light-cone coordinates (y+,y −). The eﬀective action
becomes
Sef f = 1
π
∫
d2y
{
e−2φ[2∂ +∂ −ρ − 4∂ +φ∂ −φ +e2ρ] + 1
2
N∑
i=1
∂ +fi∂ −fi
−κ [∂ +ρ∂ −ρ +φ∂ +∂ −ρ ]
}
,
(2. 26)
where κ = N
12
⋆ The constraint equations, which follow from varying g±±, are
(e−2φ + κ
4 )[2∂ 2
±φ − 4∂ ±ρ∂ ±φ ] −κ (∂ 2
±ρ − (∂ ±ρ )2 −t±) −T±± = 0. (2. 27)
HereT±± is the physical, observable ﬂux of energy-momentum. There a re subtleties involved
in the regularization of the composite operator. We deﬁne T±± to be normal ordered with
respect to the asymptotically minkowskian tortoise coordi nates (2.20).
The functions t±(y±) reﬂect both the non-local nature of the anomaly and the choi ce of
boundary conditions satisﬁed by the Green function G. They are ﬁxed by physical boundary
conditions on the semi-classical solutions.
If we deﬁne the two-component vector
Φ =
(
φ
ρ
)
, (2. 28)
then the kinetic terms in the action (2.26) may be written ( ∂ +Φ) ·M · (∂ −Φ), and one ﬁnds
that
(−det(M)
4 )− 1
4 = (e−2φ − κ
4 )− 1
2 (2. 29)
plays the role of the gravitational coupling constant for th efi ﬁelds. This coupling becomes
inﬁnite on a curve γ cr on which the classical area function (2.2) takes on the value
Acr = κ
4 . (2. 30)
The curve γ cr has been interpreted to be a boundary of the semi-classical s pacetime [17,24],
which plays the same role as the surface r = 0 in the Schwarzschild solution of four-
dimensional Einstein gravity. Accordingly, we have to impo se a boundary condition on
⋆ We will not go into the technical issues involving reparamet rization ghosts etc. which are involved in
the determination of the value of κ. Our goal here is limited to obtaining exactly solvable equa tions,
which incorporate the leading semi-classical corrections and exhibit reasonable physical behavior, such
as having a rate of Hawking radiation proportional to the num ber of matter ﬁelds.
14
γ cr when it is timelike. Following [24], the boundary condition we use is to require the scalar
curvature to be ﬁnite on γ cr. This boundary condition implements a weak form of the cosmi c
censorship hypothesis, in that curvature singularities on γ cr will necessarily be spacelike and
cloaked by a global event horizon, except possibly for isola ted points.
We next deﬁne the ﬁelds †
Ω = e−2φ + κ
2φ,
χ =e−2φ +κ (ρ − 1
2φ ),
(2. 31)
for which the eﬀective action takes the simple form
Sef f = 1
π
∫
d2y
{ 1
κ [−∂ +χ∂ −χ +∂ +Ω ∂ −Ω] + e
2
κ (χ−Ω) + 1
2
N∑
i=1
∂ +fi∂ −fi
}
. (2. 32)
The resulting equations of motion and constraint equations are
∂ +∂ −χ =∂ +∂ −Ω = −e
2
κ (χ−Ω) , (2. 33)
1
κ [(∂ ±Ω) 2 − (∂ ±χ )2] +∂ 2
±χ +T±± −κt ± = 0. (2. 34)
The ﬁeld Ω can be viewed as a quantum corrected area function. At the horizon of a
massive black hole it agrees to leading order with the classi cal area function (2.2). More
speciﬁcally, we will deﬁne the semi-classical area functio n as
A = Ω − Ω cr, (2. 35)
where Ω cr = Ω( γ cr) = κ
