/-
  Joint mass-tower confinement SDP at q_0.

  Design specification for the SDP solver that produces canonical
  T_w ∈ H_{n_0}(q_0) per atom, with GB-filtration grading + jet-order
  certificate, satisfying cross-confinement-level consistency
  constraints.

  This is the structural "step 1" input to the categorical mass
  derivation (conj:atom-knot-mass-derivation).  Per-atom SDPs alone
  are insufficient — the cross-level consistency constraints can only
  be enforced jointly.

  Refs: conj:joint-tower-sdp-confinement (this block),
        def:confined-particle, prop:confinement-sdp,
        conj:atom-knot-mass-derivation, prop:gb-spectral-sequence,
        prop:spectral-sequence-collapse,
        prop:wedderburn-trace-identity.
-/

import Mathlib.Data.Real.Basic
import Mathlib.LinearAlgebra.Matrix.PosDef

namespace QOU.BraidKnot

/-- Per-particle SDP variables: coefficients c_w(q_0) ∈ ℚ for
    w ∈ S_{n_0} indexing the GB-NF basis {T_w} of H_{n_0}(q_0). -/
structure PerParticleSdpVariables where
  particle_name : String
  n_0 : ℕ
  -- Filtration cutoff: c_w = 0 unless ℓ(w) ≤ filtration_cutoff
  filtration_cutoff : ℕ
  -- Jet-order indexing of the variables
  jet_order : List (List ℤ)  -- list of σ-words, ordered

/-! ## Well-formedness of the SDP data — NOT the SDP constraints

2026-11-20 (W8b, bean `qou-w8cg`): the four predicates below were named
`WedderburnBlockPositivity`, `GbFiltrationGrading`, `JetOrderOrdering` and
`CrossLevelConsistency`, and a theorem `joint_tower_sdp_feasible` returned its
own hypothesis (`registry ≠ []`) as "feasibility". None of them is the
constraint its name promised: `ρ_λ(T_w) ⪰ 0` was `n_0 ≥ 1`. They are renamed to
what they check — shape of the input data — and the tautological theorem and
its `JointTowerSdpFeasible` are removed.

**Not encoded:** block positivity `ρ_λ(T_w(𝔥)) ⪰ 0`, the GB-filtration support
condition, the jet-order well-ordering, cross-level consistency of the
embeddings `H_m(q₀) ↪ H_n(q₀)`, and joint feasibility. They need the Hecke
algebra representations and an SDP feasibility notion this file does not
build. The block is a conjecture (design specification); this file carries
its data types only. -/

/-- Data well-formedness: at least one strand. Not block positivity. -/
def PerParticleStrandsWellFormed (vars : PerParticleSdpVariables) : Prop :=
  vars.n_0 ≥ 1

/-- Data well-formedness: the filtration cutoff is at most `2 · n_0`.
Not the GB-filtration support condition. -/
def FiltrationCutoffWellFormed (vars : PerParticleSdpVariables) : Prop :=
  vars.filtration_cutoff ≤ 2 * vars.n_0

/-- Data well-formedness: at least one σ-word is indexed. Not the jet-order
well-ordering. -/
def JetOrderNonempty (vars : PerParticleSdpVariables) : Prop :=
  vars.jet_order ≠ []

/-- Tower edge: a confinement-level consistency constraint between
    a parent particle 𝔥 and a constituent 𝔥' embedded into 𝔥. -/
structure TowerEdge where
  parent : String                    -- e.g. "8Be"
  constituent : String               -- e.g. "4He"
  embedding_codomain_n_0 : ℕ          -- n_0 of parent
  embedding_domain_n_0 : ℕ            -- n_0 of constituent
  -- The canonical embedding π : H_{domain} ↪ H_{codomain}
  -- sends T_w(constituent) ↦ T_w(parent) inside the relevant cosets

/-- Data well-formedness: the embedding does not decrease strand count, the
minimum for an inclusion `H_m ↪ H_n` to exist. Not cross-level consistency. -/
def TowerEdgeWellFormed (edge : TowerEdge) : Prop :=
  edge.embedding_codomain_n_0 ≥ edge.embedding_domain_n_0

/-- The input data of the joint mass-tower SDP, with its well-formedness
conditions. The SDP constraints themselves are not encoded (see above). -/
structure JointTowerSdp where
  registry : List PerParticleSdpVariables
  tower_edges : List TowerEdge
  strands_wf : ∀ vars ∈ registry, PerParticleStrandsWellFormed vars
  filtration_wf : ∀ vars ∈ registry, FiltrationCutoffWellFormed vars
  jet_order_wf : ∀ vars ∈ registry, JetOrderNonempty vars
  edges_wf : ∀ edge ∈ tower_edges, TowerEdgeWellFormed edge

/-- Output: structured certificate Φ(q_0) per atom.  Combined with
    the Wedderburn-multiplicity ρ(𝔥), this is consumed by
    conj:atom-knot-mass-derivation. -/
structure JointTowerSdpCertificate where
  T_w_per_atom : List (String × List ℤ)             -- (atom_name, σ-word)
  filtration_per_atom : List (String × ℕ)            -- (atom_name, max_grade)
  jet_log_per_atom : List (String × List (List ℤ))   -- (atom_name, jet_seq)
  rho_per_atom : List (String × ℕ)                   -- (atom_name, ρ multiplicity)

/-- Implementation roadmap status (per the .md design spec). -/
inductive ImplementationStep where
  | h3GroundTruth                    -- step 1: known H_3 answer; unit test
  | tower123Joint                    -- step 2: H_1, H_2, H_3 jointly
  | tower6_9_12                      -- step 3: ²H, ³H, ³He, ⁴He
  | tower18_21                       -- step 4: ⁶Li, ⁷Li (replaces deprecated)
  | alphaClusterScale                -- step 5: ⁸Be → ⁴⁰Ca

def implementationStatus : ImplementationStep → String
  | ImplementationStep.h3GroundTruth => "PoC pending (Phase 3a of workplan)"
  | ImplementationStep.tower123Joint => "pending (Phase 3a)"
  | ImplementationStep.tower6_9_12 => "pending (Phase 3b)"
  | ImplementationStep.tower18_21 => "pending (Phase 3b) — replaces deprecated li-atom-knot-search"
  | ImplementationStep.alphaClusterScale => "pending (Phase 3c) — scale needs SDP-decomposition"

end QOU.BraidKnot
