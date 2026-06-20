# Canonical-axis QA fails — current-state triage (2026-06-03)

> Companion to PR [#1755](https://github.com/litlfred/qou/pull/1755) (post-merge cleanup; lake env unblocked).
> The [2026-06-02 canonical-axis staleness audit](2026-06-02-qa-backlog-canonical-axis-staleness-audit.md)
> predicted **7 of 11** then-open fails would clear with a sweep refresh.
> The refresh already ran (every block's `reviewed_at` is now
> `2026-06-02T19:34:22Z`) — the old 11 cleared, but a **different 11**
> are now open on two different criteria. This doc triages the
> current 11.

## Headline

The current 11 are **real content-discipline issues**, not stale
metadata. Two patterns, neither resolvable by a sweep refresh:

| pattern | criterion | count | suggested route |
|---|---|---:|---|
| A | `canonical-no-negative-result-in-paper` | 7 | content edit OR criterion refinement |
| B | `canonical-ck-tiered-not-binary` | 4 | content edit (rewrite to tiered framing) |

One block (`rem:m-tau-knot-prediction`) is flagged under both
criteria — counts as 2 entries but 1 fix-site.

## Pattern A — `canonical-no-negative-result-in-paper` (7 blocks)

Criterion: paper blocks should not carry the `scaffolding` or
`negative-result` tag — per AGENTS.md authoring discipline +
[`2026-05-31-ck-exploratory-probes-removed.md`](2026-05-31-ck-exploratory-probes-removed.md),
primary content of those kinds belongs under `docs/audits/`.

### A.1 `scaffolding` tag (5 blocks)

Each block's **manifest** (`.ts` — source-of-truth for tags / `uses[]` / `interprets`) carries `tags: [..., "scaffolding", ...]`. The links below point to the **`.md` narrative** per house style (AGENTS.md "Always provide GitHub links — default to `.md`"); the sibling `.ts` is at the same path with a `.ts` extension.

| block | label |
|---|---|
| [`braids-and-knots/braid-group-n-strand.md`](../../content/quantum-observable-universe/braids-and-knots/braid-group-n-strand.md) | `rem:braid-group-n-strand` |
| [`braids-and-knots/markov-trace-inductive-limit.md`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-inductive-limit.md) | `rem:markov-trace-inductive-limit` |
| [`braids-and-knots/markov-trace-operator-construction.md`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-operator-construction.md) | `rem:markov-trace-operator-construction` |
| [`braids-and-knots/hecke-algebra-type-scaffold.md`](../../content/quantum-observable-universe/braids-and-knots/hecke-algebra-type-scaffold.md) | `rem:hecke-algebra-type-scaffold` |
| [`mass-endomorphism/chi-v21-hoefsmit-matrix-derivation.md`](../../content/quantum-observable-universe/mass-endomorphism/chi-v21-hoefsmit-matrix-derivation.md) | `rem:chi-v21-hoefsmit-matrix-derivation` |

**Key wrinkle**: spot-checking `braid-group-n-strand.ts` line 7
shows the block is titled *"axiomatic scaffolding generalising the
2-strand B_2 foundation"* — i.e. "scaffolding" here means the
legitimate *categorical / structural* sense (foundation being built
up), **not** the *WIP placeholder* sense the criterion is gating on.

**Decision needed (owner judgment):** for each of these 5, choose

  1. **Retag** — rename the `"scaffolding"` tag to something
     non-flagged (e.g. `"foundational"`, `"axiomatic"`,
     `"structural-buildup"`).
  2. **Move to audits** — per the criterion, transfer the block to
     `docs/audits/` and replace the paper block with a forward
     reference.
  3. **Refine the criterion** — distinguish *"axiomatic
     scaffolding"* (legit content; `kind: "remark"` with formal
     backing) from *"WIP scaffolding"* (audit-doc material). The
     checker in `content/pipeline/qa-checkers-canonical.ts` would
     gain a context-sensitivity rule.

Recommend **3** for the 4 `braids-and-knots/` blocks (they have
formal Lean siblings and `interprets` backing — real content) and
**1 or 2** for `chi-v21-hoefsmit-matrix-derivation` (needs
inspection — possible WIP).

### A.2 `negative-result` tag (2 blocks)

| block | label |
|---|---|
| [`observations/m-tau-knot-prediction.md`](../../content/quantum-observable-universe/observations/m-tau-knot-prediction.md) | `rem:m-tau-knot-prediction` |
| [`observations/isospin-mirror-v9-empirical-near-match.md`](../../content/quantum-observable-universe/observations/isospin-mirror-v9-empirical-near-match.md) | `rem:isospin-mirror-v9-empirical-near-match` |

These are the more clear-cut cases — the `.ts` manifest's tag is
`"negative-result"`, matching the criterion's intent. The block
content is observation-of-empirical-failure material. **Route 2
(move to audits)** is the canonical disposition.

`m-tau-knot-prediction` is ALSO flagged under Pattern B (see
below) — the same block, two pieces of evidence; one fix-site
disposes of both entries.

## Pattern B — `canonical-ck-tiered-not-binary` (4 blocks)

Criterion: precision-ladder blocks must not use binary
"negative result" framing without the tiered (proved / near-match
/ fitted) frame from
[AGENTS.md "Q_β c_k truncation order canonical framing"](./2026-05-31-qbeta-ck-truncation-order-canonical-framing.md)
(Rule 4 — "report TIERED, never binary").

| block | label | line(s) | fix-site phrase |
|---|---|---|---|
| [`predicted-spectra/e-hartree-categorical-derivation.md`](../../content/quantum-observable-universe/predicted-spectra/e-hartree-categorical-derivation.md) | `conj:e-hartree-categorical-derivation` | 161 | "negative result" |
| [`mass-theory/chirality-writhe-ribbon-derivation.md`](../../content/quantum-observable-universe/mass-theory/chirality-writhe-ribbon-derivation.md) | `prop:chirality-writhe-ribbon-derivation` | 116 | "negative result" |
| [`mass-theory/terms-2-6-higher-operations.md`](../../content/quantum-observable-universe/mass-theory/terms-2-6-higher-operations.md) | `prop:terms-2-6-higher-operations` | 52 | "**DECISIVE NEGATIVE RESULT**" |
| [`observations/m-tau-knot-prediction.md`](../../content/quantum-observable-universe/observations/m-tau-knot-prediction.md) | `rem:m-tau-knot-prediction` | 93, 129 | "negative result" / "Negative result" |

**Fix template (mechanical-ish):** wrap each "negative result"
phrase in tiered framing:

```diff
- **DECISIVE NEGATIVE RESULT: HH¹(H_3(R, q)) = 0.**
+ **Proved (Taylor-exact at q_0): HH¹(H_3(R, q)) = 0.**
+ This rules out the previously-proposed Hochschild-mechanism c_k
+ ansatz (mech #N in the c_k flip-flop history); see
+ [`docs/coordination/1ppq-qbeta.md`](../../docs/coordination/1ppq-qbeta.md).
```

i.e. **state the result + classify the disposition under the
tiered framework + reference the c_k flip-flop log**. Avoids the
re-open-the-wire-flop trap the criterion is gating against.

Per-block work: ~5-10 min each (read context, rewrite the framing
sentence, leave the math statement untouched). Total: ~30 min for
all 4.

## Recommended disposition (priority order)

1. **`m-tau-knot-prediction`** — single fix-site, clears 2 entries
   (one under each pattern). Route: move to `docs/audits/` + add a
   forward-reference remark in `observations/`.
2. **`isospin-mirror-v9-empirical-near-match`** — clear `negative-result`
   tag case; move to audits. ~10 min.
3. **Pattern B (4 entries)** — mechanical tiered-framing rewrite per
   the fix-template above. ~30 min total.
4. **Pattern A.1 5 `"scaffolding"` blocks** — needs owner decision
   between retag / move / refine-criterion. Recommend option 3
   (refine criterion to distinguish axiomatic vs WIP scaffolding)
   for the 4 `braids-and-knots/` blocks; option 1 or 2 for
   `chi-v21-hoefsmit-matrix-derivation` after inspection.

## Pattern observation (cross-session)

This is the **fourth consecutive QA-axis** where a same-day audit
predicts staleness, the sweep refreshes, and a **different** real
backlog emerges. Sequence:

- Lean discharge queue: PR [#1720](https://github.com/litlfred/qou/pull/1720) audit → PR [#1747](https://github.com/litlfred/qou/pull/1747) (via [#1755](https://github.com/litlfred/qou/pull/1755)) marked 6 of 9 stale/re-scope
- Canonical (axis-1, 2026-06-02): predicted 7/11 stale → sweep refresh → 11 new real fails (this doc)

The recurring pattern: **sidecar `result: "fail"` entries persist
through silent content fixes (which clear the underlying issue but
don't re-run the sweep), then a *different* batch of real
discipline issues accumulates until the next audit**.

The 2026-06-02 audit's "make `/integration-audit <axis>` a CI cron
job" suggestion is the right structural fix. Tracking as a separate
ledger item.

## Out of scope for this PR

This doc is **triage only** — no content edits. The actual fixes
(11 blocks across two patterns) are in separate follow-up branches
to keep reviews focused. Per AGENTS.md "Combine related work into
one branch", Pattern B (4 mechanical rewrites) can go on one
branch; Pattern A (7 with owner judgment) is better split.

## Cross-refs

- [`docs/audits/2026-06-02-qa-backlog-canonical-axis-staleness-audit.md`](./2026-06-02-qa-backlog-canonical-axis-staleness-audit.md) — companion 2026-06-02 audit (now stale itself)
- [`docs/audits/2026-05-31-ck-exploratory-probes-removed.md`](./2026-05-31-ck-exploratory-probes-removed.md) — canonical authoring discipline for negative-result content
- [`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](./2026-05-31-qbeta-ck-truncation-order-canonical-framing.md) — tiered framing rule for precision ladders
- [`.claude/skills/local/integration-audit.md`](../../.claude/skills/local/integration-audit.md) — sidecar-invalidation utility (could be CI-cron candidate)
