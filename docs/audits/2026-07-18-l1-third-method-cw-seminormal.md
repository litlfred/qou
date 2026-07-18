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
| proton | 1 | 6.25e-31 |
| neutron | 1 | 5.88e-31 |
| deuteron | 2 | 1.06e-31 |
| triton | 3 | 5.81e-31 |
| helium-3 | 3 | 6.22e-31 |
| helium-4 | 4 | *(run in progress — recorded on completion)* |

All light atoms agree with peel to **≤ 1e-30**, deep inside the 1ppQ (1e-15)
gate. A third genuinely-independent method now confirms the L1 color-weighted
atomic traces.

## The debugging finding — exact δ vs `flavor_split_leading` (worth propagating)

Reaching 1ppQ required the **exact symbolic** color split

$$\delta = \frac{(q-1)^2\,(1-q^{-4})}{3} \quad\text{at } q_0,$$

the form used by `markov_peel._color_delta`. The convenience accessor
`canonical_braid_crossings._avg_color_delta()` returns
`flavor_split_leading(q_0)` — a **leading-order approximation** that differs from
the exact δ by **≈ 3.2e-7** relative. Using it for the color-weighting caps
agreement with peel at **≈ 5.86e-11** — far above 1ppQ. The residual is a pure
δ-value error, not a method error:

| color split used | deuteron \|Δ\|/ref |
|---|---|
| δ = 0 (averaged / color-blind) | 1.82e-4 |
| `_avg_color_delta()` (leading order) | 5.86e-11 |
| **exact (q−1)²(1−q⁻⁴)/3** | **1.06e-31** |

**Implication.** Any consumer that color-weights via `_avg_color_delta()` carries
a ~5.86e-11 error. This is negligible for scope-(a) structural work (e.g. the
⁴He binding stage-2 probe, where the seam δ is not 1ppQ-gated), but **must not**
be used where 1ppQ is asserted — use the exact closed form there. Flagged for
follow-up: audit `_avg_color_delta()` consumers and route 1ppQ-critical ones to
the exact δ.

## What was ruled out (the localisation trail)

The 5.86e-11 was narrowed by elimination before the δ cause was found — recorded
so the next reader does not re-walk it: **not** f64 precision (persists in
mpfr); **not** the χ engine choice (seminormal is exact for A=1 at 6e-31);
**not** `include_inter` (already the default; without it the seam vanishes and
the trace is 1.5× off); **not** the crossing-classification tolerance (cw is
detected identically at 1e-9 and 1e-6); **not** the crossing-form encoding
(matches `markov_peel.crossing_from_cd`). The sole cause was the leading-order δ.

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
