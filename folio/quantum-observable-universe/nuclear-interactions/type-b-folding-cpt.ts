import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:type-b-folding-cpt",
  title:
    "Type-B Cartan folding realises CPT via symmetric-crystal $\\mathbb{Z}/2$ fixed points",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.TypeBFoldingCpt",
    validation: "not_checked",
  },
  uses: [
    "conj:cpt-d6-d7-d8-closure",
    "conj:c-from-color-flavor-swap",
    "conj:p-from-braid-mirror",
    "conj:t-from-trace-cyclicity",
    "rem:breit-wheeler-vertex",
  ],
  cites: [
    "kashiwara1991",
    "khovanovlauda2009",
    "brundankleshchev2009",
    "lecouvey2007",
    "geck-lambropoulou-2004",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Scope at fixed q (owner decision D-H5 = D, relayed 2026-11-15; bean qou-hlx7). Lean, `QOU/QuarkState/HelicityCommonSource.lean`: Klein four-group `flip_flip`, `swap_swap`, `flip_neg`, `flip_swap`, `neg_hecke`; profiles `flip_Pp`, `swap_Pp`, `neg_Pp`, `positron_ne_electron`, `swap_electron`, `neg_electron`; non-linearity `no_linear_flip`, `no_linear_neg`. That q -> 1/q has no field automorphism of the reals behind it is a standard fact, not formalised. The conjecture's kind is unchanged.",
    },
  ],
  tags: [
    "type-b-folding",
    "duality-d22",
    "symmetric-crystal",
    "cpt",
    "matter-antimatter",
    "claude-md-7b",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
});
