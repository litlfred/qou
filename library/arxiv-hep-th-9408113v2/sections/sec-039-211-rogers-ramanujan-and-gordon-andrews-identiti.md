---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-039-211-rogers-ramanujan-and-gordon-andrews-identiti
section_title: "Rogers-Ramanujan and Gordon-Andrews identities"
section_number: 2.1.1
pages: 34-35
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
Theorem C. Leta be an integer, 1≤a≤k + 1. Then
i) (Gordon-Andrews)
∑
n1,...,nk
qN 2
1 +...+N 2
k +Na+...+Nk
(q)n1... (q)nk
=
∏
n⁄≡0, ±a mod (2 k+3)
(1−qn)−1 = (2 .1.a)
= (q)−1
∞
∑
m∈Z
(−1)mq
1
2 [m(m+1)(2k+3)−am], (2.1.b)
ii) (G¨ ollnitz-Gordon-Andrews)
∑
n1,...,nk
(−q;q2)N1qN 2
1 +N 2
2 +···+N 2
k +Na+...+Nk
(q2;q2)n1... (q2;q2)nk
=
∏
n⁄≡2(mod 4)
n⁄≡0,±(2a− 1) (mod 4k + 4)
(1−qn)−1, (2.2)
Dilogarithm identities 35
whereNi =ni +... +nk, (q)n := (q;q)n and (x;q)n = (1−x)(1−qx)··· (1−qn−1x).
The Rogers-Ramanujan identities correspond to k = 1, a = 1, or 2 in (2 .1a).
Note that the second equality (2.1.b) follows from the Jacob i triple-product formula∑
m∈Z
xmq
1
2 m(m+1) =
∏
m≥1
(1−qm)(1 +xqm)(1 +x−1qm−1),
which follows from the Cauchy identity (2.6) after passing t o the limit N→∞ .
There exist essentially four methods of proving the partiti on identities of Gordon-
Andrews’ type, namely, analytical one, using the transform ation properties of q-series
(L. Rogers, G. Watson, I. Schur, W. Bailey, L. Slater, G. Andr ews, D. Bressoud, J. Stem-
bridge, ...), algebraic one, based on the recurrence relati ons technique (L. Rogers, S. Ra-
manujan, G. Andrews, R. Baxter, P. Forrester, ...), combina torial one, based on an ex-
plicit construction of a bijection between some sets of part itions (F. Franklin, G. Andrews,
W. Durfee, A. Garsia, S. Milne, D. Bressoud, W. Burge, ...) an d group-theoretical one,
based on an investigation of the (integrable) highest-weig ht modules over the Kac-Moody
or Virasoro algebras and the Weyl-Kac character formula (I. Macdonald, A. Feingold,
J. Lepowsky, R. Wilson, M. Primc, V. Kac, S. Milne, B. Feigin, D. Fuchs, E. Frenkel, ...).
We give here an analytical proof of (2.1) due to D. Bressoud [B re2].
Proof of the Gordon-Andrews identity (for a =k + 1).
It is convenient to divide the proof into three steps.
