# The deuteron's bar-even/bar-odd split IS the *signed* H₆ partition-conjugation parity — the categorical derivation (with a corrected sign)

**Date:** 2026-07-26 · **Branch:** `claude/deuteron-C-categorical-trm-2026-07-26` ·
**Axis:** Δ_λ binding — μ₀ −9% closure, categorical structure of the deuteron correction ·
**Owner steer:** *"push from categorical side"* · **Tier:** three exact categorical identities (25 dps,
against derived caches) + Lean-proved signed-parity backbone (**scope-(a); no fit**; nothing wired).

> **⚠ Correction (same day).** An earlier draft of this note dropped the Markov weight's own
> bar-parity `w_λ(q⁻¹) = (−1)^{n-1} w_λ(q)` and therefore assigned the self-conjugate `(3,2,1)` to the
> **wrong channel** (it claimed `(3,2,1) → g₂`). With the sign restored, the physical bar on the
> per-block term carries `(−1)^{n-1}`, which for the deuteron `n = 6` is `−1`. The corrected,
> numerically-verified result is that **`(3,2,1)` is bar-ODD and feeds `t`, never `g₂`.** All artifacts
> (Lean, probe, this note, the content block) are corrected accordingly.

## 0. The move

#4369 (merged) reduced the deuteron correction to the frame-invariant `C = B/E₀ = 1.1015`, whose exact
form **is** the Δ_λ closure. This note pushes it through the canonical categorical object — the
Frobenius-paired Markov trace over the Wedderburn blocks of `H₆(q)`
(`build_markov_trace_assembly_deuteron_chain.py`):

$$\mathrm{tr}_M(\beta_D) = \sum_{\lambda \vdash 6} w_\lambda(q)\,\chi^\lambda_q(\beta_D), \qquad B = m_e\sum_\lambda w_\lambda \chi^\lambda \Delta_\lambda,$$

and **derives the (signed) parity structure of the correction** — verified against the committed
derived caches.

## 1. Three exact facts (verified to 25 dps)

- **I1 — weight conjugation-invariance: `w_λ(q) = w_{λ'}(q)`.** `w_λ = (q−q⁻¹)^{n-1}/∏[hook]_q`;
  conjugation transposes the diagram → permutes the hook multiset → `∏[hook]_q` (hence `w_λ`)
  invariant.
- **I2 — character conjugation is the bar involution: `χ^{λ'}(β_D; q) = χ^λ(β_D; q⁻¹)`.** Verified
  (ratio `1.0` for all 11 partitions) from the `chi-deuteron-free-h6-at-q0` / `at-qinv` caches.
- **I3 — the weight's own bar-sign: `w_λ(q⁻¹) = (−1)^{n-1} w_λ(q)`.** The `[hook]_q` are bar-even but
  the `(q−q⁻¹)^{n-1}` prefactor flips sign for even `n`. **For `n = 6` the sign is `(−1)⁵ = −1`.** This
  is the factor the earlier draft dropped.

## 2. The signed parity map

Combining I1–I3, the per-block term `T_λ(q) = w_λ(q)χ^λ(q)` obeys

$$T_\lambda(q^{-1}) = w_\lambda(q^{-1})\,\chi^\lambda(q^{-1}) = (-1)^{n-1} w_\lambda(q)\,\chi^{\lambda'}(q) = (-1)^{n-1}\,T_{\lambda'}(q).$$

For `n=6`: `T_λ(q⁻¹) = −T_{λ'}(q)` (verified for all 11). Bar maps the `λ`-block to `−` the
`λ'`-block: conjugate pairs interchange **with a sign**, and the self-conjugate sits on the diagonal
**with that sign**. The 11 partitions are 5 conjugate pairs + the single self-conjugate `(3,2,1)`.
This is the concrete realisation of the abstract `barImage sgn c g = sgn · g∘c` in
[`ConjugationParitySplit.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ConjugationParitySplit.lean),
with `sgn = (−1)^{n-1}`.

## 3. The corrected key fact (Lean-proved, data-verified)

**The self-conjugate `(3,2,1)` is bar-ODD:** `T_{(3,2,1)}(q₀⁻¹) = −T_{(3,2,1)}(q₀)` (ratio `−1`,
verified). Because `n=6` gives `sgn = −1` and `(3,2,1)' = (3,2,1)`, its physical bar image is `−`
itself. So its Wedderburn contribution is **purely bar-odd** — it feeds the bar-odd impurity `t` and
**never** the bar-even coefficient `g₂`. This is `selfConj_barEven_zero_deuteron` in the Lean brick
(`pEven (−1) c g p = 0` when `c p = p`).

Consequently the channel assignment is:

- **bar-even `g₂` ← conjugate-pair *asymmetries* `Δ_λ − Δ_{λ'}`** (which vanish on the self-conjugate);
- **bar-odd `t` ← conjugate-pair *symmetric* parts `Δ_λ + Δ_{λ'}` plus the whole self-conjugate `(3,2,1)`.**

The sign is load-bearing: for a hypothetical odd-`n` atom (`sgn = +1`) the roles would swap
(`selfConj_barOdd_zero_oddN`).

## 4. Scope

| statement | status |
|---|---|
| `w_λ(q) = w_{λ'}(q)` (weight conjugation-invariance) | **verified exact** (I1) |
| `χ^{λ'}(β_D; q) = χ^λ(β_D; q⁻¹)` (character conjugation = bar) | **verified exact** (I2, all 11) |
| `w_λ(q⁻¹) = (−1)^{n-1} w_λ(q)` (weight bar-sign) | **verified exact** (I3) |
| signed parity map `T_λ(q⁻¹) = (−1)^{n-1} T_{λ'}(q)` | **derived + verified** |
| self-conjugate `(3,2,1)` → **bar-odd only** (feeds `t`, not `g₂`) | **Lean-proved + data-verified** (`selfConj_barEven_zero_deuteron`) |
| the Δ_λ per-partition **magnitudes** | **OPEN — Track-A gate** |
| the exact `tr_M → binding` normalization | **not addressed here** |

**Net.** The *signed parity structure* of the deuteron binding correction is derived from the
categorical side: it is the conjugation parity of the H₆ partition set **dressed by the weight sign
`(−1)^{n-1}`**, with `g₂` living in the conjugate-pair *asymmetries* and `t` in the symmetric parts
plus the self-conjugate `(3,2,1)`. Two identities (`w_λ=w_{λ'}`, `χ^{λ'}(q)=χ^λ(q⁻¹)`), the weight
bar-sign, and the corrected self-conjugate→`t` fact are machine-checked and data-verified. What remains
— the honest terminus — is the Δ_λ *magnitude* closure (Track-A gate) and the `tr_M→binding`
normalization.

Refs: probe
[`deuteron_conjugation_parity_categorical_probe.py`](../../computations/deltalambda/deuteron_conjugation_parity_categorical_probe.py);
Lean [`ConjugationParitySplit.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/ConjugationParitySplit.lean);
caches `chi-deuteron-free-h6-at-{q0,qinv}-50dps.witness.json`; #4369 (frame-independent `C`);
`build_markov_trace_assembly_deuteron_chain.py`.
