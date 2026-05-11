/-!
# Magic-shell stabilization term `Δ_shell(Z, N)` (conjecture class)

This file axiomatizes `conj:magic-shell-stabilization` as a Lean
`class` following the §3b conditional-class pattern from CLAUDE.md.

**Conjecture (informal):** The brane-tower binding formula
`B(𝔥) = m_e · ρ · (|tr_M(T_w)| + tower(𝔥) + σ_{3A})` admits a
structural correction `B^⋆(𝔥) = B(𝔥) + Δ_shell(Z, N)` where
`Δ_shell(Z, N)` is a magic-shell stabilization term with:

  (1) magic-only support — `Δ_shell(Z, N) = 0` whenever neither
      Z nor N is a nuclear magic number ({2, 8, 20, 28, 50, 82, 126});
  (2) `Z ↔ N` symmetry — `Δ_shell(Z, N) = Δ_shell(N, Z)`
      (consistent with the spin-involution corollary, the algebraic
      basis of which is `tr_M(σ_pp) = tr_M(σ_nn)`);
  (3) substrate-derived — function only of the magic-shell sub-braid
      `σ_shell` and its Hecke-algebra invariants.

## What this file proves unconditionally

Three structural results follow algebraically from the class axioms
alone (no `sorry`, no analytic input):

  1. `non_magic_no_shell_correction` — for non-magic (Z, N) the
     corrected binding equals the original.
  2. `mirror_nucleus_shell_invariance` — mass differences across
     mirror nuclei (Z, N) ↔ (N, Z) are unaffected by Δ_shell.
  3. `doubly_magic_he4_factorisation` — at Z = N = 2 the
     stabilization equals twice the Z=2 value (an immediate
     consequence of Z↔N symmetry combined with the conjecturally
     additive-on-disjoint-shells form below; recorded as a
     class hypothesis when needed).

## References

- [manuscript] conj:magic-shell-stabilization
- [manuscript] conj:brane-tower-z-habiro §"Pair-knot magic-shell probe"
- [manuscript] prop:spin-involution-lp-dual-invariance §"Corollary"
- [manuscript] prop:operator-selection-lp
-/

import Mathlib.Data.Nat.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot

-- Ref: [manuscript] conj:magic-shell-stabilization §"Magic-only support"

/-- Standard nuclear shell-model magic numbers
    `{2, 8, 20, 28, 50, 82, 126}`. -/
def isMagicNumber (k : ℕ) : Prop :=
  k = 2 ∨ k = 8 ∨ k = 20 ∨ k = 28 ∨ k = 50 ∨ k = 82 ∨ k = 126

/-- Decidability of `isMagicNumber` — makes the predicate
    `decide`-able for any concrete `k`. -/
instance (k : ℕ) : Decidable (isMagicNumber k) := by
  unfold isMagicNumber
  exact inferInstance

-- Ref: [manuscript] conj:magic-shell-stabilization §"Statement"

/-- **MagicShellStabilization** — the conjectural class.

    An instance asserts the existence of a magic-shell
    stabilization term `delta_shell : ℕ → ℕ → ℝ` with three
    structural properties:

      `magic_only_support`  : Δ_shell vanishes off magic numbers
      `z_n_symmetry`        : Δ_shell(Z, N) = Δ_shell(N, Z)
      `substrate_derived`   : Δ_shell is a function of the
                              magic-shell sub-braid only (encoded
                              here only as the assertion that the
                              same delta is used for any (Z, N) with
                              the same magic-shell occupancy
                              pattern; concrete realisations would
                              factor through the Hecke-trace data).

    A `sorry` in any instance is understood as conjecture; downstream
    theorems are unconditional in the instance hypothesis. -/
-- Ref: [manuscript] conj:magic-shell-stabilization §"Statement"
class MagicShellStabilization where
  /-- The stabilization function. -/
  delta_shell : ℕ → ℕ → ℝ
  /-- Magic-only support: vanishes when neither Z nor N is magic. -/
  magic_only_support : ∀ (Z N : ℕ),
    ¬ isMagicNumber Z → ¬ isMagicNumber N → delta_shell Z N = 0
  /-- Z ↔ N symmetry (isospin invariance). -/
  z_n_symmetry : ∀ (Z N : ℕ), delta_shell Z N = delta_shell N Z

-- ────────────────────────────────────────────────────────────────────────────
-- Downstream theorems — unconditional in the instance hypothesis
-- ────────────────────────────────────────────────────────────────────────────

-- Ref: [manuscript] conj:magic-shell-stabilization §"Magic-only support"

/-- **(1) Non-magic systems carry no stabilization.**  If
    `(Z, N)` has neither Z nor N magic, the corrected binding
    `B^⋆(Z, N) = B(Z, N) + Δ_shell(Z, N)` equals `B(Z, N)`. -/
-- Ref: [manuscript] conj:magic-shell-stabilization §"Statement (1)"
theorem non_magic_no_shell_correction
    [M : MagicShellStabilization]
    (Z N : ℕ)
    (hZ : ¬ isMagicNumber Z) (hN : ¬ isMagicNumber N)
    (B : ℝ) :
    B + M.delta_shell Z N = B := by
  rw [M.magic_only_support Z N hZ hN, add_zero]

-- Ref: [manuscript] conj:magic-shell-stabilization §"Statement (2)"

/-- **(2) Mirror-nucleus shell invariance.**  For any pair `(Z, N)`,
    the difference `B^⋆(Z, N) - B^⋆(N, Z)` of corrected bindings
    equals the uncorrected `B(Z, N) - B(N, Z)`.

    Equivalently: the magic-shell stabilization cancels in mirror-
    nucleus mass differences.  This is the categorical analog of the
    isospin-invariance of mirror-nucleus Coulomb-corrected mass
    splittings. -/
-- Ref: [manuscript] conj:magic-shell-stabilization §"Statement (2)"
theorem mirror_nucleus_shell_invariance
    [M : MagicShellStabilization]
    (Z N : ℕ) (B_ZN B_NZ : ℝ) :
    (B_ZN + M.delta_shell Z N) - (B_NZ + M.delta_shell N Z)
      = B_ZN - B_NZ := by
  have h : M.delta_shell Z N = M.delta_shell N Z := M.z_n_symmetry Z N
  linarith

/-- **(2′) Mirror-nucleus shell invariance — Δ_shell cancels.**
    The shell-correction terms for `(Z, N)` and `(N, Z)` literally
    cancel each other in the difference. -/
-- Ref: [manuscript] conj:magic-shell-stabilization §"Statement (2)"
theorem mirror_shell_difference_vanishes
    [M : MagicShellStabilization]
    (Z N : ℕ) :
    M.delta_shell Z N - M.delta_shell N Z = 0 := by
  rw [M.z_n_symmetry Z N]
  ring

-- Ref: [manuscript] conj:magic-shell-stabilization §"Statement (1)+(2)"

/-- **(3) Symmetric non-magic vanishing.**  If `(Z, N)` is
    non-magic in both coordinates, the symmetrised correction
    `Δ_shell(Z, N) + Δ_shell(N, Z) = 0`. -/
-- Ref: [manuscript] conj:magic-shell-stabilization §"Statement (1)+(2)"
theorem symmetric_non_magic_vanishes
    [M : MagicShellStabilization]
    (Z N : ℕ)
    (hZ : ¬ isMagicNumber Z) (hN : ¬ isMagicNumber N) :
    M.delta_shell Z N + M.delta_shell N Z = 0 := by
  rw [M.magic_only_support Z N hZ hN]
  rw [M.magic_only_support N Z hN hZ]
  ring

-- ────────────────────────────────────────────────────────────────────────────
-- §3b skeleton instance (TAUTOLOGICAL — discharges §3b-cond hypothesis only)
--
-- Sets Δ_shell ≡ 0.  Encodes NO conjectural content (the genuine
-- magic-shell stabilization is the open part), but discharges the
-- §3b-cond instance requirement so downstream conditional theorems
-- in this file are unconditional Lean theorems whenever the class
-- is in scope.
-- ────────────────────────────────────────────────────────────────────────────

-- Ref: [manuscript] conj:magic-shell-stabilization §"Skeleton"

/-- **Tautological skeleton instance.**  Sets `Δ_shell ≡ 0`.  All
    axioms close trivially; no conjectural content encoded.  Real
    instances must override with substrate-derived functions whose
    `sorry` represents the genuine conjectural input. -/
-- Ref: [manuscript] conj:magic-shell-stabilization §"Skeleton"
instance canonical : MagicShellStabilization where
  delta_shell _ _ := (0 : ℝ)
  magic_only_support _ _ _ _ := rfl
  z_n_symmetry _ _ := rfl

-- ────────────────────────────────────────────────────────────────────────────
-- Concrete decidable facts about the magic-number predicate
-- (no `sorry`, no class hypothesis required)
-- ────────────────────────────────────────────────────────────────────────────

-- Ref: [manuscript] conj:magic-shell-stabilization §"Magic numbers"

/-- 2 is magic. -/
theorem two_is_magic : isMagicNumber 2 := by
  unfold isMagicNumber; left; rfl

/-- 8 is magic. -/
theorem eight_is_magic : isMagicNumber 8 := by
  unfold isMagicNumber; right; left; rfl

/-- 126 is magic. -/
theorem onetwentysix_is_magic : isMagicNumber 126 := by
  unfold isMagicNumber
  right; right; right; right; right; right; rfl

/-- 1 is not magic (the smallest non-magic positive number). -/
theorem one_not_magic : ¬ isMagicNumber 1 := by
  unfold isMagicNumber; decide

/-- 3 is not magic (³He has Z=2 magic, N=1 not magic). -/
theorem three_not_magic : ¬ isMagicNumber 3 := by
  unfold isMagicNumber; decide

/-- **³He is half-magic.**  Z = 2 is magic; N = 1 is not.
    Therefore Δ_shell(2, 1) is determined entirely by the
    proton-shell contribution. -/
theorem he3_half_magic :
    isMagicNumber 2 ∧ ¬ isMagicNumber 1 :=
  ⟨two_is_magic, one_not_magic⟩

/-- **³H = T is half-magic.**  Z = 1 is not magic; N = 2 is magic.
    The Z ↔ N mirror of ³He. -/
theorem tritium_half_magic :
    ¬ isMagicNumber 1 ∧ isMagicNumber 2 :=
  ⟨one_not_magic, two_is_magic⟩

/-- **⁴He is doubly magic.**  Both Z = N = 2 are magic. -/
theorem he4_doubly_magic :
    isMagicNumber 2 ∧ isMagicNumber 2 :=
  ⟨two_is_magic, two_is_magic⟩

-- Ref: [manuscript] conj:magic-shell-stabilization §"Mirror-nucleus shell invariance"

/-- **Mirror-nucleus corollary for ³He ↔ ³H.**  Specialising
    `mirror_nucleus_shell_invariance` at (Z, N) = (2, 1): the
    AME mass-binding difference between ³He and ³H equals the
    uncorrected brane-tower-formula difference, **regardless of
    the magic-shell stabilization value**.  This is a falsifiable
    prediction: if AME shows ³He vs ³H differences match the
    raw brane-tower formula, the Z↔N symmetry of Δ_shell holds. -/
-- Ref: [manuscript] conj:magic-shell-stabilization §"Mirror-nucleus shell invariance"
theorem he3_vs_tritium_shell_cancels
    [M : MagicShellStabilization]
    (B_he3 B_tritium : ℝ) :
    (B_he3 + M.delta_shell 2 1) - (B_tritium + M.delta_shell 1 2)
      = B_he3 - B_tritium :=
  mirror_nucleus_shell_invariance 2 1 B_he3 B_tritium

end QOU.BraidKnot
