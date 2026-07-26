# The deuteron's bar-even/bar-odd split IS the H₆ partition-conjugation parity — the categorical derivation of the correction's structure

**Date:** 2026-07-26 · **Branch:** `claude/deuteron-C-categorical-trm-2026-07-26` ·
**Axis:** Δ_λ binding — μ₀ −9% closure, categorical structure of the deuteron correction ·
**Owner steer:** *"push from categorical side"* · **Tier:** two exact categorical identities (30 dps,
against derived caches) + Lean-proved parity backbone (**scope-(a); no fit**; nothing wired).

## 0. The move

#4369 (merged) reduced the deuteron correction to the frame-invariant `C = B/E₀ = 1.1015`, whose
exact form **is** the Δ_λ closure. This note pushes it **through the canonical categorical object** —
the Frobenius-paired Markov trace over the Wedderburn blocks of `H₆(q)`
(`build_markov_trace_assembly_deuteron_chain.py`):

$$\mathrm{tr}_M(\beta_D) = \sum_{\lambda \vdash 6} w_\lambda(q)\,\chi^\lambda_q(\beta_D), \qquad B = m_e\sum_\lambda w_\lambda \chi^\lambda \Delta_\lambda,$$

and **derives the parity structure of the correction** — categorically, and verified against the
committed derived caches.

## 1. Two exact identities (verified to 30 dps)

**I1 — weight conjugation-invariance: `w_λ(q) = w_{λ'}(q)`.** The Ocneanu/Jones Markov weight is
`w_λ = (q−q⁻¹)^{n-1}/∏_{cells}[hook]_q`. Conjugation `λ→λ'` transposes the Young diagram, which
*permutes* the hook multiset, so `∏[hook]_q` — hence `w_λ` — is conjugation-invariant. Verified for
all 11 partitions of 6.

**I2 — character conjugation is the bar involution: `χ^{λ'}(β_D; q) = χ^λ(β_D; q⁻¹)`.** Verified
exactly (ratio `χ^{λ'}(q₀)/χ^λ(q₀⁻¹) = 1.0000000000` for every `λ`) from the committed
`chi-deuteron-free-h6-at-q0` / `at-qinv` 50-dps caches. **Partition conjugation on the character is
literally the bar involution `q ↦ q⁻¹`.**

## 2. The parity map

Combining I1 + I2 with the bar-parity of `(q−q⁻¹)^{n-1}`, the per-block term `T_λ(q) = w_λ(q)χ^λ(q)`
obeys

$$T_\lambda(q^{-1}) = w_\lambda(q^{-1})\,\chi^\lambda(q^{-1}) = (-1)^{n-1} w_\lambda(q)\,\chi^{\lambda'}(q) = (-1)^{n-1} T_{\lambda'}(q).$$

So the bar involution maps the `λ`-block to `±` the `λ'`-block: **conjugate pairs interchange, and the
self-conjugate block sits on the diagonal.** For `n=6` the 11 partitions are **5 conjugate pairs**
`{(6),(1⁶)}, {(5,1),(2,1⁴)}, {(4,2),(2²,1²)}, {(4,1,1),(3,1³)}, {(3,3),(2,2,2)}` **+ the single
self-conjugate `(3,2,1)`**. This is the concrete realisation of the abstract involution `c` in
[`ConjugationParitySplit.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ConjugationParitySplit.lean).

## 3. The key categorical fact (Lean-proved, data-verified)

**The self-conjugate `(3,2,1)` has a bar-even character:** `χ^{(3,2,1)}(q₀) = χ^{(3,2,1)}(q₀⁻¹) =
7.6256` (ratio `1.0`). Being conjugation-fixed and bar-even, its Wedderburn contribution is **purely
bar-even** — it feeds the bar-even coefficient `g₂` and **never** the bar-odd impurity `t`. This is
exactly `barOdd_selfConj_zero` in the Lean brick: for a conjugation-fixed block the bar-odd part
vanishes identically.

So the deuteron correction's **bar-even / bar-odd decomposition is the partition-conjugation parity of
the H₆ Wedderburn sum** — bar-odd `t` lives in the 5 conjugate-pair *asymmetries*, bar-even `g₂` in
their *symmetric* combinations plus the self-conjugate `(3,2,1)`.

## 4. Scope

| statement | status |
|---|---|
| `w_λ(q) = w_{λ'}(q)` (hook conjugation-invariance) | **verified exact** (I1) |
| `χ^{λ'}(β_D; q) = χ^λ(β_D; q⁻¹)` (conjugation = bar) | **verified exact** (I2, all 11) |
| parity map `T_λ(q⁻¹) = (−1)^{n-1} T_{λ'}(q)` | **derived** |
| self-conjugate `(3,2,1)` → bar-even only | **Lean-proved + data-verified** (`barOdd_selfConj_zero`) |
| the Δ_λ per-partition **magnitudes** | **OPEN — Track-A gate** |
| the exact `tr_M → binding` normalization (β_D word / sign convention) | **not addressed here** (the parity structure alone does not reproduce `tr_M = 0.3883` or `C`) |

**Net.** The *parity structure* of the deuteron binding correction is now **derived from the
categorical side** — it is the conjugation parity of the H₆ partition set, with two exact identities
(`w_λ=w_{λ'}`, `χ^{λ'}(q)=χ^λ(q⁻¹)`) and the self-conjugate `(3,2,1)→g₂` fact machine-checked and
data-verified. What remains — and is the honest terminus — is the Δ_λ *magnitude* closure (Track-A
gate) and the `tr_M→binding` normalization. The categorical push settles *why* the correction splits
bar-even ⊕ bar-odd; it does not (and cannot without Δ_λ) settle *how large* each part is.

Refs: probe
[`deuteron_conjugation_parity_categorical_probe.py`](../../computations/deltalambda/deuteron_conjugation_parity_categorical_probe.py);
Lean [`ConjugationParitySplit.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ConjugationParitySplit.lean);
caches `chi-deuteron-free-h6-at-{q0,qinv}-50dps.witness.json`; #4369 (frame-independent `C`);
`build_markov_trace_assembly_deuteron_chain.py`.
