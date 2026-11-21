---
doc_id: arxiv-1707.00196v3
doc_title: "Yang-Baxter representations of the inﬁnite symmetric group"
section_id: sec-001-2-r-matrices-and-characters-of-s
section_title: "R-matrices and characters of S"
section_number: 2
pages: 5-6
source_pdf: 1707.00196v3.pdf
source_sha256: 9908b71521275b17
toc_source: outline
doc_brief: "Yang-Baxter representations of the inﬁnite symmetric group — Every unitary involutive solution of the quantum Yang-Baxter equation (R- matrix) deﬁnes an extremal character and a representation of the"
---
R-matrices and characters of S∞
The inﬁnite symmetric group S∞is the group of all bijections of N that move only
ﬁnitely many points, a countable discrete group with inﬁnite (non-trivial) conjugacy
classes. A character of S∞is deﬁned as a positive deﬁnite class function χ : S∞→C
that is normalized at the identity, χ(e) = 1. For example, the trivial representation
has the constant character 1. The characters of S∞form a simplex, the extreme points
of which are called extremal characters (or indecomposable characters). An example
of an extremal character is the Plancherel trace χ(σ) = δσ,e.
Thoma found the following characterization of extremality of characters of S∞,
often called Thoma multiplicativity.
In its formulation, we deﬁne the support of
σ ∈S∞as the complement of the ﬁxed points of σ : N →N.
Theorem 2.1. [23] A character χ of S∞is extremal if and only if for any σ, σ′ ∈S∞
with disjoint supports, it holds that χ(σσ′) = χ(σ)χ(σ′).
Some elements of S∞will appear repeatedly. We write σi,j = (i, j) for two-cycles,
and speciﬁcally σk = σk,k+1 for neighboring transpositions, the standard generators
of S∞. General n-cycles will be denoted cn ∈S∞. In case a speciﬁc choice of n-cycle
is necessary, we choose
cn = σn−1 · · · σ2σ1 = σ1,2σ1,3 · · · σ1,n ,
(2.1a)
σ1,n = σn−1 · · · σ2σ1σ2 · · · σn−1 .
(2.1b)
In view of the above theorem and the cycle decomposition of permutations, an ex-
tremal character χ of S∞is uniquely determined by its values on n-cycles. For a
general group element σ ∈S∞, one then has
χ(σ) =
Y
n≥2
χ(cn)kn,
where kn is the number of n-cycles in the decomposition of σ into disjoint cycles.
5
2.1
