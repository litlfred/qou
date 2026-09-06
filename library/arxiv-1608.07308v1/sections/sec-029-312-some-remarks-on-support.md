---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-029-312-some-remarks-on-support
section_title: "Some remarks on support"
section_number: 3.12
pages: 31-32
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
the sheafBσ on FHilbdg
n . For any braidσ, letwσ∈Sn denote the underlying permutation.
Proposition 3.18. (e.g. [36, Proposition 2.16]) For any braidσ and for all i∈{ 1,...,n}, the
left action ofxi on the complexσ∈Kb(SBimn) is homotopic to the right action ofxwσ(i).
In short, we will say that the left action R ↷σ is homotopic to the right actionσ ↶w(σ) R,
twisted by the permutationwσ. As a consequence, we obtain the following result:
Corollary 3.19. TheR–module RHomKb(SBimn)(1,σ ) is supported on the subspace:
{
xi =xwσ(i), i= 1,...,n
}
⊂ Cn.
Our construction of Conjecture 1.1 is predicated on the expectation that:
HomKb(SBimn)(1,σ ) =RΓ(FHilbdg
n,B(σ))
and that moreoverB(σ) can be reconstructed from the spacesHomKb(SBimn)(1,σ·∏n
i=1Lai
i ) for
all sequences of large enough natural numbers (a1,...,a n). These Hom spaces in the category
SBimn are very hard to compute, and all we can say at this stage is that Corollary 3.19 still
applies to them. Therefore, we obtain the following:
Corollary 3.20. The complexB(σ) =ι∗(σ) is supported on the subvariety:
FHilbdg
w :=ρ−1({
xi =xwσ(i), i= 1,...,n
})
⊂ FHilbdg
n = FHilbdg
n (C)
whereρ : FHilbdg
n (C)→ Cn is the map that records the eigenvalues(x1,...,x n), akin to (2.3).
Corollary 3.21. Suppose that the closure ofσ is connected. ThenB(σ) is supported on
ρ−1 ({x1 =... =xn}) = FHilbn(point)× C.
Remark 3.22. Following Section 1.9, one can prove that if the closure of σ is connected, then
the sheafB(σ) ﬁbers trivially over C, i.e.:
B(σ) =B(σ)⊠OC
for some sheafB(σ)∈ DbCoh(FHilbn(point)). Since FHilbn(point) is projective, the coho-
mology of this sheaf is expected to be ﬁnite-dimensional. Moreover, our conjectures imply the
fact that this cohomology matches the reduced Khovanov-Rozansky homology ofα.
In general, FHilbdg
w may be quite complicated. However, for certain permutations w = wσ
we can describe it explicitly. The baby case is whenw = (j,j + 1) is a transposition.
Deﬁnition 3.23. Deﬁne the dg subschemeZj⊂ FHilbdg
n by the following equation:
(3.46) OZj :=
[
... −→q2t2L2
j
L2
j+1
yj,j+1
−−−→q2tLj
Lj+1
xj−xj+1
−−−−−→qtLj
Lj+1
yj,j+1
−−−→qO
xj−xj+1
−−−−−→O
]
.
Hereyj,j+1 : tLj→L j+1 is the map of line bundles induced by the homonymous coefﬁcient
of the matrixY in (2.14), and the fact thatyj,j+1(xj−xj+1) = 0 follows from [X,Y ] = 0.
32 EUGENE GORSKY, ANDREI NEGUT , , AND JACOB RASMUSSEN
Remark 3.24. Formula (3.46) implies the following exact sequence:
(3.47)
[
qO
xj−xj+1
−−−−−→O
]
∼=
[
OZj
Id
− →qtLj
Lj+1
⊗OZj[2]
]
Our motivation for deﬁningZj is the fact that:
(3.48) OFHilbdg
(j,j+1)
=OZj
for allj∈{ 1,...,n − 1}. The following proposition follows directly by iterating (3.48).
Proposition 3.25. Suppose thatw has cycle structure:
(1,...,k 1)(k1 + 1,...,k 2),..., (kr + 1,...,n )
for some sequence 0 < k1 < ... < kr < n. Then the dg structure sheaf of FHilbdg
w has the
following periodic resolution by locally free sheaves on FHilbdg
n :
(3.49) OFHilbdg
w
∼=
⨂
j/∈{k1,...,kr}
[
... −→q2tLj
Lj+1
xj−xj+1
−−−−−→qtLj
Lj+1
yj,j+1
−−−→qO
xj−xj+1
−−−−−→O
]
.
Conjecture 3.26. Suppose thatα =∏r
i=0(σki+1··· σki+1−1) is a subword of the Coxeter word
σ1··· σn−1, for any sequence 0<k 1 <...<k r <n as in Proposition 3.25. Then:
B(α) =OFHilbdg
w
.
Example 3.27. For α = 1 , the conjecture simply reads B(α) = OFHilbdg
n
, as prescribed by
Conjecture 1.1. Forα =σ1··· σn−1, the conjecture readsB(α) =OFHilbdg
n (point)×C.
Conjecture 3.26 gives a full description ofB(α) for all braidsα on two strands (see Section
5 for the explicit construction in this case). Moreover, it completely describes B(α) for the
braidsα = 1,s 1,s 2,s 1s2 on 3 strands, multiplied by arbitrary powers of the twists FT2, FT3.
Building upon this, the following conjecture supersedes the main conjecture of [30], and it
serves as one of the motivating examples of the present work:
Conjecture 3.28. For gcd(m,n ) = 1, consider the torus braidαn,m = (σ1··· σn−1)m. Then
(3.50) B(αm,n) =
( n⨂
i=1
L⌊im
n⌋−⌊
(i−1)m
n ⌋
i
)
⊗O FHilbdg
n (point)×C
See Sections 5 and 6 for detailed computations for two and three-strand torus braids.
Remark 3.29. It was proved in [30] that the equivariant Euler characteristic of the right hand
side of (3.50) is equal to the “reﬁned Chern-Simons invariant” deﬁned by Aganagic-Shakirov
[2] and Cherednik [17]. One can therefore consider Conjecture 3.28 as a categoriﬁcation of the
conjectures in [2, 17] relating the Poincar ´e polynomial of Khovanov-Rozansky homology to
these “reﬁned invariants”.
4. C ATEGORIES AND SCHEMES
