import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "caveat",
      date: "2026-08-01",
      body:
        "**Claims 1-2 and 4 corrected.** The previous claims 1-2 stated $E_{\\mathrm{sym}} = \\sum_i |\\epsilon_i|\\cosh(\\ln q)\\,\\mathrm{sgn}(\\epsilon_i)$ and likewise for $E_{\\mathrm{asym}}$. Those evaluate to $(pq - mq^{-1})\\cosh\\lambda$ and $(pq - mq^{-1})\\sinh\\lambda$, whose sum is $q\\,\\mathfrak{E}_{\\mathrm{cross}}$ — " +
        /* <!-- literal-source: closed-form evaluation of 3*q_0^2 = 3.696167 vs 3*q_0 = 3.329940 at q_0, p=3, m=0 --> */
        "an overshoot by a factor of $q$ (numerically $3.696167$ against the true $3.329940$ at $q_0$, $p=3$, $m=0$), so they were not a decomposition. Giving both channels the same $\\mathrm{sgn}$ factor also made claim 4's ratio look composite-independent; that independence was an artifact and now carries the positive-braid hypothesis. Claim 3 and every worked number elsewhere in the corpus (the $T_{2,3}$ table, the $e^-e^+$ pair at $6\\sinh\\lambda$) already matched the corrected form, so no downstream value moves. Claim 2 additionally now distinguishes the parity of the weight *functions* from that of the channel *totals*.",
      see: "docs/audits/2026-07-29-einstein-asymmetric-metric-vs-qou.md",
    },
  ],
  label: "prop:crossing-energy-decomposition",
  lean: { ref: "qou:QOU.Braiding.crossingEnergy_split" },
  title: "Crossing energy decomposes into strong and Coulomb channels",
  uses: ["def:crossing-energy"],
  examples: ["rem:pair-creation-energy", "rem:virtual-particles-exceptional-divisor", "rem:electron-immortality", "rem:crossing-energy-decomposition"],
  tags: [
    "crossing-energy", "strong-force", "coulomb", "decomposition",
    "hyperbolic",
  ],
});
