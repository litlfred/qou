import { remark } from "../../schema/builders";

export default remark({
  label: "rem:two-tier-scaling-pq",
  title:
    "Two-tier scaling of $P_K(q)$: quantum dimension $[N]_q$ (topological) and base mass $m_0$ (physical)",
  interprets: "rem:calibration-inputs",
  uses: [
    "rem:calibration-inputs",
    "prop:three-calibration-inputs",
    "prop:three-calibration-discipline",
    "prop:categorical-mass-markov",
    "prop:markov-trace-axiomatic-closed-form",
    "prop:reidemeister-mass-invariance",
    "rem:kashaev-volume-density",
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
