# Forward-ref cluster fix: mass-endomorphism → mass-theory (17 edges)

Tracks the disposition of the largest logical-defect cluster surfaced
by [`forward_ref_classifier.py`](../folio-assistant/computations/forward_ref_classifier.py)
(see [`forward-ref-logical-analysis.md`](forward-ref-logical-analysis.md)).

## Triage result (read-only inspection)

| Finding | Evidence |
|---------|----------|
| 11 of 12 cluster **source** blocks are Lean-sorry-free | a sorry-free proof that declares a forward `uses[]` edge usually over-declares — the proof compiles without consuming the target ⇒ the edge is a narrative citation, not a logical dependency |
| `prop:mass-endomorphism` is a **genuine conjecture** mislabeled `prop:` | title "Mass endomorphism *conjecture*"; body "**Conjecture (explicit mass endomorphism)**"; Lean `class MassEndomorphism` with unproved `vol_eq` field |
| The conjecture is **not load-bearing** | the block's own prose (§"Scope: convenience target, not load-bearing") states the mass formula `thm:knot-mass-formula-unified` + `prop:mass-endomorphism-tower` "does **not** depend on the closed-form conjecture below" |
| §3b-cond already implemented in Lean | downstream results take `[M : MassEndomorphism R β]` and are proved sorry-free as conditional theorems |

## Disposition rule (per edge)

1. **Over-declared edge → rewire.** Source proof is sorry-free and does
   not actually consume the later target: drop the forward `uses[]`,
   repoint to the *proved* upstream result
   (`prop:mass-endomorphism-tower` / `thm:knot-mass-formula-unified`)
   or express as a narrative forward-pointer.
2. **Genuine conjecture → relabel** `prop:`→`conjecture` (only the
   irreducibly-open blocks — `prop:mass-endomorphism`,
   `prop:rho-k-pair-gen-canonical-form`).
3. **Conditional consumer → keep `prop:`, add §3b-cond banner.** A block
   downstream of a conjecture stays provable, proved modulo the named
   `[conj:C]` Lean class hypothesis + a "conditional on conj:C" banner.

## Edges (17)

Source blocks (sorry-free unless noted):
`prop:mass-endomorphism`, `prop:rho-k-pair-gen-canonical-form`,
`prop:markov-trace-axiomatic-closed-form`,
`prop:tau-M-asymptotic-rep-theory`, `prop:explicit-central-idempotent`,
`prop:homological-shell-condensation`,
`prop:categorical-chain-convergence-mechanisms`,
`prop:atomic-mass-gb-nf`, `prop:categorical-mass-markov`,
`prop:markov-trace-recursive-reducer`,
`prop:q-hecke-seminormal-character-closure`,
`def:qou-motivic-galois-instance` (2 Lean sorries).

## Gate

Re-run the classifier after each disposition; the logical-defect count
must drop monotonically (current baseline: 91). Regenerate
`forward-ref-classification.witness.json`.
