/-
# The two Q_β decay functionals are one functional

Bean `qou-cds1`. The arc has treated the **trace** reading
`Q_β = K · tr_M^z(Δ_S)` and the **ladder** reading
`Q_β = Q_A · cos(α − u/2) · Π_k (1 + c_k u^k)` as two competing accounts of the
decay channel, reporting `z = 0.9985` and `z = 0.4991` respectively and asking
which is right.

They are the same functional. This file proves the algebra.

The bridge is already canonical — `prop:neutron-qvalue-symbolic`, restated in
`computations/qbeta/qbeta_delta_tr_vs_formA.py`:

    Q_A = m_e · |Δ(net)_A| · E_0,   E_0 = 1/(q(q−1)),   Δ(net)_A = h(h−2)/2

and `h(h−2)/2 = h²/2 − h` is exactly the **counit of Δ_S**, which is the
Markov trace `tr_M^z(Δ_S) = h²/2 − h·z` evaluated at `z = 1`. So the ladder's
leading term is the trace functional at `z = 1` with `K = E_0`, identically —
`E0_mul_counit_eq_QA` below — and the two readings share that term by
construction rather than by agreement.

`traceDelta_cross_mul` then shows the trace functional's correction factor is
**affine in z**, equal to 1 at `z = 1`, with slope `2q/(2q − q² + 1)`
(`traceRatio_sub_one`). The ladder writes the SAME correction as a cosine of an
affine function of `z`, times a power series in `u`. Hence

    Π_k (1 + c_k u^k) = affine(z) / cos((z−1)h/2 − u/2)

is forced, and the `c_k` are the mismatch between an affine function of `z` and
a cosine of an affine function of `z`. They are a **reparametrisation residual**,
not an independent expansion — the third instance in this corpus of the
"defined residual ≠ derived decomposition" class named STRICT in `AGENTS.md`,
after `S_leak := c₃ + Vol(4₁)` and `S := −c₃/κ_(2,1)`.

Two consequences the numbers make concrete (measured in the probe
`qbeta-decay-functional-unification-protium`, not claimed here):

* The two routes report different `z` because they invert **different
  functions** to the same measured `Q_β/Q_A = 0.998325`. At `z = 1` the affine
  slope is `1.1167` and the cosine's is `4.4515e-4` — a factor **2508.65**. That
  is the whole of the "0.9985 vs 0.4991" discrepancy.
* `F_REQUIRED_TRM = 1.75923699`, carried as the decay channel's missing scale
  `K`, is exactly `(Q_β/Q_A) / affine(z_D)` — a statement about where `z_D` sits
  on the affine line, not a missing normalisation.

`alpha_two_mul` records the corpus's own definition of the ladder phase,
`2α = ε(Δ) − tr_M^z(Δ)`, in the same place, so the two coordinates can be read
against each other without leaving the file.

Everything here is a rational-function identity over a field of characteristic
zero. No convention is adjudicated, no `c_k` value is asserted, nothing is
wired: the file says the two functionals coincide at `z = 1` and are related by
an affine change of coordinate, and that is all.

## Scope

Generic in `q`, `z`, `m_e` over any `Field F` with `[CharZero F]`. The `Δ_S`
closed forms `ε = h²/2 − h` and `tr_M^z = h²/2 − h·z` are taken as the
definitions of the objects named — they are the corpus's own closed forms, valid
for the SHORT model (`qbeta_delta_element_fork_pricing_probe.py`), and this file
inherits that scope rather than re-establishing it.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.QBeta

variable {F : Type*} [Field F] [CharZero F]

/-- The substrate variable `h = q − 1/q`. -/
noncomputable def hOf (q : F) : F := q - 1 / q

/-- The counit (augmentation) of the short decay element, `ε(Δ_S) = h²/2 − h`.
Corpus closed form; `qbeta-counit-closed-form.md`. -/
noncomputable def counitDelta (q : F) : F := (hOf q) ^ 2 / 2 - hOf q

/-- The Markov trace of the short decay element at Markov parameter `z`,
`tr_M^z(Δ_S) = h²/2 − h·z`. Corpus closed form. -/
noncomputable def traceDelta (q z : F) : F := (hOf q) ^ 2 / 2 - hOf q * z

/-- The canonical hadronic energy scale `𝔈₀ = m_e/(q(q−1))` — the corpus's
derived trace→MeV conversion, fixed by CAL-1 and CAL-2 alone. -/
noncomputable def E0 (me q : F) : F := me / (q * (q - 1))

/-- The ladder's leading term `Q_A = m_e·|q²−2q−1|·(q+1)/(2q³)`, written with the
sign it carries on the substrate branch (`q² − 2q − 1 < 0` for `q` near `q₀`), so
the identity below is an equation and not an equation-up-to-sign. -/
noncomputable def QA (me q : F) : F := me * (-(q ^ 2 - 2 * q - 1)) * (q + 1) / (2 * q ^ 3)

/-- The ladder phase `α = (z−1)h/2`. -/
noncomputable def alphaOf (q z : F) : F := (z - 1) * hOf q / 2

omit [CharZero F] in
/-- The trace evaluated at `z = 1` **is** the counit. The two corpus closed
forms are one object at the augmentation point. -/
theorem traceDelta_one (q : F) : traceDelta q 1 = counitDelta q := by
  simp [traceDelta, counitDelta]

/-- **The bridge.** `𝔈₀ · (−ε(Δ_S)) = Q_A`, identically in `q` and `m_e`.

So the ladder's leading term is the trace functional at `z = 1` with the scale
`K = 𝔈₀`. This is `prop:neutron-qvalue-symbolic` stated as an identity: the two
decay readings do not merely agree numerically at leading order, they are the
same expression. -/
theorem E0_mul_counit_eq_QA (me q : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    E0 me q * (-counitDelta q) = QA me q := by
  have h2 : (2 : F) ≠ 0 := by norm_num
  unfold E0 counitDelta QA hOf
  field_simp
  ring

/-- **The correction factor is affine in `z`**, in cross-multiplied form so no
non-vanishing hypothesis on the counit is needed:
`tr_M^z(Δ_S)·(2q − q² + 1) = ε(Δ_S)·(2qz − q² + 1)`. -/
theorem traceDelta_cross_mul (q z : F) (hq : q ≠ 0) :
    traceDelta q z * (2 * q - q ^ 2 + 1) = counitDelta q * (2 * q * z - q ^ 2 + 1) := by
  unfold traceDelta counitDelta hOf
  field_simp
  ring

omit [CharZero F] in
/-- The affine correction departs from `1` linearly in `z − 1` with slope `2q`,
stated on the numerators so no non-vanishing hypothesis is needed. Non-zero slope
(`q ≠ 0`) is why the trace inversion for `z` is exact and unique rather than a
fit — and, since the ladder's cosine has a different slope at `z = 1`, why the
two routes report different `z` for one measured correction. -/
theorem traceNum_sub_denom (q z : F) :
    (2 * q * z - q ^ 2 + 1) - (2 * q - q ^ 2 + 1) = (z - 1) * (2 * q) := by
  ring

omit [CharZero F] in
/-- The same statement as a ratio, given a non-vanishing denominator. -/
theorem traceRatio_sub_one (q z : F) (hden : 2 * q - q ^ 2 + 1 ≠ 0) :
    (2 * q * z - q ^ 2 + 1) / (2 * q - q ^ 2 + 1) - 1
      = (z - 1) * (2 * q) / (2 * q - q ^ 2 + 1) := by
  rw [eq_div_iff hden, sub_mul, div_mul_cancel₀ _ hden, one_mul]
  exact traceNum_sub_denom q z

omit [CharZero F] in
/-- The affine correction is `1` exactly at `z = 1`, matching `traceDelta_one`. -/
theorem traceRatio_at_one (q : F) (hden : 2 * q - q ^ 2 + 1 ≠ 0) :
    (2 * q * (1 : F) - q ^ 2 + 1) / (2 * q - q ^ 2 + 1) = 1 := by
  rw [show 2 * q * (1 : F) - q ^ 2 + 1 = 2 * q - q ^ 2 + 1 by ring]
  exact div_self hden

/-- The trace functional, with `K = 𝔈₀`, is `Q_A` times the affine correction:
`𝔈₀·(−tr_M^z(Δ_S))·(2q − q² + 1) = Q_A·(2qz − q² + 1)`.

This is the unification in one line. The ladder asserts the same left-hand side
equals `Q_A · cos(α − u/2) · Π_k(1 + c_k u^k)`; equating the two therefore
*defines* the `c_k` as the ratio of an affine function of `z` to a cosine of an
affine function of `z`, with no independent content. -/
theorem traceFunctional_eq_QA_mul_affine (me q z : F) (hq : q ≠ 0) (hq1 : q - 1 ≠ 0) :
    E0 me q * (-traceDelta q z) * (2 * q - q ^ 2 + 1)
      = QA me q * (2 * q * z - q ^ 2 + 1) := by
  have hcross := traceDelta_cross_mul q z hq
  have hbridge := E0_mul_counit_eq_QA me q hq hq1
  calc E0 me q * (-traceDelta q z) * (2 * q - q ^ 2 + 1)
      = -(E0 me q * (traceDelta q z * (2 * q - q ^ 2 + 1))) := by ring
    _ = -(E0 me q * (counitDelta q * (2 * q * z - q ^ 2 + 1))) := by rw [hcross]
    _ = (E0 me q * (-counitDelta q)) * (2 * q * z - q ^ 2 + 1) := by ring
    _ = QA me q * (2 * q * z - q ^ 2 + 1) := by rw [hbridge]

/-- The ladder phase is the counit-minus-trace discrepancy, `2α = ε − tr_M^z`.
The corpus's *"α is neither free nor fitted: it IS the discrepancy"*, recorded
here so both coordinates sit in one file. -/
theorem alpha_two_mul (q z : F) : 2 * alphaOf q z = counitDelta q - traceDelta q z := by
  unfold alphaOf counitDelta traceDelta
  ring

omit [CharZero F] in
/-- `α = 0` exactly at `z = 1`, so both coordinates are anchored at the same
point — which is why leading-order agreement is automatic and carries no
information about which reading is correct. -/
theorem alpha_at_one (q : F) : alphaOf q 1 = 0 := by
  simp [alphaOf]

end QOU.QBeta
