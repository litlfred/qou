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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3):  That proposition is proved in Lean *conditionally* on them, with the class carrying them as an explicit instance hypothesis. Naming the conjecture as its own block is what lets the proposition's `uses[]` record the dependency, so the conditional cone is auditable from the manifest and not only from the Lean signature.\n\nThe conjecture remains open. The carrier is the class `QOU.BraidKnot.ExplicitCentralIdempotent.ExplicitCentralIdempotentConjecture`, whose field states cross-check 2 — the one downstream Lean consumes — quantified over every partition of every $n$, so it is a claim about the whole construction and not about one $\\lambda$. **No instance of the class exists anywhere in the corpus**, which is the correct representation of an unproved primary conjecture: an instance would assert the statement, not prove it.\n\n## Scope of the Lean carrier\n\nThe class carries the **interpolation-theoretic inputs**,\n\nstated above but are still not encoded — they have no downstream consumer yet.\nOrthogonality is now encoded, at the projector level, because idempotency needs\nit. The class has **no instance**: the conjecture is open." },
    {
      kind: "refined-framing",
      date: "2026-09-04",
      body: "**This replaces an earlier encoding that violated AGENTS.md §3b-cond item 5.**\nUntil 2026-09-04 the class had a single field whose type *was*\n[`prop:explicit-central-idempotent`](#prop:explicit-central-idempotent)'s\nconclusion, discharged by a bare projection `exact hi.idempotent lam h` — so\nthe \"conditional theorem\" proved nothing modulo the class. Caught by the\n`--item5` mode of `scripts/conditional-on-class-hypothesis-audit.ts`; the fix\nwas to axiomatise what interpolation actually supplies and let the theorem\ncompose it.",
    },
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
        "instance; do not fabricate one. **Re-encoded the same day**: the class " +
        "first carried a single field equal to the downstream conclusion, " +
        "discharged by a bare projection -- a ss3b-cond item-5 violation, " +
        "caught by the --item5 mode of " +
        "scripts/conditional-on-class-hypothesis-audit.ts. It now carries the " +
        "interpolation inputs (per-tableau projectors, idempotent and " +
        "pairwise orthogonal, summing to e_lambda) and the theorem DERIVES " +
        "idempotency from them.",
    },
  ],
});
