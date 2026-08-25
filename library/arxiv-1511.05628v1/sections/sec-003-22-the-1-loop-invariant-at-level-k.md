---
doc_id: arxiv-1511.05628v1
doc_title: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY"
section_id: sec-003-22-the-1-loop-invariant-at-level-k
section_title: "The 1-loop invariant at level k"
section_number: 2.2
pages: 6-8
source_pdf: 1511.05628v1.pdf
source_sha256: 3b9da2994233882b
doc_brief: "QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY — The Quantum Modularity Conjecture of Zagier predicts the existence of a for- mal power series with arithmetically interesting coeﬃcients that"
---
and a positive integer k. We use the notation of the previous section. For m∈ (Z/kZ)N, we
deﬁne
(10) am(θ) =e−iπm·B−1Amζ
1
2
[
m·B−1Am+m·B−1ν
] N∏
i=1
θ−(B−1Am)i
i
(ζθ−1
i ;ζ)mi
.
We also recall the cyclic quantum dilogarithm deﬁned by
(11) Dk(x) =
k−1∏
s=1
(1−ζsx)s D∗
k(x) =
k−1∏
s=1
(1−ζ−sx)s.
This function appears in [KMS93, Eqn.C.3] and [Kas99, Eqn.2.30].
Deﬁnition 2.1. With the above assumptions, the level k 1-loop invariant of γ is
(12) τγ,k := 1
kN/2
√
det(A∆′′
z + B∆−1
z )zf′′/kz′′−f/k
N∏
i=1
D∗
k(θ−1
i )1/k
∑
m∈(Z/kZ)N
am(θ),
where ∆z = diag(z1,...,z N) and ∆z′′ = diag(z′′
1,...,z ′′
N) are diagonal matrices.
Note that τγ,k depends on the Neumann-Zagier datum γ, the k-th root of unity ζ but also
on the choice of k-th roots θi of zi. The next theorem implies that τ 2k
γ,k depends only on γ
andζ, and therefore that τγ,k is well deﬁned modulo multiplication by a 2k-th root of unity.
The proof (given in Section 3) follows from results of Zagier and the second author [GZ]
via a a comparison of an arithmetic to a geometric mean over the Galois group of FG,k/Fk,
reminiscent of Hilbert’s theorem 90.
Theorem 2.2. We have τ 2k
γ,k∈Fk.
Remark 2.3. It is easy to see that τ 2k
k /τ 2k
1 is an S-unit of the ring of integers of Fk where
S =⟨z, 1−z⟩⊂ F∗
K. For an illustration, see Section 6.
Remark 2.4. After replacing ζ by ζ−1, We can give an alternative formula for the 1-loop
invariant at levelk as follows:
(13) τγ,k := 1
kN/2
√
det(−A∆′′
z− B∆−1
z )zf′′/kz′′−f/k
N∏
i=1
z
k−1
2k
i (z′′
i )
k−1
k
Dk(ζ−1θi)1/k
∑
m∈(Z/kZ)N
bm(θ),
where
(14) bm(θ) =eiπL·mζ− 1
2
[
mTQm+L·m
] N∏
i=1
θQi·m
i
(ζ−1θi;ζ−1)mi
and
(15) L =−B−1ν + (1,..., 1)T, Q =I− B−1A.
QUANTUM MODULARITY AND COMPLEX CHERN-SIMONS THEORY 7
2.3. The n-loop invariants at level k for n ≥ 2. The deﬁnition of the higher-loop
invariantsSγ,n,k is motivated by perturbation theory of the state-integral model for complex
Chern-Simons theory, reviewed brieﬂy in Section 4. In this section we deﬁne the higher-loop
invariants using formal Gaussian integration, and in the next section we give a Feynman
diagram formulation of the higher-loop invariants.
Fix a Z-non-degenerate Neumann-Zagier datum γ and a positive integer k. We will use
the notation of the previous section. If f : (Z/kZ)N−→ C, we deﬁne
(16) Av( f) =
∑
m∈(Z/kZ)Nam(θ)f(m)∑
m∈(Z/kZ)Nam(θ) ,
assuming that the denominator is nonzero. Consider the symmetric matrix
(17) H = 1
k(−B−1A + ∆z′),
where ∆z′ = diag(z′
1,...,z ′
N). Assuming that H is invertible, a formal power series fℏ(x)∈
Q(z)[ [x, ℏ
1
2 ] ] has aformal Gaussian integration, given by
(18) ⟨fℏ(x)⟩ =
∫
dxe− 1
2xTHxfℏ(x)∫
dxe− 1
2xTHx .
This integration, which is a standard tool of perturbation theory in physics, and may be
found in numerous texts (e.g. [BIZ80]) is deﬁned by expanding fℏ(x) as a series in x, and
then formally integrating each monomial, using the quadratic formH−1 to contractx-indices
pairwise.
The building block of each tetrahedron is the power series
(19) ψℏ(x,θ,m ) = exp
( ∞∑
n=1
∞∑
j=0
ℏn−1(−1)j
n!j!kj
k∑
s=1
Bn
(s
k
)
Li2−n−j(ζm+sθ−1)xj
)
For an ideal triangulationT withN tetrahedra, a natural number k, and m∈ (Z/kZ)N, we
deﬁne
(20) fT,ℏ(x;θ,m ) = exp
(
− ℏ
1
2
2kxTB−1ν + ℏ
8kfTB−1ν
) N∏
i=1
ψℏ(xi,θi,mi)
Deﬁnition 2.5. We deﬁne
(21) φ+
γ,ζ(ℏ) = Av(⟨fT,ℏ(x;θ,m )⟩)∈ 1 + ℏC[ [ℏ] ].
Thus, we can write
(22) φ+
γ,ζ(ℏ) = exp
( ∞∑
n=1
Sγ,n+1,kℏn
)
.
We callSγ,n,k the level k, n-loop invariant of γ. We ﬁnally deﬁne
(23) φγ,ζ(ℏ) =τγ,ζφ+
γ,ζ(ℏ).
Theorem 2.6. The coeﬃcients of the power series φ+
γ,ζ(ℏ) are in Fk.
8 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
In particular, the seriesφ+
γ,ζ(ℏ) depends onγ, thek-th root of unityζ, but it is independent
of the choice ofk-th rootsθi ofzi. The above theorem is not trivial since am(θ) is an element
of the larger ﬁeld FG,k, whereas the coeﬃcients of the above average are claimed to be in the
ﬁeld Fk. For the proof, see Section 3.
Remark 2.7. Theorems 2.2 and 2.6 remain valid if ζ denotes a ﬁxed primitive k-th root of
unity instead of ζ = e2πi/k. Probably a better notation is Sγ,n,ζ rather than Sγ,n,k which is
valid for all primitive k-roots of unity ζ.
