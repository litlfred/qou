import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:graded-hecke-energy-truncation-bound",
  proofs: ["prf:graded-hecke-energy-truncation-bound"],
  title:
    "Graded Hecke energy truncation bound: $P_K(q)$ has at most $\\ell(K, q_0) + 1$ nonzero grades",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.graded_hecke_energy_truncation_bound",
    validation: "not_checked",
  },
  uses: [
    "rem:mass-spectrum-generating-function",
    "conj:gs-graded-markov-trace-existence",
  ],
  cites: ["khovanovlauda2009", "brundankleshchev2009"],
  tags: [
    "graded-hecke-energy",
    "confinement-level",
    "truncation",
    "stratified-cache",
    "computational-bound",
    "klr-module",
  ],
});
