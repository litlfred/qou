import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-q-resums-trace-series",
  interprets: "conj:six-term-mass-formula-complete",
  title:
    "$\\Phi_q$ resums an infinite series of Markov traces",
  uses: [
    "conj:six-term-mass-formula-complete",
    "prop:phi-q-aj-machinery-identification",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The context-sorting of $\\Phi_q$ against $\\mathrm{Li}_2^q$ — which saddle regime this resummation lives in — is fixed once by the [$\\Phi_q$/AJ machinery identification](#prop:phi-q-aj-machinery-identification)." },
  ],
  tags: ["mass-tower", "markov-trace", "audit", "exposition"],
});
