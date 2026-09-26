---
# qou-k520
title: 'VALIDATE WARNINGS (10): 5x missing chap:particle-interactions, 3x no Lean decl, 1 dangling remark, 1 missing rem ref'
status: completed
type: task
created_at: 2026-08-07T10:42:40Z
updated_at: 2026-08-07T15:35:00Z
---


## Status: PRE-EXISTING on `main` — verified 2026-08-07

Same 10 warnings on a clean `origin/main` checkout as on feature branches. Non-blocking
(`run-validate` fails on the 2 errors in `qou-idd2`, not on these), but they are real and
they are the kind of rot that accumulates silently.

## Grouped by root cause — 4 groups, not 10 problems

### G1 — `chap:particle-interactions` does not exist (5 warnings, ONE cause)

```
⚠ [chapter-overview]                  Undefined cross-reference: chap:particle-interactions
⚠ [approach-to-exceptional-divisor]   Undefined cross-reference: chap:particle-interactions
⚠ [thurston-relaxation]               Undefined cross-reference: chap:particle-interactions
⚠ [observations-intro]                Undefined cross-reference: chap:particle-interactions
⚠ [ns-blowup-physical-evidence]       Undefined cross-reference: chap:particle-interactions
```

Five blocks reference a chapter label that is not defined. Either the chapter was renamed /
never landed, or the label is wrong in all five. **Resolve once, fix five.** Check first
whether a particle-interactions chapter exists under a different label before adding one.

### G2 — proposition with no Lean declaration yet (3 warnings)

```
⚠ [meson-octet-decomposition]    prop:meson-octet-decomposition: no Lean declaration yet
⚠ [borromean-decuplet-derivation] prop:borromean-decuplet:       no Lean declaration yet
⚠ [tm-gs-normal-form]            prop:tm-gs-normal-form:         no Lean declaration yet
```

Expected-but-missing per the kind→Lean table (`proposition` warns if absent). These are
**honest** warnings — the blocks are not lying about their status. Each is a formalization
task; size them individually rather than as a batch.

### G3 — dangling remark (1 warning)

```
⚠ [einstein-ether-substrate]  rem:einstein-ether-substrate: remark has no `interprets` field
```

Per AGENTS.md §3a the fix is one of three: promote the claim to a `proposition`/`lemma`,
add `interprets:` pointing at the provable it interprets, or demote to `prose` if it makes no
logical claim. **Read the block before choosing** — the right disposition depends on whether
it asserts anything.

### G4 — undefined remark reference (1 warning)

```
⚠ [meson-em-sinh-closed-form]  Undefined cross-reference: rem:fine-structure-data
```

Same shape as G1 but a single target. Check whether `rem:fine-structure-data` was renamed or
removed.

## Reproduce

```bash
bash scripts/setup-folio-assistant.sh
bun run scripts/run-validate.ts content/quantum-observable-universe
```

## Suggested order

G1 first (5-for-1 payoff), then G4 (same shape), then G3 (needs a judgement call), then G2
(three separate formalization tasks — do not bundle).

## Definition of done

`run-validate` warning count 10 → 0, or each survivor explicitly justified in this bean as
intentional.


## PROGRESS (2026-08-07): 10 warnings → 3

**G1 (5 warnings) — DONE.** Root cause found: `chap:particle-interactions` was **split** into
`knots-particles-confinement` + `nuclear-interactions`; the old chapter directory survived but
is **not registered** in the paper manifest (only a comment mentions it), so its label exists
yet cannot resolve. Section headers made the split boundary unambiguous — the orphan's §1/§2 and
§4–§9 went to `nuclear-interactions`, its §3 to `knots-particles-confinement`. Retargeted per
reference, not globally:

| block | now points at | why |
|---|---|---|
| `approach-to-exceptional-divisor` | `chap:nuclear-interactions` | SDP/LP machinery = orphan §2 |
| `thurston-relaxation` | `chap:nuclear-interactions` | algebraic SDP solver = orphan §2 |
| `observations-intro` | `chap:nuclear-interactions` | GS engine + Wedderburn mass = orphan §1, §8 |
| `ns-blowup-physical-evidence` | `chap:knots-particles-confinement` | knot-braid particle model |
| `chapter-overview` | rewritten — see below | described a chapter that no longer exists |

**Bigger finding inside G1.** The introduction's chapter tour did not merely have a stale link
— it was **missing three real content chapters**: `knots-particles-confinement`,
`eightfold-way`, and `nuclear-interactions` (0 mentions each). Two are the split successors;
`eightfold-way` is an independent gap. The defunct paragraph was replaced with three, in
reading order, matching each chapter's actual section content.

**G3 (1) — DONE.** `rem:einstein-ether-substrate` now `interprets:
prop:calibration-cohomology-alignment`. Chose `interprets` over demotion-to-`prose` because
the remark does lean on a provable statement — "q₀ is fixed by the cohomological structure of
`H¹(Bring) = 2W`" is what carries the Einstein analogy.

**G4 (1) — DONE.** Filename-vs-label mismatch: the block file is `fine-structure-data.ts` but
its label is `rem:fine-structure-observation`. Reference retargeted.

**G2 (3) — REMAINS.** Three propositions with no Lean declaration:
`prop:meson-octet-decomposition`, `prop:borromean-decuplet`, `prop:tm-gs-normal-form`. Honest
warnings; three separate formalization tasks. Do not bundle.

## Progress — 10 → 1 (branch `claude/convention-systematic-audit-2026-08-07`)

G1 (5), G3 (1), G4 (1) resolved earlier in this PR. G2 (3 propositions with no
Lean) is now 1:

- `prop:meson-octet-decomposition` — drained. `MesonOctetTracelessSplit.lean`.
- `prop:borromean-decuplet` — drained. `SymmetricChannelDimension.lean`:
  `dim_K {degree-n forms in N vars} = C(N+n-1, n)`, general in `N`, `n` and the
  base ring, sorry-free, standard axioms only. The numerals are DERIVED from it
  (`N=3 → 10`, `N=2 → 4`) and `decuplet_ne_quadruplet` machine-checks the
  block's anti-fitting conditional. Deliberately NOT `Nat.choose 5 3 = 10`.
- `prop:tm-gs-normal-form` — drained. `GSNormalForm.lean`. Formalises the two
  things the appendix's proof ARGUES and leaves what it CITES cited: the block
  step `(cσ+d)(aσ+b) → T(c,d) ⬝ᵥ (a,b)`, derived FROM the Hecke relation
  (negative control: without it `ring` fails, leaving exactly
  `a*c*(σ² − qq*σ − 1)`), and normality — a strictly increasing index word
  contains no leading word of any of the three rule families. Confluence stays
  cited to Bergman; H_A(q) is not constructed and the global block-locality
  induction remains prose. All three scope limits recorded in the docstring
  and the `.ts`.

**`run-validate` exits 0 with 0 issues. 10 → 0; definition of done met.**

## Two PLATFORM defects surfaced while doing this (folio-assistant, not qou)

Both are why `check-sidecars.sh` cannot be driven to silence here.

1. **`q-usage-audit.ts` discovers 0 blocks under the split-repo layout.** It sets
   `REPO_ROOT = resolve(SCRIPT_DIR, "..", "..")`, which resolves to the PLATFORM
   root once the pipeline lives in `folio-assistant/`, so `PAPER_ROOT` points at
   a directory that does not exist. It then exits 0 having swept nothing —
   a silent no-op. Consequence: the seven `q-usage-*` criteria are frozen at
   their pre-split hashes in every sidecar and go stale on any `.md`/`.ts` edit,
   with no working command to refresh them. `qa-sweep.ts` does not run them
   (96 criteria, none of them q-usage).

2. **`voice-scholarly-default` reads Lean docstrings but declares
   `depends_on: ["md"]`.** So a Lean-ONLY edit neither introduces nor clears a
   finding until the `.md` hash moves. Hit live: a wrapped line beginning
   "right dimension," tripped `LECTURER_OPENER_RE` (`Right,?\b`) inside the new
   Lean docstring — a false positive — and reflowing the docstring did not clear
   the cached `fail` until the entry was dropped by hand and re-swept.
   Suggest `depends_on: ["md", "lean"]` with the existing prose-only relaxation.

## Also fixed here

- `meson-octet-decomposition.qa.json` was STALE in the committed tree: its
  sidecar recorded the pre-lean-wiring `.ts` hash and carried no `lean` /
  `lean_statement` hashes at all, so the previous pass's "sidecar hash in sync"
  did not hold for it. Re-swept; that surfaced two genuine warns
  (`uses-editorial-hygiene` redundant edge, `wall-base-ring-minimal`) that had
  been masked. `uses[]` left alone — editorial relation, owner's call.
- authors-note Lean coverage was stale at HEAD independently of this work:
  a refresh on a clean HEAD gives 690/704 (98.0%) against the committed
  654/698 (93.7%). This branch's own contribution is +1 (→ 691/704, 98.2%).

## Platform defects: FIXED upstream (not yet merged)

Do not re-do these — folio-assistant branch `claude/agent-4673-validation-9hffrd`,
three commits, no PR opened yet.

- `ca574e0` — `depends_on` conflated *applicability* with *freshness*. Added
  `also_invalidated_by` (freshness only) + `freshnessKeys()`; wired the four
  `entryIsFresh` call sites; `voice-scholarly-default` now invalidates on
  `lean` without gating on it. The naive fix (adding `lean` to `depends_on`)
  would have `n/a`-ed every prose-only block — tested against.
- `1b82747` — `q-usage-audit.ts` now resolves the CONTENT repo via the
  existing `repo-root.ts` helpers instead of its own file location, drops the
  hardcoded paper name (`--paper`, else `findPapers()`), and EXITS 2 on a
  zero-block sweep instead of 0. Verified on qou: 0 blocks → 3017 across 40
  chapters, surfacing 8 fails / 729 warns invisible since the split.
- `753bdba` — third defect, found via the dirty-tree symptom: `qa-sweep`
  stamped the CONTENT repo's HEAD into the PLATFORM's script sidecars
  (`gitHeadSha()` has no `-C`), and rewrote all 76 unconditionally because
  `last_run_at` is a fresh timestamp. Both fixed; carries the overdue
  one-time refresh of 66 sidecars last stamped 2026-06-15.

Once merged, the residual `q-usage-*` staleness on this paper's sidecars
becomes refreshable and `check-sidecars` can be driven to silence again.
`one-voice-audit` will still be listed — that one is an agent-run skill, not
a script criterion, so no sweep refreshes it.

Suite there: 228 pass / 29 fail against a 201/29 baseline (+27 new tests,
identical failure set). Those 29 are the SAME split-repo defect class —
platform tests looking for content-repo files (`proof-objects.json`,
`lean-toolchain`, `lakefile.toml`) at the platform root. Unclaimed.
