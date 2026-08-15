---
# qou-ungx
title: Registry JSON twin drifts silently from the .md — validator never compares them
status: todo
type: task
priority: normal
created_at: 2026-08-15T04:32:25Z
updated_at: 2026-08-15T04:32:55Z
---


Found 2026-08-15 while chasing the `q*` blast radius (`qou-kh7e`, PR #5074).

## The gap

`docs/coordination/ck-dk-canonical-registry.md` carries the human-readable rows;
`docs/coordination/kernel-constraints-registry.json` is its machine-readable twin
(the JSON even names the MD in an `authoritative_markdown` key). The validator
`kernel_constraints_registry_validate.py` loads **only the JSON** and lints
`docs/**/*.md` for conditional-decl citations. It **never compares a row's JSON
`statement` against the MD row it mirrors.** So the twin drifts silently.

## Two live instances, both found on the same read

| row | MD said | JSON still said |
|---|---|---|
| KC21 | `q*_S` "is **NOT** an independent third determination" (2026-08-15) | "the S=0 point q* is a third, decay-sector determination of q0 (mu-p-Q_beta three-way)" |
| KC22 | "**convergent**, radius `rho = 0.1428`" (CORRECTED 2026-08-09) | "super-exponentially divergent (q-Gevrey, radius -> 0 ...)" **and** "the odd-channel element is transcendental/resurgent (Ecalle acceleration class)" |

KC22 is the worse one: that correction landed **six days** earlier and the JSON
kept the withdrawn claim the whole time. Both are fixed in PR #5074 by hand.

This is the same failure mode the `q*` chase is about — a correction lands at one
site and never reaches the consumers that restate it — but here the consumer is
**machine-readable and named authoritative**, so an agent reading the JSON gets
the withdrawn claim with no marker that it was withdrawn.

## Proposed check (cheap, precise, low false-positive)

Add **R6** to the validator: for each row id, locate its `| KCnn |` row in the MD
and extract every strikethrough span `~~...~~`. Normalise (strip markdown
emphasis/backticks/whitespace, casefold) and assert that no such span appears in
the JSON `statement`. Strikethrough is the repo's existing withdrawal idiom, so
this catches exactly the class above with no prose-similarity heuristics.

Known limitation to state in the implementation: KC21's withdrawal used the
`**WITHDRAWN 2026-08-15**` marker *without* striking the quoted text, so R6 alone
would not have caught it. Either (a) also require that a row whose MD contains
`WITHDRAWN` has that word in its JSON statement, or (b) standardise on
strikethrough-plus-marker and say so in the registry header. (b) is better — one
idiom, mechanically checkable.

## Not in scope here

A general prose-equivalence check between MD row and JSON statement. The MD rows
are much richer than the JSON summaries by design; requiring equality would be
wrong and requiring similarity would be noisy.
