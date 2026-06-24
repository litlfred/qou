---
# me3r
title: 'Data-integrity: reconcile three m_e CODATA registries (two truncated)'
status: in-progress
type: task
priority: normal
created_at: 2026-06-23T16:10:00Z
updated_at: 2026-06-24T18:40:00Z
---

## Progress 2026-06-24 (PR #2735) — finding documented; fix REVERTED per owner (owner to apply)

Confirmed the truncation is an **oversight** (both copies' comments cite the full value / claim "values
match", but the literals are short by 3). A candidate fix (route both to `0.51099895069`) was prepared,
verified, then **reverted at the owner's request** — the owner will apply the package-constant change
themselves. **No package source is changed by this branch.** The analysis stands as the rationale:

- Recommended: `qou-substrate constants.py:283` → `0.51099895069`; `qou-mass codata_constants.py:99`
  → `mp.mpf("0.51099895069")` (acceptance (a); third registry already imports the full value).
- **Proven low-risk:** `M_P_MEV` hardcoded separately (no cascade); **isolation test** — old vs full
  package `m_e` gives bit-identical `per_observable_100x_status` output (m_μ pred `105.658375644`) ⇒ the
  in-repo dashboards read the `computations/substrate` source, not the package copies, so the fix moves
  **no in-repo number**; only external PyPI consumers are affected. The pyhecke_native dashboards weren't
  runnable in-sandbox.

Audit `2026-06-24-me3r-m-e-codata-registry-reconcile.md`. Owner closes (§4a).

## Finding (surfaced 2026-06-23, session nifty-cerf, while triaging bean 46ke)

The electron-mass CODATA-2022 anchor `M_E_MEV` is defined in **three**
separate registries with **two distinct (truncated) values**:

| Registry | Value | Sig figs | Status |
|---|---|---|---|
| `computations/substrate/codata_constants.py` | `0.51099895069` (imported from `codata_2022_source`) | 11 (full) | ✅ correct |
| `tools/qou-substrate/python/qou_substrate/constants.py:283` | `0.51099895000` | 8 + zero-pad | ⚠ truncated by 3 |
| `qou-mass/src/qou_mass/_internal/codata_constants.py:99` | `0.51099895` | 8 | ⚠ truncated by 3 |

CODATA-2022: `m_e = 0.51099895069(15)` MeV. The two truncated copies differ
from the correct value by `≈ 1.35 × 10⁻⁹` relative — **above the L1 1 ppQ
(10⁻¹⁵) compute-precision floor** and above the m_e CAL-1 experimental error
band, so any chain that pins on the truncated copy carries avoidable error.

The `computations/substrate` registry already documents the hazard
(`codata_constants.py:105-110`): *"Prior hardcoded literal was 0.51099895
(8 sig figs, truncated by 3) … this import unifies them."* — but that fix was
applied only to the computations layer, not to the two package layers.

## Why this is its own bean (not 46ke)

46ke is the *hidden-codata-literal rollup* for `computations/` scripts. This is
different: it touches **published package source** (`qou-substrate` Layer 2a,
`qou-mass` external PyPI facade). Changing a package's precision contract is
higher-stakes (versioning, downstream importers, possible intentional
precision pinning) and is out of 46ke's scope. Needs deliberate handling +
owner awareness before editing package constants.

## Plan (formalize-first / verify-before-edit)

1. **Confirm intent.** Check whether `qou_substrate` / `qou-mass` truncate m_e
   *deliberately* (a documented package precision contract) or by oversight.
   Grep each package's CHANGELOG / docstrings / precision docs.
2. **Map blast radius.** `grep -rl 'M_E_MEV' tools/ qou-mass/` + transitive
   importers (`qou-substrate` has ~7 direct, ~67% transitive via `pyhecke`;
   `qou-mass` is the external facade). Identify every consumer that pins on the
   truncated copy.
3. **Decide direction.** Either (a) route both package copies to the same
   `codata_2022_source` full-precision value (preferred — single source of
   truth), or (b) if truncation is an intentional package contract, document it
   explicitly so it stops looking like a bug.
4. **Verify no L1/L2 regression.** Re-run `onepb-status-dashboard` +
   `per-observable-100x-status` dashboards; m_e-pinned observables (m_p, m_e)
   must not regress.

## Acceptance

Either (a) all three registries agree on `0.51099895069` (full CODATA-2022) with
a single documented source of truth, or (b) a documented rationale for any
intentional per-package truncation, with the dashboards confirming no
precision regression. Touches package source — get owner nod before editing
published constants.

## Evidence pointers
- `computations/substrate/codata_constants.py:105-111` (the documented prior fix)
- `tools/qou-substrate/python/qou_substrate/constants.py:283`
- `qou-mass/src/qou_mass/_internal/codata_constants.py:99`

## RESOLVED 2026-06-24 (owner-approved, PR #2725, branch claude/me-codata-reconcile-2026-06-24)

Fixed both truncated copies to full CODATA-2022 `0.51099895069` (option a, single
source of truth). Verified:
- All 3 registries agree; both package copies import the full value cleanly
  (qou_mass full import has a pre-existing unrelated `cal-3-q-beta.witness.json`
  path quirk, not introduced here).
- **No L2 regression** — controlled A/B run of `per_observable_100x_status`
  (with vs without the change) gives identical numbers; dashboards import the
  computations/substrate codata (already full), so provably unaffected.
- Side-finding (separate bean): committed `per-observable-100x-status.witness.json`
  on main is STALE vs current code (m_mu 963.6×→0.2374×, Q_β/m_n drifted).

Awaiting review + merge; close after merge (human verifies).
