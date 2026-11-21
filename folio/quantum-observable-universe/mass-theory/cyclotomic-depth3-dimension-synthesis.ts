import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:cyclotomic-depth3-dimension-synthesis",
  title:
    "Cyclotomic depth-3 dimension synthesis: $(K - 3)/2$ at every prime $K \\geq 5$",
  computation: {
    engine: "mpmath",
    script: "computations/cyclotomic_depth3_dimension_pslq.py",
    witness:
      "computations/cyclotomic-depth3-dimension-pslq.witness.json",
    status: "verified",
  },
  uses: ["conj:two-filtration-bridge-general"],
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
    "depth-3-dimension",
    "borel-saturation",
    "beilinson-conditional",
    "K-5-certified",
    "K-7-certified",
    "synthesis",
    "graded-mikusinski",
  ],
});
