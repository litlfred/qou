import { proof } from "../../schema/builders";

export default proof({
  label: "prf:alpha-em-shift-multiplicative-chain",
  title: "Proof of alpha em shift multiplicative chain",
  uses: ["prop:alpha-em-shift-multiplicative-chain"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Numerical re-evaluation at $q_0$ ([`alpha-em-shift-multiplicative-chain.witness.json`](../../../computations/alpha/alpha-em-shift-multiplicative-chain.witness.json), mpmath 50-dps) reads $\\alpha_{\\mathrm{shift}}(T_{2,9})$ and $\\alpha_{\\mathrm{shift}}(T_{3,5})$ from the upstream witness [`alpha-shift-torus.witness.json`](../../../computations/alpha/alpha-shift-torus.witness.json). It compares" },
  ],
});
