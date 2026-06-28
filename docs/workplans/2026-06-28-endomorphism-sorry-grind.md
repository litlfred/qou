# Canonical-derivation / mass-endomorphism — sorry grind

Goal: prove what is provable around the open gaps in the canonical
derivation chain and mass endomorphism, narrowing each gap honestly
(no audit-dodging per AGENTS.md §1a; every residual `sorry` carries a
`-- Ref:`; demote to `conjecture` / conditional-class per §3b-cond when
not closable).

## Frontier (from `docs/canonical-derivation-cheat-sheet.md §0`)

- **Step 9 is the frontier.** 9a per-knot `R(K)` and 9b `Δ_λ` binding
  are the SAME open object — `R(K)` runs A-dependent 2.3→63×, flip+re-pin
  refuted, owner-gated (2026-06-13). Not wireable until derived.
- Everything else is settled or proof-cleanup.

## Sorry targets (this branch)

| # | File | Live sorry? | Plan |
|---|------|-------------|------|
| 3 | `QOU/Hecke/MarkovTrace.lean` | yes (trace_pair / basis-of-reduced-words) | extract provable sub-lemmas; state real prop + `-- Ref:` |
| 4 | `QOU/WedderburnMass/confinement_categorical.lean:86` | yes (Hochschild vanish + Wedderburn, not in Mathlib) | conditional-class per §3b-cond; prove the parts not needing the missing Mathlib pieces |
| 5 | `QOU/Archimedean/SkewSYT.lean` | mostly commented-out | confirm live sorries; close jet-order parts provable by `decide`/`Finset` |
| 6 | `QOU/MassEndomorphism/ZHabiroCauchy.lean` + `PhiQConvergence.lean` | NO live sorry (conditional, sorry-free) | narrow: push `IsCauchyFiltration`-conditional toward unconditional; pin `Φ_q` identification |

## Discipline

- Verify every edit with `lean`-direct (env install backgrounded) before commit.
- Microcommit per file; PR is the living tracker.
