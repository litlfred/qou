import { definition } from "../../schema/builders";

export default definition({
  label: "def:crossing-energy",
  title: "Crossing energy of a knot composite",
  tags: ["crossing", "energy", "skein", "r-matrix", "stability"],
  lean: { ref: "qou:QOU.Braiding.CrossingEnergy",
    validation: "not_checked",
  },
  // The energy is DEFINED as a sum over the crossings of β — one term per
  // two-strand event, with no irreducible many-body remainder. That the sum
  // exhausts the interaction is prop:pairwise-interaction-decomposition;
  // without it, "sum over crossings" would be an assumption rather than a
  // consequence of the braiding being binary.
  uses: [
    "prop:nuclear-groebner-reduction",
    "prop:pairwise-interaction-decomposition",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
