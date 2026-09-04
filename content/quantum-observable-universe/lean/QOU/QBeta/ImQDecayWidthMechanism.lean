/-
# A width from `1/E` and a width from `Im E` are different mechanisms — and the framework uses the first

Bean `qou-c66b` (`conj:im-q-physical-role`), candidate (iii), companion to the
probe `imq_decay_width_mechanism_probe`. Third and last of the three, after
`ImQRealityLocus` (candidate (ii), PR #6639) and `ImQChiralityIsBarInvolution`
(candidate (i), PR #6667).

## What candidate (iii) says

> The Hoefsmit seminormal Hecke representation has real-coefficient matrices for
> `q > 0` real, giving **unitary** `H_n(q)` representations. For complex `q`
> with `|q| ≠ 1`, unitarity breaks … In quantum mechanics, non-Hermitian
> operators arise in **open systems** (decay, dissipation, resonance widths).

with the stated obstacle: *"(iii) needs a categorical formula for decay widths
`Γ`."*

## Its premise is correct

`hecke_spectrum_real_iff` below. The Hecke generator satisfies
`(σ − q)(σ + q⁻¹) = 0`, so its spectrum is `{q, −q⁻¹}`, and in real coordinates
`Im(−q⁻¹) = y/(x² + y²)` — which vanishes exactly where `y` does and contributes
**no additional** reality locus. So `Im q ≠ 0` really is precisely the
non-Hermitian deformation candidate (iii) describes. That half is not in
dispute.

## The stated obstacle is not the live one

`docs/canonical-derivation-cheat-sheet.md`, lines 134 and 490: **`𝔇_β`, the
neutron β-decay width, IS CAL-2** — one of the three calibration inputs — and
`Q_β = ℏ/𝔇_β` has the closed form `m_e·|q₀² − 2q₀ − 1|(q₀ + 1)/(2q₀³)` in real
`q₀`. The framework's decay sector is not a gap awaiting a categorical formula;
it is a calibration, and it is real.

## The two mechanisms

| | width from | needs |
|---|---|---|
| **A**, the framework's | `𝔇 = ℏ/Q`, `Q` real — the **reciprocal** of a real energy | nothing complex |
| **B**, candidate (iii)'s | `E = E₀ − iΓ/2` — the **imaginary part** of an eigenvalue | a non-Hermitian generator, hence complex `q` |

`two_width_mechanisms_are_independent` is the finding: on a **real** spectrum, B
gives `Γ = 0` identically while A gives a nonzero width. Measured, the framework
sits in exactly that configuration — `Q_β = 0.783645827374621213` MeV at
`Im q₀ = 0`, so `𝔇_β = ℏ/Q_β = 8.39935509011e-22 ≠ 0`. These are not two
descriptions of one thing.

## Scope — (a), and the Lean says so

`imaginary_mechanism_does_produce_a_width` is deliberately included: mechanism B
works perfectly well when `Im E ≠ 0`. So **nothing here excludes `Im q` from
encoding a resonance width.** What is shown is that the framework's *existing*
decay sector does not need it, which **relocates** the burden: to keep candidate
(iii) alive one must exhibit a `Γ` — for W, Z, top, or a hadronic resonance —
that mechanism A demonstrably **fails** to produce. That is a sharper and more
answerable question than the conjecture's own, and it is left open.

`AGENTS.md` §7b item 3 is where a second discharge would be owed: it gives the
corpus another real-`q` account of exactly the states (iii) names — unstable
intermediaries as **Demazure sub-crystals**, reproducing a short-lived state
*"without ad-hoc decay machinery"*. Not verified numerically here.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp

namespace QOU.QBeta

/-- **The second Hecke eigenvalue adds no reality locus.** For `q = x + iy` with
`|q|² = s ≠ 0`, the generator's spectrum is `{q, −q⁻¹}` and
`Im(−q⁻¹) = y/s`. That vanishes exactly where `y` does — so requiring the whole
spectrum real is requiring `Im q = 0`, no more and no less.

This is candidate (iii)'s unitarity premise, and it is **correct**. -/
theorem hecke_second_eigenvalue_reality_locus {y s : ℝ} (hs : s ≠ 0) :
    y / s = 0 ↔ y = 0 := div_eq_zero_iff.trans (by simp [hs])

/-- **The Hecke spectrum is real iff `Im q = 0`.** Both eigenvalue imaginary
parts — `y` and `y/s` — vanish together, by the lemma above. -/
theorem hecke_spectrum_real_iff {x y : ℝ} (hq : x ^ 2 + y ^ 2 ≠ 0) :
    (y = 0 ∧ y / (x ^ 2 + y ^ 2) = 0) ↔ y = 0 := by
  constructor
  · exact fun h => h.1
  · intro h
    exact ⟨h, (hecke_second_eigenvalue_reality_locus hq).mpr h⟩

/-- **Mechanism A — a width from a reciprocal real energy.** `𝔇 = ℏ/Q` is
nonzero whenever `ℏ` and `Q` are, and needs nothing complex. This is what the
framework does: `𝔇_β = ℏ/Q_β` with `Q_β` real at real `q₀`. -/
theorem reciprocal_width_ne_zero {hbar Q : ℝ} (hh : hbar ≠ 0) (hQ : Q ≠ 0) :
    hbar / Q ≠ 0 := div_ne_zero hh hQ

/-- **Mechanism B on a real spectrum gives exactly zero.** With
`E = E₀ − iΓ/2` the width is `Γ = −2·Im E`, so a real spectrum forces `Γ = 0` —
not approximately, identically. -/
theorem imaginary_width_zero_of_real_spectrum {imE : ℝ} (h : imE = 0) :
    -2 * imE = 0 := by simp [h]

/-- **Mechanism B is not broken — it simply is not what the framework uses.**
Included so the scope of this file is legible from the Lean alone: when
`Im E ≠ 0` mechanism B produces a perfectly good width. Nothing here excludes
`Im q` from encoding one. -/
theorem imaginary_mechanism_does_produce_a_width {imE : ℝ} (h : imE ≠ 0) :
    -2 * imE ≠ 0 := by
  simpa using h

/-- **The finding.** On a real spectrum the two mechanisms disagree completely:
A is nonzero, B is identically zero. So they are independent, and the
framework's decay width — obtained at real `q₀` — is a reciprocal real energy
rather than an imaginary one.

Scope **(a)**: this relocates candidate (iii)'s burden onto exhibiting a `Γ`
that mechanism A fails to produce; it does not exclude `Im q`. -/
theorem two_width_mechanisms_are_independent {hbar Q imE : ℝ}
    (hh : hbar ≠ 0) (hQ : Q ≠ 0) (hreal : imE = 0) :
    hbar / Q ≠ 0 ∧ -2 * imE = 0 :=
  ⟨reciprocal_width_ne_zero hh hQ, imaginary_width_zero_of_real_spectrum hreal⟩

end QOU.QBeta
