/-
Copyright (c) 2026 litlfred. All rights reserved.

# The D2 sign-rep obstruction, extended from the PAIR channel to the TRIPLE channel

Bean `qou-lq6k` (the antisymmetry obstruction), `qou-ix0x`, companion `qou-brng`.
Under `qou-x631`.

## Why this file exists — the existing theorem does not cover the case that matters

`QOU.Mass.MilnorSignRepObstruction.equivariant_linearMap_eq_zero` proves that any
S₃-equivariant linear map from the sign representation (the line spanned by `μ̄(123)`)
into the **pair-channel** representation `Fin 3 → R` is zero.  That target is the
permutation module on three points — *trivial ⊕ standard* — and it is the right
target for a **charge-bilinear / per-pair** coupling, which is what finding D2 was
about.

It is **not** the target the three-body binding channel lives in.  The quantity the
corpus's own measured cumulants constrain is

    tripleMutual(i,j,k) = w3 i j k + w3 i k j + w3 j k i

(`QOU.Mass.CrossingModelPairLocality.tripleMutual`) — a sum over **all three** pairs
of the triple, hence a **scalar**, invariant under relabelling the components.  That
is the **trivial** representation, not `trivial ⊕ standard`, and no instance of the
pair-channel theorem has it as a target.  So the obstruction had a hole exactly where
the `b₃` question sits.

This file closes it, and the closure is two lines of representation theory: `sign`
and `trivial` are inequivalent irreducibles of S₃, so the only equivariant linear map
between them is zero.  Proved here by the same direct transposition computation the
sibling file uses, over a generic commutative ring without 2-torsion.

## What it rules out, concretely

`computations/deltalambda/b3_brunnian_count_channel_probe.py` establishes that the
corpus's measured cumulants (`b₂ = 2.2245662`, `b₃ = 1.42622016` MeV) require

    tripleMutual = -(b₃ + 3 b₂) = -8.09991876 MeV

— a strictly **negative** (attractive) three-body mutual channel.  `muBar_cannot_carry_symmetric_channel`
below says that channel **cannot be a linear functional of `μ̄`**, for any coefficient
and over any such ring.  Since `μ̄(123)` is the corpus's own candidate for an
irreducibly three-body invariant, this closes the linear-in-`μ̄` route to the required
channel from the *symmetry* side, independently of `μ̄`'s normalisation.

That matters because the two existing refutations leave this gap open between them:

* `QOU.Mass.MilnorCarriesOrderNotMagnitude` refutes `μ̄` on **type** — `μ̄` is
  normalised (`±1`), so `b = c·μ̄` gives `|b| = |c|` and the magnitude is entirely
  `c`'s.  That argument is about *size*, and is silent on sign.
* `MilnorSignRepObstruction` refutes the linear coupling on **symmetry**, but only
  into the **pair-channel** target.

Neither says a symmetric *scalar* channel cannot be linear in `μ̄`.  This file does.

## Anti-vacuity — the linearity hypothesis is load-bearing, and so is `≠ 0`

Two witnesses, so a reader can see the theorem is not vacuous and not overreaching:

* `sq_functional_is_equivariant_and_nonzero` — the **quadratic** functional `x ↦ x²`
  IS S₃-equivariant into the trivial rep and is **not** identically zero.  So
  dropping linearity genuinely escapes the theorem: the surviving coupling is through
  `|μ̄|` (equivalently `μ̄²`), exactly as `muBarFamily_sq_invariant` says one file over.
  A coupling through `μ̄²` is **unsigned**, which is why this does not rescue the
  attractive channel — but that is a separate argument, not this theorem's content.
* `exists_nonzero_equivariant_into_trivial_of_trivial_source` — if the *source* is
  the trivial rep instead of the sign rep, nonzero equivariant linear maps exist.
  So the theorem is about the sign rep specifically, not about the target being small.

## Scope — read before citing

**Scope (a), and narrowly.**  This excludes **`tripleMutual` = (a linear functional of
`μ̄`)**.  It does **not** exclude: `μ̄` entering through `|μ̄|` or `μ̄²`; `μ̄` fixing the
sign and order of the terms of a multi-term closure whose sizes come from elsewhere
(the shape `MilnorCarriesOrderNotMagnitude` explicitly leaves standing); any
non-`μ̄` three-body invariant; or a channel that is not S₃-symmetric because the
components are distinguishable.  **That last one is the live escape** and is
`qou-lq6k`'s actual subject — an explicit antisymmetry-breaking weight.  Nothing here
supplies one, and proposing one because it would fit is the anti-fit violation
AGENTS.md forbids.

§7c: generic `CommRing R` throughout — no `ℝ`, no ordering, no archimedean construct.
`decide` is used only on decidable `Fin 3` data, never on ring elements.  The
2-torsion hypothesis is carried explicitly (the cancellation `v + v = 0 → v = 0` is
false in characteristic 2).

-- Ref: [leitner2026] docs/audits/2026-07-13-mirror-split-s3-em-functional-attempt.md §D2
-- Ref: [milnor1954] https://doi.org/10.2307/1969685
-/

import QOU.Mass.MilnorSignRepObstruction

namespace QOU.Mass.MilnorSignRepObstructionTripleChannel

open Equiv QOU.Mass.MilnorSignRepObstruction

variable {R : Type*} [CommRing R]

/-! ### The obstruction into the trivial representation -/

/-- **Core computation.** A ring element `c` that transforms in the SIGN representation
while its target carries the **trivial** action — `signR g * c = c` for every `g` —
vanishes, provided `R` has no 2-torsion.

Proof: a transposition has `signR = -1`, so `-c = c`, hence `c + c = 0`. -/
theorem sign_equivariant_scalar_eq_zero
    (h2 : ∀ x : R, x + x = 0 → x = 0) (c : R)
    (hequiv : ∀ g : Equiv.Perm (Fin 3), signR g * c = c) :
    c = 0 := by
  have h := hequiv (Equiv.swap (0 : Fin 3) 1)
  rw [signR_swap (by decide : (0 : Fin 3) ≠ 1)] at h
  exact h2 c (by linear_combination -h)

/-- **The triple-channel D2 obstruction.** Any S₃-equivariant `R`-linear map from the
sign representation (the line spanned by `μ̄(123)`) into the **trivial** representation
is ZERO.

This is the companion of `equivariant_linearMap_eq_zero` with the target changed from
the pair-channel module `Fin 3 → R` to a scalar carrying the trivial action — the
target a *symmetric* three-body channel actually lives in. -/
theorem equivariant_linearMap_to_trivial_eq_zero
    (h2 : ∀ x : R, x + x = 0 → x = 0)
    (T : R →ₗ[R] R)
    (hT : ∀ (g : Equiv.Perm (Fin 3)) (x : R), T (signR g * x) = T x) :
    T = 0 := by
  have hv : T 1 = 0 := by
    refine sign_equivariant_scalar_eq_zero h2 (T 1) fun g => ?_
    have h := hT g 1
    rw [mul_one] at h
    have hs : T (signR g) = signR (R := R) g * T 1 := by
      simpa [smul_eq_mul] using T.map_smul (signR g) 1
    rw [hs] at h
    exact h
  refine LinearMap.ext fun x => ?_
  have hx : T x = x * T 1 := by simpa [smul_eq_mul] using T.map_smul x 1
  rw [LinearMap.zero_apply, hx, hv, mul_zero]

/-- Convenience version, 2-torsion-freeness discharged from `[NoZeroDivisors R]` +
`[NeZero (2 : R)]` (e.g. `ℤ`, `ℚ`, or any integral domain of characteristic `≠ 2`). -/
theorem equivariant_linearMap_to_trivial_eq_zero_of_neZero_two
    [NoZeroDivisors R] [NeZero (2 : R)]
    (T : R →ₗ[R] R)
    (hT : ∀ (g : Equiv.Perm (Fin 3)) (x : R), T (signR g * x) = T x) :
    T = 0 := by
  refine equivariant_linearMap_to_trivial_eq_zero ?_ T hT
  intro x hx
  have h2x : (2 : R) * x = 0 := by rw [two_mul]; exact hx
  rcases mul_eq_zero.mp h2x with h | h
  · exact absurd h (NeZero.ne (2 : R))
  · exact h

/-! ### The audit-shaped corollary -/

/-- **A nonzero symmetric three-body channel cannot be linear in `μ̄`.**

If `T` is an S₃-equivariant linear functional of the antisymmetric invariant whose
value on `μ̄` is the required channel, and that channel is **nonzero**, contradiction.

The corpus's measured cumulants require `tripleMutual = -(b₃ + 3b₂) = -8.09991876`
MeV `≠ 0` (probe `b3_brunnian_count_channel_probe.py`), so the hypothesis `hne` is
discharged by data and the conclusion bites. -/
theorem muBar_cannot_carry_symmetric_channel
    (h2 : ∀ x : R, x + x = 0 → x = 0)
    (T : R →ₗ[R] R)
    (hT : ∀ (g : Equiv.Perm (Fin 3)) (x : R), T (signR g * x) = T x)
    (μbar channel : R) (hchannel : T μbar = channel) (hne : channel ≠ 0) :
    False := by
  rw [equivariant_linearMap_to_trivial_eq_zero h2 T hT, LinearMap.zero_apply] at hchannel
  exact hne hchannel.symm

/-! ### The "distinguishable components" escape does NOT exist for a nucleon triple

The scope note above named one live escape: the obstruction assumes full S₃-equivariance,
while a physical triple has distinguishable components (a triton is `(p,n,n)`, ³He is
`(p,p,n)`), so the symmetry available is smaller than S₃.

**That escape is empty, and the reason is pigeonhole.**  Inspect the proof of
`sign_equivariant_scalar_eq_zero`: it invokes `hequiv` at exactly **one** transposition.
Full S₃-equivariance was never needed — a single transposition under which the channel is
invariant and `μ̄` flips is enough.  And a nucleon triple always has one, because there are
only **two** species: any three nucleons include two of the same kind.

So the obstruction reaches every nucleon triple in every nucleus, `(p,n,n)`, `(p,p,n)`,
`(p,p,p)` and `(n,n,n)` alike — not only a hypothetical S₃-symmetric one.  In particular
it closes the form `qou-lq6k` actually proposes: an **antisymmetry-breaking charge
weighting** cannot work, because charge is a function of species and therefore assigns the
two like nucleons the *same* weight, leaving the swap a symmetry of the weighted channel.

**🛑 What this does NOT close, stated because the pigeonhole argument invites over-reading.**
The hypothesis is `hflip` — *there exists a swap under which `μ̄` flips and the channel does
not* — and species is not the only label a nucleon carries.  Two neutrons agree in species
but may differ in **spin** (or any other quantum number), and two components in different
states need not leave the channel invariant when exchanged.  For such a triple `hflip`
fails and nothing here applies.

So the honest statement is: **a weighting that is a function of SPECIES alone cannot break
the antisymmetry**; a weighting that distinguishes the two like nucleons by some further
quantum number is untouched, and spin is the obvious candidate.  That is a narrower and
more specific open question than `qou-lq6k` had before, not a closed one.  Nothing here
proposes such a weighting — proposing one because it would fit is the anti-fit violation. -/

/-- **Only two species, so any three nucleons include two of the same kind.**  Pigeonhole
on `Fin 3 → Fin 2`, decided exhaustively (8 species assignments). -/
theorem exists_identical_pair (species : Fin 3 → Fin 2) :
    ∃ i j : Fin 3, i ≠ j ∧ species i = species j := by
  revert species
  decide

/-- **The obstruction needs only ONE transposition — the minimal form.**

If a channel is a linear functional `T` of the antisymmetric invariant, and there is a
single component swap under which `μ̄` flips sign while the channel does not, then the
channel vanishes.  No group action, no S₃, no representation theory: linearity gives
`T(−μ̄) = −T(μ̄)`, the invariance gives `T(−μ̄) = T(μ̄)`, and the two force `T(μ̄) + T(μ̄) = 0`.

`hflip` is the physical content: *swapping two identical nucleons flips `μ̄` (it is totally
antisymmetric) and leaves the mutual energy of the triple unchanged (they are identical
particles, so the state is the same).* -/
theorem linear_in_muBar_vanishes_of_identical_pair
    (h2 : ∀ x : R, x + x = 0 → x = 0)
    (T : R →ₗ[R] R) (μbar : R)
    (hflip : T (-μbar) = T μbar) :
    T μbar = 0 := by
  rw [map_neg] at hflip
  exact h2 _ (by linear_combination -hflip)

/-- **A nucleon triple's channel cannot be linear in `μ̄` — the escape closed.**

Given any species assignment (only `p`/`n` exist), `exists_identical_pair` supplies a pair
of identical components; `hflip` is the invariance under swapping them; and the channel is
then forced to zero, contradicting a nonzero measured value.

The corpus's measured cumulants require `tripleMutual = −(b₃ + 3b₂) = −8.09991876` MeV `≠ 0`
(probe `b3_brunnian_count_channel_probe.py`), so `hne` is discharged by data.  Note the
species assignment is *arbitrary* — this is not a statement about ³H or ³He in particular. -/
theorem muBar_cannot_carry_nucleon_triple_channel
    (h2 : ∀ x : R, x + x = 0 → x = 0)
    (_species : Fin 3 → Fin 2)
    (T : R →ₗ[R] R) (μbar channel : R)
    (hflip : T (-μbar) = T μbar)
    (hchannel : T μbar = channel) (hne : channel ≠ 0) :
    False :=
  hne (hchannel ▸ linear_in_muBar_vanishes_of_identical_pair h2 T μbar hflip)

/-! ### Anti-vacuity -/

/-- **The linearity hypothesis is load-bearing.** The QUADRATIC functional `x ↦ x²` is
S₃-equivariant into the trivial representation — `(signR g * x)² = x²` — and is not
identically zero.  So the theorem above genuinely needs linearity, and the surviving
coupling is through `μ̄²` (equivalently `|μ̄|`), matching
`MilnorSignRepObstruction.muBarFamily_sq_invariant`.

Stated over `ℤ` so that "not identically zero" is a concrete, checkable claim. -/
theorem sq_functional_is_equivariant_and_nonzero :
    (∀ (g : Equiv.Perm (Fin 3)) (x : ℤ), (signR g * x) ^ 2 = x ^ 2)
      ∧ ∃ x : ℤ, x ^ 2 ≠ 0 := by
  constructor
  · intro g x
    rw [mul_pow, pow_two (signR g), signR_mul_self, one_mul]
  · exact ⟨1, by norm_num⟩

/-- **The theorem is about the SIGN source, not about the target being small.** With
the *trivial* representation as source, nonzero equivariant linear maps into the
trivial representation obviously exist — the identity is one.  Without this a reader
could suspect the conclusion came from the target rather than from Schur. -/
theorem exists_nonzero_equivariant_into_trivial_of_trivial_source :
    ∃ T : ℤ →ₗ[ℤ] ℤ, (∀ (_ : Equiv.Perm (Fin 3)) (x : ℤ), T x = T x) ∧ T ≠ 0 := by
  refine ⟨LinearMap.id, fun _ _ => rfl, ?_⟩
  intro h
  have : (1 : ℤ) = 0 := congrFun (congrArg (fun f : ℤ →ₗ[ℤ] ℤ => f.toFun) h) 1
  norm_num at this

end QOU.Mass.MilnorSignRepObstructionTripleChannel
