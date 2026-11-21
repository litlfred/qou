import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:strangelet-crossing-energy",
  label: "rem:strangelet-witten-stability",
  title:
    "Witten's strange matter hypothesis as a crossing-energy inequality",
  tags: [
    "strangelet",
    "witten",
    "strange-quark-matter",
    "stability",
    "ground-state",
    "genus",
  ],
  uses: [
    "prop:strangelet-crossing-energy",
    "rem:golden-ratio-degeneration",
  ],
  cites: [
    "witten1984",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Assumed: the crossing-energy gain ($2q^{-1}$ per baryon) and the Jones-polynomial obstruction ($|J(q_0)|$ per quark) both take each quark to carry its lepton partner's knot. Under the ruling a quark is a single crossing letter of $\\mathcal{B}_3$, so both halves of the argument, and therefore the factor-93 conclusion, need re-scoping. Still valid: the Jones values in the table as values of the lepton-partner knots, and the reduction of Witten's hypothesis to a crossing-energy versus skein-cost comparison as a structure." },
  ],
});
