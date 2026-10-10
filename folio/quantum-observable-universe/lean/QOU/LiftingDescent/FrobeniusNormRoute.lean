import Mathlib.RingTheory.Norm.Defs
import Mathlib.Algebra.Field.Basic
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.NumberTheory.Zsqrtd.GaussianInt

/-!
# The norm route to non-unitness, and why the residue route could not reach it

Bean `qou-lrnd` refuted the mod-`𝔭` route to the perpetual obstruction and
named the replacement it did not build: *"an **archimedean** bound. A unit of
`O` has norm `±1`, so bounding `|Frob_p|` below at every complex embedding
bounds `|N(Frob_p)| > 1`."*  This file supplies the algebraic half of that
route and, in the same breath, the reason the previous one was blocked.

**The obstruction was to a RING hom, and the norm is not one.**  The
refutation turns on two facts, both correct:

* `reduce p : R p →+* ℤ` cannot be reduction mod `𝔭` — that lands in
  `O/𝔭 ≅ 𝔽_p` — and **no ring hom `ℤ[ζ_2p] →+* ℤ` exists at all**, since it
  would need to send `ζ` to a rational root of `Φ_2p`, and there is none.
* With the correct target `𝔽_p`, the residue is a *unit* whenever `p ∤ C`, so
  transferring non-unitness backwards runs the wrong way.

Both are statements about **ring** homomorphisms and about **fields**.  The
field norm is neither: `Algebra.norm ℤ : S →* ℤ` is a `MonoidHom`, multiplicative
only — `N(x + y) ≠ N(x) + N(y)` — so its existence is not touched by the first
fact, and `ℤ` is **not a field**, so it is not touched by the second.  That is
the whole of why this route is open when the other is closed, and
`zmod_not_isUnit_iff_eq_zero` below states the contrast as a theorem rather
than as prose.

**What is proved and what is assumed.**  The transfer is proved outright and
needs nothing about number fields.  The *archimedean estimate* — that the norm
of the QOU Frobenius is bounded away from `±1` — is an explicit hypothesis and
is **not** established here.

🛑 **MEASURED 2026-08-25, later the same day: that hypothesis is FALSE at
`p = 3`.**  This paragraph originally called the estimate "genuinely open" and
pointed at the orbit as the missing ingredient.  The orbit was then computed
exactly, in `habiro_frobenius_conjugate_orbit_probe.py`, and the norms are

    atom        p = 2                 p = 3
    proton      N = 64    (= 8²)      N = 1     ← UNIT
    neutron     N = 4     (= 2²)      N = 1     ← UNIT
    deuteron    N = 36864 (= 192²)    N = 171

A unit of `O` has norm `±1`, so `Frob_3` **is** a unit for both nucleons and
`1 < |N(frob p)|` fails there.  Three independent checks: orbit product versus
`Res(Φ_2p, f)` with no shared code path; the `p = 2` representative collapsing
to the collapse constant with `N = C²`, forced by degree 2; and
`habiro_frobenius_norm_probe.py` flipping its own verdict from "Route A
SUPPORTED" to "Route A BLOCKED" once its input was corrected from the
`_deprecated/` coefficients to the canonical ones.

**Scope — (a), not (b).**  This is a *counterexample to the `∀ p` form*, not a
structural exclusion of the norm route.  One prime is not a positive density,
so the **almost-every-prime form is untouched and is not refuted**.  What dies
is the no-exception-set version — which is the form the corpus's Lean carries.
Whether `p = 3` is isolated is undecided and needs canonical Habiro
coefficients past index 14 (bean `qou-lrnd`).

The original observation about the *trace* witness stands and is unrelated:
`habiro-frobenius-probe.witness.json` records `abs_frob` at **one** embedding
per prime, frequently `< 1` (for the proton at `p = 11`, see its
`atoms.0.frobenius.4.abs_frob`: read the value there, it is not copied here
so it cannot drift), which is not an orbit.

Ref: [yekutieli2010] — obstruction theory
-/

namespace QOU.LiftingDescent

/-- **Non-unitness transfers backwards along any multiplicative map to `ℤ`.**

    Nothing here is about number fields: a unit maps to a unit, the units of
    `ℤ` are `±1`, so a norm of absolute value `> 1` forces a non-unit.  Stated
    for a bare `Monoid` and a `MonoidHom` precisely because that is the
    generality the norm lives in — see the file header for why the ring-hom
    version is unavailable. -/
theorem not_isUnit_of_natAbs_norm_ne_one {M : Type*} [Monoid M]
    (N : M →* ℤ) (x : M) (h : 1 < (N x).natAbs) : ¬ IsUnit x := by
  intro hu
  have hNu : IsUnit (N x) := hu.map N
  rw [Int.isUnit_iff_natAbs_eq] at hNu
  omega

/-- **The criterion at the actual algebraic norm**, so it is not merely an
    abstract shape.  `Algebra.norm ℤ` is a `MonoidHom S →* ℤ` by definition.
    The `Module.Free` / `Module.Finite` hypotheses are what make it the genuine
    field norm rather than the junk value the definition falls back to. -/
theorem not_isUnit_of_algebraNorm {S : Type*} [CommRing S] [Algebra ℤ S]
    [Module.Free ℤ S] [Module.Finite ℤ S] (x : S)
    (h : 1 < (Algebra.norm ℤ x).natAbs) : ¬ IsUnit x :=
  not_isUnit_of_natAbs_norm_ne_one (Algebra.norm ℤ) x h

/-- **The perpetual shape.**  Note there is no exception set: the conclusion is
    at *every* prime, not at all but finitely many.

    This is the structural payoff over the collapse route.  A congruence to a
    fixed constant `C` could only ever give non-unitness at the primes dividing
    `C` — finitely many, "the complement of what perpetual means" (`qou-lrnd`).
    A norm bound holding at every prime gives the obstruction at every prime.

    🛑 **The hypothesis has NO valid instantiation at the QOU Frobenius**
    (measured 2026-08-25; see the file header).  `N(Frob_3) = 1` for both
    nucleons, so `∀ p, 1 < |N (frob p)|` is false and this theorem, while true,
    cannot be applied to that family as stated.  It is kept because the
    implication is correct and is the form a caller with a genuine norm bound
    wants — but do not read it as a route the QOU Frobenius takes. -/
theorem frobenius_not_unit_of_norm_bound {M : Type*} [Monoid M]
    (N : M →* ℤ) (frob : Nat.Primes → M)
    (h : ∀ p : Nat.Primes, 1 < (N (frob p)).natAbs) :
    ∀ p : Nat.Primes, ¬ IsUnit (frob p) :=
  fun p => not_isUnit_of_natAbs_norm_ne_one N (frob p) (h p)

/-- **Why the residue route was capped, as a theorem.**

    In a group with zero — a field, and in particular `𝔽_p` — a non-unit is
    exactly zero.  So a residue map into such a target can witness non-unitness
    *only* by vanishing; there is no third option, and a congruence to a
    nonzero constant therefore cannot witness it at any prime where the
    constant survives.

    Stated at `GroupWithZero` rather than at `ZMod p` on purpose: the cap comes
    from *every nonzero element being invertible*, not from anything about
    residues or primes.  `qou-lrnd` records the `ZMod` instance of this as
    `isUnit_four_zmod` and the reasoning as prose; this is the general fact
    both are shadows of, and it is what `ℤ` — not a group with zero — escapes. -/
theorem not_isUnit_iff_eq_zero_groupWithZero {G : Type*} [GroupWithZero G]
    (y : G) : ¬ IsUnit y ↔ y = 0 := by
  simp [isUnit_iff_ne_zero]

/-- **The gap is concrete, not hypothetical.**  At the proton collapse constant
    `χ(A) = 8` (as measured, per `qou-lrnd`'s 2026-08-23 correction) and `p = 3`,
    the residue is a unit — so by `not_isUnit_iff_eq_zero_groupWithZero` the residue
    route provably concludes nothing there, while a norm bound would. -/
theorem proton_residue_isUnit_at_three : IsUnit ((8 : ℤ) : ZMod 3) := by
  decide

/-! ### The two claims of the header, machine-checked in a computable model

`ℤ[i]` has the same shape as `ℤ[ζ_2p]` for the purpose at hand: it is a
rank-2 free `ℤ`-algebra generated by a root of an integer polynomial with no
rational root.  So it can carry the header's argument concretely, and unlike
the cyclotomic case every step is `decide`-able.

The pair below is the whole point of this file. Neither is asserted; both are
proved. -/

/-- `i² = -1`, computed. -/
theorem gaussianInt_i_sq : (⟨0, 1⟩ : GaussianInt) * ⟨0, 1⟩ = -1 := by decide

/-- **Half one: the ring-hom route is blocked, and this is a proof, not a
    citation.**  There is no ring homomorphism `ℤ[i] →+* ℤ` at all — `i` would
    have to go to an integer square root of `-1`, and a square in `ℤ` is
    non-negative.

    This is the computable analogue of `qou-lrnd`'s finding that no
    `ℤ[ζ_2p] →+* ℤ` exists (there, because `Φ_2p` has no rational root).  Same
    obstruction, same reason: a ring hom must send a generator to a root of its
    minimal polynomial, and there is none in `ℤ`. -/
theorem no_ringHom_gaussianInt_to_int (f : GaussianInt →+* ℤ) : False := by
  have h : (f ⟨0, 1⟩) * (f ⟨0, 1⟩) = -1 := by
    rw [← map_mul, gaussianInt_i_sq, map_neg, map_one]
  have hnn : (0 : ℤ) ≤ f ⟨0, 1⟩ * f ⟨0, 1⟩ := mul_self_nonneg _
  rw [h] at hnn
  exact absurd hnn (by decide)

/-- **Half two: the norm route goes through anyway.**  `1 + i` is a non-unit of
    `ℤ[i]`, established through `Zsqrtd.normMonoidHom : ℤ√d →* ℤ` and the
    criterion above — in a ring that half one has just shown admits *no* ring
    hom to `ℤ`.

    Worth noting what carries it: `IsUnit` is not decidable here, so `decide`
    cannot prove this directly (it fails to synthesise `Decidable ¬IsUnit _`).
    The `decide` discharges only `1 < |N(1+i)| = 2`; the criterion does the
    rest.  So the norm is not decoration — it is what makes the statement
    reachable. -/
theorem one_add_i_not_isUnit : ¬ IsUnit (⟨1, 1⟩ : GaussianInt) :=
  not_isUnit_of_natAbs_norm_ne_one Zsqrtd.normMonoidHom _ (by decide)

end QOU.LiftingDescent
