---
# g2go
title: Credit existing sorry-free Lean for lem:jones-mobius-diagonal (checker false-negative)
status: todo
type: task
priority: normal
tags:
    - compute-wiring
    - tractable-lean
created_at: 2026-07-06T04:31:26Z
updated_at: 2026-07-06T04:31:26Z
---

Swarm triage: the block's lean.ref (qou:QOU.Braiding.JonesMobiusDiagonal.markov_eq_mobius_contact) resolves to an EXISTING sorry-free §3b-cond proof, but compute-prop-has-probe/-consumer false-flag NOT-WIRED (no sibling .lean + lean.validation:not_checked; resolveCanonicalLean/library-decl not credited by the compute checkers). Fix: make the compute-prop checkers credit the resolved library .lean (or set lean.validation), then re-sweep. DO NOT add a numeric probe (Mobius-kernel diagonal compute is not written down). No fabrication.

## Root-cause diagnosis (2026-07-06)

Not a per-block issue — a corpus-wide infra bug. folio's `schemas/lean-packages.ts`
is a dependency-injected registry (`configureLeanPackages`), but nothing calls it in
the **qa-sweep runtime** (only `scripts/tests/lean-ref-coverage.test.ts` does). So
`LEAN_PACKAGES` is empty at runtime, `leanPackageByName('qou')` → undefined, and
`resolveCanonicalLean(ref, contentRoot)` → undefined for **every** library-only block
(no sibling `.lean`) — wall-side / voice / q-usage / compute-prop all silently skip
them. Both target library Leans are confirmed sorry-free.

FIX (focused PR + corpus regression check):
1. Bootstrap `configureLeanPackages()` in the folio pipeline runtime (qou still ships
   the static qou/ugb/fred2005 list w/ lakeRoots in `schemas/lean-packages.ts`).
2. `qa-utils.ts resolveCanonicalLean` REPO_ROOT → `findContentRepoRoot()` (drafted on
   branch `claude/qa-utils-resolve-lean-content-root-2026-07-06`; do NOT ship alone —
   inert without part 1).
