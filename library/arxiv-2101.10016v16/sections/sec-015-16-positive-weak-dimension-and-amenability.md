---
doc_id: arxiv-2101.10016v16
doc_title: "Unitary coboundary weak quasi-Hopf algebras in the Kazhdan-Lusztig-Finkelberg theorem"
section_id: sec-015-16-positive-weak-dimension-and-amenability
section_title: "Positive weak dimension and amenability"
section_number: 16
pages: 114-117
source_pdf: 2101.10016v16.pdf.txt
source_sha256: 51d21209730be025
toc_source: inferred
---
16. Positive weak dimension and amenability
The Grothendieck ring Gr(C) of a rigid semisimple tensor category C is called amenable
if it admits a dimension function satisfying a certain analytic property. Such a function,
called amenable, is unique and bounds below any other dimension function, see e.g. [141].
In this section we extend the framework to weak dimension functions. We show that
the amenable dimension function is already unique among weak dimension functions and
minimizes them. This gives a weaker criterion for amenability. It follows in particular
that if C is a fusion category the lower bound of weak dimension functions is given by
the Frobenius-Perron dimension, and this was our original motivation for the study of
amenability.
Let C be a rigid semisimple tensor category and D a weak dimension function on the
Grothendieck ring Gr(C), see Def. 7.8, that will always be assumed positive and symmetric
in this section. As already mentioned, we first aim to introduce a notion of amenability for
D extending the usual amenability for a genuine dimension. To do this, we closely follow
the treatment in Sect. 2.7 in [141], dropping the unitarity assumption on C. Therefore for
ρ ∈ Irr(C) let Λρ be the operator of left multiplication by ρ on the complexified algebra
GrC(C) := Gr(C) ⊗Z C. It follows from associativity of Gr(C) that
ΛρΛσ =
X
τ
mτ
ρ,σΛτ , (16.1)
with mτ
ρ,σ = dim(τ, ρ ⊗ σ) and therefore Λ linearly extends to a representation of Gr(C).
Proposition 16.1. Let C be a rigid semisimple tensor category admitting a weak dimension
function. The operator Λρ extends to a bounded linear operator on ℓ
2
(Irr(C)). We have
∥Λρ∥ ≤ D(ρ) for ρ ∈ Irr(C) and for every weak dimension function D.

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 115
Proof. The proof extends the corresponding proof for dimension functions, see Prop. 2.7.4
in [141], with the modification that uσ = vσ = D(σ) is replaced by uσ = D(σ) and
vσ = (Γu)σ =
D(ρσ)
D(ρ) ≤ D(σ) which implies Γt
(v)σ ≤
D(ρσ)
D(ρ) ≤ D(σ) = uσ and in turn
replaces Γt(v) = u. Note indeed that these modifications are still compatible with Lemma
2.7.3 in [141] and the proof may be completed. □
Given a dimension function D we consider operators λµ =
P
ρ∈Irr(C)
µ(ρ)
D(ρ)
Λρ associated to
probability measures µ on Irr(C) and then we find that a composition λµλν = λµ∗ν, with
µ ∗ ν the convolution measure defined as at page 71 in [141],
µ ∗ ν(τ ) = X
ρ,σ∈Irr(C)
mτ
ρ,σ
D(τ )
D(ρ)D(σ)
µ(ρ)ν(σ),
with mτ
ρ,σ the multiplicity of τ in ρ ⊗ σ. For a weak dimension function a similar formula
holds but µ ∗ ν may not be a probability measure. Indeed ∥µ ∗ ν∥ =
P
τ∈Irr(C) µ ∗ ν(τ ) =
P
σ,τ∈Irr(C)
µ(σ)ν(τ)D(στ)
D(σ)D(τ) ≤ 1. Thus if Irr(C) is countable and if µ and ν have support Irr(C)
then µ ∗ ν is a probability measure precisely when D is a genuine dimension function.
Therefore we more generally consider the operators λµ for any positive measure µ with
∥µ∥ ≤ 1. One has ∥λµ∥ ≤ ∥µ∥, so ∥λµ∥ = 1 is possible only if µ is a probability measure.
Proposition 16.2. Let D be a weak dimension function on Gr(C). Then the following
properties are equivalent.
(a) 1 ∈ Spλµ for every probability measure µ,
(b) ∥λµ∥ = 1 for every probability measure µ,
(c) (ˇµ ∗ µ)
n
(ι)
1/n → 1 for every probability measure µ, with µˇ(ρ) = µ(ρ),
(d) there is a net ξα ∈ ℓ
2
(Irr(C)) of positive unit vectors such that ∥Λρξα−D(ρ)ξα∥ → 0
for all ρ ∈ Irr(C).
If they hold then D is a dimension function.
Proof. The equivalence of properties (a)–(d) may be proven just as in the case of ordinary
dimension functions, cf. Lemma 2.7.5 in [141], taking into account the slight modifications
mentioned before the statement. The last statement follows from the observation that
Λ is a representation of Gr(C) in the sense of (16.1), and a 3ε-argument applied to the
vanishing net (Λρ(Λσ − D(σ)))ξα with ξα as in (d). □
We recall the definition of amenability.
Definition 16.3. A dimension function on Gr(C) satisfying the equivalent properties of
Prop. 16.2 is called amenable. The category C is called amenable if the intrinsic dimension
function on Gr(C) is amenable.
The following result extends to weak dimension functions the uniqueness result known
for an amenable dimension function, see Prop. 2.7.7 in [141].
Theorem 16.4. An amenable dimension function on Gr(C) is unique among weak dimension functions satisfying the equivalent properties of Prop. 16.2 and is given by D(ρ) =
∥Λρ∥ for ρ ∈ Irr(C). Any other weak dimension D′satisfies D′(ρ) ≥ D(ρ) for all ρ.

116 S. CIAMPRONE, M.V. GIANNONE, AND C. PINZARI
Proof. The first statement follows from Prop. 16.2 and property (b) applied to the probability measures with support a single irreducible. The second part follows from the first
and Prop. 16.1.
□
Existence of an amenable dimension function is characterized by the following property of the left regular representation, for all ρ ∈ Irr(C), Λρ is bounded and ∥
P
i µiΛρi P
∥ =
i µi∥Λρi
∥ for finite linear combinations of basis elements with positive coefficients. These
conditions are clearly necessary as by the previous theorem the amenable dimension function is unique and explicitly given by ∥Λρ∥. Conversely, when Λρ is bounded, we define
the operators λµ as before with ∥Λρ∥ in place of D(ρ), ρ ∈ Irr(C). Then it is easy to see
using continuity of µ ∈ ℓ
1
(Irr(C)) → λµ ∈ B(ℓ
2
(Irr(C))) that the positive linearity of ∥Λρ∥
is equivalent to property (b) of Prop. 16.2. It follows that the linear extension of ∥Λρ∥ is
automatically an amenable weak dimension function by submultiplicativity of the norm.
It follows that every fusion category C admits the unique amenable dimension function,
and moreover has a unique positive dimension function, the Frobenius-Perron dimension
determined by FPdim(ρ) = ∥Λρ∥. Indeed, (d) of Prop. 16.2, has a solution given by the
vector with coordinates the dimensions of the simple objects, and by Sect. 8 in [51] or
Chapter 4 in [50], ∥Λρ∥ is indeed a dimension function on Gr(C).
Corollary 16.5. If C is a fusion category then D(ρ) ≥ FPdim(ρ) for every weak dimension
function D on Gr(C).
Another important class of examples is that for which Gr(C) is commutative. Yamagami
showed that in this case that for the existence of the amenable dimension function is
necessary and sufficient to verify that Λρ is bounded, see Theorem 3.5 in [195].
Remark 16.6. The examples that we have studied in the paper show that there may be
more than a natural choice of integral weak dimension functions associated to a fusion
category. For example, for the pointed fusion categories arising from quantum groups at
roots of unity (or vertex operator algebras) at the minimal root (level), FPdim(g) = 1 on
every irreducible object g, so FPdim is already an integral dimension function. Another
natural choice is associated to Wenzl functor or to Zhu’s functor. Consider for each level
k, Gr(C(g, q, ℓ))) for q = e
iπ/ℓ
, ℓ = d(k + hˇ) and regard it as a quotient of the classical
representation ring R(g) associated to g. Then the sequence Dk of weak dimension functions on Gr(C(g, q, ℓ)) defined by Wenzl’s functor defines in the pointwise limit the classical
dimension function of R(g), which is also the unique amenable dimension function of this
based ring.
We next apply Theorem 16.4 to a weak tensor functor between tensor C
∗–categories
studied in Sect. 5 and we find a useful upper and lower bound for the associated weak
dimension function.
Corollary 16.7. Let C and C
′
be rigid tensor C
∗
-categories such that Gr(C) admits the
amenable dimension function D. Then every weak tensor ∗-functor F : C → C
′ defined by
F and G satisfies
D(ρ) ≤ d
′
(F(ρ)) ≤ ∥Fρ,ρ∥∥Gρ,ρ∥d(ρ), ρ ∈ C,

UNITARY COBOUNDARY WEAK QUASI-HOPF ALGEBRAS 117
where d, d
′ are the intrinsic dimensions of C and C′
respectively.
Proof. Note that the weak dimension function ρ → dim(F(ρ)) is symmetric as F(ρ) is a
conjugate of F(ρ) by Prop. 5.8. The lower bound then follows from Theorem 16.4. For
the upper bound see Cor. 5.10. □
We conclude with a result concerning a dimension preserving property of unitary weak
tensor functor between rigid C
∗
-tensor categories in the amenable case. This result extends
a known property for unitary tensor functors, see Cor. 2.7.9 in [141] and references therein.
Corollary 16.8. Let C and C
′
be rigid tensor C
∗
-categories with intrinsic dimensions d
and d
′
respectively, and let (F, F, G) : C → C
′
be a unitary weak tensor ∗-functor. If C is
amenable (e.g. C is a fusion category) then d(ρ) = d
′
(F(ρ)) for all ρ. In particular, when
C
′ = Hilb then d(ρ) = dim(F(ρ)) and therefore F is already tensor.
Proof. By assumption F
∗ and G are isometric, so ∥Fρ,σ∥ = ∥Gρ,σ∥ = 1. It follows from
Cor. 16.7 that d
′
(F(ρ)) = d(ρ) as d(ρ) is the unique amenable dimension function. In
particular when C
′ = Hilb then ρ → dim(F(ρ)) is a genuine dimension function and this
implies that F is tensorial. □
Remark 16.9. Theorem 5.31 of Longo and Roberts [118] shows that a strict tensor category with a unitary braided symmetry satisfying some extra conditions is amenable. Note
that amenability in their sense is defined in a different way than the notion that we are
using (the intrinsic dimension function is amenable), which in turn is closely related to
amenability in the sense of Popa [151]. They discuss the relation between the two notions
in their Sect. 5.
By the previous corollary when the range category for a weak quasitensor functor is Hilb
then the properties of unitarity and weak tensoriality may coexist only when the functor
is automatically tensorial and the intrinsic dimension takes integral values. Thus when
a specific ∗-functor F : C → Hilb on a fusion category is given such that the intrinsic
dimension differs from the associated vector space dimension then F admits no unitary
weak tensor structure (F, G). On the other hand by the results of Sect. 32, preceded
by [25] for the type A case, non-unitary weak tensor structures exist. For example, this
applies to the functor W on C(g, q, ℓ) at level k ≥ 1.
