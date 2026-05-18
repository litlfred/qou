# Precision goals — what "1 ppb" means in QOU

> Canonical reference for all agents (Claude, Copilot, Gemini, future
> collaborators) working on QOU mass-prediction precision.
>
> Per user direction (2026-05-18): the framework's headline precision
> goal has **two independent legs**, not one.

## TL;DR

| Leg | Target | Status |
|-----|--------|--------|
| **L1. Compute precision** | internal cross-method agreement ≤ 1 ppb on every observable at substrate q_0 | **trivially met** — `_precision.py` default is 50 dps compute / 40 dps output (10⁻⁴⁰ relative); `onepb-status-dashboard` reports Layer 2 max_rel_delta = 0.0 across 8 atoms |
| **L2. Per-observable accuracy** | for each predicted observable O with experimental uncertainty σ_O: `σ_pred(O) ≤ σ_O / 100` (i.e. **100× more precise than experimental**) | **partial** — 1 of 6 observables (m_e, anchor) currently beats target; binding-constraint for absolutes is CAL-2 floor |

Both legs apply. Hitting L1 alone is not sufficient; hitting L2 alone is not
the framework's working precision discipline.

## L1 — compute precision (default 1 ppb)

**Definition.** Different methods computing the same quantity at substrate
q_0 must agree to at least 1 ppb (10⁻⁹ relative).

**Configuration.** Controlled by `folio-assistant/computations/_precision.py`:

```python
COMPUTE_DPS_DEFAULT  = 50    # mpmath working precision
OUTPUT_DPS_DEFAULT   = 40    # serialization precision
PRECISION_GUARD      = 10    # COMPUTE = OUTPUT + GUARD
```

The **1 ppb target is the *minimum*** — raise via `QOU_COMPUTE_DPS=<n>`
environment override. Some computations (operator-valued branching) target
1e-15 (15-digit) cross-method identity; that's still well above 1 ppb.

**Where measured.** `onepb-status-dashboard.witness.json`:

- Layer 1 (LP-dual / GB NF): 6/6 compounds, gap = 0
- Layer 2 (Markov-trace cross-method): 8 atoms, max_rel_delta = 0.0
- Layer 3 (Structural / AME publication rounding floor): 92.79 ppb max
  non-anchor Δ — this is the **measurement** floor, not a compute floor

**Audit rule.** Any new compute script MUST `from _precision import
set_compute_dps, fmt` and call `set_compute_dps()` before `mpmath`
operations. `compute-integration-watcher` I8 audit flags float64 leaks.

## L2 — per-observable accuracy (100× experimental)

**Definition.** For each predicted observable O, the *prediction error*
`|O_pred − O_exp| / |O_exp|` must be at most `σ_exp(O) / |O_exp| / 100`.

This is **variable per observable**. Most observables have very tight
σ_exp (CODATA 2022 absolute masses at sub-ppb), so most 100× targets
are in the ppt range. The single exception in the framework's L2 set
is the muon at σ_exp ≈ 22 ppb (100× target 0.22 ppb).

### Per-observable target table (CODATA 2022)

| Observable | σ_exp_rel | **100× target** | Current pred error | Status | Source witness |
|---|---:|---:|---:|---|---|
| Q_β (CAL-3 anchor) | 0.78 ppm | **7.8 ppb** | 1.68 ppm (relative) ≈ 1.31 keV abs | misses target by ~215 000× | `q-beta-predicted.witness.json` + `cal-3-q-beta.witness.json` |
| Δm_pn = m_n − m_p | 474 ppb | **4.74 ppb** | 254 ppb (Borromean) | misses target by 54× | `m-p-borromean-verification-50dps.witness.json` |
| m_μ (muon) | 21.8 ppb | **0.22 ppb** | 1.41 ppb (Borromean μ formula) | misses target by 6.5× | `m-p-borromean-verification-50dps.witness.json` |
| m_p | 0.31 ppb | **3.1 ppt** | 251 ppb (Borromean) | misses target by 81 000× | `m-p-borromean-verification-50dps.witness.json` |
| m_n | 0.57 ppb | **5.7 ppt** | 251 ppb (Borromean) | misses target by 44 000× | `m-p-borromean-verification-50dps.witness.json` |
| m_e (CAL-1 anchor) | 0.29 ppb | 2.9 ppt | 0 (anchor) | meets by definition | CAL-1 |

> **CAL-3 σ source.** Q_β experimental uncertainty here is the PDG 2024
> value Q_β(n) = 0.78233341(61) MeV (≈0.78 ppm, 779.7 ppb relative). The
> earlier 640 ppm draft was based on a coarser AME quote (0.78232 ± 0.00050
> MeV); that figure is **incorrect** at the precision we care about. See
> [`folio-assistant/computations/cal-3-q-beta.witness.json`](../folio-assistant/computations/cal-3-q-beta.witness.json).

For light-atom binding energies (B_D, B_T, B_³He, B_⁴He), the experimental
σ_B is dominated by the AME mass-table uncertainty (~10⁻⁶ for these atoms),
giving σ_rel(B) of order 0.04–0.45 ppm. **100× targets here are in the
0.35–4.5 ppb range — within reach post-Borromean-tower per-isotope extension.**

> **⚠ Δ_λ gate.** The per-isotope binding-energy formula is
> `B(K) = m_e · Σ_λ y_λ χ^λ Δ_λ(K)`. The Δ_λ values are *not yet
> derived* — six closure ansätze (Frobenius co-Casimir, Demazure-fibre,
> LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov) have all
> failed on the deuteron. See
> [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](audits/2026-05-18-delta-lambda-gating-context.md)
> for the full closure-attempt history. **L2 binding-energy targets are
> presently unreachable** — not because of compute precision, but
> because the structural Δ_λ derivation is open R&D (GAP-A-3 / GAP-A-4).

| Atom | B_AME (MeV) | σ_B / B | 100× target |
|---|---:|---:|---:|
| D  |   2.224 | 0.45 ppm | 4.5 ppb |
| T  |   8.482 | 0.12 ppm | 1.2 ppb |
| ³He |  7.718 | 0.13 ppm | 1.3 ppb |
| ⁴He | 28.296 | 0.035 ppm | 0.35 ppb |

### Two subgoals (L2 split)

**Subgoal-1 (achievable from current anchors).** 100× targets ≥ ~780 ppb
CAL-2 floor. Includes: Δm_pn (4.74 ppb), all light-atom binding
energies. Closure path: per-isotope Borromean-tower extension +
operator-valued branching combiner.

**Q_β was originally drafted as Subgoal-1** (6.4 ppm target) based on
the AME coarse quote. Per Copilot review on #777, the canonical CAL-3
σ is 0.78 ppm (PDG 2024), so Q_β's 100× target is 7.8 ppb — below the
CAL-2 floor. **Q_β is therefore Subgoal-2.**

**Subgoal-2 (research-grade).** 100× targets < CAL-2 floor. Includes
absolute m_p (3 ppt), m_n (6 ppt), m_⁴He (0.6 ppt). **Requires
substrate-derivation of q_0**, which the coordination ledger explicitly
declined on 2026-05-08:
> "Q_β derivation? **No** (explicit) — 780 ppb floor stands."
>
> By extension, q_0 (CAL-2) substrate-derivation is also declined.

Subgoal-2 is **out of scope** unless and until the ledger decision is
reverted by the repo owner.

## Where measured

Live snapshot: `folio-assistant/computations/per-observable-100x-status.witness.json`
(produced by `per_observable_100x_status.py`). Re-run on every Borromean /
calibration / formula change.

Reproduce:

```bash
python3 folio-assistant/computations/per_observable_100x_status.py
```

## Distinction: compute precision ≠ absolute-prediction error

The mass-table sweep (`mass-table-ppb.witness.json`) reports a 6.80% **mean
absolute** error across 10/16 light atoms. This is **not** a compute-precision
failure (L1 is met at 0.0); it is a **structural completeness** gap in the
per-isotope mass formula (only m_p, m_n, μ are wired to Borromean tower).

When reading dashboards:

- **L1 dashboards** (`onepb-status-dashboard`) → cross-method identity at
  fixed compounds. Currently 0.0 / 92.79 ppb (publication rounding floor).
- **L2 dashboards** (`per-observable-100x-status`) → predicted vs CODATA.
  Currently 1 / 6 (only m_e anchor); rest miss 100× target by 6× to 81 000×.
- **Mass-table sweep** (`mass-table-ppb`) → 10/16 with zero-param rule;
  mean |err| 6.80%. This is downstream of Borromean per-isotope extension.

## Practitioner cheat sheet

When working on a precision-affecting change:

1. **Run the L1 dashboard.** If anything regresses below 1 ppb cross-method
   identity, that's a real precision failure — stop and fix.
2. **Run the L2 dashboard.** If a per-observable target gets *worse*, that's
   a regression on accuracy.
3. **Don't conflate** L1 (compute) and L2 (accuracy). A formula that's
   compute-stable to 50 digits can still miss its 100× target by 10⁴.
4. **Don't claim "1 ppb met"** unless you're specific about *which* leg.
   Use phrases like "L1 compute met" or "L2 met for Q_β" not bare "1 ppb".

## See also

- [`docs/audits/2026-05-18-1ppb-workplan-v7-100x-experimental.md`](audits/2026-05-18-1ppb-workplan-v7-100x-experimental.md) — current workplan
- [`docs/coordination/1ppb.md`](coordination/1ppb.md) — cross-PR coordination ledger
- [`folio-assistant/computations/_precision.py`](../folio-assistant/computations/_precision.py) — compute precision infrastructure
- [`folio-assistant/computations/per_observable_100x_status.py`](../folio-assistant/computations/per_observable_100x_status.py) — L2 status reporter
