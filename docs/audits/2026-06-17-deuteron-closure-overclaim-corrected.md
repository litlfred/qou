# Deuteron "closure" overclaim — corrected (the +0.91% via E₀×q⁻¹ is unsubstantiated)

**Date:** 2026-06-17
**Branch:** `claude/deuteron-closure-overclaim-fix-2026-06-17`
**Trigger:** a "fix low-isotope binding / where are closable gaps" survey surfaced
that the corpus claims the deuteron is "the only honestly-closed light nucleus
(+0.91% via E₀×q⁻¹)" (`2026-05-26-delta-lambda-binding-formula-closure.md`,
`docs/coordination/option-e.md`). On verification the claim is **unsubstantiated**.

## The claim
> "The binding energy scale is E₀ = m_e/(q₀(q₀−1)) ≈ 4.186 MeV. The **deuteron**
> binds at +0.91% via E₀×q⁻¹ (single-isotope scale, PR #1367). This is the only
> honestly-closed light nucleus." — `2026-05-26-…closure.md:39-42`, mirrored in
> `option-e.md:31` ("CLOSED (+0.91% via E₀ × q⁻¹) … the only honestly-closed
> light nucleus").

## What every current deuteron compute actually gives (verified 2026-06-17)

| compute | B(D) MeV | vs AME 2.224566 |
|---|--:|--:|
| Σ-formula `m_e·|Σ y_λ χ^λ sgn f^λ|` (`binding_energy_categorical_deuteron.py`) | 0.380 | **−82.9%** |
| `E₀×q⁻¹`, E₀=4.186 (the *stated* formula) | 3.771 | **+69.5%** |
| `E₀×q⁻¹`, E₀=Q_β=0.782 (`E_0_CALIBRATION_MEV`) | 0.705 | −68.3% |
| interface-knot T1+T2 (`binding_via_interface_knot.py`) | 0.977 | −56% |
| interface-knot +T3 (best current) | 1.526 | **−31%** |
| **claimed "+0.91% via E₀×q⁻¹"** | (2.24) | **NOT reproduced by any compute** |

**No production compute reproduces the claimed 2.24 / +0.91%.** The stated formula
`E₀×q⁻¹` gives 3.771 (+69.5%), not 2.24.

## What the "+0.91%" actually was: a single-isotope fit
The corpus's own deuteron compute is **honest about this** — it does not claim a
derivation:

- `binding_energy_categorical_deuteron.py:79` defines `C_knot = B_AME/(m_e·|sum|)`,
  i.e. the back-solved deficit ratio. `:99` states: *"C_knot = 5.852 is the
  **FITTED deficit ratio, not a derived geometric layer**; … the Δ_λ gate remains
  open."* The witness repeats it (`…categorical-deuteron.witness.json:13`).
- `0.380 (Σ-formula) × 5.852 (C_knot) = 2.2246 = AME` **by construction** — a
  1-parameter fit to 1 datum. The "closure" is the bare Σ-formula (−82.9%)
  multiplied by a per-knot constant fitted to AME.

So the deuteron is **not** "honestly closed": it is the (refuted, −82.9%)
Σ-formula rescaled by a fitted single-isotope constant. The "+0.91% via E₀×q⁻¹"
label conflates (a) the canonical scale E₀ (which does not enter), (b) a fitted
C_knot, and (c) an orphaned PR #1367 value no current compute reproduces.

## Corrected status
- The deuteron binding is **NOT closed parameter-free**. The best current
  parameter-free prediction is the interface-knot+T3 = **1.526 MeV, −31%**.
- The Δ_λ binding-assembly gate is **open/blocked** (main `1f08f61a`, 2026-06-17:
  "both remaining Δ_λ directions closed — 𝓑₃-selection has no continuous
  principle, α-cluster fit-blocked"). No light nucleus is honestly closed.
- Per the three-calibration / no-fit discipline, a back-solved per-knot C_knot is
  exactly the kind of single-isotope fit that does not count as a closure.

## Action
Correct the two overclaiming docs to match the compute's own honest statement:
`2026-05-26-delta-lambda-binding-formula-closure.md` (the prose + the D table row)
and `docs/coordination/option-e.md` (the Status row + Reading). No math retracted
beyond the documentation claim — the chirality decomposition, the C_knot honesty
note, and the Δ_λ factor form all stand.
