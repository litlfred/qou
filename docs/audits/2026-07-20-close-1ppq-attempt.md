# Close-1ppQ attempt — L1 is already certified; L2 is measurement-limited

**Date:** 2026-07-20
**Bean:** qou-ms5a (close-1ppq)
**Branch:** claude/qlift-borel-kernel-derivation-2026-07-20
**Scope:** understand what "1 ppQ" means, verify its current state, attempt
the most tractable *honest* advance (anti-fit STRICT).

## What "1 ppQ" means (two independent legs)

Per [`docs/precision-goals.md`](../precision-goals.md), the headline precision
goal is **two** legs, not one:

- **L1 — compute precision.** Different methods computing the *same* quantity
  at substrate q₀ must agree to ≤ **1 ppQ** (1 part per quadrillion,
  10⁻¹⁵ relative). This is the actual "1 ppQ" target. It is a *compute*
  claim (no float64 in the hot path), not an accuracy-vs-experiment claim.
- **L2 — per-observable accuracy.** For each observable O,
  `σ_pred(O) ≤ σ_exp(O)/100` (100× more precise than experiment). Variable
  per observable; unrelated to 1 ppQ except by name confusion.

L1 ≠ L2: a formula compute-stable to 50 digits (L1 met) can still miss its
100× accuracy target by 10⁴ (L2 missed). "1 ppQ" = **L1**.

## L1 state — MET / CERTIFIED (independently re-verified this session)

Re-ran the producer `computations/cross_check_trM_1ppb.py` under the canonical
muon pin (`QOU_Q0_ANCHOR=ideal`, required — else peel/χ-cache color-weighting
is mixed-pin). Result:

```
atoms compared: 6, certified 1 ppQ: 6, uncertified: 0, divergent: 0
worst exact-method |Δ|: proton 9.28e-50, neutron 3.33e-50   (gate 1e-15)
χ closed-form anchor: 6/6 match, worst |Δ| = 4.54e-50
witness cross-check-trM-1ppb.witness.json: allPassed=True
  (all_atoms_within_1ppQ=True, character_engine_matches_closed_form=True)
```

The exact methods (Hoefsmit mpf, χ-cache, Habiro) agree to ~10⁻⁵⁰ — **35
orders below** the 1e-15 gate. The `0.000182` deltas printed for
deuteron/³He/⁴He/tritium are **`cb≠`** (color-weighted peel/χ-cache vs
uncolored Hoefsmit/Habiro — *different quantities*, a known structural
branch, not a cross-method precision failure). L1 is genuinely certified for
the 6 production atoms (p, n, D, T, ³He, ⁴He), consistent with
[`2026-07-13-l1-4he-certification-complete.md`](2026-07-13-l1-4he-certification-complete.md).

### Finding: the aggregate dashboard's `allPassed:false` is a reporting artifact, not an L1 failure

`computations/onepb-status-dashboard.witness.json` shows `allPassed:false`.
Assertion breakdown:

| assertion | value | passed |
|---|---|---|
| `lp_max_duality_gap` | 0.0 (tol 1e-9) | ✓ |
| `markov_trace_max_rel_delta` | 0.0 (tol 1e-9) | ✓ |
| `all_witnesses_present` | 7 of 9 | ✗ |

The two *compute* assertions pass; the whole-dashboard `false` is driven
solely by `all_witnesses_present` — the inventory is missing
`brundan-kleshchev-audit.witness.json` and
`alpha-k-macdonald-closed-form.witness.json`. Both are **structural-audit**
witnesses (Brundan–Kleshchev, Macdonald α_k closed form), **not** L1
precision cross-checks, and **neither has a producer script on disk** (no
`brundan-kleshchev-audit.py` / `alpha-k-macdonald-closed-form.py`; the
`alpha_k_*.py` scripts present are unrelated computes). So the dashboard can
never regenerate them, and its `allPassed:false` is a **stale-inventory
artifact that misrepresents the certified L1 state** to a casual reader. This
matches the note in precision-goals.md (§TL;DR) that the aggregate dashboard
is superseded by `cross_check_trM_1ppb.py` for the L1 verdict.

**Not fixed here** (task scope = new files only; editing
`onepb_status_dashboard.py` to prune the dead inventory entries or restore the
two producers is a separate, existing-file change). Documented as the honest
discrepancy; the authoritative L1 verdict is the cross-check witness
(`allPassed=True`), not the aggregate dashboard's `false`.

## L2 state — 2/7, and the 5 misses are measurement-limited (not a compute lever)

Live `per-observable-100x-status.witness.json` (`beats_100x_count=2`):

| obs | err (ppb) | 100× target (ppb) | miss | meets |
|---|---:|---:|---:|---|
| m_e (anchor) | 0 | 0.00294 | — | ✓ |
| m_K/m_π | 23.4 | 263.6 | 0.09× | ✓ |
| m_p | 1.35 | 0.00309 | 437× | ✗ |
| m_n | 2.39 | 0.00575 | 416× | ✗ |
| m_μ | 209.8 | 0.218 | 964× | ✗ |
| Q_β | 1248 | 7.80 | 160× | ✗ |
| Δ_pn | 755.6 | 4.74 | 159× | ✗ |

Per [`2026-07-18-1ppq-action-plan.md`](2026-07-18-1ppq-action-plan.md) and two
sorry-free Lean theorems (`no_anchor_invariant_realizes_swing`,
`PinRobustnessOfRatios`): four geometric routes to the c₃ swing are **proved
closed**, and every ratio observable is structurally blind to the μ–p split.
Consequence — Q_β/m_n/Δ_pn (via c₃) and m_p/m_μ (via q₀) are **measurement-
limited**: gated on a next-gen neutron Q_β measurement (σ ≈ 0.024 eV) *or* a
substrate-derivation of q₀ (Subgoal-2, open for all since 2026-07-11), **not**
on framework compute. Shared root:
[`2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md).

## Honest verdict

- **L1 (the "1 ppQ" leg): MET / CERTIFIED.** Independently re-verified this
  session — 6/6 atoms ≤ 1 ppQ, worst exact-method |Δ| ≈ 9.3e-50, χ-engine
  matches closed form. "Close 1ppq" for L1 is **already done**; nothing to
  fit or derive.
- **Advanced this session:** re-certification with provenance (above); and the
  finding that the aggregate dashboard's `allPassed:false` is a dead-inventory
  reporting artifact (2 producerless structural witnesses), not an L1 failure.
- **Honest blocker for the rest:** the remaining precision gap is entirely
  **L2**, and the 5 L2 misses are **measurement-limited** (neutron Q_β / q₀
  substrate derivation), not compute-limited. No honest compute-only or
  fit-free change closes them — closing by fitting the c₃/Habiro tower to
  CODATA is exactly the anti-fit-forbidden move (see the m_p de-fitting,
  2026-07-04). The two live *compute* levers (c₃ D-ladder Écalle acceleration;
  α_EM per-loop theta-factor) resolve transseries structure but do not move the
  measurement-limited values.
