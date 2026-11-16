/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

/-!
# QOU.AppendixQValues.ProtonBorromeanAssembly

§3b-cond conjecture class for the proton's Borromean mass assembly, and the
proton-mass substrate identity *derived* from it.

The proposition `prop:proton-mass-substrate-identity` states
  `m_p = 2 · m_μ · F_Bor(q₀) − 12 · m_e`
(0.24 ppm vs CODATA, 50-dps MPFR verified). The numerics are compute-verified;
the OPEN categorical content (block "Open work §1") is *why* the structural
integers enter linearly:

* the constituent multiplicity is `dim V_(2,1) = 2` (the trace-dominant Hecke
  irrep dimension), and
* the per-constituent electron-binding count is `|S₃| = 6` (the order `3! = 6`
  of the 3-strand symmetric group `S₃`, i.e. `dim H₃(1) = 6`; `12 = 2 · 6`;
  note per bean `qou-n04i` that the older "Ocneanu −1/12 leading-pole inverse"
  attribution is retired because `tr_M(β_Bor)` has leading pole `q⁻⁴` with
  coefficient `1`, not `q⁻¹⁰ · (−1/12)`),

assembled as `m_p = multiplicity · (m_μ · F_Bor − bindingCount · m_e)`.

We axiomatise these as a §3b-cond `class` (the conjectural *inputs*) and DERIVE
the published flat identity `2·m_μ·F_Bor − 12·m_e` from them — the concrete
`12` emerging as `multiplicity · bindingCount = 2 · 6`. This is the honest
formalisation of the stated gap: the class carries the assembly hypotheses, the
theorem composes them into the observed linear factor. Generic `[CommRing R]`
(§7c, no archimedean structure); sorry-free modulo the class instance.

-- @conjecture: primary
-- Ref: [leitner2026] quantum-observable-universe/appendix-qvalues/proton-borromean-assembly.md
-/

namespace QOU.AppendixQValues

/-- **Conjecture: the proton's Borromean mass assembly**
(`conj:proton-borromean-assembly`).

The fields are the conjectural categorical *hypotheses* (the two
structural-integer identifications and the assembly law in factored form); the
substrate identity is *derived* from them (`proton_mass_substrate_identity`),
so this is a genuine §3b-cond conditional input, not a self-assuming
projection of the conclusion. -/
class ProtonBorromeanAssembly (R : Type*) [CommRing R] where
  /-- muon mass (CAL-2 derived), electron mass (CAL-1), Borromean observable
      value `F_Bor(q₀)`, and the proton mass. -/
  mMu : R
  mE : R
  fBor : R
  protonMass : R
  /-- Conjectural input 1 — the constituent multiplicity is `dim V_(2,1) = 2`
      (the trace-dominant Hecke irrep dimension). -/
  multiplicity : R
  multiplicity_eq_two : multiplicity = 2
  /-- Conjectural input 2 — the per-constituent electron-binding count is
      `|S₃| = 6` (the order `3! = 6` of the 3-strand symmetric group `S₃`,
      `dim H₃(1) = 6`; per `qou-n04i`, the former Ocneanu `−1/12` attribution
      is retired). -/
  bindingCount : R
  bindingCount_eq_six : bindingCount = 6
  /-- Conjectural assembly law — the proton mass is the multiplicity times the
      per-constituent (muon-dressed minus electron-bound) mass. -/
  assembly : protonMass = multiplicity * (mMu * fBor - bindingCount * mE)

/-- **Proton-mass substrate identity (conditional on `ProtonBorromeanAssembly`).**

Given the conjectural Borromean assembly, the proton mass equals the published
flat form `2·m_μ·F_Bor − 12·m_e`; the concrete integers are DERIVED
(`2 = multiplicity`, `12 = multiplicity · bindingCount = 2 · 6`), not assumed.
Sorry-free modulo the single class instance. -/
-- Ref: [leitner2026] quantum-observable-universe/appendix-qvalues/proton-mass-substrate-identity.md
theorem proton_mass_substrate_identity (R : Type*) [CommRing R]
    [A : ProtonBorromeanAssembly R] :
    A.protonMass = 2 * A.mMu * A.fBor - 12 * A.mE := by
  rw [A.assembly, A.multiplicity_eq_two, A.bindingCount_eq_six]; ring

/-! ## §2  Relational mass factorization (`qou-mrel`, `qou-n04i`) and
    `δ`-split role decoupling (`qou-nbx7`)

    1. **Relational `m_e` factorization (`qou-mrel`):**
       When `m_μ = m_e · μ_ratio` (where `μ_ratio = Vol(4₁) / ℏ_q²` is the
       dimensionless muon-to-electron topological ratio), the electron scale
       `m_e` factors out of `proton_mass_substrate_identity` completely:
       $$m_p = m_e \cdot 2 \cdot (\mu_{\text{ratio}} \cdot F_{\text{Bor}} - 6).$$
       Thus the predicted quantity is the dimensionless ratio
       `protonOverMeDimensionless μ_ratio fBor = 2 * (μ_ratio * fBor - 6)`,
       and `-12 · m_e = -2 · |S₃| · m_e` is the subtraction of `|S₃| = 6`
       electron-calibrated unknotted baseline channels per `(2,1)` Hook
       component.

    2. **`δ`-split decoupling between the mass observable and the trace-path
       crossing tilt (`qou-nbx7`):**
       Separates Role (a) `deltaMassObservable lead hbarCube kSub := lead * (1 + kSub * hbarCube)`
       (the physical $n$–$p$ mass splitting ratio $\Delta m_{np}/M_N$ with
       subleading $\hbar_q^3$ coefficient $k_{\text{sub}}$) from Role (b)
       `pnCrossingTemplateFour h deltaTilt := -h * (2 - deltaTilt)` (the
       cleared-denominator trace-path crossing template $4 d = -h(2 - \delta_{\text{tilt}})$),
       and proves the exact linear decoupling law
       $$4\bigl(d(h, \delta(k_1)) - d(h, \delta(k_2))\bigr) = h \cdot \delta_{\text{lead}} \cdot \hbar_q^3 \cdot (k_1 - k_2).$$ -/

/-- Dimensionless proton-to-electron mass ratio `m_p / m_e = 2 · (μ_ratio · F_Bor − 6)`
    (`qou-mrel`, `qou-n04i`). -/
def protonOverMeDimensionless {R : Type*} [CommRing R] (muOverMeRatio fBor : R) : R :=
  2 * (muOverMeRatio * fBor - 6)

/-- **`m_e` factors out of the proton mass assembly (`qou-mrel`).**
    If `mMu = mE * muOverMeRatio`, then `protonMass = mE * protonOverMeDimensionless muOverMeRatio fBor`. -/
theorem proton_mass_factors_mE (R : Type*) [CommRing R]
    [A : ProtonBorromeanAssembly R] (muOverMeRatio : R)
    (hMu : A.mMu = A.mE * muOverMeRatio) :
    A.protonMass = A.mE * protonOverMeDimensionless muOverMeRatio A.fBor := by
  rw [proton_mass_substrate_identity R, hMu]
  unfold protonOverMeDimensionless
  ring

/-- **Degree-1 homogeneity in the calibration anchor `m_e` (`qou-mrel`).**
    Rescaling both `m_e ↦ λ · m_e` and `m_μ ↦ λ · m_μ` rescales the assembled
    proton mass `2 · m_μ · F_Bor − 12 · m_e` by `λ`. -/
theorem proton_mass_homogeneous_in_scale {R : Type*} [CommRing R]
    (lam mMu mE fBor : R) :
    2 * (lam * mMu) * fBor - 12 * (lam * mE)
      = lam * (2 * mMu * fBor - 12 * mE) := by
  ring

/-- Role (a) of `δ` (`qou-nbx7`): the physical $n$–$p$ mass-splitting observable
    $\delta_{\text{mass}}(k_{\text{sub}}) = \delta_{\text{lead}} \cdot (1 + k_{\text{sub}} \cdot \hbar_q^3)$. -/
def deltaMassObservable {R : Type*} [CommRing R] (deltaLead hbarCube kSub : R) : R :=
  deltaLead * (1 + kSub * hbarCube)

/-- Role (b) of `δ` (`qou-nbx7`): cleared-denominator trace-path $p$–$n$ crossing
    template $4 d(h, \delta_{\text{tilt}}) = -h \cdot (2 - \delta_{\text{tilt}})$. -/
def pnCrossingTemplateFour {R : Type*} [CommRing R] (h deltaTilt : R) : R :=
  -h * (2 - deltaTilt)

/-- **Linear sensitivity of the trace-path crossing template (`qou-nbx7`).**
    For any two tilt inputs $\delta_1, \delta_2$,
    $4 d(h, \delta_1) - 4 d(h, \delta_2) = h \cdot (\delta_1 - \delta_2)$. -/
theorem pnCrossingTemplateFour_diff {R : Type*} [CommRing R] (h d1 d2 : R) :
    pnCrossingTemplateFour h d1 - pnCrossingTemplateFour h d2 = h * (d1 - d2) := by
  unfold pnCrossingTemplateFour
  ring

/-- **Decoupling of the subleading coefficient $k_{\text{sub}}$ from the trace
    template (`qou-nbx7`).**
    Changing the subleading coefficient from $k_1$ to $k_2$ shifts
    $4 d(h, \delta(k))$ by $h \cdot \delta_{\text{lead}} \cdot \hbar_q^3 \cdot (k_1 - k_2)$
    (order $O(h \cdot \delta_{\text{lead}} \cdot \hbar_q^3) \sim 7 \times 10^{-8}$ at $q_0$). -/
theorem pnCrossingTemplateFour_subleading_shift {R : Type*} [CommRing R]
    (h deltaLead hbarCube k1 k2 : R) :
    pnCrossingTemplateFour h (deltaMassObservable deltaLead hbarCube k1)
      - pnCrossingTemplateFour h (deltaMassObservable deltaLead hbarCube k2)
      = h * deltaLead * hbarCube * (k1 - k2) := by
  unfold pnCrossingTemplateFour deltaMassObservable
  ring

end QOU.AppendixQValues
