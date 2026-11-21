import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-chromaticity",
  title:
    "Three colors and $q$-chromaticity: why negative coefficients require confinement",
  interprets: "rem:force-knot-identification",
  tags: [
    "color",
    "chromaticity",
    "confinement",
    "skein",
    "negativity",
    "color-tube",
    "strong-force",
    "primaries",
  ],
  uses: ["rem:force-knot-identification"],
  cites: ["feynman1963"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Owner rulings 2026-11-20 (option B of " +
        "`docs/audits/2026-11-20-up-quark-electron-knot-clash.md`) and " +
        "2026-11-21: a quark is an unknot strand of $\\mathcal{B}_3$ carrying " +
        "one crossing letter, and $T_{2,3}$ is its lepton partner. The " +
        "sentence that said an individual quark forms a trefoil was reworded " +
        "on 2026-11-21. Not re-checked: whether the negative-coefficient " +
        "argument that follows was argued from the trefoil specifically. A " +
        "single crossing letter $\\sigma$ already has the eigenvalue " +
        "$-q^{-1}$ on its antisymmetric channel, so the conclusion may survive, " +
        "but that has not been shown here.",
    },
  ],
});
