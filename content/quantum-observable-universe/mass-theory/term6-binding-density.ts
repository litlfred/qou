import { remark } from "../../schema/builders";

export default remark({
  label: "rem:term6-binding-density",
  title:
    "Term 6 binding density: $B(Z,N)/A \\approx \\alpha \\cdot T_6(Z,N)/A^3 + \\beta + \\delta_M(Z,N)$",
  interprets: "prop:gb-spectral-sequence",
  tags: [
    "binding-energy",
    "derivation-chain",
    "gs-filtration",
    "spectral-sequence",
    "term-6",
    "level-3-stratum",
    "calibrated-fit",
    "magic-shell-correction",
  ],
  uses: [
    "prop:wigner-np-pairing",
    "prop:categorical-neutrality-saturated-shells",
  ],
  cites: ["bethe1936", "weizsacker1935", "geckpfeiffer2000"],
  authorNotes: [
    {
      kind: "status",
      body: "**Structurally-shaped, empirically-calibrated.** The two\ncalibration parameters $(\\alpha, \\beta)$ improve on the\nfive-parameter Bethe–Weizsäcker SEMF, with $R^2 = 0.84$ across\n$A = 2$–$58$. A genuine categorical derivation of $\\alpha$ and\n$\\beta$ from the framework's first-principles structures\nremains the open work needed to promote this result to an\n**unconditional** proposition.\n\nThe 16-atom panel demonstrates the formula's reach; extension\nto medium-heavy nuclei ($A = 100$–$200$) will further constrain\n$\\alpha$ and may expose any structural breakdown.",
    },
  ],
});
