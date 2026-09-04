import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:explicit-central-idempotent",
  title:
    "Explicit central primitive idempotents $e_\\lambda$ via Murphy elements",
  lean: {
    ref: "qou:QOU.BraidKnot.ExplicitCentralIdempotent.explicit_central_idempotent_via_murphy",
    validation: "not_checked",
  },
  uses: [
    "prop:jucys-murphy-central-elements-qou",
    "prop:hecke-baer-star-generic",
    // conj:bring-figure-eight-depth-2-witness removed from uses[]
    // (2026-06-01 detangler Bucket-A): referenced only as numerical
    // corroboration ("verified numerically in (…)"), not a dependency
    // the idempotent construction builds on. Prose link retained.
  ],
  cites: [],
  tags: [
    "central-idempotent",
    "murphy-elements",
    "lagrange-interpolation",
    "hecke-algebra",
    "explicit-formula",
    "computability",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/explicit_central_idempotent_probe.py",
    witness: "computations/probes/explicit-central-idempotent-probe.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-04",
      body:
        "**AGENTS.md ss3b-cond item 4 is UNSATISFIABLE for this block as it " +
        "stands, and that is the finding.** The Lean theorem " +
        "`explicit_central_idempotent_via_murphy` correctly carries its " +
        "conjectural input as an explicit instance hypothesis " +
        "`[ExplicitCentralIdempotentConjecture q]` (item 2), and the " +
        "conditional banner is now on the .md (item 3). Item 4 asks that " +
        "`uses[]` name the conjecture explicitly -- but the class is declared " +
        "**only** in this block's own sibling `.lean` and has **no `conj:` " +
        "content block anywhere in the corpus** (grepped: no `conj:` label " +
        "mentions idempotent / Murphy / Lagrange / Wedderburn, and the class " +
        "name occurs in no other .lean). So the conjectural dependency is " +
        "invisible to `conjectural-propagation-audit.ts`, which reads " +
        "`uses[]`: this block reads as a plain proposition with no " +
        "conjectural cone. Registering a `conj:` block for the four " +
        "cross-checks would close it; that is a content addition, not a " +
        "compile fix, and is left open. Verified separately that **no " +
        "instance of the class exists** -- correct per ss3b-tax, an unproved " +
        "primary is a content-bearing class with no instance.",
    },
  ],
});
