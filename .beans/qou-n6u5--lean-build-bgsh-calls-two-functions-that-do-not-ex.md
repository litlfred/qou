---
# qou-n6u5
title: lean-build-bg.sh calls two functions that do not exist, so the local-mathlib redirect never runs
status: todo
type: bug
created_at: 2026-08-23T15:25:05Z
updated_at: 2026-08-23T15:25:05Z
---

**Not a new sighting.** Bean `qou-aemy` already recorded the symptom as an
aside: *"That hook also errors on main: `lean-build-bg.sh: line 177:
mathlib_local_available: command not found`."* It was never given its own bean
and is still live. What is added here is the root cause and the measured cost.

## Root cause

`scripts/lean-build-bg.sh` lines 176-179:

    # ── Step 0: local mathlib redirect (if configured) ──────────
    if mathlib_local_available; then
        mathlib_enable_local_redirect
    fi

**Neither function is defined anywhere in the repository.**
`scripts/lib/lean-env.sh`, which the script sources at line 33, defines exactly
four: `has`, `lean_toolchain_slug`, `lean_leanpath`, `lean_mathlib_url_fix`.
A repo-wide grep for either definition returns nothing.

So the guard errors, the `if` takes the false branch, and Step 0 is dead code.
The local-mathlib redirect that `lean-mcp.config.json` advertises
(`lean.local_mathlib_path`, default `../mathlib4`) is **never applied by this
hook** — the one place it would matter most, since the hook runs unattended at
every session start.

## Measured cost, this session

With no redirect, `lake build` fetches and compiles **Mathlib from source**.
Observed 2 h 26 m after session start, still in Mathlib:

    /tmp/lean-v4.24.0/bin/lean .../mathlib/Mathlib/FieldTheory/PurelyInseparable/Basic.lean
    /tmp/lean-v4.24.0/bin/lean .../mathlib/Mathlib/CategoryTheory/Adjunction/Comma.lean

Four concurrent `lean` workers at 60-99 % CPU, 1.4-2.3 GB RSS each — **~7 GB
and effectively the whole 4-core box**, with `status.json` still reading
`"Build attempt 1..."` from 13:26.

That is also the missing term in this session's OOM. A concurrent H12 producer
was killed at 9.86 GB anon-rss under the session cgroup; ~7 GB of unattended
Mathlib rebuild alongside it is what put the cgroup over, and it destroyed a
46-minute measurement. AGENTS.md already warns that a stray `lake build`
rebuilds Mathlib from source and evicts a restored olean tree; this hook does
exactly that on every session, silently.

## Fix

Either define the two functions in `scripts/lib/lean-env.sh` (the redirect
logic AGENTS.md describes: `git config url."file://<local>".insteadOf
https://github.com/leanprover-community/mathlib4`), or delete the dead Step 0
and stop advertising a redirect the hook does not perform. The second is
honest and one commit; the first is what the config promises.

Whichever is chosen, the guard should fail loudly rather than fall through —
`command not found` on a sourced helper is a wiring bug, not a capability
probe, and treating it as "feature unavailable" is what hid this.

## Scope note

Deliberately NOT folded into PR #5545 (the #5517 follow-through). That is a
compute-precision PR touching no Lean; this is Lean build infrastructure. The
build was stopped locally in that session to unblock a measurement, which is a
process action and changes no committed state.
