---
doc_id: alvarez-gaume-moore-vafa-1986-theta-functions-modular-invari
doc_title: "Theta Functions, Modular Invariance, and Strings"
section_id: sec-014-4-holomorphic-factorization
section_title: "Holomorphic Factorization"
section_number: 4
pages: 18-20
source_pdf: alvarez-gaume-moore-vafa-1986-theta-functions-modular-invariance-and-strings.pdf
source_sha256: c99ca1cd756f7aa6
doc_brief: "Theta Functions, Modular Invariance, and Strings — We use Quillen's theorem and algebraic geometry to investigate the modular transformation properties of some quantities of interest in string"
---
Quillen [15] has recently pointed out that functional determinants of operators on
Riemann surfaces have interesting holomorphic properties. We will use these
properties to investigate the Dirac determinant. However, holomorphic factoriza-
tion has other important applications. For example, as pointed out in [16,17,18]
the very existence of chiral string theories relies on the existence of such
holomorphic square roots.
In this section we will review the statement of Quillen's theorem and its relation
to the geometry of determinant line bundles. We first give an heuristic Feynman-
diagram proof of the theorem, and then proceed to the heat kernel proof of a slight
generalization of the theorem. This generalization can also be understood in the
context of determinant line bundles. In a beautiful recent paper [18] Belavin and
Knizhnik have used similar methods to investigate the holomorphic properties of
functional determinants on Teichmϋller space. For completeness we extend the
heuristic discussion of Quillen's theorem to rederive their results at the end of this
section.
Abstractly, we will consider families of operators Dy:Ln->Ln + 2. If the
parameter space Y is a complex manifold, the Dy can vary holomorphically with y.
Quillen showed that in this case the determinant line bundle i?-» Fcan be given a
holomorphic structure, and, if Dy has no index, then the ζ-regulated determinant
satisfies ntπ_ -«u +π I2 (ά u
Here detDy is a holomorphic function on Y. The "counterterm" q is defined by
choosing an operator Do to define the origin on Y and setting
2π (4.2)
Theta Functions, Modular Invariance, and Strings 19
The notation means that the family of operators is chosen so that any two differ by
a one form. The trace is a finite dimensional trace over the fiber indices. Note that
detD also depends on the choice of Do.
More concretely, we can give a simple proof of Quillen's theorem using
Feynman diagrams. Locally, Dy looks like d + A, so we can interpret A as a gauge
field. Since the obstruction to holomorphic factorization is local in A we should be
able to rederive (4.2) from perturbation theory. In perturbation theory
W=logdetζ/)ti> (4.3)
is simply given by a sum of Feynman diagrams
Λ/\Λ/ J\f\f\s
All diagrams but the first are convergent without regularization. Since the fields
are massless their sum is a functional of the form /[ΛJ+/D4J. Thus their
contribution to the determinant is gauge invariant and factorizes holomorphically
as a functional of Az. The situation is rather different for the vacuum polarization
graph, which must be regulated. One can use Pauli-Villars regularization to
maintain gauge invariance. Then as the PV mass goes to infinity one finds the
nonholomorphic residue
q=±-ld2zAgAs. (4.4)
2π Σ
It is more illuminating, however, to follow the two-dimensional calculation in
[19]. From the axial anomaly we know that to order A2 the contribution of a Weyl
fermion to the vacuum functional is (in momentum space)
§kϊ-'y <45)
If we are computing detDfD we must add the other chirality. The result
continues to satisfy holomorphic factorization, but is not gauge invariant. We can
restore gauge invariance - at the cost of factorization - by adding the counterterm
2π J (2π)2 '
which is Quillen's counterterm [20].
In applications to string theory we will need to generalize (4.1)-(4.2) to the case
when D has an index, in order to handle the ghost operators. Therefore, we now
give a heat kernel proof of the Quillen theorem in the case that Dy has a nonzero
