import { remark } from "../../schema/builders";

export default remark({
  label: "rem:einstein-nonsymmetric-metric-comparison",
  title:
    "Position against Einstein's non-symmetric field theory",
  interprets: "prop:crossing-energy-decomposition",
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-29",
      body:
        "Added after a corpus survey found the non-symmetric field-theory programme absent from every grep path. Comparison rationale, the three structural differences, and the retraction of an earlier (incorrect) reading of the $T_{2,9}$/$T_{3,5}$ selection as fitted are recorded in `docs/audits/2026-07-29-einstein-asymmetric-metric-vs-qou.md`.",
      see: "docs/audits/2026-07-29-einstein-asymmetric-metric-vs-qou.md",
    },
  ],
  uses: [
    "prop:crossing-energy-decomposition",
    "def:crossing-energy",
    "ex:braid-group-su2",
    "rem:crossing-energy-interpretation",
    "prop:em-coupling-projection",
    "rem:madelung-acoustic-metric",
    "rem:q-metric-contact-deformation",
    "rem:substrate-gm-torsion",
    "rem:lqg-adm-ashtekar-comparison",
  ],
  cites: [
    "einstein1925",
    "einstein1946",
    "einstein1955",
    "schrodinger1950",
    "damour1993",
    "moffat1995",
  ],
  tags: [
    "einstein",
    "nonsymmetric-metric",
    "unified-field-theory",
    "electromagnetism",
    "crossing-energy",
    "braiding",
    "comparison",
  ],
});
