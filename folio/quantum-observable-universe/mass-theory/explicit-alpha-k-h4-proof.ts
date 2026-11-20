import { proof } from "../../schema/builders";

export default proof({
  label: "prf:explicit-alpha-k-h4",
  title: "Proof of explicit alpha k h4",
  uses: ["prop:explicit-alpha-k-h4"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): at $q_0$ it reproduces the numerical solution. The check is\n`computations/probes/explicit_alpha_k_h4_exact_check.py`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): character matrix at $q_0$ is recorded in\n[`wedderburn-orthogonal-r-3-h4.witness.json`](https://github.com/litlfred/qou/blob/main/computations/wedderburn-orthogonal-r-3-h4.witness.json)." },
  ],
});
