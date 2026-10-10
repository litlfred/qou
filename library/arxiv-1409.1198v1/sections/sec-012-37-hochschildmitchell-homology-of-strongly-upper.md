---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-012-37-hochschildmitchell-homology-of-strongly-upper
section_title: "Hochschild–Mitchell homology of strongly upper triangular categories"
section_number: 3.7
pages: 19-21
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
trace of a linear category is just the zeroth Hochschild–Mitchell ho mology. There is a class of linear
categories for which we can compute explicitly their Hochschild–Mitch ell homology. The results de-
veloped in this section will be useful in our study of the Hochschild–Mit chell homology of categoriﬁed
quantum groups.
Deﬁnition 3.5. A linear category C is said to be upper-triangular if there is no sequence
x0
f0
− →x1
f1
− →...
fn−1
− →xn
fn
− →x0 (n ≥ 1)
of nonzero morphisms in C unless x0 = x1 = · · · = xn. Alternatively, a linear category C is upper-
triangular if there is a partial order ≤ on Ob( C) such that C(x,y ) ⁄= 0 implies x ≤y.
For a linear category C, deﬁne a ring End( C) by
End(C) =
⨁
x∈Ob(C)
C(x,x ).
Lemma 3.6 ([8]). For an upper-triangular linear category C, we have
HH∗(C) ∼=
⨁
x∈Ob(C)
HH∗(C(x,x )) ∼= HH∗(End(C)).(3.1)
Remark 14. Note that the ring End(C) is not unital if Ob(C) is inﬁnite. The deﬁnitio n of the Hochschild
homology of a non-unital ring R is diﬀerent from the case of unital rin gs (see [41]), but it is well known
that the Hochschild homology of the direct sum of unital rings is isomo rphic to the direct sum of the
Hochschild homology of its direct summands.
20 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
Deﬁnition 3.7. A strongly upper-triangular linear category is an upper-triangular linear category C
such that for all x ∈ Ob(C), we have C(x,x ) ∼= Z.
Using that HH 0(/CI ) = /CI and for n> 0, HH n(/CI ) = 0, from the previous lemma we immediately get
the following.
Corollary 3.8 ([8]). For a strongly upper-triangular linear category C, we have
TrC = HH 0(C) ∼= End(C) ∼= Z Ob(C),
HHi(C) = 0 for i> 0.
Here Z Ob(C) denotes the free Z-module spanned by Ob( C).
Let C be an additive category, and let B ⊂ Ob(C) be a subset. Denote by C|B the full subcategory
of C with Ob( C|B) = B.
The set B is called a strongly upper-triangular basis of C if the following two conditions hold.
(1) The inclusion functor C|B → C induces equivalence of additive categories ( C|B)⊕ ≃ C .
(2) C|B is strongly upper-triangular.
Proposition 3.9 ([8]). Let C be an additive category with a strongly upper-triangular basis B. Then
we have
TrC = HH 0(C) ∼= ZB,
HHi(C) = 0 for i> 0.
Remark 15. For /CZ -linear categories it is natural to modify the Deﬁnition 3.7 to deﬁne a s trongly upper-
triangular /CZ -linear category by requiring that for all x ∈ Ob(C), we have C(x,x ) ∼=
/CZ . In that case,
Corollary 3.8 and Proposition 3.9 remain valid with /CI replaced by the ﬁeld /CZ .
An additive category is said to be Krull-Schmidt if any object has a unique decomposition into a
ﬁnite direct sum of objects having local endomorphism rings. That is to say, given an isomorphism
x1 ⊕x2 ⊕ · · · ⊕xr ∼=y1 ⊕y2 ⊕ · · · ⊕ys wherexi andyj are indecomposable, then r =s, and there exists
some permutation σ ∈Sr such that xσ(i) ≃yi.
Exercise 16. Show that any category C enriched in V ect
/CZ
, i.e. the hom spaces form vector spaces
and composition is a bilinear map, is Krull-Schmidt if and on ly if all idempotents split.
In a Krull-Schmidt category C the classes of indecomposables in the split Grothendieck group K0(C)
give rise to a distinguished basis. When C is a graded linear category, then the graded hom between a
pair of objects x, y ∈ Ob(C) is deﬁned as
HOMC(x,y ) :=
⨁
k∈ /CI
HomC(x,y ⟨k⟩).
When C is a graded /CZ -linear category, this graded hom gives rise to a sesquilinear inner pr oduct
⟨−, −⟩:K0(C) ×K0(C) → /CI ((q)) deﬁned by
⟨[x]∼=, [y]∼=⟩ := dim q HOMC(x,y ) =
∑
k∈ /CI
qk dim HomC(x,y ⟨k⟩).
One consequence of a graded linear category possessing a strong ly upper triangular basis B is that
the classes of B in the Grothendieck group satisfy the property that for any pair x,y ∈B, we have
⟨x,y ⟩ ∈δx,y +q /C6 [q],
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 21
in which case the basis resulting from B is said to be almost orthogonal.
Remarks for experts . Strongly upper triangular bases often arise in geometric constru ctions where
the categories of interest are categories of sheaves on certain v arieties. Usually one starts with a trian-
gulated category C and produces an abelian category A as the heart of a t-structure for C. Distinguished
basisB arise as the simple objects in the heart of the corresponding t-structure. If A is endowed with
a grading given by the cohomological Ext-grading from C, then the resulting basis of simple objects is
strongly upper triangular and their classes in the Grothendieck gro up are almost orthogonal.
For example, categories of perverse sheaves are the heart of a c ertain t-structure on the derived
category of sheaves [6]. In this way, simple perverse sheaves natu rally give rise to distinguished bases
in geometric representation theory. The Kazhdan-Lusztig basis o f a Hecke algebra associated to a Weyl
group W arise in this way [30]. Likewise, simple integrable representations and their tensor products
of quantum Kac-Moody algebra possess canonical bases [42, 43, 4 4, 45, 27, 28]. Outside of geometry,
there is a t-structure on the bounded derived category Db(Λ −mod) of a ﬁnite-dimensional /CZ -algebra Λ
in which the simple Λ-modules form a strongly upper triangular basis in t he heart of the t-structure [1].
