import { prose } from "../../schema/builders";

export default prose({
  label: "sec:knot-notation-convention",
  title: "Knot and link notation",
  tags: ["notation", "convention", "knot", "link"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-21",
      body:
        "**Electron word ruling (owner, 2026-11-21) — not yet propagated through this block.** " +
        "The electron is now $\\sigma_0\\sigma_1\\sigma_0 \\in B_3$, whose closure is the Hopf link; " +
        "the trefoil $\\sigma_0^3 \\in B_2$ (leptons in $H_2$) is kept as the **backup** reading " +
        "(`docs/coordination/owner-rulings.md`). This block was written in the backup reading " +
        "(electron $= T(2,3)$, lepton tower $\\sigma_1^{2k+1}$ in $H_2$). Under the ruling: the " +
        "first-generation label $3$ survives as the crossing count of the word $\\sigma_0\\sigma_1\\sigma_0$; " +
        "the muon and tau entries ($T(2,5)$, $T(2,7)$) are not re-derived; and the closure of the " +
        "electron word is the same link type (Hopf link) that the notation table assigns to the gluon, " +
        "a collision not yet resolved.",
    },
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
