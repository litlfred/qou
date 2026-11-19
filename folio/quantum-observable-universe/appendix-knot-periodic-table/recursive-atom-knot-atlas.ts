import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:recursive-atom-knot-atlas",
  title:
    "Recursive atom-knot atlas at $q_0$ — elementary braids, Borromean nucleons, and three-dimensional $\\alpha$-simplicial nuclei",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.atomKnotAtlas",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "prop:fermion-boson-knot-link",
    "prop:confinement-sdp",
    // SDP-uniqueness wiring (2026-05-31): the atlas's per-atom T_w
    // canonical-knot identifications are certified at the abstract-
    // framework level by the parameterised SDP-uniqueness theorems
    // (PRs #1537/#1542/#1546). Each atlas entry's T_w uniqueness is
    // `qou:QOU.BraidKnot.nucleus_uniqueness_closed (3*A)`; named
    // wrappers exist at per-isotope (10), per-element (118), and
    // per-stable-isotope (252) granularities.
    "conj:canonical-knot-id-sdp",
  ],
  cites: ["wenzl1988"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_wave3_periodic_table_synthesis_probe.py",
    witness: [
      "computations/q-pinning-50-digit.witness.json",
      "computations/probes/nuclear-wave3-periodic-table-synthesis.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "atlas",
    "recursive",
    "atom-knot",
    "particle-registry",
    "q0",
    "braid-word",
    "markov-closure",
    "hyperbolic-knot",
    "appendix",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-05-31",
      body: "SDP-uniqueness wiring: `NucleusEmptySDPUniqueness` landed via PR #1537; the per-stable-isotope `StableIsotopeUniqueness.lean` was pending PR #1542.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** Every `ℝ` in the Lean sibling's atlas-entry " +
        "record is a measured or geometric magnitude: `vol_hyp` (the " +
        "**hyperbolic volume** of the knot closure — a transcendental period), " +
        "`m_pred_MeV` and `m_AME_MeV` (masses in MeV, the latter straight from " +
        "**AME2020**), and `err_pct` / `err_ppb` (residuals against that " +
        "measurement). §7c lists hyperbolic volume and experimental values as " +
        "`ℝ` rows explicitly. The categorical side of each entry — the " +
        "canonical Hecke element `T_w` in σ-generators, and its Markov " +
        "closure — carries no `ℝ`; the atlas is precisely the table where the " +
        "archimedean functor has already been applied, so the specialisation " +
        "is the point of the block.",
    },
  ],
});
