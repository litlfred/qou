---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-009-13-kodaira-nakano-type-vanishing-theorems-13
section_title: "Kodaira-Nakano-type vanishing theorems 13"
section_number: 1.3
pages: 21-22
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
For a given line bundleL∈Pic0(X), the set of all charactersχ with the
above property is a torsor under the groupH0(X,Ω1X). Indeed, this follows
from the truncated exact cohomology sequence
0−→H0(X,Ω1
X)−→H1(X,C∗)−→Pic0(X)−→0
attached to the exact sequence 0→ C∗X→ O∗X→ Ω1
X,cl→ 0 where Ω1
X,cl
denotes the sheaf of closed holomorphic 1-forms. On the other hand, from
the point of view of Hodge theory it is better to restrict our attention to
unitary charactersχ : π1(X,0)→U(1) ={z∈ C∗|| z| = 1}, which has the
extra beneﬁt of making the passage from coherent to constructible sheaves
unique: Comparing the exponential sequences 0→ZX→RX→U(1)X→0
and 0→ ZX→ OX→ O∗X→0 one sees that the morphism
H1(X,U(1))
∼=−→Pic0(X)
is an isomorphism, so for every line bundleL∈ Pic0(X) there is a unique
unitary characterχ with L∼= Lχ⊗C OX. Concerning the applicability of
theorem 3.1 in this unitary context, we remark that the intersection of any
thin subset of Π(X) with the set of unitary characters is mapped via the
above isomorphism to a thin subset ofPic0(X).
In what follows, forn∈ N0 we putXn ={x∈ X| dim(f−1(x)) =n} and
consider the number
w(Y) = min{2d−(dim(Xn) +2n)| n∈ N0, Xn⁄= ∅}.
Notice thatw(Y)≤ d (indeed, for somen the preimagef−1(Xn) is dense
in Y so thatd = dim(f−1(Xn)) =dim(Xn) +n, hence 2d−(dim(Xn) +2n)
is equal to 2d−(d +n) = d−n≤ d). Furthermore, by base change one
checks that for any local systemsE of complex vector spaces onY the
direct image
R f∗E[2d−w(Y)] is semi-perverse,
because forx∈ Xn(C) the ﬁbreF = f−1(x)⊆Y satisﬁesHi(F,E|F) =0 for
all i > 2n. This being said, theorem 1.1 implies the following version of the
vanishing theorem given in [47, th. 2].
THEOREM 1.4. Let E be a unitary local system on Y . Then for mostL
in Pic0(Y) we have
Hp(Y,Ωq
Y(E⊗C L )) = 0 if p +q < w(Y).
Proof. The morphismf∗ : Pic0(X)−→Pic0(Y) is an isomorphism by
construction of the Albanese variety [48, p. 553], so every coherent line
bundle L∈ Pic0(Y) arises as the pull-back of someM∈ Pic0(X). As
explained above, there is a unitary characterχ such that
M∼= OX⊗CLχ.
