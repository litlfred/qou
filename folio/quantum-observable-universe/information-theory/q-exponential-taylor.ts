import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
  label: "prop:q-exponential-taylor",
  title: "Taylor series of $\\exp_q$ (archimedean)",
  tags: ["q-exponential", "taylor-series", "archimedean"],
  lean: { ref: "qou:QOU.qExponentialTaylor",
    validation: "not_checked",
  },
  uses: [
    "def:q-exponential",
    "rem:archimedean-realisations",
  ],
});
