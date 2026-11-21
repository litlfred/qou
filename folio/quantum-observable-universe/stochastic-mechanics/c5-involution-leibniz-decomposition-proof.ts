import { proof } from "../../schema/builders";

export default proof({
  label: "prf:c5-involution-leibniz-decomposition",
  title: "Proof of c5 involution leibniz decomposition",
  uses: ["prop:c5-involution-leibniz-decomposition"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, item 4a): Lean tactic:\n\n```lean\nfield_simp; ring_nf; linarith [Real.mul_self_sqrt (by norm_num : (2:ℝ) ≥ 0)]\n```" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Proofs (Lean $\\leftrightarrow$ paper bridge)\n\nEvery substantive Lean theorem in [`c5-involution-leibniz-decomposition.lean`](c5-involution-leibniz-decomposition.lean) has both a narrative proof here and a `sorry`-free Lean proof.\n\nLean tactic: `field_simp; ring`.\n\nBy `norm_num`.\n\n**Proposition.** `c5RationalMap(h(q)) = c5Decomposition(q)`.\n*Proof.* Direct rewrite via `c5_as_function_of_skein`. $\\square$\n\n*Proof.* Direct numerical computation via `norm_num`. $\\square$\n\nAll 24 substantive Lean theorems / definitions in the sibling have narrative proofs above. The Lean file is `sorry`-free." },
  ],
});
