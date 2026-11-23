import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:wedderburn-bratteli-recursion",
  label: "rem:wedderburn-bratteli-recursion-proof-sketch",
  title: "Proof sketch: wedderburn bratteli recursion",
  uses: ["conj:wedderburn-bratteli-recursion"],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Moved out of the prose by the voice-leak drain (qou-d4kh, W14b, 2026-11-21): Lean: three-row weights vanish by `QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`; the recursion is `QOU.BraidsAndKnots.wedderburn_bratteli_recursion` with `jonesWeightD_edge_row`, `jonesWeightD_edge_col` (sorry-free over a generic field); the n = 3 weights are `jonesWeightD_h3`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The witness file [`y-lambda-jones-markov-witness.json`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-jones-markov-witness.json) tabulates all 270 weights\n\nthe symbolic linear-system solve in `y-lambda-symbolic-witness.json` — produced by sympy in $\\mathbb{Q}(q^{1/2})$." },
  ],
});
