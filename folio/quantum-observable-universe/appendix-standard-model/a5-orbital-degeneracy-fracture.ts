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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The branching arithmetic is pinned in the witness `a5-so3-branching.witness.json`." },
    {
      kind: "refined-framing",
      body: "An earlier version of this block rested its stated value on a falsifiability claim (differing from SO(3) \"at some resolution\"); the claim was withdrawn.",
    },
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
    {
      kind: "caveat",
      date: "2026-08-15",
      body:
        "Bean qou-cy2h. The block's stated value was falsifiability in " +
        "principle; that claim is withdrawn. Free-atom f-shell structure " +
        "is already described to spectroscopic precision by rotationally " +
        "invariant theory (J labels, exact 2J+1, spin-orbit lifting in a " +
        "J pattern), and \"at some resolution\" names no resolution, so the " +
        "claim was compatible with every null result. Scope-(a): the " +
        "branching arithmetic is untouched and the truncation picture is " +
        "NOT excluded. The open item is upstream of any bound — the " +
        "framework does not say whether the A5 frame is fixed in space " +
        "(Hughes-Drever anisotropy bounds apply) or independently oriented " +
        "per atom (ensemble line structure applies), so the constraining " +
        "experiment cannot yet be chosen.",
    },
  ],
});
