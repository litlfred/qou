---
# qou-gld2
title: 'OWNER DECISION (G2): IsOcneanuWeightSystem single-Z field cannot carry normalised weights'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - schur-weyl
created_at: 2026-11-15T12:00:00Z
updated_at: 2026-11-15T10:00:00Z
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

## 2026-11-15 — owner ruling: delete the class, then normalise by size

(b) The size-indexed normalisation is proved (#7846): `JimboGL.sum_card_mul_schurPrincipal`, `markov_tr_blockE`
and `normaliser_eq`. Every Markov trace at the level-d parameter has weights s_λ/[d]_{q²}^n, and the
normaliser is forced. It is derived from G1/G2, `heckeProduct` bijectivity and Markov uniqueness; nothing is fitted.

(a) Class deleted (PR on branch claude/delete-ocneanu-weight-class-2026-11-15). Consumers:
- WenzlWeightVanishing: the class, plus ocneanuWeight_eq_zero_iff_of_wenzl,
  conventionD_ocneanuWeight_eq_zero_iff_of_wenzl, conventionD_ocneanuWeight_ne_zero_of_two_rows_of_wenzl,
  isOcneanuWeightSystem_schurPrincipal and not_isOcneanuWeightSystem_const_one. All removed. The unconditional
  twins are SchurWeyl.wenzlWeight_eq_zero_iff, SchurWeyl.ocneanuWeight_conventionD_eq_zero_iff and
  OcneanuWeightTwoRowNonzero.ocneanuWeight_conventionD_ne_zero_of_two_rows.
- QBeta/VanishingSetUnderdetermines.lean: deleted. Every theorem in it was about the class.
- SchurWeyl/OcneanuWeightSystemScope.lean: deleted. not_isOcneanuWeightSystem was the evidence for the ruling.
- 6 files carried prose mentions; they are updated.
- No imports, content blocks, witnesses or Python code used the class.
