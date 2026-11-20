import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vol-through-tau",
  title:
    "$\\mathrm{Vol}(K)$ factors strictly through the fibre functor $\\tau$",
  tags: ["fibre-functor", "knot-volume", "archimedean", "factorization"],
  foreshadows: ["conj:kashaev-volume-conjecture"],
  uses: [
    "def:archimedean-realization-functor",
    "conj:kashaev-volume-conjecture",
  ],
  cites: ["kashaev1997", "murakami-murakami2001"],
  lean: {
    ref: "qou:QOU.BraidsKnots.vol_through_tau_of_volumeConjecture",
    validation: "not_checked",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): this composition is the Lean-derived step, with the Kashaev identification consumed as the class hypothesis rather than asserted." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): , Lean class `VolumeConjecture`, field `kvc_holds`)" },
    {
      kind: "refined-framing",
      date: "2026-08-25",
      body: "**Quantifier corrected 2026-08-25 (PR #5765).** This read *\"for every braid $\\beta \\in H_n(R,q)$\"* — which conflates a **braid** (an element of $B_n$, which has a closure) with a general **Hecke element** (an element of $H_n(R,q)$, which does not). $\\rho : B_n \\to H_n(R,q)$ is neither injective nor surjective, and the statement is only meaningful on its image.\n\nThis is not pedantry: the production binding pipeline evaluates $\\mathrm{tr}_M$ on `atom_braid_word_3A`, whose letters are $c\\,\\sigma_g + d\\,\\mathbf{1}$ — **general Hecke elements, not braid generators**. Read with the old quantifier, this proposition appeared to license a volume for that object. It does not, and the corresponding $\\mathrm{Vol}$ is in fact $0$ ([`2026-08-25-atom-word-closures-are-not-hyperbolic.md`](../../../docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md)).",
    },
  ],
});
