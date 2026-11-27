import HeckeTemperleyLieb.OcneanuWeightBranching
import HeckeTemperleyLieb.QIntegerCanonical

/-!
# QOU.Mass.TwoRowBratteliWeights — the two-row weights `y_(a,b)`, derived from the Ocneanu trace

`conj:wedderburn-bratteli-recursion` states that at convention D (`z = q³/(q²+1)`) the
Jones–Markov weight of a two-row shape `(a, b)`, `a ≥ b`, is

```
y_(a,b) = [a − b + 1]_q / [2]_q^{a+b}.
```

The content block (`mass-theory/wedderburn-bratteli-recursion.lean`) *defines* `jonesWeightD` by
this formula and proves its Bratteli recursion.  Nothing there shows that the formula is the weight
of the Markov trace.  This module supplies that derivation.

## The derivation

* The Markov trace on `H_n(q)` at parameter `z` is `tr = Σ_λ w_λ(z) χ_λ` with
  `w_λ = ocneanuWeight q z λ`; its existence and Markov property at every `z` are
  `SeminormalRep.ocneanuMarkovTraceEveryZ` (BraidKnotOctonion), uniqueness is
  `HeckeCoset.markovTrace_unique`.
* At `z_D`, every shape with three or more rows has weight `0`
  (`ocneanuWeight_conventionD_eq_zero_of_three_rows`), i.e. the trace factors through the
  Temperley–Lieb quotient; that the kernel of this quotient is exactly the radical at generic `q`
  is the general-`n` TL kernel threshold (`BraidKnotOctonion.TLKernelThreshold`, #9668).
* On the two-row shapes the Ocneanu weight telescopes to
  `q^{2k}(1 + q² + ⋯ + q^{2(m−k)}) / (q² + 1)^{m+k}` (`schurPrincipal_twoRow`), and
  `twoRow_weight_eq_y` below identifies this with `[m − k + 1]_q / [2]_q^{m+k}`, because
  `[m−k+1]_q = q^{−(m−k)}(1 + ⋯ + q^{2(m−k)})` and `[2]_q^{m+k} = (q²+1)^{m+k} / q^{m+k}`,
  and `−(m−k) + (m+k) = 2k`.

So `y_(a,b)` is a **theorem about the Markov trace**, not a postulate.  The Bratteli recursion
`y_(a,b) = y_(a+1,b) + y_(a,b+1)` then also follows from the trace tower
(`ocneanuWeight_twoRow_branching`), consistently with the content block's direct proof.

## Base ring

Generic field `K`; genericity hypotheses on `q` only (`q ≠ 0`, `q² + 1 ≠ 0`, `q²` not a root of
unity).  Nothing archimedean.

LaTeX label: `thm:two-row-weights-derived`
-/

namespace QOU.Mass.TwoRowBratteliWeights

open QOU.SchurWeyl QOU.QBeta.WenzlWeight QOU.QInteger Finset

variable {K : Type*} [Field K]

/-- The two-row weight `y_(a,b) = [a − b + 1]_q / [2]_q^{a+b}` (same formula as the content
block's `jonesWeightD`). -/
noncomputable def y (q : K) (a b : ℕ) : K :=
  qIntBalZ q ((a : ℤ) - b + 1) / (q + q⁻¹) ^ (a + b)

/-- The balanced bracket at `d + 1` is `q^{−d}(1 + q² + ⋯ + q^{2d})`. -/
theorem qIntBalZ_succ_eq (q : K) (hq : q ≠ 0) (h1 : q ^ 2 ≠ 1) (d : ℕ) :
    q ^ d * qIntBalZ q ((d : ℤ) + 1) = ∑ i ∈ range (d + 1), (q ^ 2) ^ i := by
  have hgeom : (∑ i ∈ range (d + 1), (q ^ 2) ^ i) * (q ^ 2 - 1) = (q ^ 2) ^ (d + 1) - 1 :=
    geom_sum_mul _ _
  have hq21 : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr h1
  have hqq : q - q⁻¹ ≠ 0 := by
    intro h
    apply hq21
    have : q * (q - q⁻¹) = q ^ 2 - 1 := by field_simp
    rw [← this, h, mul_zero]
  rw [qIntBalZ_def]
  have hz : q ^ ((d : ℤ) + 1) - q ^ (-((d : ℤ) + 1)) = ((q ^ 2) ^ (d + 1) - 1) / q ^ (d + 1) := by
    rw [show ((d : ℤ) + 1) = ((d + 1 : ℕ) : ℤ) by push_cast; ring, zpow_neg, zpow_natCast]
    field_simp
    ring
  rw [hz, ← hgeom]
  field_simp
  ring

/-- **The two-row Ocneanu weight at convention D is `y_(m,k)`.** -/
theorem twoRow_weight_eq_y (q : K) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0) (h1 : q ^ 2 ≠ 1)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1) {m k : ℕ} (h : k ≤ m) :
    ocneanuWeight q (q ^ 3 / (q ^ 2 + 1)) (twoRow m k h) = y q m k := by
  rw [ocneanuWeight_conventionD_eq_schurPrincipal q hq hq21, card_twoRow,
    schurPrincipal_twoRow (q ^ 2) hgen h, y]
  obtain ⟨d, rfl⟩ : ∃ d, m = k + d := ⟨m - k, by omega⟩
  rw [show k + d - k = d by omega,
    show ((↑(k + d) : ℤ) - k + 1) = (d : ℤ) + 1 by push_cast; ring]
  have hb := qIntBalZ_succ_eq q hq h1 d
  have h2 : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [h2, div_pow, ← hb]
  have hqd : q ^ (k + (k + d)) ≠ 0 := pow_ne_zero _ hq
  have hp : (q ^ 2 + 1) ^ (k + (k + d)) ≠ 0 := pow_ne_zero _ hq21
  rw [show k + d + k = k + (k + d) by ring]
  field_simp
  ring

/-- **The Bratteli recursion, read off the trace tower.**  Restricting the convention-D Markov
trace from `H_{n+1}` to `H_n` gives `y_(m,k) = y_(m+1,k) + y_(m,k+1)` (`k < m`). -/
theorem y_bratteli (q : K) (hq : q ≠ 0) (hq21 : q ^ 2 + 1 ≠ 0) (h1 : q ^ 2 ≠ 1)
    (hgen : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1) {m k : ℕ} (hk : k < m) :
    y q m k = y q (m + 1) k + y q m (k + 1) := by
  rw [← twoRow_weight_eq_y q hq hq21 h1 hgen hk.le,
    ← twoRow_weight_eq_y q hq hq21 h1 hgen (by omega : k ≤ m + 1),
    ← twoRow_weight_eq_y q hq hq21 h1 hgen (by omega : k + 1 ≤ m)]
  exact ocneanuWeight_twoRow_branching q hq hq21 hgen hk

end QOU.Mass.TwoRowBratteliWeights
