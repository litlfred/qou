# Convention: narrative proofs are separate `proof` blocks

**Status:** the mechanism already exists in the platform and is in use
(~170 proof blocks). This doc records the convention and the audit/QA
gap. Adopted/clarified 2026-06-24 (author directive: "narrative proof as
a separate `.md`, part of the content block, to track easier").

## The mechanism (already supported — no schema change needed)

A provable block's narrative proof is its **own content block** of kind
`proof`, a sibling triple sharing the parent's root name plus `-proof`:

```
<name>.ts          parent provable block (theorem/lemma/proposition/corollary)
<name>.md          the STATEMENT (+ motivation)
<name>.lean        formalization
<name>-proof.ts    proof block:  proof({ label:"prf:<name>", title, uses:["<parent-label>"] })
<name>-proof.md    the narrative PROOF  ← the separate .md the author asked for
```

Three links make it first-class and trackable:

1. **Proof block** `<name>-proof.ts` — `export default proof({ label:
   "prf:<name>", title: "Proof of …", uses: ["prop:<name>"] })`.
2. **Parent links down** — the provable block carries
   `proofs: ["prf:<name>"]`.
3. **Chapter manifest lists it** — add `"<name>-proof"` to the section's
   `blocks: [...]` array, right after `"<name>"`.

The render pipeline already emits `<name>-proof.md` inside a proof
environment after the statement. So "does this block have a paper proof?"
is answered by **file/link presence** — exactly the trackability the
author wants — without a prose heuristic.

### Authoring a proof `.md`

- Same markdown/TeX conventions as any `.md` (inline `$…$`, display
  `$$…$$`, fenced ```tex, cross-refs `[text](#label)`).
- **Do not** add a `**Proof.**` header or a trailing `∎` expectation as a
  hard rule — match the surrounding chapter; existing proof blocks open
  directly with the argument and close with `$\qquad\blacksquare$`.
- Keep it **human-readable**. When a step becomes pedantic combinatorics
  or bookkeeping, state the structure and **refer to the Lean witness**
  (e.g. "(`QOU.Mass.evenPart_fixed`, using $\sigma^2=\mathrm{id}$)")
  rather than belabouring it in prose. The `.lean` is the rigorous record;
  the `.md` is the readable account.
- When a sorry-free Lean proof exists, the `.md` should be a faithful
  account of the *same* argument (`proof-narrative-lean-equiv` adjudicates
  drift).

### Deliberate exemptions (no proof block expected)

Some provable blocks cite an external/axiomatic result instead of proving
it internally (e.g. `thm:jones-markov-trace` → Jones 1987). These need no
proof block; the citation lives in the statement `.md`. (A manifest
`proof?: "external" | "definitional"` marker is proposed in the
folio-assistant requirements so the audit can distinguish "deliberately
external" from "missing".)

## Audit + QA

- **Audit:** `bun run content/pipeline/audit-narrative-proof-presence.ts`
  reports, per chapter, provable blocks with vs. without a linked
  non-trivial proof block. Current state: **167** covered, **492** gaps.
- **Proposed QA criterion** `proof-narrative-present` (folio-assistant
  `qa-criteria-registry.ts §PROOF`): `pass` iff a linked non-trivial proof
  block exists, or the block is marked external/definitional. This is the
  only genuinely *new* platform work — the proof block kind, the `proofs`
  field, and rendering already exist. See
  [`narrative-proof-sidecar-folio-assistant-requirements.md`](narrative-proof-sidecar-folio-assistant-requirements.md).

## Drain

Fill the 492 gaps incrementally (largest chapters first: mass-theory 198,
particle-interactions 53, predicted-spectra 44): for each provable block
without a proof block, add `<name>-proof.{ts,md}`, the parent `proofs`
link, and the chapter-manifest entry — OR mark it external/definitional.
Tracked in bean `k65k` (children `i7fd` drain, `i4fx` folio-assistant QA
criterion).
