import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:casimir-first-q-correction",
  title:
    "First substrate correction to the Casimir force is carried by the figure-eight knot $4_1$",
  lean: {
    ref: "qou:QOU.AppendixSurreals.FigureEightCasimirWeight",
  },
  uses: [
    "conj:casimir-epsilon-vacuum",
    "lem:degree-one-braid-trivial-volume",
  ],
  cites: ["casimir1948", "lickorish1997"],
  tags: [
    "tier:P",
    "surreal-numbers",
    "vacuum",
    "casimir-effect",
    "figure-eight-knot",
    "hyperbolic-volume",
    "skein-expansion",
    "open-problem",
  ],
  computation: {
    engine: "python",
    script:
      "folio-assistant/computations/casimir_d6_qcorrection_structure.py",
    witness: [
      "folio-assistant/computations/casimir-d6-qcorrection-structure.witness.json",
    ],
    status: "experimental",
  },
});
