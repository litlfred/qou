import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lr-coefficient-hecke",
  title:
    "Littlewood-Richardson coefficient $c^\\lambda_{\\mu\\nu}$ for Iwahori-Hecke branching",
  chapter: "mass-theory",
  cites: ["wenzl1988", "ariki1996", "ram1991"],
  uses: [],
  defines: [],
  tags: [
    "littlewood-richardson",
    "branching",
    "hecke-algebra",
    "wedderburn",
    "non-negative-integer",
  ],
  lean: { ref: "qou:QOU.BraidKnot.LRCoefficientHecke" },
  authorNotes: [
    {
      kind: "status",
      body: "**Statement.** Proven in the symmetric-function literature\n(\\cite{macdonald1995} §I.9, \\cite{stanley1999} §A1.3) and the\nHecke deformation (\\cite{ariki1996}). For QOU, the proof is consumed\nas a class hypothesis via the\n[`LRCoefficientHecke`](#prop:lr-coefficient-hecke) Lean class — the\nnon-negativity, integrality, and the LR-tableau formula are all\nrecorded as class fields, sorry-free per AGENTS.md §3b-cond.\n\nDownstream consumers ([`def:wenzl-A-operator`](wenzl-A-operator.md),\n[`prop:crystal-r-matrix-sub-lemma`](crystal-r-matrix-sub-lemma.md),\n[`prop:operator-valued-combiner-convergence`](operator-valued-combiner-convergence.md))\ntake `[LRCoefficientHecke]` as an explicit class hypothesis.",
    },
  ],
});
