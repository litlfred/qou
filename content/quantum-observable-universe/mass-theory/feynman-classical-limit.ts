import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:feynman-classical-limit",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.ClassicalLimitDegeneration",
    validation: "not_checked",
  },
  title: "Classical limit: recovery of the symmetric path integral",
  tags: ["path-integral", "feynman", "classical-limit", "hecke-degeneration"],
  uses: [
    "prop:feynman-categorical-trace",
    "def:q-energy",
    "conj:classical-limit-stpart",
  ],
  proofs: [],
});
