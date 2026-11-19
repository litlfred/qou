import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fivetwo-trace-field",
  lean: {
    ref: "qou:QOU.QBeta.FiveTwo.disc_eq_neg_23",
    validation: "not_checked",
  },
  title:
    "The $5_2$ saddle cubic has discriminant $-23$: the invariant trace field is the cubic field of discriminant $-23$, and its only quadratic is $\\mathbb{Q}(\\sqrt{-23})$",
  tags: [
    "five-two",
    "trace-field",
    "discriminant",
    "cubic-field",
    "bar-odd",
    "quadratic-resolvent",
  ],
  uses: [],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-19",
      body:
        "**Proved sorry-free** — Lean `QOU.QBeta.FiveTwo.disc_eq_neg_23` " +
        "(`FiveTwoSumRuleIntegrand.lean`). Stated over a generic " +
        "`CommRing R` with the three Vieta relations as hypotheses (§7c: no " +
        "ordering, no radical, no archimedean construct), discharged by " +
        "`rw [disc_eq_symm, e1, e2, e3]; norm_num`. The geometric reading in " +
        "the block body — that this is the invariant trace field of $5_2$, " +
        "with one real and one complex-conjugate pair of embeddings — is the " +
        "archimedean specialisation and is classical; it is not part of what " +
        "the Lean discharges.",
    },
    {
      kind: "caveat",
      date: "2026-08-19",
      body:
        "The $S_3$/$A_3$ Galois argument identifying $\\mathbb{Q}(\\sqrt{-23})$ " +
        "as the unique quadratic attached to $K$ is standard field theory and " +
        "is **not** formalised here; only the discriminant identity is. The " +
        "tower-law exclusion of $\\mathbb{Q}(\\sqrt{-7})$ likewise rests on " +
        "$2 \\nmid 3$, which is argued in prose rather than in Lean.",
    },
    {
      kind: "refined-framing",
      date: "2026-08-19",
      body:
        "The final section exists because the corpus carried the opposite " +
        "claim. `docs/audits/2026-07-18-5two-dilog-qsqrt7-bar-odd-action-home.md` " +
        "asserted that the $5_2$ invariant trace field is " +
        "$\\mathbb{Q}(\\sqrt{-7})$, reading it off $\\det(5_2) = 7$ — an " +
        "Alexander-polynomial datum. That premise was retracted 2026-08-11 " +
        "(bean `qou-ynff`, PR #5271); certification in " +
        "`computations/probes/qbeta_5two_trace_field_disc23_not_qsqrt7.py`, " +
        "correction recorded in " +
        "`docs/audits/2026-08-11-5two-trace-field-is-disc-minus-23.md`. The " +
        "distinction is stated in the block body rather than left implicit, " +
        "since both fields are genuinely attached to $5_2$ and only the layer " +
        "separates them.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/qbeta_5two_trace_field_disc23_not_qsqrt7.py",
    witness: [
      "computations/probes/qbeta-5two-trace-field-disc23-not-qsqrt7.witness.json",
      "computations/qbeta-route75-multiknot-gluing-symbolic.witness.json",
      "computations/qbeta/qbeta-wedderburn-phase-twoterm-pin.witness.json",
      "computations/qbeta/five-two-disc-neg23-cyclotomic-asymmetry.witness.json",
    ],
    status: "verified",
  },
});
