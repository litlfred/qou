---
doc_id: arxiv-2210.09583v1
doc_title: "A NEW PRESENTATION OF THE osp(1|2)-POL YNOMIAL LINK INVARIANT"
section_id: sec-011-43-e-graded-covering-khovanov-homology
section_title: "e-graded Covering Khovanov Homology"
section_number: 4.3
pages: 15-16
source_pdf: 2210.09583v1.pdf
source_sha256: 38fc6fa465a06a7b
doc_brief: "A NEW PRESENTATION OF THE osp(1|2)-POL YNOMIAL LINK INVARIANT — There is a known connection between the osp(1|2n) polynomial knot invariant J n K and the so(2n + 1) knot invariant soJ n K studied by"
---
π for the remainder of the paper. This
section assumes prior knowledge of Putyra’s work on Covering Khov anov homology [ 28]. For the sake
of brevity we omit most of the technical details and deﬁnitions involvin g ”chronology”. Covering
Khovanov homology constructs a chain complex of modules over the ring k := /CI [X, Y, Z]/(X 2 = Y 2 =
1) such that the homology of the chain complex if we specialize X, Y, Z to be 1 is regular Khovanov
homology and the homology of the chain complex where we take X, Z to be 1 but Y to be −1 is Odd
Khovanov homology. For our purposes, we can describe this as a ch ain complex of R = /CI
π modules
with π playing the role of Y .
We ﬁrst construct an e-graded version of the generalized Khovan ov bracket eKh cov(L) from [ 28,
Deﬁnition 5.9] by following the exact same procedure as Putyra exce pt we handle the gradings and
shifts exactly as in Section 4.2. This is a chain complex in the additive closure of the R-linear category
of chronological cobordisms RChCob.
Then one can show that this complex is an invariant of oriented links if w e consider it as a chain
complex of chronological cobordisms modulo the S, T, and 4Tu relatio ns [ 28, Section 7]. The quotient
of RChCob by these relations is denoted RChCob/ℓ. The proof of invariance is exactly the same as
the proof presented in [ 28, Section 7].
Deﬁnition 4.11. [28, Deﬁnition 10.1] Set G = /CI × /CI
4 × /CI
2, and U (R) to be the group of invertible
elements in R. Then deﬁne a group homomorphism λ : G × G → U (R) by
λ((a, b, c)(d, e, f)) = πcf
We also deﬁne a e-graded super tensor product of G-graded modules as usual, but for homogeneous
homomorphisms f, g we deﬁne f ⊗ g by the formula:
(f ⊗ g)(m ⊗ n) = λ(deg(g), deg(m))f (m) ⊗ g(n)
This deﬁnes a symmetric monoidal structure on the category of G-graded R-modules, which we call
R-egSmod.
16 MARK EBERT
We refer to R-egSmod as the category of e-graded R-supermodules.
Deﬁnition 4.12. Let A = R[X]/(X 2) be the free e-graded R-supermodule of rank 2 spanned by /BD
and X in degrees deg(/BD ) = (1 , −1, 0) and deg(X) = ( −1, 1, 1). Equip it with the following operations
ε : A → R
{
/BD → 0
X → 1(4.10)
η : R → A {1 → /BD(4.11)
m : A ⊗ A → A
{
/BD ⊗ /BD → /BD /BD ⊗ X → X
X ⊗ /BD → X X ⊗ X → 0(4.12)
∆ : A → A ⊗ A
{
/BD → π /BD ⊗ X + X ⊗ /BD
X → X ⊗ X(4.13)
These maps have degrees
deg(∆) = ( −1, 1, 1), deg (m) = ( −1, 1, 0), deg (ε) = (1 , −1, 1), deg (η) = (1 , −1, 0).
The pair ( R, A) with these operations deﬁnes a Chronological Frobenius system a s in [ 28, Deﬁnition
10.5] Then we obtain a well deﬁned, degree preserving chronologica l TQFT functor F : RChCob →
R-egSmod as in [ 28, Proposition 10.6]. This functor preserves the S, T, and 4Tu relatio ns, so we get
a well-deﬁned functor Fcov : RChCob/ℓ → R-egSmod.
Let Ccov(L) be the chain complex of e-graded R-supermodules given by Ccov(L) := Fcov(eKh cov(L)).
When π = 1, Ccov(L) = C(L) by construction, which is the chain complex for e-graded Khovano v
homology. We call the homology H(Ccov(L)) of this complex the e-graded version of covering Khovanov
homology. If we forget the /CI
4-grading of each module in the complex, then we obtain the covering
Khovanov homology Hcov(L) deﬁned in [ 28, Example 10.7].
