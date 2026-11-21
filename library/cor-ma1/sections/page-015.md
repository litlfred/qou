---
doc_id: cor-ma1
doc_title: "Overpartitions, lattice paths and Rogers-Ramanujan identities"
section_id: page-015
section_title: "Page 15"
section_number: null
pages: 15-15
source_pdf: cor-ma1.pdf
source_sha256: d90c91dcd82bfcab
toc_source: undetermined
doc_brief: "Corteel & Mallet, Overpartitions, lattice paths, and Rogers-Ramanujan identities (HAL hal-00017295) — extends Andrews, Bressoud and Burge to overpartitions via successive ranks and generalized…"
---
14
SYLVIE CORTEEL AND OLIVIER MALLET
We will ﬁrst give a generating function proof of that proposition (without the reﬁnement). Then we will
give the sketch of a combinatorial proof which is a generalization of Burge’s correspondence for partitions
presented in [16].
Recall that Bk,i(n, j) is the number of overpartitions λ of n with j overlined parts such that for all ℓ,
f1 < i
λℓ−λℓ+k−1 ≥
(
1
if λℓ+k−1 is overlined
2
otherwise
or equivalently,
f1 < i
∀ℓ, fℓ+ fℓ+1 <
(
k + 1
if a part ℓis overlined
k
otherwise
We will abbreviate this last condition with the notation ∀ℓ, fℓ+ fℓ+1 < k+1.
5.1. A generating function proof. Let Bk,i(a, q) = P
n,j≥0 Bk,i(n, j)ajqn. We prove that
(5.1)
Bk,i(a, q) = Ek,i(a, q)
We will generalize Lovejoy’s proof of Theorem 1.1 of [28]. Let
Jk,i(a, x, q)
=
Hk,i(a, xq, q) −axqHk,i−1(a, xq, q)
(5.2)
Hk,i(a, x, q)
=
∞
X
n=0
xknqkn2+n−inan(1 −xiq2ni)(axqn+1)∞(1/a)n
(q)n(xqn)∞
.
(5.3)
Andrews showed in [3, p. 106-107] that
Hk,i(a, x, q) −Hk,i−1(a, x, q)
=
xi−1Jk,k−i+1(a, x, q)
(5.4)
Jk,i(a, x, q) −Jk,i−1(a, x, q)
=
(xq)i−1(Jk,k−i+1(a, xq, q) −aJk,k−i+2(a, xq, q)).
(5.5)
We plug i = 0 in equation (5.3) and obtain Hk,0 = 0. We then plug i = 1 in equation (5.4) and obtain
Hk,1(a, x, q) = Jk,k(a, x, q). Then we plug i = 1 in equation (5.2) and obtain Jk,1(a, x, q) = Jk,k(a, xq, q).
Finally we set x = 0 in equations (5.2) and (5.3) and get Jk,i(a, 0, q) = 1. This implies for 1 ≤i ≤k, the
following equations determine Jk,i(a, x, q):
Jk,i(a, 0, q)
=
1
Jk,i(a, x, q) −Jk,i−1(a, x, q)
=
(xq)i−1(Jk,k−i+1(a, xq, q) −aJk,k−i+2(a, xq, q));
Jk,1(a, x, q)
=
Jk,k(a, xq, q).
Let Bk,i(a, x, q) = P
n,j,p≥0 Bk,i(n, j, p)ajxpqn where Bk,i(n, j, p) is the number of overpartitions counted
by Bk,i(n, j) with p parts. We show that
Lemma 5.2. For 1 ≤i ≤k,
Bk,i(a, x, q) = Jk,i(−a, x, q).
Proof. The only overpartition with zero parts is the empty one. Therefore Bk,i(a, 0, q) = 1. It is obvious
that for 2 ≤i ≤k, Bk,i(a, x, q) −Bk,i−1(a, x, q) is the generating function for overpartitions such that
∀ℓ, fℓ+ fℓ+1 < k+1 and f1 = i −1. Moreover Bk,i(a, xq, q) is the generating function for overpartitions such
that ∀ℓ, fℓ+fℓ+1 < k+1, f2 < i and f1 = 0. Therefore (xq)i−1Bk,k−i+1(a, xq, q) is the generating function for
overpartitions such that ∀ℓ, fℓ+fℓ+1 < k+1, f1 = i−1 and 1 is not overlined and a(xq)i−1Bk,k−i+2(a, xq, q)
is the generating function for overpartitions such that ∀ℓ, fℓ+ fℓ+1 < k+1, f1 = i −1 and 1 is overlined. We
get, for 2 ≤i ≤k, Bk,i(a, x, q) −Bk,i−1(a, x, q) = (xq)i−1(Bk,k−i+1(a, xq, q) + aBk,k−i+2(a, xq, q)). Finally
Bk,k(a, xq, q) is the generating function for overpartitions such that ∀ℓ, fℓ+ fℓ+1 < k+1, f2 < k and f1 = 0
and therefore is equal to Bk,1(a, x, q).
□
