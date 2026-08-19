---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-034-611-proposition-suppose-that-λ-n-k-1k-for-some-k
section_title: "Proposition. Suppose that λ = (n −k, 1k), for some k with 0 ≤k <n. Then"
section_number: 6.11
pages: 16-17
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
the Gram matrix G(λ) of S(λ) is divisibly diagonalizable over Z[q,q −1] with
(n−2
k
)
elementary divisors equal to [k]!
q and with the remaining
(n−2
k−1
)
elementary divisors
being equal to [k]!
q[n]q.
ELEMENTARY DIVISORS OF SPECHT MODULES 17
Proof. By Proposition 6.1 the Gram matrix G(λ) of S(λ) is equal to [ k]!
q times the
Gram matrix of S′(λ). Therefore, by Lemma 4.1 it is enough to show that there is
an invertible diagonal matrix D such that
G′(λ) =
(
⟨w′
s,v ′
t⟩
)
s,t∈Std(k|n−k)
=D ·
(
I ∗
0 [ n]qU
)
,
where I is a
(n−2
k
)
×
(n−2
k
)
identity matrix and U is a
(n−2
k−1
)
×
(n−2
k−1
)
upper tri-
angular matrix with 1’s down its diagonal. Here we order the rows and c olumns
lexicographically with respect to the entries in the ﬁrst column of s and t. Because
D is invertible its non–zero entries are all of the form ±qm, for some integer m.
By Corollary 6.7, the rows of G′(λ) which are indexed by those tableaux which
have n in their ﬁrst row have the required form. This accounts for the iden tity
matrix in the top half of the Gram matrix G′(λ).
Next, suppose that s is a standard (k|n −k)–tableau and that n does not appear
in the ﬁrst row of s. If s = tλ then ⟨w′
s,v ′
t⟩ = 0, for all t ⁄= s, by Corollary 6.9.
If s ⁄= tλ then there exists an integer i, 1 ≤ i < n, such that ℓ(d(s)ri) < ℓ(d(s)).
Therefore,
⟨w′
s,v ′
t⟩ = ⟨w′
sriTi,v ′
t⟩ = ⟨w′
sri,v ′
tTi⟩.
It follows that ⟨w′
s,v ′
t⟩ = 0 if t appears before s in our chosen ordering of Std( λ).
Finally, if t does not appear before s then [n]q divides ⟨w′
s,v ′
t⟩ by Corollary 6.10. □
Notice, in particular, that the Gram matrix calculation in the proof of the Propo-
sition implies that {w′
t | t ∈ Std(λ) } is indeed a basis of S′(λ).
Proposition 6.11 also gives the decomposition numbers of S(λ) (by inducing the
corresponding principal indecomposable modules); however, as th ese are already
known we leave these as an exercise for the reader. We will, however , give one
application of this result.
Let π :S(λ) − →S′(λ) be the isomorphism of Proposition 6.1 and for each stan-
dard λ–tableau t let wt = π−1(w′
t). Then {wt | t ∈ Std(λ) } is a basis of S(λ).
Then, in the case where S(λ) is not irreducible, the proof of Proposition 6.11 also
gives a basis for the simple module D(λ). More precisely, we have the following.
