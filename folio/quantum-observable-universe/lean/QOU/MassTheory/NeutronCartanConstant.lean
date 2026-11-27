import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-!
# Which term of the categorical mass formula can carry the n–p split

A nucleon mass assembly has an isospin-blind amplitude `vol` (the volume term, a braid-class
function, the same for p and n because the γγ selection gives both the same element) and a
constant `const`, entering as `−const`. Each of the two terms is either *bare* (weight 1) or
*Cartan-weighted*: on the proton weight space it carries `s·q`, on the neutron weight space
`s·q⁻¹`. The ratio `q²` between the two weights is the quantum-trace ratio on the nucleon weight
spaces (`QOU.BraidsAndKnots.NucleonIsospinExclusions.restrictedTrace_ratio`); `s` is the
normalisation.

Results (generic field; the sign results over an ordered field):

* `split` : `m_n − m_p = −s(q − q⁻¹)·W`, where `W` is the net coefficient of the weighted terms.
* `neutron_heavier_iff` : for `q > 1`, `s > 0`, the neutron is heavier iff `W < 0`.
* `volume_weighted_neutron_lighter`, `const_weighted_neutron_heavier`: the two single-term cases.
* `split_proton_normalised`, `split_symmetric`: the closed forms `12(1 − q⁻²)·mₑ` and `12h·mₑ`
  when `const = 12·mₑ`.

No measured value enters. Whether the constant term carries a Cartan weight, and which `s`, is
not derived here (the constant itself is issue #8809).
-/

namespace QOU.MassTheory.NeutronCartanConstant

variable {R : Type*}

/-- The two nucleons. -/
inductive Nucleon
  | p
  | n

/-- A two-term mass assembly: `vol` (isospin-blind amplitude) and `const` (entering as `−const`),
each bare or Cartan-weighted. -/
structure Assembly (R : Type*) where
  vol : R
  const : R
  wVol : Bool
  wConst : Bool

section Field

variable [Field R]

/-- Cartan weight on the nucleon weight space: `s·q` on the proton, `s·q⁻¹` on the neutron. -/
def weight (s q : R) : Nucleon → R
  | .p => s * q
  | .n => s * q⁻¹

/-- The weight a term carries: the Cartan weight if weighted, else `1`. -/
def termWeight (w : Bool) (s q : R) (N : Nucleon) : R :=
  if w then weight s q N else 1

/-- The assembled mass. -/
def mass (a : Assembly R) (s q : R) (N : Nucleon) : R :=
  termWeight a.wVol s q N * a.vol - termWeight a.wConst s q N * a.const

/-- Net coefficient of the Cartan-weighted terms. -/
def weightedNet (a : Assembly R) : R :=
  (if a.wVol then a.vol else 0) - (if a.wConst then a.const else 0)

/-- **Split law.** Bare terms cancel; the weighted terms give `−s(q − q⁻¹)·W`. -/
theorem split (a : Assembly R) (s q : R) :
    mass a s q .n - mass a s q .p = -(s * (q - q⁻¹)) * weightedNet a := by
  rcases a with ⟨v, c, wv, wc⟩
  cases wv <;> cases wc <;> simp [mass, termWeight, weight, weightedNet] <;> ring

/-- With no weighted term the assembly is isospin-blind. -/
theorem bare_equal (v c s q : R) :
    mass ⟨v, c, false, false⟩ s q .n = mass ⟨v, c, false, false⟩ s q .p := by
  simp [mass, termWeight]

/-- Proton-normalised constant weight (`s = q⁻¹`, so the proton term stays `−const`):
`m_n − m_p = 12(1 − q⁻²)·mₑ` when `const = 12·mₑ`. -/
theorem split_proton_normalised (v me q : R) (hq : q ≠ 0) :
    mass ⟨v, 12 * me, false, true⟩ q⁻¹ q .n - mass ⟨v, 12 * me, false, true⟩ q⁻¹ q .p
      = 12 * (1 - q⁻¹ ^ 2) * me := by
  simp [mass, termWeight, weight]
  field_simp

/-- The proton-normalised reading leaves the proton term unchanged. -/
theorem proton_normalised_proton_unchanged (v me q : R) (hq : q ≠ 0) :
    mass ⟨v, 12 * me, false, true⟩ q⁻¹ q .p = v - 12 * me := by
  simp [mass, termWeight, weight, hq]

/-- Symmetric constant weight (`s = 1`, the plain `K^{⊗3}` eigenvalue):
`m_n − m_p = 12(q − q⁻¹)·mₑ` when `const = 12·mₑ`. -/
theorem split_symmetric (v me q : R) :
    mass ⟨v, 12 * me, false, true⟩ 1 q .n - mass ⟨v, 12 * me, false, true⟩ 1 q .p
      = 12 * (q - q⁻¹) * me := by
  simp [mass, termWeight, weight]
  ring

end Field

section Ordered

variable [Field R] [LinearOrder R] [IsStrictOrderedRing R]

theorem cartan_gap_pos {s q : R} (hs : 0 < s) (hq : 1 < q) : 0 < s * (q - q⁻¹) := by
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hinv : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  exact mul_pos hs (by linarith)

/-- **Sign criterion.** For `q > 1` and `s > 0`, the neutron is heavier exactly when the
Cartan-weighted part of the assembly is net negative. -/
theorem neutron_heavier_iff (a : Assembly R) {s q : R} (hs : 0 < s) (hq : 1 < q) :
    mass a s q .p < mass a s q .n ↔ weightedNet a < 0 := by
  have hk := cartan_gap_pos hs hq
  have hsplit := split a s q
  constructor
  · intro h
    by_contra hW
    push_neg at hW
    have : 0 ≤ s * (q - q⁻¹) * weightedNet a := mul_nonneg hk.le hW
    linarith
  · intro hW
    have : s * (q - q⁻¹) * weightedNet a < 0 := mul_neg_of_pos_of_neg hk hW
    linarith

/-- Weighting the (positive) volume term alone makes the neutron lighter. -/
theorem volume_weighted_neutron_lighter {v c s q : R} (hv : 0 < v) (hs : 0 < s) (hq : 1 < q) :
    mass ⟨v, c, true, false⟩ s q .n < mass ⟨v, c, true, false⟩ s q .p := by
  have hk := cartan_gap_pos hs hq
  have hsplit := split ⟨v, c, true, false⟩ s q
  have hW : weightedNet (⟨v, c, true, false⟩ : Assembly R) = v := by simp [weightedNet]
  rw [hW] at hsplit
  have : 0 < s * (q - q⁻¹) * v := mul_pos hk hv
  linarith

/-- Weighting the (positive) constant alone makes the neutron heavier. -/
theorem const_weighted_neutron_heavier {v c s q : R} (hc : 0 < c) (hs : 0 < s) (hq : 1 < q) :
    mass ⟨v, c, false, true⟩ s q .p < mass ⟨v, c, false, true⟩ s q .n :=
  (neutron_heavier_iff _ hs hq).2 (by simp [weightedNet]; exact hc)

/-- Both weighted: the neutron is heavier iff the constant exceeds the volume amplitude. -/
theorem both_weighted_neutron_heavier_iff {v c s q : R} (hs : 0 < s) (hq : 1 < q) :
    mass ⟨v, c, true, true⟩ s q .p < mass ⟨v, c, true, true⟩ s q .n ↔ v < c := by
  rw [neutron_heavier_iff _ hs hq]
  simp [weightedNet]

end Ordered

end QOU.MassTheory.NeutronCartanConstant
