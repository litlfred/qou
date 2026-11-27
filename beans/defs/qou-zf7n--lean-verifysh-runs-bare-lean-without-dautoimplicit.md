---
# qou-zf7n
title: lean-verify.sh runs bare lean without -DautoImplicit=false -s 65536 (false green)
status: todo
type: bug
priority: high
created_at: 2026-11-27T20:03:47Z
updated_at: 2026-11-27T20:03:47Z
---

scripts/lean-verify.sh calls `lean "$f"` with no flags. Bare lean defaults autoImplicit=true, so an unbound identifier is auto-bound and the file exits 0. Reproduced 2026-11-27: `theorem foo : x = x := rfl` gives bare exit 0, `lean -DautoImplicit=false -s 65536` exit 1 with two unknown-identifier errors. The flavour-W thread hit this: a draft with two Lean errors passed lean-verify.sh. AGENTS.md already mandates the two flags for lean-direct. Fix: pass -DautoImplicit=false -s 65536 in the verify loop. Until merged, verify with direct lean using those flags. lean-direct-cone.sh (used by the merge train) is separate; check its flags too.
