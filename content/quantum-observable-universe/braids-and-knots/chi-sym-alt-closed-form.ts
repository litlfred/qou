import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:chi-sym-alt-closed-form",
  title:
    "Closed form for $\\chi_{\\mathrm{sym}}(\\beta)\\,\\chi_{\\mathrm{alt}}(\\beta)$ " +
    "on the atomic word, with the colour-weighted interface carried exactly",
  lean: {
    ref: "qou:QOU.ChiSymAlt.chiPairProductC_eq",
  },
  uses: [],
  cites: [
    "jones1987",
    "kassel1995",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/chi_sym_alt_closed_form.py",
    witness: "computations/chi-sym-alt-closed-form.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-26",
      body:
        "The colour-blind specialisation was the form stated first, and it " +
        "carried a systematic $5.1139\\times10^{-9}$ discrepancy against the " +
        "canonical word on all four of D, T, $^3$He, $^4$He. The cause is the " +
        "substitution this block's statement avoids: raising the $ud$ factor " +
        "to the power $2A+1$ folds the colour-weighted p-n interface in as if " +
        "it were a $ud$ letter. Carrying it as itself takes the residual to " +
        "$1.2\\times10^{-14}$, the float64 floor of the word's own offsets.",
    },
    {
      kind: "caveat",
      date: "2026-08-26",
      body:
        "Both constructors of the atomic word emit float64 interface offsets " +
        "(`atom_braid_word_3A` wraps one in `mpf`), so any character built " +
        "from them is capped at $\\sim10^{-15}$ regardless of the working " +
        "precision downstream. The stationarity identity is exact; the " +
        "numerical agreement is not better than that cap.",
    },
  ],
  tags: [
    "hecke-character",
    "wedderburn",
    "atomic-braid-word",
    "colour-weighting",
    "closed-form",
    "categorical-derivation",
  ],
});
