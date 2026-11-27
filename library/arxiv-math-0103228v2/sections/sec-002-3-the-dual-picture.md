---
doc_id: arxiv-math-0103228v2
doc_title: "arXiv:math/0103228v2 [math.QA] 9 Apr 2002"
section_id: sec-002-3-the-dual-picture
section_title: "The Dual Picture"
section_number: 3
pages: 14-16
source_pdf: 0103228v2.pdf
source_sha256: 7d66dbbd4b87798f
toc_source: inferred
doc_brief: "arXiv:math/0103228v2 [math.QA] 9 Apr 2002 — Coideal subalgebras of the quantized enveloping algebra ar e sur- veyed, with selected proofs included."
---
In this section, we consider the connection between coideal subalgebras of
U and coideal subalgebras inside the Hopf dual of U. The results presented
in this section are well known and are related to the theory of quantum
homogeneous spaces. A good reference for most of the materia l presented
here and for other basic results about quantum homogeneous s paces is [KS,
Chapter 11] (see also [Jo, 1.4.15]).
LetRq[G] denote the quantized function algebra of the connected, si mply
connected algebraic Lie group G with Lie algebra g. (See [Jo, Section 9.1]
for a precise deﬁnition.) Note that up to a ﬁnite group, Rq[G] is the Hopf
dual of U. Furthermore, Rq[G] satisﬁes a Peter-Weyl theorem ([Jo, 9.1.1 and
1.4.13]). That is, there is an isomorphism of U bimodules
(3.1) Rq[G] ∼=
⨁
λ ∈P +(π )
L(λ) ⊗L(λ)∗.
14
HereL(λ) is the (left) ﬁnite-dimensional simple U module with highest weight
λ contained in the set P +(π) of dominant integral weights. Moreover, L(λ)∗
is thought of as a right U module. Thus, the right U module action on Rq[G]
comes from the action of U on L(λ)∗, while the left action comes from the
action of U on L(λ).
Given a left coideal I of U and a (left) U module M, a (left) invariant is
an m ∈M such that am =ǫ(a)m for all a ∈I. Write M I
l for the collection
of all left invariants in M. Equivalently, M I
l is equal to the elements of
M annihilated (on the left) by the augmentation ideal of I. Consider the
special case where I is the quantum analog of the enveloping algebra of a Lie
subalgebra of g corresponding to a subgroup H of G. Then Rq[G]I
l is often
written as Rq[G/H]. In particular, Rq[G/H] is thought of as the quantized
function algebra on the quotient space G/H.
Theorem 3.1 For any left coideal I ofU, Rq[G]I
l is a left coideal subalgebra
of Rq[G].
Proof: Letφ,φ ′ be elements of Rq[G]I
l andr an element of I. We ﬁrst show
that φφ′ is also in Rq[G]I
l . To see this, consider
r · (φφ′) =
∑
(r(1) ·φ)(r(2) ·φ′)
=
∑
(r(1) ·φ)ǫ(r(2))φ′ = (r ·φ)φ′ =ǫ(r)φφ′
We now check the coideal condition. One can show using the pre cise
deﬁnition of the action of U on Rq[G] and the coalgebra structure of Rq[G]
that
(3.2) ∆ (r ·φ) = (1 ⊗r)∆ (φ) =
∑
φ(1) ⊗r ·φ(2).
On the other hand,
(3.3) ∆ (r ·φ) = ∆ (ǫ(r)φ) =
∑
φ(1) ⊗ǫ(r)φ(2).
Since we can choose the φ(1) to be linearly independent, (3.2) and (3.3) force
r ·φ(2) =ǫ(r)φ(2). Thus each φ(2) ∈Rq[G]I
l . ✷
In [KS, Chapter 11.6], a quantum homogeneous space associat ed to Rq[G]
is deﬁned up to isomorphism as a one-sided coideal subalgebr a of Rq[G].
(Note that quantum homogeneous spaces are actually quantum analogs of
15
the algebra of regular functions on classical homogeneous s paces.) Thus the
theorem above shows there is a left quantum homogeneous spac e, Rq[G]I
I,
associated to each left coideal subalgebra I. Using the Peter-Weyl decompo-
sition (3.1), we obtain the following nice description of Rq[G]I
l .
(3.4) Rq[G]I
l ∼=
⨁
λ ∈P +(π )
L(λ)I
l ⊗L(λ)∗.
Now Rq[G]I
l is the set of left I invariants of Rq[G]. We may similarly
deﬁne the set of right I invariants Rq[G]I
r. Using the fact that the right
action satisﬁes ∆ (φ ·r) = ∆ (φ) · (r ⊗ 1), the same argument as in the proof of
Theorem 3.1 shows that Rq[G]I
r is a right coideal subalgebra of Rq[G]. One
may also study the set of bi-invariants Rq[G]I
bi =Rq[G]I
l ∩Rq[G]I
r. As above,
Rq[G]I
bi is a subalgebra of Rq[G]I. However, it is not a coideal.
