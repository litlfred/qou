import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fourier-mukai-and-orlov",
  title: "Fourier–Mukai transforms and Orlov's theorem: where a derived realisation would close a gap",
  interprets: "lem:brings-euler-characteristic",
  uses: [
    "lem:brings-euler-characteristic",
    "def:chern-character",
    "def:hochschild-homology",
    "rem:hkr-theorem",
    "def:spatial-realization-functor",
    "rem:three-euler-characteristics",
  ],
  cites: ["caldararu-willerton-2010", "orlov1997", "bondal-orlov2001"],
  tags: ["fourier-mukai", "derived-category", "orlov", "bondal-orlov", "hochschild-homology", "trace-map", "brings-surface", "open-direction"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Part of the 2026-09-15 explicit-layer selection (owner option B), recording §11 of the analysis doc. A direction, not a closure: the corpus has no derived-level archimedean realisation (the fibre functor lands in Vect), so no integral transform exists to which Orlov's theorem could apply. The remark says what such a transform would give (a canonical trace map with trace ch(K)) and what it would force (the substrate's Hochschild dimensions to be the curve's, 2/4/4 and 1/4/9, with S₅-invariant parts 2/0/0 and 1/0/0 — the ledger in `QOU/Brings/S5CharactersOnBringDeformations.lean`).",
    },
  ],
});
