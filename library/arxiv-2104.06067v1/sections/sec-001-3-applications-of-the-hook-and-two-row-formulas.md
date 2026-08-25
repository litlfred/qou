---
doc_id: arxiv-2104.06067v1
doc_title: "ON IRREDUCIBLE CHARACTERS OF THE IW AHORI-HECKE ALGEBRA IN TYPE A"
section_id: sec-001-3-applications-of-the-hook-and-two-row-formulas
section_title: "Applications of the hook and two-row formulas"
section_number: 3
pages: 11-12
source_pdf: 2104.06067v1.pdf
source_sha256: 750303181ca019ba
doc_brief: "ON IRREDUCIBLE CHARACTERS OF THE IWAHORI-HECKE ALGEBRA IN TYPE A — We use vertex operators to compute irreducible characters o f the Iwahori-Hecke algebra of type A."
---
Let V = V¯
0
⨁ V¯
1 be a Z2-graded vector space over C(q) with basis {v1, v2, · · · , va} for the even
subspace V¯
0 and basis {va+1, va+2, · · · , va+b} for the odd subspace V¯
1. Let π be the endomorphism of
V ⊗ V by
(vk ⊗ vl)π =











(−1)|vk||vl|vl ⊗ vk + (q − 1)vk ⊗ vl, k < l
(−1)|vk |(q+1)+q−1
2 vk ⊗ vl, k = l
(−1)|vk||vl|tvl ⊗ vk, k > l,
(3.1)
and let πi be the endomorphism of V ⊗n by letting π acting on the ( i, i + 1) factor and identity
elsewhere, i = 1, · · · , n − 1. It is known [16] that the map Φ q,n
a,b : Hn(q) − →EndC(t)(V ⊗n) deﬁned by
Ti ↦− →πi
gives rise to a representation of Hn(q) called the sign q-permutation representation.
Let ϕn
a,b be the character of Φ q,n
a,b and let sa,b (λ) be the number of ( a, b)-semi standard tableaux of
shape λ [20]. Then ϕn
a,b decomposes as follows [25]:
ϕn
a,b =
∑
λ ∈H(a,b ;n)
sa,b (λ)χλ
where H(a, b; n) = {λ ⊢ n | λa+1 ≤ b} and χλ is the irreducible character of Hn(q) labeled by λ ⊢ n.
We consider two special cases a = b = 1 and a = 2, b = 0. Then
ϕn
1, 1 =
n−1∑
k=0
χ(n−k, 1k)(3.2)
ϕn
2, 0 =
[n/ 2]∑
k=0
(n − 2k + 1)χ(n−k,k )(3.3)
Theorem 3.1. For µ ⊢ n with l(µ) = l, we have that
ϕn
1, 1(Tγµ ) =
n−1∑
i=0
χ(n−i, 1i)
µ (q) = ( −1)n−l2l−1
l∏
i=1
[µi]−q,(3.4)
11
ϕn
2, 0(Tγµ ) =
[n/ 2]∑
i=0
(n − 2i + 1)χ(n−i,i )
µ (q) = qn−2l(µ )
l∏
i=1
(1 + q + µi(q − 1)).(3.5)
Proof. It follows from the hook formula (2.31) that
n−1∑
i=0
χ(n−i, 1i)
µ (q) =
n−1∑
i=0
(−1)l+i
n∑
j=n−i
aj(µ; q)qj
=(−1)n+l−1
[n/ 2]∑
j=1
a2j−1(µ; q)q2j−1
=(−1)n−l
n∑
j=0
(−1)j − 1
2 aj(µ; q)qj
=(−1)n−l2l−1
l∏
i=1
[µi]−q,
where we have used Lemma 2.8 and the identity ∑ n
i=0 ai(µ; q)qi = 0.
Similarly, using the two-row formula (2.32) and (2.30) we ha ve that
[n/ 2]∑
i=0
(n − 2i + 1)χn−i,i
µ (q)
=
[n/ 2]∑
i=0
(n − 2i + 1)qn−l(bn−i(µ; q) − bn−i+1(µ; q))
=qn−l
n∑
i=0
bi(µ; q)
=qn−2l(µ )
l∏
i=1
(1 + q + µi(q − 1)).
□
We remake that Zhao [25] obtained a negated version of (3.4) a s a q-analog Berele-Regev formula
[1] by the Murnaghan-Nakayama rule.
