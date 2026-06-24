import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:braiding-induced-ordering",
  proofs: ["prf:braiding-induced-ordering"],
  title:
    "Canonical admissible ordering on the Hecke basis induced by braiding",
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
