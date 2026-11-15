---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-023-151-first-deﬁnition
section_title: "First deﬁnition"
section_number: 1.5.1
pages: 43-44
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
First deﬁnition
Given a ﬁnite complex C∗of k-vector spaces
C0
d0
−→C1
d1
−→...
dn−1
−−−→Cn
ﬁx {ci}i=0...n and {hi}i=0...n families of basis of the Ci’s and the Hi’s, one can deﬁne
the torsion of the based complex tor(C∗, {ci}, {hi}) to be the alternating product
of the determinants of the base change induced by this choices. More precisely, we
have the exact sequences
0 →Zi →Ci →Bi+1 →0
0 →Bi →Zi →Hi →0
42
that deﬁne Bi, Zi and Hi. Pick a system of basis {bi} of the Bi’s, ﬁrst one obtains
a basis of Zi for any i, given by a section Hi →Zi, and then a section Bi+1 →Ci
provides a basis of Ci : bi ⊔¯hi ⊔¯bi+1, where the bars denote the image by the chosen
sections. Now compare this new basis with ci, and take the determinant of the matrix
which exchange those basis, denoted by [bi ⊔¯hi ⊔¯bi+1 : ci]. One can show that the
alternating product of those determinants does not depend of the lifts and of the
system {bi} and we deﬁne
tor(C∗, {ci}, {hi}) =
Y
i
[bi ⊔¯hi ⊔¯bi+1 : ci](−1)i ∈k∗/{±1}
