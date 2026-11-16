import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:phi-q-categorical-truncation",
  title: "Brane-tower truncation depth = NF support depth (centre stratification)",
  lean: { ref: "qou:QOU.WedderburnMass.phi_q_categorical_truncation",
    validation: "not_checked",
  },
  uses: ["cor:habiro-expansion-atomic"],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "yekutieli",
    "regularization",
    "centre-stratification",
  ],
  authorNotes: [
    { kind: "status", date: "2026-11-16", body: "Demoted from proposition on owner ruling 2026-11-16 (card \"Demote all six\"): the claim is not proved from established results, so it is stated as a conjecture. Label renamed conj:phi-q-categorical-truncation -> conj:phi-q-categorical-truncation." },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "The statement uses 'GB-depth', which has no agreed definition (docs/audits/2026-08-16-three-gb-filtrations-one-name.md): ideal-power is zero above degree 0, Coxeter length fails a dimension count at n<=3, rewrite depth is zero on T_w. Scoping sentence added; queued for demotion until a filtration is fixed.",
    },
  ],
});
