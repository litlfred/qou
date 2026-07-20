# c_3 via the colored-Jones / GGM-resurgence (Stokes) route — a falsifiable two-anchor test: NEGATIVE, scope-(a)

**Date:** 2026-07-20 · **Bean:** `qou-1dnr` (c_3 → Q_β 100× gap-closer) ·
**Branch:** `claude/argument-principle-residue-sum-2026-07-20`
**Axis:** c_3 / Q_β bar-odd decay face / 1ppQ · **Tier:** numerical scope-(a)
measurement + a sorry-free formalize-first obstruction ·
**Discipline:** no fit (nothing inverted from Q_β / CODATA to tune c_3), no c_k
wired, nothing to production, no tier change.

## 0. Route + parallelism (owner directive 2026-07-17: parallel independent
attack on open research is endorsed)

Door-v established Q_β is the **bar-odd / sinh / decay** face = the **GGM
colored-Jones / Gu–Mariño resurgence (Stokes)** face (opposite `(−1)^m` parity to
the bar-even mass face). This attacks the task's route directly: derive `c_3` as
an **"order-3 Stokes/resurgence coefficient"** of the Q_β decay-width period — the
integer Stokes constant of the figure-eight `4₁` — and subject it to the
falsifiable two-anchor test.

Distinct from the two sibling routes on `qou-1dnr`:

| route | agent | object | this-doc relation |
|---|---|---|---|
| q-lift recursion / DM-cubic / Berezinian | sibling | real-q 3-jet `∂³F` / `B·D⁻¹·C` | NEGATIVE (commit `e52279df`): real-q candidate anchor-flat, refuted. Genuine target = resurgent bar-odd `S = h·D(ũ)`. |
| Habiro element | sibling | fibre-level `F(q)` Habiro ring elt | in progress |
| **GGM colored-Jones / Stokes resurgence** | **this** | **integer Stokes constant `−3` / `S⁺₁₁` tower** | tests the *resurgent* target the DM sibling pointed to; the naive bare-Stokes reading also fails. |

My angle is genuinely distinct from the refuted **Li₂^q × spectral combiner**
(mech #7, PR #1609) — that averaged a dilog-weighted `c_3^(λ)`; this reads the
**exact GGM state-integral / 3d-index Stokes datum** (integer count), the anti-fit
route the G3 keystone evidence base names.

## 1. The GGM order-3 Stokes datum (consumed, NOT re-derived)

From Garoufalidis–Gu–Mariño (`uploads/2012.00062v3.pdf`) §§4–5, already
implemented + certified exact in the corpus (`qbeta_g3_ggm_stokes_41.py`,
`qbeta-g3-ggm-stokes-41.witness.json`):

- singularity `ι = ±Vol(4₁)/π ≈ 0.646` (= the corpus's measured Borel `A`);
- **integer Stokes constant `3`** on that singularity (`S⁰ = [[1,0],[−3,1]]`,
  q→0 limit `S⁺(0) = [[1,3],[0,1]]`, eq 60);
- descendant tower `S⁺₁₁(q) = 1 − 8q − 9q² + 18q³ + 46q⁴ + 90q⁵ + 62q⁶ + …`
  (eq 61), certified exact (det `W_m = 2`; eq-49 q-difference; sandwich (59a)).

This probe **invents no Stokes data** — it consumes the published/certified
series and the integer `−3`.

## 2. The falsifiable two-anchor test

Producer:
[`computations/probes/qbeta_c3_stokes_ggm_order3_probe.py`](../../computations/probes/qbeta_c3_stokes_ggm_order3_probe.py)
→ [`qbeta-c3-stokes-ggm-order3.witness.json`](../../computations/probes/qbeta-c3-stokes-ggm-order3.witness.json)
(mpmath dps=60, audit_only). Anchors: proton-pinned `q₀ = q_at(60) =
1.10997858275138…`; muon-pinned `q₀ = 1/(1−√(Vol(4₁)/(m_μ/m_e))) =
1.10997859555418…` (CAL-2; solved in-probe, `Vol(4₁) = 3·Cl₂(2π/3)`), separated
by **11.53 ppb**.

**Test (per the task honesty rule):** a DERIVED `c_3` must be **anchor-invariant**;
a GGM Stokes constant IS (a fixed integer / a fixed convergent q-series) — so the
route passes the **type** test. The question is whether its **value** is `c_3`.

## 3. Results — three clean facts

| quantity | proton anchor | muon anchor | swing |
|---|---|---|---|
| GGM `S⁺₁₁` tower(`q=1/q₀`) | `116.5212824` | `116.5212754` | **`6·10⁻⁶ %`** |
| integer Stokes constant | `−3` | `−3` | `0` (exact) |
| Habiro **smooth** near-match `c_3(q₀)` | `−2.06934806` | `−2.06934808` | **`6.2 ppb`** |
| cal-anchored `c_3` (extracted from CODATA Q_β) | `−2.06934257711…` | — | — |

**Q_β `c_3`-rung residual** (`u = b·ℏ_q² ≈ 0.00852`, `u³ = 6.185·10⁻⁷`), vs the
**7.8 ppb** L2 100× target:

| `c_3` hypothesis | Q_β residual | miss |
|---|---|---|
| **`−3` (raw GGM order-3 Stokes integer)** | **575.6 ppb** | **73.8×** |
| `−2` (`J_Hopf(q=1)` near-match) | 42.9 ppb | 5.5× |
| `−2.069` (cal-anchored) | 0 | 0 |

Reading:

1. **The Stokes datum is the RIGHT TYPE.** Both the integer `−3` and the `S⁺₁₁`
   tower are anchor-invariant (tower swings `6·10⁻⁶ %`) — exactly the
   anchor-invariance a *derived* coefficient must have. The route is not
   disqualified for being anchor-invariant.
2. **The "swing" is NOT the obstruction.** The *extracted* `c_3` swings ~2–3.5%
   (`dc_3/dq ≈ 4.6·10⁶`, PR #1821), but the **smooth** Habiro closed form swings
   only **6.2 ppb** — the extracted swing is `1/u³` ladder-inversion
   hyper-sensitivity magnifying a smooth numerator zero (registry KC21), not
   physical anchor-dependence. So a Stokes datum being flat is *correct*.
3. **The VALUE is wrong.** `−3 ≠ −2.069` (off ~45%). As a `c_3` the raw Stokes
   integer gives a **576 ppb** Q_β residual — **74× the 7.8 ppb target**, and
   **worse than even the crude `−2` near-match** (43 ppb). The bare Stokes
   integer does not even beat the near-match it would have to improve on.

**Substrate-meridian complement** (already in corpus,
[`2026-07-18-dladder-fibre-branch-stokes-ambiguity.md`](2026-07-18-dladder-fibre-branch-stokes-ambiguity.md)):
on the real-`q₀` meridian the Stokes jump `exp(−A/u)` is `~10⁻²⁷`–`10⁻³⁹`
suppressed (anchor-blind), so there is **no substrate-meridian Stokes mechanism**
to source a ppm-level `c_3` rung; the unsuppressed `A_ω` lives on the fibre branch
(`|q|=1`, `u ~ O(1)`, leaving the ladder edge at `|u| ≳ 0.19`).

## 4. Verdict — NEGATIVE, scope-(a)

The GGM colored-Jones / resurgence (Stokes) route supplies a **correctly
anchor-invariant** order-3 datum (integer Stokes constant `−3`, `4₁` singularity
at `Vol(4₁)/π`) — the right **type** for a derivation — but its **value is not
`c_3`**. As a `c_3` it misses the Q_β 100× target by 74× and is worse than the
`−2` near-match; the substrate-meridian Stokes jump that would transport it is
`10⁻²⁷`-suppressed. **c_3 is NOT a bare GGM order-3 Stokes constant.**

This is a **scope-(a)** negative — *"the bare-Stokes-integer construction, alone,
does not reproduce c_3 as-is."* It is **NOT** a scope-(b) structural exclusion of
the Stokes route: a **normalized** Stokes datum (the open **§4e
quantum-modularity / 3d-index** bridge — a fixed-basis normalization of the
anchor-invariant integer onto the smooth bar-odd object) is not excluded and
remains the genuine open target (per KC22 the bar-odd object is
resurgent/transcendental, so the normalization is not a low-order q-holonomic
scalar to read off). Matching two `−3`'s (the GGM constant and, e.g.,
`disc ℚ(√−3)`) is **not** a derivation.

## 5. Formalize-first (sorry-free, lean-direct verified, Lean 4.24.0)

[`QOU/Mass/QbetaC3Stokes.lean`](../../content/quantum-observable-universe/lean/QOU/Mass/QbetaC3Stokes.lean)
— generic `{R} [Field R] [LinearOrder R] [IsStrictOrderedRing R]` (§7c; no `ℝ`):

- `stokesInt_strictly_worse_c3_than_nearMatch` (sorry-free) — for every `empC3 ∈
  [-21/10, -2]`, `|(-3) - empC3| > |(-2) - empC3|`: the algebraic shadow of the
  576 vs 43 ppb residuals.
- `constantStokesDatum_cannot_match_both_anchors` /
  `…_misses_other_anchor_by_full_swing` (sorry-free) — a constant Stokes datum is
  anchor-invariant ⇒ matches at most one anchor; pinned at proton it misses muon
  by the full swing.
- `NormalizedStokesC3Bridge` — content-bearing **primary conjecture class**
  (`norm * stokesDatum = smoothC3`, `norm ≠ 1`, `smoothC3 ≠ 0`), **no instance**:
  the honest open §4e normalization bridge.

**Intended import line (batch-add to `QOU.lean` — NOT edited here, concurrent
siblings):**

```
import QOU.Mass.QbetaC3Stokes
```

## 6. Discipline

scope-(a) vocabulary; pre-stated falsifiability test (anchor-invariant →
derivation; wrong value → negative); the `−3` and the `S⁺₁₁` tower are read off
GGM (certified in `qbeta-g3-ggm-stokes-41`); the cal `c_3` is the corpus's
already-published extraction, used only as the comparison target — **nothing
inverted from Q_β to fit `c_3`** (anti-laundering). Fibre-vs-observable respected
(the `c_k` live at fibre level; the substrate-meridian jump is suppressed, the
open datum is on the fibre). No `c_k` wired; no production; no tier change; bean
`qou-1dnr` STAYS OPEN. Honest NEGATIVE — it narrows the Stokes route from "bare
integer = c_3" (refuted) to the open normalized §4e bridge.
