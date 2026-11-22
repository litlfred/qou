---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-024-152-second-deﬁnition-the-euler-isomorphism
section_title: "Second deﬁnition : the Euler isomorphism"
section_number: 1.5.2
pages: 44-45
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
Second deﬁnition : the Euler isomorphism
Recall that the determinant of a n-dimensional vector space V is det(V ) = ΛnV . One
deﬁne the determinant of a complex det(C∗) = N
i det(Ci)⊗(−1)i. The cohomology of
this complex is naturally graded by the degree, and we have the following theorem.
Theorem 1.5.1. There is a natural isomorphism
Eu : det(C∗)
∼−→det(H∗(C∗))
Proof. Again, we write the two exact sequences
0 →Zi →Ci →Bi+1 →0
0 →Bi →Zi →Hi →0
Then the proof reduces to the particular case of a short exact sequence :
Lemma 1.5.2. For an exact sequence of vector spaces
0 →A →B →C →0
one has an isomorphism
det(A) ⊗det(C) ≃det(B)
given, for any choice of basis {a1, ...am} of A, {c1, ..., cn} of C and of a section
C →B, ci 7→¯ci, by
(a1 ∧... ∧am) ⊗(c1 ∧... ∧cn) 7→a1 ∧... ∧am ∧¯c1 ∧... ∧¯cn
43
Deﬁnition 1.5.3. Given a complex C∗, and a system of basis {ci} of the Ci’s,
ci = {ci
1, ..., ci
ni}, then V ci = ci
1 ∧... ∧ci
ni is a basis of det(Ci), and then we denote
by c = N
i(V ci)⊗(−1)i the induced basis of det(C∗).
Then the torsion of the based complex is deﬁned by
tor(C∗, {ci}) = Eu(c) ∈det(H∗(C∗))
Remark 1.5.4. The two deﬁnitions coincide in the following sense :
tor(C∗, {ci}, {hi}) = tor(Ci, {ci}) ⊗i (∧hi)⊗(−1)i
