---
doc_id: arxiv-math-0108046v3
doc_title: "arXiv:math/0108046v3 [math.RT] 3 May 2002"
section_id: page-034
section_title: "Page 34"
section_number: null
pages: 34-34
source_pdf: 0108046v3.pdf
source_sha256: f47c1bd39c671cf3
toc_source: undetermined
doc_brief: "Presenting Schur algebras — Motivated by work of R.M. Green, we obtain a pre- sentation of Schur algebras (both the classical and quantized ver- sions) in terms of generators and relations."
---
34
STEPHEN DOTY AND ANTHONY GIAQUINTO
Proposition 11.1. Let EA ∈S+
A and suppose the products are taken
in the box order. Then EA = 0 if |A| > d. Similarly if FC ∈S−
A and
the products are taken in the reverse box order, then FC = 0 if |C| > d.
Proof. Let EA ∈S+
A be given in the box order with |A| > d. For each
j = 2, . . . , n set
EAj =
j−1
Y
i=1
X
(Aj−i,j)
j−i,j
,
where we write Xj−i,j (resp., Aj−i,j) short for Xεj−i−εj (resp., Aεj−i−εj).
Then EA = EAn · · · EA2. According to Proposition 7.9, if EAj1λ̸ = 0,
then EAj1λ = 1µEAj where µj = λj −Pj−1
r=1 Aj−r,j and µs = λs if s > j.
Therefore for EA1λ̸ = 0 it is necessary that λj ≥Pj−1
r=1 Aj−r,j for all
j = 2, . . . , n, and thus
n
X
j=2
λj ≥
n
X
j=2
j−1
X
r=1
Aj−r,j = |A|.
This inequality cannot be satisﬁed since Σn
j=2λj ≤d and |A| > d.
Therefore EA1λ = 0 for all λ ∈Λ(n, d). This forces EA = 0, since
1 = P 1λ. This completes the proof for the claim about the plus part.
The proof for the other claim is similar.
Proposition 11.2. Fix an order on Φ+. The set of EA (resp., FA)
such that |A| ≤d, with products of factors taken in the designated
order, is an A-basis of S+
A (resp., S−
A).
Proof. First consider the box order on Φ+. From Lusztig [Lu2, §4.7]
we know that the set of all EA (products taken in the box order) is
an A-basis of U+. Thus, by Proposition 11.1, the set Γ consisting of
those EA satisfying the condition |A| ≤d is an A-spanning set of S+
A.
The cardinality of this spanning set is equal to dimQ(v) S+, so it follows
that it forms a basis (over Q(v)) of S+. Hence the elements in the set
are linearly independent over Q(v), and thus also over A. Hence they
form an A-basis of S+
A.
Now we form products EA with respect to an arbitrary (but ﬁxed)
order on Φ+. By [Xi2, Theorem 2.4] the set of such products spans
S+
A. But the commutation formulas (8.2) do not increase degree; hence
when we express an element of Γ as an A-linear combination of EA’s (in
the given ﬁxed order on factors) the degree cannot increase. It follows
that the set of EA (|A| ≤d) must span S+
A (over A). It follows that
this set is also an A-basis of S+
A.
