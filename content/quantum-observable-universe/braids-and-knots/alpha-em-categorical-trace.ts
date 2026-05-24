import { remark } from "../../schema/builders";

export default remark({
  label: "rem:alpha-em-categorical-trace",
  title: "Legacy closed form $1/\\alpha_{EM} = 45 \\cdot [3]_q \\cdot (1 + \\delta_{CS} + 8q \\cdot \\delta_{CS}^2)$ as a consequence of the spectral-completeness program",
  interprets: "thm:em-spectral-completeness",
  uses: [
    "cor:gauge-coupling-uniqueness",
    "prop:gram-determinant-plancherel-ratio",
    "prop:exterior-square-borromean",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05",
      body:
        "The bare formula $1/\\alpha_{EM} = q[9]_q[10]_q$ now has a clean structural derivation as a categorical trace ratio, [prop:alpha-em-categorical-trace-ratio](#prop:alpha-em-categorical-trace-ratio) ($\\alpha_{EM} = h^2/(q\\,\\delta_q(T_{2,9})\\,\\delta_q(T_{3,5}))$). The $1.55 \\times 10^{-3}$ residual gap to CODATA is the subject of [rem:alpha-em-derivation-open-problems](#rem:alpha-em-derivation-open-problems); the current preferred lead is the *additive* Bring zero-mode form [prop:em-coupling-bring-zero-mode](#prop:em-coupling-bring-zero-mode), not the multiplicative gluon-octet ansatz reproduced below. The 100-dps PSLQ scan over an extended 54-element basis ruled out the multiplicative $q$-rational family entirely. This remark is retained for historical context.",
    },
  ],
});
