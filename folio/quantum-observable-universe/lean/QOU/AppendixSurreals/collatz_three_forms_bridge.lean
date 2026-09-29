import QOU.QCollatz
import QOU.AppendixSurreals.collatz_three_forms

/-!
Bridge: the §7c-generic `contactThreshold` of `collatz_three_forms` is the
library's `qInt`-based quantity, so the missing lower half proved there closes
`QOU.Substrate.contact_threshold_lt_two`'s two-sided claim **in the library's own
terms**. Verified against the real QOU import cone.
-/
namespace QOU.AppendixSurreals.CollatzThreeFormsBridge

open QOU.Substrate QOU.AppendixSurreals.CollatzThreeForms

/-- The two spellings of the contact threshold agree. -/
theorem contactThreshold_eq_qInt (q : ℝ) (hq1 : q ≠ 1) :
    contactThreshold q = Real.log (qInt q 3) / Real.log (qInt q 2) := by
  rw [contactThreshold, qInt_two q hq1, qInt_three q hq1]

/-- **The two-sided threshold, in the library's own `qInt` terms.** The upper half
    is `QOU.Substrate.contact_threshold_lt_two`; the lower half is the one this
    PR supplies. Together they are the statement that theorem's docstring had
    been claiming. -/
theorem qInt_contactThreshold_mem_Ioo (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) :
    1 < Real.log (qInt q 3) / Real.log (qInt q 2) ∧
      Real.log (qInt q 3) / Real.log (qInt q 2) < 2 := by
  rw [← contactThreshold_eq_qInt q hq1]
  exact contactThreshold_mem_Ioo q hq

/-- Cross-check: the landed one-sided theorem is recovered from the bridge, so
    the two developments are consistent rather than merely parallel. -/
theorem agrees_with_landed (q : ℝ) (hq : 0 < q) (hq1 : q ≠ 1) :
    contactThreshold q < 2 := by
  rw [contactThreshold_eq_qInt q hq1]
  exact contact_threshold_lt_two q hq hq1

end QOU.AppendixSurreals.CollatzThreeFormsBridge
