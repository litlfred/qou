---
# qou-k3hh
title: 'q-NS: two conjecture statements weaker than their .md (critical-exponent, ns-counterexample)'
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:40:02Z
updated_at: 2026-08-29T16:40:43Z
---

**Verified** by `docs/audits/2026-08-29-q-ns-conjecture-statement-strength-probe.lean`
(`lean`-direct, exit 0, no `sorryAx` on either witness).

Two carriers state strictly less than their `.md`:

- `p2-critical-exponent.lean` — `enstrophy_diverges : ∀ M, ∃ q ≠ 1, M < enstrophy q`
  omits the `q → 1` limit. Witness `regularAtOne` (`enstrophy q = max q 0`) is the
  identity near `q = 1` — regular there — and inhabits the class.
  Also: `criticalExponent` is unconstrained; the asymptotic `~ |q-1|^{-γ_c}` that
  defines it is never encoded.
- `p5-counterexample.lean` — `ns_counterexample_holds` omits the `t → T*⁻` limit.
  Witness `noSingularityAtT` (`velocityProfile t x = max (-t) 0`, `T* = 1`) tends to
  0 at `T*` — no finite-time singularity — and inhabits the class.

**This is NOT the `qou-hjf4` defect.** That one is vacuity (fields that cannot be
false, discharged by unconditional instances, in `QOU.AlgebraicSubstrate`). These
fields *can* be false and have no instance; they are conditional on the wrong
proposition. A zero-inhabitability detector cannot find them.

**Fix** (proposed in the audit, §"Proposed fix"): add the neighbourhood quantifier
to each field. One line each. **Blast radius nil** — neither class has an instance
anywhere, and `ConditionalCorollaries.lean` binds the same five *names* in the
`QOU.AlgebraicSubstrate` namespace, not these.

`conj:levi-degeneracy` recorded in the same audit as a lesser instance: `leviForm`
and `leviForm_symm` are inert, never related to `degeneracySet`.
