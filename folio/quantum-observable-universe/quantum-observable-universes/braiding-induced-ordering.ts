import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:braiding-induced-ordering",
  title:
    "Degree-lexicographic well-ordering on braid words",
  tags: [
    "braiding",
    "well-ordering",
    "admissible-system",
    "hecke-algebra",
    "arrow-of-time",
    "temporal",
    "groebner",
  ],
  lean: { ref: "qou:QOU.braiding_induced_ordering_holds",
    validation: "not_checked",
  },
  uses: [
    "prop:braid-action-tensor",
    "def:braid-group",
    "rem:hecke-algebra-from-braiding",
    "unital-groebner-bases:def:admissible-system",
  ],
});
