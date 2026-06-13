# Phase 0 — baseline confirmation (2026-06-13)

Executes **Phase 0** of [`docs/workplans/2026-06-09-overall-strategy-update.md`](../workplans/2026-06-09-overall-strategy-update.md)
(strategy #2041): re-establish ground truth after the week of v4.24.0 repair +
the witness-wiring / Wenzl-scope sessions. **Verdict: state is stable, no
regressions.**

## Confirmed baselines

| Metric | Value (2026-06-13) | Prior | Note |
|---|---|---|---|
| **L1 — 1 ppQ compute** | met | met | `qou_substrate.precision` defaults (65 dps compute / 50 dps serialise) |
| **L2 — per-observable 100×** | **3 / 7** | 3 / 7 | m_p, m_e, m_K/m_π ✓; numbers **byte-identical** to committed (Q_β truncation-order reframing did **not** move them) |
| **conjectural-propagation** | 1968 blocks | 1919 | +49 blocks; on the strategy's "~1,900+" track |
| **lean_uniqueness on-disk** | 114 witnesses, 12 wired (10.5%) | 163 / 6 (stale heuristic) | producer-pool **exhausted** (#2203); the on-disk lag is CI witness-regen (billing-blocked), self-clearing |
| **raw `sorry` occurrences** | 1171 | "50" (pre-#1566) | **not** a regression — dominated by the 12,804 generated isotope-uniqueness stubs (#1566) + conjecture-class axioms; a real-gap count needs the classifying audit, not a raw grep |

### L2 detail (per-observable 100× status)

| Observable | role | pred err (ppb) | 100× target | miss | 100×? |
|---|---|---|---|---|---|
| m_p | CAL-2 anchor | 0.0004 | 0.0031 | 0.13× | ✓ |
| m_e | CAL-1 anchor | 0 | 0.0029 | — | ✓ |
| m_K/m_π | meson ratio | 23.44 | 263.6 | 0.09× | ✓ |
| **m_n** | validation | **1.066** | 0.0057 | **185×** | ✗ |
| **Δ_pn** | validation | 773.9 | 4.74 | **163×** | ✗ |
| **Q_β** | CAL-3 anchor | 1279 | 7.80 | **164×** | ✗ |
| m_μ | validation | 209.8 | 0.218 | 964× | ✗ |

**Highest-leverage next work:** the three failing non-anchor observables
**Q_β (164×), m_n (185×), Δ_pn (163×)** share a single root cause — the τ_M
Kashiwara derivation of Q_β truncated at k=2 (per
[`docs/audits/2026-05-30-l2-100x-status-3-failing-shared-root.md`](2026-05-30-l2-100x-status-3-failing-shared-root.md)).
**Phase 2 (Q_β k=3 closure) closes all three at once.** m_n is the closest
(1.066 ppb absolute). m_μ is an independent μ–p floor, not on this chain.

## Sandbox compute capability (correction for future agents)

CLAUDE.md implies the compute stack is unavailable in the web sandbox ("mpmath
IS [pip-installable]" by contrast). **That is too pessimistic.** Verified
2026-06-13 in this environment:

```bash
python3 -m pip install numpy scipy cvxpy clarabel   # ✓ all install from PyPI
python3 -m pip install -e tools/pyhecke              # ✓ editable repo package
```

With these, `deuteron_real_sdp.py` (numpy + cvxpy/clarabel SDP solve + the
`pyhecke` LP-dual entry point) **runs end-to-end in-sandbox**. Only the
**`pyhecke-native` Rust wheel** is genuinely unavailable (no prebuilt wheel; no
in-sandbox Rust toolchain). Scripts that import `pyhecke_native` remain blocked;
everything routed through pure-Python `pyhecke` + standard PyPI scientific
packages is runnable. This unblocks per-nucleus SDP / L2 / α_EM compute work
that was previously assumed gated.

## Deliverables

- Refreshed witnesses: `audit-lean-uniqueness-ref-wiring.witness.json`
  (114/12), `2026-05-01-p3-1-conjectural-propagation.witness.json` (1968
  blocks). The per-observable witness was re-run and confirmed **numerically
  unchanged** (not committed — timestamp-only drift).

## Recommended next (post-Phase-0)

1. **Phase 2 — Q_β k=3 closure** (highest leverage: closes Q_β + m_n + Δ_pn).
   Gated on the Option-E Kashiwara cell-content recurrence — research-grade,
   and subject to the c_k truncation-order canonical framing + no-fitting
   discipline (CLAUDE.md). Not a mechanical task.
2. **Phase 1 — per-nucleus real SDP** is now runnable in-sandbox, but the
   deuteron closure is the **Δ_λ gate**: encoding 5 (LR-branching, canonical)
   is feasible but does not reproduce the binding; encoding 2 (color-flavor) is
   infeasible. Per CLAUDE.md, do **not** add a fitted 7th ansatz.
