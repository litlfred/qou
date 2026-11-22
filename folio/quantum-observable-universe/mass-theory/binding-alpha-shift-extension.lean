/-
  # Binding A≥3 via per-rep Reeb phase at a force-carrier torus knot

  The binding-endomorphism analogy
  (`docs/audits/2026-05-28-binding-endomorphism-analogy.md`) closes the
  deuteron (A = 2) to **+0.19 %** via `B = m_e · Vol(𝓑₃) · Δtr` but
  undershoots A ≥ 3 by 44–72 %.  The audit diagnoses: `Δtr` is the
  *linear truncation* of `log(tr) ~ Vol`; the extensive observable
  lives in the **per-rep q-Reeb rotation phase**.

  The merged α_shift universal chain
  (`docs/audits/2026-05-30-alpha-shift-universal-derivation-chain.md`)
  proves `α_shift(T_{p, k}) = k · (p - 1)` (sorry-free conditional on
  `HasAlphaShiftTorus`) — the **pole order** of σ on the column-rich
  irrep of T(p, k), equivalently the boundary holonomy of the
  Yekutieli non-abelian Stokes integral around the column cycle.

  This file wires the binding per-rep Reeb phase into the α_shift
  universal chain.  For each light nucleus K, identify a
  **binding-specific force-carrier torus knot** `T(p_K, k_K)` whose
  α_shift sets the per-rep Reeb eigenvalue.  The binding closure
  is then

      B(K) = m_e · ρ_0 · α_shift(T(p_K, k_K))

  with `ρ_0` a substrate-universal per-rep coupling (deuteron pins it
  at ρ_0 ≈ 14.7 MeV/rad per `binding_rotation_phase_lead.py`).

  This is the A≥3 analogue of:
  - `meson-color-tube-uniqueness.lean` for m_K/m_π (force-carrier pair
    `{T(2, 3), T(2, 4)}`, smallest non-trivial pair);
  - `em-coupling-bring-zero-mode.lean` for 1/α_EM (force-carrier pair
    `{T(2, 9), T(3, 5)}`, genus-4 Bring pair);
  - the T(2, k) lepton tower for the electroweak triplet (k = 4, 6, 8)
    and τ candidate (k = 7).

  **Open math (Phase 3 of this extension):** identify the specific
  `(p_K, k_K)` for each light nucleus K ∈ {D, T, ³He, ⁴He}.  The
  agent-survey hypothesis (2026-05-30) suggests p ∈ {2, 3} with k ≥ 5
  for A ≥ 3, based on the observed ρ ≈ 18.5 MeV/rad for the mirror
  pair — a ~25 % rise from the deuteron's ρ ≈ 14.7 MeV/rad, consistent
  with a per-λ jump in pole order.

  **Base ring (AGENTS.md §7c).**  Nothing here divides: the class field is
  the product `B A = m_e · ρ_0 · (α_shift A : R)` and both theorems are pure
  rewriting.  So the carrier is the weakest typeclass that admits the
  statement — a generic `{R : Type u} [Semiring R]` (multiplication plus the
  `ℕ`-cast of the pole order).  The previous `[Field R]` was gratuitous, as
  was the `Mathlib.Data.Real.Basic` import.

  Ref: [leitner2026] prop:binding-alpha-shift-extension
       [leitner2026] prop:alpha-shift-torus-knot
       [audit] docs/audits/2026-05-28-binding-endomorphism-analogy.md
       [audit] docs/audits/2026-05-30-alpha-shift-universal-derivation-chain.md
       [probe] computations/binding_rotation_phase_lead.py
       [probe] computations/binding_qhamiltonian_rotational_scale.py
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Data.Nat.Cast.Defs

namespace QOU.BraidKnot

universe u

/-- α_shift formula (local mirror of
    `mass-theory/alpha-shift-torus-knot.alphaShift` for ergonomics).
    Pole order of σ on the column-rich irrep of T(p, k). -/
def bindingAlphaShift (p k : ℕ) : ℕ := k * (p - 1)

/- The α_shift specialisations relevant to A ≥ 3 binding (open math
   per Phase 3 of this extension): the substrate-specific force-
   carrier torus knot for each light nucleus is yet to be identified.
   Candidate forms per the agent-survey hypothesis. -/
section CandidateForceCarrierKnots
/-- Hypothesis (Phase 3 open): T(2, 5) for tritium / ³He at A = 3.
    α_shift = 5. -/
example : bindingAlphaShift 2 5 = 5 := by rfl
/-- Hypothesis (Phase 3 open): T(3, 4) for ⁴He at A = 4.
    α_shift = 8. -/
example : bindingAlphaShift 3 4 = 8 := by rfl
end CandidateForceCarrierKnots

/-- **Binding per-rep Reeb phase class.**  For each light nucleus
    `A`, the binding energy `B(A)` scales as `m_e · ρ_0 · α_shift_K`
    where `α_shift_K` is the pole order of σ on the column-rich
    irrep of the binding-specific force-carrier torus knot
    `T(p_K, k_K)`, and `ρ_0` is the substrate-universal per-rep
    Reeb coupling pinned by the deuteron (≈ 14.7 MeV/rad per
    `binding_rotation_phase_lead.py`).

    Per AGENTS.md §3b-cond: the binding closure is gated on the
    **per-rep Reeb phase axiom** (substrate identity) and the
    **force-carrier knot identification** (Phase 3 open math).  -/
class BindingPerRepReebPhase {R : Type u} [Semiring R]
    (B : ℕ → R) (m_e ρ_0 : R) where
  /-- B(A) factors through α_shift at the binding-specific torus
      knot.  The function `αShiftAt` records, per nucleus index A,
      the proved α_shift value `k_A · (p_A − 1)` of the substrate-
      identified force-carrier torus knot `T(p_A, k_A)`. -/
  αShiftAt : ℕ → ℕ
  /-- B(A) = m_e · ρ_0 · (αShiftAt A : R).  Substrate identity. -/
  factors : ∀ A : ℕ, B A = m_e * ρ_0 * (αShiftAt A : R)

/-- **Force-carrier knot identification class.**  The substrate
    fixes a torus knot `T(p_A, k_A)` per nucleus A such that
    `αShiftAt A = bindingAlphaShift p_A k_A = k_A · (p_A − 1)`.

    Phase 3 open math: the identification (`p_A`, `k_A`) for each
    A ∈ {2, 3, 4, ...} must be derived from the substrate's
    Hecke-Wedderburn block structure on H_{3A}(q) at the binding's
    minimum-dimensional non-trivial irrep, analogous to the meson
    force-carrier pair derivation. -/
class BindingForceCarrierKnot
    (αShiftAt : ℕ → ℕ) (p k : ℕ → ℕ) : Prop where
  /-- For every nucleus A, the per-rep α_shift equals the formal
      value at the identified torus knot. -/
  matches_alpha_shift : ∀ A : ℕ, αShiftAt A = bindingAlphaShift (p A) (k A)

/-- **Binding uniqueness theorem (via α_shift).**  Given the
    per-rep Reeb phase axiom + the force-carrier knot identification,
    two binding evaluators sharing the same substrate parameters
    (m_e, ρ_0, knot identification) agree pointwise.

    Per AGENTS.md §3b-cond: sorry-free conditional on the two
    classes.  Phase 3 (the actual `(p_A, k_A)` identification) is
    research-grade and deferred.

    **Refactored 2026-05-30 per @litlfred review** (#1464 line-129
    comment): the theorem now derives the `αShiftAt` equality from
    the shared `BindingForceCarrierKnot` class via
    `matches_alpha_shift`, eliminating the ad-hoc hypothesis and
    aligning the Lean structure with the audit's §3b-cond gating
    intent. -/
theorem binding_unique_via_alpha_shift
    {R : Type u} [Semiring R]
    (B B' : ℕ → R) (m_e ρ_0 : R) (p k : ℕ → ℕ)
    [hB : BindingPerRepReebPhase B m_e ρ_0]
    [hB' : BindingPerRepReebPhase B' m_e ρ_0]
    [hFC : BindingForceCarrierKnot hB.αShiftAt p k]
    [hFC' : BindingForceCarrierKnot hB'.αShiftAt p k] :
    B = B' := by
  funext A
  rw [hB.factors A, hB'.factors A,
      hFC.matches_alpha_shift A, hFC'.matches_alpha_shift A]

/-- **Sub-singleton companion.**  The space of binding evaluators
    sharing the same `(m_e, ρ_0)` and a common
    `BindingForceCarrierKnot` identification `(p, k)` is a
    subsingleton.  Refactored 2026-05-30 per the same #1464 review
    to consume the force-carrier class rather than an ad-hoc
    equality. -/
theorem binding_subsingleton
    {R : Type u} [Semiring R] (m_e ρ_0 : R) (p k : ℕ → ℕ) :
    Subsingleton {B : ℕ → R //
      ∃ (hB : BindingPerRepReebPhase B m_e ρ_0),
        BindingForceCarrierKnot hB.αShiftAt p k} := by
  refine ⟨fun ⟨B, hB, hFC⟩ ⟨B', hB', hFC'⟩ => ?_⟩
  apply Subtype.ext
  funext A
  show B A = B' A
  rw [hB.factors A, hB'.factors A,
      hFC.matches_alpha_shift A, hFC'.matches_alpha_shift A]

/-! ### Concrete light-nuclei force-carrier candidates (#1485)

    The four light-nuclei candidate identifications from the
    Phase-3 audit table, packaged as concrete `(p, k)` selectors and
    a single `BindingForceCarrierKnot` instance.  This is the
    "do all four in one go" consolidation requested on PR #1485:
    rather than four separate sibling blocks (one per nucleus),
    the four selectors share a single `αShiftAt`, `lightNucleusP`,
    `lightNucleusK` and one instance discharges
    `matches_alpha_shift` for all `A ∈ {2, 3, 4}`.

    | A | nucleus    | T(p, k)  | α_shift |
    |--:|------------|----------|--------:|
    | 2 | D          | T(2, 3)  | 3       |
    | 3 | T / ³He    | T(2, 5)  | 5       |
    | 4 | ⁴He        | T(3, 4)  | 8       |

    The A = 2 (D) candidate is informed by:
    - T(2, 3) is the smallest non-trivial torus knot (trefoil) —
      minimum-pole-order column-rich irrep;
    - 𝓑₃-braid-closure consistency: the binding-endomorphism
      analogy closes the deuteron via Vol(𝓑₃) to +0.19 %, and
      T(2, 3) is the canonical boundary torus knot of 𝓑₃;
    - calibration consistency with the `binding_rotation_phase_lead.py`
      probe: `rho_full(D) = 14.6673 MeV/rad` is the per-deuteron
      phase-weighted aggregation (witness output); the abstract
      substrate coupling `ρ_0` in the class signature is the
      dimensionless ratio `B(D)/(m_e · 3) ≈ 1.451` derived after
      dividing by `m_e · α_shift`.  The two quantities are **distinct**
      — bridged by the `α_shift = 3` normalisation — see the .md
      narrative for the full disambiguation.

    The A = 3 (T, ³He) and A = 4 (⁴He) candidates are reproduced
    from the audit table in the file header, with sentinel `0` for
    A ∉ {2, 3, 4}.

    **Status.**  These are CANDIDATE identifications, not derived
    uniqueness theorems.  Phase 3 closure — proving each `(p_A, k_A)`
    is the substrate's unique choice — requires the per-nucleus
    H_{3A}(q) Wedderburn-block minimisation queued alongside the
    meson force-carrier identification.  This block provides the
    instance scaffolding; substrate-uniqueness is the remaining
    open math. -/

/-- Light-nuclei force-carrier `p`-index selector at A ∈ {2, 3, 4}.
    A=2 → 2 (T(2,3)); A=3 → 2 (T(2,5)); A=4 → 3 (T(3,4)).  Sentinel
    `0` elsewhere. -/
def lightNucleusP : ℕ → ℕ := fun A =>
  if A = 2 then 2
  else if A = 3 then 2
  else if A = 4 then 3
  else 0

/-- Light-nuclei force-carrier `k`-index selector.  A=2 → 3 (T(2,3));
    A=3 → 5 (T(2,5)); A=4 → 4 (T(3,4)).  Sentinel `0` elsewhere. -/
def lightNucleusK : ℕ → ℕ := fun A =>
  if A = 2 then 3
  else if A = 3 then 5
  else if A = 4 then 4
  else 0

/-- Light-nuclei α_shift profile, defined directly as
    `bindingAlphaShift (lightNucleusP A) (lightNucleusK A)`.

    Using the structural composition rather than re-listing the
    magic values (3, 5, 8) eliminates duplication and lets all
    downstream proofs close definitionally (`rfl`).  Per Gemini
    medium-priority review on #1485. -/
def lightNucleusAlphaShift (A : ℕ) : ℕ :=
  bindingAlphaShift (lightNucleusP A) (lightNucleusK A)

/-- Sanity check at the deuteron candidate T(2, 3): α_shift = 3. -/
theorem light_nucleus_alpha_shift_at_deuteron :
    lightNucleusAlphaShift 2 = 3 := rfl

/-- Sanity check at the A = 3 mirror pair T(2, 5): α_shift = 5. -/
theorem light_nucleus_alpha_shift_at_A3 :
    lightNucleusAlphaShift 3 = 5 := rfl

/-- Sanity check at ⁴He's candidate T(3, 4): α_shift = 8. -/
theorem light_nucleus_alpha_shift_at_He4 :
    lightNucleusAlphaShift 4 = 8 := rfl

/-- **Concrete `BindingForceCarrierKnot` instance covering all four
    light-nuclei candidates A ∈ {2, 3, 4}.**

    Closes the Phase-3 candidate identifications in a single
    instance.  Since `lightNucleusAlphaShift` is defined directly
    as `bindingAlphaShift ∘ ⟨lightNucleusP, lightNucleusK⟩`,
    `matches_alpha_shift` holds **definitionally** — the proof is
    `rfl`.  **No** `sorry`.

    Substrate-uniqueness of each `(p_A, k_A)` — proving these are
    the substrate's choices rather than candidates — remains open
    pending the H_{3A}(q) Wedderburn-block minimisation. -/
instance lightNucleiForceCarrierKnot :
    BindingForceCarrierKnot lightNucleusAlphaShift lightNucleusP lightNucleusK where
  matches_alpha_shift _ := rfl

end QOU.BraidKnot
