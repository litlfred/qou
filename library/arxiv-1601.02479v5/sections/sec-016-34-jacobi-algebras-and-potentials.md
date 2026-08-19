---
doc_id: arxiv-1601.02479v5
doc_title: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A"
section_id: sec-016-34-jacobi-algebras-and-potentials
section_title: "Jacobi algebras and potentials"
section_number: 3.4
pages: 32-34
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and the associated cohomo logical Hall alge- bra"
---
combination of equivalence classes of cyclic words in CQ. Such a W is called
a potential. A potential W induces a function Tr(W ) on M, deﬁned as follows.
Firstly, assume that W lifts to a single cyclic word c = ar . . . a0 in CQ. Then a
CQ-module F determines an endomorphism
F (ar) ◦ . . . ◦ F (a0) : F (s(a0)) → F (s(a0)),
and Tr(F (ar) ◦ . . . ◦ F (a0)) determines a function on X(Q)d, for each d ∈ NQ0 . By
cyclic invariance of the trace, this function is Gd-invariant, and does not depend
on the lift c of W . Extending by linearity, we deﬁne for general W ∈ CQ/[CQ, CQ]
the induced function
Tr(W )d : Md → C.
COHAS AND QUANTUM ENVELOPING ALGEBRAS 33
We denote by Tr(W )ζ
d the restriction of this function to Mζ -ss
d , and by
T r(W )ζ
d : Mζ -ss
d → C
the unique function through which Tr(W )ζ
d factors. Similarly, we deﬁne
T r(W )ζ
f ,d := T r(W )ζ
d ◦πζ
f ,d : Mζ
f ,d → C,
and we deﬁne Tr(W )ζ
d′,d′′ to be the composition
Mζ -ss
d′,d′′֒→Mζ -ss
d′ + d′′
Tr(W )ζ
d′ + d′′
− − − − − − − − →C.
Associated to the data ( Q, W ) is the Jacobi algebra
Jac(Q, W ) := CQ/⟨∂W/∂a | a ∈ Q1⟩.
Here the noncommutative derivatives ∂W/∂a are deﬁned as follows. First assume
that W lifts to a single cyclic word c ∈ CQ. Then
∂W/∂a :=
∑
c=c′ac′′
c′′c′.
We then extend the deﬁnition to general W by linearity. We deﬁne MW , the stack
of ﬁnite-dimensional Jac( Q, W )-modules, in the same way as the stack of ﬁnite-
dimensional CQ-modules. In particular there is a natural closed embedding of
stacks MW ⊂ M, and it is easy to show that MW = crit( Tr(W )) as substacks of
M.
In order to keep to Assumption 2.14 we will assume that W ∈ ⟨∂W/∂a |a ∈ Q1⟩,
for then crit( Tr(W )) ⊂ Tr(W )−1(0). One very common set of circumstances in
which this requirement is met is when there is a grading of the arrows Q1 with in-
tegers such that W is homogeneous of nonzero weight. As mentioned after Assump-
tion 2.14, we can drop this requirement at the expense of slightly mor e complicated
deﬁnitions.
Proposition 3.11. Let W ∈ CQ/[CQ, CQ] be a potential. Then
φ mon
T r(W )ζ
µ
: D≥,lf(
MHM(Mζ -ss
µ )
)
→ D ≥,lf(
MMHM(Mζ -ss
µ )
)
is a symmetric monoidal functor.
Proof. Let F , G ∈ MHM(Mζ -ss
µ ). Let π : Mζ -ss
µ × Mζ -ss
µ → Mζ -ss
µ × Mζ -ss
µ be the
map swapping arguments. The statement follows from exactness o fφ mon
T r(W )ζ
µ
and
biexactness of ⊠⊕ and the claim that the following diagram is commutative,
φ mon
T r(W )ζ
µ
(F ⊠⊕ G) /d47/d47
/d15/d15
φ mon
T r(W )ζ
µ
(G ⊠⊕ F )
/d15/d15
φ mon
T r(W )ζ
µ
F ⊠⊕φ mon
T r(W )ζ
µ
G /d47/d47
φ mon
T r(W )ζ
µ
G ⊠⊕φ mon
T r(W )ζ
µ
F ,
where the horizontal maps are induced by the symmetrizing natura l isomorphisms
of Section 3.2, and the vertical maps are given by the Thom-Sebast iani natural
isomorphism. By faithfulness of the functor forg mon
Mζ -ss
µ
deﬁned in (28), it is enough to
prove commutativity of the diagram at the level of perverse sheav es, or constructible
complexes. Since ⊕ is ﬁnite, by natural commutativity of vanishing cycle functors
34 BEN DA VISON AND SVEN MEINHARDT
with proper maps, it is enough to prove commutativity of the diagram
(53) φ T r(W )ζ
µ
(F ⊠ G) [−1] /d47/d47
/d15/d15
φ T r(W )ζ
µ
(G ⊠ F ) [−1]
/d15/d15φ T r(W )ζ
µ
F [−1] ⊠φ T r(W )ζ
µ
G[−1] /d47/d47
φ T r(W )ζ
µ
G[−1] ⊠φ T r(W )ζ
µ
F [−1].
Let ι : Mζ
µ → X be an embedding inside a smooth scheme, let f be a function on X
extending T r(W )ζ
µ and consider F as a perverse sheaf on X via the direct image.
Then we deﬁne the functor on the category of constructible shea ves on X
Γf −1(R≤0)F (U ) := ker
(
F (U ) → F (U \ f −1(R≤0))
)
and we may alternatively deﬁneφ f F [−1] := (RΓf −1(R≤0)F )|f −1(0). By [5, Prop.A.2]
[32] the Thom–Sebastiani isomorphism is given by the natural morph ism
α : RΓf −1(R≤0)×f −1(R≤0) (• ⊠ •) → RΓ(f ⊞f )−1(R≤0) (• ⊠ •)
induced by the inclusion
f −1(R≤0) × f −1(R≤0) ⊂ (f ⊞ f )−1(R≤0),
and the horizontal maps in (53) are induced by the natural morphis m
F ⊠ G
π #
− − →π ∗ (G ⊠ F )
on both sides. Applying the natural isomorphism α to this morphism, we obtain
the diagram (53). □
