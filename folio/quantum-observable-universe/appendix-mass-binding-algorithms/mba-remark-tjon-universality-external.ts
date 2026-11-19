import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Formalization and probe pointers moved out of published prose: the simplex-baseline inequalities are formalized over a generic commutative ring in `QOU.MassTheory.TjonSimplexForm` (`tjon_baseline_lt_four_ratio`, `universal_ratio_not_in_tjon_baseline`, `universal_ratio_forces_mu4`) and cross-checked numerically in `computations/deltalambda/tjon_external_cross_check_probe.py`.",
    },
  ],
  label: "rem:tjon-universality-external",
  title: "The external three-body/four-body correlation, and why it does not license the simplex baseline",
  interprets: "alg:delta-lambda-closure",
  tags: [
    "mba",
    "delta-lambda",
    "magnitude-open",
    "external-literature",
    "epistemic-status",
  ],
  uses: [
    "alg:delta-lambda-closure",
  ],
  cites: [
    "platter2005tjon",
    "hammer2007fourbody",
    "jurgenson2009srg",
    "ame2020",
  ],
});
