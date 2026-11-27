import { remark } from "../../schema/builders";

export default remark({
  label: "rem:tjon-universality-external",
  title:
    "The external three-body/four-body correlation, and why it does not license the simplex baseline",
  interprets: "prop:delta-lambda-dt-index-unification",
  lean: {
    ref: "qou:QOU.MassTheory.TjonSimplexForm.universal_ratio_forces_mu4",
    validation: "not_checked",
  },
  tags: [
    "delta-lambda",
    "magnitude-open",
    "external-literature",
    "epistemic-status",
  ],
  uses: [
    "prop:delta-lambda-dt-index-unification",
    "rem:delta-lambda-value-vs-magnitude",
  ],
  cites: [
    "platter2005tjon",
    "hammer2007fourbody",
    "jurgenson2009srg",
    "ame2020",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Relocated intact from `appendix-mass-binding-algorithms/mba-remark-tjon-universality-external` under `qou-mba8`. Numerical cross-check script: `computations/deltalambda/tjon_external_cross_check_probe.py`; generic-ring Lean formalization in `QOU.MassTheory.TjonSimplexForm`.",
    },
  ],
});
