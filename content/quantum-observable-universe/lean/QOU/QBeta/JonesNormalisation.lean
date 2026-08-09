import Mathlib.Algebra.Algebra.Defs
import Mathlib.Tactic.NoncommRing
import QOU.QBeta.TemperleyLiebTower

/-!
# The Jones normalisation under convention D

**What `markov-pair-z2` got wrong, and what the right statement is.**

That block asserts

> The value $z^2$ is the **Jones polynomial of the Hopf link**:
> $J_{\mathrm{Hopf}}(q) = -(q^{1/2} + q^{-1/2})\cdot z^2$

and it is wrong three times over, only one of which is about the convention:

1. **Wrong link.** `z² = tr_M(σᵢσⱼ)` for `i < j`. The closure of `σ₁σ₂` in `B₃`
   is the **unknot**, and the closure of `σ₁σ₃` in `B₄` is the **two-component
   unlink**. Neither is the Hopf link. The Hopf link is the closure of `σ₁²` in
   `B₂`, whose trace is `tr_M(σ₁²) = hz + 1`, not `z²`.
2. **Wrong kind of object.** A raw Markov-trace value is not a Jones polynomial.
   The invariant needs the loop factor `δ^{n-1}` and a framing correction
   `q^{-2e}`; without them the "value" is not even an invariant of the closure,
   since it changes under Markov stabilisation.
3. **Wrong loop parameter.** The prefactor `q^{1/2} + q^{-1/2}` is `[2]_{√q}`, the
   loop value at *half* argument. The Temperley–Lieb loop value of the
   production trace is `δ = [2]_q = q + q⁻¹`. At `q₀` these are `2.0027…` and
   `2.010896866707122…` — the same conflation as `1/δ = 0.4972905456…` against
   the excised `z_C = 0.4993203342…`.

## The theorem

For a braid `β ∈ B_n` with exponent sum `e`, the Jones polynomial of its closure
is

    V(β̂)(t) = q^{-2e} · [2]_q^{n-1} · tr_M(β),        t = q^{-2}

with no square roots anywhere. This file proves the algebraic core and checks it
on four closures whose answers are known independently.

## Why convention D is exactly the right trace for this

The derivation turns on one identity, and it is the *definition* of convention D
in disguise.

Put `eᵢ := q − σᵢ`. From the Hecke quadratic relation `σ² = hσ + 1` with
`h = q − q⁻¹`,

    eᵢ² = q² − 2qσ + σ² = (q²+1) − (q+q⁻¹)σ = [2]_q · eᵢ

so `eᵢ` is a Temperley–Lieb generator with loop parameter `δ = [2]_q`
(`tl_generator_sq`). Its trace is `tr_M(eᵢ) = q − z`, and convention D says
precisely

    (q − z) · [2]_q = 1        (`TemperleyLiebTower.loop_reciprocal`)

i.e. `tr_M(eᵢ) = 1/δ` — the standard Temperley–Lieb Markov normalisation. The
peel follows: `tr_M(x eₙ) = (q − z) tr_M(x) = δ⁻¹ tr_M(x)`.

So convention D is not *compatible with* the Jones/Temperley–Lieb trace; under
`eᵢ = q − σᵢ` it **is** that trace. This is the content of the registry naming D
"SU(2)/Temperley-Lieb (Jones) decomposition", made into an identity.

## The Kauffman dictionary

`δ = −A² − A⁻²` with `A² = −q` (`kauffman_loop`), hence `t = A⁻⁴ = q⁻²`. The
Hecke generator and the Kauffman bracket generator differ by a scalar:
`ρ(σᵢ) = (A/q)·σᵢ`, since both have eigenvalue ratio `−q² = −A⁴`. That scalar,
run against the writhe correction `(−A³)^{-e}`, collapses to `q^{-2e}` — every
odd power of `A` cancels, which is why the final formula has no square roots even
though the Kauffman variable does.

## Status

The four closure checks are proved as scalar identities under `IsConventionD`.
They are checks of the *normalisation*, not of the braid-group topology: that
`cl(σ₁σ₂) ⊂ B₃` is the unknot and `cl(σ₁σ₃) ⊂ B₄` is the two-component unlink is
input here, taken from the standard theory, not derived. What is proved is that
given those closures the formula returns `1`, `1`, `q⁻¹+q⁻⁵` and `δ` — the
correct Jones polynomials — which is what pins the normalisation.
-/

namespace QOU.QBeta.JonesNormalisation

open QOU.QBeta.TemperleyLiebTower

section TLGenerator

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A]

/-- **`eᵢ := q − σᵢ` is a Temperley–Lieb generator with loop parameter `[2]_q`.**

From the Hecke quadratic relation `σ² = (q − q⁻¹)σ + 1` alone — no trace, no
convention. This is what makes `[2]_q` the loop value and hence what makes
`q^{1/2} + q^{-1/2}` the wrong prefactor in `markov-pair-z2`.

Stated in an arbitrary `R`-algebra rather than a commutative ring: `σᵢ` does not
commute with `σⱼ`, and the point is that this identity needs no such assumption,
only that scalars are central (`Algebra.commutes`). -/
theorem tl_generator_sq (q : R) (hq : q ≠ 0) (s : A)
    (hs : s * s = algebraMap R A (q - q⁻¹) * s + 1) :
    (algebraMap R A q - s) * (algebraMap R A q - s)
      = algebraMap R A (q + q⁻¹) * (algebraMap R A q - s) := by
  -- Scalars are central: this is the only structural input beyond `hs`.
  have hcom : s * algebraMap R A q = algebraMap R A q * s := (Algebra.commutes q s).symm
  -- `q - q⁻¹ = 2q - (q + q⁻¹)`. Substituting this into the quadratic relation is
  -- what makes the `s`-linear terms cancel identically, leaving a scalar identity.
  have hH : algebraMap R A (q - q⁻¹)
      = algebraMap R A q + algebraMap R A q - algebraMap R A (q + q⁻¹) := by
    rw [← map_add, ← map_sub]
    congr 1
    ring
  -- `(q + q⁻¹)·q = q² + 1`, the one place `q ≠ 0` is used.
  have hprod : algebraMap R A (q + q⁻¹) * algebraMap R A q
      = algebraMap R A q * algebraMap R A q + 1 := by
    rw [← map_mul, ← map_mul, ← map_one (algebraMap R A), ← map_add]
    congr 1
    field_simp
  rw [hH] at hs
  simp only [sub_mul, mul_sub]
  rw [hs, hcom, hprod]
  noncomm_ring

end TLGenerator

section Scalars

variable {R : Type*} [Field R]

/-! ### The normalisation, as scalar identities

`V(β̂) = q^{-2e} · [2]_q^{n-1} · tr_M(β)` evaluated on four closures whose Jones
polynomials are known independently. Each is stated under `IsConventionD` and
under nothing else, so each is a check that convention D — and not merely *some*
Markov parameter — is what makes the normalisation land. -/

/-- The Jones normalisation factor: `q^{-2e} · [2]_q^{n-1}`. -/
noncomputable def jonesFactor (q : R) (e n : ℕ) : R :=
  (q⁻¹) ^ (2 * e) * (q + q⁻¹) ^ (n - 1)

/-- **`q² + 1 ≠ 0` is forced, not assumed.** In a general field it could vanish
(characteristic `2`, or `q = i` over `ℂ`), but convention D rules it out: if
`q² + 1 = 0` then `q³ = z(q²+1) = 0`, so `q = 0`. Needed to clear denominators in
every identity below, and worth isolating so the hypothesis list stays honest —
none of these theorems needs an ad-hoc side condition. -/
theorem q_sq_add_one_ne_zero (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z) :
    q ^ 2 + 1 ≠ 0 := by
  intro h
  have hzero : z * (q ^ 2 + 1) = 0 := by rw [h, mul_zero]
  rw [hD] at hzero
  exact hq ((pow_eq_zero_iff (by norm_num : (3 : ℕ) ≠ 0)).mp hzero)

/-- Convention D in solved form: `z = q³/(q²+1)`. Convenient for substitution. -/
theorem z_eq_div (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z) :
    z = q ^ 3 / (q ^ 2 + 1) :=
  (eq_div_iff (q_sq_add_one_ne_zero q z hq hD)).mpr hD

/-- **Unknot as the closure of `σ₁ ∈ B₂`.** `e = 1`, `n = 2`, `tr_M(σ₁) = z`.

`q⁻² · [2]_q · z = 1`. The base case that fixes the normalisation: any other
choice of framing exponent or loop power fails here. -/
theorem unknot_two_strand (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z) :
    (q⁻¹) ^ 2 * (q + q⁻¹) * z = 1 := by
  have hne := q_sq_add_one_ne_zero q z hq hD
  rw [z_eq_div q z hq hD]
  field_simp

/-- **Unknot again, as the closure of `σ₁σ₂ ∈ B₃`.** `e = 2`, `n = 3`,
`tr_M(σ₁σ₂) = z²`.

`q⁻⁴ · [2]_q² · z² = 1`. This is the closure `markov-pair-z2` calls the Hopf
link. It is the **unknot** — and the formula says so, independently of the
`σ₁ ∈ B₂` computation above, which is a real consistency check on the `n`- and
`e`-dependence rather than a restatement. -/
theorem unknot_three_strand (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z) :
    (q⁻¹) ^ 4 * (q + q⁻¹) ^ 2 * z ^ 2 = 1 := by
  have h := unknot_two_strand q z hq hD
  have : ((q⁻¹) ^ 2 * (q + q⁻¹) * z) ^ 2 = 1 := by rw [h]; ring
  calc (q⁻¹) ^ 4 * (q + q⁻¹) ^ 2 * z ^ 2
      = ((q⁻¹) ^ 2 * (q + q⁻¹) * z) ^ 2 := by ring
    _ = 1 := this

/-- **The Markov trace of `σ₁²`.** `tr_M(σ₁²) = hz + 1` with `h = q − q⁻¹`, from
the quadratic relation and the Markov peel. Under convention D this is
`(q⁴+1)/(q²+1)`.

This — not `z²` — is the Hopf-link trace. -/
theorem trace_sigma_sq_conventionD (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z) :
    (q - q⁻¹) * z + 1 = (q ^ 4 + 1) / (q ^ 2 + 1) := by
  have hne := q_sq_add_one_ne_zero q z hq hD
  rw [z_eq_div q z hq hD]
  field_simp
  ring

/-- **The Hopf link.** Closure of `σ₁² ∈ B₂`: `e = 2`, `n = 2`.

`q⁻⁴ · [2]_q · (hz + 1) = q⁻¹ + q⁻⁵`.

In the Jones variable `t = q⁻²` with `t^{1/2} := A⁻² = −q⁻¹`, this is
`−t^{1/2} − t^{5/2}` — the standard value for the positive Hopf link. The sign
lives entirely in the branch of `t^{1/2}`; in `q` there is no ambiguity, which is
one practical reason to state the normalisation in `q` rather than `t`. -/
theorem hopf_link (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z) :
    (q⁻¹) ^ 4 * (q + q⁻¹) * ((q - q⁻¹) * z + 1) = q⁻¹ + (q⁻¹) ^ 5 := by
  have hne := q_sq_add_one_ne_zero q z hq hD
  rw [z_eq_div q z hq hD]
  field_simp
  ring

/-- **The two-component unlink.** Closure of `σ₁σ₃ ∈ B₄`: `e = 2`, `n = 4`,
`tr_M(σ₁σ₃) = z²`.

`q⁻⁴ · [2]_q³ · z² = [2]_q = q + q⁻¹`, which is `−t^{1/2} − t^{-1/2}` — the Jones
polynomial of the 2-component unlink.

The sharpest of the four checks. It has the *same* trace value `z²` as
`unknot_three_strand` and a different answer, purely through `n`. Any account
that reads a Jones polynomial off a raw trace value — as `markov-pair-z2` does —
cannot distinguish these two links at all. -/
theorem two_component_unlink (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z) :
    (q⁻¹) ^ 4 * (q + q⁻¹) ^ 3 * z ^ 2 = q + q⁻¹ := by
  have h := unknot_three_strand q z hq hD
  calc (q⁻¹) ^ 4 * (q + q⁻¹) ^ 3 * z ^ 2
      = ((q⁻¹) ^ 4 * (q + q⁻¹) ^ 2 * z ^ 2) * (q + q⁻¹) := by ring
    _ = 1 * (q + q⁻¹) := by rw [h]
    _ = q + q⁻¹ := one_mul _

end Scalars

section Kauffman

variable {R : Type*} [Field R]

/-- **The Kauffman dictionary.** With `a := A² = −q`, the bracket loop value
`−A² − A⁻²` is `[2]_q`.

Hence `t = A⁻⁴ = q⁻²`. Note `A` itself is a square root of `−q` and does *not*
appear in the final normalisation: the odd powers of `A` in `ρ(σᵢ) = (A/q)σᵢ` and
in the writhe factor `(−A³)^{-e}` cancel, leaving `q^{-2e}`. The half-argument
quantity `q^{1/2} + q^{-1/2}` never enters. -/
theorem kauffman_loop (q : R) (hq : q ≠ 0) :
    -(-q) - (-q)⁻¹ = q + q⁻¹ := by
  field_simp
  ring

/-- **The framing factor has no square roots.** `[(A/q)·(−A³)⁻¹]^e = q^{-2e}`,
written with `a = A² = −q` so that only even powers of `A` appear:
`(A/q)·(−A³)⁻¹ = −1/(q·A²) = −1/(q·(−q)) = q⁻²`. -/
theorem framing_factor (q : R) (hq : q ≠ 0) :
    -(1 / (q * (-q))) = (q⁻¹) ^ 2 := by
  field_simp

end Kauffman

end QOU.QBeta.JonesNormalisation
