---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-030-5-moduli-space-on-r2-s1
section_title: "Moduli space on R2× S1"
section_number: 5
pages: 41-42
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
One simple way to test the correspondence M ←→TM is to associate a moduli space to
each side. In the analogous construction [ 1] of the 4d N = 2 superconformal theory from
a Riemann surface C, there is a similar test of the correspondence C ←→T (C) based on
comparing the moduli space of complex (equivalently, conformal) structures on C with the
moduli space of marginal couplings of the theory T (C).
In the present case, there is a similar test of the correspondence M ←→ TM based
on comparing moduli spaces of complex ﬂat connections on M and the moduli space of
supersymmetric vacua of the theory TM. To be more precise, the space of complex ﬂat
connections on M can be identiﬁed with the space of SUSY moduli in the theory TM on
R2×S1 [4]:
Mﬂat(M,SL (2, C)) = MSUSY(TM). (5.1)
While the deﬁnition of the moduli space Mﬂat(M,SL (2, C)) is clear (and was reviewed in
section 2) we need to properly interpret the right-hand side of ( 5.1).
Upon compactiﬁcation on R2× S1, the N = 2 theory TM becomes eﬀectively two-
dimensional. Supersymmetry then requires that the vevs of chiral and twisted chiral ﬁelds,
whether dynamical or not, are complex valued. For example, 3d real mass parameters as-
sociated to a background U(1) gauge multiplet V become complexiﬁed by the holonomies
of the background photon on S1. Therefore, moduli spaces parametrized by vevs of chiral
and twisted chiral ﬁelds are always complex manifolds. Here, we are mostly interested in the
moduli space parameterized by vevs of twisted chiral ﬁelds — the descendants of 3d gauge
multiplets — and denote this space MSUSY.
For example, ifM is a closed 3-manifold without boundaries or cusps, the corresponding
ﬁeld theory TM on R2×S1 has the moduli space of supersymmetric vacua MSUSY(TM)
obtained by minimizing the twisted superpotential ~W. Since the twisted superpotential is a
holomorphic function, the variety deﬁned by the equations ∂~W = 0 is a complex variety, just
like the moduli space of ﬂat SL(2, C) connections on M.
More generally, if M is a 3-manifold with boundary C =∂M , it is natural to project the
moduli spaceMﬂat(M,SL (2, C)) onto the moduli space of ﬂat connections onC, i.e. consider
those ﬂat connections on C which can be extended to all of M. In Section 2, this projection
was cut out by the Lagrangian submanifold
LM ⊂ P∂M =Mﬂat(C,SL (2, C)). (5.2)
Correspondingly, in theN = 2 gauge theory TM, it is natural to ask for which values of the
parametersvi (= vevs of non-dynamical ﬁelds) the theoryTM has SUSY vacua on R2×S1. In
order to answer this question, we introduce the eﬀective twisted superpotential ~Weﬀ obtained
by minimizing ~W with respect to all dynamical ﬁelds, and then deﬁne [ 35]:
M(param)
SUSY (TM) : ui = ∂~Weﬀ
∂vi
. (5.3)
– 40 –
In the the case where vi is the twisted mass in a background U(1) gauge ﬁeld, the coordinate
ui should be thought of as the background FI parameter for this ﬁeld; then it is clear that
(5.3) is the condition for unbroken supersymmetry. As we illustrate in a number of examples
below,~Weﬀ is a transcendental function, generically a sum of dilogarithm functions. However,
after taking the derivatives in ( 5.3) and introducing the new coordinates
𝓁i =evi, m i =eui (5.4)
(which are natural, because the complexiﬁed vevs ui and vi are periodic), one ﬁnds a nice
algebraic variety that is identical to LM.
Geometrically, it should be clear that the Lagrangian submanifold LM cannot depend
on the coordinates and polarization used to describe the phase space P∂M when M has
a boundary. Changing coordinates will simply re-parametrize LM. Similarly, the space
M(param)
SUSY (TM,Π) should not depend on the polarization Π (or boundary triangulation, etc.)
used in previous sections to deﬁne a theory TM,Π. One way to see this is to interpret
TM,Π on R2×S1 as describing a boundary condition B[TM,Π] for a 4d N = 2 theory T [C]
(C = ∂M ) compactiﬁed on R3×S1, as in Section 4.4. With a little bit of work, one can
show that the coordinates 𝓁i, mi become boundary values of natural coordinates ( e.g.XE
of [ 2, 16]) on the moduli space of the compactiﬁed 4d theory. From this point of view,
M(param)
SUSY (TM) = LM becomes a complex Lagrangian submanifold in the four-dimensional
moduli space16MSUSY(T [C])≃P ∂M . This Lagrangian characterizes the boundary condition
itself, rather than any speciﬁc realization of it via a 3d SCFT. In particular, changing the
polarization Π merely shifts the duality frame of the combined 4d-3d system, and must map
M(param)
SUSY (TM) to an isomorphic space.
The present discussion of supersymmetric vacua, particularly as given by equations ( 5.3)
with~W a sum of dilogarithm functions, is highly reminiscent of recent work relating eﬀective
2d ﬁeld theories to quantum integrable systems [ 36, 37, 38]. For example, 3d N = 2 theories
much likeTM compactiﬁed on a circle are related to the XXZ spin chain. A precise connection
between our present constructions and integrable systems would be very interesting, but has
yet to be established.
