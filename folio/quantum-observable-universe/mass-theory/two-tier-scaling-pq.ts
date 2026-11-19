import { remark } from "../../schema/builders";

export default remark({
  label: "rem:two-tier-scaling-pq",
  title:
    "Two-tier scaling of $P_K(q)$: quantum dimension $[N]_q$ (topological) and base mass $m_0$ (physical)",
  interprets: "rem:calibration-inputs",
  uses: [
    "prop:three-calibration-inputs",
    "def:three-calibration-discipline",
    "prop:markov-trace-axiomatic-closed-form",
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
  computation: {
    engine: "mpmath",
    script: "computations/atomic_tr_m_mpfr_50dps.py",
    witness: "computations/atomic-tr-m-mpfr-50dps.witness.json",
    status: "verified",
  },
});
