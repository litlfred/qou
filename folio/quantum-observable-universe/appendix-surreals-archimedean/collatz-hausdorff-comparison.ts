import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-hausdorff-comparison",
  title:
    "The Lyapunov function $\\Phi = \\log_q |P|$ and the Hausdorff phase transition",
  interprets: "prop:collatz-contact-boundary",
  uses: [
    "prop:collatz-no-cycles",
    "rem:hausdorff-dimension-recurrence",
  ],
  tags: [
    "collatz",
    "lyapunov",
    "hausdorff-dimension",
    "entropy",
    "contraction-mapping",
    "phase-transition",
    "superattraction",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/qbeta/qbeta_fsc_g_pattern_comparison.py",
    witness: "computations/qbeta/qbeta-fsc-g-pattern-comparison.witness.json",
    status: "verified",
  },
});
