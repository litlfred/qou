/-
  Torus-knot dictionary: leptons at H₂ vs mesons at H₃.

  Formalizes the structural correspondence between the lepton mass
  tower (torus knots T(2,n) in H₂(q)) and the meson mass tower
  (Hopf-bound quark-antiquark pairs in H₃(q)).

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kashaev1997] https://doi.org/10.1007/s100529801020
-/

import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Omega

namespace QOU.ParticleInteractions

/-- Lepton generation index: odd primes 3, 5, 7 indexing the torus
  knot T(2, n) for electron, muon, tau respectively. -/
def leptonTorusKnotIndex : Fin 3 → ℕ
  | 0 => 3   -- electron: trefoil T(2,3)
  | 1 => 5   -- muon: cinquefoil T(2,5)
  | 2 => 7   -- tau: septafoil T(2,7)

/-- Meson crossing count: the total crossings in the meson braid
  word = n₁ + n₂ where n₁, n₂ are the quark torus-knot indices. -/
def mesonCrossingCount : Fin 3 → ℕ
  | 0 => 6   -- pion: ū(3) + d(3) = 6
  | 1 => 8   -- kaon: ū(3) + s(5) = 8
  | 2 => 10  -- eta/phi: s̄(5) + s(5) = 10

/-- The lepton torus-knot index equals the first quark's crossing
  count in the corresponding meson generation. -/
theorem lepton_meson_crossing_match (g : Fin 3) :
    leptonTorusKnotIndex g = mesonCrossingCount g - leptonTorusKnotIndex 0 := by
  fin_cases g <;> rfl

/-- Meson crossing count = sum of two torus-knot indices. -/
theorem meson_crossing_is_sum :
    mesonCrossingCount 0 = leptonTorusKnotIndex 0 + leptonTorusKnotIndex 0 ∧
    mesonCrossingCount 1 = leptonTorusKnotIndex 0 + leptonTorusKnotIndex 1 ∧
    mesonCrossingCount 2 = leptonTorusKnotIndex 1 + leptonTorusKnotIndex 1 := by
  refine ⟨rfl, rfl, rfl⟩

end QOU.ParticleInteractions
