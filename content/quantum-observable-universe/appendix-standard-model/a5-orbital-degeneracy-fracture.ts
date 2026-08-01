import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:sm-gauge-truncation",
  label: "rem:a5-orbital-degeneracy-fracture",
  title: "Orbital degeneracies fracture along $A_5$ irreducibles",
  tags: [
    "appendix",
    "standard-model",
    "icosahedral",
    "orbitals",
    "brings-surface",
  ],
  uses: ["conj:sm-gauge-truncation"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-01",
      body:
        "Bean qou-a2g2. The branching arithmetic is exact and " +
        "witness-pinned (computations/a5-so3-branching.witness.json, " +
        "integer residuals < 1e-30); the physical fine-structure " +
        "reading is interpretive and conditional on the truncation " +
        "conjecture — nothing is wired to production. Ties to the " +
        "shell-filling swarm (bean 1c24).",
    },
  ],
});
