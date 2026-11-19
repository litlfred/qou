import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum

/-!
# Periodic-table demand conjecture (`rem:periodic-table-demand`, §3b-cond)

Class-axiomatised formulation of the periodic-table demand conjecture and its
subsidiary shell-closure statements over `ℚ`-valued demand magnitudes (§7c,
no `ℝ` specialisation), with zero `opaque` declarations and zero global dummy
instances.

## Unconditional vs conditional content

1. **Unconditional (`magic_numbers_contain_two`, `zero_demand_is_isobar_minimizer`):**
   structural membership properties of the nuclear magic list
   `[2, 8, 20, 28, 50, 82, 126]` and the fact that any non-negative demand
   profile achieving exact demand closure (`dem Z N = 0`, such as `³He`)
   automatically minimises demand along its entire `Z + N = A` isobar.
2. **Conditional (`he4_doubly_magic`, `o16_doubly_magic`, `pb208_doubly_magic`):**
   under `[PeriodicTableDemand]`, `A = 4` (`⁴He`), `A = 16` (`¹⁶O`), and
   `A = 208` (`²⁰⁸Pb`) satisfy both isobaric demand minimisation along the
   observed valley of stability and nuclear demand-closure witnesses for their
   magic proton and neutron counts.

## References

- [leitner2026] `rem:periodic-table-demand`
- [leitner2026] `prop:demand-stability`
- [leitner2026] `def:derived-atom`
-/

namespace QOU.Nuclear

/-- Observed nuclear magic numbers `{2, 8, 20, 28, 50, 82, 126}`. -/
def nuclearMagicNumbers : List ℕ := [2, 8, 20, 28, 50, 82, 126]

/-- Observed atomic noble-gas proton numbers `{2, 10, 18, 36, 54, 86}`. -/
def nobleGasAtomicNumbers : List ℕ := [2, 10, 18, 36, 54, 86]

/-- `(Z, N)` minimises a `ℚ`-valued demand profile along its `Z' + N' = Z + N` isobar. -/
def IsIsobarDemandMinimizer (dem : ℕ → ℕ → ℚ) (Z N : ℕ) : Prop :=
  ∀ Z' N' : ℕ, Z' + N' = Z + N → dem Z N ≤ dem Z' N'

/-- **Unconditional.** The nuclear magic-number list contains `2`. -/
theorem magic_numbers_contain_two : 2 ∈ nuclearMagicNumbers := by decide

/-- **Unconditional.** Any pair `(Z, N)` with exact demand closure `dem Z N = 0`
    under a non-negative demand profile `0 ≤ dem Z' N'` is automatically an
    isobaric demand minimiser (illustrating exact closure at `³He`). -/
theorem zero_demand_is_isobar_minimizer
    (dem : ℕ → ℕ → ℚ)
    (hnonneg : ∀ Z' N' : ℕ, 0 ≤ dem Z' N')
    (Z N : ℕ) (hzero : dem Z N = 0) :
    IsIsobarDemandMinimizer dem Z N := by
  intro Z' N' _
  rw [hzero]
  exact hnonneg Z' N'

/-- **Periodic-table demand conjecture (§3b-cond).**
    Packages the atomic demand profile `demMag`, bare-nuclear demand profile
    `nuclearDemMag`, observed valley representative `observedValley A = (Z*, N*)`,
    isobaric minimisation for `1 ≤ A ≤ 238`, and the magic-number / noble-gas
    demand-closure characterisations. No global instance is registered. -/
class PeriodicTableDemand where
  /-- Atomic demand magnitude `|dem(𝓐(Z, N))|` valued in `ℚ`. -/
  demMag : ℕ → ℕ → ℚ
  demMag_nonneg : ∀ Z N : ℕ, 0 ≤ demMag Z N
  /-- Bare-nuclear demand magnitude `|dem(𝓝(Z, N))|` valued in `ℚ`. -/
  nuclearDemMag : ℕ → ℕ → ℚ
  nuclearDemMag_nonneg : ∀ Z N : ℕ, 0 ≤ nuclearDemMag Z N
  /-- Experimentally observed valley-of-stability representative `(Z*, N*)` at mass `A`. -/
  observedValley : ℕ → ℕ × ℕ
  observedValley_mass :
    ∀ A : ℕ, 1 ≤ A → A ≤ 238 → (observedValley A).1 + (observedValley A).2 = A
  /-- Main claim: for `1 ≤ A ≤ 238`, `observedValley A` minimises `demMag` on `Z + N = A`. -/
  valley_minimizes_demand :
    ∀ A : ℕ, 1 ≤ A → A ≤ 238 →
      IsIsobarDemandMinimizer demMag (observedValley A).1 (observedValley A).2
  /-- Subsidiary (i): nuclear magic numbers are iff nuclear demand vanishes for some partner. -/
  magic_iff_nuclear_closure :
    ∀ M : ℕ, M ∈ nuclearMagicNumbers ↔
      (∃ K : ℕ, nuclearDemMag M K = 0 ∨ nuclearDemMag K M = 0)
  /-- Subsidiary (ii): noble-gas `Z` iff atomic demand vanishes on the valley of stability. -/
  noble_iff_atomic_closure :
    ∀ Z : ℕ, Z ∈ nobleGasAtomicNumbers ↔
      (∃ A : ℕ, 1 ≤ A ∧ A ≤ 238 ∧ (observedValley A).1 = Z ∧
        demMag Z (observedValley A).2 = 0)

/-- **Conditional (`⁴He`, `A = 4`, `Z = N = 2`).** Under `[PeriodicTableDemand]`,
    `A = 4` satisfies isobaric demand minimisation on the valley of stability and
    `2` admits a nuclear demand-closure witness. -/
-- Ref: [leitner2026] rem:periodic-table-demand
theorem he4_doubly_magic [h : PeriodicTableDemand] :
    (h.observedValley 4).1 + (h.observedValley 4).2 = 4 ∧
    IsIsobarDemandMinimizer h.demMag (h.observedValley 4).1 (h.observedValley 4).2 ∧
    (∃ K : ℕ, h.nuclearDemMag 2 K = 0 ∨ h.nuclearDemMag K 2 = 0) :=
  ⟨h.observedValley_mass 4 (by omega) (by omega),
   h.valley_minimizes_demand 4 (by omega) (by omega),
   (h.magic_iff_nuclear_closure 2).mp (by decide)⟩

/-- **Conditional (`¹⁶O`, `A = 16`, `Z = N = 8`).** Under `[PeriodicTableDemand]`,
    `A = 16` satisfies isobaric demand minimisation and `8` admits a nuclear
    demand-closure witness. -/
-- Ref: [leitner2026] rem:periodic-table-demand
theorem o16_doubly_magic [h : PeriodicTableDemand] :
    (h.observedValley 16).1 + (h.observedValley 16).2 = 16 ∧
    IsIsobarDemandMinimizer h.demMag (h.observedValley 16).1 (h.observedValley 16).2 ∧
    (∃ K : ℕ, h.nuclearDemMag 8 K = 0 ∨ h.nuclearDemMag K 8 = 0) :=
  ⟨h.observedValley_mass 16 (by omega) (by omega),
   h.valley_minimizes_demand 16 (by omega) (by omega),
   (h.magic_iff_nuclear_closure 8).mp (by decide)⟩

/-- **Conditional (`²⁰⁸Pb`, `A = 208`, `Z = 82`, `N = 126`).** Under
    `[PeriodicTableDemand]`, `A = 208` satisfies isobaric demand minimisation
    and both `82` and `126` admit nuclear demand-closure witnesses. -/
-- Ref: [leitner2026] rem:periodic-table-demand
theorem pb208_doubly_magic [h : PeriodicTableDemand] :
    (h.observedValley 208).1 + (h.observedValley 208).2 = 208 ∧
    IsIsobarDemandMinimizer h.demMag (h.observedValley 208).1 (h.observedValley 208).2 ∧
    (∃ K : ℕ, h.nuclearDemMag 82 K = 0 ∨ h.nuclearDemMag K 82 = 0) ∧
    (∃ K : ℕ, h.nuclearDemMag 126 K = 0 ∨ h.nuclearDemMag K 126 = 0) :=
  ⟨h.observedValley_mass 208 (by omega) (by omega),
   h.valley_minimizes_demand 208 (by omega) (by omega),
   (h.magic_iff_nuclear_closure 82).mp (by decide),
   (h.magic_iff_nuclear_closure 126).mp (by decide)⟩

end QOU.Nuclear
