import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:wenzl-positivity-implies-substrate-positivity",
  title:
    "Wenzl positivity at $q_0$ implies substrate $C^*$-Frobenius positivity",
  lean: {
    ref: "qou:QOU.AppendixSurreals.WenzlPositivityImpliesSubstratePositivity",
    validation: "not_checked",
  },
  uses: [
    "conj:os-reflection-positivity-from-reeb",
    "def:frobenius-hopf-substrate",
    "def:archimedean-realization-functor",
    "def:adelic-substrate",
  ],
  cites: [
    "wenzl1988",
    "wenzl1990",
    "kazhdanwenzl1993",
  ],
  tags: [
    "wenzl-positivity",
    "c-star-frobenius",
    "muger-positivity",
    "yang-mills",
    "mass-gap",
    "millennium-problem",
    "derivation-of-axiom",
    "open-problem",
  ],
});
