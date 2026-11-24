/-
  The bar-odd observable's normalization: complex volume `𝔙` (κ_pot = √3/4) vs
  full Neumann–Zagier potential `Φ = ∫₀ᵘ log(−L) dt` (κ_shape = √3/2). The
  STRUCTURAL identification of the two coefficients of the qou-yh67 binary with
  two genuinely-different geometric objects — `Φ = 2·𝔙` (the NZ ½).

  CONTEXT (bean qou-yh67; companion to
  `QOU/QBeta/BoostFactorNZNormalization.lean` (#4541), which proves
  `κ_shape = 2·κ_pot` and the conditional boost identity `c = √2`).

  #4541 reduced the opaque boost factor `c ≈ 1.4305` (`A ≈ 2.054`) to one binary:
  does the bar-odd leak `S = Q_β/E₀` carry `κ_shape = √3/2` (⇒ `A = 2`, `c = √2`)
  or `κ_pot = √3/4` (⇒ `A = 1`)? #4541 stopped there — the number is at the
  precision ceiling (σ_A ≈ 40 %), so the binary CANNOT be settled numerically. It
  must be settled by identifying WHICH geometric object the observable inherits.

  THIS FILE identifies the two coefficients with the two objects, making the
  binary concrete and non-arbitrary. Per the A-polynomial ground-truth audit
  (`docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md`, convention map):

    * `κ_shape = √3/2` is the imaginary part of the FULL NZ potential
      `Φ(u) = ∫₀ᵘ log(−L(t)) dt` (the raw A-polynomial longitude integral,
      WITHOUT the NZ ½): `Im Φ = (√3/2)·(Re²u − Im²u)`.
    * `κ_pot = √3/4` is the imaginary part of the deformed COMPLEX VOLUME
      `𝔙 = Vol + i·CS = Φ/2` (WITH the NZ ½ `∂𝔙/∂u = ½·v`): the genuine
      Chern–Simons invariant, `QOU.Knot.FigureEightComplexVolume.imV₄₁`.

  So `Φ = 2·𝔙`: the two candidate coefficients are ONE object (the complex volume,
  the physical Chern–Simons invariant) and TWICE it (the un-halved longitude
  integral). The qou-yh67 boost factor `A ∈ {1, 2}` is therefore EXACTLY the
  object choice {complex volume 𝔙, full potential Φ = 2𝔙} = the presence/absence
  of the NZ ½ — not a free convention.

  WHAT THIS DOES NOT CLAIM (anti-fit / anti-laundering, STRICT). This file states
  the exact `Φ = 2·𝔙` dictionary ONLY. It does NOT assert that the physical `S`
  carries `κ_shape` (that would force `A = 2`, `c = √2` — a fit) NOR that it
  carries `κ_pot`. Which object the τ/archimedean evaluation of `Q_β` inherits is
  the OPEN sub-obstruction (bean qou-yh67); it is conjectural
  (`conj:binding-qbeta-complex-volume`, a CAL-2 / Subgoal-2 input), not proved.
  The theorems below are unconditional arithmetic facts about the two constants —
  falsifiable (`κ_shape/κ_pot` could have been any real; it is exactly `2`) and
  content-bearing, not tautologies. Nothing inverts `Q_β`/CODATA; no
  `SDeformedVolumeChannel` instance is fabricated; no `c_k` is produced or wired.

  Base ring: genuinely archimedean (`Real.sqrt`, `Complex`) — §7c-correct `ℝ`/`ℂ`.

  -- Ref: [leitner2026] docs/audits/2026-08-02-nz-half-observable-normalization-structural-resolution.md
  -- Ref: [leitner2026] docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md
  -- Ref: [leitner2026] conj:binding-qbeta-complex-volume; bean qou-yh67; PR #4541 (qou-iyj5)
  -- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-/
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Analysis.SpecialFunctions.Complex.Analytic

namespace QOU.QBeta.ObservableComplexVolumeVsFullPotential

open scoped Real

/-- **Complex-volume coefficient `κ_pot = √3/4`.** The imaginary-part coefficient
    of the deformed COMPLEX VOLUME `𝔙 = Φ/2` — the genuine Chern–Simons invariant,
    carrying the Neumann–Zagier ½ (`∂𝔙/∂u = ½·v`). Same constant as
    `QOU.Knot.FigureEightComplexVolume.cuspModulus`. -/
noncomputable def kappaCV : ℝ := Real.sqrt 3 / 4

/-- **Full-potential coefficient `κ_shape = √3/2`.** The imaginary-part coefficient
    of the FULL NZ potential `Φ(u) = ∫₀ᵘ log(−L) dt` — the raw A-polynomial
    longitude integral WITHOUT the NZ ½ (A-polynomial ground truth,
    `docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md`). Same constant as
    `QOU.MassTheory.nzReVolume` / `QOU.QBeta.ArgUPhaseBranchSelection.nzImVolume`. -/
noncomputable def kappaFull : ℝ := Real.sqrt 3 / 2

theorem kappaCV_pos : 0 < kappaCV := by unfold kappaCV; positivity
theorem kappaFull_pos : 0 < kappaFull := by unfold kappaFull; positivity

/-- **The Neumann–Zagier ½.** `κ_shape = 2·κ_pot`: the full-potential coefficient
    is exactly twice the complex-volume coefficient (`Φ = 2·𝔙`). Falsifiable: the
    ratio could have been any real; it is exactly 2. -/
theorem kappaFull_eq_two_mul_kappaCV : kappaFull = 2 * kappaCV := by
  unfold kappaFull kappaCV; ring

/-- **Im of the complex volume `𝔙`** (the physical Chern–Simons invariant):
    `Im 𝔙(u) = κ_pot·(Re²u − Im²u)`. -/
noncomputable def imComplexVolume (u : ℂ) : ℝ := kappaCV * (u.re ^ 2 - u.im ^ 2)

/-- **Im of the full NZ potential `Φ = 2𝔙`** (the raw longitude integral):
    `Im Φ(u) = κ_shape·(Re²u − Im²u)`. -/
noncomputable def imFullPotential (u : ℂ) : ℝ := kappaFull * (u.re ^ 2 - u.im ^ 2)

/-- **`Φ = 2·𝔙` on the imaginary face (the object dictionary).** For every `u`,
    `Im Φ(u) = 2·Im 𝔙(u)`: the full NZ potential is exactly twice the complex
    volume. The two qou-yh67 candidate coefficients are ONE geometric object
    (`𝔙`, the Chern–Simons invariant) and TWICE it (`Φ`, the un-halved longitude
    integral) — related by the NZ ½, not by a free convention. -/
theorem imFullPotential_eq_two_mul_imComplexVolume (u : ℂ) :
    imFullPotential u = 2 * imComplexVolume u := by
  unfold imFullPotential imComplexVolume
  rw [kappaFull_eq_two_mul_kappaCV]; ring

/-- On the real substrate ray (`u = r : ℝ`): `Im 𝔙(r) = κ_pot·r²`. -/
@[simp] theorem imComplexVolume_ofReal (r : ℝ) :
    imComplexVolume (r : ℂ) = kappaCV * r ^ 2 := by
  simp [imComplexVolume]

/-- On the real substrate ray (`u = r : ℝ`): `Im Φ(r) = κ_shape·r² = 2·(κ_pot·r²)`.
    The boost factor relative to the complex-volume scale `κ_pot·r²` is exactly
    `2` for the full potential. -/
@[simp] theorem imFullPotential_ofReal (r : ℝ) :
    imFullPotential (r : ℂ) = 2 * (kappaCV * r ^ 2) := by
  rw [show (r : ℂ) = ((r : ℝ) : ℂ) from rfl, imFullPotential_eq_two_mul_imComplexVolume,
    imComplexVolume_ofReal]

/-- **The qou-yh67 boost factor IS the object choice.** For a real deformation
    `r ≠ 0`, the ratio of the imaginary face to the complex-volume scale `κ_pot·r²`
    is exactly `1` for the complex volume `𝔙` and exactly `2` for the full
    potential `Φ`. So the opaque `A ∈ {1, 2}` (#4541) is precisely the binary
    "observable = complex volume `𝔙` (A=1, `c=1`) vs full NZ potential `Φ = 2𝔙`
    (A=2, `c=√2`)" — the presence/absence of the NZ ½. This does NOT decide which
    the physical `S` inherits (open, bean qou-yh67); it only fixes that the choice
    is a genuine object choice with the two clean values `1` and `2`. -/
theorem boost_factor_dictionary {r : ℝ} (hr : r ≠ 0) :
    imComplexVolume (r : ℂ) / (kappaCV * r ^ 2) = 1 ∧
      imFullPotential (r : ℂ) / (kappaCV * r ^ 2) = 2 := by
  have hden : kappaCV * r ^ 2 ≠ 0 :=
    mul_ne_zero (ne_of_gt kappaCV_pos) (pow_ne_zero 2 hr)
  refine ⟨?_, ?_⟩
  · rw [imComplexVolume_ofReal, div_self hden]
  · rw [imFullPotential_ofReal, mul_div_assoc, div_self hden, mul_one]

end QOU.QBeta.ObservableComplexVolumeVsFullPotential
