import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:coxeter-tits-residue-collapse",
  lean: {
    ref: "qou:QOU.Machinery.CoxeterParabolic.isReduced_iji_iff",
    validation: "not_checked",
  },
  title:
    "The Tits residue collapsed: cell faithfulness is simple-distinctness",
  tags: [
    "coxeter",
    "hecke-algebra",
    "faithfulness",
    "reflection-cocycle",
    "inversion-counting",
  ],
  uses: [
    "prop:coxeter-strong-exchange",
    "prop:coxeter-parabolic-transversal",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): , and which it settles\nunconditionally\n([simple-injectivity](#prop:coxeter-geometric-representation))" },
  ],
  cites: ["kassel1995", "jones1987"],
});
