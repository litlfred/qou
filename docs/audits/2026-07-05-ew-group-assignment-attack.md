# EW group-assignment attack — far-commutation obstruction (2026-07-05)

**Branch:** `claude/ew-group-assignment-attack-2026-07-05` — PR #3397
**Target:** the group-assignment postulate `EWGroupAssignment` /
`conj:weinberg-angle-categorical` / `conj:categorical-linking-operation`
that the merged EW-triplet work relocated the residual EW openness to.

**Discipline:** formalize-first, honest. A proved *negative* that narrows the
postulate is the intended good outcome. No θ_W numerics chased; no CAL-4 / free
coupling introduced.

---

## 1. What is now PROVED (the obstruction)

New content block
[`prop:ew-slot-far-commutation-obstruction`](https://github.com/litlfred/qou/blob/claude/ew-group-assignment-attack-2026-07-05/content/quantum-observable-universe/particle-interactions/ew-slot-far-commutation-obstruction.md)
(Lean sibling
[`ew-slot-far-commutation-obstruction.lean`](https://github.com/litlfred/qou/blob/claude/ew-group-assignment-attack-2026-07-05/content/quantum-observable-universe/particle-interactions/ew-slot-far-commutation-obstruction.lean),
namespace `QOU.ParticleInteractions`, sorry-free, generic ring — no ℝ, §7c).

**The chain (all sorry-free):**

1. **The slot indices are pairwise far apart.** `1,3,5` satisfy `|i−j| ≥ 2`
   (`slot_indices_farApart`, by `decide`). So the braid far-commutation relation
   `σ_i σ_j = σ_j σ_i` (`|i−j| ≥ 2`) — carried as the defining field
   `BraidGenerators.farCommute` — applies to every pair.

2. **The slot subalgebra is mutually abelian.**
   `slotSubmonoid_commutative`: any two elements of
   `Submonoid.closure {σ₁, σ₃, σ₅}` commute. Proved through the centralizer
   submonoid (`closure S ≤ centralizer S`, then
   `closure S ≤ centralizer ↑(closure S)`) — no induction bookkeeping,
   robust. Grounded, non-vacuous: the actual carriers
   `W = σ₁⁴, Z = σ₃⁶, H = σ₅⁸` pairwise commute (`carriers_commute`).

3. **A nonzero Lie bracket forbids commutation.**
   `nonabelian_bracket_forbids_commute`: `⁅x,y⁆ = z ≠ 0 ⟹ ¬ Commute x y`
   (crux; runs `bracket_eq_zero_of_commute` against `z ≠ 0`, not vacuous).

4. **Capstone — `su2L_nonabelianness_not_in_slots`.** If two `su(2)_L` adjoint
   generators `J₁,J₂` satisfy `⁅J₁,J₂⁆ = J₃` with `J₃ ≠ 0` and **both** lie in
   the slot subalgebra, that is a contradiction (`False`). Positive form
   `su2L_generator_escapes_slots`: at least one of `J₁,J₂` is not slot-built.

**Scope classification (AGENTS.md §"Before declaring refuted"): case (b),
structural exclusion.** The forbidding invariant is a *proved* Lean
impossibility — the identical vanishing of the commutator on a commutative
subalgebra — not a numerical near-miss. This is a legitimate (b) because it
cites a proved invariant (commutator vanishing), exactly as the rule requires.
It is **not** an over-claim: it excludes only realisation *purely among the
far-commuting slots*, and explicitly points to where the structure does live.

## 2. What is DERIVED for Task 2 (Cartan-slot assignment) — HONESTLY: nothing new is forced

**Question:** is there a structural reason forcing WHICH vector slot is the
neutral Cartan `W³ → Z`, independent of the θ_W number?

**Answer: NO — and the obstruction sharpens *why* not, without fabricating a
forcing.** The obstruction says the non-abelian (Cartan/root-distinguishing)
structure is a property of the inter-slot *linking*, not of the individual
far-commuting slots. Since the slots mutually commute, they are
interchangeable at the level of the commutative subalgebra: no invariant of a
single slot (or of the commuting triple alone) can distinguish the Cartan
member. This is fully consistent with — and gives the algebraic *reason* for —
the pre-existing sorry-free `which_slot_is_W_free` /
`signed_C_does_not_force_W_slot_but_forces_neutral_mixed` results
([`thm:ew-triplet-charge-spin-from-involution`](https://github.com/litlfred/qou/blob/claude/ew-group-assignment-attack-2026-07-05/content/quantum-observable-universe/particle-interactions/electroweak-triplet-charge-spin-from-involution.md)):
no single-slot topological invariant selects the neutral slot.

**The exact missing input (unchanged, now localized):** the alignment of the
two `A₋` vector slots with the `su(2)_L` Cartan–Weyl basis — the open class
`EWGroupAssignment`, equivalently the `(W³,B) → (Z,γ)` Weinberg mixing data of
`conj:weinberg-angle-categorical`. The obstruction does not supply it; it
proves the datum must come from the linking layer, so any future derivation of
the Cartan slot must be built from `σ₂, σ₄` / `Lk_R`
(`conj:categorical-linking-operation`), never from the slots alone.

## 3. What stays OPEN

- **The θ_W numerics.** Untouched by design. The simple uniform-multiplicity
  reading `cot θ_W = q₀⁻⁴ ≈ 0.66` is numerically refuted vs CODATA `1.82`
  (recorded in `weinberg-angle-categorical.md`); a fitted match would violate
  three-calibration discipline. Not attempted.
- **The Cartan-slot selection** (`EWGroupAssignment` instance) — the residual
  group-theoretic input, now provably a linking-layer object.
- **The categorical-linking-operation** substrate-specific properties
  (Properties 3 post-trace / 4 / 5 of `conj:categorical-linking-operation`)
  that a concrete `Lk_R`-based su(2)_L realisation would need.

## 4. Net: NARROWED, not closed

The postulate is **narrowed**: the non-abelian `SU(2)_L` gauge structure is
now *proved* to be un-realisable among the far-commuting slots, hence localized
to the inter-slot linking (`σ₂, σ₄` do not far-commute —
`interSlot_not_farApart`; `Lk_R` braids between slots). The relocated postulate
`EWGroupAssignment` is *not* discharged — it remains the open input — but its
domicile is now pinned to the linking layer rather than left ambiguous between
"slots" and "linking".

**Verification:** `lean`-direct exit 0 (sorry-free, no warnings) on
`lake-cache/qou-v4-24-0`, toolchain `leanprover/lean4:v4.24.0`.
