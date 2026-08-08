import { lemma } from "../../schema/builders";

export default lemma({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The eigenbasis data in " +
        "`lean/QOU/FeynmanPathIntegrals.lean` is real-valued by design: " +
        "`markovWeight : YoungDiagram → ℝ`, " +
        "`partialTrace : YoungDiagram → carrier → ℝ`, and the derived " +
        "`transitionAmplitude : carrier → ℝ`. A transition amplitude is a " +
        "physical observable, and the file's surrounding claims about it are " +
        "the ε–δ classical-limit statements (`planck_limit`, " +
        "`|qNum q m - (m : ℝ)| < ε`). The Wedderburn decomposition indexing " +
        "these weights is generic upstream; what this lemma names is its " +
        "archimedean evaluation.",
    },
  ],
  label: "lem:feynman-eigenbasis-decomposition",
  lean: { ref: "qou:QOU.FeynmanPathIntegrals.eigenbasis_decomposition",
    validation: "not_checked",
  },
  title: "Eigenbasis decomposition for the Feynman amplitude",
  tags: ["schur-weyl", "eigenbasis", "feynman", "hecke", "decomposition"],
  uses: ["prop:knot-eigenbasis-complete"],
  proofs: ["prf:feynman-eigenbasis-decomposition"],
});
