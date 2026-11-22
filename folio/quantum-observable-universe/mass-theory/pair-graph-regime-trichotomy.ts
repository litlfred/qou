import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:pair-graph-regime-trichotomy",
  title:
    "Pair-graph regimes of $A$: $2\\bigl(\\binom A2-(3A-6)\\bigr)=(A-3)(A-4)$ splits $A\\ge2$ into $\\{2\\}$, $\\{3,4\\}$, $\\{\\ge5\\}$",
  lean: {
    ref: "qou:QOU.MassCore.PairGraphRegime.regime_trichotomy",
  },
  uses: [],
  tags: ["regime", "combinatorics", "pair-graph", "max-contact", "no-fit"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): It shows that the boundaries $2\\mid3$ and $4\\mid5$ used in [Mass formula regime switch](#conj:mass-formula-regime-switching) are determined by $A$ alone. It does not say which evaluation belongs to which regime; that assignment remains a selection against the measured target. The criterion was identified after the selected cut-offs were known, and is recorded as such." },
    {
      kind: "status",
      date: "2026-11-16",
      body: "Proved core of conj:mass-formula-regime-switching (issue #8094): the cut-offs 2 | 3-4 | >=5 depend on A alone. This criterion was identified after the AME-selected cut-offs were seen; it does not derive which evaluation belongs to which regime. Sorry-free sibling .lean, lean-direct exit 0.",
    },
  ],
});
