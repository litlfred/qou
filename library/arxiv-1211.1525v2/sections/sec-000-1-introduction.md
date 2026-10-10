---
doc_id: arxiv-1211.1525v2
doc_title: "PARTIAL TRANSPOSE OF RANDOM QUANTUM STATES: EXACT FORMULAS AND MEANDERS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1211.1525v2.pdf
source_sha256: 51ff1c8f90c025a4
toc_source: outline
doc_brief: "PARTIAL TRANSPOSE OF RANDOM QUANTUM STATES: EXACT FORMULAS AND MEANDERS — We investigate the asymptotic behavior of the empirical eigenvalues distribution of the partial transpose of a random quantum"
---
In this paper, we investigate asymptotic behavior of the empirical eigen-
values distribution of the partial transpose of the random quantum state
(positive semideﬁnite Hermitian matrix of trace one). This problem origi-
nated from the ﬁeld of quantum information theory in relation to detecting
entanglement in a bipartite system. Non-entangled states, called separable
states, are necessarily positive semideﬁnite after partial transpose [Per96],
where the latter property is called Positive Partial Transpose, abbreviated
as PPT. The converse statement is not true except for bipartite states on
C2 ⊗C2 and C2 ⊗C3 [HHH96]. Here, the partial transpose is made by
writing the bipartite matrix as a Kronecker product and transposing each
block. Therefore, the generic eigenvalue distribution of the partial trans-
pose of a random quantum state is interesting and especially the behavior
of the minimal eigenvalue is important.
2010
Mathematics
Subject
Classiﬁcation. 60B20
(Primary)
81P40,
05A15
(Secondary).
Key words and phrases. quantum states, entanglement, random matrices, Wishart ma-
trix, partial transpose, meanders.
1
arXiv:1211.1525v2  [math-ph]  23 Apr 2013
2
MOTOHISA FUKUDA AND PIOTR ´SNIADY
Mathematically, we investigate the following problem. Take three com-
plex vector spaces Cl, Cm and Cn with l, m, n ∈N and deﬁne ρ :=
TrCl |v⟩⟨v| for a uniformly random unit vector |v⟩in the product space
Cl ⊗Cm ⊗Cn. Space Cl is called the environment, space Cm ⊗Cn is called
the system, and individual spaces Cm and Cn correspond to individual parts
of the bipartite system. We will present the details of this construction in
Section 2.3. This way of inducing measure on mixed quantum states was
investigated in [˙ZS01, B˙Z06]. Then, we study the asymptotic behavior of
the eigenvalues of its partial transpose ρΓ where the transpose acts only on
the space Cn.
Although quantum states correspond to positive semideﬁnite Hermitian
matrices of trace one, Aubrun in [Aub12] used the normal Wishart matrix
model to approximate a random quantum state. The trace of such a Wishart
matrix is a random variable which converges to one only asymptotically.
Aubrun showed that the empirical eigenvalues distribution converges to the
semicircular distribution as the dimension of the spaces grow in such a way
that l ∝mn and m ∝n. Later, Banica and Nechita [BN12a, BN12b]
showed with the same model that the limiting distribution is the free differ-
ence of two free Poisson distributions in the regime where the dimension m
of one of the parts of the system is ﬁxed and the dimension l of environment
and the dimension n of the other system grow proportionally.
By contrast, we look into this problem more directly by considering the
matrix ρ :=
1
Tr W W, where W is a Wishart matrix. Since the trace Tr W is
a χ2-random variable, independent from ρ, the problem of calculating mo-
ments of (the partial transpose of) ρ is reduced to calculating appropriate
moments of the Wishart matrix W. This idea was sketched brieﬂy already
by Aubrun [Aub12, Section 8.2]. In this way we obtain exact combinatorial
formulas involving summation over the symmetric group. We ﬁnd three nat-
ural types of geodesics in the Cayley graph of the symmetric group which
yield interesting asymptotic distributions. Two of them correspond to the
above mentioned cases ([Aub12] and [BN12a, BN12b]), and the remaining
new case turns out to be related to the meander polynomials [DFGG97].
Our paper is organized as follows. After explaining necessary mathemati-
cal techniques (in particular, free probability) and our precise mathematical
model in Section 2, we analyze the regime, where l, m, n grow such that
l ∝mn in Section 3. In [Aub12] one requires m ∝n but we drop this con-
dition to get the same limiting measure in Section 3.1, although we need
some weak conditions to show the convergence of extreme eigenvalues and
their large deviation in Sections 3.2 and 3.4. Then, it is shown in Section
PARTIAL TRANSPOSE OF RANDOM QUANTUM STATES
3
1
2
3
4
5
6
FIGURE 1. A graphical representation of a noncrossing par-
tition τ =

{1}, {2, 3, 6}, {4, 5}
	
.
4 that our random matrix model yields the meander polynomials. The con-
nection to free Poisson distribution is presented in Section 5. Section 6
contains the concluding remarks.
