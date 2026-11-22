import QOU.Mass.GammaGammaWordSelection
import QOU.StandardModel.WritheChargeLeavesNoHypercharge

/-!
# The ruled nucleon word refutes the halved-writhe charge on the nucleons

The proton and the neutron are both read off the ruled nucleon word
`β_Bor = (σ₀σ₁⁻¹)³` (`QOU.Mass.GammaGammaWordSelection.borromean`); they differ in which
strands carry `u` and `d`, not in the braid. That word has writhe `0`
(`borromean_writhe`). The proton has charge `1` and the neutron charge `0` (comparison data;
they enter here only as the hypotheses `hp`, `hn`). So the electric charge is not a function of
the writhe of the nucleon word, and `Q = w/2` (`def:coulomb-charge`) cannot be the electric
charge on the nucleons.

The corpus also carries older nucleon writhe readings: `w(p) = +1`, `w(n) = −1` for the
inter-nucleon arc, `±2` for the corresponding Hopf-link pair framing
(`docs/audits/2026-06-02-u1-hypercharge-assignment.md`), and the intra-block `+3`, `+1` of
`mba-sidecar-mirror-cancellation`. None of them is the writhe of `β_Bor`.
-/

namespace QOU.StandardModel.NucleonWritheCharge

open QOU.Mass.GammaGammaWordSelection

/-- **No function of the nucleon-word writhe gives the nucleon charges.** For any state type
whose proton and neutron both carry the word `β_Bor`, and any charge with `Q p = 1`,
`Q n = 0`, the charge does not factor through the writhe of the word. -/
theorem charge_not_writhe_on_nucleons {S : Type*}
    (word : S → Word) (Q : S → ℚ) (p n : S)
    (hwp : word p = borromean) (hwn : word n = borromean)
    (hp : Q p = 1) (hn : Q n = 0) :
    ¬∃ f : ℤ → ℚ, ∀ X, Q X = f (writhe (word X)) :=
  WritheChargeHypercharge.charge_not_writhe_of_equal_writhe (fun X => writhe (word X)) Q p n
    (by simp only [hwp, hwn]) (by rw [hp, hn]; norm_num)

/-- In particular the halved writhe gives the proton charge `0`, not `1`. -/
theorem halved_writhe_proton_charge_zero : (writhe borromean : ℚ) / 2 = 0 := by
  rw [borromean_writhe]; norm_num

end QOU.StandardModel.NucleonWritheCharge
