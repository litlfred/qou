import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
  label: "rem:connes-distance-not-reeb-step-count",
  title:
    "$d_{\\mathrm{Connes}}$ is a minimal Reeb step count only in the $q \\to \\infty$ limit",
  interprets: "prop:reeb-coefficient-is-hbar-q",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.dirac_coefficients_convex",
    validation: "not_checked",
  },
  uses: [
    "prop:reeb-coefficient-is-hbar-q",
    "prop:reeb-operations-per-planck",
  ],
  tags: ["connes-distance", "reeb-flow", "limit", "dirac-operator"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_wave3_periodic_table_synthesis_probe.py",
    witness: "computations/probes/nuclear-wave3-periodic-table-synthesis.witness.json",
    status: "verified",
  },
});
