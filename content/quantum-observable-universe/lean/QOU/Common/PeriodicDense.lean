import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Tactic

/-!
# A continuous function periodic on a dense set is periodic everywhere

The identity-theorem-free core of the `hibinv` input of
`QOU.QBeta.FaddeevRigidityReduction` (bean `qou-q95i`). The dual-shift
periodicity of the `Φ_b` ratio (`CyclicDilogPentagon.ratio_ibinv_periodic`) is
proved only **off** the discrete dual pole lattice (the `shift_binv` guard). To
promote it to the everywhere-periodicity the reduction consumes, one does **not**
need the full complex-analytic identity theorem: the dual pole lattice is
discrete, so its complement is **dense**, and a *continuous* function agreeing
with its shift on a dense set agrees everywhere. This isolates the remaining two
inputs cleanly: the ratio is continuous (from the entireness endowment,
`qou-2cvs`) and the dual-lattice complement is dense (a discreteness fact).

Verified `lean`-direct against pinned Mathlib (exit 0).
-/

open Complex

namespace QOU.Common

/-- A continuous `r : ℂ → ℂ` that is `c`-periodic on a **dense** set is
`c`-periodic everywhere: `r(·+c)` and `r` are continuous and agree on a dense
set, so they agree. -/
theorem periodic_of_continuous_of_eqOn_dense
    {r : ℂ → ℂ} {c : ℂ} {S : Set ℂ}
    (hcont : Continuous r) (hS : Dense S)
    (hper : ∀ z ∈ S, r (z + c) = r z) :
    ∀ z, r (z + c) = r z := by
  have hg : Continuous (fun z => r (z + c)) :=
    hcont.comp (continuous_id.add continuous_const)
  have hfun : (fun z => r (z + c)) = r :=
    Continuous.ext_on hS hg hcont (fun z hz => hper z hz)
  intro z
  exact congrFun hfun z

end QOU.Common
