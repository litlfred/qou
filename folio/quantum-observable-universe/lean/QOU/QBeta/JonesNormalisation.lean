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

## Why this is a link invariant at all — and why D is forced

An earlier version of this file checked the formula on four closures and noted
that the closure identifications (`cl(σ₁σ₂) ⊂ B₃` is the unknot, and so on) were
taken from standard theory rather than derived. That caveat is now unnecessary,
and the reason is better than a formalisation of knot topology would have been.

By **Markov's theorem**, two braids have the same closure exactly when they are
related by conjugation and by stabilisation `β ∈ B_n ↦ βσ_n^{±1} ∈ B_{n+1}`. So a
function of `(β, e, n)` that is invariant under those moves *is* a link
invariant — no knots required. All three checks are algebra:

* **Conjugation.** `e` and `n` do not change, and `tr_M` is cyclic
  (`jonesV_conj`). Free, for any Markov parameter.
* **Positive stabilisation.** `e ↦ e+1`, `n ↦ n+1`,
  `tr_M(βσ_n) = z·tr_M(β)`. Invariance is exactly `q⁻²·[2]_q·z = 1`
  (`jonesV_stabilise_pos`).
* **Negative stabilisation.** `e ↦ e−1`, `n ↦ n+1`. From the quadratic relation
  `σ⁻¹ = σ − h` (`sigma_inv`), so `tr_M(βσ_n⁻¹) = (z−h)·tr_M(β)`, and invariance
  is exactly `q²·[2]_q·(z−h) = 1` (`jonesV_stabilise_neg`).

Both stabilisation conditions are not merely *satisfied by* convention D — each
one, on its own, **forces** it (`stab_pos_iff_conventionD`,
`stab_neg_iff_conventionD`, needing only `q ≠ 0`). That is the theorem this file
is really about:

> **Convention D is the unique Markov parameter for which
> `q^{-2e}[2]_q^{n-1}tr_M` is a link invariant.**

`markov-pair-z2`'s prefactor `q^{1/2}+q^{-1/2}` is not a near-miss under this
statement; with it the quantity is not an invariant of anything, because it fails
to survive a stabilisation move.

The four closure values are then corollaries worth keeping as sanity checks —
they confirm the invariant is normalised so that the unknot is `1` — but they are
no longer load-bearing, and nothing here assumes which link a given braid closes
to.
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

/-- **The inverse braid generator is `σ − h`.** From the quadratic relation
alone: `σ(σ − h) = σ² − σh = (hσ + 1) − hσ = 1`, and symmetrically on the left.

This is what makes negative stabilisation computable without ever inverting
anything: `tr_M(σ⁻¹) = z − h`. -/
theorem sigma_inv (q : R) (s : A)
    (hs : s * s = algebraMap R A (q - q⁻¹) * s + 1) :
    s * (s - algebraMap R A (q - q⁻¹)) = 1 ∧
      (s - algebraMap R A (q - q⁻¹)) * s = 1 := by
  have hcom : s * algebraMap R A (q - q⁻¹) = algebraMap R A (q - q⁻¹) * s :=
    (Algebra.commutes _ s).symm
  constructor
  · rw [mul_sub, hs, hcom]; abel
  · rw [sub_mul, hs]; abel

end TLGenerator

section Scalars

variable {R : Type*} [Field R]

/-! ### The normalisation, as scalar identities

`V(β̂) = q^{-2e} · [2]_q^{n-1} · tr_M(β)` evaluated on four closures whose Jones
polynomials are known independently. Each is stated under `IsConventionD` and
under nothing else, so each is a check that convention D — and not merely *some*
Markov parameter — is what makes the normalisation land. -/

/-- The Jones normalisation factor `q^{-2e} · [2]_q^{m}`, where **`m = n − 1`**
is the strand count less one.

Carrying `m` rather than `n` is deliberate: `n - 1` in `ℕ` is truncated
subtraction, which would silently do the wrong thing at `n = 0` and force a side
condition on every lemma. With `m` the stabilisation moves are `m ↦ m + 1` and
nothing is ever subtracted. -/
noncomputable def jonesFactor (q : R) (e m : ℕ) : R :=
  (q⁻¹) ^ (2 * e) * (q + q⁻¹) ^ m

/-- The normalised invariant `V = q^{-2e}·[2]_q^{m}·tr`, with `tr` the Markov
trace of the braid and `m = n − 1`. -/
noncomputable def jonesV (q : R) (e m : ℕ) (tr : R) : R := jonesFactor q e m * tr

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

section MarkovInvariance

variable {R : Type*} [Field R]

/-! ### Markov invariance — the reason this is a link invariant

Markov's theorem: braid closures coincide exactly under conjugation and
stabilisation. So invariance under those two moves makes `jonesV` a link
invariant, with no knot theory in the statement. Each move turns out to *force*
convention D. -/

/-- **Positive stabilisation ⟺ convention D.** The move
`β ∈ B_n ↦ βσ_n ∈ B_{n+1}` sends `e ↦ e+1`, `m ↦ m+1` and multiplies the trace
by `z`. Invariance is the single identity `q⁻²·[2]_q·z = 1` — and that identity
is equivalent to `z(q²+1) = q³`.

Only `q ≠ 0` is needed in either direction; no `q² + 1 ≠ 0` side condition,
because if `q² + 1 = 0` then `[2]_q = 0` and both sides are false. -/
theorem stab_pos_iff_conventionD (q z : R) (hq : q ≠ 0) :
    (q⁻¹) ^ 2 * (q + q⁻¹) * z = 1 ↔ IsConventionD q z := by
  unfold IsConventionD
  constructor <;> intro h
  · field_simp at h
    linear_combination h
  · field_simp
    linear_combination h

/-- **Negative stabilisation ⟺ convention D.** The move
`β ↦ βσ_n⁻¹` sends `e ↦ e−1`, `m ↦ m+1`, and by `sigma_inv` multiplies the trace
by `z − h`. Invariance is `q²·[2]_q·(z−h) = 1`, again equivalent to convention D.

That the two stabilisations force the *same* `z` is not automatic — it is a
consistency check on the whole normalisation, and it passes. -/
theorem stab_neg_iff_conventionD (q z : R) (hq : q ≠ 0) :
    q ^ 2 * (q + q⁻¹) * (z - (q - q⁻¹)) = 1 ↔ IsConventionD q z := by
  unfold IsConventionD
  constructor <;> intro h
  · -- Cancel the `q` on the goal rather than dividing the hypothesis by it:
    -- `linear_combination h / q` would introduce `q⁻¹`, which `ring` cannot
    -- discharge without knowing `q * q⁻¹ = 1`.
    field_simp at h
    apply mul_left_cancel₀ hq
    linear_combination h
  · field_simp
    linear_combination q * h

/-- **`jonesV` is invariant under positive stabilisation.** `e ↦ e+1`,
`m ↦ m+1`, `tr ↦ z·tr`. -/
theorem jonesV_stabilise_pos (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z)
    (e m : ℕ) (tr : R) :
    jonesV q (e + 1) (m + 1) (z * tr) = jonesV q e m tr := by
  have hz : (q⁻¹) ^ 2 * (q + q⁻¹) * z = 1 := (stab_pos_iff_conventionD q z hq).mpr hD
  unfold jonesV jonesFactor
  calc (q⁻¹) ^ (2 * (e + 1)) * (q + q⁻¹) ^ (m + 1) * (z * tr)
      = ((q⁻¹) ^ 2 * (q + q⁻¹) * z) * ((q⁻¹) ^ (2 * e) * (q + q⁻¹) ^ m * tr) := by
        rw [Nat.mul_succ, pow_add, pow_succ]; ring
    _ = (q⁻¹) ^ (2 * e) * (q + q⁻¹) ^ m * tr := by rw [hz, one_mul]

/-- **`jonesV` is invariant under negative stabilisation.** `e ↦ e−1`,
`m ↦ m+1`, `tr ↦ (z−h)·tr`. Stated with the source exponent as `e + 1` so that
the target is `e` — no truncated subtraction anywhere. -/
theorem jonesV_stabilise_neg (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z)
    (e m : ℕ) (tr : R) :
    jonesV q e (m + 1) ((z - (q - q⁻¹)) * tr) = jonesV q (e + 1) m tr := by
  have hz : q ^ 2 * (q + q⁻¹) * (z - (q - q⁻¹)) = 1 :=
    (stab_neg_iff_conventionD q z hq).mpr hD
  have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  unfold jonesV jonesFactor
  have expand : (q⁻¹) ^ (2 * (e + 1)) = (q⁻¹) ^ (2 * e) * ((q⁻¹) ^ 2) := by
    rw [Nat.mul_succ, pow_add]
  rw [expand, pow_succ]
  have key : (q + q⁻¹) * (z - (q - q⁻¹)) = (q⁻¹) ^ 2 := by
    have h2 : q ^ 2 * ((q + q⁻¹) * (z - (q - q⁻¹))) = 1 := by
      rw [← hz]; ring
    field_simp at h2 ⊢
    linear_combination h2
  calc (q⁻¹) ^ (2 * e) * ((q + q⁻¹) ^ m * (q + q⁻¹)) * ((z - (q - q⁻¹)) * tr)
      = (q⁻¹) ^ (2 * e) * (q + q⁻¹) ^ m * ((q + q⁻¹) * (z - (q - q⁻¹))) * tr := by ring
    _ = (q⁻¹) ^ (2 * e) * (q + q⁻¹) ^ m * ((q⁻¹) ^ 2) * tr := by rw [key]
    _ = (q⁻¹) ^ (2 * e) * ((q⁻¹) ^ 2) * (q + q⁻¹) ^ m * tr := by ring

/-- **Conjugation invariance.** `e` and `m` are unchanged by conjugation and the
trace is cyclic, so nothing needs proving beyond transporting the trace equality.
Recorded because Markov's theorem needs *both* moves, and it costs one line —
leaving it implicit would make the invariance argument look narrower than it is.

Holds for any Markov parameter; it is the stabilisation moves, not this one, that
pin convention D. -/
theorem jonesV_conj (q : R) (e m : ℕ) (tr₁ tr₂ : R) (hcyc : tr₁ = tr₂) :
    jonesV q e m tr₁ = jonesV q e m tr₂ := by rw [hcyc]

/-- **The characterisation.** Bringing the two together: the normalisation
survives both stabilisation moves **iff** the Markov parameter is convention D.

With `jonesV_conj` and Markov's theorem this says convention D is the *unique*
Markov parameter for which `q^{-2e}[2]_q^{n-1}tr_M` is a link invariant. The
uniqueness is the part that matters for the excision: a wrong loop parameter does
not give a slightly-off invariant, it gives something that is not an invariant. -/
theorem conventionD_iff_markov_invariant (q z : R) (hq : q ≠ 0) :
    ((q⁻¹) ^ 2 * (q + q⁻¹) * z = 1 ∧ q ^ 2 * (q + q⁻¹) * (z - (q - q⁻¹)) = 1)
      ↔ IsConventionD q z := by
  constructor
  · rintro ⟨hp, -⟩
    exact (stab_pos_iff_conventionD q z hq).mp hp
  · intro hD
    exact ⟨(stab_pos_iff_conventionD q z hq).mpr hD,
           (stab_neg_iff_conventionD q z hq).mpr hD⟩

end MarkovInvariance

section InterfaceFactorisation

variable {R : Type*} [CommRing R] {A : Type*} [Ring A]

/-! ### The interface factorisation `z^{p₊}(z−h)^{p₋}`

`prf:interface-knot-markov-z` claims

    tr_M^FULL / tr_M^CONSTIT  =  z^{p₊} · (z − h)^{p₋}

for an atom with `p₊` positive and `p₋` negative interface crossings. That claim
is **convention-independent** — it is iterated Markov peel and holds for any
Markov parameter — which is why regenerating its table under convention D should
reproduce agreement to the same precision rather than break it. The two
per-crossing factors are `tr_M(σ) = z` and `tr_M(σ⁻¹) = z − h`, the latter from
`sigma_inv` (`σ⁻¹ = σ − h`, from the quadratic relation alone). -/

/-- **Iterated Markov peel.** One peel hypothesis, applied `k` times. -/
theorem peel_pow (tr : A → R) (z : R) (s : A)
    (hpeel : ∀ y : A, tr (y * s) = z * tr y) (x : A) (k : ℕ) :
    tr (x * s ^ k) = z ^ k * tr x := by
  induction k with
  | zero => simp
  | succ n ih =>
      calc tr (x * s ^ (n + 1)) = tr (x * s ^ n * s) := by rw [pow_succ, mul_assoc]
        _ = z * tr (x * s ^ n) := hpeel _
        _ = z * (z ^ n * tr x) := by rw [ih]
        _ = z ^ (n + 1) * tr x := by ring

/-- **The interface factorisation.** `p₊` positive crossings contribute `z` each,
`p₋` negative ones contribute `w = z − h` each, multiplicatively.

Stated with the crossings already gathered at the peelable end, because that is
what the Markov axiom licenses: `tr(y·σₙ) = z·tr(y)` needs `σₙ` to be the *top*
generator, outside the subalgebra `y` lives in. That the interface crossings of a
nuclear braid can be brought into that position is the physical input of
`prf:interface-knot-markov-z` — a claim about `atom_braid_word_3A`, not about the
trace — and is **not** proved here. What is proved is that once they are, the
factorisation is exact, and exact for *every* Markov parameter. -/
theorem interface_factorisation (tr : A → R) (z w : R) (sp sm : A)
    (hp : ∀ y : A, tr (y * sp) = z * tr y)
    (hm : ∀ y : A, tr (y * sm) = w * tr y)
    (x : A) (p m : ℕ) :
    tr (x * sp ^ p * sm ^ m) = z ^ p * w ^ m * tr x := by
  rw [peel_pow tr w sm hm _ m, peel_pow tr z sp hp x p]
  ring

end InterfaceFactorisation

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


section ConventionDLoopGap

variable {R : Type*} [Field R]

/-- **Structural separation between convention-D `z` and the loop reciprocal `1 / [2]_q` (`qou-98g5`).**
Under `IsConventionD q z` (`z = q³ / (q² + 1)`), the loop reciprocal `tr_M(e_i) = q - z` equals
`q / (q² + 1)`, so the gap `z - (q - z)` equals `q * (q² - 1) / (q² + 1)` and their sum is `q`. -/
theorem conventionD_loop_reciprocal_and_gap (q z : R) (hq : q ≠ 0) (hD : IsConventionD q z) :
    q - z = q / (q ^ 2 + 1) ∧
      z - (q - z) = q * (q ^ 2 - 1) / (q ^ 2 + 1) ∧
      z + (q - z) = q := by
  have hne := q_sq_add_one_ne_zero q z hq hD
  refine ⟨?_, ?_, by ring⟩
  · rw [z_eq_div q z hq hD]
    field_simp
    ring
  · rw [z_eq_div q z hq hD]
    field_simp
    ring

end ConventionDLoopGap

end QOU.QBeta.JonesNormalisation
