---
# qou-ix74
title: 'W-squared table-wiring: replace s² by the derived W(q) in the half-life predictions and measure the heavy-nucleus residual — and the two trace engines disagree on the word'
status: completed
type: task
priority: normal
created_at: 2026-09-05T05:45:22Z
updated_at: 2026-09-05T05:59:21Z
---

Owner "merge then the |W|² table-wiring compute tranche" (2026-09-05). Follow-on to qou-egvf (closed form) and qou-4x7c (content correction).

Measured on entry:
- computations/t35-weak-vertex.py is a LIVE producer (not the deprecated t35-full-calculation.py my audit doc named) and its committed witness (2026-08-29) carries W_q = 0.9684 under z_D = 0.61269 — a THIRD value for the same word, disagreeing with the canonical tr_M_word / Wedderburn / Jones-cross-checked 1.18748 under the same convention. One engine is wrong on (σ₁σ₂)⁵; hecke_division agrees with the canonical trace on the trefoil σ₁³ (0.8485), so the defect is word-specific. To localise per power k.
- That producer already encodes the wiring rule t_new = t_old · s⁴/|W|² and prints rate ratio |W|²/s⁴ ≈ 7.9e3 (with its 0.968): the naive substitution shortens every half-life by ~1e-4. With W = 1.1875 the factor is ≈ 1.2e4. Scope-(a): the like-for-like replacement of s² by |W|² prescribed in prf:hadron-half-life item 1 is not a small correction.
- Table 4 of ex:hadron-half-life-verification (the "<3 %" Skein-Coulomb table: 12.28 yr, 5896 yr, 5.308 yr, 28.92 yr, 30.26 yr, 5.022 d) has NO producer in computations/ or docs/ (grep on the six values: zero hits outside an unrelated audit line). The producer's own "old pred" list (12.40, 6690, 6.17, 31.9, 32.9, 5.79) and the Lean pred_* (13.0, 6800, 6.2, 32, 33, 5.8) are two further, different sets.


## Result (2026-09-05)

Three findings, on branch `claude/weak-vertex-table-wiring-2026-09-05`.

1. **The prescribed wiring is a scope-(a) NEGATIVE.** |W(q0)|²/s⁴ = 1.18754e4, so half-lives scale by 8.42e-5: every one of the six s²-based predictions lands at ~1e-4 of observed. Not the 10-17 % correction the corpus attributed to it. Lean sorry-free (substitutionRateFactor_eq / _gt_ten_thousand / _lt_twenty_thousand); producer weak_vertex_substitution_scale_probe.py, 6/6.
2. **hecke_division's Markov trace was wrong** on every word with a repeated lower generator: _trace_word applied the Markov rotation without the Hecke relation, collapsing to z^{len}. Per-power table k=1..5 (0.375/0.423/1.339/0.808/0.968 vs canonical 0.375/0.520/1.440/0.917/1.187); the reducer was correct throughout. Also a shared mutable memo keyed on the word alone, so a second z read the first instance's numbers. Fixed by delegating to markov_trace_canonical.tr_M_word; agreement < 5e-16 at every k. t35-weak-vertex.witness.json regenerated: 0.9684 -> 1.18748.
3. **The 0.7036 provenance in my own qou-egvf audit was wrong** (blamed the deprecated t35-full-calculation.py from file names). It is the same defective rule at z_C = 0.70355. Corrected at every in-repo site; PR bodies left as record.

Plus: Table 4 of ex:hadron-half-life-verification (the '< 3 %' Skein-Coulomb table) has NO producer anywhere — zero hits on its six values. Recorded, not edited.

STILL OPEN: what the correct coupling normalisation is (W/W(1)? W against the trefoil trace? a different object?) — a derivation question, deliberately not guessed.
