import { definition } from "../../schema/builders";

export default definition({
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-21", body: "Rewritten from the paper arXiv:math/0602138 (Leitner 2006, library `arxiv-math-0602138v1`). The previous text said the lift is \"obtained by integrating $\\pi_<$ in the sense of Fresse\" and that $\\mathrm{Dist}(\\widehat G)$ is a $p$-adic completion of a deformed enveloping algebra. That paper works over a field of characteristic $p$ throughout and constructs no lift to $W(k)$, so the claim had no source; it is removed. The Lean is stated over an arbitrary ring map $\\varphi$, because Mathlib's `WittVector` oleans are not in the restored cache; specialising $\\varphi$ to $W(k)\\to k$ gives this definition." },
  ],
  label: "def:witt-vector-lift",
  lean: { ref: "qou:QOU.WittVectorLift", validation: "not_checked" },
  title: "Witt vector lift of a formal group",
  uses: [],
});
