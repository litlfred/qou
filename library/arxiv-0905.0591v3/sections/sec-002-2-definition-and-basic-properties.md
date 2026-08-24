---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-002-2-definition-and-basic-properties
section_title: "Definition and basic properties"
section_number: 2
pages: 3-4
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
2.1. Twisted Reidemeister torsion. Let N be a 3–manifold with empty or toroidal
boundary, F a torsion–free abelian group and α : π1(N ) → GL(k,R [F ]) a representation.
Recall that we denote by Q(R[F ]) the quotient ﬁeld of R[F ].
We endow N with a ﬁnite CW–structure. We denote the universal cover of N by ˜N .
Recall that there exists a canonical left π1(N )–action on the universal cover ˜N given by deck
transformations. We consider the cellular chain complex C∗( ˜N ) as a right Z[π1(N )]-module
by deﬁning σ ·g := g−1σ for a chain σ. The representation α induces a representation
α : π1(N ) → GL(k,R [F ]) → GL(k,Q (R[F ])) which gives rise to a left action of π1(N ) on
Q(R[F ])k. We can therefore consider the Q(R[F ])–complex
C∗( ˜N ) ⊗Z[π1(N )]Q(R[F ])k.
We now endow the free Z[π1(N )]–modules C∗( ˜N ) with a basis by picking lifts of the cells
ofN to ˜N . Together with the canonical basis for Q(R[F ])k we can now view the Q(R[F ])–
complex C∗( ˜N ) ⊗Z[π1(N )]Q(R[F ])k as a complex of based Q(R[F ])–modules.
If this complex is not acyclic, then we deﬁne τ (N,α ) = 0. Otherwise we denote by
τ (N,α ) ∈Q(R[F ]) \ {0} the Reidemeister torsion of this based Q(R[F ])–complex. We will
not recall the deﬁnition of Reidemeister torsion, referrin g instead to the many excellent
expositions, e.g. [Mi66], [Tu01] and [Nic03]. However, in t he next section we will present a
method for computing explicitly the twisted Reidemeister t orsion of a 3–manifold.
It follows from Chapman’s theorem [Chp74] and from standard arguments (cf. the above
literature) that up to multiplication by an element in
{± det(α(g)) |g ∈π1(N )}
the Reidemeister torsion τ (N,α ) is well–deﬁned, i.e. up to that indeterminacy τ (N,α ) is
independent of the choice of underlying CW–structure and th e choice of the lifts of the cells.
In the following, given w ∈Q(R[F ]) we write
τ (N,α ) .=w
if there exists a representative of τ (N,α ) which equals w.
Note that if γ : π1(N ) → GL(k,R ) is a representation and ψ :π1(N ) →F a homomor-
phism to a free abelian group, then we get a tensor representa tion
γ ⊗ψ :π1(N ) → GL(k,R [F ])
g ↦→ γ(g) ·ψ(g)
and the corresponding Reidemeister torsion τ (N,γ ⊗ψ). Except for parts of Section 5.2
we will always consider the twisted Reidemeister torsion co rresponding to such a tensor
4 STEF AN FRIEDL AND STEF ANO VIDUSSI
representation. In that case, specializing the previous fo rmula,τ (N,γ ⊗ψ) is well–deﬁned
up to multiplication by an element in
{± det(γ(g))f |g ∈π1(N ),f ∈F }.
In particular, if γ : π1(N ) → SL(k,R ) is a representation to a special linear groups, then
τ (N,γ ⊗ψ) ∈Q(R[F ]) is well–deﬁned up to multiplication by an element in ±F . Further-
more, if k is even, then τ (N,γ ⊗ψ) ∈Q(R[F ]) is in fact well–deﬁned up to multiplication
by an element in F (cf. e.g. [GKM05]).
Finally we adopt the following notation:
(1) Given a homomorphism γ :π →G to a ﬁnite group G we get an induced represen-
tationπ → Aut(Z[G]) ∼
= GL(|G|, Z) given by left multiplication. In our notation we
will not distinguish between a homomorphism to a ﬁnite group and the correspond-
ing representation over Z.
(2) If N is the exterior of a link L ⊂ S3, ψ : π1(S3 \νL) → F the abelianization and
γ :π → GL(k,R ) a representation, then we write τ (L,γ ) for τ (S3 \νL,γ ⊗ψ).
