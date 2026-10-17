---
doc_id: li-braid-closures
doc_title: "Knot polynomials on braid closures"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-2
source_pdf: Li-braid-closures.pdf
source_sha256: f7410e7be5bc187e
toc_source: outline
doc_brief: "Knot polynomials on braid closures — We explore properties of the Jones and Alexander polynomials of braid closures of braids of index 3."
---
Introduction
A knot is an embedding of the circle S1 in S3, while a link is an embedding of several circles
in S3. Through the remainder of this paper, we tacitly work with tame links only.
Definition 1.1. A splitting of a link L is a manifold B ⊂S3\L such that B is homeomorphic
to S2 and L intersects both connected components of S3 \ B.
Informally, this occurs exactly when L can be separated into two rigid components that
can be moved arbitrarily far away from each other without disturbing isotopy classes.
Example 1.2. The Hopf link features two linked circles; physical intuition implies that it
exhibits no splitting. Indeed, if a split link has two circles, then it must be the unlink on
two circles, which has Jones polynomial −1
√
t(1 + t). Meanwhile, the Hopf link has different
Jones polynomial −1
√
t(1 + 1
t2).
The Jones polynomial VL(t) is obtained upon specialization of the HOMFLYPT poly-
nomial XL(q, Λ) at q = Λ = t, where we have used the capital letter Λ instead of the more
standard λ in order to avoid confusion with the partitions λ ⊢n.
Proposition 1.3. If L is a split link, then ∆L(t) = 0.
1
Proof. If L splits into L1 and L2, then by the skein relations [1, Example 6.7] we have
XL(q, Λ) = −(1 −Λq)XL1(q, Λ)XL2(q, Λ)
√
Λ(1 −q)
,
which must equal zero if Λq = 1 and q̸ = 1.
Since the Alexander polynomial satisfies
∆L(t) = XL(t, 1
t), it follows that ∆L(t) = 0 for all t ∈C \ {1}. We finish by continuity.
By Proposition 1.3 that the Alexander polynomial detects all splittings. We concern
ourselves with the special value of the the knot determinant VL(−1) = ∆L(−1).
Question 1.4. Is there a link L with no splitting such that ∆L(−1) = 0?
The answer to Question 1.4 is in the positive. In fact, given any L, there is [2] an infinite
family of distinct links L′ all with Jones polynomial equal to VL′(t) = −(
√
t +
1
√
t)VL(t).
Thus ∆L′(−1) = VL′(−1) = XL′(−1, −1) = 0. However, the construction used to create
such links are quite complicated, so we will consider simpler methods.
Theorem 1.5 (Theorems 3.8 and 3.9). There exists an infinite family of links Lm,k, indexed
by pairs of integers (m, k), with the property that any link L satisfying VL(−1) = ∆L(−1) = 0
is equivalent to some Lm,k. In addition, Lm,k has a splitting if and only if m = 0.
The construction of each Lm,k is much simpler than that of [2]. It turns out our work
also yields pairs of distinct non-split links with the same HOMFLYPT polynomial, as in
our second main result.
Theorem 1.6 (Theorem 3.10). If 6 | k, then Xˆγm,k(q, Λ) = Xˆγm+ k
6 ,−k(q, Λ).
The links Lm,k all contain either two or three circles, motivating us to consider how
∆L(−1) would behave if L had braid index at most 3 but was forced to be a knot. Surpris-
ingly, we prove the following third main result in Section 3.2.
Theorem 1.7 (Theorem 3.15). If L is a knot with braid index at most 3, then VL(−1) ≡
∆L(−1) ≡1 (mod 4).
