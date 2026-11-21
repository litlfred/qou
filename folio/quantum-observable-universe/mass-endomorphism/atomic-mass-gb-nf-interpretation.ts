import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:atomic-mass-gb-nf",
  label: "rem:atomic-mass-gb-nf-interpretation",
  title: "Three equivalent forms, the density factor $\\rho_K$, and Class-A discipline status",
  tags: [
    "mass",
    "atomic-mass",
    "markov-trace",
    "categorical-density",
    "three-calibration-discipline",
  ],
  uses: [
    "prop:atomic-mass-gb-nf",
    "prop:categorical-mass-markov",
    "prop:rho-k-graded-expansion",
    "prop:alpha-shift-torus-knot",
    "prop:alpha-em-shift-multiplicative-chain",
    "conj:binding-scale-catalan",
    "sec:atomic-braid-mass-foundations",
    "prop:per-nucleon-shift-additive-linearity",
    "thm:wedderburn-mass-formula",
    "thm:knot-mass-formula-unified",
  ],
  cites: ["kassel1995", "jones1987"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): verified to $3.2 \\times 10^{-14}$ in `rho-k-markov-multiplicativity.witness.json`)\n\n## Witnesses\n\n* `rho-k-codata-vs-six-term.witness.json` — $\\rho_K^{\\mathrm{CODATA}}$ vs $\\rho_K^{6\\text{-term}}$ table for $A = 1, 2, 3$.\n* `rho-k-scaling-structure.witness.json` — leading-order ansatz $\\rho_K \\approx (Z m_{\\mathfrak{p}} + N m_{\\mathfrak{n}})/(m_e \\cdot |\\!\\mathrm{tr}_M\\!|)$ ($0.14\\%$ mean residual); mirror-pair analysis.\n* `atomic-tr-m-mpfr-50dps.witness.json` — canonical $\\lvert\\!\\mathrm{tr}_M(\\mathrm{NF}_{\\mathrm{GS}}(\\mathcal{B}_K))\\!\\rvert$ at $50$ decimal-place precision.\n* `atom-mass-atomic-braid.witness.json` — (constituent) form $m_e$-scaled mass renderings.\n* `paper-six-term-isotope-sweep.witness.json` — (six-term spectral) $m_e$-scaled mass renderings across all five tower modes." },
  ],
});
