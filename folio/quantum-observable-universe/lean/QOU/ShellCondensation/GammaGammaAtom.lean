import QOU.Photon

/-!
# QOU.ShellCondensation.GammaGammaAtom

Formalize-first definitions for the γγ shell study (bean `qou-mgg1`,
`docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md`).

In any ring `A` with a family of units `σ : ℕ → Aˣ` (the braid generators;
no Hecke relation is assumed), strand `0` is the nucleus and strand `k ≥ 1`
is electron `k`. We define the three processes and the atom recursion:

* capture `K k = (A₀ₖ)⁻¹`, where `A₀ₖ = σ_{k−1}⋯σ₁ σ₀² σ₁⁻¹⋯σ_{k−1}⁻¹`;
* electron–electron interaction `I k = σ_{k−1}`;
* photon emission `E k = γ_{k−2}(φ)` (`def:photon`, fourth term `σᵢσᵢ₊₁⁻¹`);
* `W 1 = K 1`, `W (k+1) = W k · K (k+1) · I (k+1) · E (k+1)`.

Proved: the pure-braid generator and the capture operator are units, and are
inverse to each other; with the bare photon (`φ = 0`) every atom word is a
unit, i.e. a genuine braid. These are the statements the probe relies on
when it reads `W` at `φ = 0` as a braid closure.

-- Ref: [leitner2026] docs/audits/2026-11-21-magic-shells-gamma-gamma-model.md
-/

namespace QOU.ShellCondensation.GammaGammaAtom

open QOU.Photon

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- `σ_{k−1} ⋯ σ_1` as a unit (the empty product for `k ≤ 1`). -/
def ladder (σ : ℕ → Aˣ) : ℕ → Aˣ
  | 0 => 1
  | 1 => 1
  | (k + 2) => σ (k + 1) * ladder σ (k + 1)

/-- The pure braid `A₀ₖ = σ_{k−1}⋯σ₁ σ₀² σ₁⁻¹⋯σ_{k−1}⁻¹` in which strand `k`
    encircles strand `0` (for `k ≥ 1`). -/
def pureGen (σ : ℕ → Aˣ) (k : ℕ) : Aˣ :=
  ladder σ k * (σ 0 * σ 0) * (ladder σ k)⁻¹

/-- Capture of electron `k`: the inverse pure braid (negative nucleus–electron
    orientation). -/
def capture (σ : ℕ → Aˣ) (k : ℕ) : Aˣ := (pureGen σ k)⁻¹

/-- Electron–electron interaction between electrons `k−1` and `k`. -/
def interaction (σ : ℕ → Aˣ) (k : ℕ) : Aˣ := σ (k - 1)

/-- The photon emitted when electron `k` is captured, on strands `k−2, k−1, k`. -/
def emission (σ : ℕ → Aˣ) (c : Colour R) (k : ℕ) : A :=
  photon (σ (k - 2) : A) (σ (k - 1)) c

/-- The binding operator that adds electron `k` (`k ≥ 2`). -/
def bindOp (σ : ℕ → Aˣ) (c : Colour R) (k : ℕ) : A :=
  (capture σ k : A) * (interaction σ k : A) * emission σ c k

/-- The atom word with `k` electrons (`W 0 = 1`, `W 1 = K 1`). -/
def atom (σ : ℕ → Aˣ) (c : Colour R) : ℕ → A
  | 0 => 1
  | 1 => (capture σ 1 : A)
  | (k + 2) => atom σ c (k + 1) * bindOp σ c (k + 2)

/-- The capture operator undoes the pure-braid generator. -/
theorem capture_mul_pureGen (σ : ℕ → Aˣ) (k : ℕ) :
    (capture σ k : A) * (pureGen σ k : A) = 1 := by
  simp [capture]

/-- With the bare photon the emission factor is `1`. -/
theorem emission_bare (σ : ℕ → Aˣ) (k : ℕ) :
    emission σ (bare : Colour R) k = (1 : A) := by
  simp [emission, photon_bare]

/-- With the bare photon every atom word is a unit: it is a genuine braid,
    the product of capture and interaction braids. -/
theorem atom_bare_isUnit (σ : ℕ → Aˣ) : ∀ k, IsUnit (atom σ (bare : Colour R) k)
  | 0 => isUnit_one
  | 1 => (capture σ 1).isUnit
  | (k + 2) => by
      have ih := atom_bare_isUnit σ (k + 1)
      simp only [atom, bindOp, emission_bare, mul_one, ← mul_assoc]
      exact (ih.mul (capture σ (k + 2)).isUnit).mul (interaction σ (k + 2)).isUnit

/-! ### All-pairs interaction (owner card, 2026-11-21)

Electron `k` links every earlier electron `j` (`1 ≤ j < k`) by the pure braid
`A_{jk} = σ_{k−1}⋯σ_{j+1} σ_j² σ_{j+1}⁻¹⋯σ_{k−1}⁻¹` (positive orientation, like
charges), in place of the single neighbour crossing. -/

/-- `σ_{k−1} ⋯ σ_{j+1}` as a unit (empty when `k ≤ j + 1`). -/
def ladderFrom (σ : ℕ → Aˣ) (j : ℕ) : ℕ → Aˣ
  | 0 => 1
  | (k + 1) => if j + 1 ≤ k then σ k * ladderFrom σ j k else 1

/-- The pure braid `A_{jk}`: strand `k` encircles strand `j`. -/
def pairGen (σ : ℕ → Aˣ) (j k : ℕ) : Aˣ :=
  ladderFrom σ j k * (σ j * σ j) * (ladderFrom σ j k)⁻¹

/-- `A_{1k} A_{2k} ⋯ A_{mk}`. -/
def pairsUpTo (σ : ℕ → Aˣ) (k : ℕ) : ℕ → Aˣ
  | 0 => 1
  | (m + 1) => pairsUpTo σ k m * pairGen σ (m + 1) k

/-- `∏_{j=1}^{k−1} A_{jk}`, taken in increasing `j`. -/
def allPairs (σ : ℕ → Aˣ) (k : ℕ) : Aˣ := pairsUpTo σ k (k - 1)

/-- The all-pairs binding operator that adds electron `k`. -/
def bindOpAll (σ : ℕ → Aˣ) (c : Colour R) (k : ℕ) : A :=
  (capture σ k : A) * (allPairs σ k : A) * emission σ c k

/-- The all-pairs atom word. -/
def atomAll (σ : ℕ → Aˣ) (c : Colour R) : ℕ → A
  | 0 => 1
  | 1 => (capture σ 1 : A)
  | (k + 2) => atomAll σ c (k + 1) * bindOpAll σ c (k + 2)

/-- With the bare photon every all-pairs atom word is a unit (a pure braid). -/
theorem atomAll_bare_isUnit (σ : ℕ → Aˣ) : ∀ k, IsUnit (atomAll σ (bare : Colour R) k)
  | 0 => isUnit_one
  | 1 => (capture σ 1).isUnit
  | (k + 2) => by
      have ih := atomAll_bare_isUnit σ (k + 1)
      simp only [atomAll, bindOpAll, emission_bare, mul_one, ← mul_assoc]
      exact (ih.mul (capture σ (k + 2)).isUnit).mul (allPairs σ (k + 2)).isUnit

end QOU.ShellCondensation.GammaGammaAtom


