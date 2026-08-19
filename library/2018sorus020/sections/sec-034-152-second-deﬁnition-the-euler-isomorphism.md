---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-034-152-second-deﬁnition-the-euler-isomorphism
section_title: "Second deﬁnition : the Euler isomorphism"
section_number: 1.5.2
pages: 44-45
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
Recall that the determinant of an-dimensional vector spaceV is det(V ) = ΛnV. One
deﬁne thedeterminant of a complexdet(C∗) =⨂
i det(Ci)⊗(−1)i
. The cohomology of
this complex is naturally graded by the degree, and we have the following theorem.
Theorem 1.5.1.There is a natural isomorphism
Eu : det(C∗)
∼
− →det(H∗(C∗))
Proof. Again, we write the two exact sequences
0→Zi→Ci→Bi+1→ 0
0→Bi→Zi→Hi→ 0
Then the proof reduces to the particular case of a short exact sequence :
Lemma 1.5.2.For an exact sequence of vector spaces
0→A→B→C→ 0
one has an isomorphism
det(A)⊗ det(C)≃ det(B)
given, for any choice of basis{a1,...am} of A,{c1,...,c n} of C and of a section
C→B,ci↦→ ¯ci, by
(a1∧...∧am)⊗ (c1∧...∧cn)↦→a1∧...∧am∧ ¯c1∧...∧ ¯cn
43
Deﬁnition 1.5.3.Given a complex C∗, and a system of basis{ci} of the Ci’s,
ci ={ci
1,...,c i
ni}, then⋀ci =ci
1∧...∧ci
ni is a basis ofdet(Ci), and then we denote
byc =⨂
i(⋀ci)⊗(−1)i
the induced basis ofdet(C∗).
Then the torsion of the based complex is deﬁned by
tor(C∗,{ci}) = Eu(c)∈ det(H∗(C∗))
Remark 1.5.4.The two deﬁnitions coincide in the following sense :
tor(C∗,{ci},{hi}) = tor(Ci,{ci})⊗i (∧hi)⊗(−1)i
