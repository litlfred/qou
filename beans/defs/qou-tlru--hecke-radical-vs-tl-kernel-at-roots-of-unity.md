---
# qou-tlru
title: 'Hecke radical vs TL kernel at roots of unity: first failure (n = 2, q² a primitive cube root)'
status: completed
type: task
priority: normal
created_at: 2026-11-27T17:45:00Z
updated_at: 2026-11-27T17:50:00Z
parent: qou-0cyu
---

Follow-up to `qou-tlrv` (generic equality rad(wtrace) = θ(tlKernelPulled), PR #9488). Carl asked (2026-11-27) what happens at roots of unity and chose "Formalize first failure".

**Proved (PR #9520, `BraidKnotOctonion/TLKernelRootOfUnity.lean`, sorry-free):** if q⁴ + q² + 1 = 0, then on H₃ the q-symmetriser x = a₀a₁a₀ − a₀ (a_i = σ_i + q⁻¹) is in the radical of the Jimbo trace form while ρ(x) ≠ 0 and θx ∉ tlKernelPulled (`not_rad_le_tlKernel_rootOfUnity`). It uses jimboTrace because wtrace needs NotRootOfUnity. Also `jimbo_eq_tlRep_comp`: ρ = tlRep ∘ π ∘ θ for every q ≠ 0.

**Not proved (open, do not close on this):** the exact threshold (failure iff [k]_q = 0 for some 2 ≤ k ≤ n + 1), and H/rad ≅ semisimple quotient of TL (literature: Jones 1983, Wenzl 1988).

## 2026-11-27 — #9520 merged (95e333a43b)

The first-failure theorem is on main, so this bean is completed. The threshold question is a separate open item and goes on a decision card, not this bean.
