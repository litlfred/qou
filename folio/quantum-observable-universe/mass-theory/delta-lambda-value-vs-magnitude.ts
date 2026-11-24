import { remark } from "../../schema/builders";

export default remark({
  label: "rem:delta-lambda-value-vs-magnitude",
  renamedFrom: ["alg:delta-lambda-closure", "alg:per-isotope-binding"],
  title:
    "Per-partition $\\Delta_\\lambda$ value versus open super-pairwise many-body binding magnitude",
  interprets: "prop:delta-lambda-dt-index-unification",
  uses: [
    "prop:delta-lambda-dt-index-unification",
    "rem:term6-binding-density",
  ],
  cites: ["springer1976", "shoji2019", "garoufalidis-gu-marino2021"],
  lean: {
    ref: "qou:QOU.MassTheory.BindingSaturationCapA4.exchangeDet_pow_two_le_four",
    validation: "not_checked",
  },
  computation: {
    engine: "python+mpmath",
    script: "computations/delta_lambda_value_witness.py",
    witness: "computations/delta-lambda-witness.json",
    status: "verified",
  },
  tags: [
    "delta-lambda",
    "value-proved",
    "magnitude-open",
    "binding",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Consolidated and relocated from `appendix-mass-binding-algorithms` (`mba-sidecar-delta-lambda-closure` + `mba-step09b-per-isotope-binding`) under `qou-mba8`. Exact integer witness at `computations/delta-lambda-witness.json` (`delta_lambda_value_witness.py`); determinant cap `exchangeDet_pow_two_le_four` in `QOU/MassTheory/BindingSaturationCapA4.lean`.",
    },
  ],
});
