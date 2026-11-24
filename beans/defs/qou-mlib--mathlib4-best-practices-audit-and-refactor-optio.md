---
# qou-mlib
title: 'Lean KG Stage 2: Mathlib4 Best-Practices Audit (`#lint`, Naming, Minimal Imports, §7c Generality) & Present Subgraph Refactor Options'
status: in-progress
type: task
priority: high
created_at: 2026-11-23T20:22:30Z
updated_at: 2026-11-24T00:25:56Z
parent: qou-lnkg
blocked_by:
    - qou-kgdt
---

## Deliverables
1. Audit all pure-math candidate modules (`Mathlib/`, `MathlibExt/`, `MathlibInfra/`, plus pure algebra/Hopf/toric/Rieffel/Hecke/Jackson modules) against `Mathlib4` style & linter rules (`snake_case`/`UpperCamelCase`, module `/-! ... -/` & decl `/-- ... -/` docstrings, minimal `import Mathlib.<Specific>`, `@[simp]`/`@[ext]` lemmas, `simpNF`/`docBlame`/`unusedArguments`, §7c typeclass generality).
2. Present concrete structured `AskUserQuestion` options (with full 6-part framing) for (a) separate `MathlibStaging/` root vs `QOU/MathlibExt/<MathlibPath>/` mirror, (b) collapsing the `78` `QOU/*` dirs into `~12-14` canonical chapter-aligned subgraphs, and (c) phased upstream PR slicing to `leanprover-community/mathlib4`.


## Updated Scope (`2026-11-23`): Reservoir Community `lean_lib` Packages + Selective `Mathlib4` Core
Present structured `AskUserQuestion` options comparing:
- Multi-library `lakefile.toml` layout (`lean_lib` community packages depending only on `Mathlib`, zero `QOU` imports, directly publishable to Lean Reservoir / `leanprover-community` ecosystem) + selective `MathlibExt` core-PR staging, vs.
- Single `QOU.MathlibContrib.*` namespace mirror, alongside collapsing the remaining QOU-specific `78` dirs into `~13` chapter-aligned `QOU.*` subgraphs.



## Worker 27 Stage 1b Readiness Delivery (2026-11-23 — Issue #9235, Ready PR #9236)
- Implemented `scripts/lean-best-practices-lint.py` (`BP001`–`BP009`: `autoImplicit false`, copyright/module header + Lean 4.24+ import order, minimal imports, `snake_case`/`UpperCamelCase` naming, §7c ring/universe generality, empirical/decimal literal ban, `: True`/projection vacuity ban, strict zero-`QOU.*` upward import boundary, synonym-dir blocklist) + `pytest` suite (`7/7` green in `0.21s`).
- Quantified Tier-A (`321` modules, `312` cone-pure) and 6 Tier-B Reservoir `lean_lib` packages (`HeckeTemperleyLieb` `635`, `TwistedFrobeniusHopf` `38`, `ToricConicOpt` `33`, `CompactQuantumMetrics` `10` [0 cut-edges!], `QCalculus` `58`, `BraidKnotOctonion` `585`; `1,489` cone-pure immediately extractable, `191` cut-blocked by `188` edges).
- Ready PR: https://github.com/litlfred/qou/pull/9236 (Stage 2 directory moves gated on owner `AskUserQuestion` per `qou-lref`).
