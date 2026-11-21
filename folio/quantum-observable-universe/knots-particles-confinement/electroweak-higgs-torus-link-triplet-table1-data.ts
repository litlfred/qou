import { table } from "../../schema/builders";
export default table({
  label: "tbl:electroweak-higgs-torus-link-triplet-table1-data",
  title: "Data table 1 from conj:electroweak-higgs-torus-link-triplet",
  uses: ["conj:electroweak-higgs-torus-link-triplet"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): | Spectral completeness | [Two-strand spectral completeness](#thm:em-spectral-completeness) | open: [Plancherel completeness for the EW/Higgs idempotent decomposition](#conj:weak-spectral-completeness) |" },
    { kind: "note", date: "2026-11-21", body: "Main revised the relocated row after it was removed (conj -> prop); its revised text, kept verbatim: | Spectral completeness | [Two-strand spectral completeness](#thm:em-spectral-completeness) | [Weak-sector spectral completeness](#prop:weak-spectral-completeness) (exhaustion proved; the $W$, $Z$, $H$ naming is open) |" },
  ],
  tags: ["extracted-table"],
});
