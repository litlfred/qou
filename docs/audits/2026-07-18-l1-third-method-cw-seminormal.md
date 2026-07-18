# L1 defense-in-depth — a third, independent color-weighted method (Wedderburn/seminormal), and the exact-δ finding

**Date:** 2026-07-18 · **Axis:** L1 compute precision (1ppQ) ·
**Tier:** measurement (scope-(a); audit-only; no fit; nothing wired). **Branch:**
`claude/focused-euler-ez3iu4`.
**Producer:** [`computations/cross_check_trM_cw_seminormal_leg.py`](../../computations/cross_check_trM_cw_seminormal_leg.py)
· **Witness:** `computations/cross-check-trM-cw-seminormal.witness.json`.

## What this closes

The L1 1ppQ certification
([`2026-07-13-l1-4he-certification-complete.md`](2026-07-13-l1-4he-certification-complete.md))
left one optional hardening item open: *"a genuinely independent color-weighted
third method,"* because the two certified methods — `markov_peel` (Markov-axiom
recursion) and the chi-cache combiner — both realise the color-weighted atomic
trace, and the closed-form χ-anchor covers only the χ engine itself. This audit
supplies that third method and validates it against the peel reference at 1ppQ.

## The method

A third decomposition — **Wedderburn / seminormal** — for the color-weighted
atomic Markov trace:

$$\mathrm{tr}_M(\beta_{\mathrm{atom}}) = \Bigl|\, \textstyle\sum_\lambda y_\lambda(q_0)\,\chi_\lambda(\beta_{\mathrm{atom}}) \,\Bigr|,$$

with $\chi_\lambda$ from the Hoefsmit **seminormal** engine
(`pyhecke_native.chi_lambda_all_partitions_mpfr`, 50 dps) and the color-weighted
p–n seam handled by the exact two-branch identity

$$\sigma - h(\tfrac12 - \tfrac\delta4)\,\mathbf{1} \;=\; a_{cw}\,\sigma + b_{cw}\,\sigma^{-1}, \qquad a_{cw},b_{cw} = \tfrac12 \pm \tfrac\delta4,$$

so $\chi_\lambda(\text{cw word}) = a_{cw}\,\chi_\lambda(\sigma\text{-branch}) + b_{cw}\,\chi_\lambda(\sigma^{-1}\text{-branch})$ by linearity. This is a genuinely
different computational path from peel's Markov-axiom recursion — agreement at
1ppQ is an independent confirmation of both the χ engine and the color-weighting.

## Result

Cross-checked against the canonical `markov-peel-atomic-tr-m.witness.json`
reference (loaded live, so this tracks it):

| atom | A | \|Δ\|/ref |
|---|---|---|
| proton | 1 | 2.208e-49 |
| neutron | 1 | 2.403e-49 |
| deuteron | 2 | 4.387e-49 |
| triton | 3 | 3.612e-49 |
| helium-3 | 3 | 7.278e-49 |
| **helium-4** | 4 | **7.031e-49** |

All **6/6 atoms** agree with peel to **≤ 7.3e-49** (worst-case), ~34 orders of
magnitude inside the 1ppQ (1e-15) gate. A third genuinely-independent method
(exact-δ, full-mpf, `mp.fsum`) now confirms the L1 color-weighted atomic traces.
Witness: `cross-check-trM-cw-seminormal.witness.json` (`allPassed: True`, ⁴He
n=12 leg ~17.5 min).

## The debugging finding — exact δ vs `flavor_split_leading` (worth propagating)

Reaching 1ppQ required the **exact symbolic** color split

$$\delta = \frac{(q-1)^2\,(1-q^{-4})}{3} \quad\text{at } q_0,$$

the form used by `markov_peel._color_delta`, **evaluated at the same q₀ pin as
the L1 traces**.

> **Correction (2026-07-18, this session — corrected twice).** An earlier draft
> attributed the 3.2e-7 δ gap to `_avg_color_delta()` being a *"leading-order
> approximation"* (wrong — `flavor_split_leading(q)` IS the exact
> `(q−1)²(1−q⁻⁴)/3`, = `markov_peel._color_delta`'s δ_symbolic to 2.6e-54). A
> second draft then called `_avg_color_delta()` *"proton-pinned"* with a live
> *"mixed-pin hazard"* — **also over-stated.** `q_parameter.Q` is
> **anchor-adaptive**: proton by default, **muon under `QOU_Q0_ANCHOR=ideal`**
> (which every L1/he4 producer sets). The 5.86e-11 I measured came from my
> *diagnostic* running standalone **without** the anchor. A full sweep of the
> ~40 consumers finds **0 live mixed-pin bugs**. What remains is a **fragile
> guard** (correctness depends on the anchor being set) + a precision ceiling
> (~5e-16 under the anchor, since the accessor reads the f64 `q_parameter.Q`).
> Full corrected analysis: [`2026-07-18-avg-color-delta-q0-pin-mismatch.md`](2026-07-18-avg-color-delta-q0-pin-mismatch.md).

| color split used | deuteron \|Δ\|/ref |
|---|---|
| δ = 0 (averaged / color-blind) | 1.82e-4 |
| `_avg_color_delta()`, **no anchor** (proton) — my un-anchored diagnostic | 5.86e-11 |
| `_avg_color_delta()`, `QOU_Q0_ANCHOR=ideal` (muon, f64 q₀) | ~1e-16 |
| **exact `(q₀−1)²(1−q₀⁻⁴)/3` at the 50-dps muon q₀** (this producer) | **≤ 7e-49** |

**Implication.** No production consumer is a live bug: muon-q₀ producers set
`QOU_Q0_ANCHOR=ideal`, under which `_avg_color_delta()` is muon-correct to ~5e-16
(inside 1ppQ, ~10× margin). This producer sidesteps both the anchor dependence
and the f64 ceiling by evaluating the closed form at the **50-dps** muon q₀
directly (~7e-49). For deep-1ppQ elsewhere, do the same:
`flavor_split_leading(local_q0_50dps)`.

## What was ruled out (the localisation trail)

The 5.86e-11 was narrowed by elimination before the δ cause was found — recorded
so the next reader does not re-walk it: **not** f64 precision (persists in
mpfr); **not** the χ engine choice (seminormal is exact for A=1 at 6e-31);
**not** `include_inter` (already the default; without it the seam vanishes and
the trace is 1.5× off); **not** the crossing-classification tolerance (cw is
detected identically at 1e-9 and 1e-6); **not** the crossing-form encoding
(matches `markov_peel.crossing_from_cd`). The sole cause was the δ **q₀-pin**:
my diagnostic called `_avg_color_delta()` **un-anchored** (proton default)
against the muon L1 reference — an artifact of the diagnostic, not of any
consumer (see the Correction box above).

## Note — the GP path

The now-fixed Geck–Pfeiffer engine (`chi_lambdas_via_gp`, main `61c401a610`,
verified here: reproducer χ_[12] = q exactly) was also tried as the independent
engine, but a naive two-branch evaluation of its Laurent output gave nonsense
(O(1–60) errors) — its sign/word convention differs and needs a dedicated
adapter. The seminormal path already supplies a fully-independent third method,
so the GP adapter is left as optional further hardening.

## Relationship to the L1 gate (standalone, not inlined)

The ⁴He leg of this method costs ~17 min (n = 12, seminormal-mpfr over all 77
H₁₂ blocks × 2 branches), so it is deliberately **not** inlined into the fast
L1 gate `computations/cross_check_trM_1ppb.py` (peel + chi-cache). It is a
**standalone third-method confirmation** — its own producer + witness — that the
L1 cert references as the independent-Wedderburn cross-check. The gate stays
fast; the third method runs on demand / in the witness pipeline.

## Cross-references

- L1 cert: [`2026-07-13-l1-4he-certification-complete.md`](2026-07-13-l1-4he-certification-complete.md)
- L1 gate (peel + chi-cache): `computations/cross_check_trM_1ppb.py`
- Precision goals: [`docs/precision-goals.md`](../precision-goals.md) L1 row
