---
doc_id: arxiv-1512.04993v2
doc_title: "Complexity, action, and black holes"
section_id: sec-003-22-bounds-on-information-scrambling-or-chaos
section_title: "Bounds on information scrambling or chaos"
section_number: 2.2
pages: 10-11
source_pdf: 1512.04993v2.pdf
source_sha256: b8047bc3d3815406
doc_brief: "Complexity, action, and black holes — Our earlier paper “Complexity Equals Action” conjectured that the quantum computational complexity of a holographic state is given by the classical action of a"
---
For a system with N degrees of freedom, the scrambling time t∗ is a measure of how
long it takes for information about a small O(1) perturbation to spread over O(N)
degrees of freedom [21]. Another useful deﬁnition [22] is that this is the time required
for reduced density matrix of any subsystem with fewer than half the degrees of freedom
to look approximately thermal. 3
Black holes are the fastest scramblers in nature [21,23,24]. There are two senses in
which this is true:
First, for a system arranged on a d-dimensional lattice, the scrambling time can be
no faster thant∗∼N 1/d, whered is the number of spatial dimensions of the system [21].
N 1/d is proportional to the system’s linear dimensions and implies that the scrambling
is ballistic. It was conjectured [21, 23] (see also [25]) and then shown [26] that the
scrambling time for black holes in AdS is given by
t∗∼β logN. (2.4)
For black holes the dimensionality of the lattice d is eﬀectively inﬁnite.
Second, not only are black holes the fastest scramblers because the scrambling time
is logarithmic in N, they also have the smallest possible coeﬃcient in front of the
logarithm
t∗ =λ−1
L logN, (2.5)
where the rate of scrambling can be interpreted in terms of chaos as a Lyapunov
exponent λL [24,27]. A useful measure of the strength of chaos is given by the out-of-
time-order four-point correlator [28]
⟨W (t)V W(t)V⟩β, (2.6)
where⟨·⟩β is the thermal expectation value, W and V are simple local Hermitian
operators, and W (t)≡ eiHtWe−iHt. In chaotic systems, this correlation function will
exhibit chaotic Lyapunov behavior (the butterﬂy eﬀect) and initially decay as [24,27,28]
⟨W (t)V W(t)V⟩β =f0−f1eλL(t−t∗) +O(N−2), (2.7)
3In general, this concept is only useful for systems described by k-local Hamiltonian with k≪N.
For more discussion, see Appendix A.1
9
with O(1) constants f0,f 1. Quantum mechanics puts a bound on this exponent [24]
λL≤ 2πkBT
ℏ , (2.8)
and black holes saturate this bound [7,26,27,29,30].
