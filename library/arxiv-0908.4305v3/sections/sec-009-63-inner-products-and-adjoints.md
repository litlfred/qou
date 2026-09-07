---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-009-63-inner-products-and-adjoints
section_title: "Inner Products and Adjoints"
section_number: 6.3
pages: 56-58
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
---
Now we prove our results about the inner product of groupoids ove r a ﬁxed
groupoid, and the adjoint of a span:
Theorem 45. Given a groupoid X, there is a unique inner product ⟨·, ·⟩ on the
vector space L2(X) such that
⟨Φ
~
, Ψ
~
⟩ = |⟨Φ, Ψ ⟩|
whenever Φ and Ψ are square-integrable groupoids over X. With this inner
productL2(X) is a real Hilbert space.
Proof. Uniqueness of the inner product follows from the formula, since eve ry
vector in L2(X) is a ﬁnite-linear combination of vectors Ψ
~
for square-integrable
groupoids Ψ over X. To show the inner product exists, suppose that Ψ i, Φ i are
square-integrable groupoids over X andαi,β i ∈ R for 1 ≤i ≤n. Then we need
to check that ∑
i
αiΨ
~
i =
∑
j
βjΦ
~
j = 0
implies ∑
i,j
αiβj |⟨Ψ i, Φ j⟩| = 0.
The proof here closely resembles the proof of existence in Theorem 34. We
leave to the reader the task of checking that L2(X) is complete in the norm
corresponding to this inner product.
56
Proposition 46. Given a span
S
q
/d127/d127/d127/d127/d127/d127/d127/d127/d127 p
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
and a pair v : Ψ →X,w : Φ →Y of groupoids over X andY , respectively, there
is an equivalence of groupoids
⟨Φ,S Ψ ⟩ ≃ ⟨S†Φ, Ψ ⟩.
Proof. We can consider the groupoids over X and Y as spans with one leg
over the terminal groupoid 1. Then the result follows from the equiv alence
given by associtativity in Lemma 43 and Theorem 35. Explicitly, ⟨Φ,S Ψ ⟩ is the
composite of spans SΨ and Φ, while ⟨S†Φ, Ψ ⟩ is the composite of spans S†Φ
and Ψ.
Proposition 47. Given spans
T
qT
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pT
/d31/d31/d64/d64/d64/d64/d64/d64/d64 S
qS
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Z Y Y X
there is an equivalence of spans
(ST )† ≃T †S†.
Proof. This is clear by the deﬁnition of composition.
Proposition 48. Given spans
S
qS
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64 T
qT
/d127/d127/d126/d126/d126/d126/d126/d126/d126 pT
/d32/d32/d64/d64/d64/d64/d64/d64/d64
Y X Y X
there is an equivalence of spans
(S +T )† ≃S† +T †.
Proof. This is clear since the addition of spans is given by coproduct of group oids.
This construction is symmetric with respect to swapping the legs of t he span.
Proposition 49. Given a groupoid Λ and square-integrable groupoids Φ , Ψ ,
and Ψ ′ over X, we have the following equivalences of groupoids:
1.
⟨Φ, Ψ ⟩ ≃ ⟨Ψ, Φ ⟩.
57
2.
⟨Φ, Ψ + Ψ ′⟩ ≃ ⟨Φ, Ψ ⟩ + ⟨Φ, Ψ ′⟩.
3.
⟨Φ, Λ × Ψ ⟩ ≃ Λ × ⟨Φ, Ψ ⟩.
Proof. Each part will follow easily from the deﬁnition of weak pullback. First
we label the maps for the groupoids over X as v : Φ → X, w : Ψ → X, and
w′ : Ψ ′ →X.
1. ⟨Φ, Ψ ⟩ ≃ ⟨Ψ, Φ ⟩.
By deﬁnition of weak pullback, an object of ⟨Φ, Ψ ⟩ is a triple (a,b,α ) such
that a ∈ Φ,b ∈ Ψ, and α : v(a) → w(b). Similarly, an object of ⟨Ψ, Φ ⟩ is
a triple ( b,a,β ) such that b ∈ Ψ,a ∈ Φ, and β : w(b) → v(a). Since α is
invertible, there is an evident equivalence of groupoids.
2. ⟨Φ, Ψ + Ψ ′⟩ ≃ ⟨Φ, Ψ ⟩ + ⟨Φ, Ψ ′⟩.
Recall that in the category of groupoids, the coproduct is just th e disjoint
union over objects and morphisms. With this it is easy to see that the
deﬁnition of weak pullback will ‘split’ over union.
3. ⟨Φ, Λ × Ψ ⟩ ≃ Λ × ⟨Φ, Ψ ⟩.
This follows from the associativity (up to isomorphism) of the cartes ian
product.
Acknowledgements
We thank James Dolan, Todd Trimble, and the denizens of the n-Category Caf´ e,
especially Urs Schreiber and Bruce Bartlett, for many helpful conv ersations. AH
was supported by the National Science Foundation under Grant No . 0653646.
CW was supported by an FQXi grant.
