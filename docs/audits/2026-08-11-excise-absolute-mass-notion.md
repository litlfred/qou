# Owner ruling 2026-08-11 — the notion of *absolute mass* is EXCISED

> **Notation note.** This document predates the 2026-09-05 calibration rename and uses
> the superseded symbols `𝔇_β` (CAL-2) and/or `𝔇_π` (CAL-3). Those are now
> `P_skew^β` (the bar-skew β-channel) and `P_avg^π` (the bar-even π-channel); the
> `𝔇` family is reserved for genuine decay rates (`𝔇_n`, `𝔇_μ`, `𝔇_K` = ℏ/τ).
> The analysis below is left as the record of what was analysed at the time.

**Bean:** `qou-exam` (excise-absolute-mass)
**Status:** permanent standing directive (framework reframing)

## The ruling

The repo owner ruled, in response to the "absolute masses have hit a
well-characterized wall" assessment, verbatim:

> **NO ABSOLUTE MASS — excise the notion.**

The framework no longer claims, targets, or scores an **absolute** nucleon
or atomic mass in MeV (m_p ≈ 938.27, m_n, m_⁴He, …) as a prediction. The
notion of "absolute mass as a framework output" is removed.

This is distinct from — and broader than — the 2026-08-02 *q₀-derivation
FOREVER GATED* ruling ([`2026-08-02-subgoal2-q0-derivation-forever-gated.md`](2026-08-02-subgoal2-q0-derivation-forever-gated.md),
bean `qou-eic1`). That gate closed one *route* (deriving q₀) while leaving
"absolute m_p/m_n via non-q₀ routes" nominally open. **This ruling closes the
*target itself*.**

## Why it is the honest reframing (not a retreat)

1. **Absolute mass carries no content beyond a ratio × the scale calibration.**
   Every mass in the framework is `m(K) = m_e · (dimensionless categorical
   quantity)`. The single dimensional input is the electron mass **m_e**
   (CAL-1); it *sets the MeV scale by fiat*, it is not derived. So
   `m_p [MeV] = m_e · (m_p/m_e)` — the only predictive content is the
   **dimensionless ratio** `m_p/m_e`. Reporting `m_p` in MeV as a "prediction"
   double-counts the m_e calibration and dresses a ratio as an absolute.

2. **The unreachable part was never content-bearing anyway.** Sub-CAL-2-floor
   absolute precision on m_p/m_n required deriving q₀ — now FOREVER GATED. So
   the absolute-mass target was both *not content-bearing* (ratio × scale) and
   *not achievable* (sub-floor gated). Excising it removes a goal that could
   only ever be met by fitting (the dropped Habiro tower, 2026-07-04) — exactly
   the anti-fit failure mode the discipline exists to prevent.

3. **The framework's genuine claims are dimensionless or differential** and are
   untouched.

## Scope

**EXCISED** (removed as predictions / goals / scored observables):

- absolute nucleon / atomic mass in MeV: **m_p, m_n, m_⁴He**, and any other
  absolute `m(K) [MeV]` reported as a framework output;
- the corresponding L2 100× *absolute-mass* scorecard rows (m_p ~437×,
  m_n ~420×, and m_μ-as-absolute ~964×) — you do not score what you no longer
  claim;
- "absolute nucleon mass" framing on the `computations/canonical_mass.py`
  facade → relabel its MeV outputs as **m_e-scaled realizations of the
  dimensionless ratio**, not fundamental predictions.

**RETAINED** (the framework's genuine, dimensionless-or-differential content):

- **dimensionless ratios**: `m_μ/m_e` (the 9.5σ μ-p tension prediction),
  `m_K/m_π` (MET), `m_p/m_e` (the CAL-2 pin — a calibration *input*, not a
  scored prediction);
- **binding energies** `B(K)` — dimensional as `m_e · Σ_λ y_λ χ^λ Δ_λ`, but the
  predictive content is the **dimensionless categorical binding**; the m_e is a
  passive scale;
- **decay Q-values / widths**: `Q_β = ℏ/𝔇_β` (the CAL-2 proxy), a difference,
  not an absolute mass;
- **mass splittings**: `Δ_pn = m_n − m_p` — a difference; its content is
  dimensionless up to the m_e scale.

The three calibration inputs are unchanged (m_e sets the scale; 𝔇_β, 𝔇_π the
two moduli). What changes is that **the scale calibration m_e is no longer
laundered back out as an "absolute mass prediction."**

## Consequence for the L2 precision scorecard

The L2 "N/7 meet" framing is reframed from *seven mixed observables* (five of
them absolute masses that miss by 160–960×) to the **dimensionless / differential
predictions only**: `m_μ/m_e`, `m_K/m_π`, `Q_β`, `Δ_pn`, `B(K)`. The absolute
`m_p`/`m_n` rows are removed rather than carried as perpetual ~400× misses. This
is the honest scorecard: it reports what the framework predicts, at the precision
it predicts it, without the m_e-calibration double-count.

## Follow-through (beaned — `qou-exam` children)

Mechanical sweep, to land after this ruling:

1. `docs/precision-goals.md` — reframe §L2 + the scorecard table (anchor edit in
   this PR).
2. `AGENTS.md` — the mass-formula banners (the `m(K)=m_e·Vol·ρ/ℏ_q²` and
   `canonical_mass` 🛑 banners) + §Precision goals L2 table: annotate that
   absolute mass is excised; keep the *ratio* / *binding* framing.
3. `docs/canonical-derivation-cheat-sheet.md` + `docs/canonical-mass-formula-guardrail.md`
   — relabel "absolute nucleon mass" → "m_e-scaled ratio realization".
4. `computations/canonical_mass.py` — docstring + emit metadata relabel (no
   compute change; the numbers are still available as `m_e · ratio`, just not
   called an absolute prediction).
5. `content/` mass-theory blocks that state absolute m_p/m_n as predictions —
   reframe to the ratio; audit via `grep -rl "938.27\|absolute mass" content/`.

**Honest scope.** This ruling changes *framing and targets*, not any proved
result: every Lean theorem, every dimensionless ratio, every binding derivation
stands. It removes a goal (absolute mass) that was ratio-redundant and
gated-unreachable. No compute is deleted; the MeV numbers remain derivable as
`m_e × ratio` for anyone who wants them — they are simply no longer a claim of
the framework.
