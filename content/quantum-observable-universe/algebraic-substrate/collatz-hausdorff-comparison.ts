import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-hausdorff-comparison",
  title:
    "The Lyapunov function $\\Phi = \\log_q |P|$ and the Hausdorff phase transition",
  interprets: "prop:collatz-contact-boundary",
  uses: [
    "conj:q-collatz",
    "prop:collatz-contact-boundary",
    "prop:collatz-no-cycles",
    "rem:hausdorff-dimension-recurrence",
    "def:operational-entropy",
    "prop:reeb-operations-per-planck",
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
});
