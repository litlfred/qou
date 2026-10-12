# Quark template, tracked order by order in the tower: results

Recipe: `preregistration.md`, committed (6b9dd5d172) before anything was computed. Producer: `quark_template_tower_probe.py`. Verdicts use exact arithmetic over ℚ(q) (sympy); values use mpmath at 60 dps at the proton pin q₀. **4/4 checks pass.** Nothing is compared with Q_β, CODATA or any mass, and nothing is selected. The selection rule stays open (bean `qou-99qc`).

Notation: t = q − 1 and h = q − q⁻¹ = 2t + O(t²). Reading 3 (the ruled confinement test) requires χ_(3) ≥ 0 and χ_(2,1) ≥ 0. Here χ_(3) > 0 for every variant, so the verdict is the sign of χ_(2,1).

## 1. Where in the tower the quark content lives

**At order t⁰, flavour is invisible.** σ⁻¹ = σ − h, so every quark letter equals σ at q = 1. All 8 templates then give the same element (check C2, at the level of the matrix, not just the trace). That element has χ_(2,1) = 0, so at order zero reading 3 holds with **equality** for every template. The classical level of the tower cannot tell the templates apart.

**The verdict is decided at order t¹,** the first order where the quark sign bits enter. When the t¹ coefficient cancels, it is decided at order t³. For all 32 cells (8 templates × 2 nucleons × 2 dressings), the partial sums of the t-series have the same sign at q₀ from the leading order through t⁶. Every sign at q₀ also agrees with the exact sign on the sub-interval of (1, ∞) that contains q₀. So no verdict flips as the tower is truncated at a different order.

This makes the owner's remark precise: the quarks sit one order up the tower from the γγ core, and reading 3 sees them only there.

## 2. Primary result: no gluon dressing (k = 0), builder's generator placement

| template (sign map, pair rule) | proton χ_(2,1)(q₀) | leading order | neutron χ_(2,1)(q₀) | leading order | admissible for both? |
|---|---|---|---|---|---|
| **S+ AVG (corpus)** | **−0.09198** | t¹, − | **−0.18200** | t¹, − | **no** |
| S+ LO | 0 (identically) | — | −0.42477 | t¹, − | no |
| S+ HI | −0.18003 | t¹, − | +0.05684 | t³, + | no |
| S− AVG | +0.14944 | t¹, + | +0.23946 | t¹, + | yes |
| S− LO | +0.05684 | t³, + | +0.48410 | t¹, + | yes |
| S− HI | +0.23687 | t¹, + | 0 (identically) | — | yes |
| S0 (flavour-blind, all σ) | 0 (identically) | — | 0 (identically) | — | yes (equality) |
| S1 (flavour-blind, all σ⁻¹) | +0.05684 | t³, + | +0.05684 | t³, + | yes |

Sign maps: S+ is u = +1, d = −1 (the corpus); S− is the bar-swap, u = −1, d = +1. Pair rules: AVG = ½(σ^{ε_a} + σ^{ε_b}); LO and HI take the sign of the lower- or higher-index quark.

**Outcome (iii): the corpus template conflicts with the ruled SDP**, even with no gluons. Its χ_(2,1) is negative for both nucleons, with the sign set at order t¹. For example, for the proton

    χ_(2,1) = (q−1)(q+1)(q⁴+1)·P(q) / (4q⁹),   P = q¹² − 2q¹⁰ + 2q⁸ − 3q⁶ + 2q⁴ − 2q² + 1,

and the neutron carries the same P. P has exactly one root q* > 1, and it is exact: **q*² + q*⁻² = 1 + 2cos(2π/7)**, so q* = 1.278895277… (P becomes y³ − 2y² − y + 1 with y = q² + q⁻², the heptagon cubic). χ_(2,1) is negative on (1, q*) and positive above q*. q₀ = 1.10998 lies in the negative part.

**Within flavour-distinguishing templates, reading 3 picks the sign map, not the pair rule.** Every S+ template fails for at least one nucleon, and every S− template passes for both. So under the builder's placement, reading 3 forces **ε_u = −1, ε_d = +1**, the reverse of the corpus, and leaves AVG, LO and HI all admissible. The two flavour-blind templates also pass, so reading 3 alone does not force flavour to matter.

## 3. Secondary: with the gluon dressing G = σ₀σ₀

No template is admissible for both nucleons. The survivors are S− AVG (neutron only), S− LO (neutron only) and S− HI (proton only). The S+ AVG cell reproduces the known values −0.28059 (p) and −0.37196 (n) (check C1, against `build_nucleon_nf_mp` to 10⁻⁴⁰). So G breaks reading 3 for every template, which agrees with the corpus finding that the gluon pair σ₀σ₀ fails reading 3.

## 4. Tertiary: template and placement varied together (k = 0)

Number of admissible placements out of 8 (each of the 3 quark letters on σ₀ or σ₁):

| template | p | n |
|---|---|---|
| S+ AVG | 4 | 4 |
| S− AVG | 4 | 4 |
| S+ LO | 7 | 6 |
| S+ HI | 2 | 5 |
| S− LO | 5 | 2 |
| S− HI | 6 | 7 |
| S0 | 7 | 7 |
| S1 | 5 | 5 |

The S+ AVG row reproduces the corpus count of 4/8 per nucleon (check C4). So **the conflict in §2 depends on the placement.** With placement free, S+ AVG has 4 admissible placements per nucleon: proton 000, 011, 100, 111; neutron 010, 011, 100, 101. The builder's placement 001 is not among them, for either nucleon. Reading 3 constrains the sign map and the placement **jointly**; it does not constrain the template on its own.

## 5. What this does and does not establish

- **Established (exact).** Flavour enters the nucleon element at order t¹ and not at t⁰. Reading 3 is marginal at t⁰ for every template and decided at t¹ or t³. No verdict changes between truncation orders t¹ … t⁶ or between q₀ and the rest of its sub-interval.
- **Established (exact).** With the builder's placement and no gluons, the corpus template fails reading 3 for both nucleons, and the bar-swapped sign map passes with every pair rule.
- **Not established.** That the bar-swapped template is "the" quark template. Reading 3 does not choose between the swap with any pair rule, the flavour-blind templates, and the corpus template on a different placement. That choice is the owner's.
- **Tension to note, not resolve.** Bean `qou-y2np` records the bar-swap as "refuted" (2026-09-05), but that refutation compares binding energies with measured data. That is a comparison at the measurement boundary, not a derived constraint, so under the no-fitting rule it cannot select. Reading 3 is the ruled derived constraint, and at k = 0 with the builder's placement it points the other way.
- The tower here is the order in q. The other half of the full tower, all n of H_n, is the separate H_9 run (`../ales_h9/`).
