import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:gs-archimedean-agreement-trace",
  title:
    "Archimedean agreement: Habiro polynomial trace evaluates to GB mass",
  lean: {
    ref:
      "qou:QOU.BraidKnot.HabiroResidueSumEquivalence.archimedean_agreement",
    validation: "not_checked",
  },
  uses: [
    "prop:habiro-residue-sum-equivalence",
    "def:archimedean-realization-functor",
    "conj:gs-spectral-decomposition-existence",
  ],
  cites: ["habiro2004"],
  tags: [
    "gs-filtration",
    "spectral-sequence",
    "habiro-ring",
    "archimedean-agreement",
    "equivalence",
    "noncomputable-opaque",
    "audit-flag-13a",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Conjectural status.** A Lean proof requires the spectral decomposition existence, the `tail_in_ideal` axiom for the Habiro completion, and the analytic identification of the residues." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean encoding.** Encoded as the class field axiom `archimedean_agreement`. Instances supply it as a substrate axiom." },
  ],
});
