import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:braiding-induced-ordering",
  title:
    "The braiding induces a canonical admissible well-ordering on the Hecke basis",
  tags: [
    "braiding",
    "well-ordering",
    "admissible-system",
    "hecke-algebra",
    "arrow-of-time",
    "temporal",
    "groebner",
  ],
  lean: { ref: "qou:QOU.braiding_induced_ordering",
    validation: "not_checked",
  },
  uses: ["prop:braid-action-tensor"],
});
