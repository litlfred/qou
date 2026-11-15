---
doc_id: bq28-r2r7
doc_title: "Classical and Quantum Algorithms for Characters of the Symmetric Group"
section_id: sec-001-ii-group-theory-refresher
section_title: "II.. GROUP THEORY REFRESHER"
section_number: null
pages: 3-3
source_pdf: bq28-r2r7.pdf
source_sha256: 38419a88531ebce7
toc_source: outline
doc_brief: "Classical and Quantum Algorithms for Characters of the Symmetric Group — 12 sections: Front matter; I.. INTRODUCTION; II.. GROUP THEORY REFRESHER"
---
Suppose that G is a ﬁnite group. A d-dimensional rep-
resentation of G is a group homomorphism from G to
the unitary group U(d). A representation is irreducible if
the ambient Hilbert space Cd contains no proper subspace
invariant under the action of all group elements. It is stan-
dard to identify irreps that diﬀer only by a basis change
in the ambient Hilbert space. Then any ﬁnite group has a
ﬁnite set of irreps. Given a group element g ∈G and an
irrep λ, let ρλ(g) be the unitary matrix corresponding to g.
The character of g associated with an irrep λ is deﬁned as
a complex number χλ(g) = Tr[ρλ(g)]. The fact that ρλ is
a group homomorphism implies that χλ(g) depends only
on the conjugacy class of g, that is, χλ(g) = χλ(hgh−1) for
all g, h ∈G. Organizing all characters into a matrix with
rows labeled by irreps and columns labeled by conjugacy
classes of G gives the character table of G.
The symmetric group Sn is the group of permutations of
n objects, say integers [n] = {1, 2, . . . , n}. Irreps and con-
jugacy classes of Sn are labeled by partitions of n, that is,
sorted sequences of positive integers λ = (λ1, λ2, . . . , λm)
such that λ1 ≥λ2 ≥· · · ≥λm and m
j =1 λj = n. Here m is
the number of parts in λ. We write λ ⊢n to indicate that λ
is a partition of n. A permutation g ∈Sn is said to be a cycle
of length ℓif there exists a subset J ⊆[n] such that |J| = ℓ
and g cyclically shifts elements of J while acting trivially
on [n] \ J. Any permutation g ∈Sn can be uniquely written
as a composition of cycles with pairwise disjoint supports.
Denoting the number of cycles by c(g) and the length of
the j th longest cycle by νj one obtains a partition of n with
c(g) parts, namely, ν = (ν1, ν2, . . . , νc(g)). The partition ν
speciﬁes the conjugacy class of Sn that contains g. Irreps
of Sn are also labeled by partitions of n. For example, a
partition λ = (n) with a single part labels the trivial rep-
resentation, while a partition λ = (1, 1, . . . , 1) with n parts
labels the sign representation. The general recipe for con-
structing the unitary action ρλ for a given partition λ can
be found in Ref. [28]. The explicit forms of matrices ρλ(g)
are irrelevant for our purposes since we are only interested
in the characters χλ(g) = Tr(ρλ(g)).
