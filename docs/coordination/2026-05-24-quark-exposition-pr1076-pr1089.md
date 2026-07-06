# Coordination ledger — 2026-05-24

## Goal
Two parallel PRs working in adjacent layers of the Borromean / mass-derivation domain.

## Scope map

| PR | Branch | Layer | Files | Status |
|---|---|---|---|---|
| [#1076](https://github.com/litlfred/qou/pull/1076) | `claude/vigilant-allen-UNXwm` | Content (.md/.ts), Lean (.lean), Skill | quark exposition cleanup + one-voice criterion 11 + Lean `PlanarDiagram` → `BraidWord` migration | open, 10 commits, witness-pipeline CI fighting |
| [#1089](https://github.com/litlfred/qou/pull/1089) | `claude/great-galileo-ahGfj` | Production Python (computations) | `λ_scale` → `linking_weight` / `vol_density_borromean` rename + low-isotope sign-flip diagnostic | open, 2 commits, mergeable_state dirty |

## Overlap classification

| Axis | Overlap | Notes |
|---|---|---|
| Files | 0 | PR #1076 touches `.md` / `.ts` / `.lean` only; PR #1089 touches 6 `.py` files in `computations/`. Zero shared files. |
| Dependency | 0 | Neither blocks the other. |
| Cherry-pick | 0 | No commits worth cherry-picking either direction. |
| Theme | adjacent | Both clean up the Borromean / mass-derivation domain — #1076 narrative + Lean encoding, #1089 production Python rename. Consistent framing. |
| Lean coverage | shared concern | #1089's Lean-coverage table flags `VolDensity(K)` + `Vol(𝓑₃)` as not formalised. #1076 formalises the *braid-word* side (first-class `hopfLink` / `borromeanRings`) but does NOT close the VolDensity gap. |

## Coordination comments posted
- On #1089: https://github.com/litlfred/qou/pull/1089#issuecomment-4527780582
- On #1076: https://github.com/litlfred/qou/pull/1076#issuecomment-4527780839

## Heads-up shared with #1089
The `e0_calibration_audit --strict` pre-existing failure (3 docstring sites in `derived_masses.py:63,473` and `homflypt_su_n_mass_tower.py:107` using `0.782` instead of canonical `0.78233341`) — fixed in #1076 commit `db1658a5`. #1089 may hit the same gate on rebase.

## Escalations (§6)
None.

## Next concrete task
1. Resolve PR #1076 CI failure (`validate` failing without log-accessible diagnostic).
2. Once CI green, perform rebase-merge of #1076 per AGENTS.md §Branch+PR rule 7.
3. Continue any post-merge follow-up (hedging sweep batch 2 if requested).
