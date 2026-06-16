# m_μ thread pivot — open the genuine next-largest gap

**Created:** 2026-05-30
**Status:** thread opened; multi-week research target
**Reason:** with α/(4π) thread structurally closed (Habiro Taylor +
categorical identification + Lean conditional), m_μ at 210 ppb /
0.22 ppb target (`misses ~964×`) is the largest open gap among
**absolute-mass predictions** on the L2 100× dashboard.

> **Scope note.**  Per `docs/precision-goals.md` line 190, `m_K/m_π`
> misses by ~1098× — strictly larger in miss-factor.  But `m_K/m_π`
> is a meson ratio prediction; the largest single gap on
> *absolute mass* predictions (m_μ, Q_β, m_n, Δ_pn) is m_μ at 964×.
> A separate thread for `m_K/m_π` closure is warranted but out of
> scope here.

## Current state

Per `docs/precision-goals.md` line 186:

| Observable | role | σ_exp | 100× target | Current pred error | Status |
|---|---|---:|---:|---:|---|
| m_μ | prediction | 21.8 ppb | **0.22 ppb** | 210 ppb | **misses ~964×** (9.5σ μ-p tension) |

The 210 ppb is the residual after the current production m_μ
derivation, **not** a free parameter. The production hypothesis is
**muon = 4_1 (figure-8 knot)** per `prop:skein-mass-relation`.

Audit-probe Markov-trace data (from
[`computations/lepton_tower_probe_1_cinquefoil_muon.py`](../../computations/lepton_tower_probe_1_cinquefoil_muon.py),
which is **audit-only, not production-wired** per its module
docstring):

- `|tr_M(4_1)| = z²·(1 - h + h³) ≈ 0.199476` at q_0
- `|tr_M(4_1)| / |tr_M(trefoil)| ≈ 0.273178`
- Required scaling ξ_(4_1) = 757 (compared to `1/ℏ_q² ≈ 102`)

The factor ξ_(4_1) ≈ 7.43 · (1/ℏ_q²) suggests an unaccounted prefactor
in the production chain.

## Known structural framing — μ-p tension audit

Per `docs/precision-goals.md` lines 117-120 + `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md`:

> *The μ-p 240 ppb is the floor of the current low-order shell; it is
> derivable-below (lower N residual), but not fittable-below.*

The 210 ppb m_μ residual sits **inside** the μ-p tension band (240 ppb).
This means:

- The current low-order substrate shell is already saturated for m_μ.
- Closing the m_μ gap requires **deriving the next-order shell** (a
  proved higher-order categorical term), **not** fitting.
- The next-order shell for m_μ is structurally the same as for m_p
  (both substrate-anchored leptonic/baryonic floors).

## Candidate next steps (multi-week)

1. **Audit the current m_μ chain** — trace through
   `lepton_tower_probe_1_cinquefoil_muon.py` + canonical mass-formula
   scripts to localize the 210 ppb residual to a specific structural
   contribution.
2. **Identify the next-order categorical correction** — the framework's
   `VolDensity` refinement work for m_p (~2.89% gap per
   `docs/canonical-derivation-cheat-sheet.md` §5 item #1) is the
   parallel work for the baryonic side. The leptonic side needs a
   similar `VolDensity` refinement for 4_1 (hyperbolic figure-8 knot).
3. **Habiro element for 4_1** — the framework has Habiro extraction
   infrastructure (`habiro_exact_taylor_extraction.py`,
   `gb-depth-period-bring-fig8.witness.json`). The 4_1 Habiro element
   at substrate q_0 should give Vol(4_1)/ℏ² + higher-order corrections.
4. **Cross-thread leverage from α/(4π) closure** — the Habiro Taylor
   framework established in PR #1511 (binomial closed form, exact
   rational coefficients) is the **same machinery** that should
   determine the next-order m_μ correction. The c_k structure for the
   4_1 Habiro element is the leptonic analog of the [2]_q binomial
   expansion.

## Anti-patterns to avoid

- ✗ Fit ξ_(4_1) = 757 to CODATA m_μ — this is the **4th-calibration
  violation** explicitly forbidden by the framework's 3-calibration
  discipline.
- ✗ Treat m_μ as ratio-anchored (m_μ/m_e) for the L2 dashboard — this
  hides the genuine prediction error.
- ✗ Introduce a 5th calibration (e.g., direct m_μ measurement
  separate from m_e) — same discipline violation.

## Cross-references

- `docs/audits/2026-05-28-mu-p-tension-substrate-floor.md` — current
  state of the floor
- `prop:skein-mass-relation` — production muon = 4_1 hypothesis
- `lepton_tower_probe_1_cinquefoil_muon.py` — current probe
- `docs/canonical-derivation-cheat-sheet.md` §5 item #1 — parallel
  `VolDensity` refinement for m_p

## Thread opening — what this doc accomplishes

Not a derivation, not a probe — a **structured opening** of the m_μ
research thread so future work has a single canonical entry point.
The α/(4π) thread was structured the same way at #1495's coord ledger;
this doc is the m_μ analog.

The next concrete branch (when picked up) is the audit of the current
chain to localize the 210 ppb residual.  Naming convention:
`claude/m-mu-chain-audit-2026-05-30+` or similar.
