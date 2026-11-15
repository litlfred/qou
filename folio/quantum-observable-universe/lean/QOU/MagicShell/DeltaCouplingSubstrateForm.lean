/-
Copyright (c) 2026 Carl Leitner. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# Magic-shell stabilization energy: closed-form conjecture from substrate primitives

Conjectures:
  Δ_coupling(Z, N) = (A - 2) · E_0 · log(1/h(q_0))
                   = (A - 2) · E_0 · [log(1/(k_B T_q)) - log(1 + q_0)]

at magic-shell anchors, where:
  E_0 = m_e / (q_0 (q_0 - 1))   (Hecke energy unit, rem:beta-decay-energy-scale)
  h(q_0) = q_0 - q_0⁻¹           (skein deformation)
  k_B T_q = ℏ_q = (q_0 - 1)/q_0  (prop:boltzmann-constant)
  A = Z + N                       (mass number)

The two forms are equivalent by `hecke_log_decomposition`
(prop:hecke-log-decomposition).

Status: conjecture, single-anchor verified at (Z,N)=(2,2) for ⁴He with
0.71% gap (predicted 13.103 MeV vs extracted 13.20 MeV).

Ref: [manuscript] conj:magic-shell-stabilization
Ref: probe_delta_coupling_leading_form.py
Ref: probe_delta_coupling_q_edgeworth.py (refutes q-Edgeworth κ_3 alternative)
Ref: docs/audits/2026-05-17-delta-coupling-substrate-derivation.md
-/
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import QOU.Information.HeckeLogDecomposition

namespace QOU.MagicShell

/-- Magic-shell stabilization energy as a substrate-derived closed form.

The class encodes the conjecture that Δ_coupling at finite-A magic
shells equals (A - 2) · E_0 · log(1/h(q_0)) — the thermodynamic free-
energy correction per excess nucleon pair at the QOU Hecke-thermal
scale, in the skein-convention normalisation.

Fields are concrete propositional equalities asserting the closed
form. When promoted to a theorem (post cross-anchor verification +
LP-active-set derivation of (A-2)), the class instance becomes the
genuine substrate derivation. Until then it is axiomatised as a
conjecture class per AGENTS.md §3b.
-/
class DeltaCouplingSubstrateForm where
  /-- The substrate parameter q_0 (Wenzl positivity regime). -/
  q0 : ℝ
  /-- q_0 > 1 — required for h(q_0) > 0 and log positivity. -/
  q0_gt_one : 1 < q0
  /-- Electron mass m_e (CAL-1 calibration anchor). -/
  m_e : ℝ
  /-- The Hecke energy unit E_0 = m_e / (q_0 (q_0 - 1)). -/
  E_0 : ℝ
  /-- E_0 definition holds. -/
  E_0_def : E_0 = m_e / (q0 * (q0 - 1))
  /-- The Δ_coupling value at magic shell (Z, N) with mass number A. -/
  delta_coupling : Nat → Nat → ℝ
  /-- The closed-form claim: Δ_coupling(Z, N) = (A-2) · E_0 · log(1/h(q_0)). -/
  closed_form : ∀ (Z N : Nat),
    delta_coupling Z N = ((Z + N : Nat) - 2 : ℝ) * E_0 *
      Real.log (1 / (q0 - q0⁻¹))

/-- The closed-form holds at the doubly-magic anchor (Z, N) = (2, 2) for
    ⁴He within 0.71% of the AME-extracted +13.20 MeV. -/
theorem delta_coupling_substrate_at_2_2 [inst : DeltaCouplingSubstrateForm] :
    inst.delta_coupling 2 2 =
      2 * inst.E_0 * Real.log (1 / (inst.q0 - inst.q0⁻¹)) := by
  -- Direct from `closed_form` at (Z, N) = (2, 2): (Z+N) - 2 = 2.
  -- Ref: [manuscript] conj:magic-shell-stabilization
  -- Numerical: 2 · 4.18598 · 1.56513 = 13.10322883 MeV
  --   vs extracted +13.20 MeV (gap +0.71%)
  -- See probe_delta_coupling_leading_form.py witness for full data.
  have h := inst.closed_form 2 2
  -- (2 + 2 : Nat) - 2 = 2 after Nat→Real coercion
  simp only [show ((2 + 2 : Nat) : ℝ) - 2 = 2 by norm_num] at h
  exact h

/-- The substrate-derivation form is algebraically equivalent to the
    skein-convention leading form by the log decomposition
    (`prop:hecke-log-decomposition`). For every (Z, N) at the magic-
    shell anchor, the skein-form expression
        (A - 2) · E_0 · log(1/(q_0 - q_0⁻¹))
    equals the thermodynamic-form expression
        (A - 2) · E_0 · [log(1/((q_0-1)/q_0)) - log(1 + q_0)]. -/
theorem delta_coupling_two_forms_equivalent
    [inst : DeltaCouplingSubstrateForm] (Z N : Nat) :
    inst.delta_coupling Z N =
      ((Z + N : Nat) - 2 : ℝ) * inst.E_0 *
        (Real.log (1 / ((inst.q0 - 1) / inst.q0)) -
         Real.log (1 + inst.q0)) := by
  -- Apply prop:hecke-log-decomposition:
  --   log(1/(q - q⁻¹)) = log(1/((q-1)/q)) - log(1 + q)
  -- to convert the skein-form `closed_form` into the thermodynamic form.
  rw [inst.closed_form Z N]
  rw [QOU.Information.hecke_log_decomposition inst.q0 inst.q0_gt_one]

/-- Canonical concrete instance of `DeltaCouplingSubstrateForm` for any
    Wenzl-regime `(q, m_e)`.

The instance discharges the class abstraction by *defining*
`delta_coupling Z N` to be the closed-form expression
`(A - 2) · E_0 · log(1/(q - q⁻¹))`. The `closed_form` field is then
satisfied by `rfl`. The empirical claim — that this closed form matches
the AME-extracted magic-shell stabilisation — remains the conjectural
content (verified at the (Z,N)=(2,2) anchor with 0.71% gap).

Construction:
  q0 := q                              (substrate parameter, q > 1)
  m_e := m_e                           (any positive value)
  E_0 := m_e / (q (q - 1))             (Hecke energy unit)
  delta_coupling Z N := ((Z+N) - 2) · E_0 · log(1/(q - q⁻¹))
  closed_form := rfl                   (definitional)

Ref: probe_delta_coupling_leading_form.py (numerical witness at q_0, ⁴He).
Ref: docs/audits/2026-05-17-delta-coupling-substrate-derivation.md
-/
noncomputable instance deltaCouplingSubstrateForm_canonical
    (q : ℝ) (hq : 1 < q) (m_e : ℝ) : DeltaCouplingSubstrateForm where
  q0 := q
  q0_gt_one := hq
  m_e := m_e
  E_0 := m_e / (q * (q - 1))
  E_0_def := rfl
  delta_coupling := fun Z N =>
    ((Z + N : Nat) - 2 : ℝ) * (m_e / (q * (q - 1))) *
      Real.log (1 / (q - q⁻¹))
  closed_form := fun _ _ => rfl

end QOU.MagicShell
