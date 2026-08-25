/-
# The categorical volume constraint pins the fibre dimension

`markovWeights_eq_jones_of_fibre_categorical`
(`FibreCategoricalTraceForcesJones.lean`) takes `hN : N = 2` as an **explicit
hypothesis**, sourced from the corpus theorem `thm:su2-emergence`. That
sourcing is weaker than it looks, and this file replaces it.

## Why the existing sourcing does not carry weight

Two independent problems, both checkable:

1. **The corpus proof assumes the `2` it is cited for.** `prf:su2-emergence`
   argues `G = SL(2) ∩ U(2) = SU(2)` from two lemmas whose conclusions are
   *stated* as `G ⊆ SL(2, ℂ)` and `G ⊆ U(2)`. The rank is an input to both,
   not an output of either. What the proof establishes is which **subgroup**
   of a rank-2 general linear group survives — not the rank. The Lean side
   agrees in its own section heading: `VolumeForm.lean` §2 is "SU(2) from
   **rank-2** + dagger".
2. **Its `lean.ref` does not resolve, and the Lean that does exist carries no
   rank content.** `thm:su2-emergence` names `qou:QOU.RankOneGaugeData`; no
   declaration of that name exists in this tree and the canonical resolver
   returns unresolved. (Before folio-assistant PR #121 it resolved to the
   import-only library root, where every checker passed vacuously — which is
   why this went unnoticed.) Lean for the theorem *does* exist under a
   different name, `QOU.SU2Emergence` (`VolumeForm.lean`), carrying this
   theorem's `\label`; but its fields are `gaugeGroupType : Type*`,
   `ext_sq_action`, and `det_one : ∀ g, ext_sq_action g = 𝟙 exteriorSquare`.
   It says a group acts trivially on the exterior square. It does not mention
   `SU(2)`, and it does not mention the rank. The two supporting lemmas are
   `class SU2EmergenceVolumeDeterminant (det_g : ℝ) where det_eq_one :
   det_g = 1` and its dagger twin — restatements of their own conclusions,
   with docstrings saying the witness is "pending the categorical determinant
   formalisation in Mathlib".

So link 1 of the D-forcing chain rests on a citation, not a derivation, in
both the prose and the formalisation.

## What actually forces the rank

The framework definition already contains the statement that does the work.
`def:quantum-observable-universe` condition (v), the **categorical volume
constraint**, posits

    a non-degenerate epimorphism  ε : Λ²V → 𝟙  on the fundamental object V,
    preserved by all tensor automorphisms.

Read at the fibre, that is a statement about `dim Λ²V`, and `dim Λ²V` is
`C(N, 2)` for `dim V = N`. Both readings of "non-degenerate epimorphism" are
recorded below, because they do **not** have the same strength and only the
stronger one forces anything:

| reading of ε | dimension statement | forces |
|---|---|---|
| epimorphism onto `𝟙` (target hit) | `C(N,2) ≠ 0` | `N ≥ 2` only |
| **iso** `Λ²V ≅ 𝟙` (no kernel either) | `C(N,2) = 1` | **`N = 2`** |

`exteriorSquareDim_ne_zero_iff` and `exteriorSquareDim_eq_one_iff` below are
those two rows. The forcing argument consumes the second.

This is also the reading under which condition (v) does the job the corpus
proof asks of it. `det(g)` is the scalar by which `g` acts on the **top**
exterior power `Λ^N V`; a constraint imposed on `Λ²V` is a determinant
constraint exactly when `2 = N`. Under the weak reading `ε` constrains the
second elementary symmetric function of the eigenvalues and the step to
`det(g_V) = 1` does not go through.

## Status: this shifts the premise, it does not discharge it

`N = 2` is now derived from a **stated axiom of the framework** rather than
from a citation with no formal content. That is strictly better sourcing, and
it is independent of any measured quantity — nothing here mentions a numerical
substrate value or compares against one.

It is **not** a proof that the physical mass channel satisfies condition (v)
under the strong reading. `def:quantum-observable-universe` writes
"non-degenerate epimorphism"; whether the author intends iso is an editorial
question this file cannot settle.

And the *formalised* condition currently carries neither reading. In
`CategoricalFoundations.lean` it is two free fields,

    exteriorSquare : C
    volumeForm     : exteriorSquare ⟶ (𝟙_ C)

with nothing tying `exteriorSquare` to `Λ²(fundamentalObj)` and no
non-degeneracy, epi, or invariance hypothesis on `volumeForm`. Since
`QuantumUniverse` carries a `HasZeroMorphisms C` instance (it is needed for
block orthogonality), `volumeForm := 0` inhabits the field for **any**
`exteriorSquare`, so the formalised condition (v) constrains nothing
whatever. `QOU.SU2Emergence` takes `exteriorSquare` as an unconstrained
parameter for the same reason. Both are honest placeholders rather than
errors — but a placeholder cannot be the source of a rank.

Bean `qou-n1dj` stays open; what changes is where its remaining weight sits.

## Base ring (§7c)

Everything here is `Nat` arithmetic and the re-export is generic
`{R : Type*} [CommRing R]`, inheriting `[IsDomain R]` from the theorem it
wraps. No archimedean construct of any kind: no order relation, no
real-analytic function, no numerical substrate value, no tactic that reasons
about magnitude. The binomial idiom matches `RowCapObstruction`, which states
the sibling fact about the same `N` the same way.
-/
import QOU.BraidsAndKnots.FibreCategoricalTraceForcesJones

namespace QOU.BraidsAndKnots

open QOU.Eightfold.RowCapObstruction

variable {R : Type*} [CommRing R]

/-! ## The volume constraint as a dimension statement -/

/-- `dim Λ²V` for a fibre `V` of dimension `N`.

Stated combinatorially, exactly as `RowCapObstruction` states `dim V_λ` for
the three `λ ⊢ 3` channels (`weylDimSym`, `weylDimMixed`, `weylDimAlt`) — the
same `N`, the same idiom, so the two constraints on it compose without a
translation step. -/
def exteriorSquareDim (N : ℕ) : ℕ := N.choose 2

@[simp] theorem exteriorSquareDim_zero : exteriorSquareDim 0 = 0 := rfl

@[simp] theorem exteriorSquareDim_one : exteriorSquareDim 1 = 0 := rfl

@[simp] theorem exteriorSquareDim_two : exteriorSquareDim 2 = 1 := rfl

@[simp] theorem exteriorSquareDim_three : exteriorSquareDim 3 = 3 := rfl

/-- **Weak reading of condition (v): `ε` is onto.**

If `Λ²V → 𝟙` hits its target then `Λ²V` is nonzero, which says only `N ≥ 2`.
Recorded to make precise how much of the volume constraint is *not* enough:
this reading admits every fibre of rank at least two, the colour fibre `N = 3`
included. -/
theorem exteriorSquareDim_ne_zero_iff (N : ℕ) : exteriorSquareDim N ≠ 0 ↔ 2 ≤ N := by
  unfold exteriorSquareDim
  rw [Ne, Nat.choose_eq_zero_iff]
  omega

/-- **Strong reading of condition (v): `ε` is an isomorphism `Λ²V ≅ 𝟙`.**

`C(N,2) = 1` has the unique solution `N = 2`: below it the exterior square
vanishes, above it the exterior square is at least three-dimensional and can
carry no non-degenerate map to a one-dimensional unit.

This is the rank statement the D-forcing chain needs, and it comes from the
framework's own definition rather than from `thm:su2-emergence`. -/
theorem exteriorSquareDim_eq_one_iff (N : ℕ) : exteriorSquareDim N = 1 ↔ N = 2 := by
  unfold exteriorSquareDim
  refine ⟨fun h => ?_, fun h => by subst h; rfl⟩
  by_contra hne
  rcases Nat.lt_or_ge N 3 with hlt | hge
  · interval_cases N <;> simp_all
  · have hmono : Nat.choose 3 2 ≤ Nat.choose N 2 := Nat.choose_le_choose 2 hge
    have h3 : Nat.choose 3 2 = 3 := rfl
    omega

/-- **The volume constraint excludes the colour fibre.**

At `N = 3` the exterior square is three-dimensional, so condition (v) under
the strong reading fails. This is the formal counterpart of the observation
in bean `qou-n1dj` that the mass chain does not inherit the eightfold
chapter's `N = 3` construction: the two channels are constrained by the same
axiom to different ranks, so no re-tuning connects them. -/
theorem exteriorSquareDim_three_ne_one : exteriorSquareDim 3 ≠ 1 := by decide

/-! ## Re-sourcing the forcing theorem -/

/-- **Convention D, with the rank sourced from the framework axiom.**

Identical in content to `markovWeights_eq_jones_of_fibre_categorical`, with
the hypothesis `hN : N = 2` — cited to a corpus theorem that assumes its own
`2` and has no Lean declaration — replaced by `hvol`, the categorical volume
constraint of `def:quantum-observable-universe` read at the fibre.

Still an implication. The premise `MassTraceIsFibreCategorical` is untouched
and remains the open input; what this changes is that the *other* hypothesis
is now discharged from a stated axiom of the framework instead of carried as
a citation. -/
theorem markovWeights_eq_jones_of_volume_constraint [IsDomain R] {N : ℕ}
    (ctx : MassTraceIsFibreCategorical R N)
    (hvol : exteriorSquareDim N = 1)
    (q qi z : R)
    (hqi : q * qi = 1)
    (hnorm : ctx.weightSym + 2 * ctx.weightMixed + ctx.weightAlt = 1)
    (hsigma : q * ctx.weightSym + (q - qi) * ctx.weightMixed
      + (-qi) * ctx.weightAlt = z)
    (hsigmasigma : q ^ 2 * ctx.weightSym + (-1) * ctx.weightMixed
      + qi ^ 2 * ctx.weightAlt = z ^ 2) :
    (q + qi) ^ 2 * ctx.weightMixed = 1
      ∧ ctx.weightSym = 1 - 2 * ctx.weightMixed
      ∧ z * (q + qi) = q ^ 2 :=
  markovWeights_eq_jones_of_fibre_categorical ctx
    ((exteriorSquareDim_eq_one_iff N).mp hvol) q qi z hqi hnorm hsigma hsigmasigma

/-- **Convention C is excluded, with the rank sourced from the framework
axiom.**

Same re-sourcing applied to `ocneanu_eq_jones_of_fibre_categorical`. -/
theorem ocneanu_eq_jones_of_volume_constraint [IsDomain R] {N : ℕ}
    (ctx : MassTraceIsFibreCategorical R N)
    (hvol : exteriorSquareDim N = 1)
    (q qi z : R)
    (hqi : q * qi = 1)
    (hnorm : ctx.weightSym + 2 * ctx.weightMixed + ctx.weightAlt = 1)
    (hsigma : q * ctx.weightSym + (q - qi) * ctx.weightMixed
      + (-qi) * ctx.weightAlt = z)
    (hsigmasigma : q ^ 2 * ctx.weightSym + (-1) * ctx.weightMixed
      + qi ^ 2 * ctx.weightAlt = z ^ 2)
    (hC : z * (q + qi) ≠ q ^ 2) : False :=
  ocneanu_eq_jones_of_fibre_categorical ctx
    ((exteriorSquareDim_eq_one_iff N).mp hvol) q qi z hqi hnorm hsigma hsigmasigma hC

/-- **The weak reading does not suffice — stated, not assumed.**

`exteriorSquareDim_ne_zero_iff` gives `2 ≤ N`, and `N = 3` satisfies it. The
class `MassTraceIsFibreCategorical` admits an instance at `N = 3` with a
nonzero alternating weight (`weightAlt_ne_zero_at_three`, proved in the
sibling file), so under the weak reading the alternating channel need not
vanish and nothing forces convention D.

This is the anti-vacuity check for the distinction this file draws: the two
readings of condition (v) are genuinely different in consequence, not two
phrasings of one thing. -/
theorem weak_volume_reading_admits_three :
    exteriorSquareDim 3 ≠ 0 ∧ exteriorSquareDim 3 ≠ 1 := by
  refine ⟨?_, exteriorSquareDim_three_ne_one⟩
  decide

end QOU.BraidsAndKnots
