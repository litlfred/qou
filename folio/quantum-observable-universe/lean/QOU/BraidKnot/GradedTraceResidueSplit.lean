import QOU.BraidKnot.ConfinementLevel
import Mathlib.Algebra.Field.Basic
import Mathlib.LinearAlgebra.Quotient.Basic

/-!
# QOU.BraidKnot.GradedTraceResidueSplit — graded-trace residue split

The Markov trace on the filtered Hecke algebra `H_n(q)` decomposes
canonically as

    tr_M(T_w) = tr_gr(σ(T_w)) + Res_GB(T_w)

where `σ` is the symbol map to the associated graded algebra and
`Res_GB` is the sum of rewriting-defect residues at root-of-unity
poles.  Filtered-algebra analogue of Strutinsky's smooth-plus-
oscillating nuclear-energy decomposition.

**Pre-Archimedean.** Polymorphic in the ground field `R`; the
opaque trace declarations carry `q : R` and return values in `R`,
not `ℝ`.  Per `QOU.GroundRingAnnotations`, this stub is in the
formal pre-Arch chain.

**Formal-chain version.**  Lives under `lean/QOU/` and is compiled
by `lake build`.  The co-located documentation stub at
`braids-and-knots/graded-trace-residue-split.lean` mirrors this.

LaTeX label: `prop:graded-trace-residue-split`
-/

namespace QOU.BraidKnot

universe u

/-- The symbol map `σ: J^ℓ → J^ℓ/J^{ℓ+1}`.  Concrete model: identity. -/
def symbolMap
    {_R : Type u} [CommRing _R] (_ℓ : ℕ) (_q : _R) : Unit → Unit := id

/-- The Markov trace on the associated graded algebra.  Concrete
    model: returns 0. -/
def GradedTraceResidueSplit.gradedTrace
    {R : Type u} [CommRing R] (_q : R) (_x : Unit) : R := 0

/-- The total residue contribution.  Concrete model: returns 0. -/
def GradedTraceResidueSplit.gbResidue
    {R : Type u} [CommRing R] (_q : R) (_x : Unit) : R := 0

/-- The full Markov trace.  Concrete model: returns 0. -/
def GradedTraceResidueSplit.markovTrace
    {R : Type u} [CommRing R] (_q : R) (_x : Unit) : R := 0

/-- **Graded-trace residue split.**  Polymorphic in the ground field `R`.

    The Markov trace decomposes as smooth (graded) + oscillating
    (residue), the categorical analogue of Strutinsky's
    macroscopic + shell-correction split. -/
class GradedTraceResidueSplit (R : Type u) [CommRing R] where
  q : R
  element : Unit
  smooth : R       -- tr_gr(σ(element), q)
  oscillating : R  -- Res_GB(element, q)
  total : R        -- tr_M(element, q)
  split_identity :
    total = smooth + oscillating
  smooth_is_graded :
    smooth = GradedTraceResidueSplit.gradedTrace q element
  oscillating_is_residue :
    oscillating = GradedTraceResidueSplit.gbResidue q element

/-- Level-0 case: when oscillating residue vanishes, total = smooth.
    This recovers the pure-descended regime.

    Ref: [leitner2026] `prop:categorical-mass-markov`. -/
theorem level_zero_pure_descended
    {R : Type u} [CommRing R] (S : GradedTraceResidueSplit R)
    (h : S.oscillating = 0) :
    S.total = S.smooth := by
  rw [S.split_identity, h, add_zero]

/-- The graded-trace residue split is the algebraic shadow of
    Strutinsky's `E = Ẽ + δE_shell`.

    Ref: [leitner2026] §Nuclear Binding and Beta Stability. -/
theorem strutinsky_analogue
    {R : Type u} [CommRing R] (S : GradedTraceResidueSplit R) :
    -- The split exists and is canonical; the physics interpretation
    -- is developed in the Physical Observations chapter.
    S.total = S.smooth + S.oscillating :=
  S.split_identity


/-! ### The split, proved for a filtered module

The class and the `Unit`-valued model above carry no content: the model traces
are all `0`, and the class assumes `total = smooth + oscillating`.  Defining the
residue as `tr − tr_gr ∘ σ` would make the split true by definition, so that is
not what is proved here.  What is proved is the part that has content: for a
filtration step `J^{ℓ+1} ≤ J^ℓ`, the symbol `σ : J^ℓ → J^ℓ/J^{ℓ+1}` and a linear
section `s` of it, every `x ∈ J^ℓ` decomposes as

    x = s(σ x) + r,   r ∈ J^{ℓ+1},

the decomposition is unique, and so `τ x = τ(s(σ x)) + τ r` for any linear
`τ`: the graded part is `τ ∘ s` on the associated graded piece, and the residue
is `τ` of an element of the **next** filtration stratum.  If `τ` vanishes on
`J^{ℓ+1}`, the residue vanishes (the level-zero case).

Not proved here: the identification of the residue with the Habiro-expansion
root-of-unity residues `Res_GB` of the block prose, and the choice of the GS
filtration on `H_n(q)`.  The statement is for an arbitrary filtration step and
section.
-/

section FilteredSplit

variable {R : Type u} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M]

/-- **Graded-trace residue split** ([`prop:graded-trace-residue-split`], for one
filtration step).  Let `J₁ ≤ J₀` be submodules (`J^{ℓ+1} ≤ J^ℓ`), let
`σ = mkQ : J₀ → J₀/J₁` be the symbol map, and let `s` be a linear section of
`σ`.  For every `x ∈ J₀`:

1. the residue `x − s(σ x)` lies in `J₁`;
2. `τ x = τ(s(σ x)) + τ(x − s(σ x))` for every linear `τ : M → R`;
3. the split is unique: if `x = s y + r` with `r ∈ J₁`, then `y = σ x` and
   `r = x − s(σ x)`;
4. if `τ` vanishes on `J₁`, then `τ x = τ(s(σ x))`. -/
theorem graded_trace_residue_split_of_section
    (J₁ J₀ : Submodule R M) (hJ : J₁ ≤ J₀) (τ : M →ₗ[R] R)
    (s : (J₀ ⧸ J₁.comap J₀.subtype) →ₗ[R] J₀)
    (hs : ∀ y, (J₁.comap J₀.subtype).mkQ (s y) = y) (x : J₀) :
    ((x : M) - (s ((J₁.comap J₀.subtype).mkQ x) : M) ∈ J₁) ∧
    τ x = τ (s ((J₁.comap J₀.subtype).mkQ x))
        + τ ((x : M) - (s ((J₁.comap J₀.subtype).mkQ x) : M)) ∧
    (∀ (y : J₀ ⧸ J₁.comap J₀.subtype) (r : M), r ∈ J₁ → (x : M) = s y + r →
        y = (J₁.comap J₀.subtype).mkQ x ∧
        r = (x : M) - (s ((J₁.comap J₀.subtype).mkQ x) : M)) ∧
    ((∀ m ∈ J₁, τ m = 0) → τ x = τ (s ((J₁.comap J₀.subtype).mkQ x))) := by
  set σx := (J₁.comap J₀.subtype).mkQ x with hσx
  have hres : (x : M) - (s σx : M) ∈ J₁ := by
    have h0 : (J₁.comap J₀.subtype).mkQ (x - s σx) = 0 := by
      rw [map_sub, hs, hσx, sub_self]
    have hmem : x - s σx ∈ J₁.comap J₀.subtype :=
      (Submodule.Quotient.mk_eq_zero _).mp h0
    simpa [Submodule.mem_comap] using hmem
  have hsplit : τ x = τ (s σx) + τ ((x : M) - (s σx : M)) := by
    rw [map_sub]; ring
  refine ⟨hres, hsplit, ?_, ?_⟩
  · intro y r hr hx
    have hrJ0 : r ∈ J₀ := hJ hr
    have hxeq : x = s y + ⟨r, hrJ0⟩ := Subtype.ext (by simpa using hx)
    have hrN : (⟨r, hrJ0⟩ : J₀) ∈ J₁.comap J₀.subtype := by
      simpa [Submodule.mem_comap] using hr
    have hy : σx = y := by
      rw [hσx, hxeq, map_add, hs, Submodule.mkQ_apply, (Submodule.Quotient.mk_eq_zero _).mpr hrN,
        add_zero]
    refine ⟨hy.symm, ?_⟩
    rw [hy, hx]; abel
  · intro hτ
    rw [hsplit, hτ _ hres, add_zero]

end FilteredSplit

/-! ### Removed 2026-08-30 — self-assuming projections

- `graded_trace_residue_split` — body was `s.split_identity`: the conclusion was the projected field
  verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, which asserts the same proposition under the same hypotheses; only
the restatement goes. That is the vacuity ledger's recorded disposition for
this category — *"drop the pseudo-theorem and project the field at use sites"*
— and there were no use sites: each had **zero references anywhere in the
corpus**, including in this file. Bean `qou-z9ws`.
-/

end QOU.BraidKnot
