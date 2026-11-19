import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:categorical-proton",
  label: "rem:meson-to-proton-via-borromean",
  title:
    "Proton formation: three pair productions and the energy scale $\\mathbf{E}_0$",
  tags: [
    "proton",
    "baryon-number",
    "borromean",
    "energy-scale",
    "typed-crossings",
    "beta-decay",
    "formation-chain",
    "hecke-algebra",
    "computational-witness",
    "pair-production",
  ],
  uses: ["rem:energy-scale-planck"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Witnesses moved from prose: `meson-nucleon-nf.witness.json`, `beta-decay-energy-scale.witness.json`, and `confinement-operator-selection.witness.json`.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/confinement-operator-selection.witness.json",
      "computations/qbeta/qbeta-three-nucleon-nf-alpha-spread.witness.json",
    ],
    status: "verified",
  },
});
