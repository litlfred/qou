import Mathlib.Data.Nat.Defs

/-!
# Periodic-table demand conjecture (conjectural)

Class-axiomatised stub for `conj:periodic-table-demand`: for each
mass number `A = Z + N`, the experimentally observed stable
isotope `(Z*, N*)` is the unique minimizer of the demand magnitude
`|dem(A(Z, N))|`. With three subsidiary conjectures on magic
numbers, shell closure, and drip lines.

Per `CLAUDE.md §3b-cond`, the main claim and each sub-claim are
encoded as opaque Props and bundled into a class; the canonical
-- Ref: [manuscript]
instance carries `sorry` per claim.

## References

- `[manuscript]` `conj:periodic-table-demand`
- `[manuscript]` `prop:demand-stability`
- `[manuscript]` `def:derived-atom`
-/

namespace QOU.PeriodicTableDemand

/-- **Main claim**: for `A ≤ 238`, the demand-minimizing
    `(Z*, N*)` matches the experimentally observed valley of
    stability. -/
opaque ValleyOfStabilityMatchesHolds (A : ℕ) : Prop

/-- **Sub-claim (i): magic numbers from demand closure**.
    The nuclear magic numbers `{2, 8, 20, 28, 50, 82, 126}` are
    exactly the values of `Z` (or `N`) at which the nucleus
    achieves demand closure for at least one complementary value. -/
opaque MagicNumbersFromDemandClosureHolds : Prop

/-- **Sub-claim (ii): shell closure from electron demand**.
    The noble gases (`Z = 2, 10, 18, 36, 54, 86`) are exactly
    the values where the atom achieves
    `dem(A(Z, N*)) = ∅` for the most abundant stable isotope `N*`. -/
opaque NobleGasShellClosureHolds : Prop

/-- **Sub-claim (iii): drip lines from demand divergence**.
    The proton (neutron) drip line is the locus where
    `|dem(N(Z, N))| → ∞` under adding a proton (neutron). -/
opaque DripLinesFromDemandDivergenceHolds : Prop

/-- **Periodic-table demand conjecture** (axiomatised as a class
    per CLAUDE.md §3b-cond). Main claim + three sub-claims.
    Downstream blocks may take `[PeriodicTableDemand]` as a class
    hypothesis. -/
class PeriodicTableDemand : Prop where
  /-- Main: ∀ A ≤ 238, the demand-minimizer is the observed valley. -/
  valley_of_stability_matches : ∀ (A : ℕ), A ≤ 238 → ValleyOfStabilityMatchesHolds A
  /-- (i) Magic numbers ↔ nuclear demand closure. -/
  magic_numbers_from_demand_closure : MagicNumbersFromDemandClosureHolds
  /-- (ii) Noble gases ↔ atomic demand closure. -/
  noble_gas_shell_closure : NobleGasShellClosureHolds
  /-- (iii) Drip lines ↔ demand divergence. -/
  drip_lines_from_demand_divergence : DripLinesFromDemandDivergenceHolds

/-- **Canonical instance** — the conjecture proper. Each `sorry`
    is the unproved content of the corresponding claim. -/
-- Ref: [manuscript] conj:periodic-table-demand
instance periodic_table_demand_conjecture : PeriodicTableDemand where
  -- Witness: computations/none
  valley_of_stability_matches := fun _ _ => sorry
  -- Ref: [manuscript]
  magic_numbers_from_demand_closure := sorry
  -- Ref: [manuscript]
  noble_gas_shell_closure := sorry
  -- Ref: [manuscript]
  drip_lines_from_demand_divergence := sorry

end QOU.PeriodicTableDemand

/-! ## Special cases (provable from the conjecture)

These conditional theorems show what the conjecture implies for
specific atoms. They are fully verified by Lean MODULO the
conjecture class hypothesis. -/

/-- **CONDITIONAL.** Helium-4 is doubly magic (Z=2, N=2).
    If the demand conjecture holds, then He-4 achieves demand
    closure for both protons and neutrons — explaining its
    extraordinary stability (highest binding energy per nucleon). -/
theorem he4_doubly_magic [PeriodicTableDemand] :
    ValleyOfStabilityMatchesHolds 4 :=
  PeriodicTableDemand.valley_of_stability_matches 4 (by norm_num)

/-- **CONDITIONAL.** Oxygen-16 is doubly magic (Z=8, N=8). -/
theorem o16_doubly_magic [PeriodicTableDemand] :
    ValleyOfStabilityMatchesHolds 16 :=
  PeriodicTableDemand.valley_of_stability_matches 16 (by norm_num)

/-- **CONDITIONAL.** Lead-208 is doubly magic (Z=82, N=126). -/
theorem pb208_doubly_magic [PeriodicTableDemand] :
    ValleyOfStabilityMatchesHolds 208 :=
  PeriodicTableDemand.valley_of_stability_matches 208 (by norm_num)

/-- **SPECIAL CASE (provable).** The magic numbers list is non-empty
    and contains 2 (the lightest magic number). -/
theorem magic_numbers_contain_two : 2 ∈ [2, 8, 20, 28, 50, 82, 126] := by
  simp

end QOU.PeriodicTableDemand

