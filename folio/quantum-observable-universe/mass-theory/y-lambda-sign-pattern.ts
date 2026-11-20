import { remark } from "../../schema/builders";

export default remark({
  label: "rem:y-lambda-sign-pattern",
  title:
    "Jones–Markov block weights $y_\\lambda$ are not individually non-negative for $n \\geq 4$",
  interprets: "conj:alpha-k-derivation-procedure",
  uses: [
    "conj:alpha-k-derivation-procedure",
    "conj:explicit-alpha-k-h3",
  ],
  tags: [
    "jones-markov",
    "y-lambda",
    "positivity",
    "sign-pattern",
    "lp-feasibility",
    "structural-observation",
    "alternating-block",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3):  identically for $\\ell(\\lambda) \\geq 3$ ([`TemperleyLiebTower.lean`](../lean/QOU/QBeta/TemperleyLiebTower.lean))." },
  ],
});
