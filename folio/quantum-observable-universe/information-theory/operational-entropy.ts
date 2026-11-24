import { definition } from "../../schema/builders";

export default definition({
  label: "def:operational-entropy",
  title: "Operational entropy of the Reeb dynamics",
  tags: [
    "information-theory",
    "metric-entropy",
    "julia-set",
    "reeb-flow",
    "hausdorff-dimension",
  ],
  lean: { ref: "qou:QOU.Information.operationalEntropy",
    validation: "not_checked",
  },
  uses: ["prop:reeb-operations-per-planck"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation twin-audit (`qou-x60n`): `2026-09-05-archimedean-twins-are-instantiations-probe.lean` proves `operationalEntropy` in `MathConstants.lean` is the `ℝ` instantiation of the generic `[CommRing k]` unit-typed sibling (`q = 0` junk point unreachable under `1 ≤ q`).",
      see: "docs/audits/2026-09-05-archimedean-twins-are-instantiations-probe.lean",
    },
  ],
});
