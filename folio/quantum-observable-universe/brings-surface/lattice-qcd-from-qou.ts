import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:qu-to-qou",
  label: "rem:lattice-qcd-from-qou",
  title:
    "Lattice gauge theory as a proposed $q\\to 1$ shadow of the $q$-deformed surface state-sum",
  tags: ["yekutieli", "brings-surface", "non-abelian-stokes", "lattice-gauge"],
  cites: ["broda2002"],
  uses: [
    "thm:qu-to-qou",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-02",
      body:
        "Empirical-tier interpretive remark, not a derivation. The state-sum / " +
        "lattice-gauge correspondence is conjectural; numerical agreement with " +
        "lattice-QCD is an evidence-tier cross-check (below a Lean proof). " +
        "Formalization is tracked in bean `qou-1puy`.",
    },
  ],
});
