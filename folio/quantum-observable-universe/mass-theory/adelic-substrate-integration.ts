import { remark } from "../../schema/builders";

export default remark({
  label: "rem:adelic-substrate-integration",
  title: "Motivation for the adelic substrate and Tate integration",
  interprets: "def:adelic-substrate",
  tags: ["adeles", "macroscopic-limit", "tate-integral", "global"],
  uses: [
    "def:adelic-substrate",
    "def:archimedean-realization-functor",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): of [classical Riemann zeta](#def:classical-riemann-zeta)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): already noted in\n[classical limit (preamble)](#sec:classical-limit-preamble)" },
  ],
  cites: ["tate1967"],
});
