import { remark } from "../../schema/builders";

export default remark({
  label: "rem:two-tier-scaling-pq",
  title:
    "Two-tier scaling of $P_K(q)$: quantum dimension $[N]_q$ (topological) and base mass $m_0$ (physical)",
  interprets: "rem:calibration-inputs",
  uses: [
    "conj:three-calibration-inputs",
    "def:three-calibration-discipline",
    "prop:markov-trace-axiomatic-closed-form",
    "rem:kashaev-volume-density",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([three calibration discipline](#def:three-calibration-discipline))" },
  ],
  tags: [
    "calibration",
    "mass-scale",
    "quantum-dimension",
    "markov-trace",
    "normalization",
    "boundary-conditions",
  ],
});
