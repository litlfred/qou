# Pre-registration: a γγ electron dressed by the weak vertex (owner: "b, then a as fall back")

Bean `qou-a1hh`, PR #7741. Written and pushed **before** any computation below.

## Generator

The weak vertex, from `weakVertex_eq_split` (QOU/QuarkState/WeakVertexLeftProjector.lean), with
P_L = (σ + q⁻¹)/[2] and P_R = 1 − P_L:

  W = σ P_R + σ⁻¹ P_L = q⁻¹(2σ − h)/[2],   h = q − q⁻¹, [2] = q + q⁻¹.

W is not a braid letter: W² = q⁻²·1 (weak-vertex thread, 2026-11-15). It cannot build writhe, so the
form tested is the one that thread says it can realise: **flip the chirality of one crossing of a γγ word.**
Mirror vertex, recorded for the chirality comparison only: W' = σ P_L + σ⁻¹ P_R.

## Family

Electron e_{k,j} = V^k on 3 strands (V = σ₀σ₁⁻¹), with letter j (1 ≤ j ≤ 2k) replaced by W on that
letter's generator, for k = 1 … 6. Each word is also run with W' in place of W, and the two are compared.
Nucleon p = V³, as in `h2_gg_atom`. Reading 3, levels from m = 1, convention D, proton pin, and mpmath
at the dps the reused base code sets (40).

## Tests

- **T1 (electron alone):** reading 3 at levels 1–3 on its own three strands.
- **P1 (prediction from the closed form, `h2_gg_atom/results.md`):** for each e, the hydrogen atom
  V³ ⊗ e passes level 6 iff χ_(3)(e) + χ_(2,1)(V³)·χ_(2,1)(e) ≥ 0, with χ_(2,1)(V³) ≈ 1.99419. Checked
  against the computed (3,3) value for every e; a mismatch is a FAIL of the check.
- **T3 (full H₂):** for each e passing T1, bare H₂ = H ⊗ H (atom 2 "pe" and "ep") at levels 1–12, plus
  bonds V^k at s ∈ {4, 5}, k ≤ 3, as in `h2_gg_atom`.
- **Chirality (reported only):** whether the characters of e (with W) differ from e' (with W').

## Outcomes, fixed now

- **(i)** Some e passes T1, and some H₂ cell passes every level. Report **all** passing (k, j, W/W',
  orientation, bond) and do not choose among them.
- **(ii)** Some e passes T1 but no H₂ cell passes every level.
- **(iii)** No e passes T1. Then (b) in this form gives no electron, and fallback (a) runs next under its
  own pre-registration.

Trace ratios are reported, never used to select. Nothing fitted, selected against data, or wired.
