---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-014-a-quantum-dilogarithm-and-q-series
section_title: "A Quantum dilogarithm and q-series"
section_number: null
pages: 41-43
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
A.1 Faddeev’s non-compact quantum dilogarithm
The quantum dilogarithm Φ b(x) is deﬁned in the strip |Imz|<|Imcb| as [96, 97]
Φb(x) = exp
(∫
R+iϵ
e−2ixz
4 sinh(zb) sinh(zb−1)
dz
z
)
, (A.1)
which can be analytically continued to all values of b with b2⁄∈ R≤0. When Im b2 > 0, the
integral can be evaluated explicitly and one ﬁnds
Φb(x) = (e2πb(x+cb);q)∞
(e2πb−1(x−cb); ˜q)∞
, (A.2)
where
q = e2πib2
, ˜q = e−2πib−2
, Im(b2)> 0 (A.3)
and
cb = i
2
(
b + b−1)
. (A.4)
From this inﬁnite product representation, one ﬁnds that Φ b(x) is a meromorphic function of x
with
poles: xm,n =cb + imb + inb−1, zeros: −cb− imb− inb−1, m,n ∈ N. (A.5)
– 40 –
The residues at poles can be found from the identity [75]
Φb(x +xm,n) = (q;q)∞
(˜q; ˜q)∞
1
(q;q)m
1
(˜q−1; ˜q−1)n
φm(2πbx)~φn(2πb−1)
1− e2πb−1x (A.6)
where
φm(x) =(qm+1ex;q)∞
(qm+1;q)∞
,
~φn(x) = (˜q; ˜q)∞
(˜qex; ˜q)∞
(˜q−1; ˜q−1)n
(˜q−1ex; ˜q−1)n
.
(A.7)
Furthermore, we have the expansion properties of φm(x),~φn(x)
φm(x) = exp
(
−
∞∑
𝓁=1
1
𝓁!E(m)
𝓁 (q)x𝓁
)
,
~φn(x) = exp
(
+
∞∑
𝓁=1
1
𝓁!
~E(n)
𝓁 (˜q)x𝓁
)
.
(A.8)
where
E(m)
k (q) =
∞∑
s=1
sk−1qs(m+1)
1−qs ,
~E(n)
k (˜q) =



−n +E(n)
1 (˜q) if k = 1
E(n)
k (˜q) if k> 1 is odd
2E(0)
k (˜q)−E(n)
k (˜q) if k> 1 is even
(A.9)
The expansion of Φb(x) near its zeros can be found using the inversion formula (A.10).
Some additional useful properties of quantum dilogarithms include
• Inversion formula
Φb(x) Φb(−x) = eπix2
Φb(0)2, Φb(0) =
(q
˜q
) 1
48
= eπi(b2+b−2)/24. (A.10)
• Complex conjugation
Φb(x)∗ = 1
Φb∗(x∗). (A.11)
• Special value
Φb
( i
2(b− b−1)
)
= (q;q)∞
(˜q; ˜q)∞
= b−1e
πi
4−πi
12 (b2+b−2). (A.12)
• Asymptotic behavior
Φb(x)∼
{
Φb(0)2eπix2
when Re( x)≫ 0,
1 when Re( x)≪ 0. (A.13)
– 41 –
• Quasi-periodicity
Φb(x +cb + ib)
Φb(x +cb) = 1
1−qe2πbx (A.14a)
Φb(x +cb + ib−1)
Φb(x +cb) = 1
1− ˜q−1e2πb−1x. (A.14b)
• When b is small, we have the asymptotic expansion
log Φb
( x
2πb
)
∼
∞∑
k=0
(
2πib2)2k−1B2k(1/2)
(2k)! Li2−2k(−ex), (A.15)
where B2k(z) are Bernoulli polynomials. Similarly when b is large, we have
log Φb
( x
2πb−1
)
∼−
∞∑
k=0
(
−2πib−2)2k−1B2k(1/2)
(2k)! Li2−2k(−ex), (A.16)
