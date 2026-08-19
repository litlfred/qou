---
doc_id: arxiv-gr-qc-0407051v2
doc_title: "Black hole entropy from Quantum Geometry"
section_id: sec-005-iii-the-combina-toric-formula-tion-of-the-proble
section_title: "THE COMBINA TORIC FORMULA TION OF THE PROBLEM"
section_number: III
pages: 7-9
source_pdf: 0407051v2.pdf
source_sha256: 2de07e909b17c5a5
doc_brief: "Black hole entropy from Quantum Geometry — Quantum Geometry (the modern Loop Quantum Gravity using gra phs and spin-networks instead of the loops) provides microscopic d egrees of freedom that"
---
From now our treatment starts to diﬀer from that of [8]. Our ai m is to deﬁne the number
of the quantum states of the horizon which contribute to the e ntropy in a form of a clear
and precise combinatoric formula.
Recall that the classical area a of the horizon is ﬁxed as
a = 4 πγℓ 2
Plk, k ∈ N. (24)
7
Calculation of the horizon entropy consists in counting tho se quantum horizon states, ele-
ments of the Hilbert space HS,phys (21) labeled by the ﬁnite sequences deﬁned in (15) (the
number n of the entries can be arbitrary) which correspond to subspac es Hb(m),j,m in (23)
such that the area operator eigenvalue aj
S satisﬁes the following inequality 3
aj
S = 8 πγℓ 2
Pl
n∑
i=1
√
ji(ji + 1) ≤ a. (25)
Combinatorially, the task amounts to counting the ﬁnite seq uences ( b1, ..., bn) of elements of
Zk, such that the following two conditions ( i) and ( ii) are satisﬁed:
(i)
n∑
i=1
bi = 0 , (26)
(ii) there exist two sequences: a sequence ( j1, ..., jn) consisting of non-zero elements of 1
2N
which satisﬁes the inequality (25), and a sequence ( m1, ..., mn) such that
bi = −2mi mod k , (27)
and mi ∈ {− ji, −ji + 1, ..., ji} , (28)
for every i = 1, , , n.
This recipe can be simpliﬁed. It is easy to eliminate the ji’s by noting that, given a
sequence ( m1, ..., mn), there is a sequence ( j1, ..., jn) such that (28) and (25) if and only if
8πγℓ 2
Pl
n∑
i=1
√
|mi|(|mi| + 1) ≤ a. (29)
Next, it follows from (26, 27) that
n∑
i=1
mi = n′ k
2 , (30)
with some n′ ∈ Z. But then,
a = 4 πγℓ 2
Plk ≥ 8πγℓ 2
Pl
n∑
i=1
√
|mi|(|mi| + 1) > (31)
> 8πγℓ 2
Pl
n∑
i=1
|mi| ≥ 8πγℓ 2
Pl|
n∑
i=1
mi| = (32)
= 4 πγℓ 2
Plk|n′|. (33)
3Assuming just inequality instead of considering an interval [a−δa, a +δa ] simpliﬁes the calculation.
Knowing the result for all a one can always consider the interval. The result, at least in our case,
is the same.
8
Hence
n∑
i=1
mi = 0, and also
n∑
i=1
|mi| ≤ k
2 . (34)
Finally, notice that given a sequence (b1, ..., bn) of elements of Zk there is exactly one sequence
(m1, ..., mn) of elements of 1
2Z such that (27) and (34) holds. In this way, we have derived
the following formula for the entropy counting:
The entropy S of a quantum horizon of the classical area a according to Quantum Ge-
ometry and the Ashtekar-Baez-Corichi-Krasnov [8] framewo rk is
S = ln N(a), (35)
where N(a) is 1 plus the number of all the ﬁnite sequences (m1, ...., mn) of non-zero elements
of 1
