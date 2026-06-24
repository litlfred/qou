import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ordering-jet-compatibility",
  proofs: ["prf:ordering-jet-compatibility"],
  lean: { ref: "qou:QOU.Torsion.degLex_wellFounded" },
  title:
    "The admissible ordering extends through the jet tower",
  tags: [
    "ordering",
    "jet-tower",
    "direct-limit",
    "admissible-system",
    "groebner",
    "time",
  ],
  uses: [
    "def:direct-limit-algebra",
    "unital-groebner-bases:def:jet-stratified-reduction",
  ],
});
