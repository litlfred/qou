# The three calibration layers — math ideal / observational ideal / fitted ideal

**Status:** convention record. Owner-specified 2026-08-26.
**Beans:** `qou-mkgt` (epic), `qou-nds9` (this doc), `qou-zeeg` (producer).

The framework has **exactly three calibration points** in every layer below.
The layers differ *only* in **how the three values are chosen** — never in how
many there are. No layer introduces a fourth degree of freedom, and the count
identity with `H¹(Bring) = 2W` (rank-2 W-plane scale + modulus + one orthogonal
class; 2+1 = 3, Lean `QOU.Mass.calibrations_eq_cohomology`) is untouched.

| Layer | The three points are… | Chosen by |
|---|---|---|
| **Math ideal** | the canonical triple CAL-1 `m_e`, CAL-2 `𝔇_β`, CAL-3 `𝔇_π` | definition — this is *what the calibration is* |
| **Observational ideal** | the same three, taken as **measured values** (CODATA / PDG), via their numerical proxies `m_e`, `m_μ/m_e` (or `m_p/m_e`), `m_π` | measurement |
| **Fitted ideal** | the same three, treated as **free parameters** | minimising binding-energy error over a set of low isotopes (²H, ³H, ³He, ⁴He, …) against AME2020 |

## What the fitted ideal is for

It separates two things the other two layers confound:

- the **choice of calibration** (which observables you elect to reproduce exactly), and
- the **model's own error** (how well the framework's *shape* tracks nature once
  calibration is chosen as favourably as possible).

The observational ideal reproduces its three anchors *exactly by construction* —
so those three carry no information about model quality (this is the same
tautology `AGENTS.md` §"Precision goals" already forbids scoring: `m_e` and `m_p`
are inputs, not predictions). The fitted ideal instead spends the same three
degrees of freedom on an **over-determined** objective: 3 parameters against
N > 3 isotopes. The residual that survives is therefore a genuine, falsifiable
measure of model error, and it is the strongest of the three layers for judging
the framework.

## The fitted ideal is a fit, and is labelled one

Per `AGENTS.md` §"Axiomatization is NOT a Proof" and the Δ_λ anti-fit rule:

- The fitted-ideal values are **fitted**, not derived. They may be reported and
  compared; they may **not** be wired to production as canonical, and no
  quantity derived from them may be presented as a parameter-free prediction.
- The canonical layer remains the math ideal; the production numerical pin
  remains the **proton** experimental anchor (owner directive 2026-08-07,
  re-affirmed 2026-08-15 R2). This layer changes neither.
- It is *not* a fourth calibration: the count stays three. What changes is the
  objective the three are chosen against.

## Identifiability — measured, not assumed

Low-isotope binding enters the chain as

    B(K) = Q_β(n) · ( tr_M(W_free) − tr_M(W_atom) )

(`computations/binding_canonical.py`). Reading the three calibration DOF off
that formula:

1. **CAL-1 (`m_e`)** — a pure multiplicative MeV scale on every `B`. Identifiable,
   and only through the overall normalisation.
2. **CAL-2 (`𝔇_β`, proxy `q₀`)** — enters both `Q_β` and the dimensionless trace
   difference, non-linearly and differently per isotope. Identifiable.
3. **CAL-3 (`𝔇_π`, proxy `m_π`)** — **does not appear in `B` at all.** The
   low-isotope binding objective is therefore *flat* in CAL-3: it cannot be
   fitted against this target set.

So the fitted ideal has **three calibration points but two identifiable
directions** under a pure low-isotope-binding objective. CAL-3 must either be
held at its observational value, or the objective must be widened by a
meson-sector observable (e.g. `m_K/m_π`) that does constrain it. Any report of a
fitted-ideal calibration must say which of the two was done — a fitted CAL-3
quoted off a flat objective is meaningless.

## Result

Producer: [`computations/fitted_ideal_low_isotope_calibration.py`](../../computations/fitted_ideal_low_isotope_calibration.py)
→ `computations/fitted-ideal-low-isotope-calibration.witness.json`. Runs in 0.3 s.

Relative-RMS binding error over the seven isotopes (²H, ³H, ³He, ⁴He, ⁶Li, ⁷Li, ⁷Be):

| Layer | rel-RMS | calibration values |
|---|---|---|
| Observational ideal | **93.09 %** | `q₀ = 1.10997858`, `Q_β = 0.78233 MeV`, `m_e = 0.51100 MeV` (all measured) |
| Fitted ideal, scale only | **62.26 %** | `q` held at `q₀`; scale free |
| Fitted ideal, both identifiable directions | **28.80 %** | `q = 1.14615282` (+3.26 %), `Q_β = 2.7435 MeV` (3.5×), implied `m_e = 1.9455 MeV` (3.8× CODATA) |

Per-isotope residual at the two-direction best fit:

| | ²H | ³H | ³He | ⁴He | ⁶Li | ⁷Li | ⁷Be |
|---|---|---|---|---|---|---|---|
| observational | −80.4 % | −91.8 % | −91.0 % | −96.9 % | −96.6 % | −97.2 % | −96.6 % |
| fitted | +31.4 % | −21.2 % | −17.4 % | **−59.2 %** | −12.3 % | +0.4 % | +20.2 % |

Two things the numbers carry:

1. **Recalibration buys a lot and still fails.** 93.1 % → 28.8 % is a real
   improvement — the observational layer is a long way from the best this model
   can do — but 28.8 % RMS is still ~10⁷ times outside the L2 100× target, and
   the residual remains **shape-structured, not normalisation-structured**
   (²H over-predicts, ⁴He under-predicts by −59 %, ⁷Li lands at +0.4 %). ⁴He,
   the doubly-magic case, is the worst outlier at the fitted point.
2. **The fit demands calibration values far outside measurement.** Reaching
   28.8 % requires an implied `m_e` of 1.95 MeV against CODATA's 0.511 — a
   factor 3.8 — and `q` shifted +3.26 % off the substrate pin. So the fitted
   ideal is not a rescue of the model under a kinder calibration; it is a
   **bound on what recalibration alone can buy**, and the bound is far short.

**Reading (scope-(a), per `AGENTS.md` §"Before declaring refuted"):** a
scope-limited negative about the *current* binding construction — its
`A`-dependence is wrong, not merely its normalisation, and no choice of the
three calibration values fixes that. It excludes no ingredient. It is
independent evidence for the already-recorded finding that the missing object is
a separate super-pairwise **additive extensive** term rather than a per-block
re-weighting
(`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`).

### One defect avoided, worth recording

`tr_m_wenzl_bridge_mpfr._load_y_lambda` picks a **cached** `y_λ` table by
matching `q_str` against the known anchors, and for an **unrecognised** `q₀`
"keeps the previous default rather than guessing" — the proton table. Inside a
fit loop *every* trial `q` is unrecognised, so calling the bridge naively pairs
proton-pinned `y_λ` with `χ_λ` evaluated at the trial `q`: a systematic instance
of the layer straddle `AGENTS.md` documents (the μ₃ Fréchet incident, 11.54 ppb
— and far worse here, since the trial `q` ranges over several percent rather
than sitting 11 ppb away). The producer takes `χ_λ` from the bridge's
`return_breakdown` (χ depends only on the word and `q`, never on the `y` table)
and recombines it with `y_λ(q)` from the live closed form at the same `q`.

Anyone extending this objective to another observable must do the same. The
producer is gated on reproducing the committed
`low-isotopes-binding-sweep.witness.json` `B_pred` at `q₀` to 1e-6 and refuses
to print a fitted number otherwise, precisely so a broken evaluator cannot
launder one.

## Superseded baseline (scale-only, kept for the record)

Fitting **only** the overall scale (CAL-1 direction) against the seven isotopes in
`computations/low-isotopes-binding-sweep.witness.json`, holding `q₀` at the
production pin:

| | RMS relative error | worst |
|---|---|---|
| Observational ideal (scale = 1, as-is) | 93.09 % | −97.18 % (⁷Li) |
| Fitted ideal, scale-only (scale ≈ 8.649) | 62.26 % | −75.62 % (⁷Li) |

The residual is **shape-structured, not normalisation-structured**: at the
best-fit scale ²H over-predicts by +69 % while every `A ≥ 4` isotope
under-predicts by −70…−76 %. The `B_AME/B_pred` ratios span 5.11 (²H) → 35.48
(⁷Li), a factor of ~7. A single multiplicative scale cannot absorb a factor-7
spread, and neither can adding one more smooth DOF in `q₀`.

**Reading (scope-(a), per `AGENTS.md` §"Before declaring refuted"):** this is a
scope-limited negative about the *current* binding construction — the
`A`-dependence of `B_pred` is wrong, not merely its normalisation. It is
consistent with, and independent evidence for, the already-recorded finding that
the missing object is a **separate super-pairwise additive extensive term**
rather than a per-block re-weighting
(`docs/audits/2026-08-02-deltalambda-value-proved-downstream-and-additive-term.md`).
It excludes no ingredient; it bounds what recalibration alone can buy.
