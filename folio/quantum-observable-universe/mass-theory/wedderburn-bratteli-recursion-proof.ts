import { proof } from "../../schema/builders";

export default proof({
  label: "prf:wedderburn-bratteli-recursion",
  title: "Proof of wedderburn bratteli recursion",
  uses: ["prop:wedderburn-bratteli-recursion"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the symbolic linear-system solve in `y-lambda-symbolic-witness.json` — produced by sympy in $\\mathbb{Q}(q^{1/2})$." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The witness file [`y-lambda-jones-markov-witness.json`](https://github.com/litlfred/qou/blob/main/computations/y-lambda-jones-markov-witness.json) tabulates all 270 weights" },
  ],
});
