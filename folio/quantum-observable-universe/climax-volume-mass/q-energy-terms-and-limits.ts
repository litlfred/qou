import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-energy-terms-and-limits",
  title:
    "The three energy terms, classical/deep-quantum limits, " +
    "and crossing-energy relation",
  interprets: "def:q-energy",
  uses: [
    "def:q-energy",
    "def:crossing-energy",
    "prop:categorical-mass-markov",
    "conj:topological-mass-formula",
    "conj:mass-endomorphism",
  ],
  tags: [
    "energy",
    "q-deformed",
    "categorical-action",
    "crossing",
    "mass-energy",
    "limits",
  ],
});
