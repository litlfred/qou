---
# qou-ogrk
title: 'A2 (leg 1): prove Cov_Planch(ln f, omega3) <= 0 via Ivanov-Olshanski 2nd-order covariance'
status: todo
type: task
priority: high
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T03:31:40Z
parent: qou-v8t7
---

## A2 — leg 1: Cov_Planch(ln f, ω₃) ≤ 0 (the leading / m=1 term)
IDEA. ω₃=Σc²−C(n,2) is the Σ_2 central character — a polynomial function of the diagram (in the
Ivanov-Olshanski algebra A). ln f = ln n! − Σ_□ ln h is the Kerov "log-dimension" functional; it is
NOT in A but has a known expansion in the Σ_μ basis. The Plancherel 2nd-order covariances Cov(Σ_i,Σ_j)
are EXACT (Ivanov-Olshanski). So Cov(ln f, ω₃) = Σ_j c_j Cov(Σ_j, Σ_2) with c_j the ln-dim expansion
coeffs — a computable combination whose sign we need ≤ 0.
FIRST STEP. Read uploads/0304010v1.pdf §6-8 (CLT characters / Young diagrams / transition measures) +
§10 (free cumulants, Biane). Extract the covariance formula Cov_Planch(Σ_2,Σ_j) and the ln-dim
expansion. Assemble Cov(ln f,ω₃); check sign vs numerics (Cov<0 all n≤19).
SUCCESS. Closed-form sign Cov(ln f,ω₃) < 0 (proves leg 1).
KILL. Genuinely sign-indefinite — but numerics say <0 for all n, so this leg looks the more tractable.
This is the more promising of the two sufficient legs.
