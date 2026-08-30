---
doc_id: arxiv-math-0411647v2
doc_title: "Asymptotics of characters of symmetric groups, genus expansion and free probability"
section_id: sec-002-12-the-main-technical-problem-convolution-in-sq
section_title: "The main technical problem: convolution in Sq"
section_number: 1.2
pages: 2-4
source_pdf: 0411647v2.pdf
source_sha256: d79f96b416cb28da
doc_brief: "Asymptotics of characters of symmetric groups, genus expansion and free probability — The convolution of indicators of two conjugacy classes on the symmetric group Sq is usually a complicated linear"
---
central functions f, g ∈ C(Sq ) has a very simple structure if we write them
as linear combinations of characters: if
f(π ) =
∑
λ⊢q 
aλ
χ λ(e)χ λ(π )
q! , g (π ) =
∑
λ⊢q 
bλ
χ λ(e)χ λ(π )
q!
ASYMPTOTICS OF CHARACTERS AND GENUS EXPANSION 3
then
(fg)(π ) =
∑
λ⊢q 
aλbλ
χ λ (e)χ λ(π )
q! ,
where the product fg denotes a product of elements of the group algebra,
i.e. the convolution of functions. However, in many cases we cannot afford
the luxury of using the character expansion, for example in t he case when
we actually try to ﬁnd the asymptotics of characters. For thi s reason we
should ﬁnd some other families of central functions on Sq for which the
convolution would have a relatively simple form.
In Section 2.1.10 we shall deﬁne such a family Σ k1 ,...,k m ∈ C(Sq ) which
has a particularly simple structure: Σ k1 ,...,k m is (up to a normalizing fac-
tor) an indicator of the conjugacy class of permutations wit h a prescribed
cycle decomposition k1, . . . , k m . This great simplicity has very appealing
consequences: it will be very easy to evaluate functions Σ on permutations
and also it will be very simple to write any central function o n Sq as a
linear combination of functions Σ (operations which are somewhat cumber-
some for characters). This object was introduced and studied by Ivanov and
Kerov [IK99].
A question arises how to express a productΣ k1 ,...,k m · Σ l1 ,...,l n ∈ C(Sq ) as
a linear combination of some other normalized conjugacy cla ss indicators
Σ . This problem is very closely related to calculation of the, so called,
connection coefﬁcients [GJ96, GJL01, Gou90, Gou94, GS98]. The latter
problem asks for the number of solutions of the equationπ 1π 2π 3 = e where
π 1, π 2, π 3 ∈ Sq must have a prescribed cycle structure. The formulas for
the connection coefﬁcients are available in many concrete c ases, however
they are not satisfactory for the purpose of this article.
1.2.1. The ﬁrst main result: calculus of partitions and genus expansion. It
turns out that the solution to the above problem can be obtained by consider-
ing some more general objects. In Section 3.1.1 we shall deﬁne normalized
conjugacy class indicators Σ π which are indexed no longer by sequences
of integers but by partitions of ﬁnite ordered sets. We also e quip partitions
with an explicit multiplicative structure in such a way thatΣ becomes a ho-
momorphism. For this reason we can in fact forget in applications about the
symmetric group Sq and perform all calculations in the partition language.
In applications we are interested in the asymptotic behavior of the contri-
bution of various conjugacy classes whenq → ∞. It turns out that the order
of such a contribution of Σ π can be read directly from the genus of a two-
dimensional surface associated to the partitionπ; in this way our description
is very similar to the genus expansion for random matrices [Z vo97]. Even
more striking is that the degree q of the symmetric group Sq does not enter
into the multiplicative structure of partitions and theref ore the calculus of
4 PIOTR ´SNIADY
partitions is able to provide statements about symmetric gr oups which do
not depend on q. Another great advantage is that the moments of the Jucys–
Murphy element (which are closely related to the moments of the transition
measure) can be easily expressed within our calculus. All th ese features
make the calculus of partition and its genus expansion a perfect tool for the
study of symmetric groups.
Unfortunately, one of our ultimate goals—formulas which re late char-
acters and the moments of the transition measure—turn out to be quite in-
volved and we need also some other tools to solve this problem. As we shall
see in the following, these tools are provided by the free probability theory.
