---
doc_id: arxiv-math-9909027v1
doc_title: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California"
section_id: sec-028-4110-to-see-this-observe-that-the-conditional-ex
section_title: "To see this observe that the conditional expectatio n EpN : pM p → pN"
section_number: 4.1.10
pages: 114-115
source_pdf: 9909027v1.pdf
source_sha256: e6cd544cdc141d3b
doc_brief: "Planar Algebras, I V. F. R. Jones ∗ Department of Mathematics University of California — We introduce a notion of planar algebra, the simplest exampl e of which is a vector space of tensors, closed"
---
is just 1
tr(p) EN . It follows that αaj = ajα and clearly αµj = µjα, so by 4.1.24,
α is a ∗-algebra homomorphism.
The next thing to show is that α takes pN -central vectors to θ−1(pk(N ′ ∩
Mk−1)pk), with pk as in 3.3, using the planar algebra structure on N ′ ∩ Mk.
Let π : ⊗k
N M → ⊗ k
N M be the map π(x1 ⊗ x2 . . . ⊗ xk) = px1p ⊗ px2p ⊗ . . . ⊗
pxkp, which is well deﬁned since p commutes with N. Then a diagram shows
that, for x ∈ N ′∩Mk−1, pkxpk = θ(π(θ(x))), and conversely, if θ−1(x) is in the
image of α, π(θ−1(x)) = θ−1(x) so pkxpk = x. Hence α induces a ∗-algebra
isomorphism between P pN ⊂pM p
k and pk(N ′ ∩Mk−1)pk. To check that this map
induces the right planar algebra structure, we ﬁrst observe that α commutes
suitably with the maps η and κ of 4.1.19. For η we have α ◦ η = π ◦ η ◦ α
by deﬁnition. For κ, note that if we perform the basic construction of [J1]
on L2(M), 1
tr(p) pEN p is the basic construction projection for pN ⊂ pM p on
114
L2(pM p). Thus if {b} is a basis for pM p over pN we have ∑
b bEN b∗ = tr(p)p.
So if
x = x1 ⊗ . . . ⊗ xk ∈
k⨂
pN
pM p ,
α(κj(x)) = 1
tr(p)δ
∑
b
x1 ⊗ . . . ⊗ xjb ⊗ b∗ ⊗ xj+1 ⊗ . . . ⊗ xk
and
κj(α(x)) = 1
δ
∑
c
x1 ⊗ . . . ⊗ xjc ⊗ c∗ ⊗ xj+1 ⊗ . . . ⊗ xk .
Applying θ we see that ακj = κjα.
With these two commutation results it is an easy matter to che ck that α
deﬁnes planar algebra isomorphism between P N p⊂pM p and p(P N ⊂M )p, using
the uniqueness part of 4.2.1 or otherwise.
Corollary 4.2.15 If N1 ⊂ M1 and N2 ⊂ M2 are extremal ﬁnite index
subfactors, then P N1⊗N2⊂M1⊗M2 is naturally isomorphic to the tensor product
P N1⊂M1 ⊗ P N2⊂M2 of §3.4.
Proof. We leave the details to the reader. □
