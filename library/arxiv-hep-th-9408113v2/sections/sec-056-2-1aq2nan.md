---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-056-2-1aq2nan
section_title: "(1−aq2n)(a)n"
section_number: 2
pages: 52-55
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
(1−a)(q)n
.
Hint: use the Agarwal identity (see e.g. [An2]):
N∑
k=0
(1−aq2k)(q−n)k(a)kqnk
(1−a)(q)k(aqn+1)k
= (aq)NqnN (q1−n)N
(q)N (aqn+1)N
.
Dilogarithm identities 53
It is easy to see that the Watson-Andrews identity (9) (with j = 1 or k + 1) follows
from (14) and (15).
ii) Prove that if α ={αn} and β ={βn} be a Bailey pair relative to a, then
α′
n :=





α0, n = 0,
(1−a)anqn2−n
{ αn
1−aq2n− aq2n−2αn−1
1−aq2n−2
}
, n> 0,
β′
n :=
n∑
k=0
akqk2−k
(q)n−k
βk
is also a Bailey pair relative to aq−1.
Proofs and further details see in [AAB], [Bre6], [P2], [GS], [FQ], [Q2], [Sl], [ML]. It is
well-known (see e.g. [W1]) that the classical Rogers-Raman ujan identities (see e.g. Exercise
6 to Section 2.1) can be deduced from Watson’s [W1] q-analog of Whipple’s transformation
formula (see e.g. [GR]). It seems very interesting to unders tand what kind of partition
identitis correspond to the Milne (see e.g. [Ml3], [ML]) mul tidimensional generalization of
Bailey’s lemma and the Watson-Whipple transformation form ula.
2.2. Dilogarithm and characters of the aﬃne Kac-Moody algeb ras.
Theorem E (Kac-Wakimoto [KW2]). Let chV k
r be the character of level k represen-
tation V (kΛ 0) of the aﬃne Kac-Moody Lie algebra ˆslr. Then
lim
q→1
(1−q) log chV k
r = π2
6
(r2− 1)k
r +k .
Theorem 10. We have
ch(V (kΛ 0)) =
∑
λ∈Zr−1
+
Θ k
λ(z)ck
λ(q),
where
Θ k
λ(z) := Θ k
λ(z1,...,z r−1) =
∑
m∈Zr−1
zkm+λq
1
2 kmAr−1mt+mAr−1λt
, (2.19)
ck
λ(q) = 1
(q)r−1∞
∑
n=(na
i )
q
1
2 n(Ar−1⊗T −1
k−1)nt
∏
a,i(q)na
i
, k ≥ 2; c(1)
λ (q) = δλ,0
(q)r−1∞
(2.20)
and summation in (2.20) is taken over the sequences of nonneg ative integers n = (na
i ),
1≤a≤r− 1, 1≤i≤k− 1 under the following constraints
k−1∑
i=1
ina
i =λa, 1≤a≤r− 1.
54 Anatol N. Kirillov
In (2.19) and (2.20) we used the Cartan matrices
Al =





2 −1 ··· 0
−1 ···
··· ···
··· − 1
0 ··· − 1 2





l×l
Tn =





2 −1 ··· 0
−1 ···
··· ···
··· 2 −1
0 ··· − 1 1





n×n
= (min(i,j ))−1
1≤i, j ≤n
Corollary 5. The constant term of ch(V (kΛ 0)) with respect to z is equal to
CT [ch(kΛ 0)] = 1
(q)r−1∞
∑
n∈(na
i )
q
1
2 n(Ar−1⊗A−1
k−1)nt
∏
i,a
(q)na
j
, (2.21)
where summation is taken over the sequences of nonnegative i ntegers n = ( na
i ),
1≤a≤r− 1, 1≤i≤k− 1, such that
k−1∑
i=1
ina
i≡ 0 (mod k), 1≤a≤r− 1.
Forr = 2 the formula (2.21) is exactly the result of Lepowsky and Pr imc [LP] (see also
[FeSt], [DKKMM], [KMM]). Analogously, for any weight λ = (λ1≥λ2≥···≥ λr−1≥ 0),
one can ﬁnd the coeﬃcient before zλ in the Laurent series (ch V k
r )(z). The result is given
by the RHS(2.21) under the following constraints
k−1∑
i=1
ina
i≡λa(mod k), 1≤a≤r− 1.
The last result about the constant term CT[ z−λ(chV k
r )(z)] coincides with Ar-case of the
Terhoeven and Kuniba-Nakanishi-Suzuki conjecture (see [T r1] and [KNS], Section 2, (9)).
Dilogarithm identities 55
