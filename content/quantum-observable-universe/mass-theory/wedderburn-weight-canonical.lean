import Mathlib.Algebra.Field.Basic

/-!
# QOU.BraidKnot.wedderburnWeightCanonical

The q-deformed Wedderburn-block weight `tilde w_λ = dim_q(λ)² / [n]_q!`
is the canonical combinatorial coefficient associated with each
partition `λ ⊢ n` in the Hecke algebra `H_n(R, q)`.

The BW and LP scalings are definitional for every λ:

  β_λ := -½ tilde w_λ                    (BW form, all λ)
  C_λ := tilde w_λ · h/2,  h = q - q⁻¹   (LP shadow-price, all λ)

The Markov coefficient `y_λ(q)` is given by Wenzl's hook–content
closed form [wenzl1988]; on the self-conjugate stratum
(`κ_λ = Σ c(x) = 0`) it coincides with `tilde w_λ`:

  y_λ = tilde w_λ                         (Wenzl-bridge, κ_λ = 0)

Off the self-conjugate stratum, `y_λ` and `tilde w_λ` are genuinely
distinct weight families — the in-repo witness
`computations/probe-wedderburn-weight-scheme.witness.json`
records `|y_λ / tilde w_λ|` ratios from ≈0.14 to ≈2.54 at q₀ for
n ∈ {2, 3}.

The BW/LP scaling ratios — verified symbolically in
`computations/_deprecated/bw_wenzl_shadow_equivalence.py`
for `λ = (2,2)` and `λ = (3,2,1)` (both self-conjugate) — are:

  β / C = -1/h        (all λ)
  β / y = -1/2        (self-conjugate λ only)
  C / y = h/2         (self-conjugate λ only)

**Pre-Archimedean stub.** Polymorphic in the ground field `R`.
The previous version typed every coefficient to `ℝ`; the
canonical Wedderburn weight is `q`-rational (a Laurent
polynomial / element of `ℚ(q)`), not a real number.  The
Archimedean specialisation `q ↦ q₀ ∈ ℝ` is downstream
(`QOU.Calculations`).

Ref: [jones1985] https://doi.org/10.2307/1971403
Ref: [wenzl1988] https://doi.org/10.1007/BF01393378
Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

namespace QOU.BraidKnot

universe u

/-- A partition (placeholder; the canonical weight is parameterised
    over an abstract partition type so the discipline holds for any
    realisation). -/
structure Partition where
  parts : List ℕ
  -- Could add: parts.Sorted (· ≥ ·), parts.all (· > 0)

/-- The canonical Wedderburn-block weight discipline, polymorphic in
    the ground field `R`.

    An instance asserts:
      • the BW mass coefficient `β_λ = -½ tilde w_λ` (for all λ);
      • the LP shadow-price `C_λ = tilde w_λ · h/2` (for all λ);
      • the Markov coefficient `y_λ`, with the **self-conjugate
        Wenzl-bridge identity** `y_λ = tilde w_λ` whenever `κ_λ = 0`.

    Off the self-conjugate stratum, `y_λ` is given by Wenzl's
    hook–content closed form [wenzl1988] and is, in general,
    distinct from `(-1)^κ_λ · tilde w_λ` — see the in-repo witness
    `probe-wedderburn-weight-scheme.witness.json` for empirical
    `|y_λ / tilde w_λ|` ratios at `q₀`. -/
class WedderburnWeightCanonical (R : Type u) [Field R] where
  /-- The Hecke-generator scalar `h = q - q⁻¹` in `R`. -/
  h : R
  /-- The canonical q-deformed Wedderburn weight `tilde w_λ ∈ R`
      (Laurent in `q`). -/
  w : Partition → R
  /-- Content sum `κ_λ`. -/
  kappa : Partition → ℤ
  /-- BW mass coefficient `β_λ = -½ tilde w_λ`. -/
  beta : Partition → R
  /-- LP shadow-price `C_λ = tilde w_λ · h/2`. -/
  C : Partition → R
  /-- Markov coefficient `y_λ(q)` (Wenzl closed form; abstract
      here, supplied per instance). -/
  y : Partition → R
  /-- BW scaling identity (all λ). -/
  beta_eq : ∀ λ, beta λ = -(1 / 2 : R) * w λ
  /-- LP shadow-price scaling identity (all λ). -/
  C_eq : ∀ λ, C λ = w λ * (h / 2)
  /-- **Wenzl-bridge identity, restricted to self-conjugate λ.**
      Whenever `κ_λ = 0`, the Markov coefficient agrees with the
      Wedderburn-block weight: `y_λ = tilde w_λ`. -/
  y_eq_self_conjugate : ∀ λ, kappa λ = 0 → y λ = w λ

/-- For self-conjugate partitions (κ = 0), the Markov coefficient
    coincides with the Wedderburn-block weight. -/
theorem WedderburnWeightCanonical.y_self_conjugate
    {R : Type u} [Field R] [c : WedderburnWeightCanonical R]
    (λ : Partition) (h_self : c.kappa λ = 0) :
    c.y λ = c.w λ :=
  c.y_eq_self_conjugate λ h_self

/-- Cross-ratio: `β / C = -1/h` (when `C ≠ 0`). -/
theorem WedderburnWeightCanonical.beta_over_C
    {R : Type u} [Field R] [c : WedderburnWeightCanonical R]
    (λ : Partition) (hC : c.C λ ≠ 0) (hh : c.h ≠ 0) :
    c.beta λ / c.C λ = -(1 / c.h) := by
  rw [c.beta_eq, c.C_eq]
  -- β/C = (-½ w) / (w · h/2) = -1/h, provided w ≠ 0 (which
  -- follows from C ≠ 0 since C = w · h/2 and h ≠ 0).
  have hw : c.w λ ≠ 0 := by
    intro h_w
    apply hC
    rw [c.C_eq, h_w, zero_mul]
  field_simp
  ring

end QOU.BraidKnot
