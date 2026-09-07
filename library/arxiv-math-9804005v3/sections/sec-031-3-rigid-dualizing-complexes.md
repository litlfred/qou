---
doc_id: arxiv-math-9804005v3
doc_title: "RINGS WITH AUSLANDER DUALIZING COMPLEXES"
section_id: sec-031-3-rigid-dualizing-complexes
section_title: "Rigid Dualizing Complexes"
section_number: 3
pages: 16-18
source_pdf: 9804005v3.pdf
source_sha256: 62d069533bb97a00
doc_brief: "RINGS WITH AUSLANDER DUALIZING COMPLEXES — A ring with an Auslander dualizing complex is a generalizati on of an Auslander-Gorenstein ring."
---
In this section we consider dualizing complexes which satisfy a special condition
discovered by Van den Bergh [VdB]. Rigid dualizing complexes are unique and
even functorial. Furthermore if R is an Auslander rigid dualizing complex then the
canonical dimension CdimR is particularly well behaved (as examples indicate; see
Question 3.15). By default A and B denote noetherian k-algebras.
First we shall need some more notation for bimodules. Suppose A and B are
k-algebras. For an element a ∈ A we denote by a◦ ∈ A◦ the same element. Thus
fora1,a 2 ∈A,a◦
1 ·a◦
2 = (a2 ·a1)◦ ∈A◦. With this notation if M is a right A-module
then the left A◦ action is a◦ ·m =m ·a,m ∈M . The algebra Ae has an involution
Ae → (Ae)◦, a1 ⊗a◦
2 ↦→a2 ⊗a◦
1 which allows us to regard every left Ae-module M
as a right Ae-module in a consistent way:
(a1 ⊗a◦
2) ·m = (a2 ⊗a◦
1)◦ ·m =m · (a2 ⊗a◦
1) = a1 ·m ·a2.
Given an (A ⊗B)-module M and a (B ⊗A)-module N we deﬁne a mixed action
of Ae ⊗Be on the tensor product M ⊗N as follows. Ae acts on M ⊗N by the
outside action
(a1 ⊗a◦
2) · (m ⊗n) := (a1 ·m) ⊗ (n ·a2),
whereas Be acts on M ⊗N by the inside action
(b1 ⊗b◦
2) · (m ⊗n) := (m ·b2) ⊗ (b1 ·n).
By default we regard the outside action as a left action and the inside action as
a right action. If A = B and M = N then the two actions by Ae on M ⊗M
are interchanged the involution m1 ⊗m2 ↦→m2 ⊗m1. However for the sake of
deﬁniteness in this case, given an Ae-module L, HomAe (L,M ⊗M ) shall refer to
homomorphismsL →M ⊗M which areAe-linear with respect to the outside action.
Deﬁnition 3.1 ([VdB] Deﬁnition 8.1) . Suppose R is a dualizing complex over A.
If there is an isomorphism
φ :R
≃
→ R HomAe(A,R ⊗R)
in D(ModAe), we call ( R,φ ) a rigid dualizing complex .
It is obvious that if R is rigid, then any shift R[n], for n ⁄= 0, is no longer rigid.
Van den Bergh proved that a rigid dualizing complex ( R,φ ) over A is unique, up to
an isomorphism in D(ModAe) (see [VdB] Proposition 8.2). Below we extend this
result by proving that rigid dualizing complexes are functorial, in a suit able sense.
Let A → B be a k-algebra homomorphism. Given M ∈ D+(ModB), N ∈
D+(ModA) and a morphism ψ :M →N in D(ModA),ψ factors naturally through
R HomA(B,N ). This can be seen by replacing N with an injective resolution I in
D+(ModA), and then we can take ψ to be a homomorphism of complexes. The
image of ψ will then land inside Hom A(B,I ). The same fact is true for bimodules.
We say a k-algebra homomorphism A →B if ﬁnite if B is ﬁnitely generated as
a left and as a right A-module.
Theorem 3.2. Let A → B be a ﬁnite k-algebra homomorphism. Suppose A and
B have rigid dualizing complexes (RA,φA) and (RB,φB) respectively. Then there
is at most one morphism ψ :RB →RA in D(ModAe) satisfying conditions (i) and
(ii) below:
RINGS WITH AUSLANDER DUALIZING COMPLEXES 17
(i) ψ induces an isomorphism
RB ∼= R HomA(B,RA) ∼= R HomA◦ (B,RA)
in D(ModAe).
(ii) The diagram
RB
φB
− − − − →R HomBe (B,RB ⊗RB)
ψ
↓ ψ⊗ψ
↓
RA
φA
− − − − →R HomAe (A,RA ⊗RA)
in D(ModAe) is commutative.
The theorem is proved after this lemma. Given a k-algebra homomorphism
A →B, denote by Z B(A) ⊂B the centralizer of A.
Lemma 3.3. Let A →B be a ﬁnite k-algebra homomorphism. Suppose A and B
have dualizing complexes RA andRB respectively, andψ :RA →RB is a morphism
in D(ModAe) satisfying condition (i) of the theorem. Then HomD(ModAe)(RB,RA)
is a free left and right ZB(A)-module with basis ψ.
Proof. Denote by D := R HomA(−,RA) and D◦ := R HomA◦ (−,RA) the dualizing
functors. By assumption RB ∼=D◦B. Applying the functor D we get isomorphisms
of left ZB(A)-modules
HomD(ModAe)(RB,RA) ∼= HomD(ModAe)(D◦B,D ◦A)
∼= HomD(ModAe)(A,B )
∼= HomAe (A,B ) ∼= ZB(A).
Likewise for the right action.
Proof of the theorem. Assume ψ′ is another such isomorphism. According to the
lemma above,
ψ′ = (b1 ⊗ 1)ψ = (1 ⊗b◦
2)ψ
for suitable bi ∈ ZB(A)×. So
ψ′ ⊗ψ′ = (b1 ⊗b◦
2)(ψ ⊗ψ).
Now the diagram in condition (ii) consists of morphisms in D(ModAe). Since
multiplications by b1 and b◦
2 are Ae-linear, we see that
(b1 ⊗ 1)ψ = (b1 ⊗b◦
2)ψ ∈ HomD(ModAe)(RB,RA).
Hence dividing by the unit b1 ⊗ 1, we see that b2 = 1.
Corollary 3.4. A rigid dualizing complex (R,φ ) over A is unique up to a unique
isomorphism.
Proof. Suppose (R′,φ ′) is another rigid dualizing complex. We claim that there
is an isomorphism ψ : R
≃
→ R′ in D(ModAe) which satisﬁes condition (ii) of the
theorem. By Theorem 3.2 such ψ is unique.
To produce ψ, choose any isomorphism ψ′ : R
≃
→ R′, which we know exists by
[VdB] Proposition 8.2. Then by Lemma 3.3 there are ai ∈ Z(A)× such that
(a1 ⊗ 1)−1ψ′ = (1 ⊗a◦
2)−1ψ′ =φ′−1(ψ′ ⊗ψ′)φ.
