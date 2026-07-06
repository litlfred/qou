# Chain 4 mixed chains — Wenzl × Kashaev × Kashiwara — NEGATIVE

**Date:** 2026-06-04
**PR:** [#1797](https://github.com/litlfred/qou/pull/1797) ([branch](https://github.com/litlfred/qou/tree/claude/qbeta-mixed-chains-2026-06-04))
**Status:** NEGATIVE — diagnostic-only, no closure
**Plan:** [2026-06-04-qbeta-mixed-chains-plan.md](./2026-06-04-qbeta-mixed-chains-plan.md)
**Predecessor:** [PR #1787 — n=5 + Demazure NEGATIVE](./2026-06-04-qbeta-chain4-n5-demazure-verdict.md)

## Target (carried verbatim)

| Quantity | Value |
|---|---|
| Residue A | `1.804e-15` (PR #1727; simple pole, fibre-level, anchor-independent) |
| ℏ_q | `(q − 1)/q ≈ 0.099082` at proton q₀ |
| Target prefactor (proton) | `A / ℏ_q^15 ≈ 2.0717328` |
| Target prefactor (muon) | `A / ℏ_q^15 ≈ 2.0717061` |

## What was probed

Script:
[`computations/qbeta/qbeta_chain4_mixed_wenzl_kashaev_kashiwara.py`](../../computations/qbeta/qbeta_chain4_mixed_wenzl_kashaev_kashiwara.py).
Witness:
[`computations/qbeta/qbeta-chain4-mixed-wenzl-kashaev-kashiwara.witness.json`](../../computations/qbeta/qbeta-chain4-mixed-wenzl-kashaev-kashiwara.witness.json).

**480 mixed candidates** for λ ⊢ n, n ∈ {3, 4, 5}, combining:

```
Wenzl  W_λ ∈ { f^λ            (SYT count / block dim; q-INDEPENDENT),
               qdim(λ)        (fake degree q^{n(λ)}·[n]_q!/∏[h]_q; q-dep),
               wmarkov        (z^{n-1}·qdim, Markov param z=1/(√q+1/√q)) }
Kashaev K_λ ∈ { Li_2^q(z_λ), Phi_q(z_λ), (z_λ;q⁻¹)_∞, Li_2^q(ℏ_q), Phi_q(ℏ_q) }
               with z_λ = q^{-(n(λ)+1)} ∈ (0,1)   (ρ-shifted lowest weight)
Kashiwara    n(λ)            (partition statistic feeding z_λ)
```

Mixed candidate = `W_λ · K_λ`, ratios `W_λ / K_λ`, conjugate-pair Wenzl
products `qdim(λ)·qdim(λ')`, and an `f·qdimᵀ·Φ` form.

**Self-checks (passed):** Σ_λ (f^λ)² = n! for n ∈ {3,4,5}; qdim(λ) → f^λ
as q → 1. (The native `hecke-engine` is not built in this sandbox; the
hook-length closed form is the canonical Wenzl-block q-value.)

## Result — tier histogram (proton anchor)

| Tier | Count |
|---|---:|
| NEAR-1PPM / NEAR-0.1PCT | 0 |
| NEAR-1PCT | 2 |
| NEAR-FUZZY | 7 |
| NEAR-CLOSE | 52 |
| MISS | 419 |

## Verdict — NEGATIVE

**No GENUINE mixed q-product reaches NEAR-1PCT.** A candidate tests the
mixed-chain hypothesis only if its Wenzl factor is **q-dependent**
(`qdim` / `wmarkov`). The best genuine q-mixed candidate is

- `qdim(2,1) / Li_2^q(ℏ_q)` → **NEAR-FUZZY**, ratio 1.0487 (4.87 % off).

All 52 NEAR-CLOSE + 7 NEAR-FUZZY genuine products land ≥ 3 % off target.

### The two NEAR-1PCT hits are Kashaev × integer, not mixed

Both NEAR-1PCT candidates are `f^λ · Li_2^q(ℏ_q)` for shapes (2,1) and
(2,2) — i.e. **`2 · Li_2^q(ℏ_q) ≈ 2.0547`, ratio 0.99177 (0.82 % off)**.
The Wenzl factor `f^λ = 2` is a **q-independent integer block-dimension**;
all q-structure lives in the single-chain Kashaev Rogers-dilog
`Li_2^q(ℏ_q)`. This is:

- **Not a genuine mixed q-product** — there is no Wenzl × Kashaev
  q-interaction; it is a single-chain Kashaev value scaled by an integer.
- **A NEAR-1PCT artifact at 0.82 % off** — directly analogous to the
  `1 + q` q-binomial artifact catalogued in PR #1787 (a low-degree
  q-expression landing ~1 % from a ~2.07 target by combinatorial
  density, not structural alignment). The dilog factor `≈ 1.027` merely
  re-expresses the known "A/ℏ_q^15 ≈ 2.07" prefactor as `2 × 1.03`; it
  does **not** explain the residual 0.82 %.

### Cross-anchor swing is vacuous here (method note)

The proton- and muon-pinned q₀ differ by only **~1e-7** relative, so the
cross-anchor swing is near-zero (0.0013 %) for **every** closed-form
candidate — this is **not** the c_3 FITTED-coefficient swing test (which
detects fitted coefficients absorbing fibre structure across re-pins).
For a probe where every candidate is a closed-form function of q
evaluated at the anchor, swing cannot discriminate categorical from
fibre. The operative discriminators are therefore **(a)** the proximity
tier and **(b)** whether the Wenzl factor is q-dependent. Both say
NEGATIVE.

## Anti-pattern compliance

- ✅ TIERED reporting; no ansatz at NEAR-FUZZY/NEAR-CLOSE/MISS.
- ✅ Cross-anchor wired (both targets in witness); method note records
  why swing is non-discriminating here, instead of over-reading the
  tiny swing as a structural signal.
- ✅ Honest classification: NEAR-1PCT hit demoted to Kashaev×integer
  artifact, not surfaced as a find.
- ✅ ℏ_q from `(q − 1)/q`, never hard-coded.
- ✅ No production wiring; no λ_scale re-framing; no Δ_λ closure.
- ✅ 4-grep corpus check on "residue A" + "mixed chain" + "Kashaev"
  done — no prior closure this PR duplicates.

## Updated search-space narrowing

| Direction | Status |
|---|---|
| n ≤ 5 partition Kashiwara crystal | NEGATIVE (PR #1772, #1787) |
| Demazure chars at ω_j (sl_3/4/5) | NEGATIVE (PR #1787) |
| ℏ_q^N / b^N·ℏ_q^M / Q_β·ε (38) | NEGATIVE (residue-A probe) |
| **Mixed Wenzl × Kashaev × Kashiwara (n ≤ 5)** | **NEGATIVE (this PR)** |
| Higher-rank Demazure (sl_n, n ≥ 6) | UNPROBED |
| n ≥ 6 partitions | UNPROBED (exponential; needs shape priors) |
| Genuinely transcendental / period-style residue | OPEN QUESTION |

## Open questions for the author

1. With all four catalogued families NEGATIVE (single-chain partitions,
   Demazure, ℏ_q/b power-products, and now mixed chains), is residue A
   plausibly **non-algebraic** at proton q₀ — implying the closure path
   needs a different framework (adèlic / period-style) rather than a
   finite categorical invariant?
2. The persistent `≈ 2.07 = 2 × 1.03` near-pattern (here `2·Li_2^q(ℏ_q)`,
   in PR #1787 `1+q`, in the residue-A probe `2·ℏ_q^15·(1+ε)`) keeps
   surfacing at ~1 % from target across unrelated families. Is the "2"
   structural (a doubling / `[2]_q`-like factor) with a separate ~3 %
   correction still to be identified, or is it combinatorial density?
3. Should sl_6 Demazure be probed next as a control, or is the
   higher-rank direction low-yield given no scaling-toward-target signal
   in sl_3/4/5?

## Cross-references

- PR #1727 (merged) — residue A ≈ 1.804e-15, simple pole, fibre-level.
- PR #1772, #1787 (merged) — single-chain Kashiwara NEGATIVE n ≤ 5 + Demazure.
- [1ppQ master ledger](../coordination/1ppq-qbeta.md).
