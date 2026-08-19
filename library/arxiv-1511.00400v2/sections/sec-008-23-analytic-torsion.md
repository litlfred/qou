---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗"
section_id: sec-008-23-analytic-torsion
section_title: "Analytic torsion"
section_number: 2.3
pages: 14-15
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties Joan Porti ∗ — This is a survey on Reidemeister torsion for hyperbolic thre e-manifolds of ﬁnite volume."
---
Consider now a smooth compact manifold M and a representation
ρ∶ π1M → SLn(R).
The manifold M has a unique C1-triangulation, so one can view it as a CW-
complex and compute its torsion. Consider the associated ﬂat bund le
Eρ = /tild⟩comb.alt1M × Rn/slash.l⟩ftπ1M, (9)
where π1M acts on the universal covering /tild⟩comb.alt1M by deck transformations and on
Rn via ρ. The space of Eρ-valuated diﬀerential forms is denoted by Ω p(Eρ),
and its de Rham cohomology by H ∗(M ; Eρ). To simplify, we assume that ρ is
acyclic, namely, by de Rham theorem we assume that
H ∗(M ; Eρ) ≅H ∗(M ; ρ) = 0. (10)
We choose a Riemannian metric g on M and a metric µ on the bundle Eρ (notice
that since we do not assume ρ to be orthogonal, perhaps the metric µ cannot
be chosen to be ﬂat). This yields a metric on Ω p(Eρ). Using it, we may deﬁne
the adjoint to the diﬀerential and the Laplacian ∆ p(ρ) on Ω p(Eρ). As it is an
elliptic operator, it has a discrete spectrum 0 < λ0 ≤λ1 ≤⋯ → ∞. The zeta
function is deﬁned on the complex half-plane Re (s) ≥n/slash.l⟩ft2:
ζp(s) = /summ⊗tion.disp
λi
λ−s
i
and it extends to the a meromorphic function on the complex plane, h omomor-
phic at s = 0.
Deﬁnition 2.26. The analytic torsion is deﬁned as:
toran(M, ρ, g, h) = exp /par⟩nl⟩ft.alt21
2
dim M
/summ⊗tion.disp
p=0
(−1)p pζ ′
p(0)/par⟩nright.alt2. (11)
14
In [71] M¨ uller proves that if dim M is odd and, as we assume ρ is acyclic,
then it is independent of g and h. It can also be deﬁned using the trace of the
heat operator:
toran(M, ρ) =
exp ⎛
⎝
1
2
dim M
/summ⊗tion.disp
p=0
(−1)pp d
ds /par⟩nl⟩ft.alt4 1
Γ (s) /integr⊗l.disp
∞
0
/par⟩nl⟩ft.alt1Tr(e−t∆ p(ρ))ts−1d t/par⟩nright.alt1/par⟩nright.alt4/divid⟩s.alt4
s=0
⎞
⎠ . (12)
In the following theorem notice that we use the convention for Reide meister
torsion opposite to the usual in analytic torsion.
Theorem 2.27 ([13, 71]). Let M be a closed hyperbolic manifold of odd dimen-
sion and ρ∶ π1(M ) → SLn(R). Then
toran(M, ρ) = 1
/divid⟩s.alt0tor(M, ρ)/divid⟩s.alt0.
This theorem was ﬁrst proved by Cheeger [13] and M¨ uller [70] independently
for orthogonal representations, and later by M¨ uller [71] for unimodular ones. In
addition, aciclycity of ρ is not required by choosing orthonormal harmonic basis
in cohomology.
This subsection concludes recalling a theorem of Fried. Let ρ∶ π1M → SO(n)
be a representation of a hyperbolic manifold. For s ∈C with Re (s) suﬃciently
large, consider
Rρ(s) = /product.disp
γ
det(Id −ρ(γ)e−s l(γ))
where the product runs over the prime, closed geodesics of M and l(γ) denotes
the length of γ. This is called the Ruelle zeta function.
Theorem 2.28 ([32]). Let M be a closed hyperbolic manifold of odd dimension
and assume that ρ∶ π1M → SO(n) is acyclic. Then R(s) extends meromorphi-
cally to C and
Rρ(0) = toran(M, ρ)2.
This theorem has been extended by Wotzke [104] to other repres entations of
hyperbolic manifolds, see also [72].
