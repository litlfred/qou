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

## Baseline result (scale-only, no recompute)

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
