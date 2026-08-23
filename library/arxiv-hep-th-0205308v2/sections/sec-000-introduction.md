---
doc_id: arxiv-hep-th-0205308v2
doc_title: "WDVV Equations as Functional Relations"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0205308v2.pdf
source_sha256: 2de5a4f40d80174c
doc_brief: "WDVV Equations as Functional Relations — 5 sections: Introduction; WDVV and dispersionless Hirota equ; The associativity equations as coc"
---
The associativity or Witten-Dijkgraaf-Verlinde-Verlinde (WDVV) eq uations [1] have
been widely discussed in connection with various problems of mathema tical physics
for over ten years. They have arisen in the context of quantum co homologies and
mirror symmetry, and also with regard to multidimensional supersym metric gauge ﬁeld
theories. In their most general form these equations may be expr essed as [2]
Fi · F−1
j · Fk = Fk · F−1
j · Fi ∀i, j, k. (1)
Here the matrices ‖Fi‖jk ≡ F ijk are constructed from the third derivatives of the func-
tion F (a),
Fijk = ∂ 3F
∂a i ∂a j ∂a k . (2)
When F is a function of one or two variables then (1) are empty: that is they are
satisﬁed by any function. For more variables however, despite the simplicity of their
compact matrix form, these equations form a highly nontrivial over determined system
of nonlinear partial diﬀerential equations satisﬁed by the function F .
In their original two-dimensional topological ﬁeld theoretic setting the WDVV equa-
tions (1) were supplemented by a further constraint: there was a distinguished coor-
dinate such that the matrix F1jk was a constant. This came from the existence of a
distinguished operator, the identity operator Φ 1, and the third derivatives of F being
related to three-point functions via ⟨Φ iΦ jΦ k⟩ = Fijk . This distinguished coordinate
meant their was a preferred “metric”, F1. Associated with this class of solutions to
(1) – together with a quasi-homogeneity condition – Dubrovin introd uced the notion of
1Department of Mathematics and Statistics, University of Ed inburgh, Edinburgh EH9 3JZ Scotland;
e-mail address: hwb@ed.ac.uk
2Theory Department, Lebedev Physics Institute, Moscow 1179 24, Russia and ITEP, Moscow 117259,
Russia; e-mail address: mars@lpi.ru; andrei@heron.itep. ru
1
Frobenius manifold [3]. However, there are physically interesting solu tions of (1) that
fail to possess these extra properties and for these the notion o f Frobenius manifold fails
to encapsulate their geometry.
This more general class of solutions to (1) includes some prepotent ials arising from
low-energy eﬀective actions of N = 2 supersymmetric gauge theories in four dimensions
via Seiberg-Witten theory. Supersymmetry typically restricts the possible geometries
encountered in ﬁeld theories. Thus sigma models have target space s that are Rieman-
nian, or possibly K¨ ahler or hyper-K¨ ahler depending on the number of supersymmetry
generators. For N = 2 SUSY gauge theories the moduli space of vector multiplets is
a special 3 K¨ ahler manifold [4, 5]. This means that on the moduli space there exis ts a
single holomorphic function F (a) whose second derivatives
Tij = ∂ 2F
∂a i ∂a j (3)
determines the metric via
ds2 = gi¯j daidaj, g i¯j = 1
2 (ImT )ij. (4)
Here ai are complex coordinates on the K¨ ahler manifold (and aj their complex conju-
gates). The connection with Seiberg-Witten theory is that the sec ond derivatives Tij
coincide with the matrix elements of the period matrix of the Seiberg- Witten auxiliary
curve and F is the prepotential. In [8] it was argued that this auxiliary curve cou ld be
identiﬁed with the spectral curve of a completely integrable system . Indeed, the phase
space of (appropriate algebraically) completely integrable systems can be identiﬁed as
a toric ﬁbration (the angles xi) over a special K¨ ahler manifold (the actions yj). The
K¨ ahler form is then
ω = dxi ∧ dyi =
√−1
2 (ImT )ij dai ∧ daj, (5)
and the real coordinates {xi, y j} are related to complex coordinates by
∂
∂a i = 1
2
( ∂
∂x i − Tij
∂
∂y j
)
.
The K¨ ahler potential here is K(a, ¯ a) = 1
2
(
ai ∂F
∂a i
)
. A special K¨ ahler manifold has two
natural connections associated with it. There is the Levi-Civita con nection D, with
Christoﬀel symbols Γ ¯ijk = −
√−1
4 Fijk , and there is also a ﬂat torsionfree connection
∇ = D + A such that ∇dxi = 0 = ∇dyj. Here the connection A,
A
( ∂
∂a i
)
=
(
Aj
) ¯l
i daj ⊗ ∂
∂al
=
√−1
4
(
g
¯lmFjim
)
daj ⊗ ∂
∂al
, (6)
3In the original supergravity context such a manifold was cal led “rigid special K¨ ahler” with “special
K¨ ahler” referring to the local (supergravity) setting; si nce [6] the local setting is often known by
“projective special K¨ ahler”. See [7] for a survey of these m anifolds.
2
satisﬁes 0 = ∂ DA = ∂A + Γ ∧ A − A ∧ Γ. Because the Levi-Civita connection connection
is torsionfree we may also write this as DiA¯l
jk = DjA¯l
ik with A¯l
jk = ( Aj)¯l
k. We refer
to [9, 10] for further material on the connections between Seiber g-Witten theory and
integrable systems.
Following the work of [8], it seemed to be very important that the func tion F satisﬁed
some well-known nonlinear integrable diﬀerential equations. The con nection between
Seiberg-Witten theory and the WDVV equations is that some prepotentials lead to
solutions of (1). Certainly not all prepotentials yield solutions and a c haracterisation of
what special K¨ ahler manifolds give solutions is still sought. Now the g eometric origin
of the WDVV equations in Seiberg-Witten theory appears to be comp letely diﬀerent
from that of Frobenius manifolds. Seiberg-Witten theory lacks the analogue of the
identity operator and constant “topological metric”. Indeed the re appears no obvious
connection between the (nonholomorphic) metric of special K¨ ahler geometry, built out of
second derivatives of the prepotential, and the “topological metr ic” F1 of the Frobenius
manifolds which is a third derivative. Further, the WDVV equations we re shown to be
covariant with respect to arbitrary symplectomorphisms in [11], whic h is quite natural
in the special K¨ ahler setting, but such do not preserve the Frobenius manifold structure.
The geometric origin underlying the WDVV equations has yet be clariﬁe d. In this
note we will reformulate these equations as functional relations. I n particular, they
will be in terms of second derivatives. These functional relations ar e reminiscent of the
Hirota equations and we will give an example making this clearer.
