---
# qou-xapv
title: 'GAP: which Frobenius coproduct does the framework fix (density u in m = |∫(u·ϱ)|)?'
status: todo
type: task
priority: high
created_at: 2026-10-13T17:34:21Z
updated_at: 2026-10-13T17:34:21Z
---

Owner, 2026-10-13: option A2 (keep the antipode, general coproduct). Measured that A2 is already the general form: def:mass-identity has m(ϱ) = ‖∫(u·ϱ)‖ with u = (∫⊗id)Δ(1). MassTraceIdentity.lean proves massIntegrand_eq_leftMul_density, frobeniusForm_massIntegrand and massTrace_eq_functional_hol with no counit hypothesis. The four _of_frobeniusForm_eq_counit theorems are the special case u = 1.

THE OPEN QUESTION. On semisimple H_n(q) = ⊕_λ M_{d_λ}, a Frobenius-compatible Δ is fixed by Δ(1) = Σ_λ c_λ Σ_ij E^λ_ij ⊗ E^λ_ji, so ε = Σ_λ c_λ⁻¹ χ_λ. With ∫ = tr_M = Σ y_λ χ_λ, u = Σ_λ (y_λ/ε_λ) p_λ, so the effective Δ_λ = y_λ/ε_λ. EVERY central invertible u is reachable by choosing ε. A free Δ is therefore a per-block Δ_λ in disguise, which the no-fitting rule forbids.

ADMISSIBLE ANSWERS (derived, not chosen against data):
(a) Δ induced by ∫ itself (ε = tr_M, u = 1): the current state.
(b) Δ induced by the Plancherel trace τ_P(p_λ) ∝ dim_q(λ)·d_λ/[n]_q!: computed in computations/deltalambda/plancherel_density_u_probe.py (PR from claude/frobenius-counit-axiom2-2026-10-13).
(c) a Δ fixed by some other framework principle, not yet identified.

The open part is a structural argument selecting the coproduct. Selecting by agreement with binding data is FORBIDDEN.

ALSO. Under convention D y_(1³) = 0, so tr_M is degenerate on H_n for n ≥ 3. The Frobenius object is then H/rad ≃ TL (proved over CharZero fields, #7768), and u vanishes on three-row blocks.

Do not close until the coproduct is derived (AGENTS §13a).
