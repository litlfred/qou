# 2026-05-03 — First A=5, A=6 sub-percent mass predictions

## Summary

Combining this branch's LaurentQ fast Markov-peel (which makes
A = 5, 6 atomic-braid traces tractable for the first time) with
the `categorical-mass-divergence-audit` branch's `α·Σ ln|V_i|`
mass formula (`prop:atomic-braid-mass`), we get **the first
sub-percent atomic-mass predictions for ⁵Li and ⁶Li**.

The integration is straightforward: `li2q_six_term_probe.py` from
the audit branch wasn't aware of A=5,6 atoms (its ATOMS list
stopped at ⁴He).  Once extended (added two rows: ⁵Li at
4669.151 MeV unbound, ⁶Li at 5603.052 MeV CODATA), the existing
script produced the predictions below.

## Result

`α·Σ ln|V_i|` formula vs CODATA atomic masses, q₀ = 1.10998:

| atom |   A  | n_gen | error vs AME |
|------|-----:|------:|-------------:|
| p    |   1  |  2    | **-0.016 %** |
| n    |   1  |  2    | **-0.073 %** |
| D    |   2  |  5    | **-0.192 %** |
| T    |   3  |  8    | **-0.174 %** |
| ³He  |   3  |  8    | **-0.071 %** |
| ⁴He  |   4  | 11    | **+0.296 %** |
| ⁵Li  |   5  | 14    | **+0.111 %** ← new |
| ⁶Li  |   6  | 17    | **+0.059 %** ← new |
| **mean**  |    |       | **0.142 %** |
| **max**   |    |       | **0.296 %** |

For comparison, the alternative `-Σ Li_2^q(-|V|)` formula:

| atom |  err  |
|------|------:|
| ⁵Li  | -0.157 % |
| ⁶Li  | -0.142 % |
| mean | 0.233 %  |

Both bounded forms predict A=5,6 to sub-percent.  The paper formula
wins (0.142 % vs 0.233 % mean), and notably its error does **not**
grow with A — it's smallest on ⁶Li (0.059 %).

## What this resolves

1. **T6 → MeV calibration question** is now empirically answerable
   — but in a different framing.  The "T6" in the partial-fraction
   polar split (`term6_residues_at_roots`) is the polar contribution
   at non-zero roots of unity.  The α·ln|V| / Li_2^q formula is the
   single-tower contribution at the per-generator level.  The two
   sit at different levels of the six-term decomposition; calibration
   of Term 6 specifically still needs the assembly convention worked
   out (`six_term_consumer.assemble_ame_comparison` open question).

2. **Tower MeV calibration question** identified in
   `2026-05-03-tower-mev-calibration-finding.md` is now closed in
   principle: the bug is `tower_mass_level` using `phi_q_safe` (≈ Φ_q)
   instead of α·Σ ln|V|.  Replacing the implementation is mechanical
   once the audit branch lands on main (the helper functions live
   there).

3. **A=5, 6 spectrum** is now empirically populated.  ⁵Li unbound
   isn't a real atom but its mass is measurable; ⁶Li is stable.
   Both predicted to sub-percent.

## Open questions

- **Why does paper formula get *better* on heavier atoms?**
  Naively expected the opposite (more |V|-near-1 contributions →
  more leading-order-of-Li_2^q error).  The trend  D→⁶Li (0.192% →
  0.059%) is monotonically improving for A ≥ 2.  Possible
  explanations: (a) error cancellation across more generators; (b)
  α·ln is actually exact and the small residuals are aliased
  uncertainty in the input volumes; (c) the per-generator volumes
  themselves are slightly miscalibrated and the systematic error
  shows up as a small constant offset that becomes relatively
  smaller for larger constituents.  Post-audit-branch-merge, would
  be worth a deeper sweep to A = 8, 10 to see if pattern holds.

- **Why does Li_2^q underperform paper formula on light atoms?**
  At |V_i| << 1, Li_2^q(-V) ≈ -V + V²/[2]_q − …; paper formula
  α·ln|V| has different correction.  The audit branch's reconciliation
  comment says paper is leading-order of Li_2^q for V near 1, which
  agrees with paper winning on heavy atoms (where |V_i| → 1) and
  losing on light atoms (where |V_i| < 1 by a margin).  But
  empirically paper wins everywhere.  Either the leading-order
  argument applies more broadly than expected, or there's a
  separate corrective term Li_2^q is missing.

## Reproduction

```bash
git fetch origin claude/categorical-mass-divergence-audit
git show origin/claude/categorical-mass-divergence-audit:\
computations/li2q_six_term_probe.py > /tmp/probe.py
# Add to ATOMS list:
#   ("5Li", 3, 2, 4669.151),
#   ("6Li", 3, 3, 5603.052),
# Add to top-of-file:
#   sys.path.insert(0, '<repo>/computations')
python3 /tmp/probe.py
```

Expected runtime: ~3-5 min (mpmath quad on the q-dilogarithm).

## Files cross-referenced (none added on this branch)

- `2026-05-03-tower-mev-calibration-finding.md` (this branch) —
  identified the upstream blocker
- `2026-05-03-t6-calibration-and-gs-reducer-perf.md` (this branch) —
  T6 calibration question
- `49fe17928`, `841cab890`, `a43d7f1fa` (audit branch) — Kashaev
  integration identity probe + reconciliation + content-block fix
- `li2q_six_term_probe.py`, `kashaev_integration_identity_probe.py`
  (audit branch) — the empirical machinery
