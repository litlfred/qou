import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Algebra.Group.Invertible.Defs

/-!
# QOU.BraidKnot.MassCoefficientShadowPrice

Each QOU mass-formula coefficient is the **shadow price** (LP dual variable) of
the corresponding partition's Frobenius positivity constraint in the nuclear
operator-selection LP.  By strong duality + complementary slackness
(`prop:operator-selection-lp`), the optimal dual variable factorises as

  u_λ* = C_λ · S_λ(Z,N,A),      C_λ = tilde w_λ · h/2,   h = q - q⁻¹

where `C_λ` is the **partition-only** LP shadow-price coefficient (the same
`C_λ` as in `prop:wedderburn-weight-canonical`) and `S_λ` is the
nuclear-datum **scaling function** (classified by the content sum `c(λ)`:
`>0` volume-type, `=0` isospin-type, `<0` charge-type).  The total binding is

  B(Z,N) = (Σ_λ C_λ · S_λ) · m_e,

and at the normalisation point `S_λ = 1` the shadow price equals `C_λ`.

## What is axiomatised vs. derived

The **LP-duality content** — that the optimal dual variables ARE the mass
coefficients (strong duality + complementary slackness over the block-diagonal
Frobenius Gram matrix `G_λ = (w_λ/d_λ) I`) — is recorded in the class fields
`C_eq` and `factor`, cited to `prop:operator-selection-lp`.  The **algebraic
consequences** are then DERIVED sorry-free:

  • `shadow_price_weight_form` — the canonical-weight form
    `u_λ* = tilde w_λ · (h·⅟2) · S_λ` (combines `factor` and `C_eq`);
  • `normalization` — at `S_λ = 1`, `u_λ* = C_λ`;
  • `coefficient_nuclear_independent` — `C_λ` is independent of the nuclear
    datum (`u_λ* · S_λ⁻¹ = C_λ` whenever `S_λ` is a unit).

**Pre-Archimedean.  Base ring (§7c): a commutative ring `R`, not a field.**
`C_λ` is `q`-rational (Laurent in `q`), not a real number; the Archimedean
specialisation `q ↦ q₀ ∈ ℝ` is downstream (`QOU.Calculations`).  The two
inverses the statements need are carried explicitly rather than by importing a
field:

* the halving in `C_λ = tilde w_λ · h/2` is the single ring constant `2`, so it
  is carried as `[Invertible (2 : R)]` and written `⅟(2 : R)`.  This is exactly
  the "ground ring contains ½" hypothesis — true of `ℚ(q)` and `ℝ`, false of
  `ℤ[q, q⁻¹]` — made explicit instead of hidden inside `Field`;
* the division by the scaling function in `coefficient_nuclear_independent`
  needs `S_λ` invertible, which over a field is the old `S_λ ≠ 0`; it is now
  carried as a unit `s : Rˣ` pinned by `S_λ = ↑s`.

Note `h = q − q⁻¹` is itself an abstract class field, so no `q⁻¹` is formed here.

Ref: [wedderburn1908] Wedderburn, "On hypercomplex numbers," Proc. London Math. Soc. s2-6 (1908)
Ref: [hoefsmit1974] Hoefsmit, representations of Hecke algebras of type A
Ref: [jones1985] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidKnot

universe u

/-- A partition `λ ⊢ k` (placeholder; an abstract index so the discipline holds
    for any realisation). -/
structure Partition where
  parts : List ℕ

/-- The shadow-price discipline for the mass-formula coefficients, polymorphic
    in the ground ring `R` (with `2` invertible).

    **🛑 Vacuity status (audited 2026-11-20, bean `qou-dx7g`; triage rank 67).**
    This class does **not** encode the proposition's claim, and the repair is
    not available in the corpus.  `h`, `w`, `C`, `S` and `uStar` are all fields
    chosen by the instance, and `factor` is `uStar λ = C λ * S λ` with `S` free,
    so any instance satisfies it by *defining* `uStar := C * S` (e.g. `h = 0`,
    `w = S = 0`).  The claim the block intends is that the optimal dual
    variables of a **partition-indexed operator-selection program** factor as a
    partition-only coefficient times a scaling function of the nuclear datum
    `(Z, N, A)` alone.  Encoding that needs (i) the program itself — its
    objective, its block-diagonal Gram `G_λ = (w_λ/d_λ) I` and its net
    constraint, indexed by a finite set of partitions — so that `uStar` is its
    certified optimal dual (cf. `QOU.BraidKnot.HasFiniteLPDuality`) rather than
    a field; and (ii) a nuclear datum in that program's data, so that `S` can be
    *derived* as a function of `(Z, N, A)`.  Neither exists: the block's own
    caveat (2026-10-11, bean `qou-wg3c`) records that the stated LP's dual
    constraints carry no `(Z, N)`, so no program on record can produce the
    factorisation.  What *does* carry content below is the conditional
    direction: **if** `w̃_λ = 0` then `uStar λ = 0`
    (`shadow_price_eq_zero_of_weight_eq_zero`) — true for any instance, and
    meaningful once `uStar` is a genuine dual.  Free fields that remain:
    `h`, `w`, `contentSum`, `C` (pinned only relative to `w`, `h`), `S`, `uStar`.

    An instance records, for the nuclear operator-selection LP:
      • the canonical Wedderburn weight `tilde w_λ` and the Hecke scalar `h`;
      • the partition-only LP coefficient `C_λ = tilde w_λ · h·⅟2`;
      • the nuclear-datum scaling function `S_λ(Z,N,A)`;
      • the optimal dual variable `u_λ*` with the strong-duality factorisation
        `u_λ* = C_λ · S_λ` (`prop:operator-selection-lp`). -/
class MassCoefficientShadowPrice (R : Type u) [CommRing R] [Invertible (2 : R)] where
  /-- Hecke-generator scalar `h = q - q⁻¹`. -/
  h : R
  /-- Canonical q-deformed Wedderburn weight `tilde w_λ`
      (cf. `WedderburnWeightCanonical`). -/
  w : Partition → R
  /-- Content sum `c(λ) = Σ (j - i)` — determines the scaling type
      (`>0` volume, `=0` isospin, `<0` charge). -/
  contentSum : Partition → ℤ
  /-- LP shadow-price coefficient `C_λ` (partition-only, no nuclear datum). -/
  C : Partition → R
  /-- Scaling function `S_λ(Z,N,A)` — the only nuclear-datum-dependent factor. -/
  S : Partition → R
  /-- Optimal dual variable (shadow price) of the `λ`-Frobenius constraint. -/
  uStar : Partition → R
  /-- LP shadow-price scaling identity `C_λ = tilde w_λ · h·⅟2` (definitional;
      the same `C_λ` as `prop:wedderburn-weight-canonical`). -/
  C_eq : ∀ lam, C lam = w lam * (h * ⅟(2 : R))
  /-- Strong-duality factorisation `u_λ* = C_λ · S_λ`
      (`prop:operator-selection-lp`: strong duality + complementary slackness). -/
  factor : ∀ lam, uStar lam = C lam * S lam

/-- The shadow price in canonical-weight form:
    `u_λ* = tilde w_λ · (h·⅟2) · S_λ`.  Combines the strong-duality
    factorisation with the LP scaling identity. -/
theorem MassCoefficientShadowPrice.shadow_price_weight_form
    {R : Type u} [CommRing R] [Invertible (2 : R)]
    [c : MassCoefficientShadowPrice R] (lam : Partition) :
    c.uStar lam = c.w lam * (c.h * ⅟(2 : R)) * c.S lam := by
  rw [c.factor, c.C_eq]

/-- At the normalisation point `S_λ = 1`, the shadow price equals the
    partition-only coefficient `C_λ`. -/
theorem MassCoefficientShadowPrice.normalization
    {R : Type u} [CommRing R] [Invertible (2 : R)]
    [c : MassCoefficientShadowPrice R] (lam : Partition)
    (hS : c.S lam = 1) :
    c.uStar lam = c.C lam := by
  rw [c.factor, hS, mul_one]

/-- The coefficient `C_λ` is independent of the nuclear datum: cancelling the
    scaling off the shadow price recovers the partition-only `C_λ`.  The
    invertibility of `S_λ` — over a field, the old `S_λ ≠ 0` — is supplied by
    the unit `s` with `S_λ = ↑s`. -/
theorem MassCoefficientShadowPrice.coefficient_nuclear_independent
    {R : Type u} [CommRing R] [Invertible (2 : R)]
    [c : MassCoefficientShadowPrice R] (lam : Partition)
    (s : Rˣ) (hS : c.S lam = (s : R)) :
    c.uStar lam * ((s⁻¹ : Rˣ) : R) = c.C lam := by
  rw [c.factor, hS, mul_assoc, s.mul_inv, mul_one]

/-- **A vanishing Wedderburn weight kills the coefficient.** Immediate from
`C_eq`, and the reason it matters is that convention D's row cap
(`QOU/Hecke/RowCap.lean`: a column of height `≥ 3` has no injective filling into
a 2-dimensional fibre) makes `tilde w_λ = 0` for every `ℓ(λ) > 2`. Those blocks
therefore price nothing — which is the step `qou-a5jk` left open and
`qou-8na1` had already observed as an instance (`C_[1,1,1] = w̃·h/2 = 0` makes
`uStar = C·S = 0` consistent rather than contradictory).

The implication is proved here; the antecedent is the corpus's, cited not
re-derived. -/
theorem MassCoefficientShadowPrice.coefficient_eq_zero_of_weight_eq_zero
    {R : Type u} [CommRing R] [Invertible (2 : R)]
    [c : MassCoefficientShadowPrice R] (lam : Partition)
    (hw : c.w lam = 0) :
    c.C lam = 0 := by
  rw [c.C_eq, hw, zero_mul]

/-- **And therefore kills the shadow price**, whatever the scaling function
does. So a block the row cap annihilates contributes nothing to
`B = (Σ_λ C_λ · S_λ) · m_e` — no `S_λ` can rescue it, because the vanishing is
upstream of the nuclear datum. -/
theorem MassCoefficientShadowPrice.shadow_price_eq_zero_of_weight_eq_zero
    {R : Type u} [CommRing R] [Invertible (2 : R)]
    [c : MassCoefficientShadowPrice R] (lam : Partition)
    (hw : c.w lam = 0) :
    c.uStar lam = 0 := by
  rw [c.factor, coefficient_eq_zero_of_weight_eq_zero lam hw, zero_mul]

/-- Contrapositive, which is how a search uses it: a block that prices anything
at all must have a nonzero canonical weight — so under convention D it must have
at most two rows. -/
theorem MassCoefficientShadowPrice.weight_ne_zero_of_shadow_price_ne_zero
    {R : Type u} [CommRing R] [Invertible (2 : R)]
    [c : MassCoefficientShadowPrice R] (lam : Partition)
    (hu : c.uStar lam ≠ 0) :
    c.w lam ≠ 0 :=
  fun hw => hu (shadow_price_eq_zero_of_weight_eq_zero lam hw)

end QOU.BraidKnot
