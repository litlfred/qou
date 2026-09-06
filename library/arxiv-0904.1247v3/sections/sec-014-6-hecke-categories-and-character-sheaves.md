---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-014-6-hecke-categories-and-character-sheaves
section_title: "Hecke categories and character sheaves"
section_number: 6
pages: 34-38
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
In this section, we study the homotopical algebra of Hecke catego ries arising in representation
theory. Our focus is the Hecke category of D-modules on the double quotient stack B\G/B of a
reductive group G by a Borel subgroup B⊂G, and its unipotent monodromic variant. Our aim is
to construct a topological ﬁeld theory from these Hecke categor ies, and in particular to relate their
traces and centers with character sheaves.
If we introduce the classifying stacks X =BB, Y =BG, then the double quotient stack can be
realized as the ﬁber product
B\G/B≃X×Y X
From this point of view, the special technical features of this setu p are the following:
(1) The morphism p :X→Y is proper.
(2) The diagonal δ :X→X×X is smooth.
The second property is especially restrictive though satisﬁed by cla ssifying spaces of smooth group
schemes. The above conditions will imply that we have a suﬃcient arse nal of duality and adjunctions.
6.1. Hecke categories. We establish here that Hecke categories are semi-rigid categories w ith
a canonical Calabi-Yau structure, and thus two-dualizable monoida l categories deﬁning oriented
topological ﬁeld theories.
To begin, let p :X→Y be a morphism of stacks. Introduce the Hecke category H =D(X×YX).
Consider the convolution diagram
X×Y X×Y X
p12
/d119/d119♥♥♥♥♥♥♥♥♥♥♥♥ p23
/d39/d39PPPPPPPPPPPP
p13
/d15/d15
X×Y X X ×Y X X ×Y X
EquipH =D(X×Y X) with the monoidal product deﬁned by convolution
⋆ :H⊗H /d47/d47H
M⋆ N =p13∗(p!
12(M)⊗p!
23(N))≃p13∗(p12×p23)!(M ⊠ N)
Similar diagrams provide the usual associativity compatibilities of an alg ebra object. The monoidal
unit 1 H is given by the pushforward u∗ωX along the map u :X→X×Y X induced by the diagonal
δ :X→X×X.
Recall that if p :X→Y is safe, then the integral transform construction gives a monoida l functor
H /d47/d47 FunD(Y )(D(X),D(X)) M ✤ /d47/d47p2∗(p!
1(−)⊗ M)
Remark 6.1. More formally, the monoidal structure on D(X×Y X) can be deﬁned as follows. The
stack X×Y X can be identiﬁed with endomorphisms of X in the ∞-category of stacks over Y
with morphisms given by correspondences. The assignment of cate gories of D-modules extends to
a symmetric monoidal functor on this ∞-category (see Remark 4.1), hence induces an associative
algebra structure on D(X×Y X).
34
It is important to note that all of the maps involved in the monoidal st ructure ofH are obtained
by base change from either the diagonal map δ : X → X×X or the projection p : X → Y .
Moreover, the monoidal structure only uses pullbacks along maps o f the ﬁrst type and pushforwards
along maps of the second type. Thus if we assume δ is smooth and p is proper, the functors δ! and
p∗, and hence the monoidal product on H, will be quasi-proper. In addition, D(X) is semi-rigid
under tensor product, by Proposition 5.4.
Theorem 6.2. Suppose X is a stack with smooth diagonal, Y is a stack, and X→Y is a proper
representable map.
Then the Hecke category H =D(X×Y X) is semi-rigid (hence 2-dualizable).
Proof. To prove the theorem, let us ﬁrst establish a candidate for the dua l of a compact object.
First, recall that Verdier duality DX×Y X provides a self-duality
H =D(X×Y X)≃D (X×Y X)′ =H′
By deﬁnition, the compact objects of H andH′ form opposite categories to each other.
Next consider the swap involution
σ :X×Y X ∼ /d47/d47X×Y X σ (x1,y 12,x 2) = (x2,y −1
12,x 1)
where y−1
12 is the path y12 traced in the opposite direction. The induced equivalence on D-modules
intertwines the algebra structure and the opposite algebra struc ture
σ :H ∼ /d47/d47Hop.
Finally, introduce the composite of the swap involution, Verdier dualit y and shift
ι :H ∼ /d47/d47H′ ι(M) = DX×Y X (σ(M))[2 dimX]
We will show that any compact object M∈ His left and right dualizable, with both duals
identiﬁed with ι(M)∈H , thereby establishing that H is semi-rigid. Following the discussion of
Section 2.2.1, it suﬃces to establish for a compact object M∈H , and arbitrary objects L, N∈H ,
that there are functorial equivalences
HomH(L⋆ M, N)≃ HomH(L, N⋆ι (M)) Hom H(M⋆ L, N)≃ HomH(L,ι (M)⋆ N)
We will give a proof of the ﬁrst. The second is similar or follows by applyin g σ to the ﬁrst and
renaming objects.
Observe that it suﬃces to establish the equivalence for L, N∈H compact objects. For arbitrary
objects L, N∈H , it then follows by continuity by taking colimits ﬁrst in N then in L.
For L, M, N∈H compact objects, we will establish the equivalent identity
HomH(CX×Y X, DX×Y X (L⋆ M)⊗ N)≃ HomH(CX×Y X, DX×Y X (L)⊗ (N⋆ι (M)))
Sincep13 is a base change of p, it is proper and hence p13∗ commutes with Verdier duality. Since
p12×p23 is a base change of δ, it is smooth of relative dimension − dimX and hence (p12×p13)∗≃
(p12×p13)![2 dimX]. Hence we have the identity
DX×Y X (L⋆ M) ≃ DX×Y X (p13∗((p12×p13)!(L ⊠ M)))
≃ p13∗DX×Y X (p12×p13)!(L ⊠ M)
≃ p13∗(p12×p13)∗(DX×Y X (L) ⊠ DX×Y X (M))
≃ p13∗(p12×p13)!(DX×Y X (L) ⊠ DX×Y X (M))[2 dimX]
≃ DX×Y X (L)⋆ DX×Y X (M)[2 dimX]
Substituting this into the above sought after identity and renaming objects, we seek to establish
the following general identity
(4) Γ X×Y X ((L⋆ M)⊗ N)≃ Γ X×Y X (L⊗ (N⋆σ (M)))
35
Let us ﬁrst modestly reformulate how to calculate each side, in part icular the quantities obtained
before taking global sections. For the left hand side, consider the commutative diagram whose right
hand square is Cartesian
(X×Y X×Y X)
id×p13
/d15/d15
p12×p23×p13
/d115/d115❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
p13 /d47/d47X×Y X
∆
/d15/d15
(X×Y X)3 (X×Y X×Y X)× (X×Y X)p12×p23×p45
/d111/d111
p13×p45
/d47/d47 (X×Y X)2
By a composition identity in the triangle and base change in the right ha nd square, there is a
functorial equivalence
(L⋆ M)⊗ N≃p13∗(p12×p23×p13)!(L ⊠ M ⊠ N)
Similarly, for the right hand side, consider the commutative diagram w hose right hand square is
Cartesian
(X×Y X×Y X)
p13×id
/d15/d15
p13×σp23×p12
/d115/d115❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
p13 /d47/d47X×Y X
∆
/d15/d15
(X×Y X)3 (X×Y X)× (X×Y X×Y X)p12×σp45×p34
/d111/d111
p12×p35
/d47/d47 (X×Y X)2
By a composition identity in the triangle and base change in the right ha nd square, there is a
functorial equivalence
L⊗ (N⋆σ (M))≃p13∗(p13×σp23×p12)!(L ⊠ M ⊠ N)
Finally, observe that there is a natural commutative diagram
(X×Y X×Y X)
∼
r
/d42/d42❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯❯
p13×σp23×p12
/d15/d15
p13 /d47/d47X×Y X
(X×Y X)3 (X×Y X×Y X)p12×p23×p13
/d111/d111
p13
/d79/d79
where the diagonal map r is the rotational equivalence given by
r(x1,y 12,x 2,y 23,x 3) = (x1,y 12◦y23,x 3,y −1
23,x 2)
where the path y12◦y23 is the composition of the paths y12,y 23, and the path y−1
23 is the path y23
traced in the opposite direction.
Let us write π :X×YX→pt. We have seen that the two sides of the sought after equivalence ( 4)
can be realized by going around the edges of the above diagram
Γ X×Y X ((L⋆ M)⊗ N)≃π∗p13∗(p12×p23×p13)!(L ⊠ M ⊠ N)
Γ X×Y X (L⊗ (N⋆σ (M)))≃π∗p13∗(p13×σp23×p13)!(L ⊠ M ⊠ N)
Thus the rotational equivalence r intertwines them and we obtain the equivalence (4). □
Theorem 6.3. Suppose X,Y are as in Theorem 6.2. Then the Hecke category H =D(X×Y X)
carries a canonical Calabi-Yau structure.
Proof. Let us brieﬂy recall from [L2, Section 5.3.3] the realization of Hochs child homology and its
S1 symmetry from the point of view of topological chiral homology.
First, given a framed circle S, for example, the standard circle S1 = [0, 1]/∼ with its natural
induced orientation, let IS be the∞-category given by the nerve of the poset of framed embeddings
36
of ﬁnite disjoint unions of open intervals in S with partial order given by framed inclusions. Given
the E1-algebraH, introduce the natural functor
ψH :IS /d47/d47StC ψH(I) =H⊗π0(I)
whose structure on morphisms is given by the E1-structure on H. By deﬁnition, the topological
chiral homology of H overS is the colimit
∫
SH = colim ISψH
Observe that the above makes sense for families of framed circles, and so exhibits
∫
SH as the ﬁber
of an∞-local system over the moduli of framed circles BDiﬀ +(S1).
Recall as well that for the standard circle S1 = [0, 1]/∼, the realization of the bar resolution in
terms of subdivisions of the interval [0 , 1] provides a natural morphism which is an equivalence
Tr(H)≃|H⊗ H⊗HopC∗(H)| ∼ /d47/d47 colimIS1ψH =
∫
S1H
Now to endow H with a Calabi-Yau structure, let S→BDiﬀ +(S1) denote the universal framed
circle, and let VectC denote the constant∞-local system on BDiﬀ +(S1) with ﬁber Vect C. We must
construct a morphism of ∞-local systems
τ :
∫
SH /d47/d47 VectC
Moreover, for a given framed circle S and pair of disjoint open intervals I1
∐ I2⊂ S (hence any
framed circle with any pair of disjoint open intervals), the natural c omposite map
H⊗H≃H π0(I1
∐ I2) /d47/d47 ∫
SH
τS /d47/d47 VectC
must be the evaluation pairing of a self-duality of H∈ StC.
To achieve this, given an object I = ∐
iIi∈IS, letM(I) be the stack of maps ∐
iIi→Y with
lifts ∐
i∂Ii→X at boundary points. (Note we do not regard the boundary points o f the intervals
as embedded in S since they may coincide as, for example, for an interval of the form I =S\{s}
where s∈S is a single point.) Let D be a closed disk with ∂D =S, and M(D,I ) be the stack of
mapsD→Y with a lift over the complement S\ (∐
iIi)→X. Consider the natural correspondence
M(I) M(D,I )
p/d111/d111 q /d47/d47pt
Observe that ψH(I) =D(M(I)) and thanks to standard identities for D-modules, the functor
D(M(I)) /d47/d47 VectC M ✤ /d47/d47q∗p!M
provides a natural augmentation to the diagram given by ψH and hence a functor
τS :
∫
SH /d47/d47 VectC
Since the above makes sense for families of framed circles, it descen ds to the sought after morphism
of∞-local systems
τ : ∫
SH /d47/d47 VectC
Finally, consider the natural composite map
H⊗H≃H π0(I1
∐ I2) /d47/d47 ∫
SH
τS /d47/d47 VectC
Unwinding the above, we ﬁnd it is given by the functor
H⊗H≃D (X×Y X×X×Y X) /d47/d47 VectC M ✤ /d47/d47q∗p!M
where p :X×Y X→X×Y X×X×Y X is the diagonal and q :X×Y X→pt is the projection.
Observe that under the identiﬁcation of H∈ StC with its dual given by Verdier duality, the above
morphism is precisely the evaluation pairing. □
37
Remark 6.4. We will soon identify Tr(H)≃
∫
SH with a full subcategory of D-modules on the loop
spaceLY . Consider the natural correspondence of constant loops
LY Y e/d111/d111 π /d47/d47pt
Thanks to standard identities for D-modules, the trace τS :
∫
SH→ VectC will factor through the
functor
D(LY ) /d47/d47 VectC M ✤ /d47/d47π∗e!M
The above theorems thus allow us to apply the Cobordism Hypothesis [L3] to the Hecke category
to obtain an oriented two-dimensional topological ﬁeld theory.
Corollary 6.5. There is a unique symmetric monoidal functor Z : 2Bord → Alg(1)(StC) with
Z(pt) =H.
