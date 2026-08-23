---
doc_id: helicity03mmj
doc_title: "Geometry of higher helicities"
section_id: sec-005-33-ergodic-meaning-of-the-calabi-invariant
section_title: "Ergodic meaning of the Calabi invariant."
section_number: 3.3
pages: 8-10
source_pdf: helicity03mmj.pdf
source_sha256: e364dad3afff3180
doc_brief: "Geometry of higher helicities — We revisit an interpretation of higher-dimensional helicities and Hopf–Novikov invariants from the point of view of the Brownian ergodic theorem."
---
ﬁelds with an invariant solid torus knotted in a complicated way. However, in
the case of a “complicated ﬁeld” in a “simple” standard solid torus the following
approach based on the notion of Calabi invariant in symplectic geometry sometimes
gives sharper estimates, see [ 10], [ 12]. One has to note that the asymptotic Hopf
invariant (unlike the Hopf invariant for a map) is diﬃcult to ﬁnd explicitly for a
somewhat generic divergence-free vector ﬁeld. Here, however, we discuss the case
GEOMETRY OF HIGHER HELICITIES 997
where these calculations can be done explicitly for a ﬁeld in a solid torus, coming
from a generic area-preserving diﬀeomorphism of a two-disk.
Let D2 be a two-dimensional disk equipped with an area-form ω. Take any
primitive 1-form α, such that ω = dα. Consider a smooth area-preserving dif-
feomorphism φ of the disk, which is identity near the disk boundary. Then the
1-form φ∗α − α is closed and vanishes near ∂D. Hence there is a unique function
h(φ) : D2 → R, which vanishes near the boundary ∂D and satisﬁes
dh(φ) = φ∗α − α.
Deﬁnition 3.9. The Calabi invariant of the area-preserving diﬀeomorphism φ is
deﬁned by the integral:
C(φ) :=
∫
D2
h(φ) ω.
One can check that this integral does not depend on the choice of the primitive
1-form α, see, e. g., [ 10] or [ 2].
Remark 3.10. Another way to deﬁne this invariant is to consider a Hamiltonian
isotopy {φt}, t ∈ [0, 1], which starts with the identity map at t = 0, and at t = 1
coincides with φ. Such an isotopy can be deﬁned by a t-dependent Hamiltonian
function Ht : D2 → R, which vanishes near the boundary and satisﬁes the identity
dHt( . ) = ω
( ∂φt
∂t , .
)
for all t ∈ [0, 1]. Then one can show (see, e. g., [ 2]) that the Calabi invariant is
(twice) the volume under the graph of the Hamiltonian function Ht over D2 ×[0, 1]:
C(φ) = 2
∫ 1
0
∫
D2
Ht(x) ω dt,
Remark 3.11. One more deﬁnition of the Calabi invariant, due to A. Fathi, has
an ergodic meaning of an average orbit braiding, and was used in [ 10], [ 12] for a
variety of applications. Let {φt}, t ∈ [0, 1], be a Hamiltonian isotopy. Consider the
map
Angφ : ( D2 × D2) \ ∆ → R2,
which associates to any pair of points x ⁄= y in D2 the angular variation of the vector
from φt(x) to φt(y) when t goes from 0 to 1 (here ∆ stands for the diagonal). Note
that this map does not depend on the isotopy. Then the Calabi invariant is the
integral of this function (see [ 10]):
C(φ) =
∫ ∫
D2×D2
Angφ(x, y ) ωxωy.
Note that the latter deﬁnition is pure two-dimensional, while the former ones
allow generalizations to higher dimensional symplectic manifolds.
Problem 3.12 [10]. Find a higher-dimensional analog of the angular deﬁnition of
the Calabi invariant.
998 B. KHESIN
Consider a divergence-free vector ﬁeld ξ in a solid torus in R3 with a nonva-
nishing longitude component ∂/∂θ . It deﬁnes a Poincare map of a section, the
two-dimensional disk, from θ = 0 to θ = 2π. This Poincare map is area-preserving
(i. e. symplectic) for the area form ω = ωξ deﬁned by the substitution of this vector
ﬁeld to the volume 3-form (more precisely, by the restriction of this substitution to
a cross-section of the solid torus). One can describe the asymptotic linking num-
ber of the ﬁeld trajectories in the solitorus in terms of the Calabi invariant of the
Poincare map. The the latter deﬁnition was used to prove the homeomorphism in-
variance of the asymptotic linking (i. e., helicity) of a ﬁeld in a solid torus [ 10] and
to give more precise energy estimates for such ﬁelds in a torus in terms of average
braiding of their orbits [ 12]. The paper [ 11] shows, in particular, that signatures
of links behave much more regularly than their linking numbers under iterations
of the Poincare map. We also refer to [ 24] for a similar in spirit description of
an asymptotic version of the Bennequin invariant for a vector ﬁeld in a contact
manifold and an ergodic interpretation of the Godbillon-Vey class of a foliation of
codimension 1.
