/-
  # `conj:binding-deuteron-force-carrier` — concrete BindingForceCarrierKnot
    instance for the deuteron (A = 2)

  The Phase-3 open math noted in `binding-alpha-shift-extension`
  asks: for each light nucleus `A`, identify the substrate-specific
  force-carrier torus knot `T(p_A, k_A)`.  The candidate hypotheses
  in the audit table:

    A = 3 (T, ³He) : T(2, 5),  α_shift = 5
    A = 4 (⁴He)    : T(3, 4),  α_shift = 8
    A = 2 (D)      : T(?, ?)   ← pinned by ρ₀ calibration

  This file proposes — and constructs the `BindingForceCarrierKnot`
  instance for — the deuteron candidate

      T_D := T(2, 3),    α_shift(T(2, 3)) = 3 · (2 - 1) = 3.

  Rationale:
  - **Smallest non-trivial torus knot.**  T(2, 3) is the trefoil; the
    minimum-pole-order column-rich irrep on a torus knot, matching
    the deuteron's role as the lightest A ≥ 2 nucleus.
  - **B_3 braid closure consistency.**  The binding-endomorphism
    analogy (`docs/audits/2026-05-28-binding-endomorphism-analogy.md`)
    closes the deuteron via `B = m_e · Vol(𝓑₃) · Δtr` to +0.19 %.
    The 3-strand braid 𝓑₃ has T(2, 3) as its canonical boundary
    torus knot (the trefoil is the (2, 3)-cable of the core circle
    in 𝓑₃'s Seifert fibre structure).
  - **ρ_0 ≈ 14.7 MeV/rad calibration.**  Per
    `binding_rotation_phase_lead.py`, the deuteron's full Markov-
    weighted q-Reeb phase aggregation gives ρ_full(D) = 14.6673
    MeV/rad.  With α_shift = 3 and m_e ≈ 0.511 MeV, the substrate
    coupling reads `ρ_0 = B(D) / (m_e · 3) ≈ 1.451`, consistent with
    the substrate-universal range targeted by the audit.

  Phase-3 *closure* — proving T(2, 3) is the substrate's choice rather
  than a candidate — requires the per-nucleus minimisation argument
  on H₆(q)'s Wedderburn block at the binding's smallest non-trivial
  irrep.  This file provides the **instance scaffolding**; the
  identification is a structurally-coherent candidate, not a derived
  uniqueness theorem.

  Ref: [manuscript] prop:binding-alpha-shift-extension
       [manuscript] prop:alpha-shift-torus-knot
       [audit] docs/audits/2026-05-28-binding-endomorphism-analogy.md
       [audit] docs/audits/2026-05-30-alpha-shift-universal-derivation-chain.md
       [probe] folio-assistant/computations/binding_rotation_phase_lead.py
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot

/-- Deuteron-candidate force-carrier `(p, k)` selector: T(2, 3) at A = 2,
    sentinel `(0, 0)` for A ≠ 2.  The non-deuteron sentinel keeps the
    instance closed under `funext` without committing to a tritium /
    ³He / ⁴He identification (those are handled in their own blocks). -/
def deuteronP : ℕ → ℕ := fun A => if A = 2 then 2 else 0

/-- Deuteron-candidate force-carrier `k`-index: `k = 3` at A = 2,
    sentinel `0` elsewhere.  See `deuteronP`. -/
def deuteronK : ℕ → ℕ := fun A => if A = 2 then 3 else 0

/-- The α_shift profile induced by the deuteron candidate
    `(deuteronP, deuteronK)`.  Equals `bindingAlphaShift` pointwise
    by construction; the function is named separately so the
    `BindingForceCarrierKnot` instance is dischargeable by `rfl`-
    pattern on the `if` branch. -/
def deuteronAlphaShift : ℕ → ℕ := fun A => if A = 2 then 3 else 0

/-- Sanity check: at A = 2 the deuteron α_shift equals the formal
    pole order of T(2, 3). -/
theorem deuteron_alpha_shift_eq_three :
    deuteronAlphaShift 2 = bindingAlphaShift (deuteronP 2) (deuteronK 2) := by
  unfold deuteronAlphaShift deuteronP deuteronK bindingAlphaShift
  rfl

/-- Sanity check: the non-deuteron branch is the sentinel `0 = 0`. -/
theorem deuteron_alpha_shift_sentinel (A : ℕ) (hA : A ≠ 2) :
    deuteronAlphaShift A = bindingAlphaShift (deuteronP A) (deuteronK A) := by
  unfold deuteronAlphaShift deuteronP deuteronK bindingAlphaShift
  simp [hA]

/-- **Concrete `BindingForceCarrierKnot` instance for the deuteron
    candidate T(2, 3).**

    Discharges the §3b-cond `matches_alpha_shift` field for the
    specific candidate identification.  The proof is structural:
    case-split on `A = 2`, both branches close by `simp` on the
    definitions.  No `sorry`.

    **Status.**  This is the deuteron half of the Phase-3 closure
    queued in `binding-alpha-shift-extension`.  The candidate
    identification T(2, 3) is informed by the +0.19 % B_3-braid-
    closure consistency and the ρ_0 ≈ 14.7 MeV/rad calibration;
    proving that T(2, 3) is the *substrate's* choice (rather than
    one of several structurally-coherent candidates) is the
    remaining open math. -/
instance deuteronForceCarrierKnot :
    BindingForceCarrierKnot deuteronAlphaShift deuteronP deuteronK where
  matches_alpha_shift A := by
    by_cases h : A = 2
    · subst h
      exact deuteron_alpha_shift_eq_three
    · exact deuteron_alpha_shift_sentinel A h

end QOU.BraidKnot
