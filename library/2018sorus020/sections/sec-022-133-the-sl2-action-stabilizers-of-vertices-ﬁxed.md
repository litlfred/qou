---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-022-133-the-sl2-action-stabilizers-of-vertices-ﬁxed
section_title: "The SL2 action : stabilizers of vertices, ﬁxed points and"
section_number: 1.3.3
pages: 31-32
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
translation length
There is a natural isometric and transitive action ofGL(V ) on T, induced by the
action of GL(V ) on V.
Deﬁnition 1.3.1.The action of a subgroupG⊂ GL(V ) onT will be saidtrivial if
a vertex is ﬁxed by the whole group.
Lemma 1.3.2. For anyg∈ GL2(K), [L]∈ T, ﬁx a basis{e,f} of L∈ [L], and
n,m∈ Z such that{tne,tmf} is a basis ofg·L. Thenv(det(g)) =n +m.
Proof. In this basis,L≃O 2
v, andg can be written as the matrixA (tn 0
0 tm )B with
A,B∈ GL2(Ov). The result follows.
Now we restrict to theSL(V ) action. We say that an elementg∈ SL(V ) stabilizes
a vertex [L]∈T if for any representativeL we haveg·L =xL for somex∈ K∗.
Lemma 1.3.3.An elementg∈ SL(V ) stabilizes a vertex[L] iﬀ for any representa-
tive g·L =L.
30
Proof. Assume thatg·L =xL, then by Lemma 1.3.2,v(det(g)) = 2v(x) = 0 hence
x∈O∗ and xL =L.
Furthermore, asSL2(Ov) is the stabilizer of the standard latticeO2
v, we deduce the
proposition.
Proposition 1.3.4. The stabilizer inSL2(K) of any vertex of the treeT is a GL2-
conjugate of SL2(Ov).
Remark 1.3.5.Since for anyg∈ SL(V ),v(det(g)) = 0, we know that the distance
d([L],g· [L]) = |n−m| is even, in particularSL(V ) acts without inversion on T,
that is it can not ﬁx an edge and exchange its end points.
Deﬁnition 1.3.6.Given g∈ SL(V ), we deﬁne thetranslation lenght of g to be
equal tol(g) = min
[L]∈T
d([L],g· [L]).
There are two ways forg∈ SL(V ) acting on the tree :
