---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-034-28-ben-elias-and-geordie-williamson
section_title: "BEN ELIAS AND GEORDIE WILLIAMSON"
section_number: 28
pages: 28-29
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
Theorem 3.15. Let h be a Soergel realization ofW . There is a unique isomorphism of Z[v±1]-
algebras:
ε : H
∼
− →[SBim]
H s ↦→[Bs].
Given Soergel bimodules B and B′ the graded rank of Hom(B,B ′) as a free left (or right)
R-module is given by (ε−1[B],ε −1[B′]), where (−, −) denotes the standard pairing on H.
The uniqueness of ε is immediate, because {H s}s∈S generates H. To see that ε
is a homomorphism it is enough to check the relations (2.7) an d (2.8). Using the
Frobenius algebra structure and the isomorphismR ∼=Rs ⊕Rs(−2) ofRs-bimodules,
one can easily check that
(3.6) Bs ⊗Bs ∼=Bs(1) ⊕Bs(−1).
This isomorphism categoriﬁes equation (2.7). Under certai n assumptions on the re-
alization, the categoriﬁcation of equation (2.8) comes fro m an explicit description of
Bw as the image of a certain idempotent, for every w contained in a standard rank 2
parabolic subgroup. More details can be found in [Soe07, §4] or [Elib]. In this paper
we will give an alternate proof of the categoriﬁcation of (2. 8) in more generality . It
follows thatε is a homomorphism of Z[v±1]-algebras.
Once one knows that ε is a homomorphism, the statement that it is an isomor-
phism follows from the classiﬁcation of indecomposable Soe rgel bimodules and the
fact that their characters are upper triangular. More preci sely , if we ﬁx a rex w for
every w ∈ W then the set {Hw | w ∈ W } is easily seen to be upper triangular in
the standard basis of the Hecke algebra with respect to the Br uhat order, and hence
is a basis. On the other hand, Theorem 3.14 shows that {[Bw] | w ∈ W } is upper
triangular in the basis {[Bw] |w ∈W } for [SBim]. As H w is mapped to [Bw] it follows
thatε is an isomorphism.
In fact, Soergel shows that the character map
ch : [ SBim] → H
discussed in previous section provides an inverse to ε. The character map is rather
subtle. In general it is not known how to describe the element ch(Bw) in the Hecke
algebra. However, if k is a ﬁeld of characteristic zero Soergel proposed the follow ing
conjecture, which came to be known as Soergel’s conjecture:
Conjecture 3.16. If k is a ﬁeld of characteristic 0 then ch(Bw) = H w.
It is immediate that Soergel’s conjecture implies the Kazhd an-Lusztig positivity
conjectures. Earlier work of Soergel [Soe90] showed that hi s conjecture also implies
the Kazhdan-Lusztig conjecture. Soergel’s conjecture has recently been proved by
the authors in [EWb] for realizations (not necessarily reﬂe ction faithful) deﬁned over
R, and satisfying a certain positivity property .
SOERGEL CALCULUS 29
Remark 3.17. This statement of Soergel’s conjecture is known to fail when k is a ﬁeld
of ﬁnite characteristic p. The image of [Bw] in H is known as thep-canonical basis, and
its computation is an interesting open problem (see [Wil]).
Remark 3.18. Soergel’s conjecture is false for certain complex realizations of the afﬁne
Weyl group of type A which do not admit any real form (as in part (6) of Example
3.2, when q is a root of unity). See [Elic] for details. Hence the assumpt ion that the
underlying representation be deﬁned over R is essential for Soergel’s conjecture to
hold. (The authors’ proof of Soergel’s conjecture uses posi tivity considerations in a
crucial way!)
The fact that H s is self-biadjoint in the standard pairing is categoriﬁed by the fact
that the functor of tensoring with Bs is its own left and right adjoint. Just as in Re-
mark 2.13, any Hom space between Bott-Samelson bimodules ca n be understood af-
ter adjunction in terms of Hom(R,B w). Soergel’s Categoriﬁcation Theorem combined
with Corollary 2.11 implies that this space is free as a left R-module with a homo-
geneous basis in bijection with the subsequences of w with end-point e. Following
the work of Libedinsky [Lib08], we will show that this basis c an be constructed in a
natural way .
Remark 3.19. Suppose that (W1,S 1) and (W2,S 2) are Coxeter systems and S1 ⊂ S2
is an inclusion realizing W1 as a standard parabolic subgroup of W2. Suppose also
that we have a W1-equivariant inclusion of realizations h1 ⊂ h2. There is an obvious
functorι : BSBimS1 → BSBimS2 sendingB1
s ↦→B2
s . Soergel’s Categoriﬁcation Theo-
rem implies that this functor is “fully-faithful after base change.” That is, if R1 and
R2 denote the polynomial functions on h1 and h2 respectively then
R2 ⊗R1 Hom(B1
w,B 1
w′) = Hom(B2
w,B 2
w′).
Said another way , homomorphisms fromBw toBw′ only depend on the simple reﬂec-
tions which occur in w andw′ (up to the action of polynomials). The (diagrammatic)
proof that these functors are fully faithful after base chan ge will be clear later in this
paper. As a result, one may deﬁne the category of Soergel bimo dules for (W,S ) even
whenS is inﬁnite, either by working with an inﬁnite dimensional re alization of W ,
or by taking a limit over the categories associated to ﬁnite s ubsets ofS.
