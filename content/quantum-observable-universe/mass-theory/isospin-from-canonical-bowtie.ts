import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:isospin-from-canonical-bowtie",
  title:
    "Canonical $\\mathrm{SU}(2)_I$ isospin from the operator-valued $\\bowtie_K$ interface (regularised crystal extension)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.IsospinFromCanonicalBowtie",
    validation: "not_checked",
  },
  uses: [
    // The plain-generator restricted version (the load-bearing
    // upstream this block extends):
    "prop:crystal-isospin-degeneracy",
    // The color-tube channel-assignment that supplies the
    // canonical bowtie interface:
    "prop:inter-nucleon-channel-color-tube",
    // Substrate flavor split = the 305 ppm anomaly this block
    // identifies as the bar-anti-symmetric isospin residue:
    "prop:flavor-split-substrate",
    // The Hecke quadratic underlying sigma / sigma^-1 / averaged:
    "def:hecke-normal-form",
    "def:bar-involution",
    // The categorical proton/neutron color sheets:
    "def:categorical-proton",
    "def:categorical-neutron",
  ],
  computation: {
    engine: "python+mpmath",
    script:
      "folio-assistant/computations/_li_2_q_util.py",
    witness:
      "folio-assistant/computations/m-p-borromean-verification-50dps.witness.json",
    status: "verified",
  },
  cites: [
    "kashiwara1991",
    "wenzl1988",
    "lusztig1990",
    "wigner1937",
  ],
  tags: [
    "isospin",
    "duality-d9",
    "bowtie-interface",
    "regularised-crystal-functional",
    "bar-anti-symmetric-residue",
    "flavor-split",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
    "non-scholarly-voice-exception",
  ],
});
