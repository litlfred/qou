---
# qou-bhfg
title: 'SM-4A: audit the seven N=3 exclusions — proved-invariant vs probe, flag convention-C/float64 provenance'
status: completed
type: task
priority: normal
created_at: 2026-08-25T06:12:42Z
updated_at: 2026-08-25T10:35:59Z
---

**Answered 2026-08-25** (PR #5744, branch `claude/standard-panel-qou-derivation-ixuolx`).

Audit: `docs/audits/2026-08-25-n3-exclusion-provenance-audit.md`.

The owner's skepticism — that an exclusion might rest on stale compute — was
measured and the answer is a negative: none of the seven N=3 exclusions turns on
a convention-C or float64 probe. But one of them (route 3, the Ocneanu
$N=2$/$N=3$ weight-ratio exclusion) rested on a **finite sample** — "the ratios
differ at every $q$ tested" — not on the symbolic formula. That is a real gap in
the *argument*, independent of the compute question, and it is now closed by
proof rather than by sampling:

- `QOU.Eightfold.OcneanuTwoThreeNotProportional.ratio_eq_iff_qb_three_eq_zero`
  — the two ratios coincide **iff** $[3]_q = 0$.
- `QOU.Archimedean.OcneanuTwoThreeSubstrate.ocneanu_ratio_N2_ne_N3` — hence they
  differ at every real $q > 1$, the substrate included.
- `ocneanu_ratio_adjacent_ne` — the same for every adjacent pair, not just 2/3.

Both files `lean`-direct exit 0, sorry-free, standard axioms.

Consolidation follow-up (sibling review, bean `qou-qint`): the local `qb` is
bridged to canonical `QOU.QInteger.qIntBal` by `qb_eq_canonical`, and positivity
is stated on the canonical object as `qIntBal_pos`.
