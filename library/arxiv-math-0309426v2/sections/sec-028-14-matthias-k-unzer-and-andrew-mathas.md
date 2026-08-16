---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-028-14-matthias-k-unzer-and-andrew-mathas
section_title: "MATTHIAS K ¨UNZER AND ANDREW MATHAS"
section_number: 14
pages: 14-14
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
= (−1)kqn−k−2x(k|n−k)
{
1 +
k∑
j=1
(−q)j−k−1Tk,j
}
Tk+1,n−1Tk,1
= (−1)kqn−k−2x(k|n−k)
{
qn−k−1 +
k∑
j=1
(−q)j−k−1Tk,jTk+1,n−1
}
Tk,1
= (−1)kqn−2k−3x(k|n−k)
{
qnTk,1 +
k∑
j=1
(−q)jTk,jTk+1,1Tk+2,n−1
}
= (−1)kqn−2k−3x(k|n−k)
{
qnTk,1 +
k∑
j=1
(−q)jTk+1,1Tk+1,j+1Tk+2,n−1
}
= (−1)kqn−2k−3x(k|n−k)
{
qnTk,1 −
k∑
j=1
(−q)j+1Tk,1Tk+1,j+1Tk+2,n−1
}
= (−1)kqn−2k−3x(k|n−k)Tk,1
{
qn −
k+1∑
j=2
(−q)jTk+1,jTk+2,n−1
}
.
Now, t(k|n−k)rk,1 =
(
2 · · · k + 1
⏐
⏐
1 k + 2 · · · n
)
= ( a∗
tλ |b∗
tλ ) and, consequently,
t(k|n−k)rk,1rk+1,jrk+2,n−1 =
(
2 · · · j − 1 j + 1 · · · k + 1 n
⏐
⏐
1 j k + 2 · · · n − 1
)
, for
j = 2,...,k + 1. This completes the proof for w′
tλ .
Now suppose that t is an arbitrary standard λ–tableau which has n in its ﬁrst
row. Then d(t′) ∈ S(1,n−2,1) so d(t′) and (1 ,n ) commute and ℓ(d(t′)(1,n )) =
ℓ(d(t′)) +ℓ(1,n ). Therefore, w′
t = w′
tλTd(t′). To complete the proof now argue by
induction, as in the proof of Lemma 6.5; we leave the details to the rea der. (Indeed,
this shows that rab = ±qa for some integer a.) □
For convenience we now write ⟨, ⟩ = ⟨, ⟩(k|n−k). In terms of the standard basis
of M (k|n −k), the bilinear form ⟨, ⟩ on M (k|n −k) is determined by
⟨x(a|b),x (s|t)⟩ =
{
qℓ(d(a|b)), if ( a|b) = ( s|t),
0, otherwise,
for standard (k|n −k)–tableaux ( a|b) and ( s|t).
