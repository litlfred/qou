---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-078-1241-divisibility-in-the-ring-ˆzq-here-we-make-s
section_title: "Divisibility in the ring ˆZ[q]. Here, we make some basic observations about"
section_number: 12.4.1
pages: 43-45
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
divisibility for elements of ˆZ[q] by products of powers of cyclotomic polynomials,
which we will freely use in the rest of this section.
Lemma 12.12. Letf (q)∈ ˆZ[q], ζ∈Z , n = ordζ, and k≥ 0. Then the following
conditions are equivalent.
1. f (q) is divisible by Φ n(q)k in ˆZ[q].
2. f (q) is divisible by (q−ζ)k in ˆZ[q]⊗Z Z[ζ].
3. dif
dqi (ζ) = 0 for i = 0, 1,... ,k − 1.
Proof. It is easy to check that (2) and (3) are equivalent, and that (1 ) implies
(2). To prove (2) implies (1), use the fact that f (q) is divisible by ( q−ζ′)k for
eachζ′∈Z with ord(ζ′) = n (by Galois equivariance). The details are left to the
reader.
44 KAZUO HABIRO
Given f (q)∈ ˆZ[q] with f (q)⁄= 0, let ord n(f (q))≥ 0 denote the largest integer
l such that f (q) is divisible by Φ n(q)l. (Existence of such integer follows from
injectivity of the natural homomorphism
ˆZ[q]→ lim
←−kZ[q]/(Φ n(q)k),
see [18, Corollary 4.1].) If f (q) = 0, then set ord n(f (q)) =∞ for all n∈ N. It is not
diﬃcult to show that if d : N→{ 0, 1,... } is a function such that d(n)≤ ordn(f (q))
for all n∈ N, and such that d(n) = 0 for all but ﬁnitely many n∈ N, then f (q) is
divisible by ∏
n∈N Φ n(q)d(n) in ˆZ[q].
A consequence of this fact is the following.
Proposition 12.13. The ring ˆZ[q] is not a unique factorization domain.
Proof. One can easily check that each cyclotomic polynomial Φ n(q), n∈ N, is a
prime element in ˆZ[q]. (In fact, the principal ideal (Φ n(q)) in ˆZ[q] is a prime ideal.)
Let f (q)∈ ˆZ[q] be as deﬁned in the proof of Proposition 12.3. Thus, there is
a sequence 1 ≤ m1 < m2 <··· such that f (q)∈ (Φ mi (q))⊂ ˆZ[q] for all i≥ 1,
where{m1,m 2,... } has no limit points (see the proof of Proposition 12.3). The
observation above implies that f (q) is divisible by Φ m1(q)··· Φ mi (q) for all i≥ 1.
Since Φ mi (q) are prime elements, it follows that ˆZ[q] is not a unique factorization
domain.
12.4.2. Divisibility results.
Proposition 12.14. For any integral homology sphere M , JM− 1 is divisible by
q6− 1 in ˆZ[q].
Proof. In Lemma 10.3, we showed that JM− 1 is divisible by
(q2− 1)(q3− 1)
q− 1 = Φ 1(q)Φ 2(q)Φ 3(q) = q6− 1
Φ 6(q).
Kirby, Melvin and Zhang [39] proved that τ6(M ) = 1 for any integral homology
sphere M . Therefore, JM− 1 is divisible by Φ 6(q), hence the assertion.
Set
˜JM =q−λ1(M)JM∈ ˆZ[q],
where λ1(M ) = 6λ(M )∈ 6Z is the ﬁrst coeﬃcient of the Ohtsuki series τ O(M )∈
Z[[q− 1]]. Clearly, ι1( ˜JM− 1)∈ (q− 1)2Z[[q− 1]]. By Proposition 12.14, ˜JM− 1
is divisible by q6− 1 = (q− 1)(q + 1)(q2 +q + 1)(q2−q + 1). Kirby and Melvin
[38] proved that τ4(M ) = τ√−1(M ) = (−1)χ(M)∈{± 1}, where χ(M )∈ Z/2Z is
the Rochlin invariant of M , which is the mod 2 reduction of λ(M ). Therefore, we
have ev √−1( ˜JM− 1) = 0. Hence, ˜JM− 1 is divisible by q2 + 1. These divisibility
properties of ˜JM− 1 imply the following.
Proposition 12.15. For any integral homology sphere M , ˜JM− 1 is divisible by
Φ 1(q)2Φ 2(q)Φ 3(q)Φ 4(q)Φ 6(q) = (q− 1)(q6− 1)(q2 + 1).
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 45
