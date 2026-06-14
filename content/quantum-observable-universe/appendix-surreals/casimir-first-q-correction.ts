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
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** The weight expansion is proved (sorry-free supporting\nlemmas in `FigureEightCasimirWeight.lean`); the carrier\nidentification is additionally class-axiomatised in the same file\n(`FirstInteractingCasimirCorrection`, the §3b-cond pattern), with\nthe Taylor form, the classical limit, the enhancement bound\n$1 \\leq \\mathrm{weight}$, and the bar symmetry\n$\\mathrm{weight}(q^{-1}) = \\mathrm{weight}(q)$ machine-verified\nconditional on an instance — and constructing the instance is\nexactly the open mode-sum. The $n$-stability selection underlying\nthe parent block's mode-count functional is formalised in\n`CasimirNStability.lean`. The exclusion of torus\nclosures and the identification of $4_1$ as the minimal hyperbolic\ncarrier follow from cited content; the mode-sum itself — and with it\nthe $1/d$ power and the magnitude — is the open construction. The\nstructural identification and the supporting computation are\nrecorded in the\n[first-q-correction audit](../../../docs/audits/2026-06-01-casimir-first-qcorrection-figure8.md)\nand\n[`casimir-d6-qcorrection-structure.witness.json`](../../../folio-assistant/computations/casimir-d6-qcorrection-structure.witness.json).\nA staged construction plan for the mode-sum is maintained in the\n[N\\_⊙ scoping workplan](../../../docs/workplans/2026-06-12-n-odot-construction-scoping.md).",
    },
  ],
});
