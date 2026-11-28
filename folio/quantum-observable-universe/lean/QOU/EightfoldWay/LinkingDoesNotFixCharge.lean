import QOU.Observations.RingMassLinkingThreeStrand

/-!
# QOU.EightfoldWay.LinkingDoesNotFixCharge — the linking sign does not fix the hypercharge sign

The one remaining chirality sign is the sign of hypercharge relative to the matter part
(`ChiralitySignIsHyperchargeSign.lean`). A natural upstream candidate odd under a sign
flip is the linking number of a particle's braid closure, which
`RingMassLinkingThreeStrand.lean` ties to the energy grading (`U(1) = 3·lk`). This module
tests it and records a scope-limited negative.

* `lepton_linkSums` — the ruled lepton words (`e = σ₁σ₂σ₁`, `μ = σ₁²σ₂⁻¹`,
  `τ = σ₁⁴σ₂⁻¹`) have `linkSum = 2, 2, 4`, while all three carry charge `-1`.
* `proton_higgs_linkSum` — the proton `(σ₁σ₂⁻¹)³` and the neutral `4₁ = (σ₁σ₂⁻¹)²`
  both have `linkSum = 0`, with charges `+1` and `0`.
* `charge_not_function_of_linkSum` — so electric charge is not any function of the
  linking sum over these words.
* `mirror_negates_linkSum` — mirroring the electron negates its linking sum while its
  strand permutation is unchanged; the linking sign is the braid's handedness, a `P`-type
  datum, whereas the open sign is `C`-type (`Y ↦ -Y`).

Scope (a): the linking number, alone, does not fix the sign. It does not exclude a
closure that combines linking with the strand picture. Base ring `ℤ`.
-/

namespace QOU.EightfoldWay.LinkingDoesNotFixCharge

open QOU.Observations.RingMassLinkingThreeStrand

/-- The mirror of a letter. -/
def flip (l : Letter) : Letter := ⟨l.first, !l.pos⟩

def electron : List Letter := [s1, s2, s1]
def muon : List Letter := [s1, s1, s2i]
def tau : List Letter := [s1, s1, s1, s1, s2i]
def proton : List Letter := [s1, s2i, s1, s2i, s1, s2i]
def higgs41 : List Letter := [s1, s2i, s1, s2i]

theorem lepton_linkSums :
    linkSum electron = 2 ∧ linkSum muon = 2 ∧ linkSum tau = 4 := by decide

theorem proton_higgs_linkSum : linkSum proton = 0 ∧ linkSum higgs41 = 0 := by decide

/-- **Charge is not a function of the linking sum.** No `f` sends the linking sums of the
proton and of `4₁` to their charges `+1` and `0`. -/
theorem charge_not_function_of_linkSum :
    ¬ ∃ f : ℤ → ℤ, f (linkSum proton) = 1 ∧ f (linkSum higgs41) = 0 := by
  rintro ⟨f, hp, hh⟩
  rw [proton_higgs_linkSum.1] at hp
  rw [proton_higgs_linkSum.2, hp] at hh
  exact absurd hh (by decide)

/-- Mirroring negates the electron's linking sum and keeps its strand permutation. -/
theorem mirror_negates_linkSum :
    linkSum (electron.map flip) = -linkSum electron ∧
      perm (electron.map flip) = perm electron := by decide

end QOU.EightfoldWay.LinkingDoesNotFixCharge
