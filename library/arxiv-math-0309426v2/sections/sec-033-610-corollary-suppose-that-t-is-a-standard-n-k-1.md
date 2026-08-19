---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-033-610-corollary-suppose-that-t-is-a-standard-n-k-1
section_title: "Corollary . Suppose that t is a standard (n −k, 1k)–tableau and that n does"
section_number: 6.10
pages: 16-16
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
not appear in the ﬁrst row of t. Then ⟨w′
t,v ′
t⟩ =qk(n−k−2)[n]q.
Proof. Recall that if t is a standard λ–tableau then d(t′)d(t)−1 = wλ′ , with the
lengths adding; this is well–known and is easily proved by induction on th e domi-
nance order for tableaux. Therefore,
⟨w′
t,v ′
t⟩ = ⟨w′
tλTd(t),x (k|n−k)y′
k+1Td(t′)⟩ = ⟨w′
tλ,x (k|n−k)y′
k+1Td(t′)T ∗
d(t)⟩
= ⟨w′
tλ,x (k|n−k)y′
k+1Td(tλ ′)⟩ = ⟨w′
tλ,v ′
tλ ⟩.
Hence, it is enough to consider the case where t = tλ.
Suppose that t = tλ. Then, by Lemma 6.5 and Lemma 6.8,
⟨w′
tλ,v ′
tλ ⟩ =q2ℓ(wλ ′ )
{
q−ℓ(d(a+
λ |b+
λ ))[n −k]q +
∑
(a|b)≺tλ
(a|b)⁄=(a+
λ |b+
λ )
q−ℓ(d(a|b))
}
.
Using the remarks before Lemma 6.4 it is not hard to see that ℓ(d(a+
λ |b+
λ )) =
k(n −k) and that ℓ(d(a|b)) = (k − 1)(n −k) + 2 −It(a|b), whenever ( a|b) ≺ tλ and
(a|b) ⁄= (a+
λ |b+
λ ). Therefore,
⟨w′
tλ,v ′
tλ ⟩ =q2ℓ(wλ ′ )
{
q−k(n−k)[n −k]q +
k+1∑
i=2
q−(k−1)(n−k)−2+i
}
=q2ℓ(wλ ′ )−k(n−k)
{
[n −k]q +qn−k
k−1∑
j=0
qj
}
=q2ℓ(wλ ′ )−k(n−k)[n]q.
Asℓ(wλ′ ) = k(n −k − 1) the result follows. □
Finally, we can prove the main result of this section.
