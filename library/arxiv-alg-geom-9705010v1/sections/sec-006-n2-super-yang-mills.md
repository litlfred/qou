---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-006-n2-super-yang-mills
section_title: "N=2 Super Yang-Mills"
section_number: null
pages: 10-12
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
The setting for Montonen-Olive duality [MO], for the work of Seiberg-Witten
[SW1, SW2], and for the development discussed in later sections, is N = 2 super-
symmetric Yang-Mills theory (SYM) in four-dimensional space. The Lagrangian
for this theory is usually written in terms of super ﬁelds on an aﬃne SUSY space
[WB], making the super Poincare invariance evident. When written out explicitly
in terms of its component ﬁelds, the Lagrangian is quite complicated. It starts with
a purely bosonic term analogous to the usual Yang-Mills Lagrangian R Tr(F ∧∗F).
Additional terms, involving additional ﬁelds, are required for the N = 2 supersym-
metry. The ﬁelds involved are grouped into N = 1 multiplets (representations of
the N = 1 super Poincare algebra), which in turn combine into N = 2 multiplets.
Such a theory depends, of course, on the choice of a compact gauge group G.
For a given G there is the pure N = 2 theory, analogous to Maxwell’s equations
in vacuo, containing only those ﬁelds and terms in the Lagrangian required for
supersymmetry.
There are also various theories in which some combination of
additional fermionic (“matter”) particles is thrown in.
We will return to these
shortly.
Each SYM theory has a moduli space B of vacuum states (= eigenstates of
the Hamiltonian or energy operator corresponding to the lowest eigenvalue). This
is of course a consequence of the degeneracy, or of the gauge invariance, of the
Lagrangian: a non-degenerate Lagrangian should correspond to a unique vacuum,
and an ordinary degeneracy is obtained when two eigenvalues happen to coincide,
so there are two (or more) independent vacua. The situation in gauge theory is
that there is a continuum B of independent vacua. The complex dimension of B is
the rank r of G, and we can in fact describe a coordinate system (ui), i = 1, . . . , r,
on it. First, the classical analogue: the classical potential is
V (ϕ) = 1
g2 Tr[ϕ, ϕ†]2,
where g is a coupling constant (a parameter in the Lagrangian), and ϕ is a Higgs
ﬁeld – a complex ﬁeld transforming as a scalar under Poincare, and in the adjoint
representation of G. Since [ϕ, ϕ†] is self-adjoint, the minima occur precisely when
ϕ commutes with ϕ†. This locus is G-invariant: it is the union of the G-orbits
of elements in the Cartan subalgebra t of the complexiﬁed Lie algebra gC. The
quotient by G is thus B = t/W, where W is the Weyl group. For example, when
SEIBERG-WITTEN INTEGRABLE SYSTEMS
11
G = SU(n) we have t ≈Cn−1, and the quotient is again Cn−1, with coordinates
u2 = Tr ϕ2, . . . , un = Tr ϕn. (The reader will no doubt recognize this as a (real)
symplectic reduction: the action of G on gC is Hamiltonian with respect to the
natural translation-invariant symplectic structure induced on the real vector space
underlying gC by the imaginary part of the Killing form. The moment map sends
ϕ to Tr[ϕ, ϕ†], and the symplectic quotient is gC//G = B = t/W. We will run into
the complex analogue of symplectic quotients in the discussion of linearity in the
next section.)
Now the constraints imposed by N = 2 supersymmetry (i.e. the diﬃculty of
writing down a supersymmetric Lagrangian) imply that the quantum moduli space
remains the same B, as an abstract algebraic variety, so it still has the coordinates
ui. But we will see that just about all other features of B change in going from
the classical to the quantum: for example, this applies to the K¨ahler metric on it,
the locus of singularities (of the metric), the ﬂat structure, and the relation of the
u coordinates to the natural ﬁelds in the theory.
A central quantity in any SYM theory is the electric charge a, which is the
vector of eigenvalues of the Higgs ﬁeld ϕ. It lives in the Cartan, t. For SU(2) this
is a complex number, as is u. We can take ϕ to have eigenvalues ± a
2, and then
u = Tr ϕ2 = a2
2 , in the classical theory. In the quantum theory, this relationship
still holds approximately as u →∞, by the asymptotic freedom of the theory. But
for ﬁnite u we will see that the relationship is very diﬀerent.
A crucial property of these theories is that their low-energy (read: real-world
observable) behavior can be described in terms of only a ﬁnite number of parameters
– the coordinates ui on the quantum moduli space B. This description is via a “low
energy eﬀective Lagrangian” Leﬀ, obtained from the full Lagrangian through a
process of averaging over all heavy degrees of freedom. So all measurable quantities
become (locally) functions on B.
In particular, this applies to the components
ai = ai(u) of the electric charge. Supersymmetry implies that these functions are
holomorphic, and we will use them as alternative local coordinates on B.
While the existence of Leﬀis guaranteed by the general theory, its actual com-
putation can be extremely diﬃcult. The supersymmetry allows Leﬀto be expressed
locally in terms of a single holomorphic function F = F(a), the prepotential. (This
is due to Seiberg, cf. [SW1], (2.7) and (2.11). Note that we need F as a function
of a, not of u.) All other quantities in the theory can then be expressed in terms
of F and the coordinates a. This includes the vector
aD = dF
da ,
whose physical signiﬁcance will appear shortly; the matrix
τ(a) = d2F
da2 = daD
da ,
which is a complexiﬁed coupling constant (for SU(2), the low-energy eﬀective values
of the real coupling constant g (encountered in the potential V (ϕ)) and of a phase
angle θ are given by τ =
θ
2π + 4πi
g2 . In particular, F(a) must be such that Im(τ) > 0);
the K¨ahler metric
ds2 = Im(τ da d¯a) = Im(daD d¯a)
12
RON Y. DONAGI
which was mentioned above; and its K¨ahler potential
K = K(a, ¯a) = Im
 X
i
aD
i ¯ai
!
= Im
 X
i
dF
dai
¯ai
!
.
The eﬀective Lagrangian itself is given as a sum of kinetic and potential parts, each
a Berezin integral over an N = 1 SUSY aﬃne space of dimensions (4,4) and (4,2),
respectively:
Leﬀ= 1
4π
Z
K(Φ, ¯Φ)d4η + 1
8πIm
Z
τ(Φ)|W|2d2η.
Here Φ and W are the two N = 1 multiplets which together make up the N = 2
multiplet containing the Higgs ﬁeld ϕ. (ϕ and a fermion ψ are the ﬁelds in the
“chiral multiplet” Φ. The “vector multiplet” W contains another fermion λ and
the gauge ﬁeld A. It can be thought of as the ﬁeld strength, N = 1 super analogue
of the curvature F in ordinary Y M.) The integrands involve an analytic function
(τ) or the real part of one (K); this function is to be applied formally to the super
ﬁelds Φ, W and their conjugates. The integration over the four (or two) odd space
directions η is interpreted via Berezin’s recipe as a derivative, or as the reading oﬀ
of the relevant coeﬃcients. (The second term is actually written as an integral over
a (4,2)-dimensional “chiral” quotient of the full (4,4)-dimensional SUSY space, in
which two of the odd directions have been reduced.
What is missing is an explicit expression for F. Traditionally, F was written as
an inﬁnite sum involving its classical (“tree level”) value, the one-loop correction
which is logarithmic in a (higher loop contributions were known to vanish), and an
inﬁnite sum of mysterious instanton corrections involving negative powers of a. The
breakthrough came when Seiberg and Witten succeeded, in [SW1], in computing
F (and hence Leﬀ, ds2, etc.) exactly, for the pure N = 2 theory with G = SU(2).
Their solution is based on the global properties of the theory.
