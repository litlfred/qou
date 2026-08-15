---
doc_id: arxiv-hep-th-9408099v1
doc_title: "E. Witten Institute for Advanced Study"
section_id: sec-006-3-classical-moduli-space-of-qcd-with-matter
section_title: "Classical moduli space of QCD with matter"
section_number: 3
pages: 11-14
source_pdf: 9408099v1.pdf
source_sha256: b534faddd2e3aa71
doc_brief: "Seiberg–Witten, Monopoles, duality and chiral symmetry breaking in N=2 supersymmetric QCD (1994) — exact metric on the moduli space of quantum vacua and exact stable-state spectrum for SU(2) with…"
---
We now turn to QCD with an SU (2) gauge group. The gluons are accompanied by
Dirac fermions and complex scalars φ in the adjoint representation of the gauge group. We
also add Nf hypermultiplets of quarks in the fundamental representati on. (We will also
consider the case of a single hypermultiplet in the adjoint r epresentation, this being the
N = 4 theory.) As in the previous section, each hypermultiplet contains a Dirac fermion
and four real scalars. In terms of N = 1 superﬁelds the hypermultiplets contain two chiral
superﬁelds Qia and ~Qia (i = 1,...,N f is the ﬂavor index and a = 1, 2 the color index) and
the N = 2 gauge multiplets include N = 1 gauge multiplets and chiral multiplets Φ. The
superpotential for these chiral superﬁelds is
W =
√
2~QiΦ Qi +
∑
i
mi~QiQi (3.1)
with color indices suppressed.
When the quarks are massless the global symmetry of the class ical theory is a certain
quotient of O(2Nf ) ×SU (2)R ×U (1)R. The reason for the O(2Nf ) symmetry (rather than
10
SU (Nf ) ×U (1)) is that for an SU (2) gauge theory the quarks Q and the antiquarks ~Q
are in isomorphic representations of the gauge group. There fore, we will also often denote
these N = 1 chiral superﬁelds by Qr with r = 1,..., 2Nf labeling the components of an
SO(2Nf ) vector. The squarks ( Q,~Q) transform like ( 2Nf, 2, 0) and the scalar in the gauge
multiplet as ( 1, 1, 2). It will be important that the symmetry of the hypermultip lets is
O(2Nf ) and not SO(2Nf ); for instance there is a “parity” symmetry, Z2 ⊂O(2Nf ), acting
as
ρ :Q1 ↔ ~Q1 (3.2)
with all other squarks invariant.
Globally, the symmetry group is not quite the product of O(2NF ) ×SU (2)R ×U (1)R
with the Lorentz group. A Z2 ⊂ U (1)R is isomorphic to ( −1)F which is in the Lorentz
group. Also, when combined with the center of the SU (2)R, this Z2 acts the same as the
Z2 in the center of O(2Nf ).
As in the abelian example, there is always a ﬂat direction wit h non zero φ. Along
this direction the gauge symmetry is broken to U (1) and all the quarks are massive. Only
U (1)R is spontaneously broken there. We will refer to this branch o f the moduli space as
the Coulomb branch. For Nf = 0, 1 there are no other ﬂat directions, but such directions
appear (when mi = 0) for Nf ≥ 2. Since the gauge symmetry is completely broken along
these ﬂat directions, we will refer to them as the Higgs branc hes. The Higgs branches can
be analyzed as follows.
First, it follows from requiring that the superpotential be stationary and the D terms
vanish that on the Higgs branches, Φ must be zero. The ﬂat dire ctions in Q space are
found by setting to zero the D terms, dividing by the gauge group SU (2), and asking
for the superpotential to be stationary. The combined opera tion of setting the D terms
to zero and dividing by SU (2) is equivalent to dividing by SL(2, C). The quotient by
SL(2, C) of the space of squarks can be parametrized by the SL(2, C)-invariant functions
V rs =Qr aQsa of the squarks; here r,s = 1... 2Nf and a are the ﬂavor and color indices,
andV rs = −V sr. V generates the ring of SL(2, C)-invariant polynomials in the Q’s. The
V ’s are not independent but obey certain quadratic equations stating that V is of rank
11
two. For Nf = 2, there is a single such equation
ǫrstuV rsV tu = 0. (3.3)
We still must impose the condition that the superpotential s hould be stationary. Since
the superpotential is linear in Φ, and Φ = 0, the only non-triv ial condition is ∂W/∂ Φ = 0,
or Xab = 0 with Xab =∑
rQr aQr b. This is equivalent to
0 = QraQsbXab = −V rtV ts (3.4)
for arbitrary r,s .
For example, the above equations can be analyzed as follows f orNf = 2. The symme-
try group O(4) is locally SU (2) ×SU (2), and the antisymmetric tensor V rs decomposes
as ( 3, 1) ⊕ (1, 3); we will call the two pieces VL and VR. The symmetric tensor in (3.4)
transforms as ( 1, 1) ⊕ (3, 3). The ( 3, 3) piece is bilinear in VL and VR and so vanishes if
and only if VL = 0 or VR = 0. There are thus two Higgs branches, with V being self-dual
or anti-self-dual. The ( 1, 1) part of (3.4) gives VL2 = 0 (or VR2 = 0, for the other branch),
which actually duplicates the content of (3.3). By VL2 we mean of course v12 +v22 +v32
wherevr =V r4. The manifold given by the equation v12 +v22 +v32 = 0 for three complex
variablesvi is equivalent to the quotient C2/Z2,2 and so admits a ﬂat hyperkahler metric
with a Z2 orbifold singularity at the origin.
Thus in particular, for Nf = 2, there are two Higgs branches which meet each other
and the Coulomb branch at the origin. The two branches are exc hanged by the “parity”
symmetry generated by ρ of (3.2). For Nf > 3, instead, there is a single irreducible Higgs
branch (this follows, for instance, from the symmetries) wh ich meets the Coulomb branch
at the origin.
Along the Higgs branches the U (1)R symmetry is unbroken and the other global
symmetry is broken as
O(2Nf ) ×SU (2)R →
{ SU (2) ×SU (2)R′ for Nf = 2
O(2Nf − 4) ×SU (2) ×SU (2)R′ for Nf ≥ 3 (3.5)
2 Introduce new variables a, b , deﬁned up to an overall sign, by v1 + iv2 = a2, v 1 − iv2 =
b2, v 3 = iab.
12
where the ﬁrst SU (2) is a diagonal subgroup of an SU (2) ⊂ SO(4) ⊂ SO(2Nf ) and the
SU (2) gauge symmetry. SU (2)R′ is a diagonal subgroup of the other SU (2) ⊂ SO(4) ⊂
SO(2Nf ) and the original SU (2)R symmetry. The massless ﬁelds transform like
{ (1, 3) ⊕ (1, 1) for Nf = 2
(2Nf − 4, 2, 2) ⊕ (1, 1, 3) ⊕ (1, 1, 1) for Nf ≥ 3 (3.6)
The boson in the last representation labels inequivalent gr ound states. The other bosons
are the Goldstone bosons.
