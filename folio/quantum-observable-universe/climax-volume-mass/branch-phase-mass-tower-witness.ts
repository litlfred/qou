import { remark } from "../../schema/builders";

export default remark({
  label: "rem:branch-phase-mass-tower-witness",
  title:
    "Branch-phase localisation on $\\mathcal{X}_5$ and the mass-tower " +
    "falsifiability witness",
  interprets: "def:crossing-energy",
  tags: [
    "branch-phase",
    "phase-tube",
    "isospin",
    "mass-tower",
    "falsifiability",
    "golden-ratio",
  ],
  uses: [
    "def:crossing-energy",
    "rem:commutative-crossing-energy",
    "def:hyperelliptic-quintic",
    "rem:u1-phase-tube",
  ],
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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The symbolic pipeline ([`per_irrep_pole_atom.py`](../../../computations/per_irrep_pole_atom.py)) verifies" },
    {
      kind: "note",
      body: "The rejected Wedderburn pair-generator extension was recorded in\n`fsh-guts/deprecated/computations/rho-k-pair-gen-v2-wedderburn.witness.json`;\nthat witness is deprecated. The rejection itself (it worsens the fit\nto ~4.7% MAE) stays in the prose.",
    },
  ],
});
