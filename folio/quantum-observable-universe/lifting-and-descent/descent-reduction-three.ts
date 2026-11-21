import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:descent-reduction-three",
  title: "Reduction at dimension 3",
  tags: ["descent", "dimension-reduction", "reeb", "contact"],
  uses: [
    "ex:q-reeb-vector-field",
    "prop:brings-is-qou",
    "rem:descent-reduction-two",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The Bring realisation sits here as $M_S$, with $\\dim M_S = 3$ ([Bring's surface as a QOU](#prop:brings-is-qou))." },
  ],
});
