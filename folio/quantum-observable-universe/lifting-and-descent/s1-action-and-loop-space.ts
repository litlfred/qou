import { remark } from "../../schema/builders";

export default remark({
  label: "rem:s1-action-and-loop-space",
  title: "The circle action on Hochschild homology, the free loop space, and the Reeb generator",
  interprets: "def:hochschild-homology",
  uses: [
    "def:hochschild-homology",
    "rem:hkr-theorem",
    "def:categorical-reeb",
  ],
  cites: ["jones1987-cyclic", "loday-1998", "connes1994", "hadfield-krahmer-2005"],
  tags: ["hochschild-homology", "cyclic-homology", "free-loop-space", "connes-operator", "reeb", "cartan-calculus"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Part of the 2026-09-15 explicit-layer selection (owner option B). This is an analogy stated with its status: the circle action on `HH_•` is Connes' `B`, which under HKR is `d`; the QOU's Reeb generator with its Cartan calculus is a circle action at the algebraic level; the identification of the two on `HH_•(A)` for the substrate algebra is NOT established in the corpus, and the paragraph \"What would establish it\" names the computation that would.",
    },
  ],
});
