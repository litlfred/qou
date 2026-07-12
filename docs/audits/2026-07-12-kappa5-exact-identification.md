# κ₅ exact: (110011/688905)·√3·π⁵ — the ≥17-digit extraction gate met at 40 digits

**Date:** 2026-07-12 · **Axis:** z→c_k f-map keystone (even channel) · **Tier:**
numerical-exact (targeted leading-residual extraction + budget-gated 2-term PSLQ)
· **Discipline:** no fit to QOU data, no Q_β c_k wired, no tier change.
PR #3683 pickup item 1; follow-up to
[`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md)
(κ₂..κ₄ exact) and the #3683 G2+C3 close-out ("PSLQ gate not met (~2.9-digit
gap) — exact κ₅ still needs bridge arithmetic or ≥17-digit extraction").

## Result

| rung | exact value | parity | confident digits | height / budget |
|---|---|---|---|---|
| κ₅ | **(110011/688905)·√3·π⁵** | odd → √3 ✓ | **40** (gate 17) | 688905 ≪ 1.6·10¹⁸ |
| κ₆ | 676.946678964105031492781861098 | even → π⁶ expected | 33 | **no hit ≤ 5·10¹⁴** |

The κ₅ denominator is **688905 = 3⁹·5·7** — the 3-power-dominated ℚ(√−3)
torsion-3 signature continues exactly (108 = 2²3³, 27 = 3³, 21870 = 2·3⁷·5,
729 = 3⁶, now 3⁹·5·7). The candidate reproduces the 40-digit extraction to
< 10⁻³⁸ (the #3571-class false-positive guard), and the extraction reproduces
the #3628 main-witness κ₅ (14 digits) and κ₆ (10 digits) on the nose.

## Method — why the gap closed by 26 digits, not 3

[`scripts/qbeta_ohtsuki_kappa5_exact.py`](scripts/qbeta_ohtsuki_kappa5_exact.py)
(witness [`qbeta-ohtsuki-kappa5-exact.witness.json`](scripts/qbeta-ohtsuki-kappa5-exact.witness.json);
319 s wall, 13-point ladder to N = 12 582 912, dps 220). Two upgrades over the
κ₂..κ₄ prober:

1. **Exact-rung + amplitude stripping.** κ₁..κ₄ (#3606/#3628 exact) *and* the
   Andersen–Hansen amplitude a₀ = −(1/4)log 3 (ω₀ = 3^{-1/4},
   [andersen-hansen2006]) are subtracted exactly, so κ₅ becomes the **leading**
   1/N-power of the residual and the Vandermonde basis is pure tail
   {1/N⁵, 1/N⁶, …} — the best-conditioned "targeted extraction" geometry that
   gave κ₁ its 36 digits, now aimed at κ₅. A side-fit with a free constant
   column re-verified the a₀ strip in-run (residual constant 3·10⁻⁸²).
2. **Transcendental-free Kashaev ladder.** J_N accumulated as the raw positive
   sum Σ_k ∏_{j≤k}|1−q^j|² by complex-multiplication recurrence — ~7 mpf ring
   ops per step, zero per-step transcendentals (mpf's unbounded exponent
   absorbs the e^{±O(N)} range) — ~20× faster than the log(2 sin) path,
   which is what paid for N_max = 12.6M (2× the #3628 confirm run) in 5 min.
   Self-checked against the reference log-sum-exp evaluator to 10⁻¹⁵⁰ at
   N = 1536.

Confidence is measured, not assumed: min agreement across drop-2-largest-N and
drop-2-smallest-N refits. PSLQ is budget-gated per the PR #1805 rule (2-term,
strict parity generator only, candidate must reproduce the extraction at full
confidence).

## The κ₆ surprise — honest scope-(a) frontier

κ₆ now stands at **33 confident digits** (was 10) with **no** low-height
ℚ·π⁶ element inside the height-5·10¹⁴ entropy budget. This is the first rung
where the parity-predicted single-generator identification *resists at high
precision*. Scope-(a) reading only: κ₆ is not a rational multiple of π⁶ of
height ≤ 5·10¹⁴ — this does **not** exclude (b-style) the parity rule itself;
candidate explanations left open: (i) genuine height explosion at the even
rung following 3⁹·5·7 (the next even denominator may involve 3¹²⁺ with a large
numerator), (ii) the [1/N⁶] observable mixing an additional even-weight
generator not in the single-generator basis. Follow-up: strip exact κ₅ too,
re-extract κ₆/κ₇ (mechanical, same script pattern), and widen the even-rung
basis before concluding anything structural.

## What this feeds (downstream, not wired)

- The #3683 G2+C3 one-instanton large-order test can now be re-anchored on an
  exact κ₅ (its inverse-implied A = 0.65192 used the 14-digit numeric).
- The C2 Borel-transformed ℚ(√−3) PSLQ line at m = 5 — the "trust-limited"
  frontier — has its even-channel counterpart value pinned exactly.
- The Ohtsuki-rung parity ladder (`rem:ohtsuki-tower-bar-parity`) gains a
  fifth confirmed rung; the odd-rung √3 alternation is now confirmed through
  weight 5.

**Anti-laundering:** these are topological facts about the 4₁ Kashaev/Ohtsuki
asymptotic. The 4₁↔Q_β bridge remains the open keystone; NO fit to QOU data,
NO c_k value wired, NO tier change.

## Cross-references

- κ₂..κ₄ exact + parity rule: [`2026-07-12-ohtsuki-higher-rungs-exact.md`](2026-07-12-ohtsuki-higher-rungs-exact.md)
- G2+C3 large-order test (the gap statement): [`2026-07-12-borel-alien-calculus-utilization-audit.md §5`](2026-07-12-borel-alien-calculus-utilization-audit.md)
- Entropy-budget rule: PR #1805; C2 machinery in
  [`computations/probes/qbeta_qsqrt3_borel_pslq_probe.py`](../../computations/probes/qbeta_qsqrt3_borel_pslq_probe.py)
- Full-ladder entropy block (#3571): [`2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md`](2026-07-11-fmap-action-qsqrt3-saddle-entropy-block.md)
