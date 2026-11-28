import QOU.BringsSurface.BringHarmonicTypes

/-!
# Triple selection rules for the harmonic types of Bring's surface

Bean `qou-u81q`. The typed spectral sunset (`QOU/Transcendental/BringsSurface/
BringSpectralSunset.lean`) needs to know which triples of harmonic types `(ρ_a, ρ_b, ρ_c)` admit an
`S₅`-invariant trilinear form: `N(a,b,c) = dim Hom_{S₅}(ρ_a ⊗ ρ_b ⊗ ρ_c, 1) =
⟨χ_a χ_b χ_c, 1⟩` (all `S₅` characters are real). This file computes that table. Finite and exact.

## Results

* `tripleMult_nonneg_le_two`: every `0 ≤ N(a,b,c) ≤ 2`.
* `forbidden_count`: `200` of the `343` ordered triples have `N = 0`; `143` are allowed.
* `holomorphic_cubic_forbidden`: `N([2,1,1,1], [2,1,1,1], [2,1,1,1]) = 0`, so no invariant cubic in
  three harmonics of the holomorphic type.
* `holomorphic_pair_row`: `[2,1,1,1] ⊗ [2,1,1,1]` contains `triv, [4,1], [3,2], [3,1,1]` once each.
* `tripleMult_symm`: `N` is symmetric.

With reflection parity (`BringReflectionParity.lean`) a triple is allowed for `S₅ × C₂` iff
`N ≠ 0` and the number of odd factors is even: `143 × 4 = 572` of `14³ = 2744`.
-/

namespace QOU.Brings.TripleSelection

open QOU.Brings.S5Char QOU.Brings.HarmonicTypes

set_option maxRecDepth 100000

/-- `120 · N(a,b,c)`. -/
def tripleSum (a b c : Fin 7) : ℤ := inner (fun i => irr a i * irr b i) (irr c)

/-- `N(a,b,c) = dim Hom_{S₅}(ρ_a ⊗ ρ_b ⊗ ρ_c, 1)`. -/
def tripleMult (a b c : Fin 7) : ℤ := tripleSum a b c / 120

theorem tripleSum_divisible : ∀ a b c : Fin 7, 120 ∣ tripleSum a b c := by decide

theorem tripleMult_nonneg_le_two : ∀ a b c : Fin 7, 0 ≤ tripleMult a b c ∧ tripleMult a b c ≤ 2 := by
  decide

theorem tripleMult_symm :
    ∀ a b c : Fin 7, tripleMult a b c = tripleMult b a c ∧ tripleMult a b c = tripleMult a c b := by
  decide

/-- All ordered triples of types. -/
def triples : List (Fin 7 × Fin 7 × Fin 7) :=
  (List.finRange 7).flatMap fun a => (List.finRange 7).flatMap fun b =>
    (List.finRange 7).map fun c => (a, b, c)

theorem forbidden_count :
    (triples.filter (fun t => tripleMult t.1 t.2.1 t.2.2 = 0)).length = 200 ∧ triples.length = 343 := by
  decide

theorem holomorphic_cubic_forbidden : tripleMult 3 3 3 = 0 := by decide

theorem holomorphic_pair_row : (List.finRange 7).map (tripleMult 3 3) = [1, 0, 1, 0, 1, 0, 1] := by
  decide

/-- A pairing `N(a, b, triv) = δ_ab`: only equal types pair. -/
theorem pairing_diagonal : ∀ a b : Fin 7, tripleMult a b 0 = if a = b then 1 else 0 := by decide

/-- With parities: allowed iff `N ≠ 0` and an even number of odd factors. -/
def allowedParity (a b c : Fin 7) (pa pb pc : Bool) : Bool :=
  decide (tripleMult a b c ≠ 0) && (Bool.xor pa (Bool.xor pb pc) == false)

theorem allowed_parity_count :
    ((triples.flatMap fun t => [false, true].flatMap fun pa => [false, true].flatMap fun pb =>
      [false, true].map fun pc => allowedParity t.1 t.2.1 t.2.2 pa pb pc).filter id).length = 572 := by
  decide

end QOU.Brings.TripleSelection
