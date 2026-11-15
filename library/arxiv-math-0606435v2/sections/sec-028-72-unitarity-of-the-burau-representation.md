---
doc_id: arxiv-math-0606435v2
doc_title: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007"
section_id: sec-028-72-unitarity-of-the-burau-representation
section_title: "Unitarity of the Burau representation"
section_number: 7.2
pages: 48-50
source_pdf: 0606435v2.pdf
source_sha256: 6dddaf838a19f0f5
toc_source: inferred
doc_brief: "arXiv:math/0606435v2 [math.GT] 10 Oct 2007 — We show that 3-braid links with given (non-zero) Alexander or Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Unitarity of the Burau representation
In the following q and t are unit norm complex numbers. We deﬁne arg(eis) := s mod 2π for s ∈R. We continue using
the formalism of Young tableaux, the representations πY and the notations X(q,λ) and WY of the proof of theorem 7.1.
For the Alexander polynomial ∆(we resume the notational convention from before §7.1), as well as for 3- and 4-
braids, the representations πY are given by Burau representations. We note (again, and more explicitly) the following
descriptions of πY in terms of the Burau representation ψn given in [J]. Again the indexing is chosen so that ψn−1
is the reduced (n −1)-dimensional representation of Bn, and by −ρ we denote the direct product of ρ with the parity
representation.
As before, e stands for the exponent sum of a braid β. For 3-braids we have the following properties (with reference
to the explanation in [J]):
7.2
Unitarity of the Burau representation
49
1. π
(β)(q) = (−1)eψ2(β)(q) = qeψ2(β−1)(q) (because of row-column symmetry; see Note 4.6).
2. π (β) = (−1)e and π
(β) = qe (Note 4.7)
For 4-braids we have:
1. π
= −ψ3. So π
(β) = (−1)eψ3(β). (Note 5.7)
2. π
(β)(q) = qeψ3(β−1)(q) (because of row-column symmetry; see Note 4.6). Also
π
= −π
∧π
= −ψ3 ∧ψ3 ,
where wedge denotes antisymmetric product (see p.354 bottom).
3. π
(β) = (−1)eψ2(¯β), where bar denotes the homomorphism from B4 to B3 given by ¯σ1,2,3 = σ1,2,1. (p. 355)
4. π (β) = (−1)e and π
(β) = qe (Note 4.7)
Now Squier observes in [Sq], that ψi(β−1)(q) and ψi(β)(q−1) are conjugate and so have the same trace. So by the
self-symmetry of π
we have tr π
(t),tr π
(t) ∈(−t)e/2R. Similarly (−t)−e/2tr π
(t) and (−t)−e/2tr π
(t) are
conjugate complex numbers. These properties will be important below.
Remark 7.2 Squier uses a different convention for ψi from Jones. He transposes and changes sign in matrix entries
with odd row-column sum (i.e., conjugates by diag(1,−1,1,−1,...)). This, however, does not affect our arguments.
The key point in arguments below is Squier’s result. We write M∗for the conjugate transposed of a matrix M. (That
is, M∗
i,j = M j,i.)
Theorem 7.2 (Squier [Sq]) For any n ≥1 there exists a Hermitian matrix J = J[n+1] and a regular matrix M, such that
with J0 = M∗JM we have ψ∗
nJ0ψn = J0.
In particular, J is degenerate or deﬁnite iff J0 is so. Moreover,
Ji,j =



−1
if |i−j| = 1
√t +1/√t
if i = j
0
otherwise
.
It is easy to see that if t = 1, then J is positive deﬁnite. Now deﬁniteness is an open condition, so for t close to 1, it is
still valid. One can determine when J loses this property.
Proposition 7.1 The Squier form J[n] on Bn degenerates exactly in the n-th roots of unity. In particular, it is positive
deﬁnite exactly when |argt| < 2π/n.
Proof. Denote by J[n] the form corresponding to n-braids, i.e. the one given by restricting J to the ﬁrst n−1 rows and
columns. It is not too hard to calculate the determinant of J[n]. By development in the last row,
detJ[n] = (
√
t +1/
√
t)detJ[n−1] −detJ[n−2] ,
whence
detJ[n] =
tn −1
√t −1/√t ·
1
(√t)n .
50
7
Applications of the representation theory
Then the claim follows easily. To see deﬁniteness use the (positivity of) the principal minor criterion. Since e±2πi/n is a
simple zero of detJ[n], the determinant must become negative for |argt| ∈(2π/n,4π/n). Then applying this argument
to all n′ < n shows that J[n] is not positive deﬁnite for |argt| ≥2π/n.
So on the arcs of S1 that connect the primitive n-th root of unity to 1, we have that J is positive deﬁnite. Now if J is
such, it can be written as Q∗Q, and then conjugating ψi by QM we obtain a U(n −1)-representation. This means in
particular that all eigenvalues of ψi have unit norm. We will below derive implications of this circumstance for the
link polynomials.
