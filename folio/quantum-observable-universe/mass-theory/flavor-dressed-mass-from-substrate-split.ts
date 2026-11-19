import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:flavor-dressed-mass-from-substrate-split",
  lean: { ref: "qou:QOU.FlavorDressing.dressed_mass_from_substrate_split",
    validation: "not_checked",
  },
  title: "Aether-pure derivation of the dressed-quark mass splitting",
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-23",
      body:
        "**The sibling this block resolved to carried an axiom from which " +
        "`False` is derivable, and it had been fixed everywhere else** " +
        "(bean `qou-lo1t`). `QOU/FlavorDressing/DressedMassFromSubstrateSplit.lean` " +
        "records that `axiom dressed_mass_split_substrate_closed_form` made the " +
        "library inconsistent and demoted it to a class on 2026-08-08. The " +
        "content sibling `flavor-dressed-mass-from-substrate-split.lean` still " +
        "held the axiom verbatim — and per §0a the sibling resolves *first*, so " +
        "this block pointed at the unsound copy, not the repaired one.\n\n" +
        "Re-verified rather than taken on trust: appending a `False` derivation " +
        "to the sibling unchanged compiles, exit 0. `F`, `M_N` and `q` are " +
        "mutually unconstrained, so the constant dressing `μ ≡ 1` forces " +
        "`substrate_split_factor 2 = 0` while that expression is concretely " +
        "positive.\n\n" +
        "Sibling deleted; all three of its declarations exist in the library, " +
        "which carries the honest §3b-cond form — a `DressedMassSubstrateSplit` " +
        "class with no instance, so the open state lives in the type.",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "Worth keeping for the provenance, which the library docstring already " +
        "records: a review (Gemini #696) flagged the downstream theorem as a " +
        "**tautology**, and the repair was to introduce the axiom. The old " +
        "docstring then argued the result was \"no longer a tautology … a " +
        "substantive equality backed by the axiomatised closed form\". Both the " +
        "objection and the response were about emptiness; neither checked " +
        "soundness, and the statement stopped being empty by starting to be " +
        "false. Per AGENTS.md §\"Axiomatization is NOT a Proof\", an axiom " +
        "whose statement *is* the theorem's statement does not discharge it.",
    },
  ],
  tags: [
    "flavor",
    "dressing",
    "quark-mass",
    "substrate-derived",
    "no-fit",
  ],
  uses: [
    "def:flavor-dressing-functor",
    "prop:flavor-split-substrate",
    "lem:pair-skein-mass-formula",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probe_flavor_dressed_mass_split.py",
    witness: "computations/flavor-dressed-mass-from-substrate-split.witness.json",
    status: "verified",
  },
});
