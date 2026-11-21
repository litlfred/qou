import QOU.ArchimedeanMassFormula
import QOU.MassDerivation
import QOU.KnotRegistry
import QOU.Calculations
import QOU.HadronicMass
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.CODATAChain — End-to-End: QOU Theory → CODATA Observables

This module constructs the complete proved chain from the QOU categorical
framework to agreement with NIST CODATA 2022 experimental values.

## Dependency structure

```
ArchimedeanMassFormula          (conj: two evaluation hypotheses)
  ├─ extends TopologicalMassDecomposition   (proved: Torsion.lean)
  │
  ▼  mass_eq_vol_div_h_q_sq    (proved: algebra)
  │
TopologicalMassFormula          (constructed from ArchimedeanMassFormula)
  │
  ▼  + KnotRegistry ansatz      (data: muon = figure-eight knot 4₁)
  │
MassDerivation constants        (CODATA input: m_μ/m_e, Vol(4₁))
  │
  ▼  derive_substrate_q         (proved: interval arithmetic)
  │
substrate_q ≈ 1.1097            (proved: |q - 1.1097| < 0.001)
  │
  ×  (the former CODATA-pinned nucleon rows held by construction and were
     removed; see QOU.MassTheory.PairSkeinNucleon for what the pair Skein
     formula determines)
```

## What is assumed vs proved

| Layer | Status | Justification |
|-------|--------|---------------|
| TopologicalMassDecomposition | **Proved** | Structure fields + decomposition identity |
| ArchimedeanMassFormula.baseline_eq_volume | **Hypothesis** | Chern–Simons/Volume correspondence |
| ArchimedeanMassFormula.exceptional_sum_eq | **Hypothesis** | Dilogarithm evaluation |
| mass = Vol(K)/ℏ_q² | **Proved** | From hypotheses by field_simp; ring |
| Knot–particle identification | **Ansatz** (data) | KnotRegistry declares muon = 4₁ |
| q ≈ 1.1097 from mass ratio | **Proved** | Interval arithmetic on √(Vol/ratio) |
| CODATA-pinned table | **By construction** | values are defined from the CODATA constants they are compared with; not a prediction |

## References

- [codata2022] https://physics.nist.gov/cuu/Constants/
- [turaev2010] https://doi.org/10.1515/9783110221831
-/


open QOU.Torsion QOU.MassDerivation QOU.KnotRegistry
open QOU.Calculations QOU.HadronicMass

namespace QOU.CODATAChain

/-! ## §1 From ArchimedeanMassFormula to TopologicalMassFormula

Given an `ArchimedeanMassFormula` instance (which bundles the two
evaluation hypotheses on top of the proved decomposition), we construct
a `TopologicalMassFormula` — the interface consumed by the numerical
calculation chain. -/

/-- Construct a `TopologicalMassFormula` from any `ArchimedeanMassFormula`.

    This is the key bridge: the categorical decomposition theorem
    (with its two evaluation hypotheses) produces the closed-form
    formula that the numerical chain requires. -/
noncomputable def toTopologicalMassFormula {M : Type*}
    (amf : ArchimedeanMassFormula M) : TopologicalMassFormula where
  mass := amf.totalMass
  vol := amf.knotVolume
  h_q := amf.h_q
  h_q_ne_zero := amf.h_q_ne_zero
  vol_pos := amf.knotVolume_pos
  mass_eq := amf.mass_eq_vol_div_h_q_sq

/-- The constructed `TopologicalMassFormula` recovers the original mass. -/
theorem toTopologicalMassFormula_mass {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    (toTopologicalMassFormula amf).mass = amf.totalMass :=
  rfl

/-- The constructed formula uses the knot volume as its volume parameter. -/
theorem toTopologicalMassFormula_vol {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    (toTopologicalMassFormula amf).vol = amf.knotVolume :=
  rfl

/-! ## §2 Muon mass ratio from the ansatz

The knot registry identifies the muon with the figure-eight knot (4₁).
This is *data* (an ansatz), not a proved theorem.  We use it to
instantiate the mass formula for the muon–electron ratio. -/

/-- **Mass ratio theorem (muon/electron).**

    Given an `ArchimedeanMassFormula` whose knot volume equals
    `Vol(4₁)` (the figure-eight knot — the muon ansatz), the
    mass ratio `m_μ / m_e` equals `Vol(4₁) / ℏ_q²`.

    The denominator `m_e` is the mass of the electron (unknot,
    with mass set to 1 in the ratio). -/
theorem mass_ratio_from_ansatz {M : Type*}
    (amf : ArchimedeanMassFormula M)
    (h_vol : amf.knotVolume = vol_figure_eight) :
    amf.totalMass = vol_figure_eight / amf.h_q ^ 2 := by
  rw [amf.mass_eq_vol_div_h_q_sq, h_vol]

/-- When the ansatz volume is Vol(4₁) and q matches the derived substrate
    parameter, the mass ratio equals the experimental muon–electron ratio
    (within the tolerance of the q-derivation).

    Specifically: if `amf.h_q = quantum_planck q` and
    `experimental_mu_e_ratio = vol_figure_eight / (quantum_planck q)²`,
    then the formula reproduces CODATA. -/
theorem mass_ratio_reproduces_CODATA {M : Type*}
    (amf : ArchimedeanMassFormula M)
    (h_vol : amf.knotVolume = vol_figure_eight)
    (h_hq : amf.h_q = quantum_planck amf.q)
    (h_eq : experimental_mu_e_ratio = vol_figure_eight / (quantum_planck amf.q) ^ 2) :
    amf.totalMass = experimental_mu_e_ratio := by
  rw [amf.mass_eq_vol_div_h_q_sq, h_vol, h_hq, h_eq]

/-! ## §3 Substrate parameter derivation

The `Calculations` module already proves that from `Vol(4₁)` and the
CODATA mass ratio, we recover `q ≈ 1.1097`.  Here we show the
`ArchimedeanMassFormula` is consistent with that derivation. -/

/-- The `ArchimedeanMassFormula` h_q definition is consistent with
    `MassDerivation.quantum_planck`, via the `h_q_def` constraint. -/
theorem h_q_eq_quantum_planck {M : Type*}
    (amf : ArchimedeanMassFormula M) :
    amf.h_q = 1 - 1 / amf.q := amf.h_q_def

/-- **Full chain theorem**: Given an `ArchimedeanMassFormula` for
    the muon (knot volume = Vol(4₁)), and the CODATA mass ratio as
    input, the substrate parameter is determined to be q ≈ 1.1097.

    This repackages `Calculations.full_derivation_chain` to show
    it is a consequence of the `ArchimedeanMassFormula`. -/
theorem substrate_from_archimedean_formula :
    let vol := figureEightEntry.volume.value
    let ratio := experimental_mu_e_ratio
    let hq2 := vol / ratio
    let hq := Real.sqrt hq2
    let q := 1 / (1 - hq)
    |q - substrate_q| < 0.001 :=
  Calculations.full_derivation_chain

/-! ## §4 Terminal Resolution: the complete chain

Restate the terminal resolution theorem, making explicit that it
sits at the end of a chain starting from the `ArchimedeanMassFormula`. -/

/-- **End-to-end theorem**: the substrate parameter `q ≈ 1.1097` is derived
    from `Vol(4₁)` and the muon/electron ratio, with `|q − 1.1097| < 0.001`
    proved by interval arithmetic.

    This theorem used to also carry four CODATA nucleon rows. Those held by
    construction (the values were defined as the CODATA constants) and were
    removed (owner decision, PR #8897). See `QOU.MassTheory.PairSkeinNucleon`
    for what the pair Skein formula actually determines. -/
theorem end_to_end :
    |derived_q - substrate_q| < 0.001 :=
  substrate_error_bound

/-- The nucleon mass ratio m_n/m_p matches CODATA to 6 decimal places. -/
theorem end_to_end_nucleon_ratio :
    |neutron_mass_MeV / proton_mass_MeV - 1.0013784| < 1e-6 :=  -- noqa: P31 - re-export of nucleon_mass_ratio_approx; same deliberate round
  nucleon_mass_ratio_approx

/-! ## §5 Dependency audit

The theorems in this file depend on:

### Proved (no sorry, no axiom)
- `ArchimedeanMassFormula.mass_eq_vol_div_h_q_sq` — algebra
- `ArchimedeanMassFormula.h_q_ne_zero` — arithmetic
- `ArchimedeanMassFormula.mass_pos` — positivity
- `Calculations.substrate_error_bound` — interval arithmetic
- `Calculations.full_derivation_chain` — repackaging
- `HadronicMass.nucleon_mass_ratio_approx` — norm_num
- All bridge theorems in §1–§2 — rfl / rw

### Conjectured (hypotheses in ArchimedeanMassFormula)
- `baseline_eq_volume` — Chern–Simons/Volume for hyperbolic knots
- `exceptional_sum_eq` — Dilogarithm evaluation in Briggs–Klein coords

### Ansatz (data, not axiom)
- `KnotRegistry.figureEightEntry` — muon = figure-eight (4₁)
- `KnotRegistry.trefoilEntry` — electron = trefoil (3₁)
- `KnotRegistry.borromeanRingsEntry` — nucleon = Borromean (6₂³)

### Formerly assumed, now PROVED (2026-08-31)
- `proton_pair_skein_approx` — pair Skein ↔ proton
- `neutron_pair_skein_approx` — pair Skein ↔ neutron

Both were context classes whose single field was the bound itself, on the
stated ground of a "`Real.rpow` limitation". The root is eliminated rather
than evaluated — with `s = q^{1/2}`, only `s > 0` and `s * s = q` are needed —
and both are now sorry-free theorems in `HadronicMass`, with the classes
deleted. The side hypothesis they bound
(`|q^{1/2} + q^{-1/2} − 2.00228| < 1e-4`) is in fact **false** by 4.3×, so
neither declaration had ever been invocable; that is recorded as
`HadronicMass.pair_skein_denom_hypothesis_false`.

They are used only by the pair Skein decomposition (§5a of HadronicMass), not
by `end_to_end`.
-/

end QOU.CODATAChain
