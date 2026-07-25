# A_ω one-instanton magnitude probe — zero-crossing yes, magnitude off (2026-07-25)

**Branch:** `claude/aomega-magnitude-probe-2026-07-25`. **Continues:** the one-instanton
normalization map (`OneInstantonNormalization.lean`, PR #4246) + its audit.

> **Correction note.** An earlier version of this audit claimed the one-instanton
> exponential amplitude "matches the committed `A` magnitude to ~2% (0.009 orders),
> parameter-free" and that "the slope gap is the `1/u³` lever." Both were **wrong** and
> are **retracted** after a critical-distance re-check: the "2%" compared the
> one-instanton prefactor to `A′·u³`, a **coincidental** combination, not a clean
> observable; and the `1/u³` lever **cancels** in the slope ratio (`S`-slope ratio =
> `A`-slope ratio), so it does **not** rescue the slope gap. The honest result is below.

## The test

The normalization capstone reduces (PR #4246) to a magnitude question: does the
parameter-free one-instanton form

`N_odd(q) = 𝒜 · e^{−Re 𝔙(q)/(π ℏ)} · sin(Im 𝔙(q)/(π ℏ))`  (`𝒜 = 1`, `P = 1`, `ℏ = log q`)

reproduce the committed `BarOddLadderShape` numerator `A` (`A(q*) = 0`, `A′ ≈ +2.37`,
`|N_odd| ~ |S_swing|·u³ ≈ 2.5×10⁻⁸` at the anchors)? The A3 probe
(`qbeta_5two_sigma3_nodd_shape_probe.py`, #3927) tested the **linear** form
`N_odd ∝ Im(ι₁₃)`: monotone, no zero, slope 0.196. This probe tests the distinct
**exponential-oscillatory** form, reusing the 5₂ complex-CS `𝔙 = V₁ − V₃` machinery.

## Result (witness `qbeta-5two-one-instanton-nodd.witness.json`)

| feature | raw form (A3) | one-instanton (parameter-free) | committed |
|---|---|---|---|
| **zero-crossing near substrate** | **none** (monotone) | **yes**, `q_z ≈ 1.1013` ✅ | zero at `q*` |
| zero *location* | — | `\|q_z − q₀\| ≈ 0.0087` (~10⁶× anchor gap) ❌ | at `q* ≈ q₀` |
| slope at the zero | `0.196` | `1.25×10⁻⁴` → **4.28 orders short** ❌ | `A′ ≈ 2.37` |
| prefactor vs `\|N_odd\|(anchor)` | — | `1.44×10⁻⁶` → **~1.8 orders too large** ❌ | `~2.5×10⁻⁸` |

**The one genuine, parameter-free success:** the `sin(Im𝔙/πℏ)` CS-phase oscillation
**supplies a zero-crossing** — the defining `N_odd` feature that the monotone raw
`Im(ι₁₃)` form structurally could **not** produce. This identifies the one-instanton as
the **structurally necessary ingredient** (the only object in the census that yields a
zero at all).

**But parameter-free it does not reproduce `N_odd` quantitatively:**

- **Slope 4.28 orders short** (`1.25×10⁻⁴` vs `2.37`). The `1/u³` lever **cancels** in
  the `S = A/u³` slope ratio, so it does **not** close this gap — the shortfall is a
  genuine property of the one-instanton numerator, not a lever artifact.
- **Zero mis-located** by `~0.0087` (the committed `q*` sits within `~10⁻⁸` of `q₀`; the
  one-instanton phase-zero is at `1.1013`).
- **Prefactor ~60× too large** near the anchors (`1.44×10⁻⁶` vs `|N_odd| ~ 2.5×10⁻⁸`).

## Scope (STRICT — (a), no fit)

**scope-(a).** The parameter-free one-instanton form is the **structurally necessary**
ingredient (it alone produces the zero-crossing), but is **quantitatively insufficient**:
slope, location, and amplitude are all off by orders. This constrains the closing
prefactor `P(q)` / `ℏ`-scaling — which **must be derived, not tuned** (adjusting `ℏ` or
`P` to hit `q*`/`A′` would be a fit, forbidden). It is **not** an ingredient exclusion
(the one-instanton stays the only zero-producing mechanism) and **not** a refutation of
the Lean structural consistency (`OneInstantonNormalization.lean` — that the product
shape's slope at a simple zero is log-derivative-free — which stands independently).
No `c_k` wired; no AME inversion; `μ` never fixed from QOU data.

## What this leaves

The one-instanton map is confirmed as the **structural source of `N_odd`'s zero**, but
the parameter-free evaluation misses the magnitude on all three axes. The open capstone
(`conj:algebraic-geometric-dilog-equivalence`) now has a sharper shape: **derive** the
prefactor `P(q)` and the correct semiclassical `ℏ`-scaling from the GGM state-integral
normalization (not guess `ℏ = log q`), and check whether the derived form pins `q_z → q*`
and lifts the slope to `A′ ≈ 2.37`. That derivation — the state-integral measure
normalization — is the genuine remaining work; the numbers here say the naive scaling is
insufficient, which is a real constraint on it, honestly reported.
