import QOU.Archimedean.BlochRigidity.Instance

/-!
# The Λ-sum on the lower half plane (bean `qou-kifs`)

`blochD_eq_lob` identifies the Bloch–Wigner function `blochD` with the corpus's
Lobachevsky sum `BlochWigner_lob` on the upper half plane only. Below the real axis
the Λ-sum is not `D`: its angles degenerate there (`BlochWigner_lob_eq_zero_of_angles`),
while `D` is odd under conjugation (`blochD_conj`). This file records the correct
statement on the lower half plane, so that `D` is given by the Λ-sum on all of
`ℂ ∖ ℝ` up to a sign and a conjugation:

* `blochD_eq_neg_lob_conj`: for `Im z < 0`, `D(z) = -BlochWigner_lob (z̄)`;
* `blochD_eq_lob_signed`: for `Im z ≠ 0`, the two cases together.

-- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
-/

open Complex

namespace QOU.Archimedean.FiveTermProof

/-- Below the real axis, `D` is minus the Λ-sum at the conjugate point. -/
theorem blochD_eq_neg_lob_conj {z : ℂ} (hz : z.im < 0) :
    blochD z = -BlochWigner_lob ((starRingEnd ℂ) z) := by
  have hc : 0 < ((starRingEnd ℂ) z).im := by rw [conj_im]; linarith
  have h := blochD_conj ((starRingEnd ℂ) z)
  rw [Complex.conj_conj] at h
  rw [h, blochD_eq_lob hc]

/-- Off the real axis, `D` is the Λ-sum on the upper half plane and minus the Λ-sum
    of the conjugate on the lower half plane. -/
theorem blochD_eq_lob_signed {z : ℂ} (hz : z.im ≠ 0) :
    blochD z = if 0 < z.im then BlochWigner_lob z
      else -BlochWigner_lob ((starRingEnd ℂ) z) := by
  split_ifs with h
  · exact blochD_eq_lob h
  · exact blochD_eq_neg_lob_conj (lt_of_le_of_ne (not_lt.1 h) hz)

end QOU.Archimedean.FiveTermProof
