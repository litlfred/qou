---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-011-11-main-theorems-and-applications
section_title: "Main theorems and applications"
section_number: 11
pages: 34-35
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
11.1. Main theorems. The Reshetikhin-Turaev construction (see [Tu]) derives
from any modular category B over k equipped with a distinguished square root
of dim(B) a 3-dimensional “extended TQFT” τB. The latter is a functor from a
certain extension of the category Cob 3 to vectk; the extension in question is formed
by surfaces with a Lagrangian subspace in the real 1-homology. Fo r an anomaly free
B, we take the element ∆ = ∆ ±∈ k deﬁned in Section 10.1 as the distinguished
square root of dim( B). The corresponding extended TQFT τB does not involve
Lagrangian spaces and is a TQFT in the sense of Section 9.1.
We recall the deﬁnition of τB(M )∈ k for a closed oriented 3-manifold M and
anomaly freeB. Pick a representative set J of simple objects of B. Present M by
surgery on S3 along a framed link L =L1∪···∪ LN . Denote col(L) the set of maps
{1,...,N }→J and, for λ∈ col(L), denote Lλ the framed link L whose component
Lq is oriented in an arbitrary way and colored by λ(q) for all q = 1,...,N . Then
τB(M ) = ∆ −N −1 ∑
λ∈col(L)
( N∏
q=1
dim
(
λ(q)
)
)
FB(Lλ)
where FB is the invariant of B-colored framed oriented links in S3 discussed in
Section 10.1. In particular, we can apply these results to the anoma ly free modular
categoryB =Z(C) provided by Theorem 10.3. We can now state the main theorems
of this paper.
Theorem 11.1. LetC be a spherical fusion category over an algebraically closed
ﬁeld such that dimC ⁄= 0 . Then |M|C = τZ(C)(M ) for any closed oriented 3-
manifold M .
This equality extends to an isomorphism of TQFTs as follows.
Theorem 11.2. Under the conditions of Theorem 11.1, the TQFTs |·| C andτZ(C)
are isomorphic.
The rest of the paper is devoted to the proof of these two theore ms. The proof
is based on the following key lemma.
Lemma 11.3. Under the conditions of Theorem 11.1, the vector spaces |Σ|C and
τZ(C)(Σ) associated with any closed connected oriented surface Σ have equal dimen-
sions.
In the next two sections we deduce Theorems 11.1 and 11.2 from Lem ma 11.3.
(Only the case Σ = S1×S1 of this lemma is needed for the proof of Theorems 11.1.)
Lemma 11.3 will be proved in Sections 14 and 15.
11.2. Corollaries. Theorem 11.1 allows us to clarify relationships between invari-
ants of 3-manifolds derived from involutory Hopf algebras. Let H be a ﬁnite-
dimensional involutory Hopf algebra over an algebraically closed ﬁeld k such that
the characteristic of k does not divide dim( H). By a well-known theorem of Rad-
ford, H is semisimple, so that the category of ﬁnite-dimensional left H- modules
H mod is a spherical fusion category. The category of ﬁnite-dimensio nal left D(H)-
modules D(H)mod, where D(H) is the Drinfeld double of H, is a modular category
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 35
(see [EG, M¨ u2]). Denote by Ku H the Kuperberg invariant of 3-manifolds derived
from H, see [Ku]. Denote by HKR D(H) the Hennings-Kauﬀman-Radford invariant
of 3-manifolds derived from D(H), see [He, KR].
Corollary 11.4. For any closed oriented 3-manifold M ,
KuH (M ) = HKR D(H)(M ) = dim(H)τD(H)mod(M ) = dim(H)|M|H mod.
Proof. By [BW2], we have Ku H (M ) = dim( H)|M|H mod. By [Ke, KL], we have
HKRD(H)(M ) = dim(H)τD(H)mod(M ). Therefore we need only to prove the third
equality. This equality follows from Theorem 11.1 and the fact that th e category
D(H)mod is braided equivalent to Z(H mod), see for example [Ka]. □
We say that two fusion categories are equivalent if their centers are braided
equivalent. For example, two fusion categories weakly Morita equiva lent in the
sense of M¨ uger [M¨ u1] are equivalent in our sense. Theorem 11.2 im plies:
Corollary 11.5. Equivalent spherical fusion categories of non-zero dimens ion over
an algebraically closed ﬁeld give rise to isomorphic TQFTs.
By a Hermitian fusion category we mean a spherical fusion category C over C
endowed with antilinear homomorphisms
{f∈ HomC(X,Y )→ ¯f∈ HomC(Y,X )}X,Y ∈Ob(C)
such that ¯¯f = f , gf = ¯f ¯g, f⊗g = ¯f⊗ ¯g, evX = ~coevX , and coevX = ~evX for
all morphisms f,g inC and all X∈ Ob(C). Note that these axioms imply that
idX = id X , dim(X)∈ R for all X∈ Ob(C) and tr( f )∈ R for all endomorphisms
f inC. A unitary fusion category is a Hermitian fusion category C such that
tr(f ¯f )> 0 for any non-zero morphism f inC. This condition is equivalent to the
condition that dim(V )> 0 for all simple objects V ofC. Clearly, the dimension of
a unitary fusion category is a positive real number.
Corollary 11.6. The TQFT |·| C associated with a unitary fusion category C is
unitary in the sense of [Tu, Chapter III] . In particular |− M|C =|M|C for any
closed oriented 3-manifold M .
Proof. A half braiding ( A,σ ) of C is said to be unitary if σX = σ−1
X for all
X ∈ Ob(C). The unitary center of C, denoted Z u(C), is the full subcategory of
Z(C) formed by the unitary half braidings. The unitary center of C is a braided
subcategory of Z(C). The inclusion Z u(C) ⊂ Z(C) is a braided equivalence,
see [M¨ u2, Theorem 6.4]. Therefore Z u(C) is a modular category. The conjuga-
tion inC induces a conjugation in Z u(C) so thatZ u(C) becomes a unitary modular
category. Hence the TQFT τZ u(C) is unitary. Now there are isomorphisms of
TQFTs τZ u(C)≃τZ(C)≃|·| C. The ﬁrst one is induced by the braided equivalence
Z u(C)≃Z (C) and the second one is given by Theorem 11.2. The unitary structur e
of τZ u(C) is transported to |·| C via the isomorphism τZ u(C)≃|·| C. □
From Corollary 11.6, Theorem 11.2, and Theorem 11.5 of [Tu], we deduc e:
Corollary 11.7. IfC is a unitary fusion category, then ||M|C|≤ (dim(C))g(M)−1
for any closed oriented 3-manifold M , where g(M ) is the Heegaard genus of M .
