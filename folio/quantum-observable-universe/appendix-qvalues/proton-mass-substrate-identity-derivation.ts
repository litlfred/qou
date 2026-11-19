import { remark } from "../../schema/builders";

export default remark({
  label: "rem:proton-mass-substrate-identity-derivation",
  title:
    "Proton-mass aether identity — numerical verification, $h$-expansion, and precision frontier",
  interprets: "prop:proton-mass-substrate-identity",
  uses: [
    "prop:proton-mass-substrate-identity",
    "def:f-bor-borromean-observable",
    "prop:flavor-split-substrate",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "50-dps verification script: `computations/m_p_substrate_identity_50dps.py`; electromagnetic $(\\alpha_{\\mathrm{em}}/\\pi)/6$ near-match probe: `computations/ocneanu_12_em_correction_candidate.py`.",
    },
  ],
  tags: [
    "proton-mass",
    "substrate-identity",
    "numerical-verification",
    "h-expansion",
    "precision-frontier",
    "appendix",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/m_p_substrate_identity_50dps.py",
    witness: [
      "computations/m-p-substrate-identity-50dps.witness.json",
      "computations/ocneanu-12-em-correction-candidate.witness.json",
      "computations/probes/flavor-split-substrate-probe.witness.json",
      "computations/proton-error-anatomy-1ppb.witness.json",
      "computations/qbeta/qbeta-hoefsmit-chi-cross-anchor-stability-probe.witness.json",
      "computations/me-additive-term-structure.witness.json",
      "computations/two-term-qed-isotope-and-nucleon-compute.witness.json",
      "computations/ocneanu-54ppb-residual-exploration.witness.json",
    ],
    status: "verified",
  },
});
