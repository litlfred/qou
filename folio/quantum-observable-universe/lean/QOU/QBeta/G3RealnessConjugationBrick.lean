/-
  G3 realness from a shared conjugation law — the structural brick.

  Motivation. The 5₂ AK-integral probe (PR #4475) found numerically that the
  two representations of the same 5₂ state integral — the Fantini–Wheeler
  `Z[q^±]`-combination `I_FW(τ)` and the Garoufalidis–Gu–Mariño assembly
  `Z_GGM(τ)` — have a RATIO `I_FW(τ) / Z_GGM(τ)` that is real to ~1e-32.

  A numerical `Im ≈ 0` is NOT a theorem. This file proves the *structural*
  fact underneath it and NOTHING MORE: if two quantities transform under
  complex conjugation with the SAME law (a common unit factor), their ratio
  is fixed by conjugation, hence real — with NO appeal to the numerical bound
  and NO `native_decide` / `norm_num`-on-floats laundering.

  ── What is proved (sorry-free, unconditional) ──────────────────────────────
  * `ratio_star_fixed_of_shared_law` — over ANY field `K` with a star ring
    structure: if `star a = u * a` and `star b = u * b` for a common NONZERO
    `u`, then `star (a / b) = a / b`. Pure algebra (the unit `u` cancels in the
    ratio); no ordering, no archimedean content — §7c: stated over generic `K`,
    `ℂ` is NOT mentioned here.
  * `ratio_im_zero_of_shared_law` — the `ℂ` reading: the same hypotheses give
    `(a / b).im = 0` (genuinely real). `ℂ` appears ONLY here, where `.im` /
    conjugation-as-realness is genuinely needed (§7c wall).

  ── What is CONDITIONAL (§3b-cond) ──────────────────────────────────────────
  * `SharedConjugationCovariance I_FW Z_GGM` — a content-bearing `Prop` class
    carrying the OPEN hypothesis that `I_FW` and `Z_GGM` are conjugation-
    covariant with a common law. This is NOT proved: the 1e-32 numeric is
    EVIDENCE for it, and a full proof would follow from FW Thm 1.4 (the two
    integrals are the same object) + the established 5₂ saddle conjugate-pairing
    `V₂ = conj V₁`, `Im V₁ = Vol` (`FiveTwoSaddleCurve.lean`). Carried as an
    explicit `[Instance]` hypothesis; the theorem DERIVES realness from it.
  * `g3_ratio_real` / `g3_ratio_im_zero` — conditional on the class, the 5₂
    ratio `I_FW / Z_GGM` is real. Fully verified by Lean modulo the single,
    named, class-axiomatised covariance input.

  ── What this does and does NOT establish ───────────────────────────────────
  Does NOT prove FW Thm 1.4 (bean `qou-h7yk`). Does NOT convert the numerical
  G3 match into a theorem — it REDUCES G3-realness to the (still-open)
  conjugation-covariance of the two integrals. A proved covariance would firm
  the FW↔GGM identification and the boost/spin real–imaginary split
  (`DeltaLambdaBindingAssembly`), discharging the realness sub-part of gap
  `qou-ri9w`; it does NOT close `qou-qnnq` (braid→selection) and does NOT
  yield c₃.

  -- Ref: [leitner2026] arXiv:2410.20973 (Fantini–Wheeler 2024), Thm 1.1/1.4;
     probe PR #4475 (5₂ AK-integral G3 realness);
     docs/audits/2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md
  -- Ref: [garoufalidis-gu-marino2021] (GGM) 2012.00062 — the Z_GGM assembly
-/
import Mathlib.Data.Complex.Basic
import Mathlib.Algebra.Field.Basic

namespace QOU.QBeta.G3RealnessConjugationBrick

/-! ### Abstract brick: shared conjugation law ⇒ ratio fixed by conjugation

Pure algebra over a generic field with a star ring structure. The physical
content ("real") is deferred to the `ℂ` corollary; here the content is that
the ratio is a fixed point of the star automorphism, which needs no ordering
and no `ℂ`. -/

variable {K : Type*} [Field K] [StarRing K]

/-- **Shared conjugation law ⇒ the ratio is a fixed point of the star map.**

If `star a = u * a` and `star b = u * b` for a common NONZERO `u`, then the
unit `u` cancels in `a / b`, so `star (a / b) = a / b`.

This is genuine algebraic content, not a tautology: it is FALSE without the
shared-`u` hypothesis (e.g. `star a = u * a`, `star b = v * b` with `u ≠ v`
gives `star (a/b) = (u/v)·(a/b) ≠ a/b` in general). Holds in any field with a
star ring structure; `ℂ` is not required. -/
theorem ratio_star_fixed_of_shared_law {a b u : K} (hu : u ≠ 0)
    (ha : star a = u * a) (hb : star b = u * b) :
    star (a / b) = a / b := by
  have h : (starRingEnd K) (a / b) = a / b := by
    rw [map_div₀, starRingEnd_apply, starRingEnd_apply, ha, hb,
      mul_div_mul_left a b hu]
  simpa only [starRingEnd_apply] using h

/-! ### `ℂ` reading: fixed-by-conjugation ⇒ real

`ℂ` and `.im` appear only from here on (§7c). -/

/-- **Shared conjugation law ⇒ the ratio is real** (`(a / b).im = 0`).

The `ℂ` specialisation of `ratio_star_fixed_of_shared_law`: a complex number
fixed by conjugation has zero imaginary part. This is the honest content of the
numerical `Im(I_FW/Z_GGM) ≈ 1e-32` — realness follows from the SYMMETRY, not
from the float bound. -/
theorem ratio_im_zero_of_shared_law {a b u : ℂ} (hu : u ≠ 0)
    (ha : star a = u * a) (hb : star b = u * b) :
    (a / b).im = 0 := by
  have h : star (a / b) = a / b := ratio_star_fixed_of_shared_law hu ha hb
  -- `star z = z` for `z : ℂ` forces `z.im = 0` (conjugation-fixed ⇒ real).
  rw [← starRingEnd_apply] at h
  exact Complex.conj_eq_iff_im.mp h

/-! ### Conditional 5₂ instantiation (§3b-cond)

The conjugation-covariance of the two 5₂ integrals is NOT proved. It is carried
as an explicit hypothesis; the theorem DERIVES realness from it. The class is
content-bearing (§3b-tax): its field is a parameter-quantified equation in the
SHAPE of the claim (the shared-law covariance), carrying the *hypothesis*, not
the *conclusion* `(ratio).im = 0`. -/

/-- **OPEN hypothesis (conditional class).** The Fantini–Wheeler combination
`I_FW` and the Garoufalidis–Gu–Mariño assembly `Z_GGM` of the 5₂ state integral
are conjugation-covariant with a *common* law: for each `τ` there is a nonzero
`u` (a phase, rooted in the saddle conjugate-pairing `V₂ = conj V₁`) with
`conj (I_FW τ) = u * I_FW τ` and `conj (Z_GGM τ) = u * Z_GGM τ`.

NOT proved. The 5₂ AK-integral probe (PR #4475) found `Im(I_FW/Z_GGM) ≈ 1e-32`
— that numeric is EVIDENCE for this covariance, not a proof of it. A proof would
follow from FW Thm 1.4 (bean `qou-h7yk`) plus the established saddle
conjugate-pairing. Held as a `[SharedConjugationCovariance]` hypothesis so the
downstream realness result is an honest §3b-cond conditional theorem. -/
class SharedConjugationCovariance (I_FW Z_GGM : ℂ → ℂ) : Prop where
  /-- For each `τ`, a common nonzero conjugation factor `u` covariates both
  integrals. The existential packages the (data) phase `u` inside a `Prop`. -/
  shared : ∀ τ : ℂ, ∃ u : ℂ, u ≠ 0 ∧
    star (I_FW τ) = u * I_FW τ ∧ star (Z_GGM τ) = u * Z_GGM τ

/-- **Conditional on `SharedConjugationCovariance`:** `star (I_FW τ / Z_GGM τ)
= I_FW τ / Z_GGM τ` — the 5₂ ratio is fixed by conjugation. Fully verified by
Lean modulo the single class-axiomatised covariance input. -/
theorem g3_ratio_real (I_FW Z_GGM : ℂ → ℂ)
    [h : SharedConjugationCovariance I_FW Z_GGM] (τ : ℂ) :
    star (I_FW τ / Z_GGM τ) = I_FW τ / Z_GGM τ := by
  obtain ⟨u, hu, hI, hZ⟩ := h.shared τ
  exact ratio_star_fixed_of_shared_law hu hI hZ

/-- **Conditional on `SharedConjugationCovariance`:** the 5₂ ratio is real,
`(I_FW τ / Z_GGM τ).im = 0`. This is the structural theorem behind the 1e-32
numerical G3 match — realness from the shared conjugation symmetry, with NO
float bound in the proof. -/
theorem g3_ratio_im_zero (I_FW Z_GGM : ℂ → ℂ)
    [h : SharedConjugationCovariance I_FW Z_GGM] (τ : ℂ) :
    (I_FW τ / Z_GGM τ).im = 0 := by
  obtain ⟨u, hu, hI, hZ⟩ := h.shared τ
  exact ratio_im_zero_of_shared_law hu hI hZ

end QOU.QBeta.G3RealnessConjugationBrick
