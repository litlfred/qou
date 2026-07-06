import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:constit-factor-2q-minus-1",
  title:
    "Constit-side per-Z step factor in canonical-atom Markov trace categorically equals 2q − 1 at q_0 (to 0.033% rel. err.)",
  lean: {
    ref: "qou:QOU.BraidKnot.ConstitFactor2qMinus1",
    validation: "not_checked",
  },
  uses: [
    "prop:interface-knot-markov-z",
    "prop:lr-tensor-character-bridge",
    "thm:jones-markov-trace",
  ],
  cites: ["jones1987", "wenzl1988"],
  computation: {
    engine: "python",
    script:
      "computations/constit_factor_and_volhyp_test.py",
    witness:
      "computations/constit-factor-and-volhyp.witness.json",
    status: "verified",
  },
  tags: [
    "markov-trace",
    "constit-factor",
    "categorical-derivation",
    "z-step",
    "research-conjectural",
    "hecke-skein",
  ],
});
