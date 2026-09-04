---
doc_id: arxiv-1508.05448v1
doc_title: "Concentration of Measure Techniques and Applications"
section_id: sec-010-36-remarks
section_title: "Remarks"
section_number: 3.6
pages: 55-59
source_pdf: 1508.05448v1.pdf
source_sha256: 57d2c717d8ec74d0
doc_brief: "Concentration of Measure Techniques and Applications — 23 sections: Biographical Sketch; Acknowledgments; Abstract"
---
By generalizing this method introduced by Chatterjee and Ledoux, we are able to
show concentration of measure of the empirical spectral distribution not only for
operator compressions via SO(n) but also for operators that are ”compressed” by
conjugation with a Gaussian matrix. It is likely that this method could be applied
to a much wider range of Markov chains, given that the chain does not change too
47
many entries at once, has an appropriate invariant distribution, and for which the
spectral gap is known. It is possible that better bounds for the Gaussian compression
could be obtained by adapting the method to use the ”second” spectral gap or the
exponential decay rate in relative entropy found in [Bonetto et al., 2014].
It is worth noting that Talagrand’s isoperimetric inequality [Talagrand, 1995] gives
concentration of measure for the length of the longest increasing subsequence for ran-
dom permutations, but it cannot be used in the context of this ASEP random walk,
as it requires independence. Using Chatterjee and Ledoux’s method, independence is
not needed. We only need a spectral gap bound for the Markov chain.
48
4 Mixed Matrix Moments and
Eigenvector Overlap Functions
of the Ginibre Ensemble
The purpose of this section is to make some observations about the mixed matrix
moments for non-Hermitian random matrices. The results in this chapter can be
found in [Walters and Starr, 2015]. Let Mat n(C) denote the set of n×n matrices
with complex entries. We use this notation here because we will useMn for something
else later.
The model we will focus on most is the complex Ginibre ensemble, given by
An∈ Matn(C), A n = (an(j,k ))n
j,k=1, a n(j,k ) = X(j,k ) +iY (j,k )√
2n , (4.1)
where (X(j,k ))∞
j,k=1, (Y (j,k ))∞
j,k=1 are IID,N (0, 1) real random variables.
Much of what we will say has already been explored by Chalker and Mehlig in a
pair of papers [Chalker and Mehlig, 1998; Mehlig and Chalker, 2000], in particular,
in their deﬁnition of expected overlap functions. There are other models of inter-
est which were explored by Fyodorov and coauthors [Fyodorov and Mehlig, 2002;
Fyodorov and Sommers, 2003], for which one can obtain more explicit formulas for
the expected overlap functions. Our main emphasis will be to relate Chalker and
Mehlig’s formulas for the overlap functions of the complex Ginibre ensemble to the
49
mixed matrix moments.
Our motivation in considering this problem is the following. There is a rough anal-
ogy between mean-ﬁeld spin glasses and random matrices, as far as the mathematical
methods are concerned. We indicate this in the table in Figure 4.1. We will give more
details and references in a later discussion, but we would like to point out some of
the analogies now. This analogy leads to a method to calculate moments, but there
is still the question about how to relate the moments to the spectral information for
the matrix.
Random Matrices Spin Glasses
expectations of moments expectations of products of overlaps
recurrence relation for moments stochastic stability equations: Ghirlanda-Guerra identities
formula for Stieltjes transform of limiting law proof of Parisi’s ultrametric ansatz
Figure 4.1: Some analogous elements in random matrix and spin glass theory. (Proofs may diﬀer
considerably.)
Although the main subject of this subject is random matrices, we will give a very
brief introduction to spin glasses, just to motivate our analogy. Spin glasses are phys-
ical objects. We will not say much about the physics behind them, as the subject of
this paper is mathematics. However, we will give a quote from Daniel Mattis’s book
[Mattis, 2004] in his discussion of dilute magnetic alloys. He says :
”If the impurity atom does possess a magnetic moment this polarizes the conduction
electrons in its vicinity by means of the exchange interaction and thereby inﬂuences
the spin orientation of a second magnetic atom at some distance. Owing to quantum
oscillations in the conduction electrons spin polarization the resulting eﬀective inter-
action between two magnetic impurities at some distance apart can be ferromagnetic
(tending to align their spins) or antiferromagnetic (tending to align them in opposite
directions). Thus a given magnetic impurity is subject to a variety of ferromagnetic
50
and antiferromagnetic interactions with the various neighboring impurities. What is
the state of lowest energy of such a system? This is the topic of an active ﬁeld of
studies entitled spin glasses, the magnetic analog to an amorphous solid.” [Mattis,
2004] (p. 48)
Since this is a mathematics paper, we will consider a spin glass as a probabilistic
model. We can consider a system
ΣN ={−1, 1}N
for a large integer n. We call an element σ∈ Σn a conﬁguration. The components of
σ are called spins (and can each take the value either ±1). The energy of the system
in a conﬁgurationσ is called the Hamiltonian, which is usually denotedHN(σ). Given
a parameter β (the inverse temperature), we can deﬁne the Gibbs measure by
GN({σ}) = exp(−βHN(σ))
ZN
whereZN is a normalizing factor, called the partition function. The Gibbs measure is
a probability measure which represents the probability of observing the conﬁguration
σ after the system has reached equilibrium in a heat bath at temperature 1/β. HN(σ)
relates to the interactions between the spins. In the models that are often consid-
ered, the HN(σ) are random variables. For a given HN(σ), the main problem is to
understand the Gibbs measure. See [Talagrand, 2003] for a more in depth discussion
of the probabilistic aspect of spin glasses.
We will depart from our discussion of spin glasses now, to begin the discussion
of random matrices. The analogies between the two topics will be discussed more in
depth later.
