---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Proceedings of Symposia in Pure Mathematics"
section_id: sec-006-10-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 10
pages: 10-12
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems Ron Y. Donagi Contents Introduction §1. Some physics background Electromagnetism Yang-Mills theory Quantization Supersymmetry N = 2 super Yang-Mills — 17 sections: RO"
---
transform as a scalar under p0. This is unsatisfactory, since some free theories (e.g.
of one real scalar ﬁeld plus one real vector ﬁeld, [ F r]; such theories are not covered
by the Coleman-Mandula theorem) do admit conserved vectors and tensors, which
should survive under small perturbation.
The tasks of mixing the two particle types and of avoiding the Coleman-
Mandula restriction can fortunately be accomplished simul taneously through the
introduction of super Lie algebras: even elements preserve particle types, odd el-
ements exchange them. The even part of the algebra obeys Cole man-Mandula,
but there is room for odd symmetries and the corresponding od d, or spinorial,
conserved quantities. A theorem of Haag, Sohnius and Lopusz anski classiﬁes the
possible super Lie algebras of symmetries of physically int eresting theories: there
are the N -extended super Poincare algebras, as well as some central e xtensions and
variants including an (even) gauge algebra g acting on the odd sector.
N=2 Super Y ang-Mills
The setting for Montonen-Olive duality [ MO], for the work of Seiberg-Witten
[SW1, SW2 ], and for the development discussed in later sections, is N = 2 super-
symmetric Yang-Mills theory (SYM) in four-dimensional spa ce. The Lagrangian
for this theory is usually written in terms of super ﬁelds on a n aﬃne SUSY space
[WB], making the super Poincare invariance evident. When writt en out explicitly
in terms of its component ﬁelds, the Lagrangian is quite comp licated. It starts with
a purely bosonic term analogous to the usual Yang-Mills Lagr angian∫ Tr(F ∧ ∗F ).
Additional terms, involving additional ﬁelds, are require d for the N = 2 supersym-
metry. The ﬁelds involved are grouped into N = 1 multiplets (representations of
the N = 1 super Poincare algebra), which in turn combine into N = 2 multiplets.
Such a theory depends, of course, on the choice of a compact ga uge group G.
For a given G there is the pure N = 2 theory, analogous to Maxwell’s equations
in vacuo, containing only those ﬁelds and terms in the Lagran gian required for
supersymmetry. There are also various theories in which som e combination of
additional fermionic (“matter”) particles is thrown in. We will return to these
shortly.
Each SYM theory has a moduli space B of vacuum states (= eigenstates of
the Hamiltonian or energy operator corresponding to the low est eigenvalue). This
is of course a consequence of the degeneracy, or of the gauge i nvariance, of the
Lagrangian: a non-degenerate Lagrangian should correspon d to a unique vacuum,
and an ordinary degeneracy is obtained when two eigenvalues happen to coincide,
so there are two (or more) independent vacua. The situation i n gauge theory is
that there is a continuum B of independent vacua. The complex dimension of B is
the rank r of G, and we can in fact describe a coordinate system ( ui), i = 1,...,r ,
on it. First, the classical analogue: the classical potenti al is
V (ϕ) = 1
g2 Tr[ϕ,ϕ †]2,
where g is a coupling constant (a parameter in the Lagrangian), and ϕ is a Higgs
ﬁeld – a complex ﬁeld transforming as a scalar under Poincare , and in the adjoint
representation of G. Since [ ϕ,ϕ †] is self-adjoint, the minima occur precisely when
ϕ commutes with ϕ†. This locus is G-invariant: it is the union of the G-orbits
of elements in the Cartan subalgebra t of the complexiﬁed Lie algebra gC. The
quotient by G is thus B = t/W , where W is the Weyl group. For example, when
SEIBERG-WITTEN INTEGRABLE SYSTEMS 11
G = SU(n) we have t ≈ Cn−1, and the quotient is again Cn−1, with coordinates
u2 = Trϕ2,...,u n = Trϕn. (The reader will no doubt recognize this as a (real)
symplectic reduction: the action of G on gC is Hamiltonian with respect to the
natural translation-invariant symplectic structure indu ced on the real vector space
underlying gC by the imaginary part of the Killing form. The moment map send s
ϕ to Tr[ϕ,ϕ †], and the symplectic quotient is gC//G =B = t/W . We will run into
the complex analogue of symplectic quotients in the discuss ion of linearity in the
next section.)
Now the constraints imposed by N = 2 supersymmetry (i.e. the diﬃculty of
writing down a supersymmetric Lagrangian) imply that the qu antum moduli space
remains the same B, as an abstract algebraic variety, so it still has the coordi nates
ui. But we will see that just about all other features of B change in going from
the classical to the quantum: for example, this applies to th e K¨ ahler metric on it,
the locus of singularities (of the metric), the ﬂat structur e, and the relation of the
u coordinates to the natural ﬁelds in the theory.
A central quantity in any SYM theory is the electric charge a, which is the
vector of eigenvalues of the Higgs ﬁeld ϕ. It lives in the Cartan, t. For SU(2) this
is a complex number, as is u. We can take ϕ to have eigenvalues ± a
2 , and then
u = Trϕ2 = a2
2 , in the classical theory. In the quantum theory, this relati onship
still holds approximately as u → ∞, by the asymptotic freedom of the theory. But
for ﬁnite u we will see that the relationship is very diﬀerent.
A crucial property of these theories is that their low-energ y (read: real-world
observable) behavior can be described in terms of only a ﬁnit e number of parameters
– the coordinates ui on the quantum moduli space B. This description is via a “low
energy eﬀective Lagrangian” Leﬀ , obtained from the full Lagrangian through a
process of averaging over all heavy degrees of freedom. So al l measurable quantities
become (locally) functions on B. In particular, this applies to the components
ai =ai(u) of the electric charge. Supersymmetry implies that these f unctions are
holomorphic, and we will use them as alternative local coord inates on B.
While the existence of Leﬀ is guaranteed by the general theory, its actual com-
putation can be extremely diﬃcult. The supersymmetry allow s Leﬀ to be expressed
locally in terms of a single holomorphic function F = F(a), the prepotential. (This
is due to Seiberg, cf. [ SW1], (2.7) and (2.11). Note that we need F as a function
of a, not of u.) All other quantities in the theory can then be expressed in terms
of F and the coordinates a. This includes the vector
aD = dF
da,
whose physical signiﬁcance will appear shortly; the matrix
τ (a) = d2F
da2 = daD
da ,
which is a complexiﬁed coupling constant (for SU(2), the low -energy eﬀective values
of the real coupling constant g (encountered in the potential V (ϕ)) and of a phase
angleθ are given byτ = θ
2π + 4πi
g2 . In particular, F(a) must be such that Im(τ )> 0);
the K¨ ahler metric
ds2 = Im(τdad ¯a) = Im(daDd¯a)
