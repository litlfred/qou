import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bn-mtc-action",
  proofs: ["prf:bn-mtc-action"],
  lean: { ref: "qou:QOU.ObservableMTC.bnAction", validation: "not_checked" },
  title: "Braid group action on $\\mathbf{V}^{\\otimes n}$ does not factor through $S_n$",
  tags: ["braid-group", "mtc", "anyons", "fractional-statistics"],
  uses: ["def:observable-mtc"],
  cites: ["kitaev2006"],
});
