import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:magic-numbers-from-q",
  label: "rem:magic-numbers-from-q-computation",
  title: "Magic numbers from $q$: computation, $q$-dependence, and homological route",
  tags: ["magic-numbers", "hoefsmit", "shell-closure", "computation"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The file `shell-closure.witness.json` records $\\delta^2 \\Phi(Z)$ for $Z = 1\\ldots 30$ at $K = 10$. The block-diagonal optimised computation resides in `shell_closure_compute.py`." },
  ],
});
