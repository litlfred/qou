---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-069-121-boundedness-conditions-revisited
section_title: "Boundedness Conditions Revisited"
section_number: 12.1
pages: 221-223
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
We start by introducing some combinatorial deﬁnitions that will enable a precise
treatment of cohomological dimensions of objects and functors (in Subsection 12.4).
We also change our notation for boundedness conditions in derived categories
(Deﬁnition12.1.6)andforthetranslationfunctor(Deﬁnition12.1.7). Thesechanges
will simplify and improve our discussion (while hopefully not creating confusion).
See Remark 12.1.8 for an explanation.
Integer intervalswere introduced in Deﬁnition 11.1.10.Boundedness conditions
were introduced in Subsections 3.8 and 7.3. We need to reﬁne these notions.
Deﬁnition 12.1.1.Let S be an integer interval.
(1) We callS a bounded above integer intervalif eitherS = [i0,i 1] withi1∈Z,
or ifS =∅.
(2) We callS a bounded below integer intervalif eitherS = [i0,i 1] withi0∈Z,
or ifS =∅.
(3) Wecall S abounded integer intervalifitisbothboundedaboveandbounded
below; i.e. eitherS = [i0,i 1] with i0,i 1∈Z, orS =∅.
The next deﬁnition was already mentioned in passing in Subsection 3.8.
Deﬁnition 12.1.2.The boundedness conditions in Deﬁnition 12.1.1 have abbre-
viations, that we callboundedness indicators.
(1) The indicator “−” stands for “bounded above”.
(2) The indicator “+” stands for “bounded below”.
(3) The indicator “b” stands for “bounded”.
(4) Theindicator“⟨empty⟩”(theemptysymbol)standsfortheemptycondition
(no condition at all).
The symbol “⋆” is used to denote an unspeciﬁed boundedness indicator, i.e. it is
a placeholder for one of the boundedness indicators in Deﬁnition 12.1.2.
Deﬁnition 12.1.3.Let S be an integer interval.
(1) If S = [i0,i 1], then itslength is i1−i0∈N∪{∞}. IfS =∅, then then its
length is−∞.
(2) If S = [i0,i 1], then the reversed integer intervalis−S := [−i1,−i0]. If
S =∅, then its reverse is also∅.
(3) IfS = [i0,i 1], and ifT = [j0,j 1] is a second nonempty integer interval, then
their sum isS +T := [i0 +j0,i 1 +j1]. IfS =∅, and itT is a second integer
interval, then the sum isS +T :=∅.
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
221
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Thus an integer intervalS (whether empty or not) has ﬁnite length if and only
if it is bounded.
Deﬁnition 12.1.4.Let M ={Mi}i∈Z be a graded object in an abelian category
M, i.e.M∈G(M).
(1) We say that M is concentrated in an integer interval S if the set
{i∈Z|Mi⁄= 0}is contained inS.
(2) The concentrationofM is the smallest integer intervalcon(M) in whichM
is concentrated.
(3) We say thatM is ofboundedness type⋆, for some boundedness indicator⋆
if the integer intervalcon(M) satisﬁes the boundedness condition⋆.
Observe thatcon(M) =∅ if and only ifM = 0. Deﬁnition 12.1.4(3) agrees with
the boundedness conditions on a graded moduleM from Subsections 3.8 and 7.3.
In Deﬁnition 11.1.11 we introduced the notionsinf(M) and sup(M) for a graded
object M. Using them we can describe the concentrationcon(M) = [i0,i 1] when
M is nonzero:i0 = inf(M) andi1 = sup(M). The amplitudeamp(M) is the length
of the intervalcon(M).
Recall that to a DG moduleM∈C(A, M) we associate the graded objectM♮∈
G(M) that is gotten by forgetting the diﬀerential. The cohomologyH(M) is another
object of G(M).
Deﬁnition 12.1.5.LetA be a DG ring,M an abelian category, andM∈C(A, M).
(1) The concentrationofM and theboundedness typeofM are the same as in
Deﬁnition 12.1.4, whenM is seen as an object ofG(M).
(2) The cohomological concentrationand thecohomological boundedness typeof
M are the concentration and boundedness type, respectively, of the graded
object H(M)∈G(M), in the sense of Deﬁnition 12.1.4.
The next deﬁnition is in conﬂict with Deﬁnitions 7.3.3 and 7.3.4; but we already
warned (in Remark 7.3.13) that this change will take place. See Remark 12.1.8 for
further discussion.
Deﬁnition 12.1.6.LetA be a DG ring,M an abelian category, and⋆a bounded-
ness indicator. We denote byD⋆(A, M) the full subcategory ofD(A, M) on the DG
modules M of cohomological boundedness type⋆, as in Deﬁnition 12.1.5 above.
Thus, forexample, aDGmodule M belongsto Db(A, M)ifandonlyif con(H(M))
is a bounded integer interval. As explained in subsection 7.3,D⋆(A, M) is a full
triangulated subcategory ofD(A, M).
The notations C⋆(A, M) and K⋆(A, M) remain the same, as in Deﬁnitions 3.8.20
and 7.3.1. Namely, these are the full subcategories ofC(A, M) and K(A, M) respec-
tively on the DG modulesM of boundedness type⋆.
Deﬁnition 12.1.7.Let A be a DG ring andM an abelian category. For a DG
moduleM∈C(A, M) and an integeri, we writeM[i] := Ti(M), thei-th translation
of M, as in Deﬁnition 4.1.4.
This notation applies also to the homotopy categoryK(A, M), the derived cate-
gory D(A, M), and every other T-additive category.
The notationM[i] makes it diﬃcult to use the little t operator, and to talk about
translation isomorphisms, but hopefully we won’t require them anymore.
Remark 12.1.8. We should say a few explanatory words on the change in Deﬁni-
tion 12.1.6, that conﬂicts with earlier deﬁnitions.
Recall that in Deﬁnitions 7.3.3 and 7.3.4 we made a distinction between
(12.1.9) D⋆(A, M) = K⋆(A, M)S⋆(A,M),
222
Derived Categories | Amnon Yekutieli | 14 Apr 2019
the localization of K⋆(A, M) with respect to the quasi-isomorphisms in it, and
D(A, M)⋆, the full subcategory of D(A, M) on the complexes of cohomological
boundedness type⋆. This distinction was necessary in the early part of the book,
when we were studying foundations and resolutions. Now that the foundations are
behind us, we no longer have a need for the subcategoryD⋆(−) in the sense of
formula (12.1.9), i.e. the deﬁnition based on boundedness type.
Still, one might ask: Why make the notational switch fromD(−)⋆to D⋆(−), for
the deﬁnition based on cohomological boundedness type? There are two reasons
for that. The ﬁrst is typographic: the notationD(−)⋆becomes cumbersome when
coupled with other indicators, such asDf(−)⋆or (D(−)⋆)op. After Deﬁnition 12.1.6
we can refer to these categories by the more elegant expressionsD⋆
f (−) or D⋆(−)op,
respectively.
Second, the expressionD(−)⋆is a novelty, and nobody else uses it, whereas the
notation D⋆(−) is common. According to Proposition 7.3.12, in most situations
the two distinct meanings ofD⋆(−), the old one and the new one, refer to nested
subcategories of D(−) whose inclusion is an equivalence. Furthermore, in a few
recent texts on derived categories (such as [144, Deﬁnition tag=05RU] and [172,
Deﬁnition 1.11]) we ﬁnd the same usage of the expressionD⋆(−) as in Deﬁnition
12.1.6.
