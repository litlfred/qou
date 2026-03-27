import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-particle-correspondence",
  title:
    "Knot--particle correspondence via $q$-Schur--Weyl duality",
  tags: ["knot", "particle", "dictionary", "schur-weyl", "markov-trace"],
  lean: {
    decl: "QOU.Braiding.knot_particle_correspondence",
    validation: "not_checked",
  },
  uses: [
    "def:localized-knot",
    "prop:braid-action-tensor",
    "thm:knot-eigenbasis-complete",
    "def:hadron",
  ],
});
