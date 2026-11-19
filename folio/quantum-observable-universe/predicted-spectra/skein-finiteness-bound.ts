import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:skein-finiteness-bound",
  title:
    "Finiteness of the nuclear chart: the Skein polynomial zero as stability boundary",
  tags: [
    "finiteness",
    "stability",
    "skein-polynomial",
    "transfer-matrix",
    "eigenvalue",
    "drip-line",
    "nuclear-chart",
  ],
  lean: { ref: "qou:QOU.Archimedean.skein_finiteness_bound",
    validation: "not_checked",
  },
  uses: ["prop:shell-closure-normal-form"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
