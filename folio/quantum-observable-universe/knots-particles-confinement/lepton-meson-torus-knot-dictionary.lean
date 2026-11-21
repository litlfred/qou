/-
  Torus-knot dictionary: leptons at H₂ vs mesons at H₃.

  Formalizes the structural correspondence between the lepton mass
  tower (torus knots T(2,n) in H₂(q)) and the meson mass tower
  (Hopf-bound quark-antiquark pairs in H₃(q)).

  Reading (owner rulings 2026-11-20 and 2026-11-21): a quark is an
  unknot strand carrying one crossing letter, not a torus knot. The
  index n attached to a quark is the crossing count of its lepton
  partner T(2,n), a generation label. A meson's "crossing count" below
  is the sum of its two constituents' partner labels.

  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [kashaev1997] https://doi.org/10.1007/s100529801020
-/

import Mathlib.Tactic.FinCases
import Mathlib.Tactic

namespace QOU.ParticleInteractions

/-- Lepton generation index: odd primes 3, 5, 7 indexing the torus
  knot T(2, n) for electron, muon, tau respectively (backup reading). Under the
  owner ruling of 2026-11-21 the electron is the word σ₀σ₁σ₀ ∈ B₃ (closure: Hopf
  link), whose crossing count is still 3; the muon and tau entries are not
  re-derived under that ruling. -/
def leptonTorusKnotIndex : Fin 3 → ℕ
  | 0 => 3   -- electron: σ₀σ₁σ₀ (Hopf-link closure, owner ruling 2026-11-21); trefoil T(2,3) is the backup reading
  | 1 => 5   -- muon: cinquefoil T(2,5)
  | 2 => 7   -- tau: septafoil T(2,7)

/-- Meson crossing count: n₁ + n₂, where n₁, n₂ are the generation
  labels of the two constituents (each the crossing count of the
  quark's lepton partner T(2,n); the quarks are unknot strands). -/
def mesonCrossingCount : Fin 3 → ℕ
  | 0 => 6   -- pion: ū(3) + d(3) = 6
  | 1 => 8   -- kaon: ū(3) + s(5) = 8
  | 2 => 10  -- eta/phi: s̄(5) + s(5) = 10

/-- The lepton torus-knot index of row g equals that row's meson count
  minus the first-generation label 3 (an arithmetic offset; for the third
  row, φ = 5 + 5, it is not a constituent's label). -/
theorem lepton_meson_crossing_match (g : Fin 3) :
    leptonTorusKnotIndex g = mesonCrossingCount g - leptonTorusKnotIndex 0 := by
  fin_cases g <;> rfl

/-- Meson crossing count = sum of two lepton-partner indices. -/
theorem meson_crossing_is_sum :
    mesonCrossingCount 0 = leptonTorusKnotIndex 0 + leptonTorusKnotIndex 0 ∧
    mesonCrossingCount 1 = leptonTorusKnotIndex 0 + leptonTorusKnotIndex 1 ∧
    mesonCrossingCount 2 = leptonTorusKnotIndex 1 + leptonTorusKnotIndex 1 := by
  refine ⟨rfl, rfl, rfl⟩

end QOU.ParticleInteractions
