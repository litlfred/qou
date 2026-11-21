import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean class `AlphaKCategoricalClosure` " +
        "carries `E0_codata : ℝ` — a **CODATA value** — against which " +
        "`E0_framework : ℝ` is compared for the CAL-3 direction field. §7c " +
        "lists \"CODATA / experimental value\" as an `ℝ` row explicitly. The " +
        "stratum weights are additionally taken from " +
        "`QOU.MathlibExt.QPlancherel.measure (R := ℝ)` via " +
        "`alphaKStratumWeight`, whose companion `alphaKStratumWeight_nonneg` " +
        "is a **non-negativity** claim (`measure_nonneg`) and so needs the " +
        "ordering. Both reasons are independent of each other; either alone " +
        "puts this block on the archimedean side of the wall.",
    },
  ],
  label: "conj:alpha-k-categorical-closure",
  title:
    "Closed-form resummation of the categorical stratum prefactors $\\alpha_k$ — geometric vs symmetric q-dilogarithm candidates",
  lean: {
    ref: "qou:QOU.BraidKnot.AlphaKCategoricalClosure",
    validation: "not_checked",
  },
  uses: [
    "conj:alpha-k-derivation-procedure",
    "rem:beta-decay-energy-scale",
  ],
  cites: [
    "wenzl1988",
    "jones1985",
    "kassel1995",
  ],
  tags: [
    "tier:E",
    "alpha-k",
    "categorical-closure",
    "geometric-series",
    "q-dilogarithm",
    "li2q",
    "brane-tower",
    "CAL-3",
    "open-conjecture",
    "open-rd-item-6",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_beta_form_a_n1_extension.py",
    witness: [
      "computations/q-beta-form-a-n1-extension.witness.json",
    ],
    status: "experimental",
  },
});
