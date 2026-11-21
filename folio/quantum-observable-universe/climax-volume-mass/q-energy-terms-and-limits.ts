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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The full mass including the brane tower evaluates to $\\mathrm{Vol}(K)/\\hbar_q^2$ for hyperbolic knots ([topological mass formula](#conj:topological-mass-formula))." },
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
