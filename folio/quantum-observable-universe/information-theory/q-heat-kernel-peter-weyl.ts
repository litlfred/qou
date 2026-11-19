import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
  label: "prop:q-heat-kernel-peter-weyl",
  title: "Peter--Weyl decomposition of the $q$-heat kernel (archimedean)",
  tags: ["q-heat-equation", "peter-weyl", "heat-kernel", "hecke", "wedderburn", "archimedean"],
  lean: { ref: "qou:QOU.qHeatKernelPeterWeyl",
    validation: "not_checked",
  },
  uses: [
    "def:categorical-fourier",
    "prop:q-gaussian-solves-q-heat",
  ],
});
