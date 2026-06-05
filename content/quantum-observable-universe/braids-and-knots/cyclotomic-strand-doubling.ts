import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:cyclotomic-strand-doubling",
  title:
    "Cyclotomic doubling identity: $\\Phi_8(X) = \\Phi_4(X^2)$",
  lean: {
    ref: "qou:QOU.BraidKnot.CyclotomicStrandDoubling.cyclotomic_8_eq_cyclotomic_4_comp_X_sq",
  },
  uses: [
    "prop:habiro-pochhammer-bridge",
  ],
  cites: [
    "habiro2000",
  ],
  tags: [
    "habiro-ring",
    "cyclotomic",
    "strand-doubling",
    "1ppQ",
    "draft",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-01",
      body: "The strand-doubling interpretation was falsified 2026-06-01; see the cross-referenced audit docs in the `.md`.",
    },
  ],
});
