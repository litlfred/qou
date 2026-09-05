---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-040-81-auxiliary-lemma
section_title: "Auxiliary Lemma"
section_number: 8.1
pages: 42-45
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
ization of the previous corollary which we explain below. The statemen t that we prove in this section allows
us to use smaller intermediate space for computation of the convolu tion.
Let us introduce notation Qk...m⊂Gn for subgroup with Lie algebra qk...m spanned by Eij, i≤j, i,j ∈
[1,n ] and by Eij,i>j ,i,j ∈ [k,m ]. Respectively, we denote by Π k...m
+ the projection map Lie( Gn)→ qk...m
and Π k...m
−− is deﬁned by Id = Π k...m
+ + Π k...m
−− . Similarly we deﬁne Π k...m
++ (X) = Π k...m
−− (X t)t, where t stands
for transpose. Let us also denote by Π k...m the projection gn→ gm−k+1 that extracts the block of the matrix
elements with entries ij,i,j ∈ [k,m ]. We use the same notation for the maps of the corresponding grou ps.
Let us introduce the space X ◦
3 (Gn,G k...m) = gn×Gn×Gk−m+1× nn× nk−m+1× nn. Let us also ﬁx an
embedding ik...m of this space inside X3:
ik...m(X,g 12,g 23,⃗Y ) = (X,g 12,i k...m(g23),Y 1,i k...m(Y2) + Π k...m
++ (Adg23 (Y3)),Y 3),
where ⃗Y = (Y1,Y 2,Y 3), ik...m :Gk−m+1→Gn and ik...m : nk−m+1→ nn are the natural embeddings.
Respectively we deﬁne maps
π◦
12 : X ◦
3 (Gn,G k...m)→ X2(Gn),
π◦
23 : X ◦
3 (Gn,G k...m)→ X2(Gm−k+1),
π◦
13 : X ◦
3 (Gn,G k...m)→ X2(Gn),
(8.26) π◦
12(X,g 12,g 23,Y 1,Y 2,Y 3) = (X,g 12,Y 1,i k...m(Y2) + Π k...m
++ (Adg23 (Y3)).
(8.27) π◦
23(X,g 12,g 23,Y 1,Y 2,Y 3) = (Π k...m(Ad−1
g12 (X)),g 23,Y 2, Π k...m(Y3)),
π◦
13(X,g 12,g 23,Y 1,Y 2,Y 3) = (X,g 12g23,Y 1,Y 3).
These maps are the restrictions of the corresponding maps from X3 on the embedded subvariety X ◦
3 (Gn,G k...m).
Similarly, we deﬁne X ◦
3 (Gk...m,G n) = gn×Gk...m×Gn× nn× nk−m+1× nn. Let us also ﬁx an embedding
ik...m of this space inside X3:
ik...m(X,g 12,g 23,⃗Y ) = (X,i k...m(g12),g 23,Y 1,i k...m(Y2) + Π k...m
++ (Ad−1
g12 (Y1)),Y 3),
⃗Y = (Y1,Y 2,Y 3). The maps π◦
ij are deﬁned analogously to the previous case: by the restriction fr om ambient
space.
The spaces X ◦
3 (Gn,G k...m) and X ◦
3 (Gk...m,G n) have unique B3
n equivariant structure that makes the
maps π◦
ij B3
n-equivariant.
42
Lemma 8.1. For any
F∈ MFsc
B2
m−k+1
(X2(Gm−k+1),W ),G∈ MFsc
B2n
(X2(Gn),W )
we have
G⋆ Indk...m(F ) = CE n(2)
m−k+1
π◦
13∗(π◦∗
12 (G)⊗π◦∗
23 (F ))T (2)
m−k+1,
Indk...m(F )⋆G = CE n(2)
m−k+1
π◦
13∗(π◦∗
12 (F )⊗π◦∗
23 (G))T (2)
m−k+1,
The key observation in the proof is an alternative description of the induction functor Ind k...m. The space
X •
2 (Qk...m) := gn×Qk...m× nm−k+1× nn can be mapped into X2(Gn) with the map:
jk...m(X,g,Y 1,Y 2) = (X,j k...m(g),i k...m(Y1) + Π k...m
++ (Adg(Y2)),Y 2)
where jk...m :Qk...m→Gn is the natural embedding.
There is also a natural projection map Π k...m : X •
2 (Qk...m)→ X ◦
2 (Gm−k+1) deﬁned by:
Π k...m(X,g,Y 1,Y 2) = (Π k...m(X), Π k...m(g), Π k...m(Y1), Π k...m(Y2)).
Both of these maps are B3
n-equivariant. In particular, we have a commuting diagram:
X •
2 (Qk...m) X ◦
2 (Pk,m) X ′′
2,n
X ′
2,k× X ′′
2,m−k+1× X ′
2,n−m X ′′
2,k× X ′′
2,m−k+1× X ′′
2,n−m
X ◦
2 (Gm−k+1)
i′
Π ′
1×Π k...m×Π ′
3
pk,m
ik,m
i‖ ×1×i‖
π2
where X ′
2,k := gk×Bk× bk× bk = X ◦
2 (Bk), X ′′
2,k := gk×Gk× bk× bk = X ◦
2 (Gk) and the dotted arrow
maps are:
i′(X,g,Y 1,Y 2) = (Π k...m
+ (X),j k...m(g),i k...m(Y1) + Π k...m
++ (Adg(Y2)),Y 2),
Π ′
i(X,g,Y 1,Y 2) = (p(i)
k,m(X),p (i)
k,m(g),p (i))
k,m(Adg(Y2)),p (i)
k,m(Y2)),
here p(1)
k,m, p(3)
k,m are the compositions of pk,m with the projections on k×k and (n−m)× (n−m) blocks.
Using the base change in our previous diagram we obtain
Indk...m =ik,m,∗◦p∗
k,m◦ (i‖× 1×i‖ )◦π∗
2 =ik,m,∗◦i′
∗◦ (Π ′
1× Π k...m× Π ′
3)∗◦π∗
2
=jk...m,∗◦ Π k...m,∗.
Proof of proposition 8.1. We prove the ﬁrst formula the second is analogous. We have the follo wing com-
muting diagram of the maps:
X ◦
3 (Gn,Q k...m) X ◦
3 X ◦
2
X ◦
2 × X •
2 (Qk...m) X ◦
2 × X ◦
2
X ◦
2 (Gn)× X ◦
2 (Gm−k+1)
ik...m
π◦
12×π◦
23 π◦
12×π◦
23
π◦
13
1×jk...m
1×Π k...m
where the dotted arrow map π◦
12×π◦
23 is given by
π◦
12(X,g 12,g 23,Y 1,Y 2,Y 3) = (X,g 12,Y 1,i k...m(Y2) + Π k...m
++ (Adg23 (Y3)),
43
π◦
23(X,g 12,g 23,Y 1,Y 2,Y 3) = (Ad −1
g12 (X),g 23,Y 2, Π k...m
− (Y3)).
Now we can use the base change formula to simplify G⋆ Indk...m(F ) :
CEn(2)
n
(π◦
13∗◦ (π◦
12×π◦
23)∗◦ (Id×jk...m)∗◦ (Id× Π k...m)∗(G ⊠F )))T (2)
n =
CEn(2)
n
(π◦
13∗◦ (ik...m)∗◦ (π◦
12×π◦
23)∗◦ (Id× Π k...m)∗(G ⊠F )))T (2)
n =
CEn(2)
n
(π◦
13∗◦ (π◦
12×π◦
23)∗(G ⊠F )))T (2)
n ,
where in the last equation we use π◦
13◦ik...m =π◦
13 and Id× Π k...m◦π◦
12×π◦
23 =π◦
12×π◦
23 where the maps in
the product π◦
12×π◦
23 : X ◦
3 (Gn,Q k...m)→ X ◦
2 (Gn)× X ◦
2 (Gm−k+1) are given by the formulas (8.26), (8.27).
Let us denote by C the matrix factorization π◦
13∗◦(π◦
12×π◦
23)∗(G ⊠F ) For last step we use Hochschild-Serre
spectral sequence to compute functor CE n(2)
n
:
CEn(2)
m−k+1
(CELie(J ′
k...m)(C))⇒ CEn(2)
n
(C)
where Jk...m is the kernel of the projection homomorphism Qk...m→ Gm−k+1 and J ′
k...m is its unipotent
part. Let us abbreviate the quotient Jk...m/J ′
k...m byJ/J ′. We have
(8.28) CE Lie(J ′
k...m)(C)J/J ′
=π◦
13∗(CELie(J ′
k...m)(π◦
12×π◦
23)∗(G ⊠F )).
On the other hand the formulas for the maps π◦
12 and π◦
23 imply that the diﬀerentials of the pull back
(π◦
12×π◦
23)∗(G ⊠F ) are invariant with respect to the action of J ′
k...m. Hence to complete the computation
of (8.28) we need to compute
H∗
Lie(J ′
k...m, C[X ◦
3 (Gn,Q k...m)])J/J ′
which is a tensor product of C[b×Gn× nm−k+1× nn] and H ∗
Lie(J ′
k...m, C[Qk...m])J/J ′
, and in proposition
below we show that CE J ′
k...m
(C[Qk...m])J ′/J = C[Gm−k+1]. Hence the statement follows since T (2)
n = (J/J ′)×
Tm−k+1 where Tm−k+1 is the maximal torus of Gm−k+1⊂Gn.
✷
Proposition 8.2. For any k,m , 1≤k <m≤n we have
CELie(J ′
k...m)(C[Qk...m]) = C[Gm−k+1]⊗ C[J/J ′].
Proof. We show slightly more general statement
CELie(J ′
k...m)(C[Qk′...m′]) = C[Qk−k′+1...m−k′+1⊂Gm−k+1]⊗ C[(J/J ′)],
where k≥k′, m′≤m.
We use induction by m−k and the Hochschild-Serre Spectral sequence ([40], sect 7.5). Sinc e we have
short exact sequence of groups
1→J ′
k+1,...,m−→J ′
k...n−→ Cm−k+1→ 1,
the spectra sequence tells us that
CECm−k+1 (CELie(J ′
k+1...m)(C[Qκ′...m′ ]))⇒ CEJk...m (C[Qk′...m′ ]).
By induction we have CE Lie(J ′
k+1...m)(C[Qk′...m′ ]) = C[Qk−k′+2...m−k′+1⊂Gm−k+2]. After relabeling matrix
indices our statement is equivalent to the computation of the followin g cohomology H∗
Lie(Cm−k+1, C[Qk−k′+2...m−k′+1]).
The ring of polynomial functions on Qk−k′+2...m−k′+1 is generated by the elements E∨
kl dual to the matrix
44
units Ekl of E. The generators ∂i of the commutative algebra Cm−k+1 act on the ring generators by the
formula:
∂iE∨
kl =δk1E∨
il.
We can apply invertible linear transformation to our system of diﬀere ntial operators to obtain new system
of generators:
˜∂k =
m−k+2∑
i=2
(−1)i+k∆ ik∂k,
where ∆ ik∈ C[Qk−k′+2...m−k′+1] is the determinant of ( m−k)× (m−k) obtained from E by removing
columns and rows containing 11 and ik entries. Then we have:
˜∂iE∨
kl =δk1δilE∨
11.
and by Poincare lemma we obtain
H∗
Lie(Cm−k+1, C[Qk−k′+2...m−k′+1]) = C[Qk−k′+2...m−k′+1]/(E∨
12,...,E ∨
1,m−k+2)
and the statement follows. ✷
