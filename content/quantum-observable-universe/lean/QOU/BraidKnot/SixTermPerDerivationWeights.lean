import Mathlib.Tactic

/-
Per-term weight assembly for the six-term mass formula.

Stub formalisation of `prop:six-term-per-derivation-weights`.
The full proof requires several upstream pieces that are
currently in flight:
  - The descended Markov trace evaluation (T₁) at the
    β-decay scale `E_0_β = 0.7823 MeV`.
  - The Borromean-Catalan binding scale `α = m_e · 8G`
    proven in `BindingScaleCatalan.lean`.
  - The corrected Kashaev integration identity
    `∫_0^V (ln_q(1+t)/t) dt = -Li_2^q(-V)` (proven on
    `claude/categorical-mass-divergence-audit`,
    commit a43d7f1fa, witness
    `kashaev-integration-identity.witness.json`).

For now this file declares the assembly interface and an
axiomatised `binding_assembly` constant so the content block's
`lean.ref` resolves; the full proof is gated on the upstream
formalisations above.

Empirical witness (Python, sub-percent on A ≤ 9):
  `paper_six_term_isotope_sweep.assemble_per_derivation_weights`
  (mean 0.184 %, max 0.525 % vs CODATA atomic mass).
-/

namespace QOU.BraidKnot.SixTermPerDerivationWeights

/-- The six-term mass formula's binding-energy assembly with
    derivation-fixed per-term weights:

      B(Z, N) = E_0_β · (T1_free − T1_atom)
              + α · ((T2 + T3)_atom − (T2 + T3)_free)
              + m_e · (T4_atom − T4_free)
              + E_0_β · (a_K − 1) · T1_atom
              + (T6_atom − T6_free)

    Returns a real-valued binding energy (MeV).  Type-level
    interface only; the concrete evaluation lives in the Python
    pipeline (`assemble_per_derivation_weights`).  This Lean
    declaration provides the formal handle for downstream
    proofs that quote the assembly. -/
opaque binding_assembly (Z N : Nat) : Float

/-- The genuinely-open empirical inputs for the sub-percent
    accuracy claim: for an isotope `(Z, N)`, the per-derivation
    assembled atomic mass `assembled_mass` and the measured AME
    atomic mass `measured_mass` (both in MeV, `measured_mass > 0`).
    A categorical derivation of these from the substrate is open;
    they are carried as hypotheses (pattern C), not asserted. -/
class SixTermAssemblyData where
  /-- The per-derivation assembled atomic mass (MeV). -/
  assembled_mass : Nat → Nat → ℝ
  /-- The measured AME atomic mass (MeV). -/
  measured_mass : Nat → Nat → ℝ
  /-- Measured masses are positive. -/
  measured_pos : ∀ Z N, 0 < measured_mass Z N

/-- **Six-term per-derivation weights — sub-percent accuracy.**

Names (pattern C of the vacuity-fix playbook) the conditional
conjecture that, across the proton..⁹Be spectrum (`A = Z + N ≤ 9`),
the per-derivation assembly recovers the AME atomic mass to within
the empirical max relative error `0.0053` (= 0.53 %, from the
`A ≤ 9` sweep).  This is a *proposition* — honestly named, not a
vacuous `: True := trivial`: the mass data live on
`[SixTermAssemblyData]`, and an instance discharging the bound is
the open empirical claim (none = honest open state).

Ref: paper_six_term_isotope_sweep.py (assemble_per_derivation_weights)
Ref: docs/audits/2026-05-04-per-derivation-weights-result.md -/
-- Ref: [manuscript] prop:six-term-per-derivation-weights
def binding_assembly_subpercent [data : SixTermAssemblyData]
    (Z N : Nat) (_hA : Z + N ≤ 9) : Prop :=
    |data.assembled_mass Z N - data.measured_mass Z N| / data.measured_mass Z N ≤ 0.0053

end QOU.BraidKnot.SixTermPerDerivationWeights
