---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-027-b1-polarization-and-projection
section_title: "B.1 Polarization and Projection"
section_number: null
pages: 34-35
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
Polarization and Projection
For polynomials of degree m ≤n, the degree-n polarization map is deﬁned on monomials as follows and is
extended linearly.
Π↑
n : Cn[x] →C(1n)[x1, . . . , xn]
xk 7→1
n!
X
σ∈Sn
k
Y
j=1
xσ(j)
This deﬁnition can be extended to homogeneous polynomials in V (n) by composing with Hmg−1
n
and
Hmg(1n). The map Π↑
n has a left inverse Π↓
n, called the projection map, which we deﬁne as follows.
Π↓
n : C(1n)[x1, . . . , xn] →Cn[x]
f(x1, x2, . . . , xn) 7→f(x, x, . . . , x)
That is, Π↓
n ◦Π↑
n is the identity map. Similarly, this deﬁnition can be extended to homogeneous polynomials
by composing with Hmg−1
(1n) and Hmgn.
It is well-known that Π↑
n is an injective linear map onto the subspace of symmetric multi-aﬃne polynomi-
als. This fact then extends to homogeneous polynomials, where the terms symmetric and multi-aﬃne each
refer to pairs of homogeneous variables. Further, one can deﬁne multivariate polarization and projection
maps via composition: Π↑
λ := Π↑
λm ◦· · · ◦Π↑
λ1 and Π↓
λ := Π↓
λm ◦· · · ◦Π↓
λ1. Injectivity then automatically
extends to Π↑
λ, and Π↓
λ ◦Π↑
λ is the identity map.
These two maps arise naturally in the theory of polynomials in general, and play an important role in
the theory of stability, via the Grace-Walsh-Szeg˝o coincidence theorem as well as in the proof of the Borcea-
Br¨and´en characterization of linear operators. The next result shows they also have represention theoretic
importance.
Proposition B.1. Fix λ ∈Nm
0 , and view V (λ) ∼= V (λ1)⊠· · ·⊠V (λm) and V (1λ) ∼= V (1)⊗λ1 ⊠· · ·⊠V (1)⊗λm
as representations of (SL2(C))m. The maps Π↑
λ : V (λ) →V (1λ) and Π↓
λ : V (1λ) →V (λ) are (SL2(C))m-
invariant.
34
Proof. Note that by proving the result for Π↑
n and Π↓
n with m = 1, the general result follows since Π↑
λ
and Π↓
λ are compositions of such maps. To prove it for m = 1, note that the set of symmetric elements
in V (1)⊗n ∼= V (1n) is invariant under the diagonal action of SL2(C). Further, since V (n) is irreducible of
dimension n + 1 and V (1)⊗n has a single irreducible component of dimension n + 1, Schur’s lemma implies
the result.
This result then has a few corollaries which will help to shed light on results related to polarization and
the apolarity form. The ﬁrst will be useful in elucidating the representation theoretic ties to the Grace-
Walsh-Szeg˝o coincidence theorem below.
Lemma B.2. Fix λ ∈Nm
0 . Then the apolarity form commutes with polarization up to scalar. That is:
Dλ = D(1λ) ◦(Π↑
λ ⊗Π↑
λ)
Proof. The map D(1λ) ◦(Π↑
λ ⊗Π↑
λ) : V (λ) ⊗V (λ) →C is an (SL2(C))m-invariant bilinear form on V (λ). By
uniqueness (see Corollary A.12), this then must equal Dλ up to scalar.
The content of this result is that fact that we have commutativity even though D(1λ) is a priori the apo-
larity form with respect to a diﬀerent group action than that of Dλ (i.e., (SL2(C))|λ| instead of (SL2(C))m).
That said, it should be noted that the analogous commutativity statement with the projection map Π↓
λ does
not hold (unless of course, one restricts to the image of Π↑
λ).
The purpose of this result is then to demonstrate the connection between a polynomial and its polariza-
tion. In particular, if Grace’s theorem gives stability information via the apolarity form, then the previous
result shows that the polarizations of those polynomials will have the same stability information. We prove
this rigorously in Corollary B.5.
Proposition B.1 also leads to one of the crucial results used in the proof of the Borcea-Br¨and´en char-
acterization of linear operators (Lemma 2.5 in [BB09a]). It relies on the notion of “the polarization of an
operator”, given by T 7→Π↑
α ◦T ◦Π↓
λ (see §2.2 in [BB09a]). We do not make explicit use of this result, but we
state it here to demonstrate that operator polarization has a representation theoretic interpretation similar
to that of the usual polynomial polarization.
Proposition B.3. The symbol of the polarization of an operator T is the polarization of the symbol of T .
Proof. Using Proposition B.1 and Deﬁnition 3.6, it is straightforward to see that all the maps involved are
injective (SL2(C))2m-invariant linear maps (i.e., polarization of polynomials, polarization of operators, the
Symb map). The result then follows from a dimension argument and Schur’s lemma, in a way similar to
that of the proof of Proposition B.1.
