import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fivetwo-stokes-unimodular",
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoStokes.Splus0_transpose_mul_Sminus0",
    validation: "not_checked",
  },
  title:
    "The leading $5_2$ Stokes matrices are unimodular and mutually inverse under transposition, and the $W_{-1}$ block has determinant $-2$",
  tags: [
    "five-two",
    "stokes-matrix",
    "unimodular",
    "stokes-sandwich",
    "resurgence",
  ],
  uses: ["prop:fivetwo-dt-spectrum-split"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Original wording: heading \"Why these are Lean-provable\"; \"are checked numerically in the sandwich compute and are not formalised here.\"" },
    {
      kind: "status",
      date: "2026-08-19",
      body:
        "**Proved sorry-free** — Lean namespace `QOU.QBeta.FiveTwoStokes`: " +
        "`Splus0_det`, `Sminus0_det` ($= 1$), " +
        "`Splus0_transpose_mul_Sminus0` (the inversion relation, cited as " +
        "the block's `lean.ref`), `Wminus1_0_det` ($= -2$) with " +
        "`Wminus1_0_det_abs`, and `inversion_coeff0` through " +
        "`inversion_coeff3` carrying the relation to the first four orders in " +
        "$q$. All finite decidable identities about concrete matrices — no " +
        "analysis. The file promotes to theorems the numerical K1/K2/K3 " +
        "checks of `computations/probes/qbeta_g3_5two_stokes_sandwich.py`.",
    },
    {
      kind: "caveat",
      date: "2026-08-19",
      body:
        "**Leading order, not all orders.** The all-orders statements — " +
        "$\\det S^{\\pm}(q) = 1$ as an identity of $q$-series, and Stokes " +
        "integrality of the full sandwich — are checked numerically in the " +
        "sandwich compute and are **not** formalised. What is proved is the " +
        "$q^{0}$ instance, plus the inversion relation at the first four " +
        "orders.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-19",
      body:
        "The $W_{-1}$ determinant is $-2$, not $+2$, and the sign is the " +
        "point. $W_{-1}(0)$ carries denominators of $6$ from the $c$-slot " +
        "subtraction, so it lives over $\\mathbb{Q}$ and the honest value is " +
        "$-2$; an earlier framing assumed a fitted integer $+2$. Recorded in " +
        "the block body rather than silently corrected, since the " +
        "\"$\\det \\pm 2$ phenomenon\" is cited elsewhere and a reader " +
        "meeting it should know which sign the derivation actually gives.",
    },
    {
      kind: "note",
      date: "2026-08-19",
      body:
        "The inversion relation constrains the chirality pair without " +
        "collapsing it: transposition is not the chirality involution " +
        "$\\tau$, so `prop:fivetwo-dt-spectrum-split` is not in tension with " +
        "it — the ordered pair of off-diagonal constants stays genuinely " +
        "ordered. Stated in the block body because \"the two blocks are " +
        "mutually inverse\" reads at first like it should trivialise the " +
        "split.",
    },
  ],
});
