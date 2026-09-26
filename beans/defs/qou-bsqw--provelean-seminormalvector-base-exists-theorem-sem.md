---
# qou-bsqw
title: 'PROVE(lean): seminormalVector_base_exists — theorem seminormalVector_base_exists {k : Type} [Field k] [CharZero k] (μ : YoungDiagram)  [cited vershik-kerov1977]'
status: todo
type: task
tags:
    - lean
    - cited-sorry
    - paper-qou
    - infra-blocked
    - cite-vershik-kerov1977
created_at: 2026-08-01T23:31:02Z
updated_at: 2026-08-31T02:53:38Z
parent: qou-k1mq
---

**File:** `QOU/BraidKnot/JucysMurphy.lean` (QOU)  ·  1 cited sorry(s)
**GitHub:** https://github.com/litlfred/qou/blob/claude/cited-sorry-formalization-catalog-2026-08-01/content/quantum-observable-universe/lean/QOU/BraidKnot/JucysMurphy.lean

### `seminormalVector_base_exists`  —  line 850  ·  tier **B** (infra-blocked / open-conjecture)
- **Proposition:** `theorem seminormalVector_base_exists {k : Type} [Field k] [CharZero k] (μ : YoungDiagram) : ∃ T₀ : QOU.BraidKnot.StandardYoungTableau μ, ∃ v : Specht.Mtab (k := k) μ, v ∈ Specht.SpechtSubmodule (k := k) μ ∧ v ≠ 0 ∧ ∀ s : Fin (Specht.nOf μ), (Specht.Mtab.rep μ).asAlgebraHom (jucysMurphy (k := k) (Spe`
- **Cited:** `[vershik-kerov1977]`
  - [vershik-kerov1977] Vershik, Kerov (1977), *Asymptotic theory of characters of the symmetric group* — https://doi.org/10.1007/BF01106153
- **Tractability:** Existence of a nonzero Vershik–Kerov seminormal vector; requires Jucys–Murphy spectral theory, absent from Mathlib.
- **Next step:** Infra-blocked: needs Mathlib theory that does not exist. Track upstream; do not launder via axiom/class.

## Verdict CONFIRMED 2026-08-31 (audit: docs/audits/2026-08-31-individuating-the-fourteen-infra-blocked-verdicts.md)

Individuated with the other thirteen. For THIS item the boilerplate verdict is right: the named
theory is genuinely absent from Mathlib and is genuinely required. Kept as-is.

Recorded because the same verdict was WRONG on several siblings; "confirmed" here means checked,
not merely un-revisited.
