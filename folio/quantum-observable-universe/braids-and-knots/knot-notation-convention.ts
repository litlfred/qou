import { prose } from "../../schema/builders";

export default prose({
  label: "sec:knot-notation-convention",
  title: "Knot and link notation",
  tags: ["notation", "convention", "knot", "link"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-21",
      body:
        "Quark rows re-read under the owner rulings of 2026-11-20 (a quark is " +
        "an unknot strand of $\\mathcal{B}_3$; $T_{2,n}$ is its lepton partner) " +
        "and 2026-11-21 (the magnitude $|\\kappa| = 3, 5, 7$ is the partner's " +
        "crossing count, a generation label; the sign is the quark strand's " +
        "crossing orientation). The quark entries now use the arrow " +
        "$\\leftarrow$ (has lepton partner) instead of $=$. Table 1's charm row " +
        "keeps the label $c^{\\sigma}$ in its antiparticle column, which this " +
        "block's own text says is the weak-isospin partner rather than the " +
        "antiquark; that column header predates this note and is not changed here.",
    },
  ],
});
