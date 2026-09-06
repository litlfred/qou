---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-020-43-duality-for-actions-an-analogue-of-the-blattn
section_title: "Duality for actions. An analogue of the Blattner-Montgomery duality the-"
section_number: 4.3
pages: 14-14
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
orem for actions of quantum groupoids was proven in [N2]. Let H be a ﬁnite
quantum groupoid and A be a left H-module algebra. Then the smash product
A#H is a left ˆH-module algebra via
φ · (a#h) = a#(φ⇀h ), φ ∈ ˆH, h∈H, a∈A.(24)
In the case when H is a ﬁnite dimensional Hopf algebra, there is an isomorphism
(A#H)# ˆH ∼= Mn(A), where n = dim H and Mn(A) is an algebra of n-by-n
matrices over A [BM]. This result extends to quantum groupoid action in the
form (A#H)# ˆH ∼= End(A#H)A, where A#H is a right A-module via multi-
plication (note that A#H is not necessarily a free A-module, so that we have
End(A#H)A ⁄∼=Mn(A) in general).
Theorem 4.3.1 ([N2], 3.1, 3.2) . The map α : (A#H)# ˆH → End(A#H)A deﬁned
by
α((x#h)#φ)(y#g) = (x#h)(y#(φ⇀g )) = x(h(1) ·y)#h(2)(φ⇀g )
for all x,y ∈A, h,g ∈H, φ∈ ˆH is an isomorphism of algebras.
Proof. A straightforward (but rather lengthly) computation shows that α is a well
deﬁned homomorphism, cf. ([N2], 3.1). Let {fi} be a basis of H and {ξi} be
the dual basis of ˆH, i.e., such that ⟨fi, ξj ⟩ = δij for all i,j , then the element∑
i fi ⊗ξi ∈H ⊗k ˆH does not depend on the choice of {fi} and the following map
β : End( A#H)A → (A#H)# ˆH
: T ↦→
∑
i
T (1#fi(2))(1#S−1(fi(1)))#ξi.
is the inverse of α.
Corollary 4.3.2. H# ˆH ∼= End(H)Ht , therefore, H# ˆH is a semisimple algebra.
Proof. Theorem 4.3.1 for A = Ht shows that H is a projective generating Ht-
module such that End( H)Ht
∼=H# ˆH. Therefore, Ht and H# ˆH are Morita equiv-
alent. Since Ht is semisimple (as a separable algebra), H# ˆH is semisimple.
