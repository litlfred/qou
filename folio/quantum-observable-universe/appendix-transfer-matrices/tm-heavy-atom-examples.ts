import { prose } from "../../schema/builders";

export default prose({
  label: "tm-heavy-atom-examples",
  title: "Heavy-atom worked examples",
  uses: [
    "prop:generator-volume-decomposition",
    "rem:shell-construction-rules",
    "prop:spin-orbit-magic-closures",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-09",
      body: "Worked numerals in the illustrative two-strand tables were originally evaluated at $1/(q^{1/2}+q^{-1/2})$ (legacy Convention C) rather than canonical Convention D $z = q^3/(q^2+1)$ ($22.7\\%$ shift in $z$).",
    },
  ],
  tags: [
    "transfer-matrix",
    "worked-example",
    "heavy-atom",
    "shell-correction",
    "magic-number",
    "cobalt",
    "carbon-14",
    "bismuth",
    "appendix",
  ],
});
