---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-005-supersymmetry
section_title: "Supersymmetry"
section_number: null
pages: 8-10
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
Supermathematics is the habit of adding the preﬁx “super” to ordinary, com-
mutative objects, to denote their sign-commutative generalization. Thus, a super
space is a locally ringed topological space whose structure sheaf O = O0 ⊕O1 is Z2
graded, O0 is central, and multiplication O1 × O1 →O0 is skew symmetric. Aﬃne
super space Rm,n is the topologcal space Rm with the sheaf C∞(Rm) ⊗Λ·(Rn)
and the Z2 grading coming from the Z-grading of the exterior algebra. An (m, n)-
dimensional super manifold is a super space which is locally isomorphic to Rm,n
(The isomorphisms are, of course, isomorphisms of Z2-graded algebras, and need
not preserve any Z-grading. A typical automorphism of R1,2, with even coordinate
x and odd coordinates θ1, θ2, may send x to x + θ1θ2. So the identiﬁcation of O
as C∞tensor exterior algebras is not preserved under coordinate change.) All of
calculus extends to super manifolds. The only non-obvious point is that the trans-
formation law for diﬀerential forms involves the determinant of the transformation
in the even variables, but the inverse determinant of the transformation in the odd
variables, and a hybrid – the Berezinian – for a general transformation mixing the
parities. The resulting operation of integration looks, in the odd directions, more
like usual diﬀerentiation, i.e., in local coordinates x1, . . . , xm, θ1, . . . , θn it reads oﬀ
the coeﬃcient of the top odd part, Πn
i=1dθi.
The inﬁnitesimal symmetries of a super manifold are described by a super Lie
algebra: a Z2-graded algebra g = g0 ⊕g1 with a [ , ] operation which is sign-
antisymmetric and satisﬁes the only reasonable version of the Jacobi identity:
3
X
i=1
(−1)xi−1xi+1[Xi−1, [Xi, Xi+1]] = 0,
where the Xi (i ∈Z3) are in gxi. In particular g0 is an ordinary Lie algebra, and g1
is a g0-module with a g0-valued symmetric bilinear form [ , ] with respect to which
SEIBERG-WITTEN INTEGRABLE SYSTEMS
9
g0 acts as derivations:
[X, [θ1, θ2]] = [[X, θ1], θ2] + [θ1, [X, θ2]],
for X ∈g0, θi ∈g1. The basic example is the Poincare super algebra p = p0 + p1,
whose even part p0 is the usual Poincare algebra, and whose odd part p1 is the
spinor module S of the Lorentz group SO(3, 1). (The Poincare group P0 acts, via its
quotient SO(3, 1), on p1; this induces the inﬁnitesimal action of p0.) The pairing
γ: p1 × p1 →p0 is Cliﬀord multiplication, with image the translation subgroup of
p0. A physicist would write everything in coordinates, so γ becomes the collection
of Pauli or Dirac matrices (depending on whether real or complex forms are used).
The N-extended super Poincar´e algebra has the same p0, but p1 is replaced by
S⊕N, the sum of N orthogonal copies of the spinors.
A supersymmetric (“SUSY”) space is the super analogue of a homogeneous
space for the super Poincar´e algebra or its N-extended version. An aﬃne example is
(V, O), where V is a vector space with non-degenerate quadratic form (of signature
(3, 1), in our case), and O is given in terms of the spinor module S = S(V ) as
C∞(V ) ⊗Λ·(S⊕N). For more details on SUSY spaces, we refer to [Be], where they
are deﬁned to be super manifolds modelled on the above aﬃne example.
An N = 1 SUSY theory is a theory (i.e. a Lagrangian involving certain ﬁelds)
with an inﬁnitesimal action of the super Poincar´e algebra.
Likewise, a theory
“with N supersymmetries” has an action of the N-extended Poincar´e super algebra.
These theories can often, though not always, be described in terms of a super
Poincar´e invariant Lagrangian involving superﬁelds on a SUSY space. The ordinary
Lagrangian, on ordinary space, is recovered by Berezin integration along all the
odd directions. The classic reference on supersymmetry is [WB]. A possibly more
friendly introduction is [Fr], and the most geometrical version is [Be]. The ﬁrst
two references include a study of the supersymmetric version of Yang-Mills theory.
In physics, there are two types of particles: bosons, which combine with each
other freely, and fermions, whose combinations are restricted by Pauli’s exclusion
principle. Mathematically, the distinction is roughly this: consider a collection of
n particles with distinct physical properties. If Hi is the quantum Hilbert space
of states of the ith particle, then the space of states of the entire collection is
⊗n
i=1Hi.
Now if instead we have n identical particles, there are fewer distinct
states of the ensemble: for bosons we get SymnH, while for fermions, ΛnH. In
four dimensional theories, bosonic particles ordinarily live in representations of the
Poincare group with integer spin, while fermions have half-integer (that is, non-
integer) spin.
(This is the “spin-statistics” theorem.)
Most “matter” particles
(electrons, protons, quarks) are fermions; photons are bosons.
At a somewhat superﬁcial level, the motivation for introducing supersymmetry
is to be able to treat the two types of particles uniformly. A complementary and
deeper reason is based on the no-go theorem of Coleman and Mandula (cf. [Fr],
[WB]). This says that the most general algebra of symmetries of a class of quan-
tum theories satisfying some rather reasonable non-degeneracy assumptions (one
of these is non-freeness, another is the existence of massive particles) is of the form
p0⊕g, where p0 is the Poincar´e algebra of space-time isometries, and g is the gauge
algebra. The point is that this is a direct sum (of algebras), so there can be no
non-trivial mixing of the two symmetries. Since symmetries are equivalent to con-
served quantities, this implies for instance that any conserved quantity (“current”)
other than energy-momentum and angular momentum (which come from p0) must
10
RON Y. DONAGI
transform as a scalar under p0. This is unsatisfactory, since some free theories (e.g.
of one real scalar ﬁeld plus one real vector ﬁeld, [Fr]; such theories are not covered
by the Coleman-Mandula theorem) do admit conserved vectors and tensors, which
should survive under small perturbation.
The tasks of mixing the two particle types and of avoiding the Coleman-
Mandula restriction can fortunately be accomplished simultaneously through the
introduction of super Lie algebras: even elements preserve particle types, odd el-
ements exchange them.
The even part of the algebra obeys Coleman-Mandula,
but there is room for odd symmetries and the corresponding odd, or spinorial,
conserved quantities. A theorem of Haag, Sohnius and Lopuszanski classiﬁes the
possible super Lie algebras of symmetries of physically interesting theories: there
are the N-extended super Poincare algebras, as well as some central extensions and
variants including an (even) gauge algebra g acting on the odd sector.
