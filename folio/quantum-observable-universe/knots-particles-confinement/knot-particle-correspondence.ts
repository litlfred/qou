import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-particle-correspondence",
  title:
    "Knot--particle correspondence via $q$-Schur--Weyl duality",
  tags: ["knot", "particle", "dictionary", "schur-weyl", "markov-trace"],
  lean: { ref: "qou:QOU.Braiding.no_surjection_onto_infinite",
    validation: "not_checked",
  },
  cites: ["jones1987"],
  uses: ["def:hadron"],
});
