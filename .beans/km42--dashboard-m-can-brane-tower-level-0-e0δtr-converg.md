---
# km42
title: 'Dashboard m_can brane tower: level-0 E0·Δtr + convergent higher orders (fix divergent impl)'
status: todo
type: task
created_at: 2026-06-28T21:14:46Z
updated_at: 2026-06-29T20:30:00Z
---

## SCOPE (2026-06-29) — GATED, do not naively "fix"

The "divergent impl" is the **owner-gated T2/T3 brane-tower trace-invariance pathology**, not a
clean dashboard bug. T1 (level-0 `E0·Δtr`, `|tr_M|`) is the convergent canonical part; the
higher-order brane-tower terms (T2/T3) **diverge at q₀** because archimedean `Φ_q` is not
Markov-invariant (~10⁵× amplification; T−³He ≈ −737 MeV). All brane-tower compute is in
`computations/_deprecated/`.

Making the higher orders "convergent" = the **open trace-invariant reformulation / `α_M`
substrate derivation** — the binding-closure frontier (`z2bn`/`w5tg`/`thb7`), under the standing
"do not wire pathological Φ_q T2/T3" directive (`adhb` / PR #2846) and the Subgoal-2 decline
(2026-05-08; narrow s5-so3 reversal only). **Needs explicit owner sign-off.**

Only non-gated slice = a *display-only* robustness fix (show T1, label higher orders as
"divergent/gated"); optional, not the underlying fix. Full scoping:
`docs/audits/2026-06-29-km42-mcan-tower-scoping.md`. Keep parked unless owner re-scopes.

