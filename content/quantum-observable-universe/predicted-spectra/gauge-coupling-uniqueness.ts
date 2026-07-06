import { corollary } from "../../schema/builders";

export default corollary({
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
