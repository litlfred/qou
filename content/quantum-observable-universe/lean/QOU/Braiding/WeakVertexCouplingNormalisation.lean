import QOU.Braiding.WeakVertexSubstitutionScale
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Pow

/-!
# What the decay-rate coupling `s²` actually is, and why `W` cannot be rescaled into it

`WeakVertexSubstitutionScale` showed that substituting the weak-vertex trace
`W(q) = tr_M((σ₀σ₁)⁵)` for the single-crossing coupling
`s² = (q^{1/2} − q^{-1/2})²` in the decay rate multiplies every rate by
`≈ 129.4` (the figure read `≈ 1.19·10⁴` until 2026-09-05 — `sSq` is already `s²`
and was squared again, while the rate carries `s²` once; bean `qou-xql6`). That left
one question: what normalisation *does* relate them. Nothing in this file depends on
the magnitude: the exclusion below is about the candidate family's functional form.

This file answers the first half and prunes the obvious family for the second.

## `s²` is a classical-value deviation, not an arbitrary amplitude

`sSq_eq_twoQ_sub_two`: **`s² = [2]_q − 2` exactly**, where `[2]_q = q + q⁻¹` is
the `SU_q(2)` fundamental dimension and `2 = [2]_1` is its classical value. So
the coupling the rate uses is *the q-dimension minus its `q = 1` value*, which
is what makes the rate vanish classically. That identity — not a convention —
is what any `W`-based replacement has to imitate, and it motivates the
candidate family `c · (W(q) − W(1)) · (bridge)`, with `W(1) = 1/4`
(`weakVertexTrace_one`).

## The candidate family is excluded, and not by its order

`s²` vanishes to **second** order at `q = 1` (`sSq_one`, `hasDerivAt_sSq`
giving `s²′(1) = 0`), while `W − W(1)` vanishes to **first** order
(`hasDerivAt_weakVertexTrace_one`: `W′(1) = 5 ≠ 0`). One bridge factor
vanishing like `q − 1` — the corpus has `h = q − q⁻¹`, `ℏ_q = 1 − q⁻¹`, `s`,
`q − 1` — repairs the order, so order alone does not decide.

What decides is `no_constant_rescaling`: for the order-matched candidate
`(W − 1/4)·ℏ_q` there is **no constant `c`** with
`c · (W(q) − 1/4) · (1 − q⁻¹) = s²(q)` for all `q > 1`. The required `c` is
`100/69591` at `q = 2` and `86528/5647625` at `q = 3/2`. Equivalently the
ratio `((W − 1/4)·ℏ_q)/s²` runs from `5` (as `q → 1`) through `8.524` at the
proton pin to `695.91` at `q = 2`: it is a function, not a constant, so the
mismatch is in the functional form and no normalisation constant absorbs it.

This is a **structural exclusion of that family**, proved at two rational
points; it says nothing against `W` itself, whose closed form is
`weakVertexTrace_eq`. What the right coupling is remains open — bean
`qou-pfh7`.

Ground ring: **generic field `K` throughout this file** (AGENTS.md §7c). The
archimedean half — the vanishing-order derivatives and the numeric exclusion —
lives in `WeakVertexCouplingNormalisationArchimedean`, which consumes these
definitions at `K := ℝ`. Verified `lean`-direct, sorry-free.
-/

namespace QOU.Braiding.WeakVertexT35

variable {K : Type*} [Field K]

/-- The `SU_q(2)` fundamental quantum dimension `[2]_q = q + q⁻¹`. -/
noncomputable def twoQ (q : K) : K := q + q⁻¹

/-- `[2]_1 = 2`: the classical value of the fundamental dimension. -/
@[simp] theorem twoQ_one : twoQ (1 : K) = 2 := by
  unfold twoQ; norm_num

/-- **The single-crossing coupling is a classical-value deviation.**
`s² = (q^{1/2} − q^{-1/2})² = [2]_q − [2]_1`.  This is an identity, not a
normalisation choice, and it is why the decay rate vanishes at `q = 1`. -/
theorem sSq_eq_twoQ_sub_two (q : K) (hq : q ≠ 0) : sSq q = twoQ q - 2 := by
  unfold sSq twoQ
  field_simp
  ring

/-- `s²(1) = 0`. -/
@[simp] theorem sSq_one : sSq (1 : K) = 0 := by
  unfold sSq; norm_num

/-! ### The order-matched candidate family, and its exclusion -/

/-- `ℏ_q = 1 − q⁻¹`, the corpus's order-`(q−1)` bridge factor. -/
noncomputable def hbarQ (q : K) : K := 1 - q⁻¹

/-- The order-matched candidate coupling `(W − W(1)) · ℏ_q`, which vanishes to
second order at `q = 1` exactly as `s²` does. -/
noncomputable def candidateCoupling (q : K) : K :=
  (weakVertexTrace q - 1 / 4) * hbarQ q

/-- The ratio whose non-constancy is the content of `no_constant_rescaling`. -/
noncomputable def candidateRatio (q : K) : K := candidateCoupling q / sSq q

end QOU.Braiding.WeakVertexT35
