import Mathlib.Analysis.SpecialFunctions.Log.Basic
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

Two claims from the block, indexed by mass number `A`:

* **Dynamic cluster capacity from the Plancherel weight** — `E_gate A = E₀ · log(1 / W A)`,
  where `W A` is the Plancherel weight of the SU(4) spin-flavour conjugate partition
  `λ ⊢ 3A`.
* **Dynamic occupancy** — `c A = B_AME A / E_gate A`, superseding the empirical magic
  `A·8G` baseline.

`E₀` and the families `W`, `E_gate`, `B_AME`, `c` are parameters, so an instance is a real
commitment about a particular set of data.

## What is NOT encoded

Three properties the block names have **no statable form against existing types**, and each
keeps its `opaque marker` field rather than being silently dropped: the SU(4) action on a
nucleon's 4-dimensional internal space, Wigner's supermultiplet theorem (`A = 4`
totally-antisymmetric ⇒ trivial rep), and the α-cluster recursion as products of SU(4)
singlet quadruplets. All three need SU(4) representation infrastructure the corpus does not
have.

Per `qou-tsnp`'s guard — *"if a conjecture's claim cannot yet be stated against existing
types … say so and note what type must grow first"* — **what must grow first is an SU(4)
representation type with a decomposition into SU(2)_S × SU(2)_I isotypic parts**, so that
the supermultiplet statement can be made at all.

## Base ring

`ℝ`, because `Real.log` appears in the capacity law. Nothing else archimedean is used.

-- Ref: [leitner2026] quantum-observable-universe/nuclear-interactions/wigner-su4-from-spin-isospin.ts
-/

namespace QOU.BraidsAndKnots

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
  /-- The SU(4) action on each nucleon's 4-dimensional internal space.

  `opaque marker` — needs SU(4) representation infrastructure the corpus does not have;
  carried as an explicitly-labelled marker rather than dropped. -/
  su4_action : True
  /-- Wigner's supermultiplet theorem: the `A = 4` totally-antisymmetric tensor product
  gives the trivial representation.

  `opaque marker` — requires the representation infrastructure above. -/
  a_four_yields_singlet : True
  /-- α-cluster recursion as products of SU(4)-singlet quadruplets.

  `opaque marker` — depends on the two markers above. -/
  alpha_cluster_from_su4_quadruplets : True

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
  su4_action := trivial
  a_four_yields_singlet := trivial
  alpha_cluster_from_su4_quadruplets := trivial

end QOU.BraidsAndKnots
