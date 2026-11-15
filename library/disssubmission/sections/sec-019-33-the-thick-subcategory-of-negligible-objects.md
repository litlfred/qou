---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-019-33-the-thick-subcategory-of-negligible-objects
section_title: "The thick subcategory of negligible objects"
section_number: 3.3
pages: 55-59
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
toc_source: inferred
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 52 sections: Front matter; Introduction; Some commonly used notations"
---
47
LEMMA 3.4. For all K,M ∈D and χ ∈Π(X) one has the following
natural isomorphisms.
(a) Adjoint duality:
HomD(1,K∨∗∗M) ∼= HomD(K,M) ∼= HomD(K ∗! M∨,1).
(b) Character twists:
(Kχ)∨∼= (K∨)χ,
(K ∗! M)χ ∼= Kχ ∗! Mχ
and
(K ∗∗M)χ ∼= Kχ ∗∗Mχ.
(c) Verdier duality:
D(K ∗! M) ∼= D(K)∗∗D(M),
D(K ∗∗M) ∼= D(K)∗! D(M).
(d) K¨unneth formulae:
H•
c (X,K)⊗Λ H•
c (X,M)
∼
−→
H•
c (X,K ∗! M),
H•(X,K ∗∗M)
∼
−→
H•(X,K)⊗Λ H•(X,M).
Proof. Part (a) follows from adjunction as in [41, p. 533]. In (b) the
ﬁrst identity comes from RHom(Lχ,ΛX) = Lχ−1 and (−id)∗(Lχ−1) = Lχ,
and the other two follow as in proposition 2.1. Part (c) follows from the
compatibility of Verdier duality with exterior tensor products. Part (d) is
the K¨unneth isomorphism [7, exp. XVII.5.4] resp. its Verdier dual.
□
3.3. The thick subcategory of negligible objects
In this and in the next section we always assume that for the abelian
variety A = X/T the vanishing assumption GV(A) of section 3.1 holds. We
have seen in theorem 3.1 that GV(X) then holds as well. Let S(X) ⊂P(X)
be the full subcategory of all perverse sheaves of Euler characteristic zero,
and T(X) ⊂D(X) the full subcategory of all sheaf complexes K whose
perverse cohomology sheaves pHn(K) lie in S(X) for all degrees n ∈Z. For
brevity we put
P = P(X),
D = D(X),
S = S(X)
and
T = T(X).
The following explains why we only use characters of the tame fundamental
group — we want the Euler characteristic χ(K) = ∑i∈Z dimΛ(Hi(X,K)) of
any complex K ∈D to be invariant under character twists.
LEMMA 3.5. Let K ∈D. Then χ(K) = χ(Kϕ) for all ϕ ∈Π(X), hence
the following three conditions are equivalent:
(a) The complex K lies in the full subcategory T.
(b) We have H•(X,Kϕ) = 0 for generic ϕ ∈Π(X).
(c) We have H•
c (X,Kϕ) = 0 for generic ϕ ∈Π(X).
48
Chapter 3 – Perverse sheaves on semiabelian varieties
Proof. To prove the twist invariance of the Euler characteristic, we can
by d´evissage assume that the complex K is a constructible sheaf placed in
a single cohomology degree. Then [59, cor. 2.9] says that if j : X ,→¯X
denotes a smooth compactiﬁcation, then j!(K) and j!(Kϕ) have the same
Euler characteristic (the assumptions of the corollary are satisﬁed since χ is
a tame character, see sect. 2.6 of loc. cit.). Since for the Euler characteristic
it makes no difference whether we use compactly supported or ordinary
hypercohomology [70], it follows that χ(K) = χ(Kϕ). The equivalence of
the three conditions (a) – (c) then follows via corollary 3.3.
□
Recall that a full subcategory of an abelian category is said to be a Serre
subcategory if it is stable under the formation of arbitrary subquotients and
extensions. More generally, a full triangulated subcategory of a triangulated
category is called a thick subcategory if it has the following property: For
any morphism f : K →L which factors over an object of the subcategory
and has its cone in the subcategory, the objects K and L must both belong
to the subcategory as well.
COROLLARY 3.6. The subcategory S ⊂P is Serre, and T ⊂D is thick.
Proof. Let 0 −→P −→Q −→R −→0 be a short exact sequence in the
abelian category P. Theorem 3.1 says that for a generic character χ ∈Π(X)
the hypercohomology of the perverse sheaves Pχ, Qχ and Rχ is concentrated
in degree zero so that the long exact sequence in hypercohomology reduces
to a short exact sequence
0 −→H0(X,Pχ) −→H0(X,Qχ) −→H0(X,Rχ) −→0.
Therefore lemma 3.5 shows that Q lies in S if and only if both P and R are
in S. Hence S ⊂P is a Serre subcategory, and then the subcategory T ⊂D
is thick by [41, prop. 3.6.1(i)].
□
In particular, localizing the abelian category P at the class of morphisms
whose kernel and cokernel lie in the Serre subcategory S we can form the
abelian quotient category P = P/S in the sense of [42, chap. III]. Note that
the category P has the same objects as P and that for any objects P1,P2
the elements of HomP(P1,P2) can be represented by equivalence classes of
diagrams in P of the form
Q
f1
zuuuuuu
f2
$I
I
I
I
I
I
P1
P2
where the kernel and cokernel of the morphism f1 lie in S. In the same
way, localizing the triangulated category D at the class of morphisms whose
cone lies in the thick subcategory T we can form the triangulated quotient
category D = D/T as described in [82, sect. 2.1].
3.3. The thick subcategory of negligible objects
49
It has been shown in [41, prop. 3.6.1] that these quotient constructions
are compatible with each other in the sense that the perverse t-structure
on D induces on the triangulated quotient category D a t-structure whose
core is naturally equivalent to the abelian quotient category P. So we have
a commutative diagram
P  
/

D

P  
/ D
where the rows are embeddings of full subcategories and the columns are
the quotient functors. It turns out that convolution behaves well with respect
to the above quotient constructions in the following sense.
LEMMA 3.7. Let K,M ∈D.
(a) The cone of the morphism K ∗! M −→K ∗∗M lies in T.
(b) If K or M lies in T, then K ∗! M and K ∗∗M are also in T.
(c) If both K and M are perverse, then pHn(K ∗! M) and pHn(K ∗∗M)
lie in the Serre subcategory S for all n̸ = 0.
Proof. (a) Let C be the cone of the morphism K∗!M →K∗∗M. We want
to show that H•(X,Cχ) = 0 for a generic character χ ∈Π(X). Lemma 3.4
implies that for any character χ the twist Cχ is isomorphic to the cone of
the twisted morphism
Kχ ∗! Mχ −→Kχ ∗∗Mχ,
so it sufﬁces to check that the induced morphism
H•(X,Kχ ∗! Mχ) −→H•(X,Kχ ∗∗Mχ)
is an isomorphism for generic χ. By corollary 3.3 we can replace the left
hand side by the compactly supported hypercohomology of Kχ ∗! Mχ. So
we must see that the forget support map
fKχ⊠Lχ :
H•
c (X ×k X,Kχ ⊠Mχ) −→H•(X ×k X,Kχ ⊠Mχ)
is an isomorphism for generic χ. For this we go back to the deﬁnition
of compactly supported hypercohomology. For simplicity of notation we
will suppress the character twist in what follows, replacing K and L by
their twists Kχ and Lχ. Let j : X ,→X be a compactiﬁcation, and consider
the following diagram where all the horizontal arrows are forget support
50
Chapter 3 – Perverse sheaves on semiabelian varieties
morphisms (the vertical arrows will be discussed below).
H•
c (X ×k X,K ⊠L)
fK⊠L
/ H•(X ×k X,K ⊠L)
H•(X ×k X,(j, j)!(K ⊠L))
/
(1)
H•(X ×k X,R(j, j)∗(K ⊠L))
H•(X ×k X, j!(K)⊠j!(L))
/
O
(2)
H•(X ×k X,Rj∗(K)⊠R j∗(L))
O
H•(X, j!(K))⊗H•(X, j!(L))
/
O
(3)
H•(X,Rj∗(K))⊗H•(X,R j∗(L))
O
H•
c (X,K)⊗H•
c (X,L)
fK⊗fL
/
(4)
H•(X,K)⊗H•(X,L)
The horizontal arrow fK ⊗fL on the bottom line is the tensor product of
the forget support morphisms for K and L, hence by corollary 3.3 it is an
isomorphism for generic χ. On the other hand, the horizontal arrow fK⊠L
on the top line is the forget support morphism we are interested in. So we
will be ﬁnished if we can show that the above diagram commutes and that
all the vertical arrows (to be deﬁned yet) are isomorphisms.
The squares (1) and (4) are commutative by the very deﬁnition of fK⊠L
and fK ⊗fL. The vertical arrows in (3) are the K¨unneth isomorphisms for
the proper morphism X →Spec(k), and the commutativity of this square
follows from the fact that the K¨unneth morphisms are natural in the involved
complexes. Finally, the square (2) is induced by the square
(j, j)!(K ⊠L)
/ R(j, j)∗(K ⊠L)
j!(K)⊠j!(L)
/
ad−1
!
O
R j∗(K)⊠Rj∗(L)
ad∗
O
where the morphisms
ad! :
(j, j)!(K ⊠L) −→j!(K)⊠j!(L)
ad∗:
Rj∗(K)⊠Rj∗(L) −→R(j, j)∗(K ⊠L)
are the natural morphisms which correspond via adjunction to the identity
morphism of
K ⊠L = (j, j)!(j!(K)⊠j!(L)) = (j, j)∗(Rj∗(K)⊠R j∗(L)).
Note that ad! is an isomorphism and that over U = X ×k X ,→X ×k X all
the morphisms in the above diagram restrict to the identity. In particular,
