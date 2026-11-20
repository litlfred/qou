---
# qou-w12g
title: 'GAP: epic qou-uhx0 completion claims (qou-2och, qou-lm62) are not backed by artifacts on main'
status: todo
type: task
priority: high
created_at: 2026-11-20T09:00:00Z
updated_at: 2026-11-20T09:00:00Z
parent: qou-uhx0
---

Found by W12 (session_01VQDpPfS7H7LVPj21tEhkK3) while auditing epic `qou-uhx0`, `main` 917b69399.

1. `qou-2och` (status completed) names `QOU/BraidsAndKnots/GroebnerShirshovConfluenceLyapunovAndRadical.lean` (872 lines), an 80-dps probe, and an alpha_crit = q_0 result. None exist; `alpha_crit` occurs nowhere in `folio/`.
2. `qou-lm62` (status completed) claims a 71-entry glossary with 0 Lean refs and a Z = 1..118 table. The tree has 32 glossary blocks, 8 with `lean:` refs; no 118-row table found.
3. `qou-blf1` had the same pattern (resolution naming a nonexistent file); fixed by PR #8537.

Open, and what would close it:
- H_3(q) / n = 4 Bokut-Shiao GS confluence for the nuclear Hecke reduction: existing related Lean is `UGB/GrobnerShirshov/HeckeGS.lean`, `HeckeCompletion.lean`, `LocalConfluenceRefutation.lean`, `QOU/TransferMatrices/GSNormalForm.lean`, `QOU/Archimedean/NuclearGroebnerReduction.lean`. Nobody has checked what they already prove against the 2och statement; that comparison is the first step.
- alpha_crit = q_0: anything that derives q_0 is forever gated (owner 2026-08-02). A statement that only *evaluates* a threshold at the CAL-2 pin is not gated, but its exact content was never written down. Needs an owner-scoped statement before anyone works it.
- The GPMT radical separation part of 2och: no artifact found; unscoped.
- Whether 2och / lm62 should be set back from `completed`: owner decision (asked on #8526).
