---
doc_id: arxiv-2108.03616v2
doc_title: "Circuit imbalance measures and linear programming ∗"
section_id: sec-002-3-properties-of-the-imbalance-measures
section_title: "Properties of the imbalance measures"
section_number: 3
pages: 6-7
source_pdf: 2108.03616v2.pdf
source_sha256: 63696ad045602440
doc_brief: "Circuit imbalance measures and linear programming ∗ — We study properties and applications of various circuit imbalance mea sures associated with linear spaces."
---
Comparison to well-scaled frames Lee’s work [ Lee89] on ‘well-scaled frames’, investigated
the following closely related concepts. For a set S⊆ Q the rational linear space W is S-regular
if for every elementary vector g∈F (F ), there exists a λ⁄= 0 such that all nonzero entries of
λg are in S. For S ={−k,...,k }, the subspace is called k-regular. For k, Ω ∈ N, a subspace is
6
k-adic of order Ω if it is S-regular for S ={±1,±k,..., ±kΩ}. The frame of the subspace W
refers to the set of elementary vectors F(W ).
Using our terminology, a subspace is k-regular if and only if ¯ κW = k, and every k-adic
subspace is anchored. Many of the properties in this section were explicitly or implicitly shown
in Lee [ Lee89]. However, it turns out that many properties are simpler and more natural to state
in terms of either κW and ˙κW . Roughly speaking, the fractional circuit imbalance κW is the
key quantity of interest for continuous properties, partic ularly relevant for proximity results in
linear programming. On the other hand, the lcm-circuit imba lance ˙κW captures most clearly the
integrality properties. The max-circuit imbalance ¯κW interpolates between these two, although,
as already noted by Lee, it is the right quantity for proximit y results in integer programming
(see Section 9).
Appa and Kotnyek [ AK04] also use the term k-regularity in a diﬀerent sense, as a natural
extension of unimodularity. This turns out to be strongly re lated to ˙κW ; see Lemma 3.3 and
Corollary 3.9.
The key lemma on basis forms The following simple proposition turns out to be extremely
useful in deriving properties of κW and ˙κW . The ﬁrst statement is from [ DNV20].
Proposition 3.1. For every matrix A∈ Rm×n with rk(A) = m,
κA = max
{
‖A−1
B A‖max :AB non-singular m×m-submatrix of A
}
.
Moreover, for each nonsingular AB, all nonzero entries of A−1
B A have absolute values between
1/κA and κA and are 1/ ˙κA-integral.
Proof. Consider the matrix A′ = A−1
B A for any non-singular m×m submatrix AB. Let us
renumber the columns such that B corresponds to the ﬁrst m columns. Then, for every m + 1≤
j≤n, the jth column of A′ corresponds to an elementary vector g wheregj = 1, and gi =−A′
ij
fori∈ [m]. Hence, ‖A′‖max gives a lower bound on κA. This also implies that all nonzero entries
are between 1 /κA and κA. To see that all entries of A′ are 1/ ˙κA-integral, note that g = g′/α
for a vector g′ where all entries are integer divisors of ˙ κA. Since gj = 1, it follows that α itself
is an integer divisor of ˙κA.
To see that the maximum in the ﬁrst statement is achieved, tak e the elementary vector gC
that attains the maximum in the deﬁnition of κA; let gC
j be the minimum absolute value element.
Let us select a basis B such that C\{j}⊆ B. Then, the largest absolute value in the j-th
column of A−1
B A will be κA.
