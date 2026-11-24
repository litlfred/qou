import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:vertex-is-exceptional-divisor",
  label: "rem:generating-functions-solve-reeb-flow",
  title:
    "Generating functions ($\\exp_q$, $\\mathrm{Li}_2^q$, categorical Fourier) are the Reeb-flow solutions",
  tags: [
    "q-exponential",
    "q-dilogarithm",
    "categorical-fourier",
    "habiro-ring",
    "reeb-flow",
    "pre-archimedean",
  ],
  uses: [
    "prop:q-exponential-unique",
    "prop:q-dilogarithm-unique",
    "prop:categorical-fourier-exists",
    "prop:vertex-is-exceptional-divisor",
    "prop:thurston-volume-additivity",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-08-23-free-prop-field-triviality-probe.lean` records that the synthesis-level `HabiroFlowSolution` carrier with bare `Prop` fields was trivially inhabited by `True`.",
      see: "docs/audits/2026-08-23-free-prop-field-triviality-probe.lean",
    },
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`): `2026-08-23-free-prop-real-module-probe.lean` imports `QOU.Habiro.FlowSolution` directly and witnesses trivial inhabitation of `QOU.Habiro.HabiroFlowSolution`.",
      see: "docs/audits/2026-08-23-free-prop-real-module-probe.lean",
    },
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation shape audit (`qou-x60n`, `qou-tsnp`): `2026-09-12-prop-universe-carrier-shape.lean` (`PropUniverseWithConjunction`) proves conjoining bare `Prop`-typed fields — the shape of `HabiroFlowSolution.all_hold` — remains unconditionally inhabited.",
      see: "docs/audits/2026-09-12-prop-universe-carrier-shape.lean",
    },
  ],
});
