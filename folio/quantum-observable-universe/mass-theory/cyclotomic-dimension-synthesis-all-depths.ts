import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:cyclotomic-dimension-synthesis-all-depths",
  title:
    "Cyclotomic dimension synthesis at every depth: $(K - 3)/2$ for $n$ odd, $(K - 1)/2$ for $n$ even",
  uses: ["conj:cyclotomic-depth3-dimension-synthesis"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "Demoted from proposition to conjecture (owner card, 2026-11-21, \"Prove and demote\"). " +
        "The equality needs a lower bound: that the surviving real (or imaginary) parts are " +
        "Q-linearly independent modulo the Tate and zeta lines. That is the open Beilinson / Zagier " +
        "conjecture for cyclotomic fields, not an unconditional result. The upper-bound counting " +
        "is kept as a sketch; the PSLQ witnesses at small K are evidence, not proof. The old " +
        "lean.ref named a declaration that does not exist and is removed.",
    },
  ],
  cites: ["bloch2000", "zagier1986"],
  tags: [
    "cyclotomic",
    "dimension-synthesis",
    "all-depths",
    "borel-saturation",
    "beilinson-conditional",
    "bloch-suslin-unconditional",
    "graded-mikusinski",
  ],
});
