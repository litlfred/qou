import QOU.Braiding.WeakVertexCouplingNormalisation
import Mathlib.Algebra.Ring.GeomSum

/-!
# The weak vertex's normalisation is the Jones–Markov relation

`WeakVertexCouplingNormalisation` **excluded** the family `c · (W − W(1)) · bridge`
by proving the ratio runs, and left the normalisation itself open: what fixes the
relation between the weak-vertex form factor `W(q) = tr_M((σ₀σ₁)⁵)` and the
decay-rate coupling `s² = (q^{1/2} − q^{-1/2})²`?

This file answers it. The normalisation is not a constant to be found; it is the
framing-and-rank factor of the Jones–Markov relation, and everything else follows
as polynomial algebra over a generic field.

## The rule

For a braid word `β ∈ B_n` with exponent sum `e`, the canonical Markov trace of
its closure is `q^{2e} · V(q^{-2}) / [2]_q^{n-1}` — a **framing** factor `q^{2e}`
(the writhe correction, in the Jones variable `t = q^{-2}`) and a **rank** factor
`[2]_q^{n-1}` (the Markov normalisation `tr_M 1 = 1` on `H_n`). Both are read off
the braid word. The weak vertex is the closure of `(σ₀σ₁)⁵ ∈ B₃`, so `n = 3` and
`e = 10`, and `weakVertexTrace_eq_jones_markov` is that instance:

`W · [2]_q² = q¹² + q⁸ − 1 = q²⁰ · J`, where `J := V_{T(3,5)}(q^{-2})`.

The producer checks the same rule against the corpus's own trace engine on eight
torus knots at `n = 2, 3, 4, 5`, including the mirror pairs `T(3,4)/T(4,3)` and
`T(3,5)/T(5,3)`.

## Why that removes the free constant

`V_K(1) = 1` for every knot (`jonesT35_one` here), and `V'_K(1) = 0`. So `J − 1`
is the *canonically normalised* deviation of the weak vertex from its classical
value: both the offset and the vanishing order are topological facts rather than
choices. `W − W(1)` was trying to be this object and could not be — `W(1) = 1/4`
(`weakVertexTrace_one`) is the Markov rank factor showing through, not a knot
invariant.

## The coupling is a product of two q-differences

`jonesT35_sub_one_eq_qDiff_product`: **`J − 1 = −h₄·h₆/q¹⁰`** exactly, with
`h_k := q^k − q^{-k}` (`qDiff`). The exponents `4` and `6` are the two Jones
exponents of `T(3,5)` (`V(t) = t⁴ + t⁶ − t¹⁰`) and `q^{-10}` is the framing.
Since `h_k(1) = 0`, second-order vanishing at `q = 1` is a *consequence* of there
being two q-differences, not something a bridge factor arranges — which is the
structural fact the excluded family lacked.

`sSq_of_sq`: the rate's own coupling is the same shape at **half scale**,
`s²(u²) = (u − u⁻¹)²`, i.e. `s² = h_{1/2}²`. Stating it at `q = u²` keeps it over
a generic field, with no square root and no ordering.

## The ratio, exactly — no limit and no derivative

Clearing the framing makes the deviation polynomial, and the cofactors are
cyclotomic (`geomCofactor`):

* `jonesT35_sub_one_mul_pow`: `q²⁰(J − 1) = −(q⁸ − 1)(q¹² − 1)`
* `jones_dev_eq_sSq_mul_geom`: `q²⁰(J − 1) = −(q · s²) · G₈(q) · G₁₂(q)`
* `jones_dev_div_sSq`: `(J − 1)/s² = −G₈(q)·G₁₂(q)/q¹⁹ = couplingRatio q`
* `couplingRatio_one`: `couplingRatio 1 = −96 = −G₈(1)·G₁₂(1) = −8·12`

So the vanishing order, the leading coefficient **and the running** all come off
one rational function. Nothing here is a limit, a derivative, or a fit, which is
why the whole derivation stays over `{K : Type*} [Field K]`.

## Scope

This is a **positive derivation of the normalisation.** It produces no rescaling
**constant** and cannot: `couplingRatio` is a non-constant rational function,
consistent with `no_constant_rescaling`.

**🛑 It does NOT derive the order of the decay-rate substitution factor, and this
docstring claimed it did until 2026-09-05 (bean `qou-xql6`).** The withdrawn claim
read `96² = 9216` against `substitutionRateFactor`. `−96` is the classical value of
`(J − 1)/s²`, whose *numerator* vanishes (`V_K(1) = 1` for every knot); the
substitution factor's does not (`W(1) = 1/4`), so `|W|²/s^k` diverges as `q → 1`
and has no leading constant for `−96` to be. Separately the power was wrong: `sSq`
*is* `s²`, so the merged factor was `|W|²/s⁴` where the rate carries `s²` once —
`129.405107404`, not `11875.44`. See
`substitutionRateFactor_has_no_classical_leading_value`. **Every identity below is
untouched**; only the bridge to the rate is gone.

**Honest limit.** `s² = h_{1/2}²` is a *formal* half-scale analogue, not itself a
Jones deviation — a Jones exponent is an integer, so no knot's `V − 1` equals
`s²`. These results explain the magnitude gap between the two couplings; they do
not remove it, and they do not license substituting either for the other.

Producer: `computations/markov/weak_vertex_jones_markov_normalisation.py` (13/13)
Witness: `computations/weak-vertex-jones-markov-normalisation.witness.json`
Bean: `qou-q2l7`.
-/

namespace QOU.Braiding.WeakVertexT35

variable {K : Type*} [Field K]

/-! ## §1  The Jones polynomial of `T(3,5)` and the q-differences -/

/-- The Jones polynomial of the `(3,5)`-torus knot, `V_{T(3,5)}(t) = t⁴ + t⁶ − t¹⁰`. -/
def jonesT35 (t : K) : K := t ^ 4 + t ^ 6 - t ^ 10

/-- `V_K(1) = 1` for every knot; here the instance that fixes the offset of `J − 1`. -/
theorem jonesT35_one : jonesT35 (1 : K) = 1 := by
  simp only [jonesT35]; norm_num

/-- The q-difference `h_k = q^k − q^{-k}`. -/
noncomputable def qDiff (k : ℕ) (q : K) : K := q ^ k - (q ^ k)⁻¹

/-- Every q-difference vanishes classically, which is what makes a *product* of two of
them vanish to second order. -/
theorem qDiff_one (k : ℕ) : qDiff k (1 : K) = 0 := by
  simp only [qDiff]; simp

/-! ## §2  The normalisation: framing `q^{2e}` and rank `[2]_q^{n-1}` -/

/-- The rank factor: `W · [2]_q² = q¹² + q⁸ − 1`, the numerator of the closed form. -/
theorem weakVertexTrace_mul_twoQ_sq (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    weakVertexTrace q * twoQ q ^ 2 = q ^ 12 + q ^ 8 - 1 := by
  simp only [weakVertexTrace, twoQ]
  field_simp

/-- The framing factor: `q²⁰ · V(q^{-2}) = q¹² + q⁸ − 1` with `e = 10`. -/
theorem jones_framing_eq_numerator (q : K) (hq0 : q ≠ 0) :
    q ^ 20 * jonesT35 ((q ^ 2)⁻¹) = q ^ 12 + q ^ 8 - 1 := by
  simp only [jonesT35]
  field_simp

/-- **The Jones–Markov relation for the weak vertex.** `W · [2]_q^{n-1} = q^{2e} · V(q^{-2})`
at `n = 3`, `e = 10`: the trace *is* the Jones polynomial up to a framing power and the
Markov rank factor, both read off the braid word `(σ₀σ₁)⁵`. -/
theorem weakVertexTrace_eq_jones_markov (q : K) (hq0 : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    weakVertexTrace q * twoQ q ^ 2 = q ^ 20 * jonesT35 ((q ^ 2)⁻¹) := by
  rw [weakVertexTrace_mul_twoQ_sq q hq0 h2, jones_framing_eq_numerator q hq0]

/-! ## §3  The coupling is a product of two q-differences -/

/-- **`J − 1 = −h₄h₆/q¹⁰`.** The canonically-normalised deviation of the weak vertex from
its classical value is a product of two q-differences, at the two Jones exponents of
`T(3,5)`, divided by the framing. -/
theorem jonesT35_sub_one_eq_qDiff_product (q : K) (hq0 : q ≠ 0) :
    jonesT35 ((q ^ 2)⁻¹) - 1 = -(qDiff 4 q * qDiff 6 q) / q ^ 10 := by
  simp only [jonesT35, qDiff]
  field_simp
  ring

/-- The same fact with no negative powers: `q²⁰(J − 1) = −(q⁸ − 1)(q¹² − 1)`. This is the
form the `(q − 1)²` factor is read off. -/
theorem jonesT35_sub_one_mul_pow (q : K) (hq0 : q ≠ 0) :
    q ^ 20 * (jonesT35 ((q ^ 2)⁻¹) - 1) = -((q ^ 8 - 1) * (q ^ 12 - 1)) := by
  simp only [jonesT35]
  field_simp
  ring

/-- The decay coupling is the *same shape at half scale*: at `q = u²`,
`s² = (u − u⁻¹)² = h_{1/2}²`. Stated at `u` so it needs no square root and no ordering. -/
theorem sSq_of_sq (u : K) (hu : u ≠ 0) : sSq (u ^ 2) = (u - u⁻¹) ^ 2 := by
  simp only [sSq]
  field_simp

/-! ## §4  The ratio in closed form -/

/-- The cyclotomic cofactor `G_n(q) = 1 + q + ⋯ + q^{n-1}`, so that `G_n(q)(q − 1) = qⁿ − 1`. -/
def geomCofactor (n : ℕ) (q : K) : K := ∑ i ∈ Finset.range n, q ^ i

@[simp] theorem geomCofactor_one (n : ℕ) : geomCofactor n (1 : K) = (n : K) := by
  simp [geomCofactor]

theorem geomCofactor_mul (n : ℕ) (q : K) : geomCofactor n q * (q - 1) = q ^ n - 1 :=
  geom_sum_mul q n

/-- **The exact relation between the two couplings.** `q²⁰(J − 1) = −(q·s²)·G₈·G₁₂`: the
`(q − 1)²` that makes `J − 1` second order is exactly the one in `s²`, and what is left
over is the cyclotomic pair. -/
theorem jones_dev_eq_sSq_mul_geom (q : K) (hq0 : q ≠ 0) :
    q ^ 20 * (jonesT35 ((q ^ 2)⁻¹) - 1)
      = -(q * sSq q * (geomCofactor 8 q * geomCofactor 12 q)) := by
  have hs : q * sSq q = (q - 1) ^ 2 := by
    simp only [sSq]; field_simp
  rw [jonesT35_sub_one_mul_pow q hq0, hs, ← geomCofactor_mul 8 q, ← geomCofactor_mul 12 q]
  ring

/-- The ratio of the two couplings, `−G₈(q)·G₁₂(q)/q¹⁹`. -/
noncomputable def couplingRatio (q : K) : K :=
  -(geomCofactor 8 q * geomCofactor 12 q) / q ^ 19

/-- **`(J − 1)/s² = couplingRatio q`.** No limit and no derivative: the whole comparison
of the two couplings is one rational function. -/
theorem jones_dev_div_sSq (q : K) (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    (jonesT35 ((q ^ 2)⁻¹) - 1) / sSq q = couplingRatio q := by
  have hs : sSq q ≠ 0 := by
    simp only [sSq]
    exact div_ne_zero (pow_ne_zero 2 (sub_ne_zero_of_ne hq1)) hq0
  have h20 : (q : K) ^ 20 ≠ 0 := pow_ne_zero 20 hq0
  have h19 : (q : K) ^ 19 ≠ 0 := pow_ne_zero 19 hq0
  rw [couplingRatio, div_eq_div_iff hs h19]
  have key := jones_dev_eq_sSq_mul_geom q hq0
  have hq20 : (q : K) ^ 20 = q * q ^ 19 := by ring
  rw [hq20] at key
  field_simp at key ⊢
  linear_combination key

/-- **The leading value is `−96`, and it is the two Jones exponents.** `G₈(1) = 8` and
`G₁₂(1) = 12`, so the classical limit of the ratio is `−8·12`. That derives the
second-order leading coefficient of `J − 1` without differentiating anything. -/
theorem couplingRatio_one : couplingRatio (1 : K) = -96 := by
  simp only [couplingRatio, geomCofactor_one, one_pow]
  norm_num

/-- The ratio is **not constant**, so no normalisation constant relates the two couplings —
the derivation explains `no_constant_rescaling` rather than repairing it. Witnessed at two
rational points: `couplingRatio 1 = −96 ≠ couplingRatio 2`. -/
theorem couplingRatio_not_constant :
    couplingRatio (1 : ℚ) ≠ couplingRatio (2 : ℚ) := by
  rw [couplingRatio_one]
  simp only [couplingRatio, geomCofactor, Finset.sum_range_succ]
  norm_num

end QOU.Braiding.WeakVertexT35
