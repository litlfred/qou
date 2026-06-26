# L2 100× dashboard — current status (2026-06-26) + the `tnjb` m_μ convention caveat

**Date:** 2026-06-26
**Scope:** reporting only — **no canonical witness regenerated.** This documents the
live `per_observable_100x_status.py` output on current main and flags the known
`tnjb` convention trap so the next agent does not silently overwrite the canonical
witness.
**Beans:** `tnjb` (per-observable-100x witness convention), `z5vu` (owner-gated
muon→proton witness migration), `kehn` (m_n Kashiwara b²).

## Live dashboard output (current main)

| Observable | role | pred err (ppb) | 100× target (ppb) | miss | 100×? |
|---|---|---|---|---|---|
| m_p | CAL-2 numerical anchor | 0.0004 | 0.0031 | 0.13× | ✅ |
| m_e | CAL-1 anchor | 0 | — | anchor | ✅ |
| m_K/m_π | meson-ratio validation | 28.0 | 263.6 | 0.11× | ✅ |
| Q_β | derived (CAL-1+CAL-2) | 1248 | 7.80 | **160.1×** | ❌ |
| m_n | validation | 1.040 | 0.0057 | **181.0×** | ❌ |
| Δ_pn | validation (derived) | 755.6 | 4.74 | **159.4×** | ❌ |
| m_μ | validation | *(see caveat)* | 0.2177 | **963.6×** | ❌ |

**Canonical count: 3/7** beat the 100× target (m_p, m_e, m_K/m_π).

## The `tnjb` caveat — m_μ is FAIL, not MET

A fresh `per_observable_100x_status.py` run **reports m_μ at ~0.05 ppb (MET),
inflating the count to 4/7.** This is the recurring `tnjb` bug, not a real result:
the fresh run reads a **muon-q₀** `m_mu_pred` (≈ CODATA, ~0 ppb — the CAL-2
calibration *tautology*) and scores it as the m_μ prediction, silently flipping
m_μ from its canonical **963.6× FAIL** to MET. Per AGENTS.md §"q₀ anchor
convention": the canonical m_μ is the **proton-anchored prediction**
(m_μ ≈ 105.6583978, 209.8 ppb → 963.6× the 0.2177 ppb target), the μ–p substrate
tension — **never "exact / ~0 ppb / MET."**

**Therefore the committed `per-observable-100x-status.witness.json` (m_μ FAIL,
3/7) is the correct canonical state and was NOT overwritten by this refresh.**
Regenerating it would require the owner-gated muon→proton witness migration
(bean `z5vu`); do not do it as an idle refresh.

## What moved since the last dashboard

- **m_n: now 1.040 ppb** (was −1759 ppb) via the parameter-free Kashiwara b²
  Q_β wiring (bean `kehn`, PR #2723). It still misses its *tiny* 0.0057 ppb
  target by 181×, but the absolute prediction is now CODATA-grade — a real
  improvement, near-match tier.
- The failing trio (Q_β / m_n / Δ_pn) shares one root: the Q_β `c_k` / Habiro
  residue, gated on the s5-so3 keystone (bean `s5bb`).

## Net

3/7 canonical (unchanged headline), with m_n's absolute value much improved.
The 100× closure for the failing trio stays gated on the keystone; the m_μ
"4/7" any fresh run shows is the `tnjb` tautology, not progress.
