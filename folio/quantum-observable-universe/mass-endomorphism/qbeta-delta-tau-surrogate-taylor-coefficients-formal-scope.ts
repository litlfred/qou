import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:qbeta-delta-tau-surrogate-taylor-coefficients",
  label: "rem:qbeta-delta-tau-surrogate-taylor-coefficients-formal-scope",
  title: "Formal scope: what the Lean catalogue establishes and defers",
  tags: ["qbeta", "delta-tau", "taylor-coefficients", "lean-scope"],
  uses: ["prop:qbeta-delta-tau-surrogate-taylor-coefficients"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): - The named function `delta_tau_M_surrogate_taylor_witness : ℕ → ℚ`\n  in Lean, which catalogues the coefficients $c_0, \\dots, c_7$ in the\n  canonical (borromean) frame, matching the witness. Its theorems are\n  reflexivity on the table and prove nothing about the surrogate itself.\n- Theorems about `delta_tau_M_surrogate` itself at every order\n  $0$ to $7$: vanishing" },
  ],
});
