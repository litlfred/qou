# Form-B α_EM: the three listed premises no longer gate it

**Date:** 2026-11-28 · **Bean:** `qou-myts` (accuracy epic) · **Files:** `computations/scorecard_epistemic_status.py` (label text), `computations/scorecard-epistemic-status.witness.json` (re-run)

## 1. Claim

The scorecard listed Form-B α_EM⁻¹ (−0.365 ppb), and R∞ with it, as *"conditional on ArchimedeanLimit, BlochSuslinUniqueness, BringZeroModeBlochClass"*. On `main`, none of the three gates the value:

| class | status on `main` | artefact |
|---|---|---|
| `ArchimedeanLimit x` | **Proved** for x ∈ (0,1), the only range the α chain uses. It is also proved on (−1, 0] and refuted for x < −1. | `DilogPartAConvergence.archimedeanLimit_Ioo`; `ArchimedeanLimitDomain.lean` ("For the α_EM chain only `x ∈ (0,1)` is used") |
| `BlochSuslinUniqueness D` | The real-line form forces every solution to 0 (`blochSuslinUniqueness_iff`), so it carries no content. The corrected complex form is **proved** for the Bloch–Wigner function (`blochWignerFiveTerm_blochD`, `blochSuslinRigidity_blochD`). | `QOU/Transcendental/MassTheory/BlochSuslinComplex.lean` |
| `BringZeroModeBlochClass` | No instance. It is **expected false**: D(z) = 2/(3π) at algebraic z would put π·D(z) in ℚ, against Zagier's conjectures. It is **not needed**, because 2/(3π) is derived from the tiling and Gauss–Bonnet. | `EmCouplingBringZeroModeBloch.lean` docstring; `EmCouplingBringZeroMode.bringZeroMode_fully_tiling_derived` |

## 2. What stays conditional

The row stays **Conditional**, now on the additive form itself, `prop:em-coupling-bring-zero-mode`:

  1/α = q·[9]_q·[10]_q + 2/(3π) + α·H·(1 − h²α) + Δ₂,  H = [2]_q/(8π),

with Δ₂, the archimedean two-loop term, dropped. The pieces are proved: 2/(3π) from the tiling and Gauss–Bonnet, and the 1-loop factor from `EmFermionLoopFourTopology`. Nothing in the corpus proves that 1/α is their sum, and that is the open premise. The label now says so. No number moves.

## 3. Verification

`python3 computations/scorecard_epistemic_status.py`: 25 rows, 0 failures. The new basis excerpt `theorem bringZeroMode_fully_tiling_derived` occurs in the named Lean file. The counts are unchanged: Conditional 11.

## 4. Follow-ups, not done here

- Several 2026-11-27 probes still say "conditional on the Witten-κ Gram `sorry`". That `sorry` was refuted and removed on 2026-11-20 (`gram_kappa_numerical_value_refuted`), so the wording is stale. The affected probes are `nucleon_split_scale_ratio`, `nucleon_split_two_scale` and `nucleon_split_gibbs_coulomb`. They are owned by other threads and are left as they are.
- The scorecard renderer and `ACCURACY.md` regenerate post-merge.
