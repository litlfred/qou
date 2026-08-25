---
doc_id: arxiv-math-0605314v1
doc_title: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres"
section_id: sec-079-1243-applications-to-the-ohtsuki-series-here-we
section_title: "Applications to the Ohtsuki series. Here we apply Propositions 12.14 and"
section_number: 12.4.3
pages: 45-47
source_pdf: 0605314v1.pdf
source_sha256: 5fb8b89b432401ea
doc_brief: "A unified Witten-Reshetikhin-Turaev invariant for integral homology spheres — W e construct an invariant JM of integral homology spheres M with values in a completion ˆZ[q] of the polynomial ring"
---
12.15 to the Ohtsuki series τ O(M ), and obtain some congruence relations on the
coeﬃcients of τ O(M ), which generalize well-known results by Murakami [62] and
Ohtsuki [67], and by Lin and Wang [54, 55] for the ﬁrst and the s econd coeﬃcients.
We write
τ O(M ) = ι1(JM ) = 1 + λ1(M )ℏ +λ2(M )ℏ 2 +···∈ Z[[ℏ ]],
where we set ℏ =q− 1. We often write λi =λi(M ) in the following.
The following gives an inﬁnite set of congruence relations f or the coeﬃcients
λi(M ) of the Ohtsuki series of M .
Proposition 12.16. Fork≥ 0, we have
k∑
i=0
aiλk−i+1(M )≡ 0 (mod Z).(12.8)
Herea0 = 1/6, a1 =−1/4, a2 = 17/72, a3 =−25/144,···∈ Z[ 1
6 ] are determined
by
∑
i≥0
aiℏ i = 1
(q + 1)(q2 +q + 1) = 1
6 + 9ℏ + 5ℏ 2 + ℏ 3.
In particular, each λk+1(M ) mod 6 , k≥ 0, is determined by λi(M ), i = 1,... ,k .
Proof. Set
f (ℏ ) = ℏ −1(τ O(M )− 1) =
∑
k≥0
λk+1ℏ k∈ Z[[ℏ ]],
a(ℏ ) = (q + 1)(q2 +q + 1) = 6 + 9 ℏ + 5ℏ 2 + ℏ 3.
Using Proposition 12.14, we see that there is g(ℏ ) = ∑
k≥0gkℏ k∈ Z[[ℏ ]] such that
f (ℏ ) = a(ℏ )g(ℏ ), hence g(ℏ ) = f (ℏ )a(ℏ )−1. (Here we used the divisibility of JM− 1
by (q− 1)(q + 1)(q2 +q + 1), not by q6− 1.) We have
gk =
k∑
i=0
aiλk−i+1.
Since gk∈ Z for all k≥ 0, we have (12.8). Since a0 = 1/6, the latter assertion
follows.
By (12.8) and a0 = 1
6 , we have
λk+1≡−
k∑
i=1
6aiλk−i+1 (mod 6).(12.9)
For small values of k, (12.9) implies the following.
1. λ1≡ 0 (mod 6). This is known by Murakami [62] and Ohtsuki [67].
2. λ2≡ 3
2λ1≡ 1
2λ1 (mod 6). This is known by Lin and Wang [54]. See also
Corollary 12.20 below.
3. λ3≡ 3
2λ2− 17
12λ1 (mod 6).
4. λ4≡ 3
2λ3− 17
12λ2 + 25
24λ1 (mod 6).
46 KAZUO HABIRO
Remark 12.17. One can use divisibility of JM− 1 by q6− 1 instead of ( q− 1)(q +
1)(q2 +q + 1) = ( q6− 1)/Φ 6(q). In this case, we obtain a result equivalent to
Proposition 12.16 as a consequence of the fact that Φ 6(q) = q2−q + 1 is invertible
in Z[[q− 1]].
The above-described idea can be applied also to Proposition 12.15 to obtain
better results. We write
ι1(JM−qλ1(M)) = τ O(M )−qλ1(M) =
∑
k≥2
λ′
k(M )ℏ k.
We have
λ′
k(M ) = λk(M )−
(λ1(M )
k
)
∈ Z(12.10)
for k≥ 2.
Proposition 12.18. Fork≥ 0, we have
k∑
i=0
biλ′
k−i+2(M )≡ 0 (mod Z).(12.11)
Hereb0 = 1/12,b1 =−5/24,b2 = 41/144,b3 =−77/288,···∈ Z[ 1
6 ] are determined
by
∑
i≥0
biℏ i = 1
(q + 1)(q2 +q + 1)(q2 + 1) = 1
12 + 30ℏ + 34ℏ 2 + 21ℏ 3 + 7ℏ 4 + ℏ 5.
In particular, for k≥ 0,λ′
k+2(M ) mod 12 is determined by λ′
i(M ),i = 2,... ,k +1.
Proof. The proof is similar to that for Proposition 12.16, where we u se Proposition
12.15 instead of Proposition 12.14. The details are left to t he reader.
Corollary 12.19. For k ≥ 0, λk+2(M ) mod 12 is determined by λi(M ), i =
1,... ,k + 1.
Proof. This immediately follows from Proposition 12.18 and (12.10 ).
The case k = 0 of (12.11) is equivalent to the following.
Corollary 12.20 (Lin and Wang [55]) . We have
λ2(M )≡ 3λ(M ) = 1
2λ1(M ) (mod 12) .
Proof. We have λ2(M )≡
(λ1(M)
2
)
=
(6λ(M)
2
)
= 18λ(M )2− 3λ(M )≡ 6λ(M )−
3λ(M )≡ 3λ(M ) (mod 12).
Remark 12.21. Propositions 12.14 and 12.15 can be applied to the power seri es
ι−1(JM )∈ Z[[q + 1]] and one can obtain results similar to Propositions 12.1 6 and
12.18. In particular, we have the following.
1. λ−1,1(M )∈ 6Z.
2. λ−1,2(M )≡ 1
2λ−1,1(M ) (mod 12).
3. For k≥ 2, λ−1,k(M ) mod 12 is determined by λ−1,i(M ),i = 1, 2,... ,k − 1.
Here λ−1,k(M )∈ Z is deﬁned as in (12.5).
A UNIFIED WITTEN-RESHETIKHIN-TURAEV INV ARIANT 47
Remark 12.22. As for the relation between λ1(M ) and λ−1,1(M ), we have
λ1(M )≡λ−1,1(M ) (mod 12) .(12.12)
Hence, like the Casson invariant, the mod 2 reduction of the i nteger-valued in-
variant 1
6λ−1,1 equals the Rochlin invariant of M . (12.12) follows from λ1(M )≡
λ−1,1(M )≡ 0 (mod 3) and λ1(M )≡λ−1,1(M ) (mod 4). (Here, the latter congru-
ence follows from (12.6) for ζ = 1, ξ =−1, k = 1.)
