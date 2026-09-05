---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-045-91-general-method-of-the-proof
section_title: "General method of the proof"
section_number: 9.1
pages: 47-50
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
operation. From construction of the reduced convolution ¯⋆ we see that the key step of computation of G¯⋆F is
the ”computation” of CE n2 (¯π∗
12⊗B ¯π∗
23)(G ⊠F ). The latter complex is a matrix factorization with non-trivial
potential, we can not compute its cohomology in conventional sense , since the diﬀerential does not square
to 0. However, we can get quite close to that by contracting the pa rt of the complex with non-trivial action
of n(2). We give details below.
To simplify notations we consider problem of simplifying of the complex C En(F )T whereF∈ MFsc
B (G×
Z,F ), F ∈ C[G×Z]B and B acts on G by the left multiplication and acts trivially on Z. Let R = C[G]
and R⟨χ⟩ is the ring with B-equivariant structure twisted by the character χ∈ Hom(T, C∗): b· 1 = χ(b)1
for b∈ B and 1∈R⟨χ⟩ is the generator of R-module R⟨χ⟩. We assume that the matrix factorization that
we study is the sum of free R-modulesF = (M,D ) M =⊕N
i=1Mi and Mi = C[Z]⊗R⟨χi⟩. It is well known
that the CE homology of such free modules has a geometric interpre tation, we were unable to pinpoint a
proof of the interpretation and provide an outline of a proof for it
47
Proposition 9.1. For any χ∈ Hom(T, C∗)
H∗
Lie(n,R⟨−χ⟩)T = H ∗(G/B,L χ),
where LHS is the coherent sheaf cohomology.
Proof. Let Sn be the symmetric group and B−⊂G =GLn the subgroup of lower triangular matrices. The
Bruhat decomposition G = BSnB implies G = B−SnB because B− = w0Bw0 with w0∈ Sn being the
longest element of Sn. Each subset Gw =B−wB⊂G is an open B-invariant subset of G and let us denote
by Rw the ring of regular functions on Gw. Respectively, we denote by GS :=∩w∈SGw where S⊂Sn is a
ﬁnite subset and we use notation RS for the ring of regular functions on GS. In particular, we have R =R∅.
There are natural inclusion maps RS→RS′ forS⊂S′ and these inclusions maps with appropriate sings
form a Cech resolution ˇC•(R) of R by free n-modules ˇCi(R) = ∑
|S|=iRS. On other hand let us observe that
the decomposition above turns in a Cech cover ˇC•(G/U ) of G/U ,G/U =∪w∈SnB−w, we use same notation
for the resolution of the sheaf of regular functions on G/U induced by the cover.
Next we observe that Rw = C[B−]⊗ C[U ], Lie(U ) = n and n does not act on the ﬁrst factor. Since
H ∗
Lie(n, C[U ]) = C we see that H ∗
Lie(n,R ) = ˇC∗(G/U ). The last isomorphism is T -equivariant hence the
proposition follows.
✷
LHS of the last equation is the total space cohomology of the line bun dle Lχ. The ﬁber of Lχ at
V • ={V 1⊂···⊂ V n}∈ G/B is equal to ⨂
i(V i+1/V i)di where χ = ∑ diαi. The most important case of
this theorem is the case n = 2:
H∗
Lie(n,R⟨−kα⟩) = H ∗(P1,O(k)).
The other way to present previous proposition is to say that we use homotopy equivalence CE n(R⟨χ⟩)T∼
⊕iH i(G/B,L χ) where the RHS is complex with zero diﬀerential. The homotopy could b e constructed
explicitly by combining Chech resolution technique with the Gauss elimina tion method from below.
Proposition 9.2. LetF = (M,D )∈ MFB(G×Z,F ) as above then there is a homotopy equivalence
CEn(F )T∼ (⊕N
i=1H ∗(G/B,L ρi ), ¯D)∈ MF(Z,F ),
where ¯D is the diﬀerential induced by the diﬀerential D.
Proof. As in the proof of proposition 9.1 we can construct the Cech resolut ion ˇC•(M ) of M . Since the
Chevalley-Eilenberg diﬀerential dCE is acyclic on term of the ˇC•(M ) we apply Gauss elimination to construct
homotopy CE n(F )∼ (H 0
Lie(n, ˇC•(M ),D ′) with D′ induced by D. As it is explained in proposition 9.1
H ∗(H 0(n, ˇC•(M )),d ˇC ) = H ∗(G/B,M ) =⊕iH ∗(B/G,L ρi ) hence we again can apply the Gauss elimination
and obtain the homotopy from the statement of the proposition. ✷
The Gauss elimination lemma is the standard tool of homological algebr a, one can ﬁnd more discussion
(and applications) of this lemma in [4] in the case of complexes of vecto r spaces. Our proof below is very
close to the argument of [4].
48
Lemma 9.3. SupposeM =W⊕V , V =V 0⊕V 1, W =W 0⊕W 1 and
Di,i+1 =di,i+1
V V +di,i+1
V W +di,i+1
W v +di,i+1
W W,
di,i+1
AB ∈ Hom(Bi+1,A i) form the matrix factorization (M,D )∈ MF(Z,F ), D = D01 +D10. Let us also
assume d10
V V =φ is an isomorphism.
Then there is a homotopy equivalence in the category of matri x factorizations
(M,D )∼ (W,D W ), D W =D10
W +D01
W,
D10
W =d10
W W−d10
W V◦φ−1◦d10
V W, D 01
W =d01
W W.
Proof. Let us that ( W,D W )∈ MF(Z,F ). First, let us ﬁrst compute D2
W|W 0 :
d01
W W◦ (d10
W W−d10
W V◦φ−1◦d10
V W ) = d01
W W◦d10
W W +d01
W V◦d10
V V◦φ−1◦d10
V W =F,
where we used d01
W W◦d10
W V +d01
W V◦d10
V V = 0 for the ﬁrst equality. The check that D2
W|W 1 =F is similar.
Next we deﬁne morphisms i :W→M and π :M→W :
i =
ñ
1
ψ
ô
, π =
î
1 ρ
ó
,
hereψ =ψ00
V W +ψ11
V W,ρ =ρ00
W V +ρ11
W V andψ00
V W =−φ−1◦d10
V W ,ψ11
V W = 0, ρ00
W V = 0, ρ11
W V =−d10
W V◦φ−1.
It is immediate to see that D◦i =i◦DW and DW◦π =π◦D. Also since ψ◦π = 0 and π◦ψ = 0 we
get π◦i = 1. On the other hand we can extend by 0 the map φ−1 to obtain φ′∈⊕ i Hom(V i,V i+1) and
χ =
ñ
φ′ 0
0 0
ô
.
Since φ−1◦d10
V V = 1 and d10
V V◦φ−1 = 1 we see that i◦π− 1 = χ◦D +D◦χ ✷
Thus to obtain the reduction ¯D from the lemma we apply previous lemma to our complex CE n(F )T .
To keep exposition clear let us explain one would apply the elimination lemm a to construct homotopy
(⊕N
i=0Ci,d •)∼ (H •(C,d ), 0): the case of matrix factorizations from proposition 9.1 diﬀers fr om this model
case by feature that on every step of our construction we need t o compute correction diﬀerentials.
Indeed, in our model case we can construct a non-canonical splitt ing C0 = Im d1⊕ H 0(C,d ), C1 =
Kerd1⊕C1/Kerd1. The diﬀerential d1 provides an isomorphism between Im d1 and C1/Kerd1 and we can
apply elimination lemma to obtain homotopy equivalent complex ( C′,d )⊕ (H0(C,d ), 0): C′
i = Ci, i > 1,
C′
1 = Kerd1. Now we can apply the case method to the complex ( C′,d ) and so on.
To simplify notations, we assume for the rest of the section that G = G2 = SL2, B = B2 ⊂ G2,
b = Lie(B2). Respectively, character group of B2 under this assumption is Z, 1 ∈ Z corresponds to the
characterχ1 from the section 7.3
49
