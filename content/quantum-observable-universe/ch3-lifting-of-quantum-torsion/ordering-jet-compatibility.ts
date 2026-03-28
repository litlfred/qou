import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ordering-jet-compatibility",
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
    "def:quantum-observable-universe",
    "def:recursive-brane-tower",
    "def:direct-limit-algebra",
    "prop:jet-prolongation",
    "unital-groebner-bases:def:admissible-system",
  ],
});
