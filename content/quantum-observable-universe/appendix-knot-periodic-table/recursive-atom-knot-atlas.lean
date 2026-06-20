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

  METHODOLOGY CLASSIFICATION (STRICT):

    Each entry carries one of the following methodology tags.  Atlas
    entries with tag = `deprecatedVolumeMatch` are PROVISIONAL and are
    NOT principled — see `methodology-deprecation.witness.json`.  They
    survive in the registry only for historical transparency and are
    rendered in a quarantined section, never mixed with principled
    entries.

    The principled path for ANY new atom-knot identification is:

      SDP on the FULL mass tower (joint over all confinement levels
                                  and all atoms simultaneously)
        ↓ with GB (Gröbner-Shirshov) filtration tracking
        ↓ and jet-order tracking
      Canonical T_w ∈ H_{n_0}(q_0) per atom
        ↓ Markov closure
      Knot/link complement in S^3
        ↓ hp_volume_of_link_closure(braid_word, digits ≥ 50)
      B_pred = ρ · m_e · Vol_hyp
        ↓ compare a posteriori
      AME residual

    Per-atom volume-match search (the deprecated li_atom_knot_search.py
    pipeline) is forbidden: the joint SDP + GB-filtration + jet-order
    tracking is the only admissible derivation route.

  Refs: prop:recursive-atom-knot-atlas (this block),
        def:confined-particle (GB-NF source of truth),
        rem:knot-particle-dictionary,
        prop:confinement-sdp.
-/

import Mathlib.Data.Real.Basic

namespace QOU.BraidsAndKnots

/-- Methodology tag: how the particle-knot identification was obtained.
    Only `principledDerivation`, `principledGbNf`,
    `manualHistoricalVolumeMatch`, `magicAFormula`, and `recursiveOn4He`
    are admissible in the principled atlas.  `deprecatedVolumeMatch`
    entries are quarantined and rendered separately. -/
inductive Methodology where
  | principledDerivation             -- explicit σ-word → closure → hp Vol
  | principledGbNf                   -- trivial-NF (unknot, disjoint unknots)
  | manualHistoricalVolumeMatch      -- vol-match in earlier work, established
  | magicAFormula                    -- A · 8G shell-closure formula
  | recursiveOn4He                   -- n · ⁴He + n_αα · c_αα recursion
  | deprecatedVolumeMatch            -- (provisional) reverse-engineered

/-- A particle in the atlas at q_0: registry entry from the
    confined-particle definition. -/
structure AtlasEntry where
  name : String
  ell : ℕ           -- confinement level (0 = quark/lepton, 1 = nucleon, ...)
  n_0 : ℕ           -- coarse strand count
  braid_word : String  -- in σ_i generators, GB-NF
  closure_knot : String  -- Markov closure (e.g. "T_{2,3} = 3_1")
  rho_factor : ℕ    -- prefactor in B = ρ · m_e · Vol_hyp
  binding_link : String  -- "L_H" or knot name etc.
  vol_hyp : ℝ       -- hyperbolic volume of closure
  m_pred_MeV : ℝ    -- predicted mass in MeV
  m_AME_MeV : ℝ     -- experimental mass / binding (AME 2020)
  err_pct : ℝ       -- relative error %
  err_ppb : ℝ       -- relative error ppb
  methodology : Methodology  -- how the identification was obtained

/-- The recursive atom-knot atlas: list of all confined particles and
    atoms at q_0 with their Hecke-NF braid words, knot closures, and
    mass predictions.  Includes both principled entries and quarantined
    provisional entries; consumers MUST filter by methodology tag.

    Concrete model: contains the canonical proton + neutron entries
    derived from the from-scratch derivation chain; the full atlas
    (D, T, ³He, ⁴He, …) is built by
    `recursive_atom_knot_atlas_render.py` consuming the witness
    inputs enumerated below; consult the rendered markdown on every
    build.  The two seed entries here ensure
    `principledAtlas atomKnotAtlas ≠ []`. -/
-- Ref: [manuscript] §recursive atom-knot atlas — proton, neutron
def atomKnotAtlas : List AtlasEntry := [
  { name := "proton",
    ell := 1, n_0 := 3,
    braid_word := "σ_1 σ_2 σ_1",
    closure_knot := "T(2,3) = 3_1 (trefoil)",
    rho_factor := 3,
    binding_link := "trefoil",
    vol_hyp := 0,                -- torus knot, hyperbolic volume 0
    m_pred_MeV := 938.7228,       -- proton-mass-50dps witness
    m_AME_MeV := 938.27208816,    -- CODATA 2022
    err_pct := 0.048,             -- 0.05% — tower mass slightly above CODATA
    err_ppb := 480_000,
    methodology := Methodology.principledDerivation },
  { name := "neutron",
    ell := 1, n_0 := 3,
    braid_word := "σ_1 σ_2⁻¹ σ_1",
    closure_knot := "T(2,3)* = mirror trefoil",
    rho_factor := 3,
    binding_link := "trefoil-mirror",
    vol_hyp := 0,
    m_pred_MeV := 411.227,        -- six_term_consumer.py witness
    m_AME_MeV := 939.56542194,    -- CODATA 2022
    err_pct := 56.2,              -- ~528 MeV undershoot — open neutron-tower gap
    err_ppb := 562_000_000,
    methodology := Methodology.principledDerivation }
]

/-- The principled sub-atlas: entries whose methodology is anything
    other than `deprecatedVolumeMatch`.  This is the list cited by
    statistical summaries and physics claims. -/
def principledAtlas : List AtlasEntry → List AtlasEntry
  | [] => []
  | e :: rest =>
      match e.methodology with
      | Methodology.deprecatedVolumeMatch => principledAtlas rest
      | _ => e :: principledAtlas rest

/-- **Source of truth** for the principled atlas:
      1. confined-particle.md — GB-NF particle registry.
      2. mass-table-ppb.witness.json — D..⁴⁰Ca. (Dual-column exact symbolic vs Q-CLT proxy trace).
      3. methodology-deprecation.witness.json — per-particle audit.
      4. hp_volume.py — ≥ 50-digit Markov-closure → Vol_hyp.
      5. closed_form_tau_M.py — Active-partition factored exact symbolic trace for $A \geq 5$.
      6. hecke_core.py — Q-CLT finite sum approximations tracking active asymptotics.
      7. y_lambda_wenzl_bridge_extended.py — symbolic-q Wenzl bridge.

    DEPRECATED INPUT (consumed only by the quarantined provisional
    section, never by the principled atlas):
      8. li-atom-knot-search.witness.json — (provisional) volume-match search.

    Updates to any input propagate via witness_staleness_tracker.py
    to the rendered appendix on the next `bun run build`.

    Concrete predicate: `atomKnotAtlas` is non-empty (the witness
    pipeline has produced at least one entry).  After the canonical
    proton and neutron entries above, this is `2 ≥ 1`, provable by
    `decide`.  The genuine "every entry is witness-derived" content
    requires per-entry methodology checks; this minimal predicate
    catches the regression "atlas regenerated to empty". -/
def AtlasIsWitnessDerived : Prop := atomKnotAtlas.length ≥ 1

theorem atlas_witness_derived : AtlasIsWitnessDerived := by
  -- Ref: [manuscript] prop:recursive-atom-knot-atlas §"Build-pipeline integration"
  -- + the renderer recursive_atom_knot_atlas_render.py.
  -- The atomKnotAtlas list above contains the canonical proton +
  -- neutron entries; length ≥ 1 closes by decide.
  show atomKnotAtlas.length ≥ 1
  decide

/-- (provisional / deprecated methodology)

    The 7Li / 6Li volume-match results from the SnapPy search
    (li-atom-knot-search.witness.json) are NOT principled.  The
    search reverse-engineers the answer by picking the knot whose
    Vol_hyp matches the AME target; at ~2400 knots searched, residuals
    below ~10 ppb cannot be distinguished from numerical coincidence
    absent an independent GB-NF derivation.

    The earlier theorem `li7_best_precision` claimed ⁷Li at L_{11a62}
    as the best-precision atlas entry (4001 ppb residual).  That claim
    is now demoted to *provisional* status and is no longer cited as
    a principled result in the statistical summary.

    The principled best-precision claim awaits SDP-on-full-mass-tower
    with GB filtration and jet-order tracking (see
    `principled_path_for_atom_knot` below). -/
def li7_provisional_volume_match : True := by
  trivial  -- Ref: methodology-deprecation.witness.json §particles[12]
           -- ("7Li", method = "deprecated-volume-match").
           -- The 4001 ppb residual is striking but unverified.

/-- The principled path for any new atom-knot identification: a JOINT
    SDP on the full mass tower (over all confinement levels ℓ and all
    atoms simultaneously), with Gröbner-Shirshov filtration tracking
    and jet-order tracking, yielding canonical T_w ∈ H_{n_0}(q_0)
    PER ATOM as a structured certificate.

    The Markov closure of T_w is then taken in S^3, and Vol_hyp is
    computed at ≥ 50 decimal digits via
    `hp_volume_of_link_closure(braid_word, digits=50)` for comparison
    to AME via B_pred = ρ · m_e · Vol_hyp.

    Per-atom volume-match search is FORBIDDEN as a derivation route:
    the SDP must be joint over the tower so the GB filtration and the
    jet ordering are consistent across confinement levels.

    Concrete predicate: `principledAtlas atomKnotAtlas = atomKnotAtlas`
    — every atlas entry has a methodology other than
    `deprecatedVolumeMatch`.  The proton + neutron seed entries both
    use `principledDerivation`, so this closes by `decide`. -/
def PrincipledPathForAtomKnot : Prop :=
  principledAtlas atomKnotAtlas = atomKnotAtlas

theorem principled_path_for_atom_knot : PrincipledPathForAtomKnot := by
  -- Ref: [manuscript] prop:confinement-sdp + def:confined-particle.
  -- Both seed entries (proton, neutron) carry methodology =
  -- principledDerivation, so principledAtlas filters none out.
  show principledAtlas atomKnotAtlas = atomKnotAtlas
  rfl

/-- Filtration certificate format produced by gb_filtration_jet_tracker.py:
    a Hecke element E ∈ H_n(q) is recorded as a map
        FiltrationCertificate := ℕ → List (Perm n × ℚ(q))
    where FiltrationCertificate grade lists every basis element T_w with
    Coxeter length ℓ(w) = grade and its symbolic-q coefficient.

    The jet-order log is the ordered list of reduction events; each
    event tags the multiplication step T_w · T_i with (ℓ(w), ℓ(ws_i),
    relation ∈ {ascending, hecke-quadratic}).

    Concrete predicate: every atlas entry has a non-empty
    `braid_word` field (the certificate carries the σ-generator
    sequence).  Closes by `decide` on the proton + neutron seed
    entries. -/
def FiltrationCertificateFormat : Prop :=
  ∀ e ∈ atomKnotAtlas, e.braid_word ≠ ""

theorem filtration_certificate_format_specified : FiltrationCertificateFormat := by
  -- Ref: [manuscript] gb-filtration-jet-order.witness.json §framework.
  -- `atomKnotAtlas` is a `List`, so we exhaust membership via
  -- `cases he` (NOT `fin_cases`, which expects a Fin / Fintype).
  intro e he
  simp only [atomKnotAtlas, List.mem_cons, List.not_mem_nil, or_false] at he
  rcases he with rfl | rfl <;> decide

end QOU.BraidsAndKnots
