---
doc_id: arxiv-1208.2521v1
doc_title: "1. Introduction Several possible q-analogues of the Bessel function (1.1) Jα (x) := (−1)k (x/ 2)α +2k k! Γ( α + k + 1) have been considered in the literature. Best known are two re"
section_id: sec-003-2-symmetry-and-orthogonality-for-q-bessel-functi
section_title: "Symmetry and orthogonality for q-Bessel functions"
section_number: 2
pages: 4-6
source_pdf: 1208.2521v1.pdf
source_sha256: 8d0281aa84043865
doc_brief: "ON q-ANALOGUES OF THE FOURIER — For the third q-Bessel function (ﬁrst introduced by F. H. Jackson, later rediscovered by W. Hahn in a special case and by H."
---
We will always assume that 0 < q < 1. The general q-hypergeometric series is
deﬁned by
(2.1) rφ s
[ a1, . . . , a r
b1, . . . , b s
; q, z
]
:=
∞∑
k=0
(a1, . . . , a r; q)k
(
(−1)k qk(k− 1)/ 2) s− r+1
zk
(b1, . . . , b s; q)k (q; q)k
,
where the q-shifted factorial is deﬁned by (1.3) and
(a1, . . . , a r; q)k := (a1; q)k (a2; q)k · · · (ar; q)k.
The upper and lower parameters in the left-hand side of (2.1) may also be written
on one line as a1, . . . , a r; b1, . . . , b s. The power series, in the non-terminating case
of (2.1), has radius of convergence ∞, 1 or 0 according to whether r − s < 1, = 1
or > 1, respectively (see [6, Ch.1] for further details). Thus th e deﬁning formula
(1.2) for the Hahn-Exton q-Bessel function can be rewritten as
Cα (q; x) := (1 − q)α (qα +1; q)∞
(q; q)∞
1φ 1(0; qα +1; q, x (1 − q)2)
ON q-ANALOGUES OF THE FOURIER AND HANKEL TRANSFORMS 5
and the q-exponential functions (1.6), (1.7) can be written as 1φ 0(0; −; q, z ) and
0φ 0(−; −; q, −z), respectively.
Our object will be the Hahn-Exton q-Bessel function written as the q-hypergeometric
series (1.10). It is well-deﬁned for z, w ∈ C with w outside {1, q − 1, q − 2, . . . }. These
singularities can be removed by multiplication by ( w; q)∞ :
(2.2) ( w; q)∞ 1φ 1(0; w; q, z ) =
∞∑
k=0
(−1)k qk(k− 1)/ 2 (qkw; q)∞ zk
(q; q)k
.
Proposition 2.1. The series in (2.2) deﬁnes an entire analytic function in z, w ,
which is also symmetric in z, w :
(2.3) ( w; q)∞ 1φ 1(0; w; q, z ) = ( z; q)∞ 1φ 1(0; z; q, w ).
Both sides can be majorized by
(2.4) ( −|z|; q)∞ (−|w|; q)∞ .
Proof. Substitute for ( qkw; q)∞ in (2.2) the 0φ 0 series given by (1.7):
(w; q)∞ 1φ 1(0; w; q, z ) =
∞∑
k=0
∞∑
l=0
qkl (−1)l ql(l− 1)/ 2 wl
(q; q)l
(−1)k qk(k− 1)/ 2 zk
(q; q)k
.
The summand of the double series can be majorized by
ql(l− 1)/ 2 |w|l
(q; q)l
qk(k− 1)/ 2 |z|k
(q; q)k
.
Thus the double sum converges absolutely, uniformly for z, w in compacta, and it
is symmetric in z and w. □
Remark 2.2. Formula (2.3) is a limit case of Heine’s transformation form ula
(2.5) 2φ 1
[ a, b
c ; q, z
]
= (b, az ; q)∞
(c, z ; q)∞
2φ 1
[ c/b, z
az ; q, b
]
(cf. [6, (1.4.1)]). Indeed, ﬁrst let b → 0, then replace z by z/a and let a → ∞ . At
least formally, by termwise limits, we obtain (2.3).
Remark 2.3. For w := q1− n (n = 1, 2, . . . ) we interpret the left-hand side of (2.2)
by the series at its right-hand side. Then the ﬁrst n terms vanish, so the summation
starts with k = n. When we make the change of summation variable k = n + l, we
obtain
(2.6)
(q1− n; q)∞ 1φ 1(0; q1− n; q, z ) = ( −1)n qn(n− 1)/ 2 zn (qn+1; q)∞ 1φ 1(0; qn+1; q, q nz)
for n ∈ Z. (The case n < 0 follows from the case n > 0 of (2.6) by changing z into
q− nz.)
