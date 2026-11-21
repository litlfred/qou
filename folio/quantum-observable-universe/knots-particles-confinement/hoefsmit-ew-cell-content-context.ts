import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hoefsmit-ew-cell-content-context",
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): (defined in [weak spectral completeness](#prop:weak-spectral-completeness))" },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): The ranks of the idempotents $E(\\epsilon_1, \\epsilon_2, \\epsilon_3)$ on $\\bigoplus_{\\lambda \\vdash 6} V_\\lambda$ are a different quantity, $11$ for $(s,s,s)$ and $(a,a,a)$ and $9$ for each of the six mixed patterns, by [weak spectral completeness](#prop:weak-spectral-completeness)." },
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): , and the boson-to-strand-pair assignment is part of [the categorical Higgs mechanism](#conj:categorical-higgs-mechanism). Neither is used by the theorem." },
  ],
  title: "Electroweak naming, minimality, interface-knot refinement, and further structure of the Hoefsmit electroweak cell content",
  interprets: "thm:hoefsmit-ew-cell-content",
  tags: ["hoefsmit", "electroweak", "torus-link", "plancherel"],
  uses: [
    "thm:hoefsmit-ew-cell-content",
    "conj:electroweak-higgs-torus-link-triplet",
    "conj:categorical-higgs-mechanism",
    "prop:weak-spectral-completeness",
  ],
  cites: ["morita1982"],
});
