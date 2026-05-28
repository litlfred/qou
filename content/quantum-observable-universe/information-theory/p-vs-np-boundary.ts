import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:p-vs-np-boundary",
  title:
    "$\\mathrm{P} \\neq \\mathrm{NP}$ as jet horizon opacity",
  tags: [
    "P-vs-NP",
    "jet-horizon",
    "boundary-condition",
    "complexity",
    "information-barrier",
    "event-horizon",
    "computational-horizon",
  ],
  uses: [
    "prop:p-bandwidth-bound",
    "def:observable-subcategory",
    "def:skein-resolution-obstruction",
    "rem:substrate-gm-torsion",
  ],
  cites: ["cook1971", "freedman2003"],
});
