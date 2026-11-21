import { example } from "../../schema/builders";

export default example({
  label: "ex:brings-surface-concrete",
  title: "Bring's surface as a concrete genus-4 curve",
  interprets: "def:brings-surface",
  uses: ["def:brings-surface", "def:archimedean-condition"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([the $\\chi_{\\mathrm{eu}}(M_0) = -6$ chain](#ex:chi-minus-six-derivation))" },
  ],
  tags: ["brings-surface", "genus-4", "example"],
});
