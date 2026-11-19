import { remark } from "../../schema/builders";

export default remark({
  label: "rem:shell-construction-rules",
  title:
    "Construction rules for nuclear shells from the torus knot hierarchy",
  tags: [
    "shell-construction",
    "torus-knot",
    "magic-numbers",
    "groebner-normal-form",
    "borromean",
    "construction-rules",
  ],
  interprets: "cor:spectral-decomposition-qvalue",
  uses: ["cor:spectral-decomposition-qvalue"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/nuclear_spin_orbit_shells_and_symmetry_probe.py",
    witness: [
      "computations/probes/nuclear-spin-orbit-shells-and-symmetry.witness.json",
      "computations/spectral-decomposition-qvalue-d.witness.json",
      "computations/confined-knot-binding.witness.json",
    ],
    status: "verified",
  },
});
