import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body:
        "**Corrected 2026-11-16 (QA finding: da-non-sequitur).** The proof said the " +
        "volume-zero knots are exactly the torus knots; $3_1 \\# 3_1$ is a counterexample, so " +
        "'fundamental' is now defined as torus. The proof also now records that its skein " +
        "relation is the HOMFLY relation at the $\\mathfrak{gl}_1$ point $a = q$, where every " +
        "link equals the unknot in $\\mathrm{Sk}_q(S^3)$ (Hopf link included). **Mass-derivation " +
        "flag:** `lem:skein-mass-from-linking` reads $Q(q)$ off this resolution, and in this " +
        "skein theory that coefficient carries no linking information. That lemma is not " +
        "edited here.",
    },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:skein-generation",
  lean: { ref: "qou:QOU.Torsion.skein_generation",
    validation: "not_checked",
  },
  title: "Skein generation of hadrons from mass-zero fundamentals",
  uses: [
    "rem:hadron-operations",
    "def:hadron-fibre-embedding",
  ],
  proofs: ["prf:skein-generation"],
  tags: ["skein", "generation", "mass", "hadron", "torus-knot"],
});
