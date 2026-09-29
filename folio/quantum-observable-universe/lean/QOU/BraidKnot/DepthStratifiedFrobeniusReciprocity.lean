/-
Frobenius-reciprocity ideal restriction at low curvature-rank.

At low curvature-rank k ≤ 3, the Wedderburn weight ~w_λ pulls
back through the distinguished hyperbolic-knot ideal e_{K_k*}
via the center inclusion Z(H_3) ↪ Z(H_n).

At k = 3: K_3* = 4_1 (chirality channel) — but see the weight-family
caveat below before quoting that.
At k = 1, k = 2: K_1*, K_2* are OPEN structural questions.

WEIGHT FAMILY (added 2026-09-05).  "K_3* = 4_1" is the ranking under the
textbook weight w_λ = dim_q²/[n]_q!, and the k = 3 ranking is NOT
invariant across weight families: dim_q²/[n]_q! ranks 4_1 best, the
self-normalised dim_q²/Σ_μ dim_q² ranks 6_1 best, the Molien weight
f^λ q^{−κ_λ} dim_q(λ)/[n]_q! ranks 5_2 best, and under the Markov
weights y_λ the depth-3 stratum vanishes identically (SU(N) row cap), so
the test is vacuous.  Which family Φ_k requires is open (bean qou-oots).
Do not quote a k = 3 knot conclusion without naming the family.
Ref: docs/audits/2026-09-05-phi-k-weight-family.md
Ref: docs/audits/2026-09-05-k3-weight-family-labelling.md

The parenthetical "named in prop:plancherel-term-7-formulation" that used
to sit on the k = 3 line is dropped: that block defines w_λ and names no
knot, so it does not source the 4_1 identification.  The 4_1 result is
PR #826's empirical test, at the textbook weight.

This Lean file follows the QOU.Infra.Polylogarithm pattern:
- Concrete `noncomputable def` for the FR-pulled-back weight
  formula (no analytic content needed)
- Verified arithmetic on the FR pullback (e.g. the
  normalisation cancels uniform weight for trivial projector)
- `class` hypothesis for the FR-pullback substantive identity
  (the q-deformation case)
- Empirical falsification records as direct theorems

Ref: [frobenius1898] Über die Charaktere der symmetrischen Gruppe
Ref: [macdonald1995] Symmetric Functions and Hall Polynomials, I.7
Ref: conj:depth-stratified-frobenius-reciprocity.md
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.BraidKnot

/-- The depth-k distinguished knot ideal as a central projector.

    Fields:
    - `central_projector_value`: amplitude of the central projector
      e_K at a partition (proxy for the full Hecke-algebra projector
      in the abstract setting), valued in the generic base ring `R`.
    - `knot_label`: the name of the distinguished knot ("4_1"
      at k = 3 *under the textbook weight* `dim_q²/[n]_q!` — the label is
      family-relative, see the module docstring; pending for k = 1, k = 2).

    §7c: the FR-pullback weight algebra below is pure field arithmetic
    (a `dim_q²·χ / ([n]_q!·Z)` ratio), so it is stated over a generic
    `{R : Type*} [Field R]`. This module is now wholly on the algebraic
    side of the substrate→archimedean wall: the empirical decimal
    *variance records* (ordered `ℝ` literals) that used to sit further
    down have been split out into the sibling
    `QOU.BraidKnot.DepthStratifiedFrobeniusReciprocityVariance`. -/
structure DistinguishedKnotIdeal (k : ℕ) (R : Type*) where
  central_projector_value : R
  knot_label : String

/-- The distinguished chirality-channel ideal at k = 3:
    4_1 (figure-eight knot), as ranked best by the FR-pullback variance
    test **under the textbook weight** `w_λ = dim_q²/[n]_q!` (PR #826).
    The ranking is weight-family-dependent — see the module docstring —
    so this label records one family's answer, not a settled
    identification. -/
noncomputable def chirality_ideal_4_1 {R : Type*} [Field R] : DistinguishedKnotIdeal 3 R :=
  { central_projector_value := 1, -- placeholder for the
                                  -- abstract projector value
    knot_label := "4_1" }

/-- The classical (uniform) Wedderburn weight at depth k:
    dim_q²(λ) / [n]_q!.  Defined unconditionally as a closed-form
    placeholder; downstream code parametrises by the actual
    partition data. -/
noncomputable def uniformWedderburnWeight {R : Type*} [Field R]
    (dim_q_sq : R) (n_q_fact : R) : R :=
  dim_q_sq / n_q_fact

/-- The FR-pulled-back Wedderburn weight at depth k:
    dim_q²(λ) · χ^λ(e_{K_k*}) / ([n]_q! · Z_normalization)

    where Z_normalization is the partition-depth sum of
    dim_q²(μ) · χ^μ(e_{K_k*}).

    Verifiable identity: when χ^λ(e_K) = 1 (trivial projector,
    i.e. K is "transparent"), the FR weight reduces to the
    uniform weight times the depth-sum reciprocal. -/
noncomputable def frPulledBackWeight {R : Type*} [Field R]
    (dim_q_sq : R) (n_q_fact : R)
    (chi_lambda_eK : R) (z_normalization : R) : R :=
  dim_q_sq * chi_lambda_eK / (n_q_fact * z_normalization)

/-- Special case: when the projector character χ^λ(e_K) = 1
    uniformly across the depth stratum (the "transparent"
    projector limit), and Z_normalization = 1 (single-block
    stratum), the FR weight equals the uniform weight.
    **Verified** unconditionally. -/
theorem fr_weight_transparent_reduces_to_uniform {R : Type*} [Field R]
    (dim_q_sq n_q_fact : R) (hf : n_q_fact ≠ 0) :
    frPulledBackWeight dim_q_sq n_q_fact 1 1 =
      uniformWedderburnWeight dim_q_sq n_q_fact := by
  unfold frPulledBackWeight uniformWedderburnWeight
  field_simp

/-- The FR weight normalisation: if Z_norm = Σ dim_q²(μ) χ^μ(e_K)
    for μ in a depth stratum, then summing the FR weights over
    that stratum gives 1 (after the dim_q² · χ^μ(e_K) / n_q_fact
    normalisation). Stated as a structural property of the
    Z_normalization choice. -/
theorem fr_weight_normalised {R : Type*} [Field R]
    (dim_q_sq n_q_fact chi_lambda_eK z_normalization : R)
    (hf : n_q_fact ≠ 0) (hz : z_normalization ≠ 0) :
    z_normalization *
      frPulledBackWeight dim_q_sq n_q_fact chi_lambda_eK z_normalization =
      dim_q_sq * chi_lambda_eK / n_q_fact := by
  unfold frPulledBackWeight
  field_simp

/-- The DepthStratifiedFrobeniusReciprocity conjecture as a class.

    Fields:
    - `knot_ideal_at_k`: the distinguished knot ideal at each
      k ≤ 3 (only k = 3 has a named instance currently).
    - `fr_pullback_at_low_k`: predicate identifying the
      (q, k) pairs where the FR pullback holds.
    - `fr_pullback_classical`: the classical-limit case
      (provable in principle via Mathlib's Representation.induced;
      pending Specht-module API).

    Per AGENTS.md §3b-cond, downstream theorems consume the
    class via [Instance]. -/
class DepthStratifiedFrobeniusReciprocity (R : Type*) [Field R] where
  knot_ideal_at_k : (k : ℕ) → k ≤ 3 → DistinguishedKnotIdeal k R
  fr_pullback_at_low_k : R → ℕ → Prop
  fr_pullback_classical : ∀ k : ℕ, fr_pullback_at_low_k 1 k

/-- **Chirality-ideal model with the predicate read as its own
    witness.**  `knot_ideal_at_k` is real at `k = 3`
    (`chirality_ideal_4_1`) and a `"?"`-labelled zero projector
    elsewhere.  The conjectural field is not: `fr_pullback_at_low_k` is
    *defined* to be `fun q _k => q = 1`, so
    `fr_pullback_classical : ∀ k, fr_pullback_at_low_k 1 k` unfolds to
    `1 = 1` and closes by `rfl`, uniformly in `k`.  No Frobenius
    reciprocity, induced representation or depth stratum is encoded;
    the field is satisfied by choosing the predicate to be the equation
    the field asserts.

    The classical-limit case genuinely is provable in principle, via
    Mathlib's `Representation.induced` plus the pending Specht-module
    API — that is what a real model would have to supply here.

    **A `def`, not an `instance`, since 2026-08-24**, and given a name:
    it was anonymous, so resolution supplied it for every field under
    the generated name `instDepthStratifiedFrobeniusReciprocity`.

    Callers name it: `letI := depthStratifiedFR_chiralityIdeal R`. -/
noncomputable def depthStratifiedFR_chiralityIdeal (R : Type*) [Field R] :
    DepthStratifiedFrobeniusReciprocity R where
  knot_ideal_at_k k _h := match k with
    | 3 => chirality_ideal_4_1
    | _ => { central_projector_value := 0,
              knot_label := "?" }
  fr_pullback_at_low_k q _k := q = 1
  fr_pullback_classical _k := rfl

/-! ## Properties of the chirality ideal at k = 3 -/

/-- The chirality ideal at k = 3 is labelled "4_1". -/
theorem chirality_ideal_4_1_label {R : Type*} [Field R] :
    (chirality_ideal_4_1 (R := R)).knot_label = "4_1" := by
  rfl

/-- The chirality ideal at k = 3 has central projector value 1
    (placeholder; the full Hecke-algebra projector requires the
    q-Hecke representation infrastructure). -/
theorem chirality_ideal_4_1_value {R : Type*} [Field R] :
    (chirality_ideal_4_1 (R := R)).central_projector_value = 1 := by
  rfl

/-! ## FR-weight algebraic properties -/

/-- The FR-pulled-back weight scales linearly in χ^λ(e_K). -/
theorem fr_weight_chi_scale {R : Type*} [Field R]
    (dim_q_sq n_q_fact chi_lambda_eK z_normalization c : R)
    (hf : n_q_fact ≠ 0) (hz : z_normalization ≠ 0) :
    frPulledBackWeight dim_q_sq n_q_fact (c * chi_lambda_eK) z_normalization =
      c * frPulledBackWeight dim_q_sq n_q_fact chi_lambda_eK z_normalization := by
  unfold frPulledBackWeight
  field_simp

/-- The FR-pulled-back weight is invariant under simultaneous
    rescaling of dim_q_sq and z_normalization by the same factor
    (homogeneity of the ratio).

    Provable directly via field arithmetic. -/
theorem fr_weight_homogeneous {R : Type*} [Field R]
    (dim_q_sq n_q_fact chi_lambda_eK z_normalization c : R)
    (hf : n_q_fact ≠ 0) (hz : z_normalization ≠ 0) (hc : c ≠ 0) :
    frPulledBackWeight (c * dim_q_sq) n_q_fact chi_lambda_eK (c * z_normalization) =
      frPulledBackWeight dim_q_sq n_q_fact chi_lambda_eK z_normalization := by
  unfold frPulledBackWeight
  field_simp

/-! ## Empirical variance records — moved to the archimedean sibling

The measured decimal variance scoreboards (`fr_simpler_forms_variance_records`,
`variance_ordering_records`) live in
`QOU.BraidKnot.DepthStratifiedFrobeniusReciprocityVariance`. They are ordered
comparisons of `ℝ` literals, so per §7c they belong on the archimedean side of
the wall rather than in this generic-`[Field R]` module. -/

end QOU.BraidKnot
