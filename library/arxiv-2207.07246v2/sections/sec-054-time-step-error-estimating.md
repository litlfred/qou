---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-054-time-step-error-estimating
section_title: "Time step error estimating"
section_number: null
pages: 139-141
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 64 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
If all the conﬁgurations are taken from the ﬁnal distribution
f(x) =
ΨTΨ0
R
ΨTΨ0dx,
(B.38)
the expectation value of the local energy EL then becomes
⟨EL⟩=
Z HΨT
ΨT
f(x)dx =
R
Ψ0HΨTdx
R
ΨTΨ0dx
= ⟨Ψ0|H|ΨT⟩
⟨Ψ0|ΨT⟩
= E0.
(B.39)
Clearly, the local energy serves as the estimator for the ground state energy E0, and
⟨EL⟩is called the variational estimator.
However, the Green’s function we use is short-time approximated, so time-step
error is always there. We need to do extrapolation. Just say the local energy ⟨EL⟩,
129
what equation do we use to extrapolate the true E0? A closer look at Eq.(B.18) reveals
that the short-time approximated Green’s function (now call it G′, neglect the constant
ET) to the 3rd order of τ can be written as (by using CBH formula)
G′ = e−1
2 τV e−1
2 τJe−1
2 τJe−1
2 τV = e−τH+ τ3
48 [H−2V,[H,V ]] ≡e−τH′,
(B.40)
compare this G′ with the exact Green’s function G = e−τH, we ﬁnd that
H′ = H + τ 2
48

H −2V, [H, V ]

.
(B.41)
This result seems indicating that EDMC
0
(τ) = E0 +c2τ 2. However, since we are actually
using importance sampling, the linear term still exists (Apaja (2009); Chin (1990)).
So, full second order extrapolation
EDMC
0
(τ) = E0 + c1τ + c2τ 2
(B.42)
should be used. As pointed out in (Apaja (2009)), any extrapolation with higher than
second order must be based on diﬀerent decompositions from Eq.(B.18).
Approximated pure estimator ˜Ap
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
