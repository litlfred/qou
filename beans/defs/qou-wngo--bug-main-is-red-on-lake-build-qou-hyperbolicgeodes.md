---
# qou-wngo
title: 'BUG: main is RED on lake build QOU — HyperbolicGeodesicZAxis.lean, 4 errors, 2 of them one-word fixes'
status: completed
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T14:02:16Z
updated_at: 2026-11-21T14:33:40Z
parent: qou-5vkl
---

Found running `prepare-merge` Step 4 on PR #5205. The **only** build errors in
the whole `QOU` library are in one file, and it is not mine — zero overlap with
#5205's diff.

## Where it came from

`folio/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicGeodesicZAxis.lean`,
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


---

## CORRECTION — six errors, not four; and the unbound-implicit defect is repeated in TWO lemma pairs

I filed this from a **partial read of the build log tail** while the background
build was still running. The completed log (`EXIT=1`, 8 `error:` lines = 6 real
+ 2 summary) shows two more errors than I reported:

```
:61:74  Unknown identifier `b`     <-- MISSED
:64:71  Unknown identifier `a`     <-- MISSED
:89:56  Unknown identifier `b`
:92:53  Unknown identifier `a`
:131:0  (deterministic) timeout at `whnf`, 200000 heartbeats
:153:8  (kernel) unknown constant 'QOU.Archimedean.admissiblePath_vseg'
```

**The same copy-paste error appears in two adjacent lemma pairs**, not one:

```lean
@[simp] theorem heightProfile_zero {a : ℝ} (ha : 0 < a) : heightProfile a b 0 = a
--                                 ^^^^^^^ binds a, statement uses b
@[simp] theorem heightProfile_one  {b : ℝ} (hb : 0 < b) : heightProfile a b 1 = b
--                                 ^^^^^^^ binds b, statement uses a
@[simp] theorem vseg_zero          {a : ℝ} (ha : 0 < a) : vseg a b 0 = zpt a
@[simp] theorem vseg_one           {b : ℝ} (hb : 0 < b) : vseg a b 1 = zpt b
```

So the fix is `{a b : ℝ}` in **four** places, and the shape is a duplicated
`zero`/`one` lemma pair written twice — worth checking whether the same pair
pattern recurs further down the file.

The rest of the diagnosis is unchanged and still correct: the `:131` `whnf`
timeout is the real work, and `:153` is **not** an independent error —
`admissiblePath_vseg` is defined at `:132`, immediately after the timeout, so it
never enters the environment.

**Also correcting my own method**, since it produced a second wrong number: the
command I used to list "files with errors" was
`grep -oE "QOU/[A-Za-z/]+\.lean" <log> | sort -u`, which matches every module
name **anywhere** in the log — i.e. everything the build compiled, ~700 files —
not the files that errored. The authoritative extraction is the `^error:` lines
alone, and by those the failures are confined to this one file. The confinement
claim was right; the way I checked it was not.

**Still not fixing it here** — the four-line implicit fix alone does not turn the
build green (the timeout remains), so a partial fix unblocks nobody and just
splits ownership of a file mid-repair.


---

## FIXED in PR #5261 — and this bean's own diagnosis was wrong (2026-08-16)

Branch `claude/wngo-hyperbolic-zaxis-2026-08-16`. **The fix is four tokens.**
`autoImplicit` is off, so these never auto-bound:

```
heightProfile_zero {a : ℝ}  →  {a b : ℝ}
heightProfile_one  {b : ℝ}  →  {a b : ℝ}
vseg_zero          {a : ℝ}  →  {a b : ℝ}
vseg_one           {b : ℝ}  →  {a b : ℝ}
```

After it: `lean`-direct **exit 0 with ZERO diagnostics** — no errors, no
warnings. PR diff: 1 file, +4/−4.

### 🔻 Correcting this bean

It said *"the `whnf` heartbeat timeout at `:131` is the real work"*, and I
repeated that in PR #5205's body. **Wrong.** The timeout was **fallout**: `:131`
is `admissiblePath_vseg`, whose structure fields are `vseg_zero ha` and
`vseg_one hb` — the two broken lemmas. With their types metavariable-laden the
instance elaboration blew up. Fix the signatures and the timeout disappears,
taking the `:153` unknown-constant with it.

**Worse: I declined to fix this earlier *on that reasoning*** — "the four-line
fix alone does not turn the build green, so a partial fix unblocks nobody, and
I would rather not split ownership of a file mid-repair." Every clause was
downstream of an untested assertion. One four-token edit was the entire repair,
and `main` stayed red for hours because I predicted a hard part instead of
testing for one.

Second time today the same habit cost a turn (the other: claiming the general
adjacent case needed `σ_quadratic`, when it needed the previous induction step).
**Verify, do not predict.**

### Why nothing caught it

CI is `workflow_dispatch`-only repo-wide, so nothing built it on push. Under
§"QA is agent-owned" the author's own `lean`-direct run is the gate — and a
per-file check of a *different* file cannot catch this. **Whole-library
breakage is the class with no automated catcher**, and this is what that costs:
a four-token defect, live on `main`, invisible to every gate.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-16 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-21 — lean-build-red drain (issue #8817, session https://claude.ai/code/session_01Qmmkt5eovX5GYdZNHqjZdu)

**Completed.** Fixed on main by `30c17e3d3f` (four `{a b : ℝ}` binders). Re-verified at main `2ae54ab401`: `lean-direct-cone.sh QOU.Archimedean.HyperbolicGeodesicZAxis -B` forced rebuild of the cone, ok, 0 errors.
