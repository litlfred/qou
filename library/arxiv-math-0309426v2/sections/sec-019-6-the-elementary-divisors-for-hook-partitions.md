---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-019-6-the-elementary-divisors-for-hook-partitions
section_title: "The elementary divisors for hook partitions"
section_number: 6
pages: 9-10
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
Throughout this section we ﬁx an integer k, with 0 ≤ k < n, and consider the
Specht module S(λ), where λ = (n −k, 1k). We will show that G(λ) is divisibly
diagonalizable by explicitly constructing two bases of S(λ) which transform G(λ)
into the form of the matrix in Lemma 4.1. In particular, this will allow us t o
determine the elementary divisors of S(λ).
The Specht module S(λ) is deﬁned as a submodule of the permutation module
M (λ); however, to compute the elementary divisors we will work inside a d iﬀerent
permutation module.
By deﬁnition, S(λ) = xλTwλyλ′ H = x(n−k,1k )Tw(n−k, 1k )y(k+1,1n−k−1). We ﬁrst
need to understand the permutation wλ = w(n−k,1k) a little better. This requires
some new notation. For integers non–negative i and j deﬁne
ri,j =





1, if i = 0 or j = 0,
riri+1...r j, if 0 <i ≤j,
riri−1...r j, if i>j > 0,
and set Ti,j =Tri,j . Next, let a and b be non–negative integers such a +b ≤n. If
either a = 0 or b = 0 then set wa,b = 1. If both a and b are non–zero then deﬁne
wa,b = (ra+b−1,1)b; then one can check that, in two–line notation,
wa,b =
( 1 2 ... a
a + 1 a + 2 ... a +b
b + 1 b + 2 ... a +b 1 2 ... b
)
.
It is not hard to see that wb,a =w−1
a,b and that wa,b =ra,a+b−1wa−1,b andℓ(wa,b) =
ℓ(ra,a+b−1) +ℓ(wa−1,b); see [ 4]. Consequently,
wa,b =ra,a+b−1ra−1,a+b−2...r 1,b =r1,ar2,a+2...r b,a+b−1
with the lengths adding in both cases. Hence, ℓ(wa,b) = ab.
The permutation w(n−k,1k) is essentially one of these permutations because
w(n−k,1k) =
( 1 2 · · · n −k n −k + 1 · · · n
1 k + 2 · · · n 2 · · · k + 1
)
.
Hence, w(n−k,1k ) =rn−k,n−1rn−k−1,n−2...r 2,k+1, with the lengths adding. So
Tw(n−k, 1k )
=Tn−k,n−1...T 2,k+1,
Notice also that Twn−k.k =Tw(n−k, 1k )T1,k.
If w ∈ S(k,n−k) ∼
= Sk × Sn−k then we write w = (u,v ), where u ∈ Sk and
v ∈ S(1k,n−k) are the unique permutations such that w =uv =vu. Set
x(k|n−k) =y(k,1n−k)x(1k,n−k) =
∑
(u,v)∈S(k,n −k)
(−q)−ℓ(u)Tuv.
Then it is easy to see that Rx(k|n−k) is an H (Sµ)–module on which the subal-
gebras H (Sk) and H (S(1k,n−k)) act via their sign and trivial representations,
respectively. Let
M (k|n−k) = Ind H (Sn)
H (S(k,n −k))
(
Rx(k|n−k)
) ∼
=x(k|n−k)H.
