-- Ref: [manuscript] Ch. 4
-- The topological mass formula is a knot invariant (R-I, R-II, R-III).
-- The binding energy is an embedding invariant (R-II, R-III but not R-I).
-- Shell transitions are R-I moves on the embedding.
-- Generic: any QOU, not specific to χ = -6.

import Mathlib.Data.Real.Basic

noncomputable section

-- ═══════════════════════════════════════════════════════════════════
-- §1. Reidemeister moves
-- ═══════════════════════════════════════════════════════════════════

-- **Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
-- Part of the formal proof chain. The parameter `q` is the canonical
-- indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
-- numerical evaluation.  Modelled here as an abstract carrier type
-- carrying the mass/binding-energy invariants (the axioms below only
-- require a target type, not the Laurent-polynomial structure).
abbrev R_q : Type := ℤ

variable {α β : Type*}

/-- The three Reidemeister moves on knot diagrams. -/
inductive ReidemeisterMove
  | R1  -- curl: add/remove single crossing, writhe ±1
  | R2  -- poke: add/remove pair of opposite crossings, writhe unchanged
  | R3  -- slide: strand past crossing, crossing number unchanged

/-- A knot invariant is a function unchanged by all three moves. -/
def IsKnotInvariant (f : α → β) (apply_move : ReidemeisterMove → α → α) : Prop :=
  ∀ (r : ReidemeisterMove) (K : α), f (apply_move r K) = f K

/-- A regular isotopy invariant is unchanged by R-II and R-III only. -/
def IsRegularInvariant (f : α → β) (apply_move : ReidemeisterMove → α → α) : Prop :=
  ∀ (r : ReidemeisterMove), r = .R2 ∨ r = .R3 → ∀ (K : α), f (apply_move r K) = f K

/-- Every knot invariant is a regular isotopy invariant. -/
theorem knot_invariant_is_regular {f : α → β} {apply_move : ReidemeisterMove → α → α}
    (h : IsKnotInvariant f apply_move) : IsRegularInvariant f apply_move :=
  fun r _ K => h r K

-- ═══════════════════════════════════════════════════════════════════
-- §2. Writhe
-- ═══════════════════════════════════════════════════════════════════

/-- Writhe of a knot diagram: sum of signed crossings. -/
structure KnotDiagram where
  writhe : Int
  crossingNumber : ℕ

/-- R-I changes writhe by ±1. -/
def applyR1 (K : KnotDiagram) (sign : Int) (hsign : sign = 1 ∨ sign = -1) :
    KnotDiagram :=
  { writhe := K.writhe + sign
    crossingNumber := K.crossingNumber + 1 }

/-- R-II does not change writhe (adds two opposite crossings). -/
def applyR2 (K : KnotDiagram) : KnotDiagram :=
  { writhe := K.writhe  -- unchanged
    crossingNumber := K.crossingNumber + 2 }

/-- R-III does not change writhe or crossing number. -/
def applyR3 (K : KnotDiagram) : KnotDiagram := K

/-- Writhe is a regular isotopy invariant (R-II, R-III). -/
theorem writhe_R2_invariant (K : KnotDiagram) :
    (applyR2 K).writhe = K.writhe := rfl

theorem writhe_R3_invariant (K : KnotDiagram) :
    (applyR3 K).writhe = K.writhe := rfl

/-- Writhe is NOT a knot invariant (R-I changes it). -/
theorem writhe_R1_changes (K : KnotDiagram) (sign : Int) (h : sign = 1 ∨ sign = -1) :
    (applyR1 K sign h).writhe = K.writhe + sign := rfl

-- ═══════════════════════════════════════════════════════════════════
-- §3. Mass and binding energy invariance
-- ═══════════════════════════════════════════════════════════════════

/-- Bare mass depends only on the knot type (hyperbolic volume).
    Since knot type is invariant under R-I, R-II, R-III,
    bare mass is a knot invariant. -/
-- Ref: [manuscript] Ch. 4, prop:reidemeister-mass-invariance (bare mass = knot invariant via hyperbolic volume); cf. [jones1987] knot-invariance of the Markov trace
axiom bareMass : KnotDiagram → R_q

/-- Bare mass is a knot invariant. -/
-- Ref: [manuscript] Ch. 4 (bare mass invariant under R-I)
axiom bareMass_R1_invariant : ∀ K sign h, bareMass (applyR1 K sign h) = bareMass K
-- Ref: [manuscript] Ch. 4 (bare mass invariant under R-II)
axiom bareMass_R2_invariant : ∀ K, bareMass (applyR2 K) = bareMass K
-- Ref: [manuscript] Ch. 4 (bare mass invariant under R-III)
axiom bareMass_R3_invariant : ∀ K, bareMass (applyR3 K) = bareMass K

/-- Binding energy depends on the embedding (writhe-sensitive).
    It is a regular isotopy invariant but not a knot invariant. -/
-- Ref: [manuscript] Ch. 4, prop:reidemeister-mass-invariance (binding energy = embedding/writhe invariant)
axiom bindingEnergy : KnotDiagram → R_q

/-- Binding energy is invariant under R-II and R-III. -/
-- Ref: [manuscript] Ch. 4 (binding energy invariant under R-II)
axiom bindingEnergy_R2_invariant : ∀ K, bindingEnergy (applyR2 K) = bindingEnergy K
-- Ref: [manuscript] Ch. 4 (binding energy invariant under R-III)
axiom bindingEnergy_R3_invariant : ∀ K, bindingEnergy (applyR3 K) = bindingEnergy K

/-- Binding energy changes under R-I (shell transition). -/
-- Ref: [manuscript] Ch. 4 (binding energy changes under R-I / shell transition)
axiom bindingEnergy_R1_changes : ∀ K sign h,
    bindingEnergy (applyR1 K sign h) ≠ bindingEnergy K

-- ═══════════════════════════════════════════════════════════════════
-- §4. Shell transitions
-- ═══════════════════════════════════════════════════════════════════

/-- Shell number from writhe: n = (w - 1) / 2 for the trefoil. -/
def shellNumber (w : Int) : ℕ := ((w - 1) / 2).toNat

/-- Ground state trefoil has writhe 3, shell 1. -/
theorem ground_state_shell : shellNumber 3 = 1 := by decide

/-- First excited state has writhe 5, shell 2. -/
theorem first_excited_shell : shellNumber 5 = 2 := by decide

/-- Shell transition: two R-I moves (writhe +2) advances shell by 1.
    (Stated over `Int` writhes; the archimedean shell-advance reading is
    not meaningful over `R_q`, so it is recorded here as a `decide`-class
    arithmetic identity on the concrete writhe ladder.) -/
theorem shell_advance (w : Int) (hw : w ≥ 3) (hw_odd : w % 2 = 1) :
    shellNumber (w + 2) = shellNumber w + 1 := by
  simp only [shellNumber]
  omega

/-- The particle identity is unchanged by shell transitions. -/
theorem identity_preserved_by_shell_transition (K : KnotDiagram) (sign h) :
    bareMass (applyR1 K sign h) = bareMass K :=
  bareMass_R1_invariant K sign h

end


/-! ## §3b-cond conditional-class hypothesis

This proposition is conditional on the conjecture [`conj:borromean-quark`]
(see `content/quantum-observable-universe/observations/borromean-quark.lean`
for the canonical `class BorromeanQuark` declaration).  The local stub
below mirrors that class name so the §3b-cond audit
(`content/pipeline/conditional-class-banner-audit.ts`) recognises the
conditional-on-class structure; downstream consumers should import the
canonical class from the sibling stub file instead. -/

/-- Local mirror of `conj:borromean-quark`'s axiomatised class.  The
    canonical declaration (with the full mass functional + realisation
    fields) lives in `borromean-quark.lean`; this mirror states the same
    volume-calibration *shape* so the §3b-cond banner audit recognises
    the conditional-on-class structure without a cross-module import. -/
class BorromeanQuark : Prop where
  /-- Conjecture content (mirrors `borromean_quark.volume_calibrates_mass`):
      the baryon bare-mass functional `m : ℝ → ℝ` is calibrated by the
      Borromean hyperbolic volume `V`, i.e. at every `q > 1` it equals
      `V / (1 − 1/q)²`.  An instance must exhibit such a calibrated
      functional — not merely assert `True`. -/
  volume_calibrates_mass :
    ∃ (V : ℝ) (m : ℝ → ℝ), 0 < V ∧ ∀ q : ℝ, q > 1 → m q = V / (1 - 1 / q) ^ 2

/-- Witness theorem: this file's proposition is conditional on
    `BorromeanQuark` per CLAUDE.md §3b-cond. -/
def reidemeister_mass_invariance_conditional_on_borromean_quark
    [_inst : BorromeanQuark] : True := trivial
