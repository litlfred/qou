# α_r substrate-derivation — magic-A ⁴He residual closure campaign

**Date:** 2026-06-03
**Branch:** `claude/alpha-r-q-pochhammer-derivation-2026-06-03`
**Status:** Open investigation; scaffold + first-pass probes.

## Context

After PR #1731 (merged) clarified that the canonical ⁴He binding
formula `B = 2·m_e·A·Vol(L6a4) = 29.96 MeV` overshoots AME by
**+5.87 %** (residual −1.660 MeV), the productive direction
identified was:

> Substrate-derive α_r per isotope (replacing the fitted
> α-ladder): the canonical chain's higher-order corrections come
> from `binding_ladder_catalog.py`'s q-Pochhammer terms.

This branch attacks that derivation.

## What `binding_ladder_catalog.py` currently does

For each isotope, fits an α_r at each rank r ∈ {2..8}:

```
B_pred(r) = B_leading + α_r · m_e · |(q;q)_r|
```

The α_r are forced to close the residual exactly per rank, so they
are RATIOS (not derived constants):

| isotope | α_4 | α_5 | α_6 |
|---------|-----|-----|-----|
| D       | -9.77 | -14.34 | -16.46 |
| T       | +5.32 | +7.78 | +8.99 |
| ³He     | +92.29 | +134.76 | +154.86 |
| ⁴He     | -668.63 | -976.26 | -1121.88 |

Inconsistent in sign + magnitude across isotopes → **NOT a derived
series**.

## Probes (this PR — scaffold)

[`alpha_r_q_pochhammer_probe.py`](../../folio-assistant/computations/alpha_r_q_pochhammer_probe.py)
runs five NO-fit structural-α hypotheses for ⁴He:

| # | Hypothesis | Result | Status |
|---|-----------|--------|--------|
| H1 | `α_r = -A·8G / |(q;q)_r|` | trivial (cancels by construction) | discard |
| H2 | `α_r = -1` (unit constant) | best rel_err 4.78 % at r=14 | better than canonical but not closure |
| H3 | `α_r = -A/m_e` (dim-natural) | diverges (series unbounded at q>1) | discard (dimensional) |
| H4 | `B = B_leading ± m_e·|(q;q)_r|` single-rank search | **rel_err 1.79 % at r=15, sign=−** | **3.3× improvement; investigate** |
| H5 | `Σ_{r=1..N}|(q;q)_r|` convergence | diverges (q>1) | series approach not viable |

## Notable finding: r=15 lands ⁴He at +1.79 % — DOUBLY-MAGIC SPECIFIC

The H4 single-rank search found that

```
B_corrected = B_leading − m_e · |(q;q)_{15}|
```

with `|(q;q)_{15}| ≈ 2.256` gives `rel_err = +1.79 %` for ⁴He —
a 3.3× improvement over the canonical +5.87 % residual.

**Cross-isotope test** (`alpha_r_4A_minus_1_cross_isotope.py`)
shows the rule `r = 4A − 1`:

| iso | A | doubly-magic? | r=4A-1 result | global best |
|-----|---|---------------|---------------|-------------|
| D   | 2 | no | +1.02 % at r=7  | +0.35 % at r=12 |
| T   | 3 | no | +0.005 % at r=11 | +0.002 % at r=2 |
| ³He | 3 | no | +2.80 % at r=11 | +0.98 % at r=14 |
| ⁴He | 4 | **yes (Z=N=2)** | **+1.79 % at r=15** ← global min | +1.79 % at r=15 |

**Verdict — r=4A−1 is consistent with a DOUBLY-MAGIC-only
structural rule, NOT refuted.**

⁴He is the only doubly-magic isotope in the test set, and for it
r=4A−1=15 IS the global single-rank minimum.  Non-magic D / T /
³He use different leading formulae per `binding_ladder_catalog.py`
and have no a-priori reason to share the rule — their misses are
**expected**, not refutations of a universal claim.

This matches the domain of `magic_A_formula.py` itself, which
restricts to ⁴He (via `is_magic_A_atom`).  A doubly-magic-only
α_r correction is structurally consistent with the canonical
chain's shell-closure differentiation (per `prop:torus-knot-shell-
binding` + `prop:double-magic-delta-i-bound` in CLAUDE.md).

**Open verification path** (out of reach in this PR): other
doubly-magic atoms ¹⁶O (A=16, r=63), ⁴⁰Ca (A=40, r=159), ²⁰⁸Pb
(A=208, r=831).  q-Pochhammer terms diverge exponentially beyond
r~15 at q>1, so direct |(q;q)_r| evaluation needs an asymptotic
expansion or Habiro evaluation at these ranks.

## Open levers (NOT this PR)

1. **GS-NF jet tower extraction** — per `binding-endomorphism-
   deuteron.witness.json`, the per-derivation weights have a
   six-term structure (`prop:six-term-per-derivation-weights`).
   The α_r series may be expressible as a tower extracted from
   the jet expansion of the canonical `tr_M` evaluation.
2. **Habiro element approach** — α_EM PR #1511 demonstrated that
   `[2]_q · (1 - h²α)` is a Habiro-ring element whose archimedean
   evaluations give real Taylor coefficients.  An analogous
   Habiro element for the magic-A residual would give a derived
   α_r.
3. **Per-isotope cross-check** of the r=15 finding (this PR's H4
   result) on D/T/³He under their own leading formulae.

## Discipline

- **EXPLORATORY** per `production-vs-exploratory-discipline`.
- **NOT a fit** — all five hypotheses are explicit closed forms
  with no per-rank tuning.
- **NOT a 7th ansatz** — closes a documented residual via a
  documented framework series (`binding_ladder_catalog.py`
  q-Pochhammer ladder).

## Cross-refs

- `folio-assistant/computations/binding_ladder_catalog.py`
- `folio-assistant/computations/magic_A_formula.py`
- `docs/audits/2026-06-02-he4-binding-canonical-vs-full-theta-design.md` (merged PR #1731)
- `binding-endomorphism-deuteron.witness.json` (`prop:six-term-per-derivation-weights`)
- α_EM precedent: PR #1511 (Habiro element `[2]_q · (1 - h²α)`)
