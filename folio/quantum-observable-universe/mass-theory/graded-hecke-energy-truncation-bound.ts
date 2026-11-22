import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:graded-hecke-energy-truncation-bound",
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
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-09-06",
      body: "The scope note was added because this block's premise read as though the atomic word satisfied the braid hypothesis. The producer's docstring has carried the averaged-letter misnomer note since 2026-08-25 (PR #5765).",
    },
  ],
});
