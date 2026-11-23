---
doc_id: arxiv-math-0408078v2
doc_title: "A basis for the full Homfly skein of the annulus"
section_id: sec-006-some-basic-elements-in-the-annulus
section_title: "Some basic elements in the annulus"
section_number: null
pages: 7-9
source_pdf: 0408078v2.pdf
source_sha256: b632eb5e9b7a1753
toc_source: outline
doc_brief: "A basis for the full Homfly skein of the annulus — A basis, denoted {Qλ,µ}, for the full Homﬂy skein of the annulus C was introduced in [18], where λ and µ are partitions of integers n and p into k"
---
Some basic elements in the annulus
In Hn there is a known set of idempotent elements, Eλ, one for each partition
λ of n. These elements were originally given a purely algebraic description by
Gyoja [3], and were subsequently given a skein picture based on the Young
diagram for λ by the second author and Aiston [16].
The closure of Eλ
gives the element Qλ ∈C+, making up the basis elements used in [16], and
indirectly those used in [10]. Our construction makes use only of the sequence
of elements {hn} ∈C+ which arise from the single row Young diagrams, and
the corresponding elements {h∗
n} ∈C−.
The two simplest idempotents in Hn correspond to the single row and
single column Young diagrams, as described in [13]. In the interpretation of
the subalgebra C+ of C as the algebra of symmetric functions in inﬁnitely
many variables the closures of these idempotents correspond to the complete
symmetric function and the elementary symmetric function of degree n re-
spectively.
We give brief details of the deﬁnition and properties of these
idempotents and their closure.
Let wπ be the positive permutation braid ([2]) corresponding to π ∈Sn.
Deﬁne two quasi-idempotents an, bn ∈Hn by
an =
X
π∈Sn
sl(π)wπ
and
bn =
X
π∈Sn
(−s)−l(π)wπ,
7
where l(π) = wr(wπ), the writhe of the braid wπ.
Write gn = 1+sσn−1 +s2σn−1σn−2 +. . .+sn−1σn−1σn−2 . . . σ1, where {σi}
are the usual elementary braid generators of the braid group Bn.
We have gn+1 = 1 + sσngn, and also the immediate skein relation
gn+1
=
gn
+ sn
(1)
for tangles on n + 1 strings.
There is an algebra homomorphism ϕs : Hn →Λ deﬁned on the elemen-
tary braids σi by ϕs(σi) = s.
The following two lemmas are readily established, as in [13]:
Lemma 1.1 an = an−1gn.
Lemma 1.2 For any g ∈Hn we have ang = ϕs(g)an = gan.
The element an then satisﬁes
a2
n = ϕs(an)an = ϕs(an−1)ϕs(gn)an.
Now since ϕs(gn) = 1 + s2 + . . . + s2n−2 = sn−1[n] with [k] = sk−s−k
s−s−1 , we
have the immediate corollary:
Corollary 1.3 We can write
sn−1[n]hn = hn−1gn,
where hn = an/ϕs(an) is the true idempotent.
The element hn constructed above is the idempotent which corresponds
to the single row Young diagram with n cells. The single column idempotent,
denoted en, is constructed in an analogous way from bn. It can be obtained
from hn by using −s−1 in place of s.
With a slight abuse of the notation we shall write hn, en ∈C for the
closures ˆhn, ˆen of these idempotents as elements of C.
The skein C+ is spanned by the monomials in {hm : m ≥0}. The skein
C−is thus spanned by monomials in {h∗
l : l ≥0}. The whole skein C is then
spanned by monomials in {h∗
l , hm : l, m ≥0}.
8
