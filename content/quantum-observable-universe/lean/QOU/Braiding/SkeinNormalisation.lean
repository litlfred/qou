import QOU.Braiding.WeakVertexCouplingNormalisation

/-!
# Two Skein normalisations are live in this corpus, and they are not rescalings

`AGENTS.md` §7a states the Skein relation as **STRICT**:

    (H)   L₊ − L₋  =  (q − q⁻¹) · L₀            bridge  h₁ = q − q⁻¹

Eight live content blocks in five chapters state it differently:

    (J)   q[L₊] − q⁻¹[L₋]  =  (q^{1/2} − q^{-1/2})[L₀]   bridge  s = q^{1/2} − q^{-1/2}

The natural first reading — *"one relation, two normalisations of the
bracket"* — is **wrong**, and `no_rescaling_of_skein_weights` is why: the
weight *ratio* on `(L₊ : L₋)` is `1` in (H) and `q²` in (J), and a rescaling
`[L] ↦ c[L]` leaves that ratio fixed. So the only `q` at which a constant
carries (H) to (J) is `q² = 1`, i.e. the classical point where both bridges
vanish. The two conventions are genuinely different relations.

## How the two bridges are related

`hOne_eq_sSqrt_mul_barEven` gives the factorisation in the square-root
variable `u` (`q = u²`, so no `Real.sqrt` is needed and the file stays over a
generic field):

    h₁(u²) = s(u) · (u + u⁻¹)

and squaring removes the square root entirely:

    hOneSq_eq_twoQ_sq_sub_four        h₁² = [2]_q² − 4
    hOneSq_eq_sSq_mul_twoQ_add_two    h₁² = s² · ([2]_q + 2)

The second is the one that matters downstream, because `s²` — not `s` — is
what the decay-coupling rate carries (`sSq`, and `sSq_eq_twoQ_sub_two`).
So converting a rate between the two conventions is multiplication by
`[2]_q + 2`, which is `4.01089686671` at the proton pin.

## Why the split survived undetected

`barEven_bar_invariant` and `sJ_bar_antiinvariant`: the bridge *ratio*
`[2]_q + 2` is **bar-even** (invariant under `q ↦ q⁻¹`) while `s` itself is
**bar-odd**. A bar-parity argument — the corpus's usual separator — therefore
cannot distinguish the two conventions, because the factor between them is
even.

## What is NOT decided here

Whether the rate is restated in (H) to match §7a, or §7a is amended to record
(J) as the physics-sector convention, is an author decision: it touches a
STRICT rule and eight blocks in five chapters, and nothing proved here forces
either reading. This file measures the split; it does not pick a side.
Bean `qou-8bxv`.

Ground ring: **generic field `K` throughout** (AGENTS.md §7c) — every
statement here is an algebraic identity, so no archimedean construct appears
and there is no `ℝ` companion. The numeric evaluation at the proton pin lives
in `computations/skein-normalisation-two-conventions.witness.json`.
Verified `lean`-direct, sorry-free.
-/

namespace QOU.Braiding.SkeinNormalisation

open QOU.Braiding.WeakVertexT35

variable {K : Type*} [Field K]

/-- The **(H)** bridge of `AGENTS.md` §7a: `h₁ = q − q⁻¹`. -/
noncomputable def hOne (q : K) : K := q - q⁻¹

/-- The **(J)** bridge `s = q^{1/2} − q^{-1/2}`, written in the square-root
variable `u` (so `sJ u` is `s` at `q = u²`). Stating it this way keeps the
file over a generic field: no `Real.sqrt`, no ordering hypothesis. -/
noncomputable def sJ (u : K) : K := u - u⁻¹

/-- The bar-even cofactor `u + u⁻¹` separating the two bridges. -/
noncomputable def barEven (u : K) : K := u + u⁻¹

/-! ### The two conventions are not related by a rescaling -/

/-- **No rescaling of the bracket carries (H) to (J).**  (H) weights the two
crossings `(L₊, L₋)` as `(1, −1)`; (J) weights them `(q, −q⁻¹)`.  If a single
constant `c` reproduced both weights, then `q = q⁻¹` — so the conventions
agree only at `q² = 1`, the classical point where both bridges vanish.

This is the structural content of the finding: the two relations are not two
spellings of one relation, and no normalisation constant reconciles them. -/
theorem no_rescaling_of_skein_weights (q c : K) (hq : q ≠ 0)
    (hplus : c * 1 = q) (hminus : c * (-1) = -q⁻¹) : q ^ 2 = 1 := by
  have hc : c = q := by simpa using hplus
  have hc' : c = q⁻¹ := by
    have : -c = -q⁻¹ := by simpa using hminus
    linear_combination -this
  have hqq : q = q⁻¹ := hc ▸ hc'
  field_simp at hqq
  linear_combination hqq

/-! ### The exact relation between the two bridges -/

/-- **The (H) bridge factors through the (J) bridge.**
`h₁(u²) = s(u) · (u + u⁻¹)`: the two Skein bridges differ by the bar-even
cofactor `u + u⁻¹`. -/
theorem hOne_eq_sSqrt_mul_barEven (u : K) (hu : u ≠ 0) :
    hOne (u ^ 2) = sJ u * barEven u := by
  unfold hOne sJ barEven
  field_simp
  ring

/-- **`h₁² = [2]_q² − 4`.**  The (H) bridge squared is the fundamental
quantum dimension squared minus its classical value squared — the
square-root-free form of the factorisation above. -/
theorem hOneSq_eq_twoQ_sq_sub_four (q : K) (hq : q ≠ 0) :
    hOne q ^ 2 = twoQ q ^ 2 - 4 := by
  unfold hOne twoQ
  field_simp
  ring

/-- **`h₁² = s² · ([2]_q + 2)`** — the conversion factor between the two
conventions, at the power the decay rate actually carries.

`sSq` is `s²` (`WeakVertexSubstitutionScale.sSq`), and the decay-coupling rate
carries it once, so converting a rate from (J) to (H) multiplies by
`[2]_q + 2`.  That factor is `4.01089686671` at the proton pin. -/
theorem hOneSq_eq_sSq_mul_twoQ_add_two (q : K) (hq : q ≠ 0) :
    hOne q ^ 2 = sSq q * (twoQ q + 2) := by
  unfold hOne sSq twoQ
  field_simp
  ring

/-! ### Why bar parity cannot separate the two conventions -/

/-- The cofactor between the bridges is **bar-even**: invariant under
`u ↦ u⁻¹`. -/
theorem barEven_bar_invariant (u : K) (hu : u ≠ 0) :
    barEven u⁻¹ = barEven u := by
  unfold barEven
  field_simp
  ring

/-- The (J) bridge itself is **bar-odd**: `s(u⁻¹) = −s(u)`. -/
theorem sJ_bar_antiinvariant (u : K) (hu : u ≠ 0) :
    sJ u⁻¹ = -sJ u := by
  unfold sJ
  field_simp
  ring

/-- The bridge-squared ratio `[2]_q + 2` is **bar-even**, so a bar-parity
argument cannot tell the two conventions apart: the factor between them
carries no sign under `q ↦ q⁻¹`. -/
theorem twoQ_add_two_bar_invariant (q : K) (hq : q ≠ 0) :
    twoQ q⁻¹ + 2 = twoQ q + 2 := by
  unfold twoQ
  field_simp
  ring

end QOU.Braiding.SkeinNormalisation
