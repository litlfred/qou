---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND"
section_id: sec-042-a7-behaviour-of-bps-invariants
section_title: "A.7. Behaviour of BPS invariants"
section_number: null
pages: 41-43
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY TOM BRIDGELAND — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
A.2 completely describes the
variation of the BPS (or equivalently DT) invariants: if one knows the Ω p(γ) at some point p∈ M
then they are uniquely determined at all other points p∈ M. This statement follows immediately
from the following result.
42 TOM BRIDGELAND
Lemma A.3. Given a BPS structure (Γ , Z, Ω) , the element
S(∆) ∗ =
∏
ℓ⊂∆
S(ℓ)∗∈ ˆG∆
determines the invariants Ω( γ) for all classes γ∈ Γ satisfying Z(γ)∈ ∆ .
Proof. Suppose that ∆ is the disjoint union of two subsectors ∆ = ∆ +⊔ ∆ − where we make the
convention that ∆ + lies in the anti-clockwise direction. There is an obvious decomposition
ˆg∆ = ˆg∆ +⊕ ˆg∆ −.
It follows from this that each element g∈ ˆG∆ decomposes uniquely as a product g = g+· g− with
g±∈ ˆG∆ ±. But the obvious relation
S(∆) ∗ = S(∆ +)∗· S(∆ −)∗,
gives an example of such a decomposition, so by uniqueness it follows t hat S(∆) ∗ determines the
elements S(∆ ±)∗.
The product ( 46) can be thought of as corresponding to a decomposition of ∆ into a ﬁ nite
number of subsectors, each containing a single ray of height < N . Applying the ﬁrst part repeatedly
therefore shows that S(∆) ∗
<N determines each element S(ℓ)∗
<N for rays ℓ⊂ ∆. Since this holds for
arbitrarily large N it follows that S(∆) ∗ determines the elements S(ℓ)∗ for all such rays. But the
elements S(ℓ)∗ faithfully encode the invariants DT( γ) for classes γ∈ Γ satisfying Z(γ)∈ ℓ, so the
result follows. □
Remark A.4. Suppose given a framed variation of BPS structures (Γ , Zp, Ω p) over a manifold M
such that at some point (and hence at all points) p∈ M the form⟨−,−⟩ = 0 vanishes. Then the
Lie algebras ˆg∆ are abelian, and hence so too are the associated groups ˆG∆ . It follows that the
wall-crossing formula is satisﬁed if all elements Sp(ℓ)∗ are taken to be constant as p∈ M varies. It
follows from Lemma
A.3 that the BPS invariants Ω p(γ) = Ω( γ) are constant.
One can also easily see the following statement: suppose given a fram ed variation of BPS
structures (Γ , Zp, Ω p) over a manifold M. Then for any ﬁxed class γ∈ Γ there is a locally-ﬁnite
collection of codimension one real submanifolds Wi⊂ M such that the invariant Ω( γ) is constant
on the open complement
M\
⋃
Wi. (51)
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 43
The submanifolds Wi are called walls for the class γ, and the connected components of the com-
plement ( 51) are called chambers.
