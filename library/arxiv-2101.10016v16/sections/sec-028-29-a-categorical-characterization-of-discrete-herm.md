---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-028-29-a-categorical-characterization-of-discrete-herm
section_title: "A categorical characterization of discrete Hermitian coboundary wqh"
section_number: 29
pages: 180-183
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
29. A categorical characterization of discrete Hermitian coboundary
wqh
Let A be a discrete hermitian coboundary weak quasi-Hopf algebra. In this section we
give a categorical characterization of the axioms defining A. For simplicity, we discuss a
detailed proof only in the unitary case. It turns out that the categorical definition simplifies
considerably this structure.
Then the C
∗
-structure of A gives rise to the linear C
∗
-category C
+ = Rep+
(A) of Hilbert
space representations of A. We also have the tensor category C = Rep(A) of vector space
representations of A which has additional structure, the braiding, the ribbon structure and
coboundary symmetry.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 181
We recall that ribbon and coboundary structures in tensor categories have been studied
in Sect. 27. In particular, by Theorem 27.21 a coboundary symmetry c
w may be associated
to a ribbon category C with braided symmetry c, ribbon structure v ∈ (1, 1) when there
is a natural isomorphism w ∈ (1, 1) compatible with duality which is a square root of v.
In the setting of unitary categories when c and w are unitary then c
w is unitary, and also
selfadjoint as (c
w)2 = 1.
Theorem 29.1. Let (C, ⊗, α, c, v) be a ribbon category, w ∈ (1, 1) a square root of v
compatible with duality, C
+ a semisimple C∗
-category and let F : C
+ → C be a linear
equivalence. Let (G, F, G) : C → Herm (C → Hilb) be a faithful weak quasitensor functor
with symmetric dimension function such that G
+ = GF : C+ → Herm (C+ → Hilb) is
a
∗
-functor. Then the discrete pre-C
∗
-algebra A+ = Nat0(G
+) endowed with the natural
ribbon weak quasi-Hopf algebra structure and Ω-involution induced by duality becomes an
Hermitian (unitary) coboundary weak quasi-Hopf algebra if and only if G(α), G(c), and
G(v) are unitary and moreover (F, G) satisfies the following conditions
Fσ,ρΣ(ρ, σ)F
∗
ρ,σ = G(c
w
(ρ, σ)) (29.1)
G
∗
σ,ρΣ(ρ, σ)Gρ,σ = G(c
w
(σ, ρ)
−1
) (29.2)
with Σ the permutation symmetry of Herm (Hilb). In this case, C
+ becomes an Hermitian
(unitary) ribbon tensor category and F : C
+ → C a ribbon tensor equivalence.
Moreover there is a unitary ribbon tensor equivalence E : C
+ → Reph
(A) (C
+ →
Rep+(A)) preserving the coboundary structures such that FAE ≃ G unitarily monoidally,
with FA the forgetful functor of Rep+(A).
Remark 29.2. a) In the particular case of a trivial R-matrix, trivial ribbon element,
ordinary discrete (cocommutative) Hopf C
∗
-algebra, the categorical definition of unitary
coboundary weak quasi-Hopf algebra reduces to the property that embedding tensor functor Rep(A) → Hilb to the category of Hilbert spaces is a symmetric functor , by Theorem
29.1. For this reason, the class of unitary coboundary weak Hopf C
∗
-algebras plays a natural role in the Doplicher-Roberts program for braided tensor C
∗
-categories, see Problem
1.
b) In the non-cocommutative case (R ̸= I) with structure maps satisfying F = G∗
the equations 29.1, 29.2 say that the weak quasitensor functor (G, F, G) preserves the
coboundary symmetries of C
+ and Hilb. In particular, under the requirements F = G∗
,
equations 29.1, 29.2 uniquely determine the structure of the braided symmetry c(ρ, σ) of
C
+ on an irreducible component of the minimum energy subspace (and hence determine the
braided symmetry completely) as a scalar multiple of the permutation symmetry by the
action of the balancing element w. This form of the praided symmetry occurs in categories
arising from conformal field theory, with the braiding associated to the monodromy of the
KZ equations, see Corollary 35.1 for the loop group conformal net and Remark 38.16 for
the affine vertex operator algebra setting. This highlights the relevance of making module
categories of vertex operator algebras into unitary categories.
Proof. By theorem 7.6, A = Nat0(G) becomes a ribbon weak quasi-Hopf algebra with
coproduct and associator defined by (F, G) and R-matrix R defined in the proof and

182 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
ribbon structure G(vρ). We transfer this structure to A+ via the isomorphism A → A+
induced by F. By Prop. 26.4, A+ becomes naturally a unitary weak quasi-bialgebra if and
only if G(α) is unitary. The Ω-involution of A+ is given by Ω = F˜∗F˜ and Ω−1 = G˜G˜∗
respectively, where F˜ and G˜ correspond to F and G via the isomorphism, as in the proof of
Prop. 26.4. We have A˜+ = A
+
Ω
as weak quasi-bialgebras. When G(vρ) is unitary then the
natural transformation G(wF(x))) defines a unitary square root of the ribbon structure of
A+, and axioms a), b), c) of Def. 28.1 hold. We show that with this structure axiom d) is
equivalent to (29.1) and (29.2) if G(c) is unitary. Note that Aop = (A)R as quasitriangular
weak quasi-bialgebras. It follows that d) may equivalently be formulated as A˜+ = (A+)ER
as quasitriangular weak quasi-bialgebras together with the requirement that E is a trivial
twist, that is E
−1 = E′
, where E = ∆(I)
∗∆op(I) and E′ = ∆op(I)∆(I)∗
. On the other
hand, equations (29.1) and (29.2) are respectively equivalent to
ΣGσ,ρFσ,ρΣF
∗
ρ,σFρ,σ = ΣGσ,ρG(c
w
(ρ, σ))Fρ,σ, (29.3)
Gσ,ρG
∗
σ,ρΣGρ,σFρ,σΣ = Gσ,ρG(c
w
(σ, ρ)
−1
)Fρ,σΣ. (29.4)
We know that R and R−1correspond to ΣGσ,ρG(c(ρ, σ))Fρ,σ and Gσ,ρG(c(σ, ρ)
−1
)Fρ,σΣ. It
follows from a computation that R and R
−1
in turn correspond to ΣGσ,ρG(c
w(ρ, σ))Fρ,σ and
Gσ,ρG(c
w(σ, ρ)−1
)Fρ,σΣ. It follows that equations (29.3) and (29.4) are in turn equivalent
to E
′Ω = R, Ω−1E = R
−1
, in other words E
′ = E−1 and Ω = ER. On the other
hand, the R-matrices of A˜ and AΩ coincide by Prop. 13.2 as G(c) is a unitary braided
symmetry. Thus the proof of axiom d) is complete. Conversely, when A is a unitary
coboundary weak quasi-Hopf algebra and C = Rep(A) then the natural weak quasi-tensor
structure of the forgetful Rep(A) → Hilb satisfies F
∗
ρ,σ = ρ ⊗ σ(∆(I)
∗
)Ωρ,σ and similarly
G∗
ρ,σ = Ω−1
ρ,σρ ⊗ σ(∆(I)
∗
). Moreover c
w corresponds to ΣR. It follows that the unitarity
statements and (29.1) and (29.2) are verified. The property that C
+ is an Hermitian
(unitary) ribbon category follows from Theorem 28.13. In the unitary case it also follows
that the canonical tensor equivalence E described in Theorem 7.6 is unitary by Prop. 26.4,
see also Theorem 13.5 and preserves the coboundary symmetries by construction. □
Remark 29.3. a) It follows from the proof of Theorem 29.1 and that of Theorem 26.2 that
when C has a generating object (i.e. its powers contain every irreducible as a subobject)
then Theorem 29.1 holds if equations (29.1) and (29.2) are known to hold only for pairs ρ,
σ such that one of them, say ρ, is the generating object and the other varies among the
irreducible objects of C, or alternatively among the choice of a tensor power ρ
n
for each
integer n. b) It follows from Theorem 29.1 and Prop. 28.15 b) that c
w does not depend
on the choice of w.
Remark 29.4. It follows that Theorem 28.13 admits a categorical formulation as well.
Indeed, we may define a discrete coboundary weak quasi-Hopf algebra A equivalently as
a semisimple ribbon tensor category (C, ⊗, α, c, v) endowed with a square root w of the
ribbon element v compatible with duality and the structure of a C
∗
-category with a weak
quasi-tensor faithful functor (G, F, G) such that all the conditions of Theorem 29.1 hold
(we are choosing C
+ = C and F identity). Then any right duality (ρ∨
, bρ, dρ) is of the form

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 183
described in Example 14.7 by the proof of Theorem 7.6 (d), as an antipode (S, α, β) may
always be chosen such that S commutes with ∗ by Remark 14.6. Thus by Theorem 28.13,
the condition β = α
∗
is equivalent to the compatibility equations (28.11) making C into
an Hermitian ribbon category with respect to (c, v, ρ∨, bρ, dρ).
Taking into account the historical motivation briefly discussed in the introductory part of
Section 28, we are led to look for special examples with R-matrix given by a weak analogue
of a 2-coboundary. The next remark shows that the construction of these examples is
related to the study of unitary structures, having a suitable triviality property.
Remark 29.5. If an Hermitian coboundary A has trivial involution as introduced in Def.
11.9 then by definition Ω is a trivial twist, thus we have from relation (28.2)
Ω = ∆(I)
∗∆(I), R = ∆op(I)∆(I)∗w ⊗ w∆(w−1
), R = ∆op(I)∆(I)
∗∆(I). (29.5)
Conversely, if A is Hermitian coboundary and the R-matrix takes the previous form then
necessarily the involution is trivial. We have a particular case, when the Ω-involution of
A is strongly trivial (Ω = Ω−1 = ∆(I)) then
Ω = ∆(I), R = ∆op(I)w ⊗ w∆(w
−1
), R = ∆op(I)∆(I). (29.6)
We recall from Example 28.11 that strongly trivial Ω-involutions can be obtained from
trivial Ω-involutions via suitable twisting. Moreover, when A is in addition unitary discrete
than any trivial Ω-involution is strongly trivial by Prop. 4.21.
In the next section we consider the question of constructing new examples of unitary
coboundary weak quasi-Hopf algebras with such triviality properties from old ones, and
Theorem 29.1 will turn out useful. To construct such examples, we look for twist deformation of given examples that respect the structure, that may perhaps be regarded as
an abstract analytic analogue of part of the arguments involved Drinfeld-Kohno theorem
following [47].
