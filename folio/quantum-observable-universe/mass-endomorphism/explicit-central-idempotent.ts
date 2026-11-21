import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:explicit-central-idempotent",
  title:
    "Explicit central primitive idempotents $e_\\lambda$ via Murphy elements",
  lean: {
    ref: "qou:QOU.BraidKnot.ExplicitCentralIdempotentGeneral.centralIdem_idem",
    validation: "not_checked",
  },
  uses: [
    "prop:jucys-murphy-central-elements-qou",
    "prop:hecke-baer-star-generic",
    // Was conj:explicit-central-idempotent (conditional). Promoted to a
    // theorem 2026-11-20 (owner ruling); this block is now unconditional.
    "thm:explicit-central-idempotent-cross-checks",
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Proposition (conditional on [`conj:explicit-central-idempotent`](#conj:explicit-central-idempotent)).**\n\nThe statement below is proved in Lean *conditionally* on the\nLagrange-interpolation cross-checks, which are axiomatised as the class\n`ExplicitCentralIdempotentConjecture q` and are **open**: no instance of\nthat class exists anywhere in the corpus. The four cross-checks\n(sum-to-identity, orthogonality, self-adjointness, bar-pairing) are the\nconjectural input; everything downstream of them is machine-checked.\n\n([`prop:jucys-murphy-central-elements-qou`](#prop:jucys-murphy-central-elements-qou))\n\nIt is standard in implementations like SageMath's `IwahoriHeckeAlgebra` and the local `pyhecke-native` module." },
    {
      kind: "status",
      date: "2026-11-20",
      body:
        "The idempotency this block proves conditionally is now proved unconditionally, at generic q, on the real Hecke " +
        "algebra: `QOU.BraidKnot.ExplicitCentralIdempotentGeneral.centralIdem_idem`, together with centrality, " +
        "orthogonality and sum-to-1 (`explicit_central_idempotent_cross_checks`). Sorry-free, in any characteristic. The " +
        "block's `lean.ref` names `centralIdem_idem`. The conditional theorem over the scalar carrier " +
        "`ExplicitCentralIdempotentConjecture`, and the carrier itself, were retired 2026-11-20 (owner); the relocated " +
        "note above that calls this block conditional is historical.",
    },
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
        "was asserting compliance without checking item 5. **FIXED the same day.** " +
        "The class now carries the interpolation inputs -- an index type of " +
        "standard tableaux, a projector per tableau, and the three properties " +
        "`proj_idem`, `proj_orth` and `centralIdempotent_eq_sum` -- and the " +
        "theorem DERIVES idempotency: expand the square, kill the " +
        "off-diagonal terms by orthogonality, collapse the diagonal by " +
        "idempotency of each projector. No field carries the conclusion, so " +
        "item 5 is satisfied and the --item5 evidence mode confirms it. Item 4, which this note was " +
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Hoefsmit seminormal matrices as $R$-matrix evaluations in $H_n(q)$](#prop:hoefsmit-seminormal-form))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Canonical q-deformed Wedderburn-block weight $\\tilde w_\\lambda$ and named scalings (BW, LP for all $\\lambda$)](#prop:wedderburn-weight-canonical))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): This is numerically verified in [Bring figure-8 volume as depth-2 grouplike value (50-digit numerical witness)](#conj:bring-figure-eight-depth-2-witness)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Elementary symmetric polynomials in Jucys–Murphy elements are central in $H_n(q)$ with closed-form spectrum on each Wedderburn block](#prop:jucys-murphy-central-elements-qou))" },
  ],
});
