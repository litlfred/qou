import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Powerset
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Finset.Card
import Mathlib.Tactic.NormNum

/-!
# QOU.BraidsAndKnots.WignerSU4FromSpinIsospin — the D11 Wigner SU(4) carrier

Carrier for content block
[`conj:wigner-su4-from-spin-isospin`](../../../nuclear-interactions/wigner-su4-from-spin-isospin.md):
the SU(4) = SU(2)_S × SU(2)_I spin-isospin symmetry as the combined classical limit of the
spin SO(3) fibre action (D10) and the canonical isospin ℤ/2 swap (D9).

**No instance is provided** — the honest open state for a conjecture (AGENTS.md §3b).

## 2026-09-05 — moved here, and the two real fields were UNINHABITABLE

This file was at `QOU/ParticleInteractions/WignerSU4FromSpinIsospin.lean` under
`namespace QOU`, while the block's `.ts` referenced
`qou:QOU.BraidsAndKnots.WignerSu4FromSpinIsospin` — a **different** declaration, the
vacuous `holds : Prop` stub that used to sit beside the block. So the block resolved to a
carrier asserting nothing while this one, asserting something, had no reader.

Two things were repaired together, on an owner ruling:

**1. The ref now resolves here.** Following the disposition `TFromTraceCyclicity` already
established in this same queue — stub deleted, decl path matching file path so
[`§0a`](../../../../../AGENTS.md) candidate-2 resolution works — this file moved to
`QOU/BraidsAndKnots/`, the namespace became `QOU.BraidsAndKnots`, and the `.ts` ref was
aligned to `WignerSU4` (the correct capitalisation of the group, which the library
declaration already used; it was the *ref* that had `Su4`).

**2. 🛑 The two content-bearing fields asserted a falsehood.** They read

```lean
dynamic_capacity_from_plancherel_weight (A Z N : ℕ) (S W_lam E_gate E_0 : ℝ) :
  E_gate = E_0 * Real.log (1 / W_lam)
```

— i.e. `E_gate = E_0 · log(1/W_λ)` **for all reals whatsoever**, with no hypothesis
relating them. Instantiating at `E_gate := 1`, `E_0 := 0` gives `1 = 0`, so
`¬ Nonempty WignerSU4FromSpinIsospin` was **provable** and the class had no instance at
all. That is not the same defect as the stub's and is arguably worse: a vacuous carrier
makes a conditional theorem *conditional on nothing*, whereas an uninhabitable one makes
it **vacuously true**, which reads as proved.

The fix is the shape every other carrier in this queue uses: the quantities become
**caller-supplied parameters**, and the fields constrain them. Following the rule recorded
in `QOU/AlgebraicSubstrate/ConditionalClasses.lean` after its own retraction — an `∃` over
a quantity the class itself chooses cannot be false, whereas a `∀` about a quantity the
caller supplies can be — the class is now genuinely refutable, and that is discharged as a
theorem below rather than claimed here.

## What is encoded

1. **Concrete finite-dimensional spin-isospin state space and `A = 4` singlet uniqueness (proved unconditionally, bean `qou-n2un`):**
   * `SpinIsospinState := Fin 2 × Fin 2` carries the 4-state single-nucleon spin-isospin basis `|s, t⟩` (`Fintype.card SpinIsospinState = 4`, proved in `spinIsospinState_card`).
   * `AntisymSlaterState (k : ℕ) := {s : Finset SpinIsospinState // s.card = k}` models the `k`-nucleon totally-antisymmetric (exterior / Slater-determinant) basis states.
   * `wigner_a_four_antisymmetric_singlet : Fintype.card (AntisymSlaterState 4) = 1` proves Wigner's `A = 4` supermultiplet singlet dimension (`dim Λ⁴(ℂ² ⊗ ℂ²) = C(4, 4) = 1`), and `wigner_pauli_exclusion_gt_four : ∀ k > 4, IsEmpty (AntisymSlaterState k)` proves Pauli exclusion above `A = 4`.
   * `alpha_cluster_quadruplet_decomposition (A : ℕ)` proves the α-cluster quadruplet Euclidean decomposition `A = 4 * (A / 4) + A % 4` with residual valence `A % 4 < 4` (and exact closure `A = 4 * (A / 4)` whenever `4 ∣ A`).
2. **Conjectural dynamic capacity & occupancy laws (`WignerSU4FromSpinIsospin` class, indexed by mass number `A`):**
   * **Dynamic cluster capacity from the Plancherel weight** — `E_gate A = E₀ · log(1 / W A)`,
     where `W A` is the Plancherel weight of the SU(4) spin-flavour conjugate partition
     `λ ⊢ 3A`.
   * **Dynamic occupancy** — `c A = B_AME A / E_gate A`, superseding the empirical magic
     `A·8G` baseline.

`E₀` and the families `W`, `E_gate`, `B_AME`, `c` are parameters, so an instance is a real
commitment about a particular set of data.

## Base ring

`ℝ`, because `Real.log` appears in the capacity law. Nothing else archimedean is used.

-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/wigner-su4-from-spin-isospin.ts
-/

namespace QOU.BraidsAndKnots

/-! ## §1 Single-nucleon spin-isospin basis and `A = 4` Slater singlet (bean `qou-n2un`) -/

/-- The single-nucleon spin-isospin basis `Fin 2 × Fin 2` (`|↑/↓⟩ ⊗ |p/n⟩`),
    whose 4 states span the fundamental representation of `SU(4) ⊃ SU(2)_S × SU(2)_I`. -/
abbrev SpinIsospinState : Type := Fin 2 × Fin 2

/-- The single-nucleon spin-isospin state space has exact dimension `2 × 2 = 4`. -/
theorem spinIsospinState_card : Fintype.card SpinIsospinState = 4 := by
  decide

/-- The `k`-nucleon totally-antisymmetric (Slater-determinant / exterior-power
    `Λ^k(ℂ⁴)`) basis states, represented as `k`-element subsets of the 4
    single-nucleon spin-isospin states. -/
abbrev AntisymSlaterState (k : ℕ) : Type :=
  {s : Finset SpinIsospinState // s.card = k}

/-- **Wigner's `A = 4` totally-antisymmetric singlet (`dim Λ⁴(ℂ⁴) = 1`):**
    by construction of the 4-element subtype `AntisymSlaterState 4`, there is a
    unique 4-nucleon totally-antisymmetric spin-isospin state (the α-cluster
    `⁴He` closed shell `s = Finset.univ`), so the exterior power `Λ⁴` is
    1-dimensional. -/
theorem wigner_a_four_antisymmetric_singlet :
    Fintype.card (AntisymSlaterState 4) = 1 := by
  decide

/-- **Pauli exclusion above `A = 4` (`Λ^k(ℂ⁴) = 0` for `k > 4`):**
    no totally-antisymmetric spin-isospin state exists on a single spatial
    orbital for `k > 4` nucleons. -/
theorem wigner_pauli_exclusion_gt_four (k : ℕ) (hk : 4 < k) :
    IsEmpty (AntisymSlaterState k) := by
  refine ⟨fun ⟨s, hs⟩ => ?_⟩
  have hle : s.card ≤ Fintype.card SpinIsospinState := s.card_le_univ
  rw [spinIsospinState_card, hs] at hle
  omega

/-- **α-cluster quadruplet decomposition:** every mass number `A` decomposes
    uniquely into `A / 4` closed `SU(4)` singlet quadruplets (`4 * (A / 4)`)
    plus a valence remainder `A % 4 < 4`, with exact quadruplet closure
    (`A % 4 = 0 ↔ 4 ∣ A`). -/
theorem alpha_cluster_quadruplet_decomposition (A : ℕ) :
    A = 4 * (A / 4) + A % 4 ∧ A % 4 < 4 ∧ (A % 4 = 0 ↔ 4 ∣ A) :=
  ⟨by omega, by omega, ⟨Nat.dvd_of_mod_eq_zero, Nat.mod_eq_zero_of_dvd⟩⟩

/-! ## §2 Conjectural Plancherel capacity and occupancy carrier -/

/-- **CONJECTURE (Wigner SU(4) closure).** The SU(4) = SU(2)_S × SU(2)_I spin-isospin
symmetry arises as the combined classical limit of the spin SO(3) fibre action (D10) and
the canonical isospin ℤ/2 swap (D9).

`E_0` is the gate scale; `W`, `E_gate`, `B_AME` and `c` are families indexed by mass
number `A`, all supplied by the **caller** — so the class is false for data that does not
satisfy the two laws (see `wignerSU4FromSpinIsospin_refutable`).

**No instance is provided.** Downstream results consume this as
`[WignerSU4FromSpinIsospin E_0 W E_gate B_AME c]` and are genuinely conditional on it.

-- Ref: [leitner2026] conj:wigner-su4-from-spin-isospin -/
class WignerSU4FromSpinIsospin
    (E_0 : ℝ) (W E_gate B_AME c : ℕ → ℝ) : Prop where
  /-- The dynamic cluster capacity is dictated by the Plancherel weight `W A` of the SU(4)
  spin-flavour conjugate partition `λ ⊢ 3A`: `E_gate = E₀ · ln(1 / W_λ)`. -/
  capacity_from_plancherel : ∀ A, E_gate A = E_0 * Real.log (1 / W A)
  /-- The empirical magic `A·8G` baseline is superseded by the dynamic occupancy
  requirement `c_λ = B_AME / E_gate`, which captures ~94 % of the binding at the ⁴He
  magic shell. -/
  occupancy_from_binding : ∀ A, c A = B_AME A / E_gate A
  -- Removed 2026-11-15: three `: True` marker fields (`su4_action`,
  -- `a_four_yields_singlet`, `alpha_cluster_from_su4_quadruplets`). They
  -- asserted nothing. The SU(4) action, Wigner's A = 4 singlet and the
  -- α-cluster recursion are recorded as open in bean `qou-n2un`.

/-- **The occupancy in terms of the Plancherel weight alone** — derived by composing the
two laws, rather than stated as a third field. This is what the block's pair of equations
amounts to, and it follows. -/
theorem wignerSU4_occupancy_via_plancherel
    (E_0 : ℝ) (W E_gate B_AME c : ℕ → ℝ)
    [h : WignerSU4FromSpinIsospin E_0 W E_gate B_AME c] (A : ℕ) :
    c A = B_AME A / (E_0 * Real.log (1 / W A)) := by
  rw [h.occupancy_from_binding A, h.capacity_from_plancherel A]

/-- The class is **refutable**, which neither the vacuous stub nor the uninhabitable
predecessor was: with `E₀ = 1` and `W ≡ 1` the capacity law forces `E_gate ≡ 0`, so the
constant-one `E_gate` falsifies it.

Stated as a theorem because "the carrier asserts something, and something that *can* be
satisfied" is exactly the property both earlier versions lacked — in opposite directions. -/
theorem wignerSU4FromSpinIsospin_refutable :
    ¬ WignerSU4FromSpinIsospin 1 (fun _ => 1) (fun _ => 1) (fun _ => 1) (fun _ => 1) := by
  intro hc
  have h := hc.capacity_from_plancherel 0
  norm_num at h

/-- **The class is inhabitable** — the complement of the theorem above, and the property
the predecessor provably lacked. Taking `W ≡ 1` forces `E_gate ≡ 0` by the capacity law,
and `c ≡ B_AME / 0 = 0` by `div_zero`, so this data satisfies both laws.

Recorded because "no instance is provided" must mean *the conjecture is open*, not *no
instance could exist*. Without this, the two statements are indistinguishable from
outside. -/
theorem wignerSU4FromSpinIsospin_satisfiable :
    WignerSU4FromSpinIsospin 1 (fun _ => 1) (fun _ => 0) (fun _ => 1) (fun _ => 0) where
  capacity_from_plancherel := by intro A; norm_num
  occupancy_from_binding := by intro A; norm_num

end QOU.BraidsAndKnots
