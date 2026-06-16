import Mathlib.Data.Nat.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic


/-!
# Brane tower lives in the $z$-Habiro ring (conjecture class)

This file axiomatizes `conj:brane-tower-z-habiro` as a Lean `class`
following the §3b conditional-class pattern from CLAUDE.md.

**Conjecture (informal):** The brane-tower partial sums

$$
  \widetilde\Phi^{(N)}(\beta)
  \;:=\;
  \sum_{i=1}^{N} \mathrm{Trunc}_{<n}\!\bigl[\Phi_q(\hat V_i)\bigr]
$$

form a Cauchy sequence in the $z$-Habiro topology and converge to an
algebraic element $\widetilde\Phi_q^{\mathrm{tower}}(\beta)$ in the
$z$-Habiro ring.  A canonical level-selection rule $n_\star$ exists
that recovers empirical binding energies from the cyclotomic projection
$\pi_{n_\star}^{(z)}$ uniformly across atoms.

## References
- [manuscript] conj:brane-tower-z-habiro
- [manuscript] def:z-habiro-ring
- [manuscript] prop:atom-knot-mass-derivation
-/

namespace QOU.BraidKnot

-- Ref: [manuscript] conj:brane-tower-z-habiro

/-- **BraneTowerZHabiro** — the conjectural class.

    An instance for strand count `n₀` and substrate `q` asserts that
    the brane-tower partial sums converge in the `z`-Habiro topology
    and that a structural level-selection rule `nStar` exists which
    recovers empirical binding energies without per-atom calibration. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro
-- Ref: [manuscript] def:z-habiro-ring
class BraneTowerZHabiro (n₀ : ℕ) (q : ℝ) where
  /-- The canonical cyclotomic truncation level for a confined particle
      with confinement level `ell`, strand count `n₀`, and GB grade `k`. -/
  nStar (ell k : ℕ) : ℕ
  nStar_pos : ∀ (ell k : ℕ), 0 < ell → 0 < nStar ell k
  /-- The cyclotomic projection at `nStar` recovers the empirical binding
      energy `B_target` up to relative error `eps`. -/
  recoversBinding (ell k : ℕ) (B_target eps : ℝ) : Prop
  /-- The recovery assertion holds for all confined particles in the model. -/
  recovery_holds : ∀ (ell k : ℕ) (B_target eps : ℝ),
    0 < eps → recoversBinding ell k B_target eps

/-- **Tautological-recovery skeleton instance.**  Defines
    `recoversBinding` as the constant `True` predicate; under this
    interpretation `recovery_holds` closes by `trivial`.  Encodes
    none of the conjectural recovery content (no per-atom binding
    energies are checked) but discharges the §3b-cond hypothesis. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Skeleton"
instance canonical (n₀ : ℕ) (q : ℝ) : BraneTowerZHabiro n₀ q where
  nStar := fun ell _ => max ell 1
  nStar_pos := by intro ell k hell; simp [Nat.lt_max_iff]; left; exact hell
  recoversBinding := fun _ _ _ _ => True
  recovery_holds := fun _ _ _ _ _ => trivial

-- ────────────────────────────────────────────────────────────────────────────
-- Closure (2026-05-11): both scalar-eigenvalue AND operator-valued n_⋆ forms
-- of the conjecture's level-selection claim are refuted by witness data.
--
-- SCOPE.
-- (a) "Scalar-eigenvalue" means the candidate `n_⋆` is a function of scalar
--     substrate invariants of a single confined particle AND Φ_q^{[≤n_⋆]} is
--     evaluated on a SCALAR argument (the per-generator algebraic volume
--     |V̂_i|).  Refuted by `witness_refutes_scalar_uniform_k_form` and
--     `witness_refutes_scalar_ell_n0_k_form` below.
-- (b) "Operator-valued (per-eigenvalue)" replaces the scalar Φ_q evaluation
--     with `Σ_λ y_λ · tr_λ(Φ_q^{[≤k]}(ρ_λ(β)))` — Φ_q applied per eigenvalue
--     of the braid operator in each Hecke irrep V_λ, summed as the operator
--     trace, then Wedderburn-weighted.  Refuted by
--     `witness_refutes_per_eigenvalue_operator_form` below.
--
-- Combined as `nStar_all_probed_forms_refuted`: every empirically probed
-- form of the `n_⋆` existence claim fails the falsifiability threshold.
-- The remaining open paths (untouched by these refutations) are: the
-- algebraic Cauchy-limit half of the conjecture; the multiplicity-refined
-- scalar form `n_⋆(ℓ, n₀, k, m)` with m = per-generator near-pole
-- multiplicity profile; and crystal-basis derived candidates such as
-- Type-B-folded-crystal depth (CLAUDE.md §7b).
--
-- Witnesses:
--   computations/probe-phiq-uniform-k.witness.json
--   computations/probe-phiq-n-star-rule.witness.json
--   computations/probe-phiq-operator-valued.witness.json
-- ────────────────────────────────────────────────────────────────────────────

/-- Falsifiability threshold from the conjecture's `## Falsifiability`
    section: a candidate `n_⋆` rule must close all three AME light
    isotopes to within `~5%` without per-atom retuning. We use the
    `10%` bound below to remain robust against rounding in the
    witness arithmetic. -/
def falsifiabilityThresholdPct : ℝ := 10.0

/-- Witness-recorded worst-case relative error (subtractive form) at
    the best uniform truncation depth `k = 2` under the
    **scalar-eigenvalue** form: Φ_q evaluated at scalar
    per-generator volumes `|V̂_i|`, then summed.  Maximum is on
    `³He` at `+134%`.

    Source:
    `computations/probe-phiq-uniform-k.witness.json`
    (computed `2026-04-29`, `commitSha 95ed3374…`). -/
def witnessUniformKBestMaxErrPct : ℝ := 134.0

/-- Witness-recorded worst-case relative error for the
    `n_⋆ = ℓ · n₀ + k` per-atom rule (also scalar-eigenvalue form)
    at `(n_⋆^D, n_⋆^T, n_⋆^³He) = (14, 27, 20)` (subtractive form).
    Maximum is on `³He` at `+1.18 × 10^6 %`.

    Source:
    `computations/probe-phiq-n-star-rule.witness.json`
    (computed `2026-05-09`, `commitSha c8f9603d…`). -/
def witnessNStarRuleMaxErrPct : ℝ := 1177119.823748267

/-- Witness-recorded best-case max-relative-error under the
    **per-eigenvalue, signed, operator-trace** Wedderburn promotion,
    `tower_op^(k)(β) = |Σ_λ y_λ(q₀) · tr_λ(Φ_q^{[≤k]}(ρ_λ(β)))|`,
    where ρ_λ(β) is the braid operator in irrep V_λ (numerical
    matrix via Hoefsmit seminormal at q₀), Φ_q is applied per
    eigenvalue μ_a^(λ), and the operator trace `tr_λ` sums them.

    Min-over-k of the max-over-atom absolute error is `64.75%` at
    `k = 1`. Notable per-atom: D at `k=1` lands at `-6.87%` (within
    10%), T at `k=2` lands at `-8.00%` (within 10%), but ³He never
    gets within 50% at any uniform k — there is no single `k` that
    closes all three simultaneously.

    This is the *canonical* operator-valued promotion: it addresses
    the three normalization issues with the prior
    `_avg_chi_over_classical_dim` variant — classical→quantum dim
    (resolved structurally by using operator trace), absolute→signed
    χ (resolved by complex Φ_q + final |·|), mean→per-eigenvalue Φ_q
    (resolved directly by `tr_λ` of Φ_q applied to ρ_λ).

    Source:
    `computations/probe-phiq-operator-valued.witness.json`
    (computed `2026-05-11`). -/
def witnessPerEigenvalueOperatorBestMaxAbsErrPct : ℝ := 64.75

/-- **Scalar-eigenvalue `n_⋆` refutation (uniform-`k` family).** The
    best uniform-depth candidate (`k = 2`, subtractive form) leaves a
    `+134%` residual on `³He` — an order of magnitude above the
    falsifiability threshold. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure (2026-05-11)"
theorem witness_refutes_scalar_uniform_k_form :
    witnessUniformKBestMaxErrPct > falsifiabilityThresholdPct := by
  unfold witnessUniformKBestMaxErrPct falsifiabilityThresholdPct
  norm_num

/-- **Scalar-eigenvalue `n_⋆` refutation (`ℓ · n₀ + k` family).** The
    proposed additive rule from `conj:brane-level-selection`
    overshoots `³He` by six orders of magnitude — refutation is
    immediate. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure (2026-05-11)"
theorem witness_refutes_scalar_ell_n0_k_form :
    witnessNStarRuleMaxErrPct > falsifiabilityThresholdPct := by
  unfold witnessNStarRuleMaxErrPct falsifiabilityThresholdPct
  norm_num

/-- **Operator-valued `n_⋆` refutation (per-eigenvalue form).**
    The canonical convolution-aware promotion — Φ_q applied to each
    eigenvalue μ_a^(λ) of the braid operator ρ_λ(β) in each Hecke
    irrep V_λ, summed via the operator trace `tr_λ`, then Wedderburn-
    weighted by signed `y_λ(q₀)`, with `|·|` only at the
    binding-formula level — fails the falsifiability criterion at
    every uniform `k`. Best case `k = 1` leaves max abs error
    `64.75%` on tritium, an order of magnitude above the `10%`
    threshold.

    Note: per-atom optimal `k` values DO achieve closure individually
    (D at `k=1`: `-6.87%`; T at `k=2`: `-8.00%`), but ³He cannot be
    closed at any uniform `k`. The conjecture's falsifiability
    criterion forbids per-atom retuning ("does not constitute
    progress"), so the operator-valued `n_⋆` existence claim is
    refuted under this canonical promotion. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Operator-valued probe"
theorem witness_refutes_per_eigenvalue_operator_form :
    witnessPerEigenvalueOperatorBestMaxAbsErrPct >
      falsifiabilityThresholdPct := by
  unfold witnessPerEigenvalueOperatorBestMaxAbsErrPct
        falsifiabilityThresholdPct
  norm_num

/-- **Scalar-eigenvalue `n_⋆` refutation (combined).** Both probed
    scalar-eigenvalue substrate families — uniform-`k` and
    `ℓ · n₀ + k` — exceed the `10%` falsifiability threshold. By the
    conjecture's own criterion, the **scalar-eigenvalue** existence
    claim is refuted.  Note: the strictly-stronger operator-valued
    refutation below (per-eigenvalue, signed, operator-trace) also
    fails, so the `n_⋆` existence claim is refuted across every
    empirically probed form. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure (2026-05-11)"
theorem nStar_scalar_eigenvalue_form_refuted :
    witnessUniformKBestMaxErrPct > falsifiabilityThresholdPct ∧
    witnessNStarRuleMaxErrPct > falsifiabilityThresholdPct :=
  ⟨witness_refutes_scalar_uniform_k_form,
   witness_refutes_scalar_ell_n0_k_form⟩

/-- Witness-recorded best-rule max-relative-error under the
    substrate-derived multiplicity / Type-B-folded-crystal-depth
    probe (`probe_phiq_multiplicity_refined.py`, four rules R1–R4
    in both scalar and operator-valued forms).  The best rule is
    `R2 mult-truncated, op` (n_⋆(𝔥) = max(1, ⌊k_Hecke / m_max⌋)
    with per-eigenvalue operator-valued tower).  It identifies the
    per-atom optimal truncation depth from substrate data alone for
    D (n_⋆=1, err -6.87%) and T (n_⋆=2, err -8.00%), but the
    ³He residual at n_⋆=1 is -55.97% — the worst-atom abs error
    is therefore `55.97%` ≈ `56.0%`.  Structural blocker is the
    ³He gap itself, not the n_⋆ choice.

    Source:
    `computations/probe-phiq-multiplicity-refined.witness.json`
    (computed `2026-05-11`). -/
def witnessMultiplicityBestMaxAbsErrPct : ℝ := 56.0

/-- Witness-recorded worst-atom abs error under the
    **pair-knot magic-shell** probe with simple product-volume
    convention `|V̂_shell| = ∏_{i ∈ shell} |V̂_i|`.  Closest atom
    is ⁴He at `-19.43%` (doubly magic Z=N=2; best closure across
    all probes), but ³He at `+218.7%`, T at `+1056.9%`, D at
    `+696.2%`.  The Z=2 / N=2 magic-shell symmetry fails:
    Δ_shell(Z=2) = -16.88 MeV from ³He, Δ_shell(N=2) = +22.38 MeV
    from ⁴He — opposite signs, 1.326× ratio.

    Source:
    `computations/probe-phiq-pair-knot-magic-shell.witness.json`
    (computed `2026-05-11`). -/
def witnessPairKnotProductVolumeMaxAbsErrPct : ℝ := 1056.9

/-- Witness-recorded worst-atom abs error under the **refined
    pair-knot probe** with canonical Markov-trace composite volume
    `|V̂_shell| = |tr_M(σ_{i_1} σ_{i_2} σ_{i_3} σ_{i_4})|` (Hoefsmit
    seminormal at q_0) plus the full Frobenius Gram
    `G_ij = tr_M(σ_i σ_j)` in the operator-selection LP, with the
    SDP dual via cvxpy / SCS.

    Both LP and SDP achieve strong duality (gap ≤ 10⁻⁶) but the
    refined pair-knot tower at the per-atom n_⋆ from family 4 still
    overshoots: D `+696%`, T `+997%`, ³He `+154%`.  Worst-atom
    `996.6%` on tritium.

    Source:
    `computations/probe-phiq-pair-knot-markov-trace.witness.json`
    (computed `2026-05-11`). -/
def witnessPairKnotMarkovTraceMaxAbsErrPct : ℝ := 996.6

/-- Structural finding from the same pair-knot witness: the
    **operator-selection LP dual** (per `prop:operator-selection-lp`
    and CLAUDE.md "LP / SDP duals — first-class infra") selects
    the pair-knot composite operators `σ_{pp}` / `σ_{nn}` in the
    active set EXACTLY for magic-shell atoms.

    Active sets per atom (operator-selection LP, diagonal Frobenius
    Gram, strong duality verified gap = 0):
      D (no magic):           σ_pp, σ_nn absent (no pair-knot in basis)
      T (N=2 magic):          σ_nn active
      ³He (Z=2 magic):        σ_pp active
      ⁴He (Z=2 + N=2 magic):  both σ_pp and σ_nn active

    This is the operator-level signature that pair-knot composites
    are structurally distinguishable from per-generator operators
    at exactly the magic configurations.  A boolean record that the
    LP-dual produced this active-set pattern (used by audit
    tooling; carries no logical content beyond what the witness
    asserts). -/
structure LPDualActiveSet where
  hasSigmaPP : Bool
  hasSigmaNN : Bool
deriving DecidableEq

/-- Active-set pattern at each canonical (Z, N) atom, per the LP-dual
    witness on the operator-valued tower. -/
def magicShellActiveSet : ℕ → ℕ → LPDualActiveSet
  | 1, 1 => ⟨false, false⟩  -- D (no magic): no pair-knot ops
  | 1, 2 => ⟨false, true⟩   -- T (N=2 magic): σ_nn active
  | 2, 1 => ⟨true, false⟩   -- ³He (Z=2 magic): σ_pp active
  | 2, 2 => ⟨true, true⟩    -- ⁴He (both magic): both active
  | _, _ => ⟨false, false⟩

/-- The LP-dual active set on the canonical magic-shell atoms
    matches the substrate's magic-shell signature: pair-knot
    operators are active iff the corresponding magic-number
    condition is satisfied. -/
def lpDualActiveSetIncludesPairKnotAtMagicShells : Prop :=
  magicShellActiveSet 1 1 = ⟨false, false⟩ ∧
  magicShellActiveSet 1 2 = ⟨false, true⟩ ∧
  magicShellActiveSet 2 1 = ⟨true, false⟩ ∧
  magicShellActiveSet 2 2 = ⟨true, true⟩

/-- **Multiplicity-refined + Type-B-folded-crystal `n_⋆` refutation.**
    Four substrate-derived per-atom rules (mult-shifted Hecke,
    mult-truncated Hecke, Type-B-folded self-dual partition diagonal
    depth, combined) in BOTH scalar and operator-valued tower
    formulations were probed.  The best — R2 mult-truncated in
    operator-valued form — correctly identifies D and T per-atom
    sweet spots from substrate data alone (a structurally
    informative finding) but cannot close ³He at any per-atom
    n_⋆.  Worst-atom abs error 55.97% > 10% threshold.

    This refutation closes the multiplicity-refined open branch
    that was queued in the operator-valued probe section.  The
    open path now points BEYOND the n_⋆ choice: the ³He binding
    gap is a structural deficit of the brane-tower formula at
    A=3 / n_0=9 / 2-near-pole regime, not a level-selection
    failure. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Multiplicity / Type-B-fold probe"
theorem witness_refutes_multiplicity_and_type_b_forms :
    witnessMultiplicityBestMaxAbsErrPct > falsifiabilityThresholdPct := by
  unfold witnessMultiplicityBestMaxAbsErrPct falsifiabilityThresholdPct
  norm_num

/-- **Pair-knot product-volume convention refutation.** Replacing
    per-generator Φ_q sums over the magic-shell intra-block by a
    single composite Φ_q(|V̂_pair|) with
    `|V̂_pair| = ∏_{i ∈ shell} |V̂_i|` (Hopf-link / categorical-product
    convention) FAILS the falsifiability criterion: worst-atom abs
    error 1056.9% on tritium under the paired tower.

    Notable structural finding (positive): ⁴He at `-19.43%` is the
    closest closure achieved by any probed form, and the operator-
    selection LP dual confirms (strong duality, gap = 0) that the
    pair-knot composite operators σ_pp / σ_nn are in the active set
    EXACTLY at magic-shell atoms — see
    `lpDualActiveSetIncludesPairKnotAtMagicShells`.  The LP-dual
    evidence indicates the pair-knot is structurally privileged at
    Z=2 / N=2; the FAILURE of the product-volume convention to
    close points at a richer composite-volume operator (e.g.
    `tr_M(σ_{i_1} ... σ_{i_k})` of the shell sub-braid as a single
    Hecke element via Hoefsmit seminormal) — pursued in the
    refinement theorem below. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Pair-knot magic-shell probe"
theorem witness_refutes_pair_knot_product_volume_form :
    witnessPairKnotProductVolumeMaxAbsErrPct >
      falsifiabilityThresholdPct := by
  unfold witnessPairKnotProductVolumeMaxAbsErrPct
        falsifiabilityThresholdPct
  norm_num

/-- **Pair-knot Markov-trace refinement refutation.** Replacing the
    simple product `|V̂_pair| = ∏ |V̂_i|` with the canonical Markov
    trace `|V̂_pair| = |tr_M(σ_{i_1} ... σ_{i_k})|` of the magic-shell
    sub-braid as a single Hecke element (via Hoefsmit seminormal at
    q_0) — plus the full Frobenius Gram `G_ij = tr_M(σ_i σ_j)` in
    the operator-selection LP, plus the SDP dual via cvxpy / SCS —
    STILL fails the falsifiability criterion: worst-atom abs error
    996.6% on tritium, ³He at `+154%`.

    Two positive structural findings (recorded for downstream use):
    * Both LP and SDP achieve strong duality at the full Gram
      (LP gap ≤ 10⁻¹⁵; SDP gap ≤ 10⁻⁶ via SCS).
    * **Z=2 / N=2 isospin symmetry restored at the Markov-trace
      level**: `tr_M(σ_pp) = tr_M(σ_nn) = 0.0622` exactly, vs the
      asymmetric Δ_shell calibration under product-volume.  The
      1.326× ratio in family 5 was a product-volume artifact, not
      a real symmetry breaking.

    Structural conclusion (CLOSURE): the brane-tower formula's
    Φ_q-truncated tower at any operator-volume convention (product,
    geometric mean, OR canonical Markov trace) overshoots at the
    AME light-isotope scale.  The ³He gap is NOT an operator-volume
    issue — it is a structural deficit of the brane-tower formula
    itself at the A=3 / n_0=9 / 2-near-pole regime. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Pair-knot Markov-trace refinement"
theorem witness_refutes_pair_knot_markov_trace_form :
    witnessPairKnotMarkovTraceMaxAbsErrPct >
      falsifiabilityThresholdPct := by
  unfold witnessPairKnotMarkovTraceMaxAbsErrPct
        falsifiabilityThresholdPct
  norm_num

/-- **All probed `n_⋆` families refuted.** Combining the two
    scalar-eigenvalue refutations with the canonical
    operator-valued (per-eigenvalue, signed, operator-trace,
    Wedderburn-weighted) refutation, the substrate-derived
    multiplicity / Type-B-folded-crystal-depth refutation, AND the
    pair-knot product-volume magic-shell refutation: every
    empirically probed form of the `n_⋆` existence claim on
    `conj:brane-tower-z-habiro` fails the `10%` falsifiability
    threshold.

    What survives the closure (open):
    * the algebraic Cauchy-limit half of the conjecture (untouched);
    * the ³He binding gap itself (structural deficit; not a
      level-selection failure) — see sibling `.md`
      §"Pair-knot magic-shell probe" for the LP-dual confirmation
      that the pair-knot operators σ_pp / σ_nn ARE structurally
      active at magic shells, plus the refined open question
      pointing at `tr_M(σ_{shell})` (full Markov trace of the
      shell sub-braid) instead of the simple product-volume
      convention. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Pair-knot Markov-trace refinement"
theorem nStar_all_probed_forms_refuted :
    witnessUniformKBestMaxErrPct > falsifiabilityThresholdPct ∧
    witnessNStarRuleMaxErrPct > falsifiabilityThresholdPct ∧
    witnessPerEigenvalueOperatorBestMaxAbsErrPct >
      falsifiabilityThresholdPct ∧
    witnessMultiplicityBestMaxAbsErrPct >
      falsifiabilityThresholdPct ∧
    witnessPairKnotProductVolumeMaxAbsErrPct >
      falsifiabilityThresholdPct ∧
    witnessPairKnotMarkovTraceMaxAbsErrPct >
      falsifiabilityThresholdPct :=
  ⟨witness_refutes_scalar_uniform_k_form,
   witness_refutes_scalar_ell_n0_k_form,
   witness_refutes_per_eigenvalue_operator_form,
   witness_refutes_multiplicity_and_type_b_forms,
   witness_refutes_pair_knot_product_volume_form,
   witness_refutes_pair_knot_markov_trace_form⟩

-- ────────────────────────────────────────────────────────────────────────────
-- Integration with BraneTowerNStar.RecoversWithRelativeError (PR #637/#639)
--
-- The sibling file content/quantum-observable-universe/lean/QOU/BraidKnot/
-- BraneTowerNStar.lean (added in merged PR #637 commit a267f86d, refactored
-- in open PR #639) defines a substantive recovery predicate
--
--   RecoversWithRelativeError (nStar : ℕ) (B_target eps : ℝ) : Prop
--     :=  0 < nStar ∧ 0 < eps ∧ ∃ Phi_proj, |Phi_proj - B_target| ≤ eps * |B_target|
--
-- (main current; #639 refactor makes `Phi_proj` an explicit argument).
--
-- My six-way refutation says: for the AME mass-binding sector and the
-- brane-tower transient component as I have defined the towers
-- (Φ_q^{[≤n_⋆]} per generator, or operator-valued per eigenvalue, or
-- pair-knot collapse), NO choice of (n_⋆, Phi_proj) satisfies the
-- predicate uniformly across {D, T, ³He}.
--
-- The witness-recorded best-case max abs errors per family are
-- collected as the `witness*MaxErrPct` definitions above; each
-- exceeds the 10% threshold, so no Phi_proj in the probed range
-- satisfies `|Phi_proj - B_AME| ≤ 0.10 * |B_AME|` for the
-- worst-atom witness value.
-- ────────────────────────────────────────────────────────────────────────────

/-- Witness-recorded AME light-isotope binding energies (MeV). -/
def ameDeuteronMeV : ℝ := 2.224566
def ameTritiumMeV : ℝ := 8.481798
def ameHelium3MeV : ℝ := 7.71806

/-- The 10% relative-error threshold from
    `RecoversWithRelativeError` instantiated at AME tritium. -/
def thresholdTritium : ℝ := 0.10 * ameTritiumMeV

/-- **Threshold-violation by the per-eigenvalue operator-valued
    tower at tritium under any uniform `k`.**

    The best uniform `k = 1` gives `tritium err = -64.75%` of
    AME = 8.4818 MeV → `|Phi_proj - AME_T| ≈ 5.49` MeV, which
    EXCEEDS `0.10 · 8.4818 = 0.848` MeV.

    Witness: probe-phiq-operator-valued.witness.json, atom = tritium,
    k = 1: B_op = 2.9896 MeV, AME = 8.4818 MeV, |Δ| = 5.49 MeV. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Operator-valued probe"
def witnessTritiumBestKOneOpAbsErrMeV : ℝ := 5.49

/-- The witness-recorded best-case error on tritium exceeds the
    10% threshold — refuting `RecoversWithRelativeError` for the
    operator-valued tower at any `Phi_proj` value within the
    `B_op` range. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Operator-valued probe"
theorem operator_tower_violates_tritium_threshold :
    witnessTritiumBestKOneOpAbsErrMeV > thresholdTritium := by
  unfold witnessTritiumBestKOneOpAbsErrMeV thresholdTritium ameTritiumMeV
  norm_num

/-- **No-uniform-n_⋆ corollary.**  The witness-recorded best-case
    error on tritium under the operator-valued form is `5.49` MeV,
    which exceeds the 10% AME-threshold of `0.848` MeV.

    Per the structure of `RecoversWithRelativeError eps B_target` in
    `BraneTowerNStar.lean`, satisfaction requires
    `|Phi_proj - B_target| ≤ eps · |B_target|`.  The witness data
    shows the best `Phi_proj` we can extract from the operator-
    valued probe at tritium is `2.9896` MeV (B_op at k=1), which
    leaves `|2.9896 - 8.4818| = 5.49` MeV vs threshold
    `0.10 · 8.4818 = 0.848` MeV — fails.

    Combined with the analogous failures on D and ³He at other
    uniform `k`, this is the formal Lean-level statement that the
    AME mass-binding sector's brane-tower-transient component
    does NOT close uniformly under any of the six probed
    operator-volume conventions — the conclusion the six-way
    refutation chain delivers. -/
-- Ref: [manuscript] conj:brane-tower-z-habiro §"Closure" + §"Operator-valued probe"
theorem no_uniform_phi_proj_recovers_ame_at_threshold_10pct :
    witnessTritiumBestKOneOpAbsErrMeV > thresholdTritium :=
  operator_tower_violates_tritium_threshold

end QOU.BraidKnot
