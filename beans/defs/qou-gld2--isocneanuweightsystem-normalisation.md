---
# qou-gld2
title: 'OWNER DECISION (G2): IsOcneanuWeightSystem single-Z field cannot carry normalised weights'
status: todo
type: task
priority: normal
tags:
    - quark-state
    - schur-weyl
created_at: 2026-11-15T12:00:00Z
updated_at: 2026-11-15T12:00:00Z
parent: qou-qs4c
---

G2 of the qou-qs4c dispatch (2026-11-15).

Proved now:
- `SchurWeyl.JimboGL.jimboTrace_eq_wenzl`: the normalised K-weighted trace of the gl_d Jimbo
  action is wtraceW (wenzlWeight d (q²)), weights s_λ(1,q²,…,q^{2(d−1)}) / [d]_{q²}^{|λ|}.
- `SchurWeyl.JimboGL.qtr_jimbo_blockIdempotent`: Tr(K^{⊗n} ρ(E_λ)) = s_λ(1,q²,…) for the
  block idempotent E_λ (any char-0 field, q not a root of unity).

Not discharged: `QBeta.WenzlWeight.IsOcneanuWeightSystem` asks for one normaliser Z for all
sizes. The normalised weights cannot satisfy it (`SchurWeyl.not_isOcneanuWeightSystem`, d = 2).
The unnormalised ones satisfy it trivially (`isOcneanuWeightSystem_schurPrincipal`). Every
conditional consumer (`ocneanuWeight_eq_zero_iff_of_wenzl`, the conventionD variants) already
has an unconditional twin (`wenzlWeight_eq_zero_iff`, `ocneanuWeight_conventionD_eq_zero_iff`).

Decision for the owner: (A) index Z by size (Z_n = [r]_Q^n), then an instance for the actual
Markov weights is a few lines; (B) delete the class and point consumers at the unconditional
twins; (C) leave it. Default if nothing is said: C.
