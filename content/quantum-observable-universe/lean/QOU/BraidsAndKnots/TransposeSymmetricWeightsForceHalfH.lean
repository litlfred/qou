import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# Transpose-symmetric normalised weights force the Markov parameter to `h/2`

`mass_at_3A_proper.per_generator_V_hat_3A` builds its per-generator V̂ as a
weighted character sum over `λ ⊢ 3A`.  Factoring the collapse out
(`QOU.BraidsAndKnots.prod_eq_linear`) leaves

    V̂_i = α_i · Z + β_i · W,    Z = Σ_λ ω_λ · tr(σ^λ)/dim λ,   W = Σ_λ ω_λ

so `Z` is the effective Markov parameter the whole tower is affine in
(`QOU.BraidsAndKnots.vHat_sub_vHat`), and it is the only place a Markov-
parameter convention could enter.

**Measured** (`computations/probes/tower_vhat_markov_parameter_probe.py`,
50 dps): under the production `normalized_plancherel` scheme

    Z = 0.10453014939781965771542…

**identically at n = 3, 6 and 9** — while the *unnormalised* Plancherel scheme
gives a visibly `n`-dependent `Z` (0.10321727… at n = 3, 0.10359769… at n = 6).
And that value is not a coincidence: it is `(q − q⁻¹)/2 = h/2`, agreeing to the
full precision of the measurement.

This file says why, and the reason turns out to need nothing about Plancherel
weights, Hecke algebras, or partitions.  Two hypotheses suffice:

* the weights are **normalised**, `Σ_λ ω_λ = 1`; and
* they are **transpose-symmetric**, `ω_{λ'} = ω_λ`, together with the
  corresponding fact about the traces — transposing a shape exchanges the two
  Hecke eigenvalues `q` and `−q⁻¹`, so the `±` multiplicities swap and

      tr(σ^λ)/dim λ  +  tr(σ^{λ'})/dim λ'
        = ((m₊ q − m₋ q⁻¹) + (m₋ q − m₊ q⁻¹)) / dim λ
        = (m₊ + m₋)(q − q⁻¹) / dim λ
        = h.

`markov_param_eq_half_h` is then a two-line reindexing argument.

## What this settles, and what it does not

**Settles.** The C-vs-D Markov-parameter question does not reach this producer.
Convention C is `√q/(q+1) ≈ 0.4993`, convention D is `q³/(q²+1) ≈ 0.6127`, and
this scheme is pinned by its own symmetry to `h/2 ≈ 0.1045` — 79 % below C and
83 % below D.  So the Φ_q pole that `per_generator_V_hat_3A` runs into
(bean `qou-2tuv`; V̂ up to 1.0884 against `q = 1.1100`) is **not** an instance of
the C→D cascade recorded on bean `qou-dchz`, and re-pinning the convention
cannot move it.  The pole distance is set by `α_i`, not by `Z`.

**Does not settle.** Whether `h/2` is the *right* Markov parameter here.
`normalized_plancherel_weights_3A`'s own docstring already concedes it does
"not match the canonical Jones parameter z for tr_M(σ_i)", and
`per_generator_V_hat_3A`'s says of its two weight schemes that "both are wrong
for the tower … picking between them is not the fix".  This is scope-(a)
throughout: it measures and explains the construction as built, and excludes no
ingredient.

A corollary worth stating separately: because the conclusion needs only
normalisation and transpose symmetry, **every** normalised transpose-symmetric
scheme gives the same `Z`.  Searching that family for one that moves the pole is
therefore pointless — `markov_param_indep_of_weights` says so.
-/

namespace QOU.BraidsAndKnots

open Finset

/-- **Transpose-symmetric normalised weights force `Z = h/2`.**

`τ` is transposition on shapes (any involution would do — the proof uses only
that it is a bijection); `w` the weights; `t λ = tr(σ^λ)/dim λ`.

The hypothesis `ht` is the eigenvalue-exchange fact: transposing a shape swaps
the multiplicities of `q` and `−q⁻¹`, so the two normalised traces sum to
`h = q − q⁻¹` regardless of what those multiplicities are.  Nothing else about
the representation is used.

`two_ne` is not decoration: the argument pairs `λ` with `λ'` and halves, so in
characteristic 2 there is no `h/2` to land on and the statement is empty.  It is
carried explicitly rather than as `[CharZero R]` because that is the whole of
what the proof needs. -/
theorem markov_param_eq_half_h
    {ι : Type*} [Fintype ι] {R : Type*} [Field R]
    (w t : ι → R) (h : R) (τ : ι ≃ ι) (two_ne : (2 : R) ≠ 0)
    (hw : ∀ i, w (τ i) = w i)
    (ht : ∀ i, t i + t (τ i) = h)
    (hsum : ∑ i, w i = 1) :
    ∑ i, w i * t i = h / 2 := by
  have reindex : ∑ i, w (τ i) * t (τ i) = ∑ i, w i * t i :=
    Equiv.sum_comp τ (fun i => w i * t i)
  have two_mul : (2 : R) * ∑ i, w i * t i = h := by
    calc (2 : R) * ∑ i, w i * t i
        = (∑ i, w i * t i) + ∑ i, w (τ i) * t (τ i) := by rw [reindex]; ring
      _ = ∑ i, (w i * t i + w i * t (τ i)) := by
            rw [← Finset.sum_add_distrib]
            exact Finset.sum_congr rfl fun i _ => by rw [hw]
      _ = ∑ i, w i * h :=
            Finset.sum_congr rfl fun i _ => by rw [← mul_add, ht]
      _ = h := by rw [← Finset.sum_mul, hsum, one_mul]
  rw [eq_div_iff two_ne]
  linear_combination two_mul

/-- **Corollary: the value does not depend on which such scheme you pick.**

Two normalised transpose-symmetric weightings of the same trace data give the
same effective Markov parameter — so no search within that family can move
`Z`, and hence (by `vHat_sub_vHat`) none can move V̂ either.  Recorded because
the natural response to a Φ_q pole is to reach for a different weight scheme,
and this says which reaches are futile before any of them is coded. -/
theorem markov_param_indep_of_weights
    {ι : Type*} [Fintype ι] {R : Type*} [Field R]
    (w w' t : ι → R) (h : R) (τ : ι ≃ ι) (two_ne : (2 : R) ≠ 0)
    (hw : ∀ i, w (τ i) = w i) (hw' : ∀ i, w' (τ i) = w' i)
    (ht : ∀ i, t i + t (τ i) = h)
    (hsum : ∑ i, w i = 1) (hsum' : ∑ i, w' i = 1) :
    ∑ i, w i * t i = ∑ i, w' i * t i := by
  rw [markov_param_eq_half_h w t h τ two_ne hw ht hsum,
      markov_param_eq_half_h w' t h τ two_ne hw' ht hsum']

/-- The eigenvalue-exchange hypothesis is not an assumption about Plancherel
weights but an identity: if `λ` carries `m₊` copies of `q` and `m₋` of `−q⁻¹`,
and `λ'` carries them the other way round, the normalised traces sum to `h`.

Stated for the raw multiplicities so the arithmetic is checkable, with `d` the
common dimension `m₊ + m₋`. -/
theorem trace_pair_sum_eq_h
    {R : Type*} [Field R] (q : R) (hq : q ≠ 0) (mp mm d : R) (hd : d ≠ 0)
    (hsum : mp + mm = d) :
    (mp * q - mm * q⁻¹) / d + (mm * q - mp * q⁻¹) / d = q - q⁻¹ := by
  field_simp
  linear_combination (q * q - 1) * hsum

end QOU.BraidsAndKnots
