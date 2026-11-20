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
      kind: "status",
      date: "2026-11-20",
      body:
        "**Cross-checks 1 and 2, and centrality, are now PROVED for every n (bean qou-2150).** " +
        "`QOU.BraidKnot.ExplicitCentralIdempotentGeneral.explicit_central_idempotent_cross_checks`: at generic q (q != 0, " +
        "not a root of unity, characteristic 0) the Murphy-Lagrange elements e_lambda in the real Hecke algebra are " +
        "central, idempotent, pairwise orthogonal and sum to 1. `mulProj_eq_proj` shows that the boxed formula in the " +
        "multiplicative J_k equals the corpus' additive-JM projector, and `heckeWedderburn_symm_single` (JMProjector) maps " +
        "that projector to the matrix unit E_TT. Sorry-free; axioms propext, Classical.choice, Quot.sound. Still OPEN: " +
        "cross-checks 3 and 4 (self-adjointness and bar-pairing under the bar involution). Primitivity is not stated in " +
        "Lean. `lean.ref` still names the old scalar carrier; re-pointing it waits on the owner.",
    },
    {
      kind: "status",
      date: "2026-11-20",
      body:
        "**Re-statement on the real Hecke algebra started (owner ruling D2, 2026-11-20; bean qou-2150).** " +
        "The current carrier `ExplicitCentralIdempotentConjecture` states the conjecture about an opaque scalar in a " +
        "commutative ring, so no proof can be written against it. New module " +
        "`QOU.BraidKnot.ExplicitCentralIdempotentHecke` builds the Murphy-Lagrange projectors in " +
        "`QOU.SchurWeyl.Hecke` from the Murphy elements `qJM`. It proves the n = 2 case sorry-free " +
        "(`murphyLagrangeComplete_two`): the projectors for shapes (2) and (1,1) are idempotent, orthogonal and sum to 1, " +
        "for q*qi = 1 and q^2 != qi^2. The general statement over all standard Young tableaux is not yet written, so " +
        "`lean.ref` still names the old carrier, and the conjecture stays open.",
    },
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
