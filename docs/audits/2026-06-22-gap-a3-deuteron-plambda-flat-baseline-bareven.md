# GAP-A-3 §4 binding-P_λ probe (infra-unblocked): flat baseline + the bar-even constraint is non-trivial

**Date:** 2026-06-22
**Branch:** `claude/binding-delta-lambda-cbnf-probe-2026-06-22`
**Status:** Positive/structural — runs the cbnf §4 probe deferred to an "infra-enabled session"
(pyhecke_native now built). Canonical, no convention re-derivation. No fit; no 7th ansatz; the
underdetermined Δ_λ system is **not** solved.
**Beans:** [`cbnf`](../../.beans/cbnf--categorical-binding-wiring-no-fitting.md) (§4 follow-up), [`pyhk`](../../.beans/pyhk--pyhecke-native-build.md)
**Script:** [`computations/gap_a3_deuteron_plambda_flat_baseline_probe.py`](../../computations/gap_a3_deuteron_plambda_flat_baseline_probe.py)

## Context — the deferred step, now runnable

The per-isotope binding gate is `A(K)·Σ_{λ⊢3A} y_λ χ^λ(β_K) P_λ(K) = −B(K)/m_e`, with `A(K)`
λ-independent (Phase-4 derived) and `P_λ` the open partition projection. The cbnf state-doc
([`2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md`](2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md))
sharpened the non-fit direction to two grounded observations and **deferred the probe** explicitly
for lack of `pyhecke_native` / canonical `χ^λ` (§5 "infra blocker"). That blocker is now **lifted**
(pyhecke_native built this session, bean `pyhk`). This probe runs the §4 step for the deuteron,
canonically: `y_λ` from `wedderburn_jones_markov.y_lambda_at` (q₀ witness hot path), `χ^λ(β_D)` from
`chi_monotone_transfer.chi_all_lambda(atom_braid_word_3A(1,1), 6)` — no Markov-projection re-derivation.

## (i) The flat baseline `P_λ ≡ 1` → `A·tr_M`

Per the Frobenius pairing `tr_M(β_D) = Σ_λ y_λ χ^λ(β_D)`, `P_λ ≡ 1` gives exactly `A(D)·tr_M(β_D)`,
so binding lives in the redistribution `(P_λ−1)` reweighted by `y_λ χ^λ`. Computed (q₀, dps 20):

| quantity | value |
|----------|-------|
| `tr_M(β_D) = Σ_λ y_λ χ^λ(β_D)` | **0.38836** |
| target `−B(D)/m_e` | 4.353 |
| `A(D)` that would make the flat baseline hit the target | **11.21** |

The per-λ flat weights `w_λ = y_λ χ^λ(β_D)` are dominated by the low blocks `(5,1)` (0.190), `(6)`
(0.092), `(4,2)` (0.067), `(3,3)` (0.060); the ≥3-row blocks contribute `≲ 0.01`. So the flat
(mass-side) distribution is concentrated on the 2-row / near-2-row blocks — consistent with the
Schur–Weyl row-count picture (this session's keystone work).

**Next numerical step (bounded):** compare the Phase-4-*derived* `A(D)` (≤2.5% zero-parameter) against
`11.21`. The gap `A_derived·0.38836 − 4.353` is exactly the binding the redistribution `(P_λ−1)` must
carry; if `A_derived ≈ 11.21` the flat baseline already closes the deuteron (P_λ≈1). This needs the
canonical `Vol_hyp(D)` + `A(K)` evaluation and is the immediate follow-up.

## (ii) The bar-even (λ↔λᵀ) admissibility constraint is NON-TRIVIAL

cbnf §4(ii): since `tr_M` is the `P_λ≡1` point and the v9 closure symmetrises `χ^λ` with `χ^{λᵀ}`, any
admissible `P_λ` must be transpose/bar covariant. The structure for `λ ⊢ 6`:

- `p(6) = 11`; self-conjugate `λ=λᵀ`: `{(3,2,1)}` (1); conjugate pairs: 5
  (`(6)↔(1⁶)`, `(5,1)↔(2,1⁴)`, `(4,2)↔(2,2,1,1)`, `(4,1,1)↔(3,1,1,1)`, `(3,3)↔(2,2,2)`).
- ⇒ the **bar-even admissible `P_λ` subspace has dim 6** (of 11). The binding redistribution `(P_λ−1)`
  must lie here — a refute-on-paper filter for any candidate channel.

**New finding (the value-add):** the flat trace distribution `w_λ` is itself **bar-MIXED** — at q₀,
`χ^λ(β_D) ≠ χ^{λᵀ}(β_D)` (max pair asymmetry `|w_λ − w_λᵀ| = 0.189` on `(5,1)↔(2,1⁴)`). So the bar-even
constraint is **not automatically satisfied by the flat baseline**: an admissible `P_λ` must do real
**symmetrising work** to restore `λ↔λᵀ` covariance. This sharpens cbnf §4(ii) from "a filter" to "an
active constraint": `P_λ` is not a small perturbation of `1` in the bar-asymmetric directions — it must
carry an O(1) bar-symmetrising part. (Mechanism: `χ^{λᵀ}(β) = χ^λ(β)|_{q→q⁻¹}` up to framing; the
deuteron braid breaks transpose symmetry at q₀ ≠ 1.)

## Verdict (no fit)

- **Delivered:** the deferred cbnf §4 probe is run canonically; flat baseline `tr_M(β_D)=0.38836`
  computed; the bar-even admissible subspace pinned (dim 6 of 11); and the flat trace shown to be
  **bar-mixed**, so the bar-even constraint is an active O(1) requirement on `P_λ`, not a free filter.
- **Not delivered (and not attempted):** a value for `P_λ` — the system is 1 equation in (≤6 bar-even)
  unknowns, still underdetermined; solving it by choosing `P_λ` is the forbidden fit. This probe
  characterises the admissible subspace + baseline, as cbnf specified.
- **Immediate follow-up:** the `A_derived` vs `11.21` comparison (needs canonical `Vol_hyp(D)`), which
  quantifies how much binding the redistribution must carry.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md`](2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md) — the cbnf state-doc; §4 deferred this probe, §5 the infra blocker now lifted.
- [`2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md) — the six failed Δ_λ ansätze; the gate this respects.
- [`2026-06-20-pyhecke-native-build-unblocked.md`](2026-06-20-pyhecke-native-build-unblocked.md) — the infra unblock that made this runnable.
