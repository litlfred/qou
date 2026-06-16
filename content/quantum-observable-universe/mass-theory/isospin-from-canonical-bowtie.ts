import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:isospin-from-canonical-bowtie",
  title:
    "Canonical $\\mathrm{SU}(2)_I$ isospin from the operator-valued $\\bowtie_K$ interface (regularised crystal extension)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.IsospinFromCanonicalBowtie",
    validation: "not_checked",
  },
  uses: [
    "prop:crystal-isospin-degeneracy",
    "conj:inter-nucleon-channel-color-tube",
    "prop:flavor-split-substrate",
    "def:bar-involution",
  ],
  computation: {
    engine: "python+mpmath",
    script:
      "computations/_li_2_q_util.py",
    witness:
      "computations/m-p-borromean-verification-50dps.witness.json",
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
