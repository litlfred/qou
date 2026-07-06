import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:n-sym-symmetric-channel-normalization",
  title:
    "$\\mathcal{N}_{\\rm sym}(q)$ — symmetric-channel Plancherel normalization for the EW/Higgs sector",
  lean: { ref: "qou:QOU.BraidKnot.NSymSymmetricChannelNormalization", validation: "stub" },
  uses: [
    "conj:weak-spectral-completeness",
    "conj:electroweak-higgs-torus-link-triplet",
    "conj:force-carrier-knot-vs-link-dichotomy",
    "conj:electroweak-mass-eigenstate-count",
    "prop:gram-determinant-plancherel-ratio",
    "thm:em-spectral-completeness",
  ],
  computation: {
    engine: "sympy",
    script: "computations/n_sym_numerical_anchor.py",
    witness: [
      "computations/n-sym-numerical-anchor.witness.json",
      "computations/n-sym-goldstone-phase-space-probe.witness.json",
      "computations/n-sym-gram-determinant-probe.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "electroweak",
    "plancherel",
    "spectral-completeness",
    "weak-coupling",
    "n-sym",
    "nv-1",
    "open-problem",
  ],
});
