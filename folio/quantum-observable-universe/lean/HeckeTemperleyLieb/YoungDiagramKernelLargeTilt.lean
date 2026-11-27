import HeckeTemperleyLieb.YoungDiagramKernel

/-!
# Large-tilt sign of the covariance kernel: an exact counterexample at `k = 18`

The covariance kernel is `Σ_{λ⊢k} (f^λ)³ ω₃(λ) ≤ 0` (`kernelValue k ≤ 0`, open in general).
Write the tilted family

    tiltedSum k s := Σ_{λ⊢k} (f^λ)^(2+s) · ω₃(λ),

so `s = 1` is the kernel and `s = 0` is the Plancherel mean of `ω₃`, which vanishes.

For large `s` the sum is dominated by the shapes of maximal dimension, so its sign is the sign of
`ω₃` summed over those shapes.  At `k = 18` the maximal dimension is `16336320`, attained by
`(7,4,3,2,1,1)` and its transpose, and `ω₃ = +3` on each.  This file checks, by kernel
evaluation, that

* `tiltedSum 18 1 < 0`   (the kernel itself is negative at `k = 18`), and
* `tiltedSum 18 363 > 0` (the tilt has crossed zero; numerically the crossing is at
  `s* ≈ 362.94`, see `computations/deltalambda/wlambda_covariance_kernel_square_law_inverse.py`).

**What this excludes (structural, with this computation as the invariant).** Any argument that
would prove `Σ (f^λ)² ψ(f^λ) ω₃(λ) ≤ 0` for *every* increasing `ψ`, or for every power
`ψ = f^s` with `s ≥ 1`, proves a false statement at `k = 18`.  Equivalently, writing
`Q = (1/k!) Σ_x x²` (law of `X²`, `X` uniform on `S_k`; `Q` acts on `V^λ` by `1/f^λ`), the
sufficient condition "every power `(e − Q)^m` has non-positive 3-cycle coefficient" is false.
So a proof of the kernel must use the exponent `s = 1` (or a bounded window of exponents), not
monotonicity in the tilt.  This does not say anything against the kernel itself.

No measured value enters: every number here is an exact integer computed from the definitions.
-/

namespace QOU.BraidsAndKnots.YoungDiagramKernel

/-- `Σ_{λ⊢k} (f^λ)^(2+s) · ω₃(λ)`: the kernel tilted by `(f^λ)^(s-1)`. `s = 1` is `kernelValue`. -/
def tiltedSum (k s : ℕ) : ℤ :=
  ((partsOf k).map (fun l => ((sytDim l : ℤ) ^ (2 + s)) * omega3 k l)).sum

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 8000000 in
/-- The two maximal-dimension shapes at `k = 18` have `ω₃ = +3`. -/
theorem omega3_maxdim_eighteen :
    sytDim [7, 4, 3, 2, 1, 1] = 16336320 ∧ omega3 18 [7, 4, 3, 2, 1, 1] = 3 ∧
    sytDim [6, 4, 3, 2, 1, 1, 1] = 16336320 ∧ omega3 18 [6, 4, 3, 2, 1, 1, 1] = 3 := by
  decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 8000000 in
/-- No partition of `18` has dimension above `16336320`. -/
theorem sytDim_le_maxdim_eighteen : ∀ l ∈ partsOf 18, sytDim l ≤ 16336320 := by
  decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 8000000 in
/-- At `s = 1` the tilted sum is the kernel and is negative at `k = 18`. -/
theorem tiltedSum_eighteen_one_neg : tiltedSum 18 1 < 0 := by
  decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 8000000 in
/-- At `s = 363` the tilted sum is positive at `k = 18`: the tilt has changed sign. -/
theorem tiltedSum_eighteen_363_pos : 0 < tiltedSum 18 363 := by
  decide

/-- **No tilt-uniform proof of the kernel exists.**  The statement
"`tiltedSum k s ≤ 0` for every `k` and every `s ≥ 1`" is false. -/
theorem not_forall_tiltedSum_nonpos :
    ¬ ∀ k s : ℕ, 1 ≤ s → tiltedSum k s ≤ 0 := by
  intro h
  have := h 18 363 (by norm_num)
  have h2 := tiltedSum_eighteen_363_pos
  omega

end QOU.BraidsAndKnots.YoungDiagramKernel
