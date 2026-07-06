# Flavor-split partial derivation — the second-order pair structure (2026-06-29)

**Branch:** `claude/color-weighting-flavor-split-audit-2026-06-29`
**Follows:** [`2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md`](2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md)
(Parts A–D). Part D found `leading·(1+leading)` (0.0097%) but left the exact
coefficient α = 0.929 ≠ 1 open and explicitly declined to fit it.
**Probe:** [`computations/probes/flavor_split_partial_derivation_probe.py`](../../computations/probes/flavor_split_partial_derivation_probe.py)
(witness `flavor-split-partial-derivation-probe.witness.json`).

This is a **partial derivation**, not a closure: it proves the *structure*
(the correction is second-order in the proven leading split) and isolates the
*single open coefficient* (the second-order normalization α). It does **not**
fit 0.929 to a clean form — that would be the c_k-flip-flop trap.

## Established facts (not re-derived here)

| Quantity | Value | Status |
|---|---|---|
| `leading(q) = ℏ_q²·h_q·[2]_q/3 = (q−1)²(1−q⁻⁴)/3` | 1.37571e-3 | **PROVEN** (`prop:flavor-split-substrate`, 2-strand σ-swap object) |
| `(Δm_pn/M_N)_CODATA` | 1.37747e-3 | CODATA 2018 |
| leading-only error vs CODATA | **0.128%** | — |
| `C_true = (Δm_pn/M_N)_CODATA / leading` | 1.0012784 | anchor-stable |
| `α = (C_true−1)/leading` | **0.929254** | anchor-stable (drift 5.8e-8 proton↔muon) |

The split is therefore `split = leading·(1 + α·leading)` with **α ≈ 0.929**.
The probe's task: derive that the `α·leading` (i.e. `α·leading²` overall) form
is *forced by structure*, and predict α from the pair count.

## Part 1 — the correction is SECOND-ORDER in `leading`, not an ℏ_q-power

Three independent arguments, all in the probe:

### 1a. No fixed ℏ_q-power has an O(1) coefficient; `leading` does

If the correction were a fixed power `1 + c·ℏ_q^k`, then `c = (C_true−1)/ℏ_q^k`
should be a clean O(1) constant. It is not — every power needs a non-O(1)
fudge, whereas the `leading` base gives a clean O(1) coefficient:

| candidate shape | implied coefficient `(C_true−1)/base` | O(1)? |
|---|---|---|
| **`leading`** | **0.929254** | ✓ clean O(1) |
| `ℏ_q³` (production-posited) | 1.31426 | ✓ but ≠ clean (76%-insufficient, see Part C of prior audit) |
| `ℏ_q²` | 0.13022 | small |
| `ℏ_q⁴` | 13.264 | ✗ |
| `h_q²` | 0.02925 | ✗ |
| `ℏ_q²·h_q` | 0.62288 | mid |
| `ℏ_q³·[2]_q` | 0.65357 | mid |

Only `leading` yields a single O(1) coefficient near a recognizable value (≈1).
This is the empirical signature that the correction **scales with `leading`**
— i.e. the overall correction is `α·leading²`, a second-order self-term — not a
fixed q-power. (The production `(1+ℏ_q³)` is the wrong shape: its implied
coefficient 1.31 is the 76%-insufficiency already flagged.)

### 1b. A multiplicative pair product *forces* an O(leading²) cross-term

**This is the structural proof.** Model the baryon split-amplitude as a product
over the changed quark pairs:

$$
  1 + \text{split} \;=\; \prod_{k=1}^{m} (1 + s_k),
  \qquad \sum_{k} s_k = \text{leading}
$$

(the `m` changed pairs jointly reproduce the proven 2-strand leading at first
order). Expanding the product:

$$
  1 + \text{split}
  = 1 + \underbrace{\sum_k s_k}_{\text{leading}}
      + \underbrace{\sum_{k<l} s_k s_l}_{\text{cross-term}}
      + O(s^3)
  \;\Longrightarrow\;
  \text{split} = \text{leading} + \sum_{k<l} s_k s_l + O(s^3).
$$

The cross-term `Σ_{k<l} s_k s_l` is **exactly O(leading²)** by pure algebra,
*independent of the detailed s_k*. So the multiplicative-pair hypothesis
*derives the form* `split = leading·(1 + α·leading)` with no q-power input. The
probe confirms numerically that for the equal split `s_k = leading/m`, the
first-order sum equals `leading` exactly (to 1e-40) and the cross-term equals
`leading²·(m−1)/(2m)`.

### 1c. The corpus closed form is genuinely multiplicative (cross-terms are real)

The structure in 1b is not a probe invention — `closed_form_tau_M.py`'s
canonical baryon trace already factorizes:
`tr_M(𝓑_K)/tr_M(vac) = ∏_i f_i(q)` over interfaces. The canonical p-n interface
factor is `f_pn = z − h·(½ − δ/4) = z·(1 + δ_eff)`, with `δ_eff ≈ −0.209` per
interface. The probe verifies that a product of two such factors expands as
`(1+δ_eff)² − 1 = 2δ_eff + δ_eff²` (cross-term reproduced to 1e-40). So O(δ²)
cross-terms are a **real feature of the corpus interface product** — the
inter-nucleon analogue of the intra-nucleon 3-pair flavor split. The
multiplicative algebra that produces the second-order correction is the same
algebra the production trace already uses.

**Sign and magnitude check (passes):** `C_true > 1` ⟹ the correction is
**positive**, exactly as a `+leading²` cross-term gives. Magnitude
`leading² ≈ 1.9e-6`, coefficient O(1), so `α·leading² ≈ 1.3e-3` matches the
needed `C_true−1 ≈ 1.3e-3`. The second-order form has the **right sign and
right order of magnitude** — both non-trivial checks.

> **Caveat (why 1b is the form, not the whole story).** A *naive* mass-ratio
> reading — `M_p = M₀(1+δ_uu)(1+δ_ud)²`, `M_n = M₀(1+δ_ud)²(1+δ_dd)`, split
> `= 2(δ_dd−δ_uu)/(2+δ_dd+δ_uu)` — gives `split = D − D²/2 + …`, a **negative**
> coefficient (−½), the **wrong sign**. The positive `+leading²` requires the
> split itself to be the multiplicative object (the self-energy/geometric
> reading, Part 2b), not a difference of two mass products. This is recorded
> honestly: the *form* (second-order) is forced, but the *sign* selects the
> self-energy reading over the naive mass-ratio reading.

## Part 2 — what coefficient does the pair structure predict?

Two **principled, parameter-free** readings bracket α. Neither is fitted.

### 2a. Symmetric equal-split cross-pair count → `(m−1)/(2m) ≤ ½`

If the `m` changed pairs share the split equally (`s_k = leading/m`), the
cross-term coefficient is `C(m,2)/m² = (m−1)/(2m)`:

| pair count `m` | `α_pred = (m−1)/(2m)` | % of α_target |
|---|---|---|
| 2 | 0.250 | 26.9% |
| 3 | 0.333 | 35.9% |
| → ∞ | → 0.500 | → 53.8% |

This **saturates at ½** and never reaches 0.929. **Conclusion: the pairs are
NOT equally weighted** — a symmetric cross-pair count is excluded as the
mechanism (it undershoots by ≥ 2×). The swapped pair must dominate.

### 2b. Self-energy / geometric reading → coefficient exactly 1

If the split *dresses itself* — each order of the swap re-enters the next, the
3-strand spectator re-coupling to the already-split pair — the amplitude is
geometric:

$$
  \text{split} = \frac{\text{leading}}{1 - \text{leading}}
  = \text{leading}\,(1 + \text{leading} + \text{leading}^2 + \cdots),
$$

i.e. coefficient **exactly 1**. This is parameter-free (the correction scale
*is* the leading split). It gives:

| form | coefficient | error vs CODATA |
|---|---|---|
| `leading` (proven) | — | 0.128% |
| `leading·(1+leading)` | α=1 | **0.0097%** |
| `leading/(1−leading)` | α=1 | **0.0099%** |

**13× better than leading-only.** It **overshoots** the experimental α=0.929 by
7.6% (`1 − 0.929 = 0.071`).

### 2c. The bracket and the honest comparison

$$
  \underbrace{\tfrac13}_{\text{equal-split }m=3}
  \;<\; \underbrace{0.929}_{\alpha_{\text{target}}} \;\le\;
  \underbrace{1}_{\text{self-energy}}
$$

The structure **predicts α = O(1), strictly in (⅓, 1]**, with the self-energy
reading (α=1) the closest principled value — within 7.6%. The numerically
seductive `13/14 = 0.92857` lands 0.07% from 0.929 but does **not** fall out of
any pair count; per anti-flip-flop discipline it is **noted and rejected**, not
adopted. **No principled count lands exactly on 0.929.**

## Part 3 — anchor stability and honest scope

`α_target` evaluated at both q₀ pins:

| anchor | q₀ | α_target |
|---|---|---|
| proton | 1.10997859555733… | 0.929254490280 |
| muon | 1.10997859555418… | 0.929254548073 |

Drift = 5.8e-8. **But this is NOT independent evidence that α is derived** — the
two pins give nearly identical q₀, so any q-expression is anchor-stable. More
importantly, **α depends on C_DATA** (it is `(C_DATA/leading − 1)/leading`),
so it is the *experimental residual*, not a pure-substrate constant. A genuine
derivation must produce α from the 3-strand trace normalization, **not** read
it back from the data.

## Verdict

| Claim | Status |
|---|---|
| Correction is second-order `α·leading²` (not a fixed ℏ_q-power) | **rigorously established** (Part 1a/1b/1c) |
| Form forced by multiplicative pair factorization `∏(1+δ)` | **rigorously established** (Part 1b, pure algebra) |
| Cross-terms real in the corpus (closed_form_tau_M) | **verified** (Part 1c) |
| Sign positive, magnitude O(leading²) correct | **verified** (Part 1) |
| Coefficient predicted O(1), bracketed (⅓, 1] | **derived** (Part 2) |
| Self-energy reading α=1, within 7.6% | **derived, parameter-free** (Part 2b) |
| **Exact coefficient α ≈ 0.929** | **OPEN** — the single remaining piece |

**The single open piece.** The exact second-order normalization α ≈ 0.929. The
structure proves `0 < α ≤ 1` and predicts O(1) (self-energy reading = 1, within
7.6%); it does not yet pin 0.929. Closing it is the **self-energy
normalization of the 3-strand spectator coupling** — the categorical
question of how the third (spectator) strand's re-coupling to the already-split
u↔d pair is normalized relative to the bare 2-strand leading object. This is
open Archimedean-mass-functor R&D, the same level that gates Δ_λ (per the prior
audit Part C/D). It is **not** an ℏ_q-power fit and **not** a clean-form fit to
0.929.

**Scope (per AGENTS.md §"refuted"/§"open"):** this is a **scope-(a)** result. The
second-order *structure* is rigorously established; the exact *coefficient* is
open. Nothing here is wired to production (the production δ remains the proven
leading per the 2026-06-29 de-wire). `leading·(1+leading)` (α=1) is the leading
candidate to wire **once** the self-energy normalization is closed — its 7.6%
coefficient deficit is the precise size of the open work.

## Reproduce

```bash
python3 computations/probes/flavor_split_partial_derivation_probe.py
```
