---
doc_id: arxiv-1608.03227v4
doc_title: "January 30, 2018"
section_id: sec-034-65-proof-of-proposition-62
section_title: "Proof of proposition 6.2"
section_number: 6.5
pages: 35-38
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
doc_brief: "January 30, 2018 — For each braid β ∈ Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗ × C∗ - equivariant sheaves on the non-commutative nested Hilbert scheme Hilb f ree 1,n ."
---
ik∗◦p∗
k(F )⋆i k∗◦p∗
k(G) = ik∗◦p∗
k(F ⋆G),
whereF =F1 ⊠F2,G =G1 ⊠G2∈ MFsc
B2
k
(X ◦
2 (Gk),W )× MFsc
B2
n−k
(X ◦
2 (Gn−k),W ). The LHS of the later
formula is the result of the application of the functor CE n(2)
n
combined with extraction of T (2) invariant part
to the matrix factorization C such that:
(6.20) C♯ = ˜F⊗ [Π k
−−(X), Π k
++(Y1− Adg12 (Y2))]⊗ Kπ∗
12(δkW2)(Π k
−−(g12))⊗
˜G⊗ [Π k
−−(Ad−1
g12 (X)), Π k
++(Y2− Adg23 (Y3))]⊗ Kπ◦∗
23 (δkW2)(Π k
−−(g23)).
with ˜F =jk∗
n◦ρ∗
k(F ′) and ˜G =jk∗
n◦ρ∗
k(G′) in conventions of subsection 6.2: jk∗
n (F ′) = p∗
k(F ),jk∗
n (G′) = p∗
k(G).
Let us ﬁx coordinates X,g 23,g 13,Y 1,Y 2,Y 3 on X ◦
3 (Gn). We use the factor [Π k
−−(X), Π k
++(Y1−Adg12 (Y2))]
to exclude the variables Π k
−−(X) from the other factors. Since Π k
−−(X) is B2
n-equivariant, the exclusion
process uses only the row transformations of the ﬁrst kind and we do not need to worry about the admissibility
conditions. The elimination process changes the factor in (6.20) in th e following manner:
˜F→ ˜F1 := ˜F| Π k
−−(X)=0, ˜G→ ˜F1 := ˜F| Π k
−−(Ad−1
g12 (X))=0
[Π k
−−(X), Π k
++(Y1− Adg12 (Y2))]→ [Π k
−−(X),R 1],
[Π k
−−(Ad−1
g12 (X)), Π k
++(Y2− Adg23 (Y3))]→ [0, Π k
++(Y2− Adg23 (Y3))],
Kπ◦∗
12 (δkW2)(Π k
−−(g12))→ Kπ∗
12(δkW2)(Π k
−−(g12))|Π k
−−(X)=0,
Kπ◦∗
12 (δkW2)(Π k
−−(g23))→ Kπ◦∗
23 (δkW2)(Π k
−−(g23))|Π k
−−(X)=0
We denote the resulting equivariant matrix factorization asC1. The non-equivariant limit C♯
1 is the product of
the above listed terms. Moreover, since the only term in C♯
1 that depends on Π k
−−(X) is the Koszul matrix
factorization [Π k
−−(X),R 1], we conclude that R1 is the derivative of the potential π◦∗
13 (W ) by variables
Π k
−−(X) which equals Π k
++(Y1− Adg13 (Y3)).
Next let us observe that using the row transformations of the ﬁrs t kind we can show that the following
equivalence of the matrix factorization
Kπ◦,∗
12 (δkW2)(Π k
−−(g12))⊗ Kπ◦∗
23 (δkW2)(Π k
−−(g23))|Π k
−−(X)=0
= K π◦∗
13 (δkW2)(Π k
−−(g13))⊗ K0(Π k
−−(g23))|Π k
−−(X)=0
Finally, we use the Koszul complex K 0(Π k
−−(g23))|Π k
−−(X)=0 to exclude the variables Π k
−−(g23) from the
product; for that we use the ﬁrst type row transformations so w e do not need to worry about the admissibility.
The ﬁnal result of the sequence of row transformations is the equ ivariant matrix factorizations C2 such that
its non-equivariant limit C♯
2 is the product the following factors:
˜F2 := ˜F| Π k
−−(X)=0,Π k
−−(g23)=0, ˜G2 := ˜F| Π k
−−(Ad−1
g12 (X))=0,Π k
−−(g23)=0
[Π k
−−(X),Y 1− Adg13 (Y3)], [0, Π k
++(Y2− Adg23 (Y3))],
Kπ◦∗
13 (δkW2)(Π k
−−(g13))⊗ K0(Π k
−−(g23))|Π k
−−(X)=0.
Since the potential π◦∗
13 (δkW2) does not depend on Π k
−−(X) the last product is actually just
Kπ◦∗
13 (δkW2)(Π k
−−(g13))⊗ K0(Π k
−−(g23)).
35
Let us introduce auxiliary space Zcon(Gn) := gn×Pk×Gn× nn× (nk× nn−k)× nn andZcon(Pk) :=
pn×Pk×Pk× nn× (nk× nn−k)× nn. The variety Zcon(Gn) is a subspace of X ◦
3 deﬁned by equations
Π k
++(Y2− Adg23 (Y3)) = 0, Π k
−−(g23) = 0, thus we can deﬁne the map π◦
13 :Zcon(Gn)→ X ◦
2 (Gn) by the
restriction.
We can contract diﬀerentials in complexes [0 , Π k
++(Y2− Adg23 (Y3))], Π k
−−(g23) to obtain homotopy equiv-
alence of matrix factorizations over π◦,∗
13 (C[X ◦
2 (Gn)]):
C2∼C3,
where C3∈ MFsc
B2n
(Zcon(Gn),π ◦
13(W )). Moreover, since we only used admissible row transformations th e
matrix factorization C3 has a structure of quasi-Koszul matrix factorization:
C3 = ( ˜M⊗ Λ •V,d + +D +d−,∂ +∂−),
where V is space dual to span of equations Π k
−−(X), Π k
−−(g13), d+ is the corresponding Koszul diﬀerential
d+ : ˜M⊗ Λ •V → ˜M⊗ Λ •−1V, and d− : ˜M⊗ Λ •V → ˜M⊗ Λ •+1V the completing diﬀerentials and ∂− =∑
i>j∂−
ij ,
∂ij : Λ i(n2
n)⊗ ˜M⊗ Λ •V → Λ j(n2
n)⊗ ˜M⊗ Λ ≥•V, ( ˜M,D,∂ )∈ ModB3
n
per(Z(Gn)).
The locus insideZcon(Gn) deﬁned by the equations Π k
−−(X) = 0, Π k
−−(g13) = 0 is isomorphic to Zcon(Pn),
by construction
( ˜M,D,∂ )|Π k
−−(X)=0,Π k
−−(g13)=0 =p∗
k(π◦∗
12 (F )⊗π◦∗
23 (G)),
where pk :Zcon(Pk)→ X ◦
3 (Gk)× X ◦
3 (Gn−k) is the natural projection. Hence we can use uniqueness
lemma 3.6 to imply that we have an isomorphism of B3
n equivariant matrix factorizations
C3 =i∗(p∗
k(π◦∗
12 (F )⊗π◦∗
23 (G)),
where i is mapZcon(Pk)→Z con(Gn).
The Lie algebra n(2) does not act on variables Π k
−−(X) and Π k
−−(g13) hence we have
CEn(2) (C3) = i∗(CEn(2) (p∗
k(π◦∗
12 (F )⊗π◦∗
23 (G)))).
Let us denote by Ik the kernel of the projection homomorphism Pk → Bk×Bn−k and let I ′
k be its
unipotent part. Hence we have the short exact sequence of Lie alg ebras:
0→ Lie(I ′
k)→ nn→ nk⊕ nn−k→ 0
and we can use Hochschild-Serre spectral sequence to compute f unctor CE n(2)
n
:
CEn(2)
k ⊕n(2)
n−k
(CELie(I ′
k)(C3))⇒ CEn(2)
n
(C1).
Since the Lie algebra n(2) only acts on on the second copy of Pk in the productZcon(Pn) = pn×Pk×Pk×
nn× (nk× nn−k)× nn and the diﬀerentials in p∗
k(π◦∗
12 (F )⊗π◦∗
23 (G)) are also I ′
k invariant, the computation of
CELie(I ′
k)(p∗
k(π◦∗
12 (F )⊗π◦∗
23 (G))) reduces to the computation of
H∗
Lie(Lie(I ′
k), C[Zcon(Pk)]) = C[nn×Pk× nn× (nk× nn−k)× nn]⊗ H∗
Lie(Lie(I ′
k), C[Pk]).
The last computation is equivalent to the following
36
Proposition 6.3.
CELie(I ′
k)(C[Pk]) = C[Gk×Gn−k],
whereGk×Gn−k is the subgroup of Pk deﬁned by the equation Π k
++(g) = 0 .
Proof. The group Ik acts on Pk by right multiplication. The Lie algebra Lie( I ′
k) is generated by the elements
Eij, i∈ [1,n ],j∈ [k + 1,n ] and direct computation shows that it is a commutative algebra.
Let us denote by E∨
kl the generators of the algebra C[Pk]: E∨
kl(X) = Xkl. Let us denote by ∂ij the
diﬀerential operator corresponding to the action Eij∈ Lie(I ′
k). The action of these generators of Lie( I ′
k) is
given by:
∂ij =
∑
k+1≤l≤n
E∨
jl
∂
∂E ∨
il
.
Let us observe that vector of diﬀerential operators ∂i• is related to the vector of diﬀerential operators
∂
∂E ∨
i•
,•∈ [k + 1,n ] by the matrix M = (E∨
lm)l,m∈[k+1,n] and this matrix is invertible. Thus the condition
∂ij(f ) = 0 for all i,j is equivalent to the condition ∂f
∂E ∨
ij
= 0 for all i,j ∈ [k + 1,n ].
Since the operator ∂
∂E ∨
ij
is surjective on C[Pk] the statement of the proposition follows. ✷
The proposition implies that CE Lie(I ′
k)(C[Zcon(Pk)]) = C[Zcon(Gk×Gn)] where Zcon(Gk×Gn) := pn×
Pk×Gk×Gn−k× nn× (nk× nn−k)× nn. Thus the proposition implies that
CEn(2) (C3) = i′
∗(CEnk⊕nn−k ((p′
k)∗(π◦∗
12 (F )⊗π◦∗
23 (G)))),
where i′ :Zcon(Gk×Gn−k)→Z con(Gn) and p′
k :Zcon(Gk×Gn−k)→ X ◦
3 (Gk)× X ◦
3 (Gn−k).
Hence after extracting the torus invariant part of the last expre ssion we obtain the formula from the
statement of the proposition:
π◦
13∗(CEn(2) (C3))T (2)
=i∗
k◦p∗
k(F ¯⋆G).
6.6. T ransitivity of induction. In this section we prove the following
Proposition 6.4. The following functors:
MFk× MFm−k× MFn−m→ MFn,
MFr := MF sc
Gr×B2r
(X2(Gr),W ) are isomorphic
indk◦ Id× indm−k = ind m◦ indk× Id.
Before we start the proof let us ﬁx some notations. We denote by Pk,m a subgroup of Gn with the Lie
algebra generated by Eij, i≤j and Ei,i+1, i⁄=k,m . Given an element g∈Pk,m we denote by g′ its k×k
block, by g′′ its (m−k)× (m−k) block and by g′′′ its (n−m)× (n−m) block. We also use pk,m for
Lie(Pk,m)
We have natural homomorphisms: ik,m :Pk,m→Gn andpk,m :Pk,m→Gk×Gm−k×Gn−m. Respectively,
we deﬁne X ◦
2 (Pk,m) := pk,m×Pk,m× n2
n and using previously deﬁned maps we construct maps pk,m :
X ◦
2 (Pk,m)→ X ◦
2 (Gk)× X ◦
2 (Gm−k)× X ◦
2 (Gn−m) and ik,m : X ◦
2 (Pk,m)→ X ◦
2 (Gn). Using these maps we
can deﬁne the functor
indk,m : MF ◦
k× MF◦
m−k× MF◦
n−m→ MF◦
n,
indk,m :=ik,m,∗◦p∗
k,m,
37
MF◦
r := MF sc
B2r
(X ◦
2 (Gr),W ).
Also there are also natural maps pk :Pk,m→Gk×Pm−k,pm :Pk,m→Pk×Gn−m such that pm−k◦pk =
pk,m and pk◦pm =pk,m.
Proof of proposition 6.4. We will show that
indk◦ Id× indm−k = ind k,m = ind m◦ indk× Id
Let us indicate how we imply the ﬁrst equality, the second equality has a similar proof. Let us notice that
LHS is the composition of several functors: ik∗◦p∗
k◦ (Id×im−k)∗◦ (Id×pm−k)∗. We have the following
commuting diagram:
pk,m×Pk,m× n2
n X ◦
2 (Pk)
X ◦
2 (Gk)× X ◦
2 (Pm−k) X ◦
2 (Gk)× X ◦
2 (Gn−k)
im−k
pk pk
1×im−k
where the dotted arrow maps are: pk(X,g,Y 1,Y 2) = (pk(X),p k(g),Y 1,Y 2) where pk :Pk,m→Gk×Pm−k is
the natural homomorphism and im−k =im−k×im−k× Id× Id.
Finally let us observe that pm−k◦pk =pk,m and ik◦im−k =ik,m. Now we use the base change to show:
indk◦ Id× indm−k =ik∗◦p∗
k◦ (Id×im−k)∗◦ (Id×pm−k)∗
=ik∗◦im−k∗◦p∗
k◦p∗
m−k = (ik◦im−k)∗◦ (pm−k◦pk)∗ = ind k,m.
✷
Since the functor Φ n provides an embedding of categories we get an immediate corollary:
Corollary 6.5. The following functors from
MFsc
B2
k
(X 2(Gk),W )× MFsc
B2
m−k
(X 2(Gm−k),W )× MFsc
B2
n−m
(X 2(Gn−m),W )
to MFsc
B2
n
(X 2(Gn),W ) are isomorphic
indk◦ Id× indm−k = indm◦ indk× Id.
