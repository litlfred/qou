import QOU.MathlibExt.LaurentTwoValuation

/-!
# `v_[2]` descends at the q-Collatz fundamental cycle (Front A, A1 — corroboration)

Two prior results bracket the descent-measure candidate `μ = v_[2]` on the
domain-stable cone `D∞`:

* `collatz_vtwo_obstruction.qcollatz_vTwo_increases_on_odd_branch` — `v_[2]`
  *increases* on the odd witness `-X-2`;
* `collatz_vtwo_domain_rescope.qcollatz_vTwo_witness_escapes_domain` — but that
  witness **escapes `D∞`**, so it does not refute `v_[2]` on the cone.

This file supplies the positive side on the known `D∞` element — the fundamental
cycle `{q⁻¹, 1+q⁻¹}` (with `q⁻¹` the attractor). Using the merged Laurent
valuation (`QOU.MathlibExt.LaurentTwoValuation`, cycle values `v(q⁻¹)=0`,
`v(1+q⁻¹)=1`):

* the even branch sends the **non-attractor** point `1+q⁻¹` to the attractor
  `q⁻¹`, and `v_[2]` strictly **drops** `1 → 0`.

So `v_[2]` *satisfies* the strict-descent condition on the fundamental cycle
(descent is required only off the attractor). Combined with the out-of-cone
result above, this corroborates that `v_[2]` is a **live** descent-measure
candidate on `D∞` — the re-opened `qou-4atn` question — on every `D∞` element
checked so far. This is corroboration, **not** a closure: an arbitrary `D∞`
element's orbit is not analysed here. Base ring `ℤ[q^{±1}]` (§7c: fibre level).
-/

namespace QOU.AppendixSurreals

open QOU.MathlibExt.LaurentTwoValuation

open LaurentPolynomial in
/-- **Even-branch step of the fundamental cycle (sorry-free).**  `q⁻¹·[2]_q =
    1+q⁻¹`: the even branch `P ↦ P/[2]_q` sends `1+q⁻¹ ↦ q⁻¹`. -/
theorem cycle_even_step :
    (T (-1) : LaurentPolynomial ℤ) * (T 1 + 1) = 1 + T (-1) := by
  rw [mul_comm]; exact one_add_qinv_eq.symm

open LaurentPolynomial in
/-- **`v_[2]` strictly descends at the fundamental cycle (sorry-free).**  The even
    branch sends the non-attractor point `1+q⁻¹` to the attractor `q⁻¹`, and
    `v_[2]` drops from `1` to `0`.  So `v_[2]` satisfies the strict-descent
    condition on the fundamental cycle (descent required only off the attractor)
    — corroborating, with the out-of-cone rescope, that `v_[2]` is a live descent
    candidate on `D∞`.  Not a closure. -/
theorem laurentTwoVal_descends_on_cycle :
    laurentTwoVal (T (-1)) < laurentTwoVal (1 + T (-1)) := by
  rw [laurentTwoVal_qinv, laurentTwoVal_one_add_qinv]
  exact zero_lt_one

end QOU.AppendixSurreals
