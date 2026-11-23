---
id: qou-mlib
title: "Lean KG Stage 2: Mathlib4 Best-Practices Audit (`#lint`, Naming, Minimal Imports, §7c Generality) & Present Subgraph Refactor Options"
status: todo
type: task
priority: high
parent: qou-lnkg
blocked_by:
  - qou-kgdt
created_at: 2026-11-23T20:22:30Z
updated_at: 2026-11-23T20:22:30Z
---

## Deliverables
1. Audit all pure-math candidate modules (`Mathlib/`, `MathlibExt/`, `MathlibInfra/`, plus pure algebra/Hopf/toric/Rieffel/Hecke/Jackson modules) against `Mathlib4` style & linter rules (`snake_case`/`UpperCamelCase`, module `/-! ... -/` & decl `/-- ... -/` docstrings, minimal `import Mathlib.<Specific>`, `@[simp]`/`@[ext]` lemmas, `simpNF`/`docBlame`/`unusedArguments`, §7c typeclass generality).
2. Present concrete structured `AskUserQuestion` options (with full 6-part framing) for (a) separate `MathlibStaging/` root vs `QOU/MathlibExt/<MathlibPath>/` mirror, (b) collapsing the `78` `QOU/*` dirs into `~12-14` canonical chapter-aligned subgraphs, and (c) phased upstream PR slicing to `leanprover-community/mathlib4`.
