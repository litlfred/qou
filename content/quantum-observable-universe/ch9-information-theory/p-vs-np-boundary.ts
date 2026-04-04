import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:p-vs-np-boundary",
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
    "def:computational-horizon",
    "prop:p-bandwidth-bound",
    "def:jet-horizon",
    "rem:skein-turing-machine",
    "conj:quantum-computational-universality",
    "def:information-speed-of-light",
  ],
  cites: ["cook1971", "freedman2003"],
});
