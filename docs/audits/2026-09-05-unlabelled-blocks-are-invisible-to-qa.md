# An unlabelled content block is invisible to `qa-sweep` — 63 of them, including the notation register

**Date:** 2026-09-05
**Bean:** `qou-voa6`
**Found by:** trying to refresh one sidecar after a one-line prose edit, and failing

---

## 0. The finding

`qa-sweep` enumerates blocks **by label**. A content block whose `.ts` declares no
`label:` is silently skipped — it is never swept, and **its `.qa.json` sidecar can
never be refreshed by any chapter sweep**. The sidecar still exists, still records
`source_hashes`, and still goes stale the moment the `.md` is edited. Nothing can
bring it back.

Measured across `content/quantum-observable-universe`:

| | count |
|---|---|
| blocks with a label | **3527** |
| blocks **without** a label | **63** |
| of those, carrying a `.qa.json` that cannot be refreshed | **63** (all of them) |
| of those, **already stale** | **23** |

## 1. The mechanism, measured rather than inferred

The notation chapter is the clean test, because its manifest registers 13 blocks
and exactly 2 of them lack a label:

```
registered blocks: 13   labelled: 11   sweep saw: 11
unlabelled (skipped): ['notation-register', 'notation-collisions']
```

`bun run folio-assistant/content/pipeline/qa-sweep.ts content/quantum-observable-universe/notation`
reports `blocks: 11`. The count matches the labelled set exactly, and the two
missing blocks are exactly the two unlabelled ones. The sweep's own output keys
every result by label (`sec:…`, `tbl:…`), which is the mechanism.

## 2. Why this particular pair matters

The two blocks the notation chapter cannot sweep are the two that
[`AGENTS.md`](../../AGENTS.md) names **authoritative**:

> The authoritative source for every mathematical symbol used in the paper is the
> front-matter **Notation** chapter […] **Per-chapter symbol tables**:
> `notation/notation-register.md` — **Collision avoidances + conventions**:
> `notation/notation-collisions.md`
>
> Agents **must** treat those `.md` files as authoritative when picking a
> font/symbol for a concept.

So the corpus's symbol register and its collision register are the two files in
that chapter with **no QA coverage at all** — no voice sweep, no
`render-math-mode-envelope`, no `wall-side-correct`, no trap detectors. Every
criterion listed in their sidecars is a criterion that has not been re-run since
the sidecar was first written.

`render-math-mode-envelope` is the sharp one: AGENTS.md introduces it as a
**critical** mechanical criterion precisely because the obvious hand-grep for it
matches the thing it should catch (`\begin{align` is a prefix of
`\begin{aligned}`), and says *"run `qa-sweep … --only render-math-mode-envelope`
rather than grepping by hand"*. On these two blocks that instruction cannot be
followed.

## 3. How it was found, and the honest cost

Not by looking for it. A one-line prose correction to `notation-collisions.md`
(the `≅`-vs-`↠` fix in this PR) made its sidecar stale — verified against `main`,
where the recorded `md` hash and the live hash agreed before the edit and disagree
after. Following the documented refresh procedure — drop the stale criterion
entries, re-run `qa-sweep --only <crit>` — the sweep reported `0 findings` and
**wrote nothing back**, leaving the sidecar worse than before (three criteria
deleted, none restored). The sidecar was restored to its committed state and the
edit ships with a stale sidecar, because there is no way to refresh it.

**So this PR knowingly leaves one sidecar stale**, and that is the defect, not an
oversight: `notation-collisions.qa.json` records `source_hashes.md =
231ec75c969b` against a file that now hashes differently. It joins the 23.

Two near-misses worth recording, both caught before they reached a claim:

- The first `qa-sweep` invocation, given the block path rather than the chapter
  directory, returned `criteria: 96, blocks: 0, findings: 0`. **`0 findings` over
  `0 blocks` is a false green**, and it reads exactly like a pass.
- The first diagnosis was *"the block is not registered in its chapter manifest"*
  — wrong. It **is** registered, in its own second section; the earlier grep
  output was truncated at the first section's block list. The cause is the
  missing label, not a missing registration.

## 4. What is NOT established

- **That adding labels is the right fix.** It is the obvious one, and it is a
  judgement about authoring convention rather than a measurement: a label makes a
  block cross-referenceable and emits `\label{}` into the LaTeX, so adding 63 of
  them is a rendering change, not a metadata change. Whether prose intros and
  outros *should* be labelled is the author's call. This note does not make it.
- **That the other 62 blocks are wrong.** Most are chapter intros and outros
  (`intro-*`, `outro-*`), for which being unlabelled may well be deliberate. The
  finding is that *the sidecar they carry is inert*, not that the blocks are
  malformed — arguably the sidecar should not be written for a block the sweep
  cannot reach.
- **That 23 stale is the true count.** It counts only blocks where both a
  `source_hashes.md` entry and an `.md` file exist to compare; the rest are
  reported `ok` for want of a comparison, not for passing one.
- **Anything about other papers.** Measured on
  `content/quantum-observable-universe` only.

## 5. Reproduce

```sh
bun run folio-assistant/content/pipeline/qa-sweep.ts \
  content/quantum-observable-universe/notation          # reports blocks: 11, not 13
```

The census in §0 is a short script over `content/**/*.ts`, keyed on the presence
of `label:` in the block manifest and the existence of a `.qa.json` sibling.
