---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-004-25-q-commuting-operators
section_title: "q-commuting operators"
section_number: 2.5
pages: 15-16
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
Throughout the paper, we will consider positive operators A,B satisfying AB =
q2BA for q =eπib2
,|q| = 1.
We will realize the operators using the canonical pair A = e2πbx,B = e2πbp
where p = 1
2πi
d
dx . Then it is well-known that
Proposition 2.22. BothA,B are positive unbounded operators on L2(R) and they
are essentially self-adjoint. The domain for A is given by
DA ={f (x)∈L2(R) : e2πbxf (x)∈L2(R)} (2.39)
and the domain for B is given by the Fourier transform of DA.
Hence we can apply functional calculus and obtain various functions in A and
B. In particular, for any function deﬁned on x> 0∈ R such that|f (x)| = 1, f (A)
will be a unitary operator.
In this paper, we will be using a dense subspace W ⊂L2(R) introduced in
[12, 38].
Deﬁnition 2.23. The dense subspace W⊂ L2(R) is the linear span of functions
of the form
e−αx2+βxP (x), (2.40)
whereα,β ∈ C with Re(α)> 0, and P (x) is a polynomial in x.
Then it is known [38] that W forms a core for both A and B and it is also
stable under Fourier transform. It is obvious that these function s have analytic
continuation to the whole complex plane, and they have rapid decay a long the real
direction. All the operators in the remaining sections will ﬁrst be deﬁ ned on W
and extended by continuity to all of L2(R) or its natural domain if the operator is
unbounded.
15
We will also use the notion
W ˆ⊗W⊂ L2(R× R,dsdt ), (2.41)
where the extra exponent eγst,γ∈ C is allowed.
For convenience, we describe some computations involving A and B, and simi-
larly for the operators ˆA and ˆB with the opposite commutation relations.
Lemma 2.24. For AB = q2BA, ˆA ˆB = q−2 ˆB ˆA, both q−1BA−1 and q ˆB ˆA−1 are
positive self-adjoint operators. By the Baker-Campbell-H ausdorﬀ formula
e2πbxe2πbp =e2πb(x+p)e(2πb)2[x,p]/2 =qe2πb(x+p), (2.42)
we deduce for example
q−1BA−1 =q−1e2πbpe−2πbx =e2πb(p−x). (2.43)
Hence we can describe
(q−1BA−1)ib−1τ =eπiτ 2
Bib−1τA−ib−1τ =e−πiτ 2
A−ib−1τBib−1τ, (2.44)
(q ˆB ˆA−1)ib−1τ =eπiτ 2
ˆA−ib−1τ ˆBib−1τ =e−πiτ 2
ˆBib−1τ ˆA−ib−1τ. (2.45)
Furthermore we have commutation relations of the form
(B⊗ 1)e
i
2πb 2 log A−1⊗log ˆA =e
i
2πb 2 log A−1⊗log ˆA(B⊗ ˆA−1), (2.46)
(1⊗ ˆB)e
i
2πb 2 log A−1⊗log ˆA =e
i
2πb 2 log A−1⊗log ˆA(A⊗ ˆB), (2.47)
and similar variants.
