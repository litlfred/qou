/-
  Unit-modulus eigenvalues from det = 1 and small real trace.

  RELOCATED (no mathematical change).  This lemma was declared in
  `content/quantum-observable-universe/braids-and-knots/figure-eight-reeb-rotation.lean`.  It
  moves here because `figure_eight_classical_reeb` — a declaration the content-block resolver
  could not reach in that chapter-directory file — is proved from it, and a Lake-tree module
  cannot import a chapter `.lean`.  The source file imports this module back:
  `figure_eight_unitary_on_standard`, which stays there, still uses the lemma.

  The declaration below is verbatim as it stood in the source file — same statement, same
  proof, same `-- Ref:` citations.
-/

import Mathlib.Analysis.Complex.Norm
import Mathlib.Tactic

namespace QOU.BraidsAndKnots

/-- **Unit-modulus eigenvalues from det = 1 and small real trace.**

  The genuine structural content the figure-eight needs: if a complex
  number `λ` is a root of the real characteristic polynomial
  `x² - t·x + 1` of a `2×2` real matrix with determinant `1` and real
  trace `t` satisfying `t² < 4`, then `‖λ‖ = 1` (unit modulus).

  Proof: take real and imaginary parts of the root equation.  The
  imaginary part gives `λ.im·(2λ.re - t) = 0`; with `t² < 4` the root is
  non-real (`λ.im ≠ 0`), so `λ.re = t/2`.  The real part then pins
  `λ.im² = 1 - λ.re²`, hence `normSq λ = λ.re² + λ.im² = 1`, i.e.
  `‖λ‖ = 1`. -/
-- Ref: [jones1987] Jones, Hecke algebra representations of braid groups (1987)
theorem unit_modulus_of_det_one_small_trace
    (t : ℝ) (ht : t ^ 2 < 4) (lam : ℂ)
    (hroot : lam ^ 2 - (t : ℂ) * lam + 1 = 0) :
    ‖lam‖ = 1 := by
  -- Work with real/imaginary parts. Set a = lam.re, b = lam.im.
  set a := lam.re with ha
  set b := lam.im with hb
  -- Take the real and imaginary parts of the root equation.
  -- Real part:  a² - b² - t·a + 1 = 0.
  -- Imag part:  2·a·b - t·b = 0   ⇒  b·(2a - t) = 0.
  -- Extract the real and imaginary components of the root equation at once.
  rw [Complex.ext_iff] at hroot
  obtain ⟨hr, hi⟩ := hroot
  simp only [pow_two, Complex.add_re, Complex.sub_re, Complex.mul_re,
    Complex.one_re, Complex.zero_re, Complex.ofReal_re, Complex.ofReal_im,
    Complex.mul_im, Complex.add_im, Complex.sub_im, Complex.one_im,
    Complex.zero_im] at hr hi
  -- Real part:  a² - b² - t·a + 1 = 0.
  have hre : a ^ 2 - b ^ 2 - t * a + 1 = 0 := by linear_combination hr
  -- Imag part:  2·a·b - t·b = 0   ⇒  b·(2a - t) = 0.
  have him : b * (2 * a - t) = 0 := by linear_combination hi
  -- `b ≠ 0`: if `b = 0` then `a² - t a + 1 = 0` forces `t² ≥ 4` (discriminant).
  have hb_ne : b ≠ 0 := by
    intro hb0
    have hr0 : a ^ 2 - t * a + 1 = 0 := by nlinarith [hre, hb0]
    nlinarith [sq_nonneg (2 * a - t), hr0]
  -- Hence `2a - t = 0`, i.e. `a = t/2`.
  have ha_eq : 2 * a - t = 0 := by
    rcases mul_eq_zero.mp him with h | h
    · exact absurd h hb_ne
    · exact h
  -- Then `b² = 1 - a²` from the real part, so `normSq = a² + b² = 1`.
  have hns : Complex.normSq lam = 1 := by
    -- From `hre : a² - b² - t·a + 1 = 0` and `ha_eq : 2a - t = 0`,
    -- substitute `t = 2a`:  a² - b² - 2a² + 1 = 0 ⇒ b² = 1 - a².
    have hb2 : b ^ 2 = 1 - a ^ 2 := by linear_combination -hre + a * ha_eq
    have hsq : Complex.normSq lam = a ^ 2 + b ^ 2 := by
      rw [Complex.normSq_apply]; ring
    rw [hsq, hb2]; ring
  -- `‖lam‖² = normSq = 1` and `‖lam‖ ≥ 0` ⇒ `‖lam‖ = 1`.
  have hnorm2 : ‖lam‖ ^ 2 = 1 := by
    rw [Complex.sq_norm]; exact hns
  nlinarith [hnorm2, norm_nonneg lam]

end QOU.BraidsAndKnots
