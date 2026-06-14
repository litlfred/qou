---
id: q-clt-jsj-mass-scaling
title: "Remark: q-CLT / JSJ Volume Scaling for Heavy Isotopes"
---
# q-CLT / JSJ Volume Scaling for Heavy Isotopes

When modeling the macroscopic atomic mass of heavy isotopes up to Oganesson ($A=294$), evaluating the absolute topological Hecke trace of the $A$-nucleon knot becomes computationally intractable. The Jaco–Shalen–Johannson (JSJ) decomposition glues the atomic knot complement along essential (inter-nucleon) tori, and hyperbolic volume is additive under torus gluing. The *leading* mass term is therefore volume-additive — linear in the nucleon counts:

$$
\mathfrak{m}_{\text{qCLT,lead}}(Z, N) = Z\,\mathfrak{m}_{\mathfrak{p}} + N\,\mathfrak{m}_{\mathfrak{n}}.
$$

Accordingly we partition the absolute mass prediction into two computational channels:

1. **`m_symbolic`**: the exact closed-form evaluation of the Hecke matrix traces, computationally constrained to light isotopes ($A \le 8$).
2. **`m_qCLT_approx`**: the JSJ-additive estimator $Z\,\mathfrak{m}_{\mathfrak{p}} + N\,\mathfrak{m}_{\mathfrak{n}} - B(Z,N)$, where $B$ is the binding energy (the $\Delta_\lambda$ correction).

The additive **structure** is exact: the inter-nucleon tori make the volume — hence the leading mass term — linear in $(Z,N)$. The *absolute* prediction is gated by two residuals: the binding fraction $B/\mathfrak{m}$ (which plateaus near $0.9\%$ under nuclear saturation, so it does **not** vanish for heavy $A$) and the nucleon-mass gap. The nucleon-mass gap is $+2.89\%$ in the *proved* pipeline (the production linking weight); the derived, no-fit spectral-phase correction $\theta/(8\hbar_q^2)\approx 0.9711$ reduces it $\sim 35\times$ to $-819$ ppm, but is **exploratory and not yet wired** (its "why $\theta/(8\hbar_q^2)$" step is an unproved Lean stub). Validated on the three light compound nuclei where $B$ is available (D, T, ³He), the binding-corrected channel reproduces the CODATA atomic mass to within the nucleon-mass gap, *uniformly* across isotopes — production residual $\approx 2.89\%$ (cross-isotope spread $0.014\%$), spectral residual $\approx -800$ ppm. The uniformity is the signature that the additive structure is sound; the asymptotic claim is about the linear **structure**, not absolute exactness. See the computational witness `m-qclt-approx.witness.json`.
