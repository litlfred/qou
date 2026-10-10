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
closed form [wenzl1988].  This file **no longer asserts any relation**
between `y_λ` and `tilde w_λ`: the "Wenzl-bridge identity"
`y_λ = tilde w_λ` on the self-conjugate stratum (`κ_λ = Σ c(x) = 0`),
once carried here as a class field, is false at the intended values
(measurement below) and was **dropped on the owner's ruling,
2026-09-04** (option A of the three dispositions recorded in the
narrative block).  `y_λ` and `tilde w_λ` are distinct weight families
on every stratum; `y` stays in the class only as abstract data.

**⚠ CORRECTED 2026-09-02, twice over.**

First, the citation.  This paragraph previously cited
`computations/probe-wedderburn-weight-scheme.witness.json` for
`|y_λ / tilde w_λ|` ratios "from ≈0.14 to ≈2.54 at q₀".  That file does
not exist and `git log --all` shows it never existed in tracked history,
so it was the only evidence offered for a claim nothing backed.

Second, and more seriously, the former field `y_eq_self_conjugate` (the
Wenzl-bridge identity `y_λ = tilde w_λ` on `κ_λ = 0`) is **FALSE at the
intended values**.  Measured at every κ = 0 partition with n ≤ 6, in the
production convention D *and* in the excised convention C, the identity
holds only at the trivial `λ = (1)`:

    λ          y^D(q₀)      y^C(q₀)      tilde w(q₀)
    (1)        1.00000000   1.00000000   1.00000000
    (2,1)      0.24729789   0.28092963   0.66067377
    (2,2)      0.06115624   0.06947330   0.16604895
    (3,1,1)    0            0.01676661   0.29466896
    (3,2,1)    0            0.00731845   0.35863564

`(2,2)` and `(3,2,1)` are exactly the two partitions the cited script
`bw_wenzl_shadow_equivalence.py` is said to have verified.  The last two
rows are a **structural** exclusion: convention D is the `𝔰𝔩₂` point of
the Ocneanu family, so `y_λ = 0` once λ has more than two rows (a cell of
content -2 kills the numerator —
`QOU.Information.ocneanu_numerator_vanishes_at_content_neg`), while
`tilde w_λ > 0` as a ratio of positive quantum integers.  The identity
asserts `0 = positive`; no parameter reconciles it.

**Disposition (owner ruling, 2026-09-04): the field is DROPPED**, together
with its projection theorem `y_self_conjugate`.  It was left standing
from 2026-09-02 to 2026-09-04 because the choice between restricting it
to `λ = (1)`, dropping it, and demoting the block was the author's, not a
mechanical fix; the author chose to drop.  `beta_mul_h_eq_neg_C` below
never read the `y` field, so the BW/LP scalings are unaffected, and the
class is now inhabitable at the honest data.  Measurement:
`computations/probes/wenzl_bridge_self_conjugate_premise_is_false.py`
(10/10).

The BW/LP scaling ratio — verified symbolically in
`fsh-guts/deprecated/computations/bw_wenzl_shadow_equivalence.py`
for `λ = (2,2)` and `λ = (3,2,1)` (both self-conjugate) — is

  β / C = -1/h        (all λ),

recorded here in its division-free ("R[h]") form `β · h = -C`, which is
what actually holds in the coefficient ring; dividing recovers the ratio
whenever `C ≠ 0` and `h ≠ 0`.  The former companions
`β / y = -1/2` and `C / y = h/2` depended on `y = w` and fall with it;
they are not asserted anywhere.

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
      • the LP shadow-price `C_λ = tilde w_λ · h/2` (for all λ).

    It carries the Markov coefficient `y_λ` (Wenzl's hook–content closed
    form [wenzl1988]) as **data only**.  The self-conjugate Wenzl-bridge
    identity `y_λ = tilde w_λ` on `κ_λ = 0` was a field here until
    2026-09-04; it is false at the intended values (module docstring) and
    was dropped on the owner's ruling.  No relation between `y` and `w`
    is asserted. -/
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
      here, supplied per instance).  Data only — no axiom relates it
      to `w`; see the module docstring for the dropped identity. -/
  y : Partition → R
  /-- BW scaling identity (all λ). -/
  beta_eq : ∀ lam, beta lam = -(⅟(2 : R)) * w lam
  /-- LP shadow-price scaling identity (all λ). -/
  C_eq : ∀ lam, C lam = w lam * (⅟(2 : R) * h)

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
