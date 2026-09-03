import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Prime.Basic

/-!
# The motivic character does not vanish at places not dividing `χ(A)`

This file formalises the **final step of the sketch** of
[`thm:motivic-perpetual-obstruction`](../../../lifting-and-descent/motivic-perpetual-obstruction.md),
in the sketch's own words:

> the Euler class projects to a Frobenius character whose trace equals
> `χ(A) mod p`.  Because `p ∤ χ(A)`, this trace is non-zero modulo `p`.
> The character is non-trivial.

**Why this file exists: the block and its Lean were measuring different
propositions.**  The block's conclusion is that the character is
*non-trivial* at `p` — its local trace does not **vanish**.  Every Lean
declaration previously attached to the block concludes instead that the
Frobenius is not a **unit** (`motivic_perpetual_obstruction`,
`motivic_perpetual_obstruction_frobenius`, `habiro_frobenius_not_unit`).
Non-vanishing and non-unitness are different properties, and over a field
they point in *opposite* directions: a unit is precisely a nonzero element.

That distinction is what makes the arithmetic here work where bean
`qou-lrnd`'s route did not.  `qou-lrnd` established — scope-(b), with the
invariant exhibited — that a congruence to a fixed constant `C` can yield
non-unitness only at the finitely many primes dividing `C`, "the complement
of what perpetual means"; `HabiroCollapse.isUnit_four_zmod` is that
obstruction in Lean.  **That refutation is untouched, and this file does not
reopen it.**  What it does is observe that the same fact settles the block's
actual claim affirmatively: `IsUnit` in `ZMod p` *implies* `≠ 0`, so exactly
where the non-unit reading fails, the non-vanishing reading succeeds — and it
succeeds in the "perpetual" shape, at every prime above `|χ(A)|`.

**What is proved and what is assumed (§3b-cond).**  The two substantive
links of the sketch are carried as hypothesis fields of
`MotivicResidueRealization`, not proved:

* `chi`, the Euler characteristic `χ(A)`, identified with `tr(κ₀)` via
  `thm:qu-to-qou` — consumed as a datum;
* `residue_eq_chi`, that the local Frobenius trace reduces to `χ(A)` mod `p`
  under the realization `ρ_p` — the sketch's own "trace equals `χ(A) mod p`".

Everything below is **derived** from those: the class carries no
non-vanishing field, and `residue_eq_zero_iff_dvd` is genuine arithmetic
(`ZMod.intCast_zmod_eq_zero_iff_dvd`), not a projection.  Proving
`residue_eq_chi` itself is open and is not attempted here.

Ref: [yekutieli2010] — obstruction theory
LaTeX label: `thm:motivic-perpetual-obstruction` (sketch, final step)
-/

namespace QOU.LiftingDescent

/-- A prime is nonzero as a natural, so `ZMod p` is a genuine residue ring. -/
instance neZeroCoePrime (p : Nat.Primes) : NeZero (p : ℕ) := ⟨p.2.ne_zero⟩

/-- A prime residue ring has at least two elements, so `IsUnit` implies `≠ 0`. -/
instance nontrivialZModPrime (p : Nat.Primes) : Nontrivial (ZMod (p : ℕ)) := by
  haveI : Fact (p : ℕ).Prime := ⟨p.2⟩
  infer_instance

/-- **§3b-cond context for the sketch's mod-`p` step.**

    Fields are the *inputs* of the sketch, never its conclusion.  There is
    deliberately no non-vanishing field: that is derived below. -/
class MotivicResidueRealization where
  /-- The Euler characteristic `χ(A)`, i.e. `tr(κ₀)` via `thm:qu-to-qou`. -/
  chi : ℤ
  /-- The trace of the local Frobenius character `χ^mot_{A,p}` after
      realization `ρ_p`, living in the residue ring at `p`. -/
  residue : (p : Nat.Primes) → ZMod (p : ℕ)
  /-- INPUT — the sketch's own step: *"a Frobenius character whose trace
      equals `χ(A) mod p`"*.  This is the substantive content and is a
      hypothesis, not a theorem. -/
  residue_eq_chi : ∀ p : Nat.Primes, residue p = ((chi : ℤ) : ZMod (p : ℕ))

variable [ctx : MotivicResidueRealization]

/-- **The residue vanishes exactly at the primes dividing `χ(A)`.**

    Stated as an `iff` on purpose: it fixes the vanishing locus completely
    rather than bounding it on one side, so no later reader can mistake the
    non-vanishing result below for a one-directional estimate. -/
theorem residue_eq_zero_iff_dvd (p : Nat.Primes) :
    ctx.residue p = 0 ↔ (p : ℤ) ∣ ctx.chi := by
  rw [ctx.residue_eq_chi p]
  exact ZMod.intCast_zmod_eq_zero_iff_dvd ctx.chi (p : ℕ)

/-- **The sketch's final step, derived.**  `p ∤ χ(A)` forces the local trace
    to be non-zero mod `p`, hence the character at `p` is non-trivial. -/
theorem residue_ne_zero_of_not_dvd (p : Nat.Primes) (h : ¬ (p : ℤ) ∣ ctx.chi) :
    ctx.residue p ≠ 0 :=
  fun hz => h ((residue_eq_zero_iff_dvd p).mp hz)

/-- **The obstruction is perpetual: every prime above `|χ(A)|` is a
    non-vanishing place.**

    This is the "almost every finite place" shape the block claims, made
    quantitative.  A prime at which the residue vanishes must divide the
    nonzero integer `χ(A)`, hence is bounded by `|χ(A)|`; so the exceptional
    set is contained in the finitely many primes up to that bound. -/
theorem residue_ne_zero_of_gt_abs (hchi : ctx.chi ≠ 0) (p : Nat.Primes)
    (hp : ctx.chi.natAbs < (p : ℕ)) : ctx.residue p ≠ 0 := by
  refine residue_ne_zero_of_not_dvd p ?_
  intro hdvd
  have hnat : (p : ℕ) ∣ ctx.chi.natAbs := by
    simpa using Int.natAbs_dvd_natAbs.mpr hdvd
  exact absurd (Nat.le_of_dvd (Int.natAbs_pos.mpr hchi) hnat) (by omega)

/-- **Non-unitness and non-vanishing are not the same claim** — over `ZMod p`
    a unit is nonzero, so `IsUnit` *delivers* the block's conclusion while
    refuting the corpus's non-unit framing of it.

    Applied to `HabiroCollapse.isUnit_four_zmod`, this is the reconciliation:
    the residue's being a unit at every odd prime is exactly why the
    non-unit route dies (bean `qou-lrnd`) and exactly why the non-vanishing
    route lives. -/
theorem ne_zero_of_isUnit_residue (p : Nat.Primes) (h : IsUnit (ctx.residue p)) :
    ctx.residue p ≠ 0 :=
  h.ne_zero

/-- **A concrete realization, so nothing above is vacuous.**

    `χ(A) = 8` is the QOU proton collapse constant `a₀(-1) + 2·a₁(-1)` as
    *measured* from `habiro-coefficients-atomic.witness.json` (`a₀ = 8`
    identically, `a₁(-1) = 0`) — the value bean `qou-lrnd` corrected the
    corpus's `4` to on 2026-08-23.  Under it the vanishing locus is `p = 2`
    alone, so the character is non-trivial at every odd prime.

    Deliberately a `def`, **not** an `instance`.  As an instance it would be
    found by typeclass resolution for every downstream
    `[MotivicResidueRealization]` hypothesis, silently discharging the very
    assumption this file exists to keep visible.  It witnesses inhabitation
    and derives no physics. -/
def protonResidueRealization : MotivicResidueRealization where
  chi := 8
  residue := fun p => ((8 : ℤ) : ZMod (p : ℕ))
  residue_eq_chi := fun _ => rfl

/-- **Non-vacuity, checked rather than assumed: both branches of
    `residue_eq_zero_iff_dvd` are witnessed.**

    Without this the `iff` could hold because one side is never realised.
    At `χ(A) = 8` the residue genuinely vanishes at `p = 2` and genuinely
    does not at `p = 3`, so the theorem separates primes rather than
    describing a constant. -/
example :
    protonResidueRealization.residue ⟨2, Nat.prime_two⟩ = 0 ∧
    protonResidueRealization.residue ⟨3, Nat.prime_three⟩ ≠ 0 := by
  constructor <;> decide

end QOU.LiftingDescent
