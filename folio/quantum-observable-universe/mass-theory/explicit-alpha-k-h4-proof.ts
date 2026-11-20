import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:explicit-alpha-k-h4",
  label: "rem:explicit-alpha-k-h4-proof-sketch",
  title: "Proof sketch: explicit alpha k h4",
  uses: ["conj:explicit-alpha-k-h4"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the $5 \\times 5$ character matrix at $q_0$ is recorded in [`wedderburn-orthogonal-r-3-h4.witness.json`](https://github.com/litlfred/qou/blob/main/computations/wedderburn-orthogonal-r-3-h4.witness.json).\n\nThe check is `computations/probes/explicit_alpha_k_h4_exact_check.py`." },
  ],
});
