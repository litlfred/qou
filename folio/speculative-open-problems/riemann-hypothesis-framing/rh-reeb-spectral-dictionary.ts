import { remark } from "../../schema/builders";

export default remark({
  label: "rem:rh-reeb-spectral-dictionary",
  title: "Speculative Reeb-flow and explicit-formula analogies for the Riemann hypothesis",
  interprets: "conj:macroscopic-stability-equivalence",
  uses: [
    "conj:classical-riemann-hypothesis",
    "conj:adelic-critical-line-persistence",
    "conj:macroscopic-stability-equivalence",
    "quantum-observable-universe:conj:explicit-formula",
    "quantum-observable-universe:thm:hasse-weil-bound",
    "quantum-observable-universe:rem:unitary-stability",
  ],
  cites: ["weil1948", "rosen2002"],
  tags: ["riemann-hypothesis", "reeb", "explicit-formula", "dictionary"],
});
