import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:confinement-categorical",
  label: "rem:eigenbasis-structural-lemmas",
  title: "Content/twist eigenbasis: structural lemmas behind the Wedderburn characters",
  tags: ["hecke-character", "ribbon-eigenvalue", "eigenbasis", "confinement"],
  uses: ["prop:confinement-categorical"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: "The title previously ended \"(Lean)\". It was dropped because nothing formalises items 1–3: this block has no `.lean` sibling and no `lean.ref`, and `QOU.BraidKnot.CrossingEnergyBarParity` — the nearest Lean from the same PR — is about the crossing-energy Laurent scalar $E_\\times$, not about character parity, conjugation duality, or the framing rational. Formalising the three items is tracked as bean `qou-lw3v`.",
    },
  ],
});
