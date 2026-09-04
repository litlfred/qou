---
doc_id: arxiv-1108.0687v3
doc_title: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures"
section_id: sec-008-51-matroids
section_title: "Matroids"
section_number: 5.1
pages: 14-16
source_pdf: 1108.0687v3.pdf
source_sha256: 66ba88e13a429a0a
doc_brief: "Concentration of Lipschitz functionals of determinantal a nd other strong Rayleigh measures — Let {X1,...,X n} be a collection of binary valued random variables and let f : {0, 1}n → R be a Lipschitz"
---
measures
Gaussian random series
Zeros of the IID complex
spanning
trees measures
exclusion
Figure 2: some classes of strong Rayleigh measures
5.1 Matroids
A collection C of subsets of a ﬁnite set E, all of a given cardinality, k, is said to be the set of bases of
a matroid if it satisﬁes the base exchange axiom (see, e.g., [Tut71]): if A andB are distinct members
of C and a ∈ A \B, then there exists b ∈ B \A such that A ∪ {b} \ {a} ∈ C . Given a matroid, it
is natural to consider the uniform measure on C. More generally, the weighted random base is
chosen from the probability measure
νw(B) := C
∏
e∈B
w(e),
where {w(e) : e ∈E} is a collection of nonnegative real numbers (weights) and C is a normalizing
constant. Identifying E with the set {1,..., |E|}, the measure νw and the random variables Xe :=
1e∈B can be thought of as living on B|E|.
For general matroids, EXeXf may be greater than ( EXe)(EXf ). Some speculation has been
given to the most natural class of matroids for which negative corr elation or negative association
must hold. Feder and Mihail [FM92] deﬁne a balanced matroid to be a m atroid all of whose minors
13
satisfy pairwise negative correlation. Their proof of the following fa ct was the basis for the original
proof of negative association for determinantal processes [Lyo0 3, Theorem 6.5].
Proposition 5.1 ([FM92, Theorem 3.2]) . The law νw of a random base of a balanced matroid,
multiplicatively weighted by the weighting function w, has the SCP. □
Because measures supported on the bases of a matroid are homog eneous, there is nothing gained
by improving the SCP to the strong Rayleigh property, and we have t he following immediate corol-
lary.
Corollary 5.2. Letf be a Lipschitz-1 function with respect to Hamming distance o n the bases of a
balanced matroid of rank k on n elements. Then
P(f − Ef >a) ≤ exp
(
−a2
8k
)
.
□
Example 5.3 (spanning trees) . One of the most important examples of a matroid is the set of
spanning trees of a ﬁnite, connected, undirected graph. To s pell this out, a spanning tree for a ﬁnite
graphG = (V,E ) is a subset E′ ⊆E such that (V,E ′) is a connected and acyclic. The set of spanning
trees is a matroid on E. The weighted random spanning tree was shown to be a balanced matroid
by [BP93, Theorem 1]. In fact they showed it is determinantal (see also [Lyo03, Example 1.1]
and [HKPV09, Example 4.3.2]), though at the time consequenc es of being determinantal, such as
the Strong Rayleigh property, had not been developed. Spann ing trees are the only well known class
of matroid whose uniform (or weighted) measure is determina ntal.
Let f0 : {0, 1}E → Z count the number of vertices of odd degree in the graph deﬁned by any
subset of the edges. Deleting or adding an edge changes f0 by at most 2. Let f be the random
variable resulting from applying (1/2)f0 to a the weighted random spanning tree on a graph G.
Thus f is a Lipschitz 1 function that counts half the number of verti ces that have odd degree in
the random tree. Random variables that count local properti es such as this are of natural graph
theoretic interest. Parity counting variables similar to f play a role, for example in the randomized
TSP approximation algorithm of [GSS11]. The number of edges in any spanning tree is |V | − 1.
An application of Corollary 5.2 immediately gives the conce ntration inequality in Theorem 1.1; note
that |V |, rather than |E|, appears in the denominator of the exponent.
Example 5.4 (conditioned Bernoullis, weighted matroids) . Letλ1,...,λ n > 0 be real numbers and
let µ be the measure on the subsets of [n] of cardinality k given by
µ(x1,...,x n) =
∏ n
j=1λxj
j∑
N (y)=k
∏ n
j=1λyj
j
.
We may think of µ in two ways. The ﬁrst is as a special case of the weighted rando m base, specialized
to M (n,k ), the matroid whose bases are all the subsets of [n] that have cardinality k. The second
14
is that it is the law of independent Bernoulli variables Xj with EXj =λj/(1 +λj ), conditioned on∑ n
j=1Xj =k. We see from Proposition 5.1 that µ is strong Rayleigh. Alternatively, we may deduce
this from the strong Rayleigh property for product measures along with closure under conditioning
on the sum [BBL09, Corollary 4.18]. Restricting to [m], for m<n , gives a joint distribution on Bm
which may be thought of as a multivariate generalization of t he hypergeometric distribution. Because
the strong Rayleigh property is inherited, this restrictio n is strong Rayleigh as well. The resulting
concentration properties of these measures have been explo ited in [GSS11] in connection with TSP
approximation. We remark that more general conditioning, s uch as conditioning N :=∑
jXj to lie
in an interval of more than two points, does not preserve the s trong Rayleigh property.
