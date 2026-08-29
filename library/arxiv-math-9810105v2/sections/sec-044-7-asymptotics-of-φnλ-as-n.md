---
doc_id: arxiv-math-9810105v2
doc_title: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS"
section_id: sec-044-7-asymptotics-of-φnλ-as-n
section_title: "Asymptotics of φn(λ) as n →∞"
section_number: 7
pages: 43-44
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
doc_brief: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS — The authors consider the length, lN, of the length of the longest increasing subsequence of a random"
---
In this Section, using Lemmas 5.1 and 6.3, we obtain the large n behavior of
φn(λ). In the following δ5, δ6, δ7 are ﬁxed numbers between 0 and 1, and M5, M6, M7
are ﬁxed and positive. These numbers are free apart from the following requirements
:
(a) δ6 satisﬁes (6.35),
(b) M5 ≥1 satisﬁes (5.18),
(c) 1
2M6 ≥1 satisﬁes (5.18), and
(d) M7 ≥1 satisﬁes (6.32), (6.39) and condition (7.8) below.
We consider the following ﬁve cases for λ > 0 and n :
1. 0 ≤2
√
λ
n+1 ≤1 −δ5
2.
1
2 ≤2
√
λ
n+1 ≤1 −
M5
21/3(n+1)2/3
3. 1 −
M6
21/3(n+1)2/3 ≤2
√
λ
n+1 ≤1 +
M6
21/3(n+1)2/3
4. 1 +
M7
21/3(n+1)2/3 ≤2
√
λ
n+1 ≤1 + δ6
5. 1 + δ7 ≤2
√
λ
n+1
44
JINHO BAIK, PERCY DEIFT, AND KURT JOHANSSON
Consider case (i). For any k ≥n, 2
√
λ
k+1 ≤1 −δ5. From Lemma 5.1 (i), we have
as n →∞,
| log φn(λ)| =

∞
X
k=n
log κ2
k(λ)

 ≤
∞
X
k=n
Ce−ck ≤Ce−cn.
(7.1)
Consider case (ii). We split the sum into two pieces.
log φn(λ) =
∞
X
k=n
log κ2
k(λ)
=
X
(1)
log κ2
k(λ) +
X
(2)
log κ2
k(λ)
where (1) and (2) represent the regions
(1) n + 1 ≤k + 1 ≤4
√
λ,
(2) 4
√
λ < k + 1.
For (1), 1
2 ≤2
√
λ
k+1 ≤1 −
M5
21/3(k+1)2/3 . From Lemma 5.1 (ii), for some constant C,
independent of M5 satisfying (5.18),

log κ2
k(λ)

 ≤C e−2
√
2
3
(k+1)(1−2
√
λ
k+1 )
3/2
