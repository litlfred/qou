---
# qou-ungx
title: Registry JSON twin drifts silently from the .md — validator never compares them
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T04:32:25Z
updated_at: 2026-11-16T20:10:00Z
parent: qou-trd0
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

## Implemented (2026-08-15, branch `claude/registry-r6-twin-drift-2026-08-15`)

R6 landed in `kernel_constraints_registry_validate.py`, split into three
sub-checks because the scoped design needed one refinement: the *current*
(post-#5074) JSON rows legitimately quote the withdrawn text inside the
`previously read here as established: "..."` idiom, so a bare substring
assert would false-positive on the correct twin. Resolution: **mention vs
assertion** — double-quoted segments of the JSON statement are masked
before matching.

- **R6a (error)**: a `~~struck~~` span from the row's `| KCnn |` MD line(s)
  must not appear (normalised: NFKD accent-fold, `sqrt` dropped,
  non-alphanumerics stripped, casefolded, ≥12 chars) in the JSON statement
  outside double quotes.
- **R6b (error)**: MD row has a WITHDRAWN marker ⇒ the JSON statement must
  contain WITHDRAWN. Transliteration-proof backstop; this alone catches
  BOTH live instances above (KC21 had marker-without-strikethrough, so R6a
  alone could not have caught it — exactly the known limitation this bean
  recorded).
- **R6c (warning)**: WITHDRAWN marker without strikethrough = idiom
  violation. Option (b) taken: the idiom (strikethrough **plus** marker) is
  now stated in the §9 header, and KC21's row was brought into compliance.

Regression-tested against reconstructed pre-#5074 KC21/KC22 statements
(KC21→R6b; KC22→R6a+R6b) and the current twin (0 errors, 0 R6 warnings).
Also fixed the one live missed §9f site the #5107 scoping found: the §9a
glyph-table "what it is" cell still called `q*_S` "a third, decay-sector
determination of q₀ (μ–p–Q_β three-way)"; now (H1)-conditional per §9f.

Validator: default 0 errors / 3 pre-existing R5 warnings; `--lint-docs`
adds 6 pre-existing doc-lint warnings (2026-06-05 scope doc); `--strict`
fails on those 9 pre-existing warnings exactly as it did before R6 (R6
contributes zero warnings on the current corpus).

Left open here: nothing from this bean's scope. PR #4767 (unmerged) also
uses the name "R6" for a different check (`doc_claims`) on its own branch;
whichever lands second renumbers.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-15 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 48 Execution Update (2026-11-16, PR #8161)

- **PR:** https://github.com/litlfred/qou/pull/8161 (`38bc15fe7214bb6951d6acb18fa8c8d7d32d5225`)
- **Action taken:**
  - Verified R6 (`R6a`, `R6b`, `R6c` in `check_twin_drift`) is live in `docs/coordination/kernel_constraints_registry_validate.py` (`22 rows, 0 error(s), 0 R6 warning(s)`).
  - Added `--self-test` / `--selftest` to `docs/coordination/kernel_constraints_registry_validate.py` regression-testing `check_twin_drift` on reconstructed pre-#5074 `KC21`/`KC22` drift cases, `R6c` idiom warning, quoted-withdrawal exemption, and the live registry, and excluded `.claude` from `docs_dir.rglob("*.md")`.
- **Status:** Kept `in-progress` pending PR #8161 merge and owner review.
