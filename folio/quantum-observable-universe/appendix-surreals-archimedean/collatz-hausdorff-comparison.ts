import { remark } from "../../schema/builders";

export default remark({
  label: "rem:collatz-hausdorff-comparison",
  title:
    "The Lyapunov function $\\Phi = \\log_q |P|$ and the Hausdorff phase transition",
  interprets: "conj:collatz-contact-boundary",
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
});
