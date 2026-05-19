import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:silver-ratio-beta-decay-null",
  lean: {
    ref: "qou:QOU.ParticleInteractions.SilverRatioBetaDecayNull",
    validation: "not_checked",
  },
  title:
    "**Silver-ratio $\\beta$-decay null**: at $q = 1 \\pm \\sqrt{2}$, the categorical $\\beta$-decay $Q$-value vanishes; the Hecke generator $\\sigma$ has eigenvalues = $1 \\pm \\sqrt{2}$ (silver-ratio self-referential fixed point); proton and neutron Markov-traces become categorically indistinguishable",
  uses: [
    "prop:neutron-qvalue-symbolic",
    "prop:q-beta-form-a-n1-symbolic",
    "rem:per-block-hopf-jones-absorption-pattern",
  ],
  cites: [
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "lean-infrastructure",
    "silver-ratio",
    "beta-decay-null",
    "hecke-quadratic",
    "pell-lucas",
    "categorical-degeneracy",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/qbeta_fsc_g_pattern_comparison.py",
    witness: [
      "folio-assistant/computations/qbeta-fsc-g-pattern-comparison.witness.json",
    ],
    status: "experimental",
  },
});
