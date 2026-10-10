import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:operator-selection-lp",
  label: "rem:sdp-degeneracy-at-metallic-coincidence",
  title:
    "SDP degeneracy at cost-coincidence detects the metallic-ratio ladder",
  tags: [
    "metallic-ratio",
    "lp-degeneracy",
    "sdp-strict-complementarity",
    "active-set",
    "color-flavor-locking",
    "cfl-transition",
    "lean-proved",
  ],
  uses: [
    "prop:operator-selection-lp",
    "prop:confinement-sdp",
    "conj:color-superconductivity-borromean",
  ],
  cites: [],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-09",
      body:
        "Surfaced by the metallic-q probe series on PR #2047.  Lean " +
        "proof of the silver case is sorry-free in " +
        "`QOU.AlgebraicSubstrate.MetallicLPIdentities.silver_lp_coincidence`. " +
        "The §3b-cond classes `SDPDegeneracyDetectsMetallic` and " +
        "`CSCSilverIsCFLTransition` make the higher-n generalisation " +
        "and the physical CFL identification explicit.",
    },
  ],
});
