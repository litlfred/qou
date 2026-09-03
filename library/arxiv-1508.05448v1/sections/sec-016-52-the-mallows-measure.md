---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-016-52-the-mallows-measure
section_title: "The Mallows Measure"
section_number: 5.2
pages: 104-105
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
Given a permutation of n numbersπ∈Sn, we deﬁne the inversion number Inv(π) to
be
Inv(π) = #{(i,j ) : i<j andπ(i)>π (j)}
96
For eachq∈ (0, 1), the Mallows measure [Mallows, 1957] is deﬁned by
µn,q(π) = qInv(π)
Zn,q
where Zn,q is a normalization constant given by
Zn,q =
∑
π∈Sn
qInv(π) =
n∏
k=1
1−qk
1−q = [n]q!
where [n]q! is as stated in the previous chapter. The measure is related to the Iwahori-
Hecke algebra as shown by Diaconis and Ram [Diaconis et al. , 2000]. Note that
for q = 1, the Mallows measure is just the uniform measure on Sn, with all n!
permutations equally likely.
