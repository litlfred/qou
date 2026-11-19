import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:beta-decay-transfer-matrix",
  label: "rem:beta-decay-interpretation",
  title: "Beta decay universality, tritium example, and double beta decay",
  tags: [
    "beta-decay",
    "universality",
    "tritium",
    "double-beta",
    "transfer-matrix",
    "worked-example",
  ],
  uses: ["def:Q-value-transition"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_spin_orbit_shells_and_symmetry_probe.py",
    witness: "computations/probes/nuclear-spin-orbit-shells-and-symmetry.witness.json",
    status: "verified",
  },
});
