---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-054-72-unitarity-of-the-burau-representation-49
section_title: "Unitarity of the Burau representation 49"
section_number: 7.2
pages: 49-50
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
1. π (β)(q) = (−1)eψ 2(β)(q) = qeψ 2(β−1)(q) (because of row-column symmetry; see Note 4.6).
2. π (β) = (−1)e and π (β) = qe (Note 4.7)
For 4-braids we have:
1. π = −ψ 3. So π (β) = (−1)eψ 3(β). (Note 5.7)
2. π (β)(q) = qeψ 3(β−1)(q) (because of row-column symmetry; see Note 4.6). Also
π = −π ∧ π = −ψ 3 ∧ ψ 3 ,
where wedge denotes antisymmetric product (see p.354 bottom).
3. π (β) = (−1)eψ 2(¯β), where bar denotes the homomorphism from B4 to B3 given by ¯σ1,2,3 = σ1,2,1. (p. 355)
4. π (β) = (−1)e and π (β) = qe (Note 4.7)
Now Squier observes in [Sq], that ψ i(β−1)(q) and ψ i(β)(q−1) are conjugate and so have the same trace. So by the
self-symmetry of π we have tr π (t),tr π (t) ∈ (−t)e/ 2R. Similarly (−t)−e/ 2tr π (t) and (−t)−e/ 2tr π (t) are
conjugate complex numbers. These properties will be important below.
Remark 7.2 Squier uses a different convention for ψ i from Jones. He transposes and changes sign in matrix entries
with odd row-column sum (i.e., conjugates by diag(1,−1,1,−1, . . .)). This, however, does not affect our arguments.
The key point in arguments below is Squier’s result. We write M∗ for the conjugate transposed of a matrix M. (That
is, M∗
i,j = M j,i.)
Theorem 7.2 (Squier [Sq]) For any n ≥ 1 there exists a Hermitian matrix J = J[n+1] and a regular matrix M, such that
with J0 = M∗JM we have ψ ∗
nJ0ψ n = J0.
In particular, J is degenerate or deﬁnite iff J0 is so. Moreover,
Ji,j =



−1 if |i − j| = 1√t + 1/ √t if i = j
0 otherwise
.
It is easy to see that if t = 1, then J is positive deﬁnite. Now deﬁniteness is an open condition, s o for t close to 1, it is
still valid. One can determine when J loses this property.
Proposition 7.1 The Squier form J[n] on Bn degenerates exactly in the n-th roots of unity. In particular, it is positive
deﬁnite exactly when |argt| < 2π/ n.
Proof. Denote by J[n] the form corresponding to n-braids, i.e. the one given by restricting J to the ﬁrst n − 1 rows and
columns. It is not too hard to calculate the determinant of J[n]. By development in the last row,
detJ[n] = (
√
t + 1/
√
t)detJ[n−1] − detJ[n−2] ,
whence
detJ[n] = tn − 1√t − 1/ √t · 1
(√t)n .
50 7 Applications of the representation theory
Then the claim follows easily. To see deﬁniteness use the (positivity of) the principal minor criterion. Sincee±2πi/ n is a
simple zero of detJ[n], the determinant must become negative for |argt| ∈ (2π/ n,4π/ n). Then applying this argument
to all n′ < n shows that J[n] is not positive deﬁnite for |argt| ≥ 2π/ n. ✷
So on the arcs of S1 that connect the primitive n-th root of unity to 1, we have that J is positive deﬁnite. Now if J is
such, it can be written as Q∗Q, and then conjugating ψ i by QM we obtain a U(n − 1)-representation. This means in
particular that all eigenvalues of ψ i have unit norm. We will below derive implications of this cir cumstance for the
link polynomials.
