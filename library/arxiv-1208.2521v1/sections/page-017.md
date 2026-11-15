---
doc_id: arxiv-1208.2521v1
doc_title: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS"
section_id: page-017
section_title: "Page 17"
section_number: null
pages: 17-17
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
toc_source: undetermined
doc_brief: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS
17
Proposition A.1. For 0 < a < q−1, 0 ≤b < q−1 we have
lim
n→∞2φ1(q−n, qn+1ab; qa; q, qnx) = 1φ1(0; qa; q, x),
uniformly for x in compact subsets of C.
Proof. Put
Rn(x) := 2φ1(q−n, qn+1ab; qa; q, qnx) −1φ1(0; qa; q, x)
=
∞
X
k=1
(−1)k qk(k−1)/2 xk
(qa; q)k (q; q)k

−1 +
k
Y
j=1
(1 −qn−j+1) (1 −qn+jab)

.
Since
k
Y
j=1
(1 −xj) ≥1 −
k
X
j=1
xj
if
0 ≤xj ≤1, j = 1, . . ., k,
we have
−1 +
k
Y
j=1
(1 −qn−j+1) (1 −qn+jab)
 ≤
k
X
j=1
qn−j+1 +
k
X
j=1
qn+jab
≤qn−k+1(1 + ab)
1 −q
if k ≤n, while the left-hand side is equal to 1 otherwise. Thus, for |x| ≤M:
|Rn(x)| ≤qn+1(1 + ab)
1 −q
∞
X
k=1
qk(k−1)/2 q−kM k
(qa; q)k (q; q)k
+
∞
X
k=n+1
qk(k−1)/2 M k
(qa; q)k (q; q)k
,
which tends to 0 as n →∞.
□
Proposition A.2. For α > −1 we have
lim
q↑1 1φ1(0; qα+1; q, (1 −q)2z) = 0F1(−; α + 1; −z),
uniformly for z in compact subsets of C.
Proof.
1φ1(0; qα+1; q, (1 −q)2z) =
∞
X
k=0
(−1)k qk(k−1)/2 (1 −q)2k zk
(qα+1; q)k (q; q)k
and the summand in the sum at the right-hand side can be majorized by
(A.1)
(q−α/2|z|)k
k−1
Y
j=0
(q(α+j)/2 −q1+(α+j)/2) (qj/2 −q1+j/2)
(1 −q1+α+j) (1 −q1+j)
.
