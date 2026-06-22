# Precision goals — what "1 ppQ" means in QOU

> Canonical reference for all agents (Claude, Copilot, Gemini, future
> collaborators) working on QOU mass-prediction precision.
>
> Per user direction (2026-05-18, updated 2026-05-26): the framework's
> headline precision goal has **two independent legs**, not one.
>
> **Precision target upgrade (2026-05-26).** L1 compute precision
> target upgraded from **1 ppb** (10⁻⁹) to **1 ppQ** (1 part per
> quadrillion, 10⁻¹⁵). Rationale: at 50 dps / 40 dps output, the
> compute truncation is ~10⁻³⁴ ppb — the 1 ppb target was trivially
> met and no longer discriminating. The Q_β precision ladder (N=5)
> already produces formula residuals at ~10⁻¹⁰, approaching territory
> where the 1 ppb L1 floor is noise. "1 ppQ" = "1 part per
> quadrillion" (10⁻¹⁵ relative, 10⁻⁶ ppb). The "Q" is fitting —
> everything in this paper is q.

## TL;DR

| Leg | Target | Status |
|-----|--------|--------|
| **L1. Compute precision** | internal cross-method agreement ≤ 1 ppQ (10⁻¹⁵) on every observable at substrate q_0 | **NOT certified (2026-06-17)** — exact methods *exist* (`_precision.py` default 65 dps compute / 50 dps serialization), but the live L1 cross-check (`cross_check_trM_1ppb.py`) reports **4/6 atoms divergent / FAILURES**: the `markov_peel` atomic witness is float64-limited (~2.5e-16, stale producer) and the extended-Habiro nuclei path diverges ~1e-7. Even the two float-clean methods (Hoefsmit, chi-cache) agree only at ~2.5e-16 (float64 ε) on the atomic traces. See [`audits/2026-06-17-l1-1ppq-certification-gap.md`](audits/2026-06-17-l1-1ppq-certification-gap.md). The 3-strand closed-form χ anchor *does* hold at 4e-50. |
| **L2. Per-observable accuracy** | for each predicted observable O with experimental uncertainty σ_O: `σ_pred(O) ≤ σ_O / 100` (i.e. **100× more precise than experimental**) | **anchors only** — 2/7 meet, both calibration anchors (m_e, m_p); **0 of 5 genuine predictions** meet (m_μ, Q_β, m_n, Δ_pn, m_K/m_π all miss). The de-fitted, post-re-pin honest state. |

Both legs apply. Hitting L1 alone is not sufficient; hitting L2 alone is not
the framework's working precision discipline.

## The 1 ppQ target is on the *theory residual* (2026-05-29 reframe)

> Per owner direction (2026-05-29): the headline "1 ppQ on predictions
> from CAL-1/2/3" is a target on the **framework's own theory residual**,
> not on the absolute prediction error. This resolves an earlier
> mis-framing ("1 ppQ on a prediction is unreachable because q₀ is only
> known to 0.06 ppb"). The two error sources are separate and must not
> be conflated.

**Error decomposition.** Every prediction `O` carries two independent
error terms:

```
σ_total(O)  =  σ_theory(O, N)   ⊕   σ_CAL(O)
              └ framework's own  └ propagated experimental error of the
                formula residual   CAL-1/2/3 inputs (m_e, q₀←m_p, m_π)
                at derivation
                order N
```

| Term | Owner | Improves by | Current scale |
|------|-------|-------------|---------------|
| **σ_theory(O, N)** — the formula's own residual at brane-tower / derivation order `N` | **us** (derivation) | adding *proved* higher-order terms | m_p: 242 ppb (μ-p floor); m_avg: 2.89 % bare → 819 ppm spectral |
| **σ_CAL(O)** — propagated CAL experimental error | external labs | CODATA / PDG re-measurement | q₀: **0.06 ppb** (CODATA m_p); m_e: 0.29 ppb; m_π: ~30 ppb |

**The 1 ppQ goal = drive `σ_theory(O, N) ≤ 1 ppQ`**, so every prediction
is **CAL-limited, not theory-limited**. Once there, `σ_total ≈ σ_CAL`,
and the prediction sharpens automatically as the three calibration
measurements improve — no framework change required.

### Accepted: q₀ is known to 0.06 ppb (CODATA-limited, not a framework ceiling)

q₀ is pinned from the CODATA m_p/m_e ratio (0.06 ppb, the most precise
available — see [`substrate-anchor-alternatives.md`](../content/quantum-observable-universe/observations/substrate-anchor-alternatives.md)).
Its 0.06 ppb uncertainty is **inherited from that one measurement**, and
**improves one-for-one as CODATA improves m_p/m_e**. It is *not* a limit
of the framework. (If the QOU substrate picture is correct, the highest
leverage experimental program is tightening the three CALs — m_e, the
neutron β-decay sector behind q₀, and m_π — since every QOU prediction
then sharpens at once.) The framework's job is to make `σ_theory` small
enough that this external `σ_CAL` is the only thing left.

### Infra requirement: true arbitrary precision end-to-end (no float64)

To *certify* `σ_theory ≤ 1 ppQ` (10⁻¹⁵), the compute stack must resolve
residuals well below 1 ppQ, which **forbids any float64 in the hot path**
— float64 carries only ~16 significant digits (machine ε ≈ 2.2×10⁻¹⁶),
so a cross-method agreement that bottoms out at ~10⁻¹⁶ is *measuring
float noise*, not certifying precision. Rules:

1. **No `float(...)` / numpy `float64` / `complex128` in any value that
   feeds a witnessed quantity.** Use `mpmath.mpf` (or exact `sympy`
   rationals) throughout. Audit: `compute-integration-watcher` I8.
2. **dps headroom.** `_precision.COMPUTE_DPS_DEFAULT = 50` gives ~35
   digits of headroom below 1 ppQ — adequate. Raise via
   `QOU_COMPUTE_DPS=<n>` when bounding higher-order residuals.
3. **The L1 cross-method gate must be tightened 1 ppb → 1 ppQ** once all
   methods are float-clean. As of 2026-05-29, `cross_check_trM_1ppb.py`
   still gates at 1 ppb because the `markov_peel` *fast path* computes in
   float64 (`cf, df = float(c), float(d)`; `h_num = float(_h_num)`) and
   only agrees with the true-mpf methods (Hoefsmit, chi-cache, Habiro)
   to ~2.7×10⁻¹⁶. Fix = route peel through the exact `use_fast=False`
   sympy path (or an mpf path), then drop the gate to 1 ppQ.

### Bounding `σ_theory` vs derivation order N

We must be able to say *"order N\* achieves ≤ 1 ppQ"* before committing
compute. Two distinct "orders" exist — do not conflate them:

| Order | What it indexes | Residual behaviour |
|-------|-----------------|--------------------|
| **Habiro order M** (Markov-trace expansion `Σ a_m u^{2m}`) | the *trace* tr_M | **terminates** at M=8 (proton/neutron): finite integer-`a_m` sum ⇒ trace residual is **0**, compute-limited only |
| **Brane-tower / shell order N** (the observable formula around the trace) | the *formula shell* (e.g. `2·Vol/ℏ²·F − 12`) | **open** — this is where `σ_theory` lives |

The trace is already exact (terminating Habiro sum), so 1 ppQ on the
trace is purely a compute-precision question (met at 50 dps). The open
work is the **shell**: tabulate `σ_theory(O, N)` as each *proved*
correction order is added and project the convergence rate to find N\*.
Empirical anchor so far (m_avg, no fitting): bare Family-A shell = +2.89 %
→ first spectral correction = 819 ppm (~35× per derived order). If that
rate held, ~9 proved correction orders would reach 1 ppQ — a *projection*
to be validated, not a result. Harness:
`per_observable_100x_status.py` should grow an `N`-sweep column
(`σ_theory` vs shell order) once the second derived correction lands.

> **Discipline note.** "Adding a higher-order term" means a **proved**
> categorical term (e.g. the next Habiro `a_m`, or a derived shell
> correction), **never** a CODATA-fitted tower. Fitting below the current
> `σ_theory` models the μ-p tension as signal — see
> [`audits/2026-05-28-mu-p-tension-substrate-floor.md`](audits/2026-05-28-mu-p-tension-substrate-floor.md).
> The μ-p 240 ppb is the floor of the *current low-order shell*; it is
> *derivable-below* (lower N residual), but *not fittable-below*.

## L1 — compute precision (default 1 ppQ)

**Definition.** Different methods computing the same quantity at substrate
q_0 must agree to at least 1 ppQ (10⁻¹⁵ relative, i.e. 10⁻⁶ ppb).

**Configuration.** Controlled by `computations/substrate/_precision.py`:

```python
COMPUTE_DPS_DEFAULT  = 65    # mpmath working precision (OUTPUT + GUARD)
OUTPUT_DPS_DEFAULT   = 50    # serialization precision
PRECISION_GUARD      = 15    # COMPUTE = OUTPUT + GUARD
```

The **1 ppQ target is the *minimum*** — raise via `QOU_COMPUTE_DPS=<n>`
environment override. At 50 dps output / 65 dps compute, serialization
truncation is ~10⁻⁵⁰ absolute (10⁻⁴¹ ppb), far exceeding 1 ppQ.

**Q_β is already at 0 ppQ (exact).** The Habiro expansion of the Markov
trace terminates at $M = 8$ for the proton/neutron (integer coefficients
$a_m \in \mathbb{Z}[u]$, evaluated at $u_0 = \sqrt{q_0}$). No
truncation error exists — the formula is a finite sum. See
[`prop:habiro-precision-ladder-equivalence`](../content/quantum-observable-universe/braids-and-knots/habiro-precision-ladder-equivalence.md).

> **Historical note (superseded).** The "precision ladder" (c_k
> coefficients at each "rung" N=3, N=4, N=5) was the Taylor expansion
> of this exact Habiro sum in powers of $\hbar_q^2$. It was useful when
> the closed form was unknown; now that the Habiro identification is
> established, the c_k are a compute artefact with no independent
> mathematical role. The per-rung table below is retained for historical
> reference only.

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

> **Table updated 2026-05-29 (post q₀ re-pin #1422 + de-fitting #1416).**
> Two anchors (m_e, m_p) meet trivially; **all five genuine predictions
> miss** the 100× target. Earlier versions of this table showed the
> *muon* pin (m_μ "meets, ratio-derived") and the *fitted* Q_β "5.7 ppb
> (N=5)" — both stale. Live source: `per-observable-100x-status.witness.json`.

| Observable | role | σ_exp_rel | **100× target** | Current pred error | Status |
|---|---|---:|---:|---:|---|
| m_e | CAL-1 anchor | 0.29 ppb | 2.9 ppt | 0 (anchor) | **anchor** ✓ |
| m_p | **CAL-2 numerical anchor** | 0.31 ppb | 3.1 ppt | 0.0004 ppb (round-trip) | **anchor** ✓ (not a prediction) |
| m_μ | prediction | 21.8 ppb | **0.22 ppb** | 210 ppb | **misses ~964×** (9.5σ μ-p tension) |
| Q_β | prediction (CAL-3 cross-check) | 0.78 ppm | **7.8 ppb** | 1247 ppb (1.25 ppm) | **misses ~160×** (de-fitted; N=5 ladder was a fit) |
| m_n | prediction (Path C) | 0.57 ppb | **5.7 ppt** | 1.04 ppb | **misses ~181×** |
| Δm_pn | prediction (Path C) | 474 ppb | **4.74 ppb** | 755 ppb | **misses ~159×** |
| m_K/m_π | prediction (meson ratio) | 26.4 ppm | **264 ppb** | 23.4 ppb (post-#1442 closure via `(3q²−1)/(2q²)`) | **MET** (~11× margin below target) |

**Honest summary: 3/7 "meet" — 2 calibration anchors (m_e, m_p)
plus m_K/m_π (closed via the merged meson EM correction `(3q²−1)/(2q²)`
in PR #1442; was previously listed as missing by ~1098× pre-merge).
m_K/m_π is the first genuine prediction to meet the 100× target; the
other 4 predictions (m_μ, Q_β, m_n, Δ_pn) still miss it.**
This is the de-fitted state: production reports the real residuals, not
CODATA-fitted towers. m_p's "0.0004 ppb" is a calibration round-trip
(see §"The 1 ppQ target is on the theory residual" — σ_theory = 0, the
residual is sub-σ_CAL CODATA input slop), not a framework prediction.

> **m_p is the numerical anchor (was a prediction pre-#1422).** Because
> q₀ is now inverted from m_p/m_e, m_p matches CODATA by construction.
> The genuine baryon-mass test is the *bare* categorical value
> (Family-A Borromean tower, m_p = 965.38 MeV, +2.89% open gap) and the
> m_μ / m_n / Q_β predictions above.

> **Path C (2026-05-26).** `m_n = m_p + Q_β + m_e` bypasses the
> flavor-split X. With m_p the anchor and Q_β a 1.25 ppm prediction,
> m_n lands at ~1.04 ppb and Δ_pn at ~755 ppb — both now **miss** the
> 100× target (they previously "beat" it only via the fitted N=5 Q_β).

> **CAL-3 σ source.** Q_β experimental uncertainty here is the PDG 2024
> value Q_β(n) = 0.78233341(61) MeV (≈0.78 ppm, 779.7 ppb relative). The
> earlier 640 ppm draft was based on a coarser AME quote (0.78232 ± 0.00050
> MeV); that figure is **incorrect** at the precision we care about. See
> [`computations/cal-3-q-beta.witness.json`](../computations/cal-3-q-beta.witness.json).
>
> **Q_β Habiro-exact evaluation.** The Markov trace of the proton/neutron
> braid words lives in the Habiro ring $\widehat{\mathbb{Z}[q]}$ and
> terminates at $M = 8$ (integer coefficients $a_m \in \mathbb{Z}[u]$).
> Evaluating at $u_0 = \sqrt{q_0}$ gives the EXACT Q_β prediction at
> 5.744 ppb — below the 7.80 ppb target. No per-rung approximation
> needed. See [`prop:habiro-precision-ladder-equivalence`](../content/quantum-observable-universe/braids-and-knots/habiro-precision-ladder-equivalence.md).

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

**Subgoal-1 (currently met only by the two anchors).** 100× targets
≥ ~780 ppb CAL-2 floor. Met: m_e (CAL-1 anchor), m_p (CAL-2 numerical
anchor) — both trivial calibration matches. **No genuine prediction
currently meets Subgoal-1.** Q_β is the closest (1.25 ppm vs 7.8 ppb
target, ~160×) after de-fitting (#1416) removed the CODATA-fitted N=5
ladder that previously read "5.7 ppb"; Δ_pn (~755 ppb) and m_n
(~1.04 ppb) follow Q_β. Closing them is the GAP-A program (per-isotope
Borromean-tower extension + operator-valued branching), NOT a fit.

> **Superseded (do not restore).** Prior text claimed "Q_β N=5
> categorical meets Subgoal-1 (5.7 ppb)" and "Δ_pn via Path C beats
> (4.0 ppb)". Both relied on the CODATA-fitted N=5 Q_β ladder removed
> in #1416. The honest de-fitted values miss the target.

**Subgoal-2 (research-grade).** 100× targets < CAL-2 floor. Includes
absolute m_p (3 ppt), m_n (6 ppt), m_⁴He (0.6 ppt). **Requires
substrate-derivation of q_0**, which the coordination ledger explicitly
declined on 2026-05-08:
> "Q_β derivation? **No** (explicit) — 780 ppb floor stands."
>
> By extension, q_0 (CAL-2) substrate-derivation is also declined.

Subgoal-2 is **out of scope** unless and until the ledger decision is
reverted by the repo owner.

> **Narrow owner reversal (2026-06-19, recorded 2026-06-22; PRs
> [#2503](https://github.com/litlfred/qou/pull/2503) /
> [#2524](https://github.com/litlfred/qou/pull/2524)).** The owner reversed
> the decline **only for the s5-so3 keystone geometric-realization
> construction** — the DG / WRT(S³/2I) build of the `W_λ` index (see
> [`docs/coordination/s5-so3-keystone.md`](coordination/s5-so3-keystone.md)).
> That geometric `W_λ` build is now **in scope**. The reversal is narrow: it
> does **not** reopen fit-based q_0 derivation, and the Δ_λ "no seventh
> fit-based ansatz" rule still holds. All other Subgoal-2 items remain out of
> scope without explicit owner sign-off.

## Where measured

Live snapshot: `computations/per-observable-100x-status.witness.json`
(produced by `per_observable_100x_status.py`). Re-run on every Borromean /
calibration / formula change.

Reproduce:

```bash
python3 computations/per_observable_100x_status.py
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
- [`computations/substrate/_precision.py`](../computations/substrate/_precision.py) — compute precision infrastructure
- [`computations/per_observable_100x_status.py`](../computations/per_observable_100x_status.py) — L2 status reporter
