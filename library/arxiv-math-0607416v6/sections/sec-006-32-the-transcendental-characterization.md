---
doc_id: arxiv-math-0607416v6
doc_title: "PÓLYA-SCHUR MASTER THEOREMS FOR CIRCULAR DOMAINS AND THEIR BOUNDARIES"
section_id: sec-006-32-the-transcendental-characterization
section_title: "The Transcendental Characterization"
section_number: 3.2
pages: 16-17
source_pdf: 0607416v6.pdf
source_sha256: 0705075947ce4a3d
---
bility preservers, respectively.
Proof of Theorems 5 and 6. We only prove Theorem 6 since the proof of Theorem 5
is almost identical. Theorem 6 follows quite easily from Theorem 12 and C orollary 2.
Indeed, note that T [(1 − zw)n] ∈ H 2(C) if and only if T [(z + w)n] ∈ H 2(C). Since
T [(1 − zw)n] =
n∑
k=0
(n)k
(−1)kT (zk)
k! wk
for all n ∈ N we deduce the desired conclusion by comparing the above expressio n
with the modiﬁed symbol GT (z, w) introduced in Notation 3. □
Finally, we show how P´ olya-Schur’s algebraic and transcendental c haracteriza-
tions of multiplier sequences (Theorem 1) follow from our results.
Proof of Theorem 1. We may assume that λ(0) = 1. Statements (i)–(iv) are all
true if dim R T (R[z]) ≤ 2 since then λ(j) = 0 for all j ≥ 2. Hence we may assume
that dim R T (R[z]) > 2. Corollary 1 implies that either
T [(1 − zw)n] =
n∑
k=0
(−1)k
( n
k
)
λ(k)(zw)k ∈ H 2(R)
for all n ∈ N or
T [(1 + zw)n] =
n∑
k=0
( n
k
)
λ(k)(zw)k ∈ H 2(R)
for all n ∈ N. We claim that if f (z) ∈ R[z] then f (zw) ∈ H 2(R) if and only if all
the zeros of f are real and non-negative. Suppose ﬁrst that f (zw) is real stable.
Letting z = w = t we see that f (t2) is hyperbolic, which can only happen if all
the zeros of f are non-negative (since a + t2 is hyperbolic if and only if a ≤ 0).
On the other hand, if f has only real non-positive zeros then f (zw) factors as
f (zw) = C ∏ n
j=0(zw + αj), where αj ∈ R, 1 ≤ j ≤ n. Now zw + αj ∈ H 2(R) if and
only if αj ≤ 0. Hence (i) ⇔ (iv) and by Theorem 5 we also have (ii) ⇔ (iv). The
equivalence of (ii) and (iii) is Laguerre’s classical result. □
P ´OLYA-SCHUR MASTER THEOREMS 17
