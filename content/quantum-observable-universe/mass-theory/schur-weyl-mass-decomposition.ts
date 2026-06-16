import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:schur-weyl-mass-decomposition",
  title:
    "Schur–Weyl decomposition of the atomic mass trace",
  lean: {
    ref: "qou:QOU.BraidKnot.schur_weyl_mass_decomposition",
    validation: "not_checked",
  },
  uses: [
    "prop:wigner-2-coefficient",
    "prop:markov-pair-z2",
    "prop:shell-schur-weyl-self-duality",
    "prop:gb-residue-spectral-sum",
  ],
  tags: [
    "schur-weyl",
    "wedderburn",
    "mass",
    "hook-product",
    "partition",
    "hecke-algebra",
  ],
  computation: {
    engine: "python",
    script: "computations/atom_level_wedderburn_tower.py",
    witness:
      "computations/atom-level-wedderburn-tower.witness.json",
    status: "verified",
    requires: ["mpmath", "numpy", "scipy"],
  },
});
