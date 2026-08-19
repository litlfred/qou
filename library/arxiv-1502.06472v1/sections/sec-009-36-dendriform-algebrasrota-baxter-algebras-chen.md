---
doc_id: arxiv-1502.06472v1
doc_title: "Gr¨ obner-Shirshov bases and PBW theorems∗ L. A. Bokut †"
section_id: sec-009-36-dendriform-algebrasrota-baxter-algebras-chen
section_title: "Dendriform algebras–Rota-Baxter algebras (Chen-Mo, Kolesnikov)"
section_number: 3.6
pages: 6-7
source_pdf: 1502.06472v1.pdf
source_sha256: 381cd869fcc06f08
doc_brief: "Gröbner-Shirshov bases and PBW theorems∗ L. A. Bokut † — We review some applications of Gr¨ obner-Shirshov bases, including PBW the- orems, linear bases of free universal algebras, normal forms for"
---
Rota-Baxter identity:
P (x)P (y) = P (P (x)y) + P (xP (y)), ∀x, y ∈ A.
Dendriform identities: ( x ≺ y) ≺ z = x ≺ (y ≺ z + y ≻ z), (x ≻ y) ≺ z = x ≻ (y ≺
z), (x ≺ y + x ≻ y) ≻ z = x ≻ (y ≻ z).
D = Den(X|xi ≺ xj = {xi ≺ xj}, x i ≻ xj = {xi ≻ xj}, x i, x j ∈ X);
U(D) = RB(X|xiP (xj) = {xi ≺ xj}, P (xi)xj = {xi ≻ xj}, x i, x j ∈ X).
Then D ⊂ U(D), see Chen-Mo [49].
3.7 Shirshov’s, Cartier’s, Cohn’s counter examples to PBW f or
Lie algebras over commutative algebra
Shirshov [62] 1953 and Cartier [39] 1958 give counter examples to PB W for Lie algebras
over commutative algebra. Cohn [57] 1963 posts the conjecture :
Lp = LieK (x1, x 2, x 3 | y3x3 = y2x2 + y1x1),
K = k[y1, y 2, y 3|yp
i = 0, i = 1, 2, 3].
Lp can not be embedded into its universal enveloping associative algebr a.
Bokut-Chen-Chen [14] establish GS bases theory for Lie algebras o ver a commutative
algebra. We prove Cohn’s conjecture is correct for p = 2, 3, 5.
3.8 “1/2 PBW theorem” (Bokut-Fong-Ke)
Let k be a ﬁeld with the characteristic 0 and C a k-algebra with operations a(n)b, n ≥ 0,
and D(a). Then C is called a conformal algebra, if
(1) (the locality condition). For any a, b ∈ C, there exist N(a, b ) ≥ 0 such that a(n)b = 0
for n ≥ N(a, b ).
(2) D(a(n)b) = D(a)(n)b + a(n)D(b) and D(a)(n)b = −na(n − 1)b.
Let C be a conformal algebra. Then C is an associative conformal algebra if
(As) ( a(n)b)(m)c =
∑
s≥0
(−1)sC n
sa(n − s)(b(m + s)c);
C is a Lie conformal algebra if
(Lie) (anti-commutativity) ( a[n]b) = {b[n]a},
where {b[n]a} =
∑
s≥0
(−1)n+sD(s)(b[n + s]a), D (s) = 1/s !Ds,
(Jacoby) (( a[n]b)[m]c) =
∑
s≥0
(−1)sC s
n((a[n − s](b[m + s]c)) − (b[m + s](a[n − s]c))).
6
Gr¨ obner-Shirshov bases for conformal associative algebras (n-conformal associative al-
gebras) are established in Bokut-Fong-Ke [29] and Bokut-Chen-Z hang [27].
There is a 1/2 PBW-theorem for Lie conformal algebras: Let
L = LieCon({ai, i ∈ I}, N |ai[n]aj =
∑
α k
ijak, i ≥ j, n < N )
be a Lie conformal algebra with the linear basis {ai, i ∈ I} over k[D] and the locality N.
Let
U(L) = AsCon({ai, i ∈ I}, N |S = {sn
ij = ai(n)aj − {aj(n)ai} − ai[n]aj, i ≥ j, n < N })
be the universal enveloping associative conformal algebra for L.
Then any composition ( sn
ij, s m
jk)w = sn
ij(m)ak − ai(n)sm
jk, i > j > k, n, m < N is trivial
mod(S, w ), w = ai(n)aj(m)ak.
There is also a 1/2 PBW theorem between n-conformal Lie algebras and n-conformal
associative algebras, see [27].
