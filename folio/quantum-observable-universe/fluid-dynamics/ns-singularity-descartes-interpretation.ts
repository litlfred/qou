import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:ns-singularity-descartes",
  label: "rem:ns-singularity-descartes-interpretation",
  title: "What $\\chi(\\mathcal{S})=-6$ fixes about the Reeb bundle, and what it does not",
  uses: ["thm:ns-singularity-descartes"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped by owner decision (PR #7747, bean qou-fm7s, option 1: re-scope the files " +
        "that still stated the withdrawn Levi branch (A)). The remark interpreted the retracted " +
        "NS-singularity form of the theorem. Old title: \"Arithmetic constraint $\\chi(A)=-6$ as a " +
        "topological forcing term\". Old text, verbatim: \"**Mathematical novelty.** The proof " +
        "combines four conditional geometric inputs (Kummer tower survival, persistent obstruction, " +
        "core-Levi bounding, BKM divergence) into a single deterministic criterion. It bypasses " +
        "brute-force PDE estimates, using the arithmetic constraint $\\chi(A)=-6$ as a global " +
        "topological forcing term that dictates finite-time blowup through categorical mechanics " +
        "alone.\" Withdrawn because the theorem now states only topological facts (restated " +
        "2026-10-12) and the core-Levi input is withdrawn (conj:levi-degeneracy, branch (A) refuted " +
        "by a Beltrami solution).",
      see: "thm:ns-singularity-descartes",
    },
  ],
});
