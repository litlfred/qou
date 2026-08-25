---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCA TED THET A SERIES RELA TED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-008-6-distinct-5-regular-partitions
section_title: "Distinct 5-regular partitions."
section_number: 6
pages: 16-18
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on tru ncated"
---
Proving identities (6.8), (6.9), (6.11), and (6.14) in [14] combinator ially is still
an open problem. The diﬃculty consists in ﬁnding a combinatorial proo f of the
Weierstrass addition formula [13, Identity (8.1)] used in [13] to prov e these identi-
ties.
In this section, we use the Weierstrass addition formula to prove Th eorem 6.1
below, an interesting identity involving the number of distinct 5-regu lar partitions
of n. This is sequence A096938 in [20] where several other interpretat ions of this
sequence are discussed.
We denote by D5(n) the set of distinct 5-regular partitions of n, i.e., partitions
ofn into distinct parts not divisible by 5. If a,b are integers such that 0 <a,b< 10
anda ⁄≡ ±b (mod 10), we denote by Ca,b(n) the set of pairs of partitions ( λ,µ ) ⊢n
such that λ is a partition with distinct parts not congruent to ±a or ±b modulo 10
and µ is a distinct partition with all parts divisible by 5.
Theorem 6.1. Forn ≥ 1,
|D5(n)| = |C1,2(n)| + |C3,4(n − 1)|.
TRUNCATED THETA SERIES RELATED TO THE JTP IDENTITY 17
Proof. If m ≥ 2 and 0 <s<m , we use the notation
θ(qs;qm) := (qs;qm)∞(qm−s;qs)∞.
As explained in [13, pg. 225], if we ﬁrst replace q byq10 and then take u = −q3,
v =q,x =q4 and y =q3, in [13, Identity (8.1)], we obtain
θ(q2;q10)θ(q4;q10)θ(−q;q10)θ(−q3;q10)
+θ(q;q10)θ(q3;q10)θ(−q2;q10)θ(−q4;q10)
=θ(q3;q10)θ(−q4;q10)θ(q5;q10)θ(−1;q10).(24)
We give a combinatorial interpretation of (24). The q-series
θ(q2;q10)θ(q4;q10)θ(−q;q10)θ(−q3;q10)
is the generating function for
|{λ ∈ D 5(n) |ℓe(λ) even }| − |{λ ∈ D 5(n) |ℓe(λ) odd }|
= (−1)n (|{λ ∈ D 5(n) |ℓ(λ) even }| − |{λ ∈ D 5(n) |ℓ(λ) odd }|),
and the q-series
θ(q;q10)θ(q3;q10)θ(−q2;q10)θ(−q4;q10)
is the generating function for
|{λ ∈ D 5(n) |ℓo(λ) even }| − |{λ ∈ D 5(n) |ℓo(λ) odd }| = (−1)n|D5(n)|.
Here, we used the fact that ℓ0(λ) ≡ |λ| mod 2.
The q-series
θ(q3;q10)θ(−q4;q10)θ(q5;q10)θ(−1;q10)
= 2(q3;q10)∞(q7;q10)∞(−q4;q10)∞(−q6;q10)∞(q5;q10)2
∞(−q10;q10)2
∞
is the generating function for
2(|{(λ,µ ) ∈ C 1,2(n) |ℓo(λ) +ℓo(µ) even }| − |{(λ,µ ) ∈ C 1,2(n) |ℓo(λ) +ℓo(µ) odd }|)
= 2(−1)n|C1,2(n)|.
Hence, the combinatorial interpretation of (24) is
|{λ ∈ D 5(n) |ℓ(λ) even }| = |C1,2(n)|.
If we now follow [13, pg. 226] and ﬁrst replace q by q10 and then take u = q5,
v =q2, x =q6 and y =q4, in [13, Identity (8.1)], we obtain
θ(q2;q10)θ(q4;q10)θ(−q;q10)θ(−q3;q10)
−θ(q;q10)θ(q3;q10)θ(−q2;q10)θ(−q4;q10)
=qθ(−q2;q10)θ(−1;q10)θ(q5;q10)θ(q;q10).(25)
By the same argument as above,
θ(−q2;q10)θ(−1;q10)θ(q5;q10)θ(q;q10)
is the generating function for 2( −1)n|C3,4(n)| and the combinatorial interpretation
of (25) is
|{λ ∈ D 5(n) |ℓ(λ) odd }| = |C3,4(n − 1)|.
□
18 CRISTINA BALLANTINE AND BROOKE FEIGON
