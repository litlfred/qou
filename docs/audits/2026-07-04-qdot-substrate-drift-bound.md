# Substrate-flow bound: lab mass-ratio drift limits pin `q̇/q ≲ 5×10⁻¹⁹ yr⁻¹`

**Date:** 2026-07-04
**Branch:** `claude/mu-p-tension-closure-uua4os`
**Executes:** follow-up **#3** of [`2026-07-02-bekenstein-vsl-review.md`](2026-07-02-bekenstein-vsl-review.md) §3.4/§5 (bean `4big`)
**Probe:** [`scripts/qdot_substrate_drift_bound_probe.py`](scripts/qdot_substrate_drift_bound_probe.py) (self-contained, exit 0)

## What this closes

The Bekenstein/VSL review flagged (§4, unsoftened reception forecast) that the
framework owes a varying-constants referee **its own falsifier** — the analogue
of Bekenstein's 1982 Eötvös computation. The missing piece was a present-day
bound on the substrate flow `q̇/q`. This audit supplies it for the two
mass-ratio channels that are closed-form **today** (the α channel stays blocked
on the open `α_EM(q)` derivation).

## Method

If `q` flows in cosmic time, any dimensionless observable `X(q)` drifts with it,
and the chain rule converts a laboratory/astrophysical constancy limit into a
bound on the modulus:

$$
\frac{\dot X}{X} = \frac{d\ln X}{d\ln q}\cdot\frac{\dot q}{q}
\quad\Longrightarrow\quad
\left|\frac{\dot q}{q}\right| \le \frac{|\dot X/X|_{\text{bound}}}{|d\ln X/d\ln q|}.
$$

The mapping formula is the durable content — plug in any updated limit.

## Channel sensitivities at q₀ (= 1.10997858275…)

| channel | `d ln X / d ln q` | source |
|---|---|---|
| `m_μ/m_e = Vol(4₁)/ℏ_q²` | **−18.185** (exactly `−2/(q−1)`, analytic) | closed form; verified to 10⁻⁴² |
| `m_p/m_e = 2(Vol(4₁)/ℏ_q²)F_Bor − 12` | **−20.997** (numeric, via the canonical F_Bor) | the lab-constrained ratio μ |

Both are O(20) — the framework is **more** sensitive to `q`-drift than a naive
`ℏ_q`-only estimate, so the mass-ratio channel is a *strong* probe of the modulus.

## The bound

| stated limit `|Ẋ/X|` (per yr) | ⇒ `|q̇/q|` (per yr) | ⇒ total `|Δq/q|` over 13.8 Gyr |
|---|---|---|
| 10⁻¹⁶ (conservative) | ≲ 4.8×10⁻¹⁸ | ≲ 6.6×10⁻⁸ |
| **10⁻¹⁷** (representative best μ = m_p/m_e) | **≲ 4.8×10⁻¹⁹** | ≲ 6.6×10⁻⁹ |
| 10⁻¹⁸ (hypothetical clock tightening) | ≲ 4.8×10⁻²⁰ | ≲ 6.6×10⁻¹⁰ |

(The `m_p/m_e` channel is used for the headline because μ = m_p/m_e is the
directly lab/astro-constrained ratio — molecular H₂ / methanol absorbers; the
`m_μ/m_e` channel, tighter in principle, has no comparably direct present-day
drift limit and serves as the closed-form cross-check.)

**Reading.** The tightest available μ-drift limit already pins the substrate
modulus to `|q̇/q| ≲ 5×10⁻¹⁹ yr⁻¹` — `q` constant to ~7×10⁻⁹ over cosmic
history. This is **consistent with, and sharpens**, the corpus picture that any
interesting substrate motion is confined near the `q → 1⁺` endpoint (early
epochs), not a present-day drift — the same structure as the Albrecht–Magueijo
phase-transition VSL variant noted in the review §1.2.

## Scope / discipline

Falsifiability statement, not a value prediction and not a fit. Nothing wired;
CAL-1/2/3 untouched; the cited drift limits are representative published
order-of-magnitude bounds (the formula absorbs any exact replacement). The α
channel remains blocked on `α_EM(q)`; when that lands, the second (independent)
bound drops straight in via the same probe. Closes review follow-up #3 (bean
`4big`); follow-ups #1 (Ellis–Uzan remark block) and #2 (∂_q mass–energy
continuity law) remain open.
