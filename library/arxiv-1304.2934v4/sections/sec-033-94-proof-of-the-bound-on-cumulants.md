---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-033-94-proof-of-the-bound-on-cumulants
section_title: "Proof of the bound on cumulants"
section_number: 9.4
pages: 76-78
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
As X writes X = ∑α∈V Yα, we may use joint cumulants and expand by multilinearity:
κ(r)(X) = ∑
α1,...,αr
κ(Yα1, . . . ,Yαr ). (44)
MOD-φ CONVERGENCE, I 77
The sum runs over lists of r elements in V, that is vertices of the dependency graph G.
The proof consists in bounding each summand κ(Yα1, . . . ,Yαr ), with a bound depend-
ing on the induced subgraph G[α1, . . . ,αr].
9.4.1. Bringing terms together in joint cumulants. Recall the moment-cumulant formula
(42) which states κ(Yα1, . . . ,Yαr ) = ∑π µ(π)Mπ, where
Mπ = ∏
B∈π
E
[
∏
i∈B
Yαi
]
.
We warn the reader that the notationMπ is a little bit abusive as this quantity depends
also on the list (α1, . . . ,αr). By hypothesis, G is a dependency graph for the family
{Yα}α∈V. Hence if some block B of a partition π can be split into two sub-blocks B1
and B2 such that the sets of vertices{αi}i∈B1 and{αi}i∈B2 are disjoint and do not share
an edge, then
E
[
∏
i∈B
Yαi
]
= E
[
∏
i∈B1
Yαi
]
× E
[
∏
i∈B2
Yαi
]
. (45)
Therefore, Mπ = MφH(π), where H = G[α1, . . . ,αr] and φH(π) is the reﬁnement of
π obtained as follows: for each part πi of π, consider the induced graph H[πi] and
replace πi by the collection of vertex sets of the connected components of H[πi]. This
construction is illustrated on Figure 10.
H = 1
23
4
5 6
For example, consider the graph H here opposite
and the partition π ={π1, π2} with π1 ={1, 2, 3, 4}
and π2 ={5, 6}. Then H[π1] (respectively, H[π2])
has two connected components with vertex sets
{1, 2} and{3, 4} (resp.{5} and{6}). Thus
φH(π) ={{1, 2},{3, 4},{5},{6}}.
FIGURE 10. Illustration of the deﬁnition of φH.
We can thus write
κ(G) = ∑
π′
Mπ′

 ∑
π∈φ−1
H (π′)
µ(π)

 .
Fix π′ = ( π′
1, . . . ,π′
t) and let us have a closer look to the expression in the parentheses
that we will call απ′. To compute it, it is convenient to consider the contraction H/π′
of the graph H with respect to the partition π′.
Lemma 9.18. Let π′ be a set partition of [r]. If one of the induced graph H[π′
i] is disconnected,
then απ′ = 0. Otherwise, απ′ = (−1)𝓁(π′)−1FH/π′.
Proof. The ﬁrst part is immediate, as φ−1
H (π′) = ∅ in this case.
If all induced graphs are connected, let us try to describe φ−1
H (π′). All set partitions π
of this set are coarser than π′, so can be seen as set partitions of the index set [r] of the
parts of π′. This identiﬁcation does not change their Möbius functions, which depends
only on the number of parts. Then, it is easy to see that π lies in φ−1
H (π′) if and only
if π is coarser than π′ and two elements in the same part of π never share an edge in
78 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
H/π′ (here, π is seen as a set partition of [r]). In other words, π lies in φ−1
H (π′) if and
only if π⊥ (H/π′). This implies the Lemma. □
Consequently,
κ(Yα1, . . . ,Yαr ) = ∑
π′
(−1)𝓁(π′)−1Mπ′ FH/π′
(
t
∏
i=1
1 H[π′
i ] connected
)
, (46)
where the sum runs over all set partitions π′ of [r].
9.4.2. Bounding all the relevant quantities. Using|Yαi|≤ A for all i, we get the inequality:
|Mπ|≤ Ar−1 E[|Yα1|].
Finally, to bound each summand κ(Yα1, . . . ,Yαr ), we shall use the following bounds:
|FH/π′|≤ STH/π′ by Corollary 9.14;
1 H[π′
i ] connected≤ STH[π′
i ] .
Thus, Equation (46) gives
|κ(Yα1, . . . ,Yαr )|≤ Ar−1 E[|Yα1|] ∑
π′
STH/π′
(
t
∏
i=1
STH[π′
i ]
)
= Ar−1 E[|Yα1|] 2r−1 STH,
(47)
the last equality corresponding to Equation (43). Recall that H = G[α1, . . . ,αr]. Sum-
ming over α1, . . . ,αr and using Equation (44), we get
|κ(r)(X)|≤ (2A)r−1
∑
α1
E[|Yα1|]
[
∑
α2,...,αr
STG[α1,...,αr]
]
.
From Corollary 9.17, we know that the expression in the bracket is bounded by the
quantity rr−2(D + 1)r−1 (for any ﬁxed α1). This completes the proof of Theorem 9.8.
