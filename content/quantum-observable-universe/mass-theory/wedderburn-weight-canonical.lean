import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Invertible.Defs
import Mathlib.Tactic.Ring

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

The BW/LP scaling ratio — verified symbolically in
`computations/_deprecated/bw_wenzl_shadow_equivalence.py`
for `λ = (2,2)` and `λ = (3,2,1)` (both self-conjugate) — is

  β / C = -1/h        (all λ),

recorded here in its division-free ("R[h]") form `β · h = -C`, which is
what actually holds in the coefficient ring; dividing recovers the ratio
whenever `C ≠ 0` and `h ≠ 0`.  The companions
`β / y = -1/2` and `C / y = h/2` hold on the self-conjugate stratum only,
via `y = w`.

**Pre-Archimedean stub.**  Base ring (§7c): the previous version typed
every coefficient to `ℝ`, then to a generic `[Field R]`; neither is
needed.  The canonical Wedderburn weight is `q`-rational (Laurent in `q`),
and the *only* division in the whole file is by `2`, so the carrier is a
generic `[CommRing R]` with `[Invertible (2 : R)]` and `⅟(2 : R)` in
place of `1/2` — satisfied by `ℤ[1/2][q^{±1}]`, by `ℚ(q)`, and by any
field of characteristic `≠ 2` (`invertibleOfNonzero`, the former
`[CharZero R]` route).  `h = q - q⁻¹` is carried as an opaque ring
element, so no inverse of `q` is needed here either.  The Archimedean
specialisation `q ↦ q₀ ∈ ℝ` is downstream (`QOU.Calculations`).

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
    the ground ring `R`.

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
class WedderburnWeightCanonical (R : Type u) [CommRing R]
    [Invertible (2 : R)] where
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
  beta_eq : ∀ lam, beta lam = -(⅟(2 : R)) * w lam
  /-- LP shadow-price scaling identity (all λ). -/
  C_eq : ∀ lam, C lam = w lam * (⅟(2 : R) * h)
  /-- **Wenzl-bridge identity, restricted to self-conjugate λ.**
      Whenever `κ_λ = 0`, the Markov coefficient agrees with the
      Wedderburn-block weight: `y_λ = tilde w_λ`. -/
  y_eq_self_conjugate : ∀ lam, kappa lam = 0 → y lam = w lam

/-- For self-conjugate partitions (κ = 0), the Markov coefficient
    coincides with the Wedderburn-block weight. -/
theorem WedderburnWeightCanonical.y_self_conjugate
    {R : Type u} [CommRing R] [Invertible (2 : R)]
    [c : WedderburnWeightCanonical R]
    (lam : Partition) (h_self : c.kappa lam = 0) :
    c.y lam = c.w lam :=
  c.y_eq_self_conjugate lam h_self

/-- **Cross-ratio, division-free form**: `β · h = -C` for every `λ`.

    This is the multiplicative relation behind `β / C = -1/h`: in a
    field, dividing by `C ≠ 0` and `h ≠ 0` recovers the ratio form, and
    conversely.  Stated multiplicatively it needs *no* nonvanishing
    hypotheses at all — both sides are `-½ · w_λ · h` — so it holds in
    the coefficient ring where the weights actually live. -/
theorem WedderburnWeightCanonical.beta_mul_h_eq_neg_C
    {R : Type u} [CommRing R] [Invertible (2 : R)]
    [c : WedderburnWeightCanonical R] (lam : Partition) :
    c.beta lam * c.h = -(c.C lam) := by
  rw [c.beta_eq, c.C_eq]
  ring

end QOU.BraidKnot
