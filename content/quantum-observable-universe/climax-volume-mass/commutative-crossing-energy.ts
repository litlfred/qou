import { remark } from "../../schema/builders";

export default remark({
  label: "rem:commutative-crossing-energy",
  title:
    "Categorical coordinate of the commutative limit: " +
    "$i$ as $\\sqrt{\\lambda_-}$ and the $\\mathbb{Z}_2 \\hookrightarrow " +
    "\\mathrm{U}(1) \\hookrightarrow \\mathrm{U}_q(1)$ hierarchy",
  tags: [
    "categorical-coordinate",
    "crossing-energy",
    "commutative-limit",
    "complex-structure",
    "u1",
    "phase-tube",
    "branch-phase",
    "isospin",
    "mass-tower",
  ],
  uses: [
    "rem:u1-phase-tube",
    "rem:sqrt-q-ribbon-structure",
    "rem:archimedean-realisations",
    "prop:categorical-coordinate-ring",
  ],
  interprets: "def:crossing-energy",
  cites: ["satula1997"],
  computation: {
    engine: "python",
    script: "computations/isospin_mass_tower_collapse.py",
    witness: [
      "computations/branch-phase-fit-to-mass-tower.witness.json",
      "computations/isospin-mass-tower-collapse.witness.json",
    ],
    status: "verified",
  },
});
