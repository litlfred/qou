/-
  Generation dictionary: leptons vs mesons.

  Formalizes the label arithmetic between the lepton generations
  (crossing counts n = 3, 5, 7) and the meson tower (Hopf-bound
  quark-antiquark pairs in H₃(q)). Under the owner ruling of 2026-11-21
  the electron is σ₀σ₁σ₀ ∈ B₃ (closure: the Hopf link, 3 crossings); the
  trefoil T(2,3) is the backup reading. The muon and tau labels 5 and 7
  are the crossing counts of T(2,5) and T(2,7); no three-strand word has
  been derived for them yet. The theorems below are integer arithmetic
  on these labels only.

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

/-- Lepton generation label: the crossing counts 3, 5, 7 of the
  electron (σ₀σ₁σ₀, Hopf-link closure), the muon and the tau. -/
def leptonTorusKnotIndex : Fin 3 → ℕ
  | 0 => 3   -- electron: σ₀σ₁σ₀ (3 crossings); backup trefoil T(2,3)
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
