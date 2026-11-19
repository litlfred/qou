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
        /* <!-- literal-source: historical residual of superseded colour-blind specialisation before interface separation --> */
        "carried a systematic $5.1139\\times10^{-9}$ discrepancy against the " +
        "canonical word on all four of D, T, $^3$He, $^4$He. The cause is the " +
        "substitution this block's statement avoids: raising the $ud$ factor " +
        "to the power $2A+1$ folds the colour-weighted p-n interface in as if " +
        "it were a $ud$ letter. Carrying it as itself takes the residual to " +
        "$1.2\\times10^{-14}$, which is the residual of the character " +
        "accumulation itself, not a property of the word's offsets: those are " +
        "exact.",
    },
    {
      kind: "note",
      date: "2026-08-26",
      body:
        "**Retracted, same day.** An earlier version of this note claimed both " +
        "constructors of the atomic word emit float64 interface offsets, " +
        "capping any character built from them at $\\sim10^{-15}$. That is " +
        "false. `atom_braid_word_3A` builds $h$ and $\\delta$ inside " +
        "`workdps(max(dps, 60))` from the 50-digit $q_0$ and " +
        "`flavor_split_leading`; measured against the closed form, its $ud$ " +
        "and p-n offsets have relative error exactly zero at 60 dps. The " +
        "float64 belonged to a since-deleted local rebuild in the H_12 " +
        "branching cone, and the error was attributing a one-sided difference " +
        "to both sides.",
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
