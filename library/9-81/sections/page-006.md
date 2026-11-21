---
doc_id: 9-81
doc_title: "Singular Euclidean Structures on a Simplicial Complex with Weighted Edges"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: 9_81.pdf
source_sha256: 12a83d647032306e
toc_source: undetermined
doc_brief: "Kamei, Singular Euclidean structures on a simplicial complex with weighted edges (2003) — extends Rivin's geometric structures on a 2-simplicial complex to weighted-edge assignments."
---
The next lemma follows immediately.
Lemma 3.4.
Let , , 	 be the angles of a triangle t ¼ ABC respectively. Then Dðt; AÞ ¼ log sin   log sin 	.
Deﬁnition.
Let vi ¼ ti1 \ ti \ tiþ1. The value Hðc; A Þ ¼ Pk1
i¼1 Dðti; viÞ is called the holonomy of c.
Lemma 3.5.
There exists a singular Euclidean structure on S if and only if the holonomies of all dual cycles of S are
equal to 0.
Proof.
First we assume that the holonomies of all dual cycles of S are equal to 0. Take some base 2-face t1. For any
other 2-face t, take a chain of 2-faces a ¼ ft1; . . . ; tk ¼ tg such that ti and tiþ1 share the edge ei. This ﬁxes the size of t,
and the vanishings of the holonomies assure that this size is independent of the choice of the chain a. Conversely, if
there is a singular Euclidean structure of S, the ratios of the lengths of edges are independent of the chain connecting
them, and hence the holonomies of all dual cycles of S are equal to 0.

Lemma 3.6.
The holonomies of all dual cycles of S are equal to 0 at the critical point of V .
Proof.
We consider the volume V as a function of R3jFðSÞj of which coordinates are the angles of the 2-faces of S.
There are the constraints which are the equations t þ t þ 	t ¼  at each t 2 FðSÞ and PvalðeÞ
i¼1 i ¼ wðeÞ at each
e 2 EðSÞ.
From Lemma 3.3, the volume V has one critical point (and also it gives the maximum value). Let M be the critical
point. Take F as
F ¼ V ðA Þ 
X
t2FðSÞ
C1ðtÞðt þ t þ 	t  Þ 
X
e2EðSÞ
C2ðeÞ
X
valðeÞ
i¼1
i  wðeÞ
 
!
so that
@F
@j

M
¼ 0
from the Lagrange’s method of indeterminate coeﬃcients. Let mj be the j-th coordinate of M. Let tj be the 2-face of S
which contains j, and ej be the edge of tj which is opposite to j. Then
@F
@j

M
¼  logð2 sin mjÞ  C1ðtjÞ  C2ðejÞ ¼ 0:
ð6Þ
Now let c ¼ ft1; t2; . . . ; th ¼ t1g and vi ¼ ti1 \ ti \ tiþ1. Let ei ¼ ti1 \ ti and eiþ1 ¼ ti \ tiþ1. From (6) and Lemma
3.4, Dðti; viÞ ¼ C2ðeiþ1Þ  C2ðeiÞ at M. Thus the holonomies of all dual cycles are equal to 0.

The remainder of this section is devoted to prove that the singular Euclidean structure in AðS; wÞ is unique. In order
to see the uniqueness, it is suﬃcient to show that any singular Euclidean structure is realized as a critical point of
V ðA Þ.
Lemma 3.7.
There exists at most one singular Euclidean structure in all locally Euclidean structures on S coming
from w.
Proof.
We assume that the holonomies of all dual cycles are equal to 0, and construct ‘‘Lagrange multipliers’’
C1 : FðSÞ ! R and C2 : EðSÞ ! R. Since C1 does not contribute to the holonomy, it is suﬃcient to construct C2. Let
ABC be some 2-face of S and , , 	 be the angles of the 2-face corresponding to the vertices A; B; C. It is clear that we
can construct C2 satisfying C2ðABÞ  C2ðACÞ ¼ logð2 sin Þ  logð2 sin 	Þ.
If there is a singular Euclidean structure on S coming from w, we take multipliers the same as above. So it is a critical
point of V . On the other hand, there is only one critical point from Lemma 3.3. Then the singular Euclidean structure in
AðS; wÞ is unique if it exists.

Theorem 3.8.
If AðS; wÞ is not empty, then there is a unique singular Euclidean structure.
Proof.
The assertion follows from Lemma 3.5 and Lemma 3.7.

4.
Three Dimensional Simplicial Complexes
From Sects. 2 and 3, we obtain the following theorem.
