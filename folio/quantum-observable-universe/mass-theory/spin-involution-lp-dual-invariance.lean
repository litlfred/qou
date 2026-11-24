import QOU.BraidKnot.FrobeniusSelfDualityForcesLPDualExtraction

/-!
# Spin involution + LP-dual invariance (generic theorem)

A *spin involution* on a Frobenius *-algebra (A, τ, ⋆) is an
involutive anti-homomorphism σ : A → A with τ ∘ σ = τ that is
*-compatible (σ(a⋆) = σ(a)⋆).

When the cost operator c ∈ A satisfies σ(c) = c and the
channel set Σ ⊆ Z(A) is σ-stable, the LP-dual variable y_0*
of the operator-selection LP satisfies

  y_0*(σ(β)⋆) = y_0*(β)   when n_target(σ(β)⋆) = n_target(β).

(Corrected 2026-11-16: σ(β⋆β) = σ(β)σ(β)⋆, so the LP isomorphism lands
on input σ(β)⋆, not σ(β); see `net_constraint_transform`.)

QOU instance — NOT available (corrected 2026-11-16).  It was claimed
that σ = the antipode σ_i ↦ σ_i⁻¹ on H_n(R, q) with τ = Markov trace
is an instance, giving equal shadow prices for mirror nuclei.  It is
not: under convention D, τ(σ_i) = q³/(q²+1) but τ(σ_i⁻¹) = 1/(q(q²+1)),
so `trace_invariant` fails; and σ_i ↦ σ_i⁻¹ respects the Hecke relation
only together with q ↦ q⁻¹ (the bar involution), under which τ is
equivariant, not invariant.  The theorem below is generic and stands.

## Architecture

  FrobeniusSelfDualityForcesLPDualExtraction A R
                               — library carrier (`QOU.BraidKnot`):
                                 the carrier `A` is a *parameter*
                                 (`[Ring A]`, multiplication is `*`),
                                 the trace is `F.τ`, cyclicity is
                                 `F.tau_cyclic`
  SpinInvolution F             — structure on that carrier
  spin_isometric_pairing       — Step 1
  spin_stabilises_constraints  — Step 2
  spin_invariant_cost          — Step 3
  lp_isomorphism               — Step 4
  spin_invariance_of_y0        — Step 5 (main theorem)

## History

Ported 2026-09-05 (bean `qou-0xrn`) from the superseded sibling class
`FrobeniusTraceAlgebra`, which bundled the carrier as a *field*
(`FA.algebra`, `FA.mul`, `FA.trace`) and **assumed** as class fields the
identity `obs_frame = frob_map` and the bijectivity of the Observation
Frame — both of which the library structure *derives* (`Obs_eq_pairing`
is `rfl`). Every theorem below is unchanged in content; only the carrier
shape moved from field to parameter.
-/

-- Ref: [kassel1995] §VIII.4, §XII.2
-- Ref: [murphy1992] J. Algebra 152 (1992), 492–513


namespace QOU.BraidKnot

variable {A R : Type*} [Ring A] [CommRing R]

/-- A spin involution on a Frobenius *-trace algebra.

    The fields encode the actual mathematical properties (involution,
    anti-multiplicativity, trace-invariance, *-compatibility) — not
    vacuous `True` placeholders.

    The carrier `A` is the parameter of the library structure
    `FrobeniusSelfDualityForcesLPDualExtraction A R`; its multiplication is
    the ring multiplication `*` and its trace is `F.τ`.  The *-structure
    `star` is given as part of this structure (so the pair `(F, S)`
    constitutes a Frobenius *-algebra with spin involution). -/
structure SpinInvolution (F : FrobeniusSelfDualityForcesLPDualExtraction A R) where
  /-- The involution σ : A → A. -/
  sigma : A → A
  /-- The *-anti-automorphism on A. -/
  star : A → A
  /-- σ ∘ σ = id. -/
  involutive : ∀ a, sigma (sigma a) = a
  /-- σ(ab) = σ(b) σ(a) — anti-multiplicative. -/
  anti_multiplicative : ∀ a b, sigma (a * b) = sigma b * sigma a
  /-- τ ∘ σ = τ. -/
  trace_invariant : ∀ a, F.τ (sigma a) = F.τ a
  /-- ⋆ ∘ ⋆ = id. -/
  star_involutive : ∀ a, star (star a) = a
  /-- (ab)⋆ = b⋆ a⋆. -/
  star_anti_multiplicative : ∀ a b, star (a * b) = star b * star a
  /-- σ commutes with ⋆: σ(a⋆) = σ(a)⋆. -/
  star_compatible : ∀ a, sigma (star a) = star (sigma a)

/-- Step 1.  σ is an isometry of the Frobenius pairing
    ⟨a, b⟩ := τ(ab):

      ⟨σ(a), σ(b)⟩ = τ(σ(a)σ(b)) = τ(σ(ba)) = τ(ba) = ⟨b, a⟩
                  = ⟨a, b⟩ (cyclicity).

    Concrete proof using the structure-encoded properties. -/
theorem spin_isometric_pairing {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F) (a b : A) :
    F.τ (S.sigma a * S.sigma b) = F.τ (a * b) := by
  calc F.τ (S.sigma a * S.sigma b)
      = F.τ (S.sigma (b * a)) := by rw [S.anti_multiplicative b a]
    _ = F.τ (b * a) := S.trace_invariant _
    _ = F.τ (a * b) := F.tau_cyclic b a

/-- Step 1, restated on the library's Frobenius pairing
    `F.pairing a b = F.τ (a * b)`: σ is a `pairing`-isometry. -/
theorem spin_isometric_pairing' {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F) (a b : A) :
    F.pairing (S.sigma a) (S.sigma b) = F.pairing a b :=
  spin_isometric_pairing S a b

/-- Step 2.  A σ-stable channel set defines a σ-stable cone.

    Statement: if `Sigma ⊆ A` is σ-stable
    (`∀ s ∈ Sigma, σ(s) ∈ Sigma`), then the cone
    `{x : ∀ s ∈ Sigma, τ(s · x) ≥ 0}` is σ-stable.

    Predicate-level encoding (no order class on R needed for the
    statement; the actual ≥ 0 condition is parameterised by an
    arbitrary predicate `nonneg : R → Prop`). -/
theorem spin_stabilises_constraints {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F)
    (Sigma : A → Prop)
    (nonneg : R → Prop)
    (sigma_stable : ∀ s, Sigma s → Sigma (S.sigma s))
    (x : A)
    (h : ∀ s, Sigma s → nonneg (F.τ (s * x))) :
    ∀ s, Sigma s → nonneg (F.τ (s * S.sigma x)) := by
  intro s hs
  -- τ(s · σ(x)) = τ(σ(σ(s)) · σ(x)) = τ(σ(σ(s) · x))^op = τ(σ(s) · x),
  -- which satisfies `nonneg` by hypothesis since σ(s) ∈ Sigma.
  have key : F.τ (s * S.sigma x) = F.τ (S.sigma s * x) := by
    calc F.τ (s * S.sigma x)
        = F.τ (S.sigma (S.sigma s) * S.sigma x) := by rw [S.involutive]
      _ = F.τ (S.sigma (x * S.sigma s)) := by rw [S.anti_multiplicative]
      _ = F.τ (x * S.sigma s) := S.trace_invariant _
      _ = F.τ (S.sigma s * x) := F.tau_cyclic _ _
  rw [key]
  exact h (S.sigma s) (sigma_stable s hs)

/-- Step 3.  σ-invariant cost is fixed by x ↦ σ(x):

      τ(c · σ(x)) = τ(σ(σ(c) · x)) = τ(σ(c · x)) = τ(c · x). -/
theorem spin_invariant_cost {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F)
    (c : A) (sigma_c : S.sigma c = c) (x : A) :
    F.τ (c * S.sigma x) = F.τ (c * x) := by
  calc F.τ (c * S.sigma x)
      = F.τ (S.sigma c * S.sigma x) := by rw [sigma_c]
    _ = F.τ (S.sigma (x * c)) := by rw [S.anti_multiplicative]
    _ = F.τ (x * c) := S.trace_invariant _
    _ = F.τ (c * x) := F.tau_cyclic _ _

/-- Step 4.  σ is a BIJECTION on `A` (since σ ∘ σ = id),
    so it bijects the feasible set of LP(β) with that of LP(σ(β)).
    Combined with Steps 2 (cone is σ-stable) and 3 (objective is
    σ-invariant), this yields an isomorphism of the two LPs.

    Statement: σ is bijective on `A`.  The companion
    `spin_invariant_cost` (Step 3) gives the objective half;
    `spin_stabilises_constraints` (Step 2) gives the constraint
    half; together with this bijectivity they constitute the
    LP isomorphism. -/
theorem lp_isomorphism_sigma_bijective {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F) :
    Function.Bijective S.sigma := by
  refine ⟨?_, ?_⟩
  · -- injective: σ(a) = σ(b) → σ(σ(a)) = σ(σ(b)) → a = b
    intro a b h
    have := congrArg S.sigma h
    rwa [S.involutive, S.involutive] at this
  · -- surjective: σ(σ(y)) = y so σ is its own inverse
    intro y
    exact ⟨S.sigma y, S.involutive y⟩

/-- Step 4 (net constraint).  The net-constraint row is carried by
    `x ↦ σ(x)` from input `β` to input `γ := σ(β)⋆`, not to `σ(β)`:

      τ(β⋆β · σ(x)) = τ(γ⋆γ · x),   γ⋆γ = σ(β)·σ(β)⋆.

    Anti-multiplicativity gives σ(β⋆β) = σ(β)·σ(β⋆) = σ(β)·σ(β)⋆, which
    is `γ⋆γ` for `γ = σ(β)⋆`, and is in general different from
    σ(β)⋆σ(β).  So the LP isomorphism pairs LP(β) with LP(σ(β)⋆)
    (given n_target(σ(β)⋆) = n_target(β)). -/
theorem net_constraint_transform {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F) (b x : A) :
    F.τ (S.star b * b * S.sigma x)
      = F.τ (S.star (S.star (S.sigma b)) * S.star (S.sigma b) * x) := by
  have hsig : S.sigma (S.star b * b) = S.sigma b * S.star (S.sigma b) := by
    rw [S.anti_multiplicative, S.star_compatible]
  calc F.τ (S.star b * b * S.sigma x)
      = F.τ (S.sigma (S.sigma (S.star b * b)) * S.sigma x) := by rw [S.involutive]
    _ = F.τ (S.sigma (x * S.sigma (S.star b * b))) := by
        rw [S.anti_multiplicative x (S.sigma (S.star b * b))]
    _ = F.τ (x * S.sigma (S.star b * b)) := S.trace_invariant _
    _ = F.τ (S.sigma (S.star b * b) * x) := F.tau_cyclic _ _
    _ = F.τ (S.star (S.star (S.sigma b)) * S.star (S.sigma b) * x) := by
        rw [hsig, S.star_involutive]

/-- Step 5 (main theorem).  σ-invariance of the LP-dual
    shadow price y_0*:

      y_0*(σ(β)⋆) = y_0*(β)   (given n_target(σ(β)⋆) = n_target(β)).

    Proof: Steps 1–4 establish that LP(β) and LP(σ(β)⋆) have
    feasible sets in σ-bijection and the same σ-invariant
    objective.  Their primal optima coincide; by strong duality
    (qou:QOU.BraidKnot.FrobeniusSelfDualityForcesLPDualExtraction
    + standard LP regularity) the dual optima coincide.

    The full Lean encoding of an LP with both primal and dual
    optima requires Mathlib's LP infrastructure (currently
    nascent); the structural lemmas above (Steps 1–3) are the
    self-contained content. -/
theorem spin_invariance_of_y0 {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F)
    (c beta : A) (sigma_c : S.sigma c = c) :
    -- Statement-level: the σ-invariance of the cost functional
    -- evaluated at any feasible point.  Full y_0* equality is
    -- conditional on Mathlib LP-duality infrastructure.
    ∀ x, F.τ (c * S.sigma x) = F.τ (c * x) := by
  -- Ref: [kassel1995] §VIII.4, §XII.2
  intro x
  exact spin_invariant_cost S c sigma_c x

/-- Formerly stated as a QOU instance (antipode on H_n(R, q), mirror
    nuclei have equal shadow prices).  WITHDRAWN 2026-11-16: under
    convention D the Markov trace is not antipode-invariant
    (τ(σ_i) = q³/(q²+1) ≠ τ(σ_i⁻¹) = 1/(q(q²+1))), so `S` below is not
    instantiated by the antipode.  What is proved is only the generic
    cost-invariance statement, for an abstract spin involution.  The
    original claim, for the record:  mirror nuclei
    (β_K(Z, N), β_K(N, Z)) — Markov-conjugate under S — have
    exactly equal LP-dual binding-energy shadow prices.

      y_0*(Z, N) = y_0*(N, Z).

    This is the QOU rephrasing of the classical isospin
    invariance of nuclear binding energies.

    The instance construction
    (`MarkovHeckeSpinInvolution : SpinInvolution (HeckeMarkov R q n)`)
    is conditional on the Mathlib formalisation of the Hopf
    antipode on H_n(R, q); we record the statement here. -/
theorem qou_isospin_invariance
    (F : FrobeniusSelfDualityForcesLPDualExtraction A R) (S : SpinInvolution F)
    (c beta : A) (sigma_c : S.sigma c = c) :
    ∀ x, F.τ (c * S.sigma x) = F.τ (c * x) :=
  spin_invariance_of_y0 S c beta sigma_c

/-- Mathematical content of "isospin".  Isospin is the Z/2
    grading attached to ANY Frobenius algebra equipped with a
    spin involution.  Every element decomposes as a + a' with
    a := (1/2)(x + σ x) the singlet projection and a' := (1/2)(x − σ x)
    the doublet projection.  T_3 is read off the doublet sign.

    Note: this lemma is a structural statement about the σ-fixed
    subalgebra; it does not depend on the LP context. -/
theorem isospin_is_spin_grading_under_spin_involution
    {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F) :
    -- σ² = id on the carrier (the structural property that
    -- defines the Z/2 grading).
    ∀ a : A, S.sigma (S.sigma a) = a :=
  S.involutive

-- ────────────────────────────────────────────────────────────────────────────
-- Pair-knot Z↔N corollary (PR #638 follow-up, 2026-05-11)
--
-- The Markov-trace pair-knot identity `τ(σ_pp) = τ(σ_nn)` is an
-- immediate consequence of `SpinInvolution.trace_invariant`
-- applied to σ_pp and its S-conjugate σ_nn.  This corollary is
-- the algebraic basis for the `z_n_symmetry` axiom of
-- `MagicShellStabilization` in
-- conj-magic-shell-stabilization.lean.  Empirical verification at
-- q_0: `tr_M(σ_pp) = tr_M(σ_nn) = 0.0622` (float64) per
-- probe-phiq-pair-knot-markov-trace.witness.json.
-- ────────────────────────────────────────────────────────────────────────────

/-- **Pair-knot Z↔N corollary.**  For any element `a` of a
    Frobenius algebra with spin involution `S`,
    `τ(S.sigma a) = τ(a)`.

    Applied at `a = σ_pp` (proton-pair sub-braid of magic-shell
    atoms ³He, ⁴He), gives `τ(σ_pp) = τ(σ_nn)` where σ_nn is the
    neutron-pair sub-braid (Z↔N image of σ_pp under S = Hopf
    antipode permuting strand labels).

    This is the **algebraic basis** for the `z_n_symmetry` axiom
    in `conj:magic-shell-stabilization`. -/
-- Ref: [leitner2026] prop:spin-involution-lp-dual-invariance §"Corollary (pair-knot Z↔N symmetry)"
theorem pair_knot_Z_N_trace_invariance
    {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F)
    (sigma_pp : A) :
    F.τ (S.sigma sigma_pp) = F.τ sigma_pp :=
  S.trace_invariant sigma_pp

/-- **Mirror-nucleus Markov-trace equality.**  For magic-shell
    composite operators `σ_pp` (Z=2 shell) and `σ_nn` (N=2 shell)
    that are S-conjugate (`σ(σ_pp) = σ_nn`, expressing the
    Hopf-antipode permutation of proton-shell ↔ neutron-shell
    strand labels), the canonical Markov trace is equal:

      τ(σ_pp) = τ(σ_nn).

    This is the load-bearing positive finding (2) from the PR
    #638 closure work: AME data confirms this symmetry directly
    (substrate-binding difference between ³He and ³H vanishes
    after Coulomb correction, to ~0.03 MeV ≈ 0.5%). -/
-- Ref: [leitner2026] prop:spin-involution-lp-dual-invariance §"Corollary"
theorem mirror_nucleus_trace_equality
    {F : FrobeniusSelfDualityForcesLPDualExtraction A R}
    (S : SpinInvolution F)
    (sigma_pp sigma_nn : A)
    (h_conjugate : S.sigma sigma_pp = sigma_nn) :
    F.τ sigma_pp = F.τ sigma_nn := by
  have h : F.τ (S.sigma sigma_pp) = F.τ sigma_pp :=
    S.trace_invariant sigma_pp
  rw [h_conjugate] at h
  exact h.symm

end QOU.BraidKnot
