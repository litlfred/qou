import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:phi-q-categorical-truncation",
  title: "Brane-tower truncation depth = NF support depth (centre stratification)",
  lean: { ref: "qou:QOU.WedderburnMass.phi_q_categorical_truncation",
    validation: "not_checked",
  },
  uses: ["cor:habiro-expansion-atomic", "prop:cell-depth-truncation"],
  tags: [
    "brane-tower",
    "spectral-sequence",
    "yekutieli",
    "regularization",
    "centre-stratification",
  ],
  authorNotes: [
    { kind: "status", date: "2026-11-16", body: "2026-11-16: GB-depth fixed as Lusztig's a-function (owner choice). Centre-projection part is prop:cell-depth-truncation items 1-3 (Lean-checked); it is vacuous on T_w (k_star = binom(n,2)). The level-wise Phi_q identity jointly with stabilisation is false (item 5). The k=2 cut-off is marked as an empirical comparison. No production number moves: compute evaluates the full product cut off by tolerance." },
    { kind: "status", date: "2026-11-16", body: "Demoted from proposition on owner ruling 2026-11-16 (card \"Demote all six\"): the claim is not proved from established results, so it is stated as a conjecture. Label renamed conj:phi-q-categorical-truncation -> conj:phi-q-categorical-truncation." },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "The statement uses 'GB-depth', which has no agreed definition (docs/audits/2026-08-16-three-gb-filtrations-one-name.md): ideal-power is zero above degree 0, Coxeter length fails a dimension count at n<=3, rewrite depth is zero on T_w. Scoping sentence added; queued for demotion until a filtration is fixed.",
    },
  ],
});
