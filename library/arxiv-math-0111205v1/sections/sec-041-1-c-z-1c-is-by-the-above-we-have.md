---
doc_id: arxiv-math-0111205v1
doc_title: "From Subfactors to Categories and Topology II"
section_id: sec-041-1-c-z-1c-is-by-the-above-we-have
section_title: "(C) ≃ Z 1(C) is. By the above, we have"
section_number: 1
pages: 48-49
source_pdf: 0111205v1.pdf
source_sha256: 66325a21651aff89
doc_brief: "From Subfactors to Categories and Topology II — For every tensor category C there is a braided tensor category Z(C), the ‘center’ of C."
---
dim(I(C) ∨ ˜I( ˜C)) = dim( C ⊠ ˜C) = (dim C)2, which coincides with the dimension of Z1(C)
by our main theorem. Since dim( I(C) ∨ ˜I( ˜C)) is a full semisimple subcategory of Z1(C)
the categories must coincide. This argument does not work if C is not a ∗-category. We
therefore give another proof which works in generality.
To this purpose we show that the minimal central idempotents of Ξ L corresponding
to the simple objects I(Xk) ˜I(Xl) ∈ Z 1(C), k, l ∈ Γ sum up to the unit of Ξ L. By the
deﬁnitions of I, ˜I we have I(Xk) ˜I(Xl) = ( XkXl, eXkXl(·)) with
eXkXl(Z) = c(Xk, Z) ⊗ idXl ◦ idXk ⊗ c(Z, Xl)−1.
Thus according to Proposition 5.4 the sum over the correspon ding minimal central idem-
potents in Ξ L is given by

∑
k,l
z(I(Xk) ˜I(Xl))

 [i, j, n] = δin
di
∑
k,l
N i
kl∑
α=1
dkdl
Xj Xi
☛ ✟
❆❆
✁
✁
✁
❆❆
Xk Xl
❆
❆
❆ ✁✁
✁✁
✡ ✠
Xi Xj
Computations which are identical to those in Lemma 3.10 (exc ept for turning an over-
into an under-crossing) show that the right hand side equals
=
∑
k
dk
Xj Xi
☛ ✟
❆❆
✁
✁
✁
❆❆
Xk Xk
❆
❆
❆ ✁✁
✁✁
✡ ✠ ❆
❆
❆ ✁✁
✁✁
Xi Xj
=
∑
k
dk
Xj Xi
❆❆
✁
✁
✁
❆❆ ☛ ✟
❆❆
✁
✁
✁
❆❆
Xk Xk
❆
❆
❆ ✁✁
✁✁
✡ ✠
Xi Xj
48
But this is nothing else than
=
( ∑
k
dkS(Xk, Xj )
)
c(Xj , Xi)−1 =
( ∑
k
dkS(Xk, Xj)
)
c(Xi, Xj). (7.2)
Since C is assumed modular we have ∑
k dkS(Xk, Xj) = δj,0 dim C and thus

∑
k,l
z(I(Xk) ˜I(Xl))

 [i, j, n] = δinδj,0 dim C idXi.
The reader is invited to convince himself that this is the uni t of the tube algebra Ξ L by
plugging it into (5.2). ■
The method used in the proof allows to prove the following cha racterization of modular
categories, which appeared in [7].
Corollary 7.11 (of proof) Let C be a F-linear semisimple spherical braided tensor cat-
egory with ﬁnitely many simple objects. Then C is modular iﬀ dim C ⁄= 0 and Z2(C) is
trivial.
Proof. If C is modular then dim C ⁄= 0 [53] and Z2(C) is trivial. If, conversely, Z2(C) is
trivial then for every j ⁄= 0 there exists i such that c(Xi, Xj) ⁄= c(Xj , Xi)−1. But then
(7.2) implies ∑
k dkS(Xk, Xj) = 0 ∀j ⁄= 0, which is known to be equivalent to invertibility
of S. ■
Remark 7.12 It is well known that a braided tensor category C is monoidally isomorphic
to its reverse Crev which coincides with C as a category but has the tensor product reversed:
X ⊗rev Y := Y ⊗ X. On the other hand the duality functor X ↦→X provides a monoidal
equivalence Cop ⊗
≃ C rev . Putting this together we have ˜C
⊗
≃ C
⊗
≃ C rev ⊗
≃ C op. Thus for
modular C we actually have an equivalence Z1(C)
⊗
≃ C ⊠ Cop of tensor categories, not just
weak monoidal Morita equivalence. ✷
