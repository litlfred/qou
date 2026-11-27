import Mathlib.Data.Complex.Basic

/-!
# A real substrate parameter `q > 1` is not a root of unity

Archimedean companion of `QOU.BringsSurface.TraceCochainObstructions` (split per
§7c). The finite (fusion) quotient of `Rep U_q(sl₂)` on which Turaev–Viro,
Reshetikhin–Turaev and Levin–Wen constructions are defined exists only at a root
of unity; this file proves the premise that a real `q > 1`, in particular the
substrate value `q₀`, is not one. Used by `rem:tv-rt-string-net-root-of-unity-only`.
-/

namespace QOU.BringsSurface.RealQNotRootOfUnity

/-- A real `q > 1` is not a root of unity in `ℂ`: `(q : ℂ) ^ n ≠ 1` for `n ≥ 1`. -/
theorem realGtOne_not_rootOfUnity (q : ℝ) (hq : 1 < q) (n : ℕ) (hn : n ≠ 0) :
    (q : ℂ) ^ n ≠ 1 := by
  intro h
  have h' : ((q ^ n : ℝ) : ℂ) = 1 := by rw [Complex.ofReal_pow]; exact h
  have : q ^ n = 1 := Complex.ofReal_eq_one.mp h'
  exact (one_lt_pow₀ hq hn).ne' this

end QOU.BringsSurface.RealQNotRootOfUnity
