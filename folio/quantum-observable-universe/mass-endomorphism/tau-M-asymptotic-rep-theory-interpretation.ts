import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:tau-M-asymptotic-rep-theory",
  label: "rem:tau-M-asymptotic-rep-theory-interpretation",
  title:
    "Four complementary rep-theory anchors for the rung coefficients and their synthesis",
  tags: [
    "hecke-algebra",
    "kashiwara-crystal",
    "jucys-murphy",
    "macdonald-polynomial",
    "habiro-residue",
    "rep-theory-prediction",
  ],
  uses: [
    "prop:tau-M-asymptotic-rep-theory",
    "prop:habiro-residue-sum-equivalence",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  cites: ["kashiwara1990", "macdonald1995", "habiro2002"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Habiro completion ≡ Gröbner–Shirshov residue spectral sum (equivalence)](#prop:habiro-residue-sum-equivalence))" },
  ],
});
