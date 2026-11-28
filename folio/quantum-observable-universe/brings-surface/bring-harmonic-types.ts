import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bring-harmonic-types",
  title: "The harmonics of Bring's surface by S5 type, exhaustively",
  lean: { ref: "qou:QOU.Brings.HarmonicTypes.class_function_expansion" },
  uses: ["lem:bring-map-euler-characteristic", "lem:brings-riemann-hurwitz", "conj:bring-isospectrality-question"],
  cites: ["fulton-harris1991", "edge1978", "sunada1985"],
  tags: ["brings-surface", "harmonics", "representation-theory", "maass", "spectral-geometry", "combinatorial-map"],
  proofs: ["prf:bring-harmonic-types"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Bean `qou-u81q` (owner pick \"Also Maass harmonics\", 2026-11-27; owner asked for Lean-proved exhaustiveness). Lean, sorry-free, axioms `propext`, `Classical.choice`, `Quot.sound` only: `QOU/BringsSurface/BringHarmonicTypes.lean` (items 1–5) and, for the Laplace reading over opaque eigenvalue labels, `QOU/Transcendental/BringsSurface/BringMaassTypes.lean`. Inputs cited, not derived: the character table of $S_5$, the list of its 19 subgroup classes (probe `bring_symmetry_quotient_genus_probe.py`), Maschke, the Hopf trace formula and the spectral theorem for $\\Delta$. No eigenvalue is computed or used.",
    },
  ],
});
