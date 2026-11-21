import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "caveat", date: "2026-11-21", body: "Statement restated 2026-11-21 from \"closures are isotopic\" to \"closures have the same Markov trace\". Equal Hecke images do not give isotopic closures; the old proof treated the Hecke quadratic relation as Reidemeister II (round-trip audit pass 2, C03). The Lean `AtomKnot.unique_up_to_markov` proves only that two `AtomKnot` records with equal fields are equal (structure extensionality); it carries no topological content." },
  ],
  label: "prop:atom-knot-unique",
  title: "Uniqueness of the atom-knot up to Markov equivalence",
  lean: { ref: "qou:QOU.BraidKnot.AtomKnot.unique_up_to_markov",
    validation: "not_checked",
  },
  uses: ["prop:atom-knot-exists"],
  tags: ["uniqueness", "atom-knot", "markov-equivalence"],
});
