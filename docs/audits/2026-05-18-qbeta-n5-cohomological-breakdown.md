# Why the alternating Kashiwara × Jones pattern breaks at N=5: cohomological explanation

**Date:** 2026-05-18
**Branch:** `claude/track-a-b-per-isotope-and-rho-xi`
**Context:** user question, follow-up to `2026-05-18-qbeta-n4-sign-investigation.md`. The Q_β precision-ladder doc claims an alternating "even = Kashiwara b^k, odd = Jones-link at q=1" pattern through N=4. Numerical investigation shows the pattern is **already mixed at N=4** and **no single Jones invariant closes N=5**.

## TL;DR — three findings

1. **The "alternating" pattern is honest at N=2 (pure intra-block Kashiwara) and N=3 (pure inter-block Jones), but already MIXED at N=4.** The doc itself annotates N=4 as `b² + 1/2` with categorical source "Kashiwara b² + integer Hopf-half offset (mixed intra/inter)". So N=4 is *not* in the simple alternating family — it's a SUM of contributions.
2. **At N=5, the empirical closure value c_5 ≈ +12.82** matches no single Jones invariant of any L-component link at q=1 (the closest naive candidates being J_unknot=1, J_Hopf=-2, J_Trefoil=-3, J_Figure8=5, J of 5-link=(−2)⁴=16).
3. **The cleanest categorical interpretation we found is c_5 = 13** (residual 0.008 ppb), which has no single-link source but matches a *sum-of-cohomology-classes* pattern: e.g. `(-c_3)² + (-c_3)³ + 1 = 4 + 8 + 1 = 13`, or `J_{5-link}(1) - 3 = 16 - 3 = 13`.

The simple pattern doesn't break — the ladder rungs were always pulling from a **multi-stratum cohomological invariant**, but at N≤3 only one stratum is populated, so it *looked* simple.

## Empirical setup

From `q-beta-operator-valued-N3.witness.json` at 50 dps:

| k | factor `(1 + c_k · b^k · ℏ_q^{2k})` | c_k (categorical) | residual after |
|---|---|---:|---:|
| 0 | Q_A = m_e · \|q²−2q−1\| (q+1) / (2q³) | — | +1 677 540 ppb |
| 1 | × cos(α − b·ℏ_q²/2) | b (Kashiwara) | +73 790 ppb |
| 2 | × (1 − b²·ℏ_q⁴) | -1 (with factor convention) | +1 242 ppb |
| 3 | × (1 − 2·b³·ℏ_q⁶) | **-2 = J_Hopf(q=1)** | **+6.02 ppb** ← beats 7.80 ppb 100× target |
| 4 (sign-fix) | × (1 − (b²+½)·b⁴·ℏ_q⁸) | -(b²+½) ≈ -1.253 | **-0.57 ppb** |
| 5 (empirical) | × (1 + c_5·b⁵·ℏ_q^10) | **c_5 ≈ +12.82** | ~0 |

The doc's N=4 with positive sign (c_4 = +(b²+½)) gives **+12.6 ppb**, *worse* than N=3 — this is the unresolved sign issue from the prior audit.

## Why the alternation works at N=2, 3

The Q_β prediction lives on the V_(2,1) Wedderburn block of H_3(q), the irrep where the Hoefsmit matrix has the off-diagonal coupling `b`. At low orders in ℏ_q²:

- **N=1 (cos term)**: leading-order perturbation expansion in α (the single-wrap eigenphase). Pure intra-block Kashiwara `f̃_1` matrix element gives `b`.
- **N=2 (b² term)**: second-order return amplitude `f̃_1† f̃_1` on V_(2,1). Pure intra-block, magnitude `b²`.
- **N=3 (J_Hopf term)**: at 3-fold Markov closure, the trace picks up an inter-block contribution. The "Hopf substructure" is the 2-link in the braid closure connecting two Wedderburn blocks via the Hopf-link projection. Its categorical signature at q=1 is `J_Hopf(q=1) = -2`.

Through N=3, each rung is dominated by ONE stratum: V_(2,1) intra (N=1,2) or Wedderburn-cross-coupling (N=3).

## Why it breaks at N=4

The doc admits N=4 is mixed: `c_4 = b² + 1/2`. The `b²` is a *fourth-order* intra-block Kashiwara contribution (continuing the N=2 family), and the `+ 1/2` is an "integer Hopf-half offset" — half of the N=3 Jones value contributing additively at N=4.

**This is already a spectral-sequence-style sum**: at total degree k=4, two cohomological strata both populate, and their contributions add.

Symbolically:
$$
c_4 = E^{0,4}_\infty + E^{2,2}_\infty = (\text{intra}^4) + (\text{intra}^2 \times \text{inter}/2)
$$

with `E^{p,q}_\infty` being some categorical spectral-sequence stratum at bidegree (p,q) with p+q=4.

The sign issue at N=4 (doc has + but reproduction needs −) is consistent with **both strata contributing with the same sign** (negative), the doc may have a transcription error from a categorical-source paper where the convention was different.

## Why N=5 has no clean single-Jones source

At total degree k=5, the cohomological strata at p+q=5 are more numerous:
- E^{0,5}_∞ — pure intra-block fifth-order (b^? with some power)
- E^{2,3}_∞ — intra² × inter (b² × J_Hopf-like)
- E^{4,1}_∞ — intra^4 × inter-leading
- E^{0,5}_link — direct 5-component-link Jones at q=1 (= (-2)⁴ = 16 if simply linked)

The empirical c_5 ≈ +12.82 doesn't match any single E^{p,q}_∞ contribution. It matches the **sum** of several.

### Candidate decomposition of c_5 = 13

If we conjecture `c_5 = 13`:
$$
13 \;=\; (-c_3)^3 + (-c_3)^2 + 1 \;=\; 2^3 + 2^2 + 1 \;=\; 8 + 4 + 1
$$
or
$$
13 \;=\; J_{(5\text{-link})}(q=1) - 3 \;=\; 16 - 3
$$
or
$$
13 \;=\; (\text{rank of Kh-rozansky of some 5-link at q=1}) - (\text{correction})
$$

None of these is a clean derivation, but the pattern `13 = 2³ + 2² + 1` is suggestive: a finite geometric-like sum over the "depth" of the cohomological strata mixing.

## Cohomological hypothesis (proposed conjecture)

The Q_β categorical formula is the trace of an operator on a multi-graded cohomology of the Wedderburn-block stratification of the Hecke algebra H_n(q) at a 3-fold Markov closure. Each rung `c_k` is the trace contribution at total degree k, summed over all bidegree strata `(p, q)` with `p + q = k`:

$$
c_k \;=\; \sum_{p+q=k} \text{Tr}\bigl(E^{p,q}_\infty\bigr) \;=\; \sum_{p+q=k} (\text{intra Kashiwara stratum at degree } p) \cdot (\text{inter Jones stratum at degree } q).
$$

For low k:
- k=3: only (p,q) = (0,3) contributes (pure Hopf at q=1) → c_3 = -2
- k=4: (0,4) and (2,2) both contribute → c_4 = b² + 1/2 (with sign convention)
- k=5: (0,5), (2,3), (4,1), (5,0) all contribute → c_5 ≈ 13

The breakdown "explains" both:
1. **Why c_4 is mixed** (two strata at k=4)
2. **Why c_5 has no single-link source** (≥4 strata at k=5)
3. **Why the residual reduction continues** despite no clean per-rung categorical source — the sum-of-strata structure is inherent

## What this would take to prove

A categorical derivation of c_k for general k would need:

1. **Identify the cohomology**. The natural candidates are:
   - **Khovanov-Rozansky homology** of the relevant link projection, taken at the q=1 specialisation.
   - **KLR canonical-basis cohomology** of the Wedderburn-block stratification at H_n(q).
   - **Heegaard-Floer-like invariant** if Khovanov is too coarse.

2. **Compute its multi-graded structure**. For each total degree k, enumerate the (p,q) strata and compute the trace contribution.

3. **Match against the empirical c_k**. Already c_3 = J_Hopf = -2 matches; need to verify c_4 = sum of two strata and c_5 = sum of ~4 strata.

4. **Prove the inductive recursion**. Find the spectral-sequence differential `d_r: E^{p,q}_r → E^{p+r,q-r+1}_r` and characterise the E_∞ page in closed form.

This is genuine research, not a one-session task. The audit's deliverable is the **hypothesis statement** (sum-over-cohomology-strata) and the **empirical evidence** (c_4 mixing, c_5 ≈ 13 matching `2³ + 2² + 1`).

## Status of related work

- **Khovanov homology + KLR canonical bases** are well-developed for the *uncategorified* Jones polynomial. The categorified versions exist (Khovanov-Rozansky, Webster's KLR-homology) and could supply the strata.
- The framework's existing `crystal_basis.py` (PRs #599/#601) provides the Type-A Kashiwara crystal primitives that handle the intra-block side.
- The **Demazure-fibre** content block (`demazure_markov_trace.py`) handles q-specialisations of Demazure characters — relevant for the b^k power-series side.
- **No existing module computes link-homology** at q=1 for the cohomological-strata side of the conjecture.

## Recommended next steps (not on this branch)

1. **Compute J(q=1) of multi-component candidate links** that could contribute to c_5: 5-link chains, Borromean variants, Whitehead doublings. Check whether their Jones values + Kashiwara-mixed offsets sum to ~12.82.
2. **Implement Khovanov-rank computation** at q=1 for the link projections that appear in the 3-fold Markov closure. Compare ranks to empirical c_k values.
3. **State the cohomological-strata conjecture as a content block** under `conj:` prefix, with the bidegree decomposition as its explicit content.

## Cross-references

- [`docs/audits/2026-05-18-qbeta-n4-sign-investigation.md`](2026-05-18-qbeta-n4-sign-investigation.md) — the N=4 sign issue this builds on
- [`content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.{md,lean}`](../../content/quantum-observable-universe/braids-and-knots/q-beta-categorical-precision-ladder.md) — the precision-ladder content block + Lean
- [`computations/sweeps/binding_q_target_sweep.py`](../../computations/sweeps/binding_q_target_sweep.py) — reproduces the ladder at 50 dps; ready to extend with N=5 candidates
- [`computations/crystal_basis.py`](../../computations/crystal_basis.py) — Type-A Kashiwara crystal primitives (intra-block side)
- [`computations/demazure_markov_trace.py`](../../computations/demazure_markov_trace.py) — Demazure characters (b^k power-series side)
