import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-q-categorical-truncation",
  title: "Brane-tower truncation depth = NF support depth (centre stratification)",
  lean: { ref: "qou:QOU.WedderburnMass.phi_q_categorical_truncation",
    validation: "not_checked",
  },
  uses: ["cor:habiro-expansion-atomic"],
  proofs: ["prf:phi-q-categorical-truncation"],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "yekutieli",
    "regularization",
    "centre-stratification",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "The statement uses 'GB-depth', which has no agreed definition (docs/audits/2026-08-16-three-gb-filtrations-one-name.md): ideal-power is zero above degree 0, Coxeter length fails a dimension count at n<=3, rewrite depth is zero on T_w. Scoping sentence added; queued for demotion until a filtration is fixed.",
    },
  ],
});
