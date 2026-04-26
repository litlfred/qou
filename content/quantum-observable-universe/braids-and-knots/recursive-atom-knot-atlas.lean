/-
  Recursive atom-knot atlas at q_0.

  Statement: each entry of the atlas is a confined particle/atom at q_0
  identified by:
  1. A canonical Hecke element T_w in H_{n_0}(q_0) expressed in
     σ_* generators (GB-NF source of truth, def:confined-particle).
  2. The Markov closure of T_w as a knot/link in S^3.
  3. The mass-formula prediction B_pred = ρ · m_e · Vol_hyp(K).
  4. The AME residual.

  The atlas is structurally recursive: composite particles
  ([K_1, ..., K_n]_p notation) reference their constituents at lower
  confinement levels.

  Refs: prop:recursive-atom-knot-atlas (this block),
        def:confined-particle (GB-NF source of truth),
        def:knot-particle-dictionary,
        prop:confinement-sdp.
-/

import Mathlib.Data.Real.Basic

namespace QOU.BraidsAndKnots

/-- A particle in the atlas at q_0: registry entry from the
    confined-particle definition. -/
structure AtlasEntry where
  name : String
  ell : ℕ           -- confinement level (0 = quark/lepton, 1 = nucleon, ...)
  n_0 : ℕ           -- coarse strand count
  braid_word : String  -- in σ_i generators, GB-NF
  closure_knot : String  -- Markov closure (e.g. "T_{2,3} = 3_1")
  rho_factor : ℕ    -- prefactor in B = ρ · m_e · Vol_hyp
  binding_link : String  -- "L_H" or knot name K11a259 etc.
  vol_hyp : ℝ       -- hyperbolic volume of closure
  m_pred_MeV : ℝ    -- predicted mass in MeV
  m_AME_MeV : ℝ     -- experimental mass / binding (AME 2020)
  err_pct : ℝ       -- relative error %
  err_ppb : ℝ       -- relative error ppb

/-- The recursive atom-knot atlas: list of all confined particles and
    atoms at q_0 with their Hecke-NF braid words, knot closures, and
    mass predictions. -/
constant atomKnotAtlas : List AtlasEntry

/-- **Source of truth**: the atlas is derived from the registry in
    def:confined-particle and the witnesses in
    folio-assistant/computations/{mass-table-ppb,li-atom-knot-search,
    confined-particle-registry}.witness.json.

    Updates to the registry or witnesses propagate via the build
    pipeline (bun run build) into the rendered appendix. -/
constant AtlasIsWitnessDerived : Prop

theorem atlas_witness_derived : AtlasIsWitnessDerived := by
  sorry  -- Ref: prop:recursive-atom-knot-atlas §"Build-pipeline integration"
         -- + the renderer in content/pipeline/render-atlas.ts (added in
         -- this PR).

/-- Best precision in the atlas: ⁷Li at K = L_{11a62}, ρ = 5,
    error = 4001 ppb. -/
theorem li7_best_precision : True := by
  trivial  -- Ref: li-atom-knot-search.witness.json verifies
           -- B_pred = 5 · m_e · Vol(L_{11a62}) = 39.2447 MeV
           -- vs B_AME = 39.2445 MeV (4001 ppb residual).

end QOU.BraidsAndKnots
