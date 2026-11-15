---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-059-approximated-pure-estimator-p
section_title: "Approximated pure estimator p"
section_number: null
pages: 140-141
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
Let us denote an operator as A(x) in the coordinate space which does not commute
with the Hamiltonian. Just consider the ground state, now we have three Monte Carlo
estimators for the expectation value of A(x). Namely the pure estimator Ap, the
variational estimator Av and mixed estimator Am (Hammond et al. (1994)),
Ap =
R
Ψ0A(x)Ψ0dx
R
Ψ2
0dx
,
(B.43)
Av =
R
ΨTA(x)ΨTdx
R
Ψ2
Tdx
,
(B.44)
Am =
R
Ψ0A(x)ΨTdx
R
Ψ0ΨTdx
.
(B.45)
We deﬁne a function ∆(x) ≡Ψ0(x) −ΨT(x), and rewrite Am and Av by functional
Taylor expansion series in ∆. Now we have
Am = Ap +
Z
dxΨ0[Ap −A(x)]∆+ O(∆2),
(B.46)
Av = Ap + 2
Z
dxΨ0[Ap −A(x)]∆+ O(∆2),
(B.47)
combining them we have
Ap = 2Am −Av + O(∆2) ≈2Am −Av ≡˜Ap.
(B.48)
Eq.(B.48) the approximated estimator ˜Ap provides a better way to evaluate the pure
estimator Ap than just the mixed or the variational estimators, as long as ∆is small.
130
