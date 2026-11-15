---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-081-121-boundedness-conditions-revisited
section_title: "Boundedness Conditions Revisited"
section_number: 12.1
pages: 221-223
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
We start by introducing some combinatorial deﬁnitions that will enable a precise
treatment of cohomological dimensions of objects and functors (in Subsection 12.4).
We also change our notation for boundedness conditions in derived categories
(Deﬁnition 12.1.6) and for the translation functor (Deﬁnition 12.1.7). These changes
will simplify and improve our discussion (while hopefully not creating confusion).
See Remark 12.1.8 for an explanation.
Integer intervals were introduced in Deﬁnition 11.1.10. Boundedness conditions
were introduced in Subsections 3.8 and 7.3. We need to reﬁne these notions.
Deﬁnition 12.1.1. Let S be an integer interval.
(1) We call S a bounded above integer interval if either S = [i0, i1] with i1 ∈Z,
or if S = ∅.
(2) We call S a bounded below integer interval if either S = [i0, i1] with i0 ∈Z,
or if S = ∅.
(3) We call S a bounded integer interval if it is both bounded above and bounded
below; i.e. either S = [i0, i1] with i0, i1 ∈Z, or S = ∅.
The next deﬁnition was already mentioned in passing in Subsection 3.8.
Deﬁnition 12.1.2. The boundedness conditions in Deﬁnition 12.1.1 have abbre-
viations, that we call boundedness indicators.
(1) The indicator “−” stands for “bounded above”.
(2) The indicator “+” stands for “bounded below”.
(3) The indicator “b” stands for “bounded”.
(4) The indicator “⟨empty⟩” (the empty symbol) stands for the empty condition
(no condition at all).
The symbol “⋆” is used to denote an unspeciﬁed boundedness indicator, i.e. it is
a placeholder for one of the boundedness indicators in Deﬁnition 12.1.2.
Deﬁnition 12.1.3. Let S be an integer interval.
(1) If S = [i0, i1], then its length is i1 −i0 ∈N ∪{∞}. If S = ∅, then then its
length is −∞.
(2) If S = [i0, i1], then the reversed integer interval is −S := [−i1, −i0]. If
S = ∅, then its reverse is also ∅.
(3) If S = [i0, i1], and if T = [j0, j1] is a second nonempty integer interval, then
their sum is S +T := [i0 +j0, i1 +j1]. If S = ∅, and it T is a second integer
interval, then the sum is S + T := ∅.
This material will be published by Cambridge University Press as Derived Categories by Amnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works. c⃝Amnon Yekutieli, 2019.
221
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Thus an integer interval S (whether empty or not) has ﬁnite length if and only
if it is bounded.
Deﬁnition 12.1.4. Let M = {M i}i∈Z be a graded object in an abelian category
M, i.e. M ∈G(M).
(1) We say that M is concentrated in an integer interval S if the set
{i ∈Z | M i̸ = 0} is contained in S.
(2) The concentration of M is the smallest integer interval con(M) in which M
is concentrated.
(3) We say that M is of boundedness type ⋆, for some boundedness indicator ⋆
if the integer interval con(M) satisﬁes the boundedness condition ⋆.
Observe that con(M) = ∅if and only if M = 0. Deﬁnition 12.1.4(3) agrees with
the boundedness conditions on a graded module M from Subsections 3.8 and 7.3.
In Deﬁnition 11.1.11 we introduced the notions inf(M) and sup(M) for a graded
object M. Using them we can describe the concentration con(M) = [i0, i1] when
M is nonzero: i0 = inf(M) and i1 = sup(M). The amplitude amp(M) is the length
of the interval con(M).
Recall that to a DG module M ∈C(A, M) we associate the graded object M ♮∈
G(M) that is gotten by forgetting the diﬀerential. The cohomology H(M) is another
object of G(M).
Deﬁnition 12.1.5. Let A be a DG ring, M an abelian category, and M ∈C(A, M).
(1) The concentration of M and the boundedness type of M are the same as in
Deﬁnition 12.1.4, when M is seen as an object of G(M).
(2) The cohomological concentration and the cohomological boundedness type of
M are the concentration and boundedness type, respectively, of the graded
object H(M) ∈G(M), in the sense of Deﬁnition 12.1.4.
The next deﬁnition is in conﬂict with Deﬁnitions 7.3.3 and 7.3.4; but we already
warned (in Remark 7.3.13) that this change will take place. See Remark 12.1.8 for
further discussion.
Deﬁnition 12.1.6. Let A be a DG ring, M an abelian category, and ⋆a bounded-
ness indicator. We denote by D⋆(A, M) the full subcategory of D(A, M) on the DG
modules M of cohomological boundedness type ⋆, as in Deﬁnition 12.1.5 above.
Thus, for example, a DG module M belongs to Db(A, M) if and only if con(H(M))
is a bounded integer interval. As explained in subsection 7.3, D⋆(A, M) is a full
triangulated subcategory of D(A, M).
The notations C⋆(A, M) and K⋆(A, M) remain the same, as in Deﬁnitions 3.8.20
and 7.3.1. Namely, these are the full subcategories of C(A, M) and K(A, M) respec-
tively on the DG modules M of boundedness type ⋆.
Deﬁnition 12.1.7. Let A be a DG ring and M an abelian category. For a DG
module M ∈C(A, M) and an integer i, we write M[i] := Ti(M), the i-th translation
of M, as in Deﬁnition 4.1.4.
This notation applies also to the homotopy category K(A, M), the derived cate-
gory D(A, M), and every other T-additive category.
The notation M[i] makes it diﬃcult to use the little t operator, and to talk about
translation isomorphisms, but hopefully we won’t require them anymore.
Remark 12.1.8. We should say a few explanatory words on the change in Deﬁni-
tion 12.1.6, that conﬂicts with earlier deﬁnitions.
Recall that in Deﬁnitions 7.3.3 and 7.3.4 we made a distinction between
(12.1.9)
D⋆(A, M) = K⋆(A, M)S⋆(A,M),
222
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
the localization of K⋆(A, M) with respect to the quasi-isomorphisms in it, and
D(A, M)⋆, the full subcategory of D(A, M) on the complexes of cohomological
boundedness type ⋆. This distinction was necessary in the early part of the book,
when we were studying foundations and resolutions. Now that the foundations are
behind us, we no longer have a need for the subcategory D⋆(−) in the sense of
formula (12.1.9), i.e. the deﬁnition based on boundedness type.
Still, one might ask: Why make the notational switch from D(−)⋆to D⋆(−), for
the deﬁnition based on cohomological boundedness type? There are two reasons
for that. The ﬁrst is typographic: the notation D(−)⋆becomes cumbersome when
coupled with other indicators, such as Df(−)⋆or (D(−)⋆)op. After Deﬁnition 12.1.6
we can refer to these categories by the more elegant expressions D⋆
f (−) or D⋆(−)op,
respectively.
Second, the expression D(−)⋆is a novelty, and nobody else uses it, whereas the
notation D⋆(−) is common. According to Proposition 7.3.12, in most situations
the two distinct meanings of D⋆(−), the old one and the new one, refer to nested
subcategories of D(−) whose inclusion is an equivalence. Furthermore, in a few
recent texts on derived categories (such as [144, Deﬁnition tag=05RU] and [172,
Deﬁnition 1.11]) we ﬁnd the same usage of the expression D⋆(−) as in Deﬁnition
