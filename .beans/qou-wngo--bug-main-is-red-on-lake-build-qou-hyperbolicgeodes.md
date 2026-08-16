---
# qou-wngo
title: 'BUG: main is RED on lake build QOU — HyperbolicGeodesicZAxis.lean, 4 errors, 2 of them one-word fixes'
status: todo
type: bug
created_at: 2026-08-16T14:02:16Z
updated_at: 2026-08-16T14:02:16Z
---

Found running `prepare-merge` Step 4 on PR #5205. The **only** build errors in
the whole `QOU` library are in one file, and it is not mine — zero overlap with
#5205's diff.

## Where it came from

`content/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicGeodesicZAxis.lean`,
landed on main by:

* `5cd0e901f0` — WALL-3 upper bound (bean `qou-6eco`)
* `611fa218b3` — WALL-2 partial (bean `qou-0a0z`)

## The four errors, and what they actually are

```
:89:56  Unknown identifier `b`
:92:53  Unknown identifier `a`
:131:0  (deterministic) timeout at `whnf`, max heartbeats (200000) reached
:153:8  (kernel) unknown constant 'QOU.Archimedean.admissiblePath_vseg'
```

**They are three problems, not four.**

**1-2. Two unbound implicits — trivial.** `autoImplicit` is off, so these do not
auto-bind:

```lean
@[simp] theorem vseg_zero {a : ℝ} (ha : 0 < a) : vseg a b 0 = zpt a := …
--                        ^^^^^^^ binds a, but the statement uses `b`
@[simp] theorem vseg_one  {b : ℝ} (hb : 0 < b) : vseg a b 1 = zpt b := …
--                        ^^^^^^^ binds b, but the statement uses `a`
```

Fix is `{a b : ℝ}` in both. That is the whole change.

**3. A `whnf` heartbeat timeout at :131** — the real work. This is the one that
needs someone who knows the file.

**4. Is NOT an independent error.** `admissiblePath_vseg` **is** defined, at
:132 — immediately after the timeout. The timeout stops that declaration being
added to the environment, so :153's reference to it reports as an unknown
constant. Fix the timeout and this disappears. Do not go looking for a missing
lemma.

## Why it reached main

CI is `workflow_dispatch`-only repo-wide (2026-06-30 Actions-billing directive),
so nothing built this on push. Under AGENTS.md §"QA is agent-owned", the author's
own `lean`-direct run was the gate — and a per-file `lean`-direct check of a
*different* file would not have caught it. Whole-library breakage is exactly the
class that has no automated catcher right now.

## Scope

**Not fixed here.** Wrong domain for #5205 (hyperbolic geometry vs Hecke/Young),
and folding it in would muddy a clean review. Flagged rather than silently
absorbed. The two implicit-binder fixes are unambiguous and safe for whoever
picks this up; the timeout is not.

**Note for anyone running `lake build QOU`:** it will be red until this lands,
and the redness is entirely this one file. Per AGENTS.md the whole-library build
is not the merge gate — `lean`-direct on changed files is — so this does not
block unrelated branches, but it does mean a red build says nothing about your
own work until you check which file failed.
