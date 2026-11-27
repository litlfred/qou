---
# qou-zf7n
title: lean-verify.sh runs bare lean without -DautoImplicit=false -s 65536 (false green)
status: completed
type: bug
priority: high
created_at: 2026-11-27T20:03:47Z
updated_at: 2026-11-27T21:34:34Z
---

scripts/lean-verify.sh calls `lean "$f"` with no flags. Bare lean defaults autoImplicit=true, so an unbound identifier is auto-bound and the file exits 0. Reproduced 2026-11-27: `theorem foo : x = x := rfl` gives bare exit 0, `lean -DautoImplicit=false -s 65536` exit 1 with two unknown-identifier errors. The flavour-W thread hit this: a draft with two Lean errors passed lean-verify.sh. AGENTS.md already mandates the two flags for lean-direct. Fix: pass -DautoImplicit=false -s 65536 in the verify loop. Until merged, verify with direct lean using those flags. lean-direct-cone.sh (used by the merge train) is separate; check its flags too.



2026-11-27 (thread "Fix lean-verify false green and quick wins"): lean-verify.sh itself was fixed by PR #9655. PR #9724 finishes the bean: eight sibling verifiers that still ran bare lean (verify-lean-direct, lean-verify-changed, lean-verify-cone, lean-verify-siblings, lean-sibling-witness-check, lean-overlay-env, leancheck-worktree, lean-compile-audit via lake env lean) now pass -DautoImplicit=false -s 65536. lean-direct-cone.sh was already safe (flag hardcoded in lean_cone_build.py). Second false-green class fixed too: lean-verify.sh printed '✓ checks' on sorry files; it now reports the sorry count and fails under LEAN_VERIFY_NO_SORRY=1. Re-measured: theorem foo : x = x := rfl gives bare exit 0, strict exit 1 (lean v4.24.0). Close when #9724 merges.


2026-11-27: PR #9724 merged.
