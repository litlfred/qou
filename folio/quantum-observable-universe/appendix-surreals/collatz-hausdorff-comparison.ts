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
    "archimedean-bridge",
    "collatz",
    "lyapunov",
    "hausdorff-dimension",
    "entropy",
    "contraction-mapping",
    "phase-transition",
    "superattraction",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-28", body: "Status paragraph added: heuristic; log_q|P| undefined on Laurent polynomials; P=1 outside the domain; q0 figures use the retiring muon pin." },
  ],
});
