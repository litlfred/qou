---
doc_id: arxiv-0705.2975v1
doc_title: "On the Definitions of Difference Galois Groups"
section_id: sec-005-the-galois-group
section_title: "The Galois group"
section_number: null
pages: 18-20
source_pdf: 0705.2975v1.pdf
source_sha256: 683d6bd44cea6704
doc_brief: "On the Definitions of Difference Galois Groups — We compare several deﬁnitions of the Galois group of a linear diﬀerence equation that have arisen in algebra, analysis and model theory and sh ow"
---
From now on, we assume that all ﬁelds are of characteristic 0. Most of the statements below
can be easily adapted to the positive characteristic case. Let K be a diﬀerence subﬁeld of
U, A ∈ GLn(K), and consider the set S = S(U) of solutions of the equation
σ(X) = AX, det(X) ⁄= 0.
Consider H = Aut(K(S)/KC U ). We will call H the Galois group of σ(X) = AX over
KC U 6.
Then H is the set of CU -points of some algebraic group H deﬁned over KC U . To see
this, we consider the ring R = K[Y, det(Y )−1] (where Y = (Yi,j) is an n ×n matrix of
indeterminates), extend σ to R by setting σ(Y ) = AY , and let L be the ﬁeld of fractions
of R. Then L is a regular extension of K, and there is a K-embedding ϕ of L in U, which
sends CL to a subﬁeld of CU , and DL to a subﬁeld of DU . We let T = ϕ(Y ). Then every
elementg ∈H is completely determined by the matrix Mg =T −1g(T ) ∈ GLn(CU ), since if
B ∈ S , then B−1T ∈ GLn(CU ). Moreover, since KC ϕ(L)(T ) and KC U are linearly disjoint
overKC ϕ(L), the algebraic locus W ofT overKC U (an algebraic subset of GL n) is deﬁned
over KC ϕ(L), and H is the set of elements of GL n(CU ) which leave W invariant. It is
therefore the set of CU -points of an algebraic group H, deﬁned over KC ϕ(L). We let H′
denote the Zariski closure of H(CU ). Then H′ is deﬁned over CU , and it is also clearly
deﬁned over Kϕ(CL), so that it is deﬁned over CU ∩Kϕ(CL) = CU ∩ϕ(CL).
Proposition 4.3 Let H0 denote the connected component of H, and let M0 be the relative
algebraic closure of Kϕ(CL) in ϕ(L), M its Galois closure over Kϕ(CL).
1. dim(H) = tr.deg(L/KC L).
2. M0 is a ﬁnite σ-stable extension of Kϕ(CL) and [H : H0] divides [M :Kϕ(CL)]
3. [H′ : H0] = [ H(CU ) : H0(CU )] equals the number of left cosets of Gal(M/M0) in
Gal(M/Kϕ (CL)) which are invariant under the action of σ by conjugation.
4. If the algebraic closure of CK is contained inCU , then the element σ ∈ Aut(DL/CL) =
Gal(DL/CL) extends to an element of Aut(KC U (T )/KC U ).
Proof. 1. Choose another K-embedding ϕ′ of L into U which extends ϕ on the relative
algebraic closure of KC L in L, and is such that ϕ′(L) and ϕ(L) are linearly disjoint over
M0. Then B =ϕ′(Y )−1T ∈ H(CU ), and tr.deg(ϕ(KC L)(B))/ϕ(KC L)) = tr.deg(L/KC L).
Thus dim( H) = tr.deg(L/KC L).
6 Warning: This is not the usual Galois group deﬁned by model theorist s, please see the discussion in
subsection 4.4.
18
2. As M0 ⊂Kϕ(L), we obtain that [M0 :Kϕ(CL)] is ﬁnite and σ(M0) = M0. Furthermore,
σ(M) = M (see Thm 7.16.V in [5]). The algebraic group H is deﬁned as the set of matrices
of GL n which leaves the algebraic set W (the algebraic locus of T overKϕ(CL)) invariant.
Hence H0 is the subgroup of H which leaves all absolutely irreducible components of W
invariant. Its index in H therefore divides [M :Kϕ(CL)].
3. The ﬁrst equality follows from the fact that H0(CU ) and H′(CU ) are Zariski dense in H0
and H′ respectively. Some of the (absolutely irreducible) components of W intersect S in
the empty set. Indeed, let W0 be the component of W containing T , let W1 be another
component of W and τ ∈ G al(M/Kϕ (CL)) such that W1 = W τ
0 . Then W1 is deﬁned
over τ (M0). If τ deﬁnes a (diﬀerence-ﬁeld) isomorphism between M0 and τ (M0), then τ
extends to an isomorphism between Kϕ(L) and a regular extension of Kϕ(CL)τ (M0), and
therefore W1 ∩ S ⁄= ∅. Conversely, if B ∈ W1 ∩ S , then B−1T ∈ H(CU ), so that B is a
generic of W1. The diﬀerence ﬁelds Kϕ(CL)(B) and Kϕ(L) are therefore isomorphic (over
Kϕ(CL)), and τ (M0) ⊂ Kϕ(CL)(B). Hence the diﬀerence subﬁelds M0 and τ (M0) of M
are Kϕ(CL)-isomorphic. One veriﬁes that M0 and τ (M0) are isomorphic over Kϕ(CL) if
and only if σ−1τ −1στ ∈ Gal(M/M0), if and only if the coset τ Gal(M/M0) is invariant under
the action of σ by conjugation.
4. We know that the algebraic closure K ofK andDU are linearly disjoint over CK =CK.
Leta ∈ϕ(DL) generates ϕ(DL) over ϕ(CL). By 4.1(vi), tp(a/KC U ) = tp(σ(a)/KC U ), and
therefore there is θ ∈ Aut(U/KC U ) such that θ(a) = σ(a). Thus T −1θ(T ) ∈H.
Remarks 4.4 1. Even when the algebraic closure of CK is contained in CU , we still
cannot in general conclude that H′ = H.
2. The isomorphism type of the algebraic group H only depends on the isomorphism type
of the diﬀerence ﬁeld K (and on the matrix A). The isomorphism type of the algebraic
group H′ does however depend on the embedding of K in U, that is, on the isomor-
phism type of the diﬀerence ﬁeld Core(K/K ). Indeed, while we know the isomorphism
type of the diﬀerence ﬁeld M0 over Kϕ(CL), we do not know the isomorphism type
of the diﬀerence ﬁeld M over Kϕ(CL), and in view of 4.3.3, if Gal(M/Kϕ (CL)) is
not abelian, it may happen that non-isomorphic extensions o f σ to M yield diﬀerent
Galois groups.
3. If the action of σ on Gal(Core(K/K )/K) is trivial and Gal(Core(K/K )/K) is abelian,
then
H = H′ and [H : H0] = [M0 :Kϕ(CL)].
Indeed, by Lemma 4.2, M0 is Galois over Kϕ(CL) with abelian Galois group G and
σ acts trivially on G. The result follows by 4.3.3. Thus we obtain equality of H and
H′ in two important classical cases:
a. K = C(t), CK = C and σ(t) = t + 1.
19
b. K = C(t), CK = C and σ(t) = qt for some 0 ⁄=q ∈ C, q not a root of unity.
4. If B ∈ S , then the above construction can be repeated, using B instead of T . We then
obtain an algebraic group H1, with H1(CU ) ≃ Aut(KC U (S)/KC U ). Since KC U (B) =
KC U (T ), the algebraic groups H1 and H are isomorphic (via B−1T ).
5. In the next subsection, we will show that the algebraic gro up H and the algebraic group
GR′ introduced in section 2 are isomorphic when CR′ =CK =DK.
