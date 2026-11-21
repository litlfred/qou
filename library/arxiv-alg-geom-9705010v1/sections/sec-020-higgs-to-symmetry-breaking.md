---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-020-higgs-to-symmetry-breaking
section_title: "Higgs to ∞: symmetry breaking"
section_number: null
pages: 29-30
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
This time we ﬁx both the curve E and the mass m, and instead we ﬂow to
the theory whose gauge group is some Levi subgroup G ⊂SU(n). Fix a diagonal
matrix ψ, and consider the ﬂow sending a Higgs bundle (V, ϕ) in our system to
(V, ϕs) where ϕs := ϕ + sψ. (As before we decompose V = ⊕Li and let ψ act
diagonally.
The ﬂow is well-deﬁned only on the n!-sheeted cover of the system
on which this decomposition exists). The physics predicts that the limit of the
SU(n) integrable system as s →∞along this ﬂow should be the G-system, where
G ⊂SU(n) is the centralizer of ψ.
For generic ψ, with distinct eigenvalues, this is clear: After rescaling we have
ϕs ∼ϕ′
s := ψ+ 1
sϕ, so the limiting spectral curve is det(t−ψ) = 0, which consists of
n copies of E meeting at ∞. The Prym is then the product J(E)(n−1), independent
of the initial (V, ϕ). This trivial system corresponds to the Abelian structure group
U(1)n−1 which is the maximal torus of SU(n) and the centralizer of ψ.
In general, ψ will have, say, k distinct eigenvalues with multiplicities n1, . . . , nk,
Σni = n. The centralizer is
G = U(1)k−1 × Πk
i=1SU(ni).
Now the limit of the spectral curves of ϕ′
s is non-reduced, consisting of k compo-
nents, the i-th with multiplicity ni. What we need is the limit of the Jacobians.
This clearly has a factor (up to isogeny) from each component, and by rescaling
around the i-th eigenvalue ψi of ψ (i.e. setting t−ψi = s−1˜t) we see that this factor
30
RON Y. DONAGI
is the Jacobian of the spectral curve
det(˜t −ϕi),
where ϕi is the ni × ni dimensional i-th block of ϕ. The claim is then that this
is one of the SU(ni) spectral curves, i.e. that the residue at ∞of the i-th block
is conjugate to m · diag (1, 1, . . . , 1, 1 −ni).
An equivalent condition is: rank
(ϕi −m) ≤1, and this condition is clearly inherited by any block in ϕ, as required.
