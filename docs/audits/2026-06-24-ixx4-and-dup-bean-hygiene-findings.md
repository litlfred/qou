# Beans `ixx4` + dup-id hygiene: both are non-actionable-by-agent (inflated grep / owner-only dedupe)

**Date:** 2026-06-24
**Type:** finding (no code change, no marker removal, no bean restructure). Records why the
placeholder-drain bean `ixx4` and the malformed `[?]` beans are **not** agent-drainable, per the
resweep discipline (`docs/audits/2026-06-24-placeholder-bean-count-resweep.md`).

## `ixx4` — "Resolve 6 placeholders/TODOs in MathlibExt.lean" → **0 actionable**

The resweep audit already classifies it: **`ixx4 | claimed 6 | grep 6 | actionable 0 | all -- TODO
upstream: notes on proved lemmas (intentional)`.** Direct grep of
[`MathlibExt.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt.lean) confirms — the
6 markers are `-- TODO upstream:` **comments** (lines 20, 32, 42, 54, 153, 181, 199) documenting which
Mathlib module each **already-proved** lemma should migrate to. **Zero `sorry`/`admit`.** Line 20 states
the convention outright: *"Each lemma has a `-- TODO upstream:` comment."*

These are intentional provenance notes, not unproved obligations. Removing them to "drain a count"
is exactly what the resweep + the `doth` bean log forbid (*"do not 'drain a count' by removing them …
Re-title/close is owner-only"*). **`ixx4` has nothing for an agent to do** — it is a raw-grep
inflation. Recommend the owner re-title (`ixx4` → "MathlibExt upstream-TODO notes (0 actionable,
intentional)") or close.

## Malformed `[?]` beans — duplicate ids, owner-only dedupe

Four bean ids each have **two files** with near-identical slugs (one with frontmatter, one a
no-frontmatter orphan log) — the `[?]` entries in the coord sweep:

| id | proper bean (frontmatter) | orphan log (no frontmatter) |
|---|---|---|
| `doth` | `doth--resolve-25-placeholderstodos-in-schema.md` | `doth--resolve-25-placeholders-todos-in-schema.md` (rich bib-DOI log) |
| `mlt7` | `mlt7--resolve-15-placeholderstodos-in-qoumass-endomorphi.md` | `mlt7--resolve-15-placeholders-todos-in-qou-mass-endomorphism.md` |
| `zslh` | `zslh--resolve-103-placeholderstodos-in-qoumass-theory.md` | `zslh--resolve-103-placeholders-todos-in-qou-mass-theory.md` |
| `s5bb` | `s5bb--s5so3-keystone-backbone-verify.md` (completed) | `s5bb--s5-so3-keystone.md` (active keystone log) |

The bean id is the filename prefix, so any frontmatter an agent adds to the orphan **keeps the
duplicate id** — it cannot be cleanly fixed without **renaming/merging/deleting** a bean file, which
is owner-only (per the same `re-title/close is owner-only` rule; bean files are the work-plan tracker).
The orphan logs hold the **real content** (e.g. `doth`'s bibliography-DOI-verification results; `s5bb`'s
keystone running log), so the correct dedupe is: **move the proper bean's frontmatter onto the rich
orphan log, then delete the thin stub** — an owner action.

**Recommended owner dedupe** (per id): keep the rich-log file, give it the canonical frontmatter,
delete the stub; for `s5bb` the two files are genuinely *different* beans (active keystone log vs
completed backbone-verify) that collided on the id — give the keystone log a distinct id.

## Net

Neither `ixx4` (0 actionable) nor the `[?]` dedupe (owner-only) is agent-drainable. This note records
the honest state so the counts aren't mistaken for open work and the markers aren't wrongly removed. No
code change; no marker removed; no bean restructured.
