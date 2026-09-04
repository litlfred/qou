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
    // AGENTS.md §3b-cond item 4: the conditional dependency is now
    // auditable from the manifest. The Lean theorem carries this as
    // [ExplicitCentralIdempotentConjecture q] (item 2); this edge is
    // what lets conjectural-propagation-audit.ts see the cone at all.
    "conj:explicit-central-idempotent",
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
        "**CORRECTION 2026-09-04: this note previously claimed ss3b-cond is " +
        "satisfied on ALL FIVE items. That is WRONG on item 5, and I wrote " +
        "it earlier the same day.** Item 5 forbids the class from carrying " +
        "the block's own conclusion: `ExplicitCentralIdempotentConjecture` " +
        "has exactly one field, `idempotent`, whose type IS this block's " +
        "conclusion universally quantified, and " +
        "`explicit_central_idempotent_via_murphy` discharges it by " +
        "`exact hi.idempotent lam h` -- a bare projection, which is the " +
        "self-assuming shape item 5 names. The defect is PRE-EXISTING (the " +
        "class and the projection both predate this work); what was mine " +
        "was asserting compliance without checking item 5. Fixing it means " +
        "re-encoding the class as the genuine sub-hypotheses of the " +
        "Lagrange-interpolation argument -- the JM diagonal action and the " +
        "interpolation step -- so the theorem COMPOSES them; that is real " +
        "mathematical work and is left open. Item 4, which this note was " +
        "originally about, IS closed.** " +
        "Item 2 was already met -- the Lean theorem " +
        "`explicit_central_idempotent_via_murphy` carries its conjectural " +
        "input as an explicit instance hypothesis " +
        "`[ExplicitCentralIdempotentConjecture q]` -- and item 3's " +
        "conditional banner is on the .md. Item 4 asks that `uses[]` name " +
        "the conjecture, and until 2026-09-04 there was no label to name: " +
        "the class was declared only in this block's own sibling `.lean` " +
        "and had no `conj:` content block anywhere in the corpus. So " +
        "`conjectural-propagation-audit.ts`, which reads `uses[]`, saw an " +
        "EMPTY conjectural cone and this block presented as a plain " +
        "proposition -- the opposite blindness direction from the item-2 " +
        "gap measured in the same PR, and invisible to the same audit. " +
        "Closed by registering `conj:explicit-central-idempotent` and " +
        "adding it to `uses[]` above. The class itself moved to the " +
        "library module `QOU.BraidKnot.ExplicitCentralIdempotent` so that " +
        "the two blocks name ONE declaration: a content-block sibling " +
        "`.lean` cannot import another sibling, so leaving the class here " +
        "would have forced two independent copies -- the divergence shape " +
        "recorded in docs/audits/2026-09-03-sibling-lean-compile-sweep.md. " +
        "Still verified: **no instance of the class exists** anywhere, " +
        "correct per ss3b-tax for an unproved primary conjecture.",
    },
  ],
});
