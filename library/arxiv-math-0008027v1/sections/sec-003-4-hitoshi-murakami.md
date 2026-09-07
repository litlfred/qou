---
doc_id: arxiv-math-0008027v1
doc_title: "KASHAEV’S INVARIANT AND THE VOLUME OF A"
section_id: sec-003-4-hitoshi-murakami
section_title: "HITOSHI MURAKAMI"
section_number: 4
pages: 4-4
source_pdf: 0008027v1.pdf
source_sha256: 8bce0b8a1bca372e
doc_brief: "KASHAEV’S INVARIANT AND THE VOLUME OF A — I follow Y."
---
From the lemma below we have
⟨41⟩N = N 2
N − 1∑
j=0
(−1)[j− 1]q− j− ([j− 1]+1)([j− 1]− 2j)/ 2
(q)[− j](q− 1)[− j]
∑
k∈ [0,j − 1]
q− kj
(q)[j− k− 1](q− 1)[k]
= N 2
N − 1∑
j=0
1
(q)[− j](q− 1)[− j]
=
N − 1∑
j=0
(q)[N − 1+j](q− 1)[N − 1+j]
=
N − 1∑
j=0
(q)j (q− 1)j.
Note that the ﬁnal formula coincides with Kashaev’s [2, (2.2)].
The following lemma is a key to reduce the summations of the Kashaev’s invari-
ant.
Lemma 2.3 (Yokota’s version of [3, Lemma 3.2]) . Let 0 ≤ k, l, m ≤ N − 1 be in-
tegers. Then
∑
k∈ [l,m ]
q− (m− l+1)k
(q)[m− k](q− 1)[k− l]
= (−1)[m− l]q([m− l]+1)([m− l]− 2m)/ 2.
Proof. We use the following equality [3, Lemma 3.2].
N − 1− α∑
i=0
q(β − α )i/ 2
(q)i(q− 1)N − 1− α − i
= (−1)N − 1− α q− N (N − 1)/ 2− β (α +1)/ 2
N
(q)α (q)N − 1− α +[(α − β )/ 2]
(q)[(α − β )/ 2]
.
To prove the lemma, we put β = −α . Then we have
N − 1− α∑
i=0
q− αi
(q)i(q− 1)N − α − i− 1
= (−1)N − 1− α q− N (N − 1)/ 2+α (α +1)/ 2.
Putting i = [m − k] and N − α − 1 = [ m − l], the conclusion follows.
