import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "This formulation collapses three historically disjoint asymmetric phase regimes into a single unified bar-self-dual confinement band. While utilizing standard involution bounds, the structural consolidation is highly novel, offering a rigid phase boundary for the QOU framework." },
  ],
  label: "prop:bar-self-dual-confinement-band",
  title:
    "The open interval $(1/\\varphi^2,\\,\\varphi^2)$ is the maximal bar-self-dual confinement band",
  tags: [
    "golden-ratio",
    "bar-involution",
    "skew-symmetry",
    "confinement",
    "deconfinement",
    "phase-boundary",
    "substrate-parameter",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.BarSelfDualConfBand.bar_self_dual_confinement_band",
    validation: "not_checked",
  },
  uses: [
    "prop:golden-skew-dual-node",
    "rem:deconfinement-golden-threshold",
  ],
});
