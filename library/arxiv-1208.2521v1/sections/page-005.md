---
doc_id: arxiv-1208.2521v1
doc_title: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS"
section_id: page-005
section_title: "Page 5"
section_number: null
pages: 5-5
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
toc_source: undetermined
doc_brief: "ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS
5
and the q-exponential functions (1.6), (1.7) can be written as 1φ0(0; −; q, z) and
0φ0(−; −; q, −z), respectively.
Our object will be the Hahn-Exton q-Bessel function written as the q-hypergeometric
series (1.10). It is well-deﬁned for z, w ∈C with w outside {1, q−1, q−2, . . .}. These
singularities can be removed by multiplication by (w; q)∞:
(2.2)
(w; q)∞1φ1(0; w; q, z) =
∞
X
k=0
(−1)k qk(k−1)/2 (qkw; q)∞zk
(q; q)k
.
Proposition 2.1. The series in (2.2) deﬁnes an entire analytic function in z, w,
which is also symmetric in z, w:
(2.3)
(w; q)∞1φ1(0; w; q, z) = (z; q)∞1φ1(0; z; q, w).
Both sides can be majorized by
(2.4)
(−|z|; q)∞(−|w|; q)∞.
Proof. Substitute for (qkw; q)∞in (2.2) the 0φ0 series given by (1.7):
(w; q)∞1φ1(0; w; q, z) =
∞
X
k=0
∞
X
l=0
qkl (−1)l ql(l−1)/2 wl
(q; q)l
(−1)k qk(k−1)/2 zk
(q; q)k
.
The summand of the double series can be majorized by
ql(l−1)/2 |w|l
(q; q)l
qk(k−1)/2 |z|k
(q; q)k
.
Thus the double sum converges absolutely, uniformly for z, w in compacta, and it
is symmetric in z and w.
□
Remark 2.2. Formula (2.3) is a limit case of Heine’s transformation formula
(2.5)
2φ1
a, b
c ; q, z

= (b, az; q)∞
(c, z; q)∞
2φ1
c/b, z
az ; q, b

(cf. [6, (1.4.1)]). Indeed, ﬁrst let b →0, then replace z by z/a and let a →∞. At
least formally, by termwise limits, we obtain (2.3).
Remark 2.3. For w := q1−n (n = 1, 2, . . .) we interpret the left-hand side of (2.2)
by the series at its right-hand side. Then the ﬁrst n terms vanish, so the summation
starts with k = n. When we make the change of summation variable k = n + l, we
obtain
(2.6)
(q1−n; q)∞1φ1(0; q1−n; q, z) = (−1)n qn(n−1)/2 zn (qn+1; q)∞1φ1(0; qn+1; q, qnz)
for n ∈Z. (The case n < 0 follows from the case n > 0 of (2.6) by changing z into
q−nz.)
