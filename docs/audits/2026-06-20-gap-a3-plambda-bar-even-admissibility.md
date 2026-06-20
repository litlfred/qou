# GAP-A-3 P_λ — bar-even (λ↔λᵀ) admissibility narrowing (2026-06-20)

**Status:** audit — formalize-first *narrowing/refutation* result. Advances the
`cbnf` bean's non-fit GAP-A-3 direction
([`2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md`](2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md))
on the now-unblocked `pyhecke_native` infra
([`2026-06-20-pyhecke-native-build-unblocked.md`](2026-06-20-pyhecke-native-build-unblocked.md)).
EXPLORATORY — no production rewire, no new fitted P_λ, no 7th Δ_λ ansatz.

## Background

The two-layer factorisation `Δ_λ(K) = A(K)·P_λ(K)` takes the substrate-derived
per-atom amplitude `A(K)` as known (Phase-4, ≤ 2.5 %) and leaves `P_λ` open.
Since `tr_M(β) = Σ_λ y_λ χ^λ(β)` (Frobenius), `P_λ ≡ 1` recovers `A(K)·tr_M`
exactly, so **P_λ is the per-partition deviation of binding from the flat trace
distribution** `w_λ = y_λ χ^λ(β_K)`.

The prior probe
[`gap_a3_deuteron_p_lambda_channels_probe.py`](../../computations/probes/gap_a3_deuteron_p_lambda_channels_probe.py)
tried five *content channels* for the deuteron P_λ (sl₂/sl₃ Schur–Weyl
multiplicity, sl₂ q-dim, ≤2-row indicator, zero control) and **refuted all four
target-match channels numerically**, pointing to GAP-A-4. It never checked
whether those channels were *admissible* in the first place.

## The admissibility constraint

The bar involution `q ↦ q⁻¹` sends `χ^λ ↦ χ^{λᵀ}`. A binding deviation `P_λ`
realised by a **real, bar-symmetric** categorical map (the archimedean anchor has
`Im q₀ = 0`; CLAUDE.md §"Im(q) at fibre vs observable level") must therefore be
**transpose-invariant**: `P_λ = P_{λᵀ}`. This is a *necessary* structural
condition, independent of any numerical target.

## Probe + findings

[`computations/probes/gap_a3_plambda_bar_even_admissibility_probe.py`](../../computations/probes/gap_a3_plambda_bar_even_admissibility_probe.py)
· witness `computations/probes/gap-a3-plambda-bar-even-admissibility-probe.witness.json`.
At `n = 6` (deuteron, 11 partitions) the transpose orbits are **5 pairs + 1
self-conjugate** `(3,2,1)`.

1. **The refuted content channels are structurally inadmissible.** All four
   (C1–C4) break `P_λ = P_{λᵀ}` on 4 transpose pairs each: they are built from a
   `rows(λ) ≤ k` selector, and row count is *not* transpose-invariant
   (`rows(λᵀ) = columns(λ)`). Their numerical refutation in the prior probe is
   thus *explained by symmetry*, not coincidence — they were never admissible.

2. **The flat substrate weight carries large bar-odd mass.** `w_λ = y_λ χ^λ(β_D)`
   decomposes into a bar-even part and a bar-odd part with **bar-odd ℓ¹ fraction
   ≈ 49.4 %** (bar-even mass 0.426, bar-odd mass 0.417). The unweighted total
   `Σ w_λ = tr_M(β_D) ≈ 0.388` is bar-even (the odd parts cancel pairwise), but
   the *per-partition* weights are far from transpose-symmetric. A bar-even `P_λ`
   annihilates the bar-odd sector, so any binding deviation that would need to
   live there is structurally unreachable.

## What this buys (and the honest caveat)

- **Narrowing (the deliverable).** GAP-A-3 `P_λ` must be a **transpose-invariant
  functional** — of `{λ, λᵀ}`-symmetric statistics (`n(λ)+n(λᵀ)`, symmetric
  hook/content combinations, `|λ ∩ λᵀ|`, …) — and **cannot** be a row-count or
  column-count selector. This rules out the entire content-channel family on
  structural grounds and is the constraint the next admissible ansatz must
  satisfy. It is a refutation + constraint, **not** a new fitted P_λ.

- **Caveat (does not pin P_λ).** Bar-even admissibility is necessary, not
  sufficient: with 6 transpose-orbit budgets and one target equation the
  admissible bar-even `P_λ` is still underdetermined (the same one-equation /
  many-unknowns underdetermination as the ⁴He channel-split probe). This probe
  *narrows* the family; it does not close GAP-A-3. The large (49 %) bar-odd mass
  of `w_λ` is itself a flag worth a follow-up: it means the deuteron's per-λ
  trace structure is markedly transpose-asymmetric, which a fully bar-symmetric
  categorical picture would not predict.

## Infra note

`pyhecke_native` builds in the web sandbox (≈42 s; `pyhk` bean) — the χ^λ cache
`chi-deuteron-h6-at-q0-50dps.witness.json` consumed here was itself produced by
`pyhecke_native::chi_lambda_all_partitions_mpfr`, so the GAP-A-3 χ^λ infra the
`cbnf` bean flagged as blocked is restored. No production code or witnesses were
changed.

## References

- [`2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md`](2026-06-16-categorical-binding-wiring-state-and-no-fit-direction.md) — the `cbnf` non-fit direction.
- [`2026-06-04-gap-a3-brane-tower-level-selection-scope.md`](2026-06-04-gap-a3-brane-tower-level-selection-scope.md) — the content-channel §4 plan.
- `computations/probes/gap_a3_deuteron_p_lambda_channels_probe.py` — the refuted content channels (C1–C5).
- `computations/probes/gap_a3_plambda_bar_even_admissibility_probe.py` — this probe.
