---
# qou-tp56
title: Repo-wide autoImplicit=false in qou Lake leanOptions (Mathlib-standard hygiene; prevents the zeta-notation auto-bound trap) — needs a FULL lake build to validate, CI or non-sandbox
status: todo
type: task
created_at: 2026-08-15T03:14:24Z
updated_at: 2026-08-15T03:14:24Z
---


---
**2026-08-16 — the FULL lake build this bean asks for has now been run. One casualty.**

Run from `claude/fivetwo-level7-ladder-numerators` during a prepare-merge, per-paper
(`cd content/quantum-observable-universe/lean && lake build QOU`) because the root
workspace's Mathlib is a restored cache — 6990 oleans, **0 traces** — which
`.claude/commands/prepare-merge.md` §4 forbids building against. The paper workspace's
own Mathlib is genuinely lake-built (3338 oleans / 3344 traces), so the widened
`globs = ["QOU", "QOU.+"]` target is real coverage.

**Result: `LAKE_EXIT=1` at [5602/5603]. Exactly one module fails, and
`autoImplicit = false` is why.**

`QOU/Archimedean/HyperbolicGeodesicZAxis.lean`:

```
:61:74  Unknown identifier `b`     heightProfile_zero {a : ℝ} (ha : 0 < a)
:64:71  Unknown identifier `a`     heightProfile_one  {b : ℝ} (hb : 0 < b)
:89:56  Unknown identifier `b`     vseg_zero          {a : ℝ} (ha : 0 < a)
:92:53  Unknown identifier `a`     vseg_one           {b : ℝ} (hb : 0 < b)
:131:0  (deterministic) timeout at `isDefEq` (200000 heartbeats)
:153:8  (kernel) unknown constant 'QOU.Archimedean.admissiblePath_vseg'   [cascade]
```

Each of the four binds one of `a`/`b` and uses **both**. Under `autoImplicit = true`
the free one is auto-bound and the file elaborates; under this bean's setting it does
not. Reproduced standalone: `lean -DautoImplicit=false -s 65536 <file>` → exit 1, same
five errors.

**Why nobody saw it.** The module is an **orphan** — absent from `QOU.lean`, imported by
nothing — so it is reached only by the widened globs, never by an import-cone build or by
`lake build <name>` of anything else. Bean `qou-i0sr` records the upper bound as "LANDED
… sorry-free (PR #5236)", which is true of how it was verified and false of the library
build. This is the "files that had never compiled at all" class
`.github/workflows/lean-orphan-gate.yml`'s header predicts.

**Verdict for this bean: the setting is sound and the corpus is one file away from
clean.** 1966 of 1967 modules compile under it. The remaining work is four missing
binders plus whatever the line-131 heartbeat timeout needs — that is the z-axis arc's
(`qou-i0sr` / `qou-0a0z` / `qou-xidi`), not this bean's, and not touched here: the
prepare-merge branch that measured this does not own the file and left it alone.
