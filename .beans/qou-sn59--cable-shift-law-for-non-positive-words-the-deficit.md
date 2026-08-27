---
# qou-sn59
title: 'Cable-shift law for non-positive words: the deficit lives in the multi-dimensional channels'
status: completed
type: task
priority: normal
created_at: 2026-08-26T21:19:44Z
updated_at: 2026-08-26T21:20:07Z
---

Answered by derivation rather than by the retracted candidate-form scan.

The law is x4 on any one-dimensional channel, for EVERY word: writhe(C(w)) = 4*writhe(w) (pure combinatorics, no positivity), and a 1-dim channel sees only the writhe (charOf_eq_zpow, merged #5826). So the deficit 4*alpha(K) - alpha(C(K)) cannot come from a 1-dim channel at all; it only arises when the maximizing partition is intermediate. The law is a statement about WHICH channel wins, not about the letters -- which is why no closed form in L, W, p, alpha exists. Positivity mattered only because it keeps the max on the column channel.

Lean: QOU/BraidKnot/CableShiftFourfold.lean, 11 decls, sorry-free, lean-direct exit 0.
Probe: computations/meson/cable_shift_where_the_deficit_lives_probe.py, 7/7.
Audit: docs/audits/2026-08-26-cable-shift-deficit-lives-in-multidim-channels.md
PR #5863.

Carry-forward method note: min-plus is a BOUND, and it is loosest exactly on the maximally cancelling words -- the ones a deficit analysis cares about. On the identity word it returned alpha(cable)=2 against a true 0, a spurious negative deficit and a false counterexample. Measure densely; use min-plus only as a flagged cross-check.
