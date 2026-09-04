import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:explicit-central-idempotent",
  title:
    "The four Murphy–Lagrange cross-checks for $e_\\lambda$ follow from Lagrange interpolation in commuting variables",
  lean: {
    ref: "qou:QOU.BraidKnot.ExplicitCentralIdempotent.ExplicitCentralIdempotentConjecture",
    validation: "not_checked",
  },
  uses: [
    "prop:jucys-murphy-central-elements-qou",
    "prop:hoefsmit-seminormal-form",
  ],
  cites: [],
  tags: [
    "central-idempotent",
    "murphy-elements",
    "lagrange-interpolation",
    "hecke-algebra",
    "open-problem",
    "primary-conjecture",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-04",
      body:
        "Registered to close bean `qou-1bua`. The class " +
        "`ExplicitCentralIdempotentConjecture` had been declared **only** " +
        "inside the sibling `.lean` of `prop:explicit-central-idempotent`, " +
        "with no `conj:` content block anywhere in the corpus. The Lean was " +
        "honest -- the proposition carries the class as an explicit instance " +
        "hypothesis (AGENTS.md ss3b-cond item 2) -- but item 4 asks that " +
        "`uses[]` name the conjecture so the conditional dependency is " +
        "auditable from the manifest, and there was no label to name. " +
        "`conjectural-propagation-audit.ts` reads `uses[]`, so the " +
        "proposition presented as a plain proposition with an EMPTY " +
        "conjectural cone: the audit could not see the gap, in the opposite " +
        "direction from the item-2 blindness measured in the same PR. " +
        "This block supplies the label; the class moved to the library " +
        "module `QOU.BraidKnot.ExplicitCentralIdempotent` so that both " +
        "blocks name one declaration rather than two copies (a sibling " +
        "`.lean` cannot import another sibling). No sibling `.lean` here, " +
        "per ss0a 'no shadowing stubs' -- the ref resolves to the library " +
        "declaration. Per ss3b-tax this is a PRIMARY conjecture (its " +
        "signature binds no other conjecture class) and correctly has NO " +
        "instance; do not fabricate one.",
    },
  ],
});
