# Coordination ledger — Lean architecture / cache (sandbox build)

**Opened:** 2026-06-08 by PR #1999 (`claude/gallant-bohr-w9f6a6`)
**Goal:** share the **working** lake-cache + single-file verification
recipe across the Lean-blocked sibling PRs, and record two gotchas not
in `lean-environment-setup.md` as of this date.

## Why this ledger

Multiple open PRs report being unable to machine-check Lean in the web
sandbox ("can't compile locally", "env blocked", "will confirm green
once cache restores"). This session **got it working** — verified a new
`Mathlib`-importing file (`QOU/AlgebraicSubstrate/MetallicHierarchy.lean`,
axiom-clean) — after hitting and solving two traps. Recording so siblings
stop re-deriving.

## The working recipe (sandbox, no network)

```bash
export PATH="$HOME/.elan/bin:$PATH"          # elan/lake/lean present; toolchain v4.24.0
# 1. RESTORE prebuilt oleans (≈2 min) — do NOT build Mathlib from source.
ROOT=$(git rev-parse --show-toplevel); TGZ=$(mktemp)
SLUG=$(cut -d: -f2 "$ROOT/lean-toolchain" | tr -d '\r' | tr . -)   # v4.24.0 -> v4-24-0
git fetch --depth=1 origin "lake-cache/qou-$SLUG" \
  && git ls-tree --name-only FETCH_HEAD | grep '^lake-oleans\.tgz\.part' | sort \
     | while read -r p; do git show "FETCH_HEAD:$p"; done > "$TGZ" \
  && tar xzf "$TGZ" -C "$ROOT" && rm -f "$TGZ"
# 2. VERIFY a file WITHOUT lake (see Gotcha 2). Package oleans suffice for a
#    self-contained (Mathlib-only) file; a file importing other QOU.* modules
#    also needs the workspace + paper oleans (appended on the 2nd line):
LP=$(find "$ROOT/.lake/packages" -maxdepth 5 -type d -path '*/.lake/build/lib/lean' | tr '\n' ':')
LP="$LP$ROOT/.lake/build/lib/lean:$ROOT/content/quantum-observable-universe/lean/.lake/build/lib/lean"
env LEAN_PATH="$LP" ELAN_NO_OVERRIDE_NOTICE=1 lean path/to/File.lean      # EXIT 0 = checks
# axiom audit: append `#print axioms <Decl>` to a temp copy and run the same way.
```

## ⚠ Gotcha 1 — the cache omits the root `Mathlib.olean`

`lake-cache/qou-v4-24-0` ships **2919 Mathlib *submodule* oleans but NOT
the root aggregator `Mathlib.olean`** (the QOU lib never imports the
root, so it was never built/cached). Symptom in a NEW file:

```
error: object file '.../mathlib/.lake/build/lib/lean/Mathlib.olean' of module Mathlib does not exist
```

even though `find … -name '*.olean' | wc -l` shows thousands present.
**Fix:** import specific modules, not the root — e.g.
`import Mathlib.Analysis.SpecialFunctions.Sqrt` + `import Mathlib.Tactic`.
(Also the AGENTS.md §8 "minimal imports" rule, so do this anyway.)

## ⚠ Gotcha 2 — `lake env lean` / `lake build` on the restored cache WIPES the oleans

Running **any lake command** after the restore triggers package
dependency **re-resolution**: lake decides several packages' remote URLs
"have changed" (the cache was seeded in a different env), then
`deleting … cloning again` — which **removes the restored Mathlib oleans**
(olean count drops to ~1). This happens **even with no global `insteadOf`
redirect set** (the skill's addendum point 3 only covered the insteadOf
case). One `lake env lean` invocation cost this session a re-fetch +
re-extract.

**Fix:** to verify a *single self-contained* file, **bypass lake
entirely** — run `lean` directly with a manual `LEAN_PATH` built from the
package olean dirs (step 2 above). lake never runs ⇒ nothing re-resolves.
(For multi-module / whole-lib builds you still need lake; then expect the
re-clone and budget for it, or pre-pin the package remotes.)

## Scope map (Lean-cache axis)

| PR | branch | relationship | note |
|----|--------|--------------|------|
| **#1999** (this) | `gallant-bohr-w9f6a6` | source of recipe | verified `MetallicHierarchy.lean` axiom-clean |
| **#2001** | `lean-repair-qou-red-2` | **overlap (infra)** | active v4.24.0 lib repair (11 modules); recipe lets them verify each fixed module locally via direct-`lean` instead of waiting on full `lake build QOU` |
| **#1974** | `eager-darwin-PqAjM` | **dependency** | "restoring from lake-cache in background, will confirm green" — Gotcha 2 explains any olean-wipe they hit; their modules are self-contained → direct-`lean` works |
| #1990 | `jet-order-rank-monotonicity` | reuse (solved) | already built via "cached current-rev Mathlib oleans" — confirms cache viability |
| #1995 | `vigilant-fermat-SROph` | blocked | "Lean class stub blocked, needs lake-cache restore" — recipe unblocks |
| #1562 / #1988 | — | blocked | "can't compile locally / network-blocked" — recipe unblocks |

## Decisions / asks

1. The recipe + both gotchas are being added to
   [`lean-environment-setup.md`](../../.claude/skills/local/lean-environment-setup.md)
   so they reach every future session (durable).
2. **#2001 is the right owner of the v4.24.0 lib-green effort** — #1999
   is NOT competing; it only verified one *new* leaf module. When #2001
   lands, the QOU lib goes green and `MetallicHierarchy` builds in-lib.
3. No cherry-picks needed (recipe is a doc/skill artifact, not code).
4. Escalation: none — findings are additive to the skill, not in
   conflict with any sibling's framing.
