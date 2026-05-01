import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:residue-at-root-from-gs-filtration",
  title:
    "Residue at a root of unity of the graded Markov trace, defined algebraically (no meromorphic continuation)",
  lean: {
    ref: "qou:QOU.BraidKnot.residue_at_root_from_gs_filtration",
    validation: "not_checked",
  },
  uses: [
    "prop:graded-markov-trace-from-gs-filtration",
    "prop:gb-spectral-sequence",
  ],
  cites: ["bourbaki-LIE-VII"],
  tags: [
    "residue",
    "root-of-unity",
    "cyclotomic",
    "gs-filtration",
    "graded-trace",
    "narrative-anchor",
  ],
});
