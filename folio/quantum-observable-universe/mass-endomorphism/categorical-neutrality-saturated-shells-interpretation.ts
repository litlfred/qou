import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:categorical-neutrality-saturated-shells",
  label: "rem:categorical-neutrality-saturated-shells-interpretation",
  title:
    "Self-conjugate support, the dropped locality assumption, and operator-level vs character-sum reading",
  tags: [
    "magic-numbers",
    "shell-closure",
    "full-twist",
    "global-section",
    "categorical-neutrality",
  ],
  uses: [
    "prop:categorical-neutrality-saturated-shells",
    "prop:hoefsmit-seminormal-form",
    "rem:phi-n-global-section",
    "conj:atom-knot-mass-derivation",
  ],
  cites: ["geckpfeiffer2000", "mathas1999"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: "Provenance for the $+0.74$ magic-shell correlation quoted in the prose (GS-filtration Term 6 plus the `is_magic_pair` operator-correction, against the AME residual) and for the operator-level vs. Plancherel-weighted-character-sum reading: `docs/audits/-self-conj-support-reframing.md`. The downstream cone for this conjecture is tabulated in `docs/audits/conjecture-cones.md`. Both are branch-local working notes, so neither is cited from the published prose.",
    },
  ],
});
