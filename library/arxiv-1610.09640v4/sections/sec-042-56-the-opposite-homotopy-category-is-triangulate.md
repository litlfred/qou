---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-042-56-the-opposite-homotopy-category-is-triangulate
section_title: "The Opposite Homotopy Category is Triangulated"
section_number: 5.6
pages: 110-113
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
a canonical triangulated structure on the opposite homotopy categoryK(A, M)op.
This gives us a way to talk about contravariant triangulated functors whose source
is a full subcategory of K(A, M). Our solution is precise, but it is not totally
satisfactory – see Remark 5.6.12.
We already gave a thorough treatment of contravariant DG functors in Subsec-
tion 3.9. In the previous subsection we explained precisely how to pass from DG
functors to triangulated functors. In this subsection we treat the contravariant
case.
As before,A is a central DGK-ring, and M is aK-linear abelian category. The
DG category of DGA-modules in M is C(A, M). In Subsection 3.9 we introduced
the ﬂipped DG categoryC(Aop, Mop). In Theorem 3.9.16 we had a canonical iso-
morphism of DG categories
(5.6.1) Flip : C(A, M)op ≃
− →C(Aop, Mop).
Deﬁnition 5.6.2.The ﬂipped categoryof K(A, M) is the triangulated category
K(A, M)ﬂip := K(Aop, Mop) = Ho
(
C(Aop, Mop)
{
.
See Theorem 5.4.3. Its translation functor is denoted byTﬂip.
110
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Since Ho
(
C(A, M)op{
= K(A, M)op, the isomorphism (5.6.1) induces aK-linear
isomorphism of categories
(5.6.3) Flip := Ho(Flip) : K(A, M)op ≃
− →K(A, M)ﬂip.
Deﬁnition 5.6.4.The category K(A, M)op is given the triangulated category
structure induced from the ﬂipped categoryK(A, M)ﬂip under the isomorphism
(5.6.3). The translation functor ofK(A, M)op is denoted byTop.
Thus
(5.6.5) Top = Flip
−1
◦Tﬂip◦Flip.
The distinguished triangles ofK(A, M)op are the images underFlip
−1
of the dis-
tinguished triangles ofK(A, M)ﬂip. And tautologically,
(5.6.6) (Flip, id) : K(A, M)op→K(A, M)ﬂip
is an isomorphism of triangulated categories.
Deﬁnition5.6.7.Let K⊆K(A, M)beafulladditivesubcategory, andassumethat
Kop is a triangulated subcategory ofK(A, M)op. Then we giveKop the triangulated
structure induced fromK(A, M)op.
To say this a bit diﬀerently, the condition onK in the deﬁnition is thatKﬂip :=
Flip(Kop)⊆K(A, M)ﬂip is a triangulated subcategory. The triangulated structure
we put onKop is such that(Flip, id) : (Kop, Top)→(Kﬂip, Tﬂip) is an isomorphism
of triangulated categories.
Remark 5.6.8. It could happen (though we have no example of it) thatK⊆
K(A, M) is a full triangulated subcategory, yetKop⊆K(A, M)op is not a triangu-
lated subcategory; or vice versa. More on this issue in Remark 5.6.12.
The remark above notwithstanding, in many important cases, such as in Propo-
sitions 7.6.1 and 7.6.2, bothK⊆K(A, M) and Kop⊆K(A, M)op are triangulated.
Deﬁnition 5.6.9.Let L be a triangulated category, and let K ⊆K(A, M) be
a full subcategory such that Kop ⊆K(A, M)op is triangulated. A contravariant
triangulated functor from K to L is, by deﬁnition, a triangulated functor(F,τ) :
Kop→L in the sense of Deﬁnition 5.2.1, whereKop has the triangulated structure
from Deﬁnition 5.6.7.
Theorem 5.6.10. Let A and B be DG rings, and letM and N be abelian cate-
gories. Let C⊆C(A, M) be a full subcategory, and letF : Cop→C(B, N) be a DG
functor. Consider the homotopy categoryK := Ho(C)⊆Ho
(
C(A, M)
{
= K(A, M)
and the induced additive functor ¯F := Ho(F ) : Kop →K(B, N). Suppose that
Kop ⊆K(A, M)op is triangulated. Then there is a canonical translation isomor-
phism ¯τsuch that
( ¯F, ¯τ) : Kop→K(B, N)
is a triangulated functor.
Proof. Deﬁne
Cﬂip := Flip(Cop)⊆C(Aop, Mop) = C(A, M)ﬂip.
This is a DG category, andFlip : Cop→Cﬂip is an isomorphism of DG categories.
Also Ho(Cﬂip) = Kﬂip. There is a DG functor
F ﬂip :=F◦Flip−1 : Cﬂip→C(B, N),
and it induces an additive functor
¯F ﬂip := Ho(F ﬂip) : Kﬂip→K(B, N).
111
Derived Categories | Amnon Yekutieli | 14 Apr 2019
By Theorem 5.5.1 there is a translation isomorphism¯τﬂip such that
( ¯F ﬂip, ¯τﬂip) : Kﬂip→K(B, N)
is a triangulated functor. Using formula (5.6.5) we obtain these equalities and
isomorphisms:
¯F◦Top = ¯F◦Flip
−1
◦Tﬂip◦Flip = ¯F ﬂip◦Tﬂip◦Flip
¯τﬂip
− −− →TK(B,N)◦¯F ﬂip◦Flip = TK(B,N)◦¯F.
We deﬁne¯τto be the composed isomorphism. By construction the pair( ¯F, ¯τ) is a
triangulated functor. □
Exercise 5.6.11. Let C⊆C(A, M) be a full subcategory s.t. K := Ho( C) is a
triangulated subcategory ofK(A, M), and letG : C→C(B, N)op be a DG functor.
Write ¯G := Ho(G). Show that there is a translation isomorphism ¯νs.t. ( ¯G, ¯ν) :
K→K(B, N)op is a triangulated functor. (Hint: study the proof of the theorem
above.)
Remark 5.6.12. Let K be a triangulated category. There is a way to introduce
a triangulated structure on the opposite categoryKop. The translation functor is
Top := Op◦T−1◦Op−1. The distinguished triangles are deﬁned to be
N
Op(β)
−−−−→M
Op(α)
−−−−→L
Op(−T−1(γ))
−−−−−−−−−→Top(N),
where L
α
− →M
β
− →N
γ
− →T(L) goes over all distinguished triangles in K. See
[76, Remark 10.1.10(ii)]. This approach has an advantage: it allows to talk about
contravariant triangulated functorsK→L without any restriction on the category
K. This is in contrast to our quite restricted Deﬁnition 5.6.9. The disadvantage of
the approach presented in this paragraph is that there is no easy way to tie it with
the DG theory (as opposed to our Theorems 5.5.1 and 5.6.10).
It would have been very pleasing if in the caseK = K(A, M), the triangulated
structure on K(A, M)op presented in the paragraph above would coincide with the
triangulated structure from Deﬁnition 5.6.4. However, our calculations seem to
indicate otherwise.
Since in this book we are only interested in triangulated functors that are of DG
origin (covariant, as in Theorem 5.5.1, or contravariant, as in Theorem 5.6.10), we
decided to adopt Deﬁnition 5.6.9. It is a reliable, yet somewhat awkward approach.
For instance, it requires us to perform particular calculations for the composition
of contravariant triangulated functors, as in Lemma 13.1.16.
112
Derived Categories | Amnon Yekutieli | 14 Apr 2019
