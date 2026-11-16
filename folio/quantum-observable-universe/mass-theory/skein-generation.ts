import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-16",
      body: "Rescoped by owner ruling (2026-11-16) after the sidecar review failed the proof: with the relation $q L_+ - q^{-1} L_- = (q - q^{-1})L_0$ every link equals the unknot, so generation by torus knots and the Hopf link held only trivially and the mass-from-linking step did not follow. The statement is now the HOMFLYPT freeness of $\\mathrm{Sk}(S^3)$; the torus-knot, Hopf and hadron-mass reading moved to [rem:skein-generation-hadron-reading](#rem:skein-generation-hadron-reading). The Lean `skein_generation` proves the abstract step (generation from a terminating resolution), not freeness.",
    },
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
  title: "The skein module of the 3-sphere is free on the unknot",
  uses: [
    "rem:hadron-operations",
    "def:hadron-fibre-embedding",
  ],
  proofs: ["prf:skein-generation"],
  tags: ["skein", "generation", "homflypt"],
  cites: ["lickorish1997"],
});
