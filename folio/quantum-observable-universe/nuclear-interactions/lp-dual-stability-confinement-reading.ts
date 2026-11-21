import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:lp-dual-stability",
  label: "rem:lp-dual-stability-confinement-reading",
  title: "Confinement reading of the LP-dual stability criterion",
  tags: ["lp-duality", "confinement", "hadron", "quark", "shadow-price"],
  uses: ["prop:lp-dual-stability"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "The shadow-price bound and the sub-braid instability were claims 2 and 3 of `prop:lp-dual-stability` until this date. Neither follows from linear-programming duality: both are claimed properties of the specific Gram matrix at the substrate. Neither is currently checked: `computations/confinement-operator-selection.py` builds a singular Gram matrix (det ≈ −1.5e−17, rank 5, inverted by pseudoinverse), so the condition number κ(G) ≈ 7.0 cannot hold, and the script computes no shadow prices. The computation link was removed for that reason. They moved here on owner instruction (\"1 2\", thread \"N2 Lean foundations\") when the proposition was narrowed to the two claims Lean derives.",
    },
  ],
});
