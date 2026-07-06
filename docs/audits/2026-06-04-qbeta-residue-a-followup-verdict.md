# Residue-A follow-up — combined verdict (sl_6 · residual · period)

**Date:** 2026-06-04
**PR:** [#1804](https://github.com/litlfred/qou/pull/1804) ([branch](https://github.com/litlfred/qou/tree/claude/qbeta-residue-a-followup-2026-06-04))
**Status:** all three directions NEGATIVE / INCONCLUSIVE — diagnostic-only
**Plan:** [2026-06-04-qbeta-residue-a-followup-plan.md](./2026-06-04-qbeta-residue-a-followup-plan.md)
**Predecessor:** [PR #1797 — mixed chains NEGATIVE](./2026-06-04-qbeta-mixed-chains-verdict.md)

Three author-chosen directions, after all four catalogued categorical
residue-A families came back NEGATIVE. Target: A = `1.804e-15`,
prefactor `A/ℏ_q^15 ≈ 2.0717`.

## Direction 1 — sl_6 Demazure control → NEGATIVE

Script:
[`qbeta_residue_followup_sl6_demazure.py`](../../computations/qbeta/qbeta_residue_followup_sl6_demazure.py)
· witness `qbeta-residue-followup-sl6-demazure.witness.json`.

Extended the PR #1787 real-D_i Demazure probe to **sl_6** (720
permutations × ω_1…ω_5 = **3600 candidates**). **0 NEAR-1PCT.** Best is
the *same* `1+q ≈ 2.110` NEAR-FUZZY artifact (168 copies) already
catalogued in PR #1787. Higher rank does **not** scale toward target —
the control closes the higher-rank Demazure door.

| Tier | Count |
|---|---:|
| NEAR-1PCT or better | 0 |
| NEAR-FUZZY | 168 |
| NEAR-CLOSE | 288 |
| MISS | 3144 |

## Direction 2 — the 2×1.03 residual → NEGATIVE

Script:
[`qbeta_residue_followup_residual_2x.py`](../../computations/qbeta/qbeta_residue_followup_residual_2x.py)
· witness `qbeta-residue-followup-residual-2x.witness.json`.

The prefactor factors as `2 × 1.0359` (literal) or `[2]_q × 1.0303`
(quantum). Characterised the residual against a **fixed 18-factor
canonical basket** (no free parameters). **0 closure (NEAR-1PPM) hits.**

The 8 NEAR-1PCT hits **match the basket-density baseline** — with 18
factors over a band of width ≈ 0.05, ~7 are *expected* within 1% by
density alone. So the cluster is combinatorial density, **not** structure
(the `1+q` lesson). The lone sub-0.1% hit `R2 ≈ q^(1/3)` (460 ppm) is
also within density expectation (~0.7 expected sub-0.1%), is **not** a
standard substrate factor, and sits ~460× above the 1ppQ floor — a
flagged near-match, not a closure.

**Conclusion:** the residual ≈ 1.036 is not a finite product of standard
substrate factors at the 1ppQ scale.

## Direction 3 — transcendental / period reframe → INCONCLUSIVE (precision-capped)

Script:
[`qbeta_residue_followup_pslq_periods.py`](../../computations/qbeta/qbeta_residue_followup_pslq_periods.py)
· witness `qbeta-residue-followup-pslq-periods.witness.json`.

PSLQ probe of P and A against a 12-constant period basis (π, π², ζ(3),
Catalan G, ln q₀, Li₂ variants, Bloch-Wigner D(q₀), Vol(4_1),
Vol(Borromean)).

**Critical precision ceiling (the headline finding):** A is empirically
known only to **~12 sig figs** (`A = u_subst · tail_mean`, with
tail_mean = `2.11794472225e-13` the Step-1 PR #1727 limiter). A PSLQ
relation among `k` terms at height `h` is non-spurious only if
`precision > k·log10(2h) + margin`. The full-12-basis height-8 relation
has search entropy ≈ **15 digits ≫ 11-digit precision** → **SPURIOUS**
(a degrees-of-freedom artifact: a relation of that height exists by
chance). No meaningful **2-term** relation `P·c₀ = const·c₁` exists at
low height either.

**Verdict:** the period reframe is **not confirmable at A's current
precision — and cannot be**, since a 12-constant basis needs ≥ ~15
digits to resolve. `BlochWigner(q₀) = 0` (real q₀, non-hyperbolic) is
recorded, consistent with the trefoil/real-q audit note.

**Actionable next step (the real product of Direction 3):** to test the
period reframe properly, **A must be recomputed to ≥ 30 digits** from the
PR #1727 residue compute. `tail_mean` (12 sig figs) is the precision
limiter — refining it is the prerequisite for *any* high-precision
residue-A structural search (PSLQ, period, or otherwise).

## Anti-pattern compliance

- ✅ TIERED reporting; no ansatz/fit at NEAR-FUZZY or coarser.
- ✅ Direction 2 basket is fit-free; NEAR-1PCT cluster explicitly
  attributed to density (with the quantitative baseline), not structure.
- ✅ Direction 3 PSLQ uses an **entropy-based** meaningfulness criterion;
  the height-8 full-basis relation is correctly reported SPURIOUS, not
  surfaced as a find.
- ✅ Cross-anchor wired throughout; method note on its vacuity here
  (anchors ~1e-7 apart).
- ✅ ℏ_q from `(q - 1)/q`, never hard-coded.
- ✅ No production wiring; no λ_scale re-framing; no Δ_λ closure.
- ✅ 4-grep corpus check on "residue A" / "period" / "PSLQ" / "sl_6" —
  no prior closure duplicated.

## Updated search-space narrowing

| Direction | Status |
|---|---|
| single-chain partitions (n ≤ 5) | NEGATIVE (PR #1772, #1787) |
| Demazure ω_j sl_3/4/5 | NEGATIVE (PR #1787) |
| Demazure ω_j **sl_6** | **NEGATIVE (this PR, D1)** |
| ℏ_q^N / b^N·ℏ_q^M / Q_β·ε | NEGATIVE (residue-A probe) |
| mixed Wenzl × Kashaev × Kashiwara | NEGATIVE (PR #1797) |
| **2×1.03 residual vs canonical basket** | **NEGATIVE (this PR, D2)** |
| **period / transcendental (PSLQ)** | **INCONCLUSIVE — precision-capped (this PR, D3)** |
| **higher-precision A (≥30 digits)** | **PREREQUISITE for any further structural search** |

## Bottom line for the author

The categorical-invariant search for residue A is **comprehensively
NEGATIVE** across every algebraic family probed. The period reframe is
the one remaining live hypothesis, but it is **gated on precision**: at
A's empirical ~12 digits, no structural search (categorical or period)
can resolve a closure — the NEAR-1PCT noise floor is set by basket/basis
density, not by the absence of structure. **The highest-leverage next
action is to recompute A to ≥ 30 digits** from the PR #1727 residue
(refining `tail_mean`); only then can Direction 3 (and any future
attack) discriminate structure from coincidence.

## Cross-references

- PR #1727 — residue A simple pole, fibre-level (the `tail_mean` source).
- PR #1772 / #1787 / #1797 — prior NEGATIVE families.
- [1ppQ master ledger](../coordination/1ppq-qbeta.md).
