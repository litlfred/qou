import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fivetwo-bar-odd-arithmetic-home",
  interprets: "prop:fivetwo-trace-field",
  title:
    "The bar-odd channel of $5_2$ is confined to the $\\sqrt{-23}$ line, and chirality is why the question is asked on $5_2$ rather than $4_1$",
  tags: [
    "five-two",
    "bar-odd",
    "bar-involution",
    "chirality",
    "amphichiral",
    "trace-field",
  ],
  uses: ["prop:fivetwo-trace-field", "prop:fivetwo-saddle-sum-rule"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-19",
      body:
        "Interpretive only — it makes no claim beyond the propositions it " +
        "cites. The location statement (a bar-odd combination of the " +
        "conjugate pair lies on the $\\sqrt{-23}$ axis) follows from the " +
        "field structure in `prop:fivetwo-trace-field`; the amphichirality " +
        "argument ($J_{K^*}(q) = J_K(q^{-1})$, so the bar-odd part of an " +
        "amphichiral knot's Jones polynomial vanishes) is classical. Neither " +
        "is separately formalised, and neither needs to be.",
    },
    {
      kind: "caveat",
      date: "2026-08-19",
      body:
        "**Location is not evaluation.** Knowing the line a bar-odd datum " +
        "must lie on does not evaluate anything on it. No bar-odd action " +
        "value is asserted here. Stated because the surrounding lane exists " +
        "to chase that value, and a clean structural confinement result is " +
        "the kind of thing that gets cited as though it were progress on the " +
        "value.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-19",
      body:
        "The final section carries a retraction forward into the paper. The " +
        "bar-odd channel's arithmetic home was recorded in " +
        "`docs/audits/2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md` " +
        "as $\\mathbb{Q}(\\sqrt{-7})$, inferred from $\\det(5_2) = 7$; that " +
        "premise was retracted 2026-08-11 (bean `qou-ynff`, PR #5271). The " +
        "$\\sqrt{-23}$ line was already visible in the corpus's own " +
        "$\\sigma$-pair data — " +
        "`computations/probes/qbeta_5two_gswz_saddle_arithmeticity_probe.py` " +
        "§4 records the bar-odd projection landing on the " +
        "$\\sqrt{-23}\\cdot\\mathbb{R}$-axis of $K \\otimes \\mathbb{C}$ — so " +
        "the live lane and the audit disagreed, and the live lane was right. " +
        "The generalised lesson (ask which *layer* of the knot a field is " +
        "attached to) is kept in the block body rather than in a note, since " +
        "it is the reusable part.",
    },
  ],
});
