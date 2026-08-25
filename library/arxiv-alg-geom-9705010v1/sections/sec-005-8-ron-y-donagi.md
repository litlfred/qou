---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-005-8-ron-y-donagi
section_title: "RON Y. DONAGI"
section_number: 8
pages: 8-10
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
doc_brief: "Seiberg-Witten Integrable Systems — 17 sections: RON Y. DONAGI; Introduction; References"
---
to β <0 for small values of g. In the boundary case where β is identically 0, the
theory is scale-invariant.
An additional complication is involved in the quantization of theories which are
(that is, their Lagrangian is) gauge-invariant. The proble m with gauge-invariant
theories stems from the degeneracy of their Lagrangian. In c lassical gauge theory,
the classical solutions (extrema of the action) are not isol ated, but come in entire
gauge-group orbits. The equivalence of the Lagrangian and H amiltonian descrip-
tions breaks down: this equivalence is based on a Legendre tr ansform, which makes
sense only near isolated points. In the quantized theory, th e path integral needs
to be taken not over all paths, but over gauge-equivalence cl asses. This is seen
already for the free (unperturbed) theory: the value of a Gau ssian integral is given
by the inverse determinant of the operator in the exponent; d egeneracy (or gauge
invariance) implies that this determinant vanishes, and ne eds to be replaced by a
determinant on an appropriate transversal slice or quotien t. For quantized Yang-
Mills, or gauge, theories, a good reference is [ FS]. The reward for handling these
additional complications is a collection of theories which are renormalizable and
sometimes asymptotically free: the beta-function of the ba sic theory (correspond-
ing to Maxwell’s in vacuo) is negative. The coupling to matte r increases beta, but
it remains negative when the number of quarks is small enough .
Supersymmetry
Supermathematics is the habit of adding the preﬁx “super” to ordinary, com-
mutative objects, to denote their sign-commutative genera lization. Thus, a super
space is a locally ringed topological space whose structure sheaf O = O0 ⊕ O1 is Z2
graded, O0 is central, and multiplication O1 × O1 → O0 is skew symmetric. Aﬃne
super space Rm,n is the topologcal space Rm with the sheaf C∞(Rm) ⊗ Λ ·(Rn)
and the Z2 grading coming from the Z-grading of the exterior algebra. An ( m,n )-
dimensional super manifold is a super space which is locally isomorphic to Rm,n
(The isomorphisms are, of course, isomorphisms of Z2-graded algebras, and need
not preserve any Z-grading. A typical automorphism of R1,2, with even coordinate
x and odd coordinates θ1, θ2, may send x to x +θ1θ2. So the identiﬁcation of O
as C∞ tensor exterior algebras is not preserved under coordinate change.) All of
calculus extends to super manifolds. The only non-obvious p oint is that the trans-
formation law for diﬀerential forms involves the determina nt of the transformation
in the even variables, but the inverse determinant of the tra nsformation in the odd
variables, and a hybrid – the Berezinian – for a general transformation mixing the
parities. The resulting operation of integration looks, in the odd directions, more
like usual diﬀerentiation , i.e., in local coordinates x1,...,x m,θ 1,...,θ n it reads oﬀ
the coeﬃcient of the top odd part, Π n
i=1dθi.
The inﬁnitesimal symmetries of a super manifold are describ ed by a super Lie
algebra: a Z2-graded algebra g = g0 ⊕ g1 with a [ , ] operation which is sign-
antisymmetric and satisﬁes the only reasonable version of t he Jacobi identity:
3∑
i=1
(−1)xi−1xi+1[Xi−1, [Xi,X i+1]] = 0,
where the Xi (i ∈ Z3) are in gxi. In particular g0 is an ordinary Lie algebra, and g1
is a g0-module with a g0-valued symmetric bilinear form [ , ] with respect to which
SEIBERG-WITTEN INTEGRABLE SYSTEMS 9
g0 acts as derivations:
[X, [θ1,θ 2]] = [[X,θ 1],θ 2] + [θ1, [X,θ 2]],
for X ∈ g0, θi ∈ g1. The basic example is the Poincare super algebra p = p0 + p1,
whose even part p0 is the usual Poincare algebra, and whose odd part p1 is the
spinor module S of the Lorentz group SO(3, 1). (The Poincare group P0 acts, via its
quotient SO(3, 1), on p1; this induces the inﬁnitesimal action of p0.) The pairing
γ: p1 × p1 → p0 is Cliﬀord multiplication, with image the translation subg roup of
p0. A physicist would write everything in coordinates, so γ becomes the collection
of Pauli or Dirac matrices (depending on whether real or comp lex forms are used).
The N -extended super Poincar´ e algebra has the same p0, but p1 is replaced by
S⊕N , the sum of N orthogonal copies of the spinors.
A supersymmetric (“SUSY”) space is the super analogue of a ho mogeneous
space for the super Poincar´ e algebra or itsN -extended version. An aﬃne example is
(V, O), where V is a vector space with non-degenerate quadratic form (of sig nature
(3, 1), in our case), and O is given in terms of the spinor module S = S(V ) as
C∞(V ) ⊗ Λ ·(S⊕N ). For more details on SUSY spaces, we refer to [ Be], where they
are deﬁned to be super manifolds modelled on the above aﬃne ex ample.
An N = 1 SUSY theory is a theory (i.e. a Lagrangian involving certa in ﬁelds)
with an inﬁnitesimal action of the super Poincar´ e algebra. Likewise, a theory
“with N supersymmetries” has an action of the N -extended Poincar´ e super algebra.
These theories can often, though not always, be described in terms of a super
Poincar´ e invariant Lagrangian involving superﬁelds on a SUSY space. The ordinary
Lagrangian, on ordinary space, is recovered by Berezin inte gration along all the
odd directions. The classic reference on supersymmetry is [ WB]. A possibly more
friendly introduction is [ F r], and the most geometrical version is [ Be]. The ﬁrst
two references include a study of the supersymmetric versio n of Yang-Mills theory.
In physics, there are two types of particles: bosons, which c ombine with each
other freely, and fermions, whose combinations are restric ted by Pauli’s exclusion
principle. Mathematically, the distinction is roughly thi s: consider a collection of
n particles with distinct physical properties. If Hi is the quantum Hilbert space
of states of the i th particle, then the space of states of the entire collection i s
⊗n
i=1Hi. Now if instead we have n identical particles, there are fewer distinct
states of the ensemble: for bosons we get Sym nH, while for fermions, Λ nH. In
four dimensional theories, bosonic particles ordinarily l ive in representations of the
Poincare group with integer spin, while fermions have half- integer (that is, non-
integer) spin. (This is the “spin-statistics” theorem.) Mo st “matter” particles
(electrons, protons, quarks) are fermions; photons are bos ons.
At a somewhat superﬁcial level, the motivation for introduc ing supersymmetry
is to be able to treat the two types of particles uniformly. A c omplementary and
deeper reason is based on the no-go theorem of Coleman and Man dula (cf. [ F r],
[WB]). This says that the most general algebra of symmetries of a class of quan-
tum theories satisfying some rather reasonable non-degene racy assumptions (one
of these is non-freeness, another is the existence of massiv e particles) is of the form
p0 ⊕ g, where p0 is the Poincar´ e algebra of space-time isometries, and g is the gauge
algebra. The point is that this is a direct sum (of algebras), so there can be no
non-trivial mixing of the two symmetries. Since symmetries are equivalent to con-
served quantities, this implies for instance that any conse rved quantity (“current”)
other than energy-momentum and angular momentum (which com e from p0) must
