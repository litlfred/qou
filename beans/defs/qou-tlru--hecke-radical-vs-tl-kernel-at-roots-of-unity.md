---
# qou-tlru
title: 'Hecke radical vs TL kernel at roots of unity: first failure (n = 2, q² a primitive cube root)'
status: completed
type: task
priority: normal
created_at: 2026-11-27T17:45:00Z
updated_at: 2026-11-27T18:30:00Z
parent: qou-0cyu
---

Follow-up to `qou-tlrv` (generic equality rad(wtrace) = θ(tlKernelPulled), PR #9488). Carl asked (2026-11-27) what happens at roots of unity and chose "Formalize first failure".

**Proved (PR #9520, `BraidKnotOctonion/TLKernelRootOfUnity.lean`, sorry-free):** if q⁴ + q² + 1 = 0, then on H₃ the q-symmetriser x = a₀a₁a₀ − a₀ (a_i = σ_i + q⁻¹) is in the radical of the Jimbo trace form while ρ(x) ≠ 0 and θx ∉ tlKernelPulled (`not_rad_le_tlKernel_rootOfUnity`). It uses jimboTrace because wtrace needs NotRootOfUnity. Also `jimbo_eq_tlRep_comp`: ρ = tlRep ∘ π ∘ θ for every q ≠ 0.

**Not proved (open, do not close on this):** the exact threshold for general n (literature: failure iff [k]_q = 0 for some 3 ≤ k ≤ n + 2, n generators), and H/rad ≅ semisimple quotient of TL (literature: Jones 1983, Wenzl 1988).

## 2026-11-27 — #9520 merged (95e333a43b)

The first-failure theorem is on main, so this bean is completed. The threshold question is a separate open item and goes on a decision card, not this bean.

## 2026-11-27 — correction and three-strand threshold (PR #9535)

**Correction.** This bean, the #9520 PR body and the merged TLKernelRootOfUnity.lean Scope paragraph gave the general threshold as [k] ≠ 0 for 2 ≤ k ≤ n + 1. That range is one short. The n = 2 Gram determinant is −(q⁴+1)(q⁴+q²+1)⁴/(q²+1)¹⁰, measured in sympy on the explicit 8×8 matrices and proved in Lean via the ε-rescaled basis. So three strands fail at [4] = 0 (q⁴ = −1) as well as at [3] = 0. The docstring is fixed in #9535 and the #9520 body is edited. The thread messages of 17:3x UTC carried the same error, and a correction was posted there.

**Proved (#9535, `TLKernelThresholdThree.rad_eq_tlKernel_iff`, sorry-free):** for q ≠ 0, q² + 1 ≠ 0, rad(jimboTrace) = θ(tlKernelPulled) on H₃ ⟺ (q⁴+q²+1)(q⁴+1) ≠ 0. The witness is [3]·(Jones–Wenzl), with ρ(w) entry 1 for every q.

**Still open:** general n (TL Gram determinant).
