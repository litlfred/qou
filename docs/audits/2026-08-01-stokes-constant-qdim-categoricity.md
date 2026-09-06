# Horn 2 — are the descent-scaffold orbit magnitudes categorical q-dimensions? (algebraic test)

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


**Date:** 2026-08-01 · **Bean:** `qou-nkm1` (epic `qou-r2nh`, horn 2) ·
**Branch:** `claude/stokes-constant-qdim-categoricity-2026-08-01` ·
**Tier:** algebraic / rep-theory (formalize-first, generic `[Field K]` / `Polynomial ℤ`, §7c) ·
**Discipline:** anti-fit; no `c_k`, no `Δ_λ` closure, nothing wired to production.
**Verdict: honest NEGATIVE — the direct "orbit magnitudes = q-dims" identification does not hold.**
The lone `3 = [3]_{q=1}` match is *vacuous* (every integer is a `q=1` quantum
integer), and the actual GGM Stokes *q-series* is structurally excluded from
being a categorical q-dimension (it carries negative coefficients; q-dims do not).

## 0. The question (horn 2 of the descent scaffold)

PR #4525 (`claude/stokes-descent-ward-filtration-scaffold-2026-08-01`,
[`StokesMatrixDescent.lean`](../../content/quantum-observable-universe/lean/QOU/Resurgence/StokesMatrixDescent.lean)
+ [`WardFiltrationCounting.lean`](../../content/quantum-observable-universe/lean/QOU/Resurgence/WardFiltrationCounting.lean))
proved sorry-free that the gauge-invariant Markov trace `tr_M(S)` of the
resurgent Stokes matrix is constant on bar-orbits, so the Ward/filtration count
is **over-determined**: it forces the magnitude pairing `|Δ_λ| = |Δ_{λ'}|` and
**relocates** the residual gap to two categoricity questions — the **sign** (horn 1,
sibling `claude/stokes-phase-sign-delta-lambda-2026-08-01`) and the **magnitudes**
(horn 2, this doc): *are the closed bar-orbit magnitudes categorical q-dimensions?*

The established anchor is the GGM state-integral Stokes datum for the figure-eight
`4₁` ([`qbeta_g3_ggm_stokes_41.py`](../../computations/probes/qbeta_g3_ggm_stokes_41.py),
[`StokesSymmetryConstant.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/StokesSymmetryConstant.lean)):

```
S⁰ = [[1, 0], [−3, 1]],   S⁺(q→0) = [[1, 3], [0, 1]],   integer Stokes constant 3.
```

**The perturbative large-order AMPLITUDE route already FAILED** (PR #4521 `qou-fgte`,
[`2026-08-01-stokes3-largeorder-amplitude-41.md`](2026-08-01-stokes3-largeorder-amplitude-41.md)):
12 real κ_n give `2πP ≈ 1`, not 3 (entropy-limited). This doc runs the **orthogonal
ALGEBRAIC / rep-theory** angle instead, per the bean.

## 1. Corpus state — Stokes spectrum vs q-dimensions (STEP 1)

| object | value(s) | source |
|---|---|---|
| geometric Stokes constant (single integer) | `3` (= `−3` in `S⁰`) | GGM state-integral, exact |
| descendant Stokes **q-series** `S⁺_{σ₁σ₁}(1;q̃)` | `1 − 8q̃ − 9q̃² + 18q̃³ + 46q̃⁴ + 90q̃⁵ + 62q̃⁶ + …` | GGM 2012.00062 eq 21 (proven for 4₁); [`2026-07-31-awpk-perwinding-stokes-41.md`](2026-07-31-awpk-perwinding-stokes-41.md) |
| per-winding integer family `I(0,e)` (e=0 row) | `1, −2, −3, 2, 8, 18, 18, 14, −12, −52, −106, …` | same, exact-int flux-sum engine |
| Markov-trace / Jones normalization | `dim_q = [n]_q`, `[n]_1 = n` | corpus `QIntegerFactorial.lean` (`qInt`), Hoefsmit/Wenzl |

Corpus q-dim infrastructure (reused): `QOU.MathlibExt.qInt q n = ∑_{i<n} qⁱ`
= `[n]_q = (qⁿ−1)/(q−1)`, `[n]_1 = n`
([`QIntegerFactorial.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/QIntegerFactorial.lean));
balanced `[a+b]_q` identity in `QPartitionCombinatorics.lean`; Wenzl semisimplicity
(`[n]_q! ≠ 0`) parameter side. **No prior corpus item claims the Stokes spectrum is a
q-dim spectrum** (grep of `docs/audits/`, `content/`, `computations/`): the descent
audit explicitly leaves this OPEN, relocated to `qou-fgte`.

## 2. The algebraic test (STEP 2) and why the naive match is vacuous

**Candidate identifications and their outcome:**

1. **`3 = [3]_{q=1}`? — TRUE but VACUOUS.** `[n]_q|_{q=1} = ∑_{i<n} 1 = n`, so the
   `q=1` quantum-integer "spectrum" is *all of* `ℕ`. Every integer `k` equals
   `[k]_1` — including `8 = [8]_1`, `46 = [46]_1`. A `q=1` match therefore carries
   **zero information**; it cannot distinguish "categorical" from "coincidence."
   (This is the small-integer trap the bean flags: "a lone 3 is weak evidence.")

2. **The spectrum must match at `q ≠ 1`** to be categorical — i.e. the Stokes
   *q-series* itself must **be** a quantum dimension as an element of `ℤ[q,q⁻¹]`.
   It is not:
   - The geometric constant is the **`q`-independent** integer `3`, whereas
     `[3]_q = 1 + q + q²` is genuinely `q`-dependent. They agree **only at `q=1`**
     (the vacuous point); as polynomials `3 ≠ 1 + q + q²`.
   - The descendant `q`-series `1 − 8q̃ − 9q̃² + …` has **negative coefficients**
     (`−8`, `−9`, GGM-exact). A categorical quantum dimension lies in
     `ℕ[q,q⁻¹]` — non-negative integer Laurent coefficients (it is a sum of
     `q^{weight}` over a crystal / a Markov-trace value; this is the same
     positivity as the PROBE-4 KL-positivity that pruned the *sign*). No such
     object, nor any `ℕ`-combination of them, can have a negative coefficient.

**Structural exclusion (scope-(b), proved invariant).** Any polynomial with
non-negative coefficients — every categorical q-dimension and every `ℕ`-linear
combination of q-dimensions — is unequal to the Stokes descendant series, because
that series has `coeff₁ = −8 < 0`. This is the magnitude analogue of the KL-positivity
sign prune: **positivity of categorical q-dimensions vs a negative Stokes coefficient.**

## 3. Proved / open split

**Proved sorry-free** ([`StokesConstantQDimCategoricity.lean`](../../content/quantum-observable-universe/lean/QOU/Resurgence/StokesConstantQDimCategoricity.lean)):

| Lean decl | content |
|---|---|
| `qInt_at_one` | `[n]_q\|_{q=1} = n` — the `q=1` spectrum is all of `ℕ` (the vacuity engine) |
| `qInt_three` | `[3]_q = 1 + q + q²` (genuinely `q`-dependent, over generic `[Field K]`) |
| `qInt_three_at_one` | `[3]_1 = 3` — the observed match, exhibited as the vacuous `q=1` coincidence |
| `qIntThreePoly_ne_const_three` | `[3]_q ≠ 3` as polynomials — the match fails off `q=1` |
| `qIntPoly_coeff_nonneg` | the q-integer polynomial `∑_{i<n} Xⁱ` has all coefficients `≥ 0` |
| `stokesDesc_coeff_one_neg` | the GGM Stokes descendant series has `coeff₁ = −8 < 0` |
| `stokes_not_nonneg_combination` | **(b) exclusion:** no non-negative-coefficient polynomial equals the Stokes series |
| `stokesDesc_ne_qIntPoly` | in particular the Stokes series is no `[n]_q` |

**Open, honestly represented (content-bearing carrier, NO instance):**
`OrbitMagnitudesAreQDims` — the horn-2 positive hypothesis. It is **not**
instantiated (that would be laundering a refuted identification); the obstruction
theorems above show the direct route to it fails. Left open per anti-fit discipline.

## 4. Verdict (STEP 3 discipline honored)

**HORN 2 → honest NEGATIVE (a full win per the bean).** The bar-orbit magnitude
spectrum of the 4₁ resurgent Stokes data is **not** a categorical q-dimension
spectrum by the direct identification:

- the single `3` matches `[3]_{q=1}` only **vacuously** (`[k]_1 = k` for all `k`);
- across the actual multi-orbit spectrum (descendant tower + per-winding family)
  the Stokes q-series carries **negative** coefficients that q-dimensions
  structurally cannot (scope-(b), positivity invariant proved sorry-free).

**Consequence for the descent scaffold:** the magnitude closure `|Δ_λ| = |Δ_{λ'}|`
that PR #4525 proved is **real**, but it is **not** realized *via* categorical
q-dimensions. The magnitudes are 3d-index / Donaldson–Thomas integers (a distinct
positivity-violating integer structure), not Markov-trace quantum dimensions.
No `c_k`, no `Δ_λ`, nothing wired to production. `A_ω = 3` remains the correct GGM
value; only its *identification as a q-dim* is refuted (and only vacuously matched
at `q=1`).

## Cross-references

- Descent scaffold (horn source): [`2026-08-01-stokes-descent-ward-filtration-counting.md`](2026-08-01-stokes-descent-ward-filtration-counting.md) (PR #4525)
- Failed AMPLITUDE route (do not repeat): [`2026-08-01-stokes3-largeorder-amplitude-41.md`](2026-08-01-stokes3-largeorder-amplitude-41.md) (PR #4521)
- GGM keystone evidence: [`2026-07-18-g3-stokes-keystone-evidence-base.md`](2026-07-18-g3-stokes-keystone-evidence-base.md)
- Per-winding integer family: [`2026-07-31-awpk-perwinding-stokes-41.md`](2026-07-31-awpk-perwinding-stokes-41.md)
- q-integer infra: [`QIntegerFactorial.lean`](../../content/quantum-observable-universe/lean/QOU/MathlibExt/QIntegerFactorial.lean)
- KL-positivity sign prune (parallel positivity argument): [`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md)
