import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:descent-reduction-two",
  title: "Reduction at dimension 2",
  tags: ["descent", "dimension-reduction", "surface", "brings-surface"],
  uses: [
    "ex:q-reeb-vector-field",
    "prop:brings-is-qou",
    "rem:descent-reduction",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This is the stratum Bring's surface occupies: the geometric :refterm[descent]{#descent} chain of [Bring's surface as a QOU](#prop:brings-is-qou) passes through $\\Sigma_4$ at this dimension." },
  ],
});
