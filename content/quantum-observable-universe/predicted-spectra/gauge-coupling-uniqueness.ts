import { corollary } from "../../schema/builders";

export default corollary({
  authorNotes: [
    { kind: "note", date: "2026-06-26", body: "Re-framing the conventional scalar uniqueness corollary explicitly within the context of spectral completeness provides a mathematically novel uniqueness constraint for the QOU gauge sector, bounding possible gauge couplings strictly by algebraic singlets." },
  ],
  label: "cor:gauge-coupling-uniqueness",
  title:
    "Uniqueness of the scalar gauge coupling on $A \\otimes A$",
  lean: {
    ref: "qou:QOU.Archimedean.gauge_coupling_uniqueness",
    validation: "not_checked",
  },
  uses: ["thm:em-spectral-completeness"],
  tags: [
    "uniqueness",
    "gauge-coupling",
    "singlet",
    "central-idempotent",
    "no-other-alpha",
  ],
  computation: {
    engine: "sympy",
    script: "computations/probes/gauge_coupling_uniqueness_probe.py",
    witness: "computations/probes/gauge-coupling-uniqueness-probe.witness.json",
    status: "verified",
  },
});
