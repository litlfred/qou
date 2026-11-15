---
doc_id: 022201-1-online
doc_title: "Efficient algorithms for approximating quantum partition functions"
section_id: sec-002-i-introduction
section_title: "INTRODUCTION"
section_number: I
pages: 2-3
source_pdf: 022201_1_online.pdf
source_sha256: 50331bf18a2bd4d5
toc_source: inferred
doc_brief: "Efficient algorithms for approximating quantum partition functions — 13 sections: Front matter; AFFILIATIONS; ABSTRACT"
---
Classical algorithms for approximating partition functions of quantum models that make use of cluster expansions have occurred in two
recent papers.1,2 In this paper, we provide a simple and concise exposition of how to construct such algorithms, with the intent of making the
technique accessible to a wide audience.
A quantum spin system is modelled by a hypergraph G = (X, E). At each vertex x of G, there is a d-dimensional Hilbert space Hx with d <
∞. The Hilbert space on the hypergraph is given by HG ∶= ⊗x∈XHx. An interaction Φ assigns a self-adjoint operator Φ(e) on He ∶= ⊗x∈eHx
to each hyperedge e of G. The Hamiltonian on G is defined by HG ∶= ∑e∈E(G)Φ(e). We are interested in the quantum partition function ZG(β)
at inverse temperature β, defined by ZG(β) ∶= Tr[e−βHG].
In what follows, we shall focus our attention on quantum spin systems modeled by bounded-degree graphs; however, generalizations
to bounded-degree bounded-rank hypergraphs are also possible. We shall assume that ∥Φ(e)∥≤1 for every e ∈E, where ∥⋅∥denotes the
operator norm. Note that this is always possible by a rescaling of β. To state our main result, recall that a fully polynomial-time approximation
scheme for a sequence of complex numbers (zn)n∈N is a deterministic algorithm that, for any n and ϵ > 0, produces a complex number ˆzn such
that ∣zn −ˆzn∣≤ϵ∣zn∣in time polynomial in n and 1/ϵ.
Theorem 1. Fix Δ ∈Z+. There is a fully polynomial-time approximation scheme for the partition function ZG(β) for all graphs G of
maximum degree at most Δ and all complex numbers β such that ∣β∣≤
1
e4Δ.
Our algorithm is based on combining the abstract cluster expansion for quantum spin systems of Netoˇcný and Redig3 with the algo-
rithmic framework of Helmuth, Perkins, and Regts.4 The condition ∣β∣= O( 1
Δ) is optimal under the complexity-theoretic assumption that
RP (randomized polynomial time) is not equal to NP (non-deterministic polynomial time) due to the results on the hardness of approximate
counting.5,6 We remark that these results concern real values of β; however, similar computational complexity transitions from P (polynomial
time) to BQP-hard (bounded-error quantum polynomial time) and P to #P-hard can also be observed for complex values of β by using the
methods of Refs. 7–9. For a formal definition of these complexity-theoretic notions, we refer the reader to Ref. 10.
Previous work on polynomial-time approximate counting algorithms for classical models have typically followed one of the three
approaches: the correlation decay method,11,12 Markov-chain Monte Carlo,13 or interpolation-type methods.4,14 The latter two of these
J. Math. Phys. 62, 022201 (2021); doi: 10.1063/5.0013689
62, 022201-1
© Author(s) 2021
 30 August 2026 09:11:26
Journal of
Mathematical Physics
methods have also been used to design classical algorithms for quantum models.1,2,9,15–17 The goal of this paper is to convey the simplicity
and flexibility of the third method that results from using the cluster expansion formalism. We emphasize that ideas of this type have previ-
ously been used to establish similar algorithms: for ∣β∣≤(10e2Δ)−1 with quasi-polynomial runtime1 and for ∣β∣≤(16e3Δ)−1 with polynomial
runtime.2 Both the runtime of our algorithm and that of Ref. 2 are polynomials of a relatively high degree; examining our proof gives an upper
bound of O(log(dΔ)) for the degree. While our results represent a modest improvement in the bound for ∣β∣, we view our main contribution
as being the simplicity of our analysis.
We note also that a priori information on the location of zeros of the partition function can be combined with the methods of this
paper to develop polynomial-time algorithms. As noted in Ref. 4, this is an alternate route to the results of Patel and Regts18 using Barvinok’s
method.14 For quasi-polynomial time results of this flavour in the quantum setting, see Ref. 1.
This paper is structured as follows: In Sec. II, we introduce the abstract cluster expansion. Then, in Sec. III, we show how the parti-
tion function of quantum spins systems admits such a cluster expansion. In Sec. IV, we use this framework to establish our approximation
algorithm for the quantum partition function at high temperature. Finally, we conclude in Sec. V with some remarks and open problems.
