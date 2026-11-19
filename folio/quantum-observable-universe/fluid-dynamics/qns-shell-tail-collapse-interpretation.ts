import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qns-shell-tail-collapse-interpretation",
  interprets: "prop:qns-shell-tail-collapse",
  title:
    "Scope and measured support for the $q$-shell tail collapse",
  uses: ["def:qns-unit-layers", "prop:qns-shell-tail-collapse"],
  tags: [
    "navier-stokes",
    "fluid-dynamics",
    "shell-model",
    "probe-support",
    "millennium-problem",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Supporting trajectory witnesses: qns-dissipation-scale-probe.witness.json, qns-nonlocal-transfer-probe.witness.json, qns-allpairs-transfer-probe.witness.json, qns-phase-decorrelation-probe.witness.json, and qns-phase-scramble-probe.witness.json.",
    },
  ],
});
