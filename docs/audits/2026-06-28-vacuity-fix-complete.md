# Vacuity-defect fix — COMPLETE (2026-06-28)

All **95 genuine** Lean vacuity defects from the 2026-06-26 triage are fixed
and **compile-verified** against a from-source Lean 4.24.0 + Mathlib build.

## Final audit (full tree, 1777 `.lean`)

| genuine category | before | after |
|---|--:|--:|
| `proof-no-empty-prop-carrier` | 5 | **0** |
| `proof-no-self-assuming-projection` | 55 | **0** |
| `proof-no-placeholder-stub` | 6 | **0** |
| `proof-dependent-conjecture-not-conditional` | — | **0** |

Remaining flags are the **legit** (no-fix) bucket the triage identified, not
fake proofs: 33 `trivial-true` documented shadow-stubs (real formalisation
elsewhere), 14 `false-premise` honest theorems with real proofs, 17
`decide-masking` `native_decide` on concrete finite facts (advisory: prefer
`decide`).

## How

- Built Lean 4.24.0 + Mathlib **from source** (olean cache host was
  policy-blocked) — `~/.elan` + `.lake`, ~3097 mathlib oleans.
- Swarm of high-quality agents over the 31 `.beans/vq*` work-units +
  `vacuity-fix-playbook.md`, each fix compile-verified (`lake build <Module>`
  for library modules, `lake env lean <file>` for content-block siblings) and
  re-audited to 0 before commit.

## Fix patterns used (per playbook)

- **A — derive**: real computations restated and proved — `12!`/`7!` term
  counts, `[2]²·[3]`, geometric-sum/q-integer identities (`geom_sum_mul`),
  `Finset.sum_le_sum` degree bounds, summability via
  `summable_geometric_of_lt_one`, Vieta/Binet–Chebyshev recurrences, gauge
  invariance, β₄ = −½·w₂₂ + `linarith`.
- **B — genuine-formalize via Mathlib**: `Dic₃ := QuaternionGroup 3`
  (order 12), `DihedralGroup.card` (D₆=12), Riemann–Roch/Riemann–Hurwitz
  arithmetic (genus = 4, branch count = 6), FTC antiderivative uniqueness
  (`eq_of_has_deriv_right_eq`), 2×2 transfer matrices (`trace_fin_two`,
  `det_fin_two`), `Set.Finite` via injection, `Function.Perm.prod_eq`,
  `IsEmpty` of an antipattern class.
- **C — name the conditional conjecture**: only where irreducibly abstract
  over opaque carriers — `def name (ctx) : Prop := <statement>`, with the dead
  `claim_*` conclusion fields removed from the carrier (no conclusion re-baked
  in; an instance is the conjecture, none = honest open state). No
  detector-gaming, no `native_decide`, no hardcoded observables.

Several files also had **pre-existing standalone-compile breakage** (orphan
content-siblings never built by CI: missing imports, a false `ring` proof over
ℕ-truncated subtraction, parse bugs) which was repaired so they verify.
