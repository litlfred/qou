---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-028-polite-duality
section_title: "Polite duality."
section_number: null
pages: 31-35
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
Polite duality.
Recall from Section 2.2 that for every space X there is the Serre kernel
ΣX: X →X such that for spaces X and Y the functor
ΣY ◦−◦ΣX: HomV ar(X, Y) →HomV ar(X, Y)
is a Serre functor for the category HomV ar(X, Y).
31
Deﬁnition. If Φ: X →Y and Φ† : Y →X are kernels then a polite du-
ality between them, denoted Φ
∨
←→Φ†, consists of adjunctions as follows
(numbered as shown)
Φ† ◦ΣY ⊣1 Φ ⊣2 ΣX ◦Φ†,
Φ ◦ΣX ⊣3 Φ† ⊣4 ΣY ◦Φ,
such that the following compatibility relations hold.
(1+2). For kernels Θ: Z →X and Ψ: Z →Y, the diagram of iso-
morphisms below commutes:
Hom(Ψ, Φ ◦Θ)
1
→Hom(Φ† ◦ΣY ◦Ψ, Θ)
Hom(Φ ◦Θ, ΣY ◦Ψ ◦ΣZ)∨
Serre↓
2→Hom(Θ, ΣX ◦Φ† ◦ΣY ◦Ψ ◦ΣZ)∨.
Serre↓
(2+3). The composite map
Hom(Θ, Φ†◦Ψ) ∼−→
3 Hom(Φ◦ΣX◦Θ, Ψ) ∼−→
2 Hom(ΣX◦Θ, ΣX◦Φ†◦Ψ)
is the one induced by composition with ΣX.
(3+4). Same as (1+2), but for adjunctions 3 and 4.
(1+4). Same as (2+3), but for adjunctions 1 and 4.
It is useful to think of this deﬁnition in terms of string diagrams. For
each of the four adjunctions we get a unit and a counit. Denoting Φ by an
upward oriented line and Φ† by a downward oriented line, we can draw the
units and counits as follows.
η1:
η2:
η3:
η4:
ǫ1:
ǫ2:
ǫ3:
ǫ4:
Relation (2+3) can be represented graphically in the following way: for
any α ∈Hom(Θ, Φ† ◦Ψ) we have
Ψ
α
Θ
=
α
Ψ
Θ
.
From this we can deduce the equality
=
,
32
so we deﬁne the following diagram to be this common morphism:
γΦ :
.
Similarly we can deduce that the counits ǫ2 and ǫ3 are equal, and we deﬁne
the following diagram to be the common morphism:
ǫ
Φ :
.
Likewise, using the relation (1+4), from the units η1 and η4, and the counits
ǫ1 and ǫ4 we obtain the common morphisms denoted as follows.
γΦ∨:
ǫ
Φ∨:
So the four units and four counits are obtained from these two M-shaped
and two Y-shaped morphisms.
Relations (1+2) and (3+4) in the deﬁnition of polite duality are essen-
tially equivalent to the invariance of the Serre trace under a partial trace
in the following sense. Given a polite duality Φ
∨
←→Φ† and a morphism
α ∈Hom(Φ◦Θ, Σ◦Φ◦Ψ) we can deﬁne the left partial trace in Hom(Θ, Σ◦Ψ)
with respect to Φ† as drawn below.
Θ
α
Ψ
Similarly we can deﬁne a right partial trace when the Φ is on the right
rather than on the left. So the following diagram is the right partial trace
with respect to Φ and Φ† of a morphism α′ ∈Hom(Θ′ ◦Φ, Ψ′ ◦Φ ◦Σ).
Θ′
α′
Ψ′
Theorem 17. If Φ and Φ† form a politely dual pair of kernels, then the
Serre trace is invariant under partial trace with respect to Φ:
Tr




Ψ
α
Ψ



= Tr




Ψ
α
Ψ 


;
Tr




Ψ′
α′
Ψ′



= Tr




α′
Ψ′
Ψ′



.
33
Proof. We will just prove the left partial trace case. Relation (1+2) says
that for β ∈Hom(Ψ, Φ ◦Θ) and γ ∈(Θ, Σ ◦Φ† ◦Σ ◦Ψ ◦Σ) we have the
equality
Tr






Θ
Ψ
β
γ
Ψ 





= Tr






Θ
Ψ
β
γ
Ψ 





.
Applying this with
β :=
Ψ
and
γ :=
Ψ
α
Ψ
we obtain the equality
Tr






α
Ψ
Ψ






= Tr






Ψ
Ψ
α






.
The result follows from the commutativity property of the Serre trace,
namely that Tr(β ◦v α) = Tr(S(α) ◦v β).
Proposition 18. Polite dualities Φ
∨
←→Φ† and Ψ
∨
←→Ψ† for two kernels
Φ: X →Y and Ψ: Y →Z canonically induce a polite duality
Ψ ◦Φ
∨
←→Φ† ◦ΣY ◦Ψ†.
Proof. The required adjunctions are constructed in the obvious fashion, us-
ing the fact that the composition, in reverse order, of adjoints (left or right)
of composable functors is naturally an adjoint (in the same direction) of
the composition of the functors. The compatibilities required by the polite
duality follow from straight forward checks.
Adjunctions are intrinsic parts of a polite duality. Conversely, the fol-
lowing proposition shows that any adjunction induces a polite duality in a
natural way.
Proposition 19. Given an adjunction Ψ ⊣Φ, deﬁne Φ† := Ψ ◦Σ−1
Y . Then
there exists a polite duality Φ
∨
←→Φ† where the adjunction ⊣1 is the given
one Ψ ⊣Φ.
Proof. As ΣX ◦Φ† = ΣX ◦Ψ ◦Σ−1
Y , compatibility relation (1+2) yields an
adjunction
Φ ⊣2 ΣX ◦Φ†.
34
Similarly, relations (1+4) and (2+3) force adjunctions
Φ ◦ΣX ⊣3 Φ† ⊣4 ΣY ◦Φ,
and it is easy to see that relation (3+4) is then automatically satisﬁed.
Proposition 20. Let Φ ∈D(X × Y) be a kernel, and let Φ∨∈D(Y × X) be
the dual R HomX×Y(Φ, OX×Y), regarded as a kernel from Y to X. Then there
exists a canonical polite duality Φ
∨
←→Φ∨.
Proof. For kernels Θ ∈D(Z × X) and Ψ ∈D(Z × Y) consider the sequence
of isomorphisms
HomD(Z×Y)(Ψ, Φ ◦Θ)
∼= HomD(Z×Y)(Ψ, πZY,∗(π∗
ZXΘ ⊗π∗
XYΦ))
∼= HomD(Z×X)(πZX,!(π∗
ZYΨ ⊗π∗
YXΦ∨), Θ)
= HomD(Z×X)(πZX,∗(π∗
ZYΨ ⊗π∗
YX(Φ∨⊗ωY[dim Y])), Θ)
= HomD(Z×Y)((Φ∨◦ΣY) ◦Ψ, Θ).
Taking Z = Y, Θ = Φ∨◦ΣY and Ψ = IdY yields a morphism of kernels
IdY →Φ ◦Φ∨◦ΣY;
in a similar fashion we obtain a morphism
Φ∨◦ΣY ◦Φ →IdX.
These two morphisms satisfy the identities needed to make Φ∨◦ΣY the left
adjoint of Φ. Proposition 19 gives the result.
