---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-008-vii-classical-mps-algorithm-for-kostka-numbers
section_title: "VII.. CLASSICAL MPS ALGORITHM FOR KOSTKA NUMBERS"
section_number: null
pages: 12-14
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
toc_source: outline
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 12 sections: Front matter; I.. INTRODUCTION; II.. GROUP THEORY REFRESHER"
---
KOSTKA NUMBERS
In Sec. IV we showed that Crichigno and Prakash’s con-
nection between quantum spin chains and characters of the
symmetric group can be leveraged in an MPS algorithm
for characters. In Ref. [13] they also proved mappings
between spin chains and Kostka numbers and Littlewood-
Richardson coeﬃcients. Using similar ideas to characters,
we show that this correspondence can be used to give an
MPS algorithm for Kostka numbers.
Kostka numbers appear frequently in combinatorics and
representation theory. Let λ ⊢n. A semistandard Young
tableau of shape λ is a ﬁlling of the boxes in the Young
diagram corresponding to λ with positive integers between
1 and n such that the labels are nondecreasing across rows
and strictly increasing down columns. The weight of such
a tableau is an integer-valued vector of length n such that
the ith entry is the number of occurrences of i. The Kostka
number Kλ,μ is the number of semistandard Young tableaus
of shape λ and weight μ. Note that Kλ,μ is independent of
the order of the entries in μ and thus we assume that μ
is a partition of n. A notable special case is Kλ,(1n), which
is the dimension of the irrep labeled by λ. More gener-
ally, Kλ,μ appears in the representation theory of Sn as
the multiplicity of the irrep λ in the permutation module
indexed by μ. In the language of symmetric polynomials,
the Kostka numbers encode the change of basis from Schur
polynomials to complete symmetric polynomials.
Crichigno and Prakash used this latter characterization
to demonstrate that quantum spin chains encode Kostka
numbers as well [13]. We brieﬂy review their construc-
tion here. Again, let the initial state |xτ⟩correspond to the
integer sequences (n −1, n −2, . . . , 0) in the second quan-
tization picture. For commuting variables, the complete
symmetric polynomial hk is given by
hk =

1≤i1≤···≤ik
xi1xi2 · · · xik.
(44)
For example, in three variables h2 = x2
1 + x2
2 + x2
3 +
x1x2 + x1x3 + x2x3. In Crichigno and Prakaksh’s construc-
tion the commutative variables are replaced with oper-
ators ˆxi := a†
i+1ai, where a (a†) is again an annihilation
(creation) operator. Then, the noncommutative complete
symmetric polynomials take the form
ˆhk =

i1>···>ik
ˆxi1 ˆxi2 · · · ˆxk.
(45)
Note that the indices are required to be strictly decreasing,
which follows from ˆx2
i = 0 for any index i. Say that μ ⊢n
is a partition of length m. We deﬁne ˆhμ = m
j =1 ˆhμj (the
operators commute and thus the order of the product does
not matter [13]). The authors showed that
Kλ,μ = ⟨xλ+τ|ˆhμ|xτ⟩.
(46)
Note that ˆhμ moves fermions at most n sites to the right and
we can again truncate the chain to 2n sites with the initial
state |xτ⟩= |1n0n⟩.
Similarly to the MPS algorithm for characters, we rep-
resent the 2n-qubit state
|ψμ⟩=
m

i=1
ˆhμi|1n0n⟩
(47)
by an MPS. We do so via the following lemma.
Lemma 7. The noncommuting complete symmetric
polynomial ˆhk is an MPO with bond dimension 2k + 1.
Proof. Figure 4 deﬁnes a tensor T ∈C2 ⊗C2k+1 ⊗
C2k+1 ⊗C2, where C2 represents physical indices and
C2k+1 represents virtual indices of the MPO. Taking 2n
FIG. 4.
MPO representation of the noncommuting complete
symmetric polynomial ˆhk. Horizontal lines represent virtual
indices of dimension 2k + 1. We label basis vectors of C2k+1 by
integers {0, 1, . . . , 2k}. The MPO consists of 2n copies of T. We
list all nonzero components of tensor T.
copies of T and contracting the virtual indices gives an
operator

i1>i2>···>ik
ˆxi1 ˆxi2 · · · ˆxik.
(48)
This is exactly ˆhk as deﬁned in Eq. (45).
■
From the bond dimension of this MPO, we can upper
bound the maximum bond dimension of all states during
compression as
D ≤
m

j =1
(2μj + 1).
(49)
In running numerics, however, bond dimensions appeared
to be signiﬁcantly lower.
Denote the compressed MPS state as |mpsμ⟩. Similarly
to characters, Kostka numbers take integer values and thus
the correct value is recovered as long as
|Kλ,μ −⟨λ|mpsμ⟩| < 1
2.
(50)
We again used the mpnum software for numerical simula-
tions with an error rate ε = 10−11. We compared the MPS
algorithm to the symmetrica library of SAGE; see Fig. 5.
For numerical experiments, we selected random par-
titions μ with a smaller number of parts, fewer than
FIG. 5.
Runtime for computing Kostka numbers Kλ,μ. Each
runtime is, ﬁxing a random μ, for computing the set {Kλ,μ}λ.
One hundred random μ’s of length less than n/3 were sampled
for each n. The MPS compression error is set to ε = 10−12 for
all the data. Boxes indicate the ﬁrst and third quartiles and the
whiskers denote 1.5 times the interquartile range.
n/3. On longer partitions the MPS algorithm appears to
require smaller ε and longer run times. For example,
μ = (1, . . . , 1) proved diﬃcult to compute via the MPS
algorithm yet can be quickly computed via the hook length
formula. However, in the regime of shorter partitions, our
numerics oﬀer evidence that the MPS is competitive and
often faster than Sage for large n. It is further worth noting
that most partitions are relatively short, the average being
[√n log(n)] [51]. Our implementation, as well as that for
skew Kostka numbers (a generalization), is available from
GitHub [33].
An interesting question, which we leave for future work,
is if Littlewood-Richardson coeﬃcients can be recovered
by a nontrivial MPS algorithm. Doing so via a mapping to
spin chains would require MPO constructions for noncom-
mutative Schur polynomials [13]. Schur polynomials do
not admit an obvious modular construction unlike c(g)
j =1 Jηj
and m
j =1 ˆhμj (from the commuting products). This would
seem to complicate MPO constructions.
We also leave open the question of sampling from dis-
tributions with probabilities deﬁned by normalized Kostka
numbers, in analogy to the results in Sec. V. A related task
was studied in Refs. [27,37], but there the distributions
contained just a single probability that was a normalized
Kostka number. It would be interesting to ﬁnd quantum
circuits that prepare a quantum state that corresponds to
