---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-010-4-noncolliding-particles-on-a-circle-and-eigenva
section_title: "Noncolliding particles on a circle and eigenvalues of unitary matrices"
section_number: 4
pages: 21-22
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
Recall from Section 2 the deﬁnition of Bk,n. Due to the relation between Bk,n and the quan-
tum cohomology of the Grassmannian whose ring structure is described by Schur functions, it is
sometimes better to see Bk,n as a graph of partitions (see Appendix A for some reminders on parti-
tions). We denote by Λk the set of generalized partitions of length k≥ 1, which are nondecreasing
sequences of integers of length k and Λk,n the set of partitions of length k such that the ﬁrst part
is smaller that n−k. There is a bijection φ from Λk,n to Bk,n deﬁned by the shift
φ(λ) =λ +I0,
where we recall that I0 = (k− 1,..., 0). By the latter bijection, φ(∅) = I0 and we then have
φ−1(I) =I−I0. Since we will make an extensive use of the maps φ and φ−1, we will simply write
Iλ =φ(λ) and λI =φ−1(I) when there is no ambiguity. Remark that the map φ is independent of
n and extends to a map from Λk toBk, whereBk denotes the set of increasing sequences of integers
of length k. The graph structure of Bk,n yields a graph structure on Λ k,n given by the following
rule, which is a specialization of the so-called quantum Pieri rule, see [5].
Lemma 4.1. There is an oriented edge between I and J in Bk,n if and only if either λI↗λJ in
the usual sense of partition or if (λI)1 = n−k, (λI)k > 0 and λJ =~λI, where for λ∈ Λk,n such
that λ1 =n−k and λk > 0, we write
˜λ = (λ2− 1,...,λ k− 1, 0).
The proof of the latter lemma is a simple transposition to partitions of the edge rule for Bk,n,
which we do not detail here. Finally, recall from Section 2.1 that we also embed Bk,n intoTk with
the map
ξn :



Bk,n → Tk
I ↦→Rk−1
2n
(2π
n I
),
and we have set Tk,n = ξn(Bk,n). To summarize, we have then three sets of cardinal
(n
k
)
related
together as in the following picture.
22 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Tk,n⊂Tk Bk,n⊂Bk
Λk,n⊂ Λk
ξn
φ
