# Covariance-kernel epic (`qou-x631`) — synthesis map

**Date:** 2026-07-25 · **Branch:** `claude/covariance-kernel-synthesis-2026-07-25` · **Tier:**
epic-level consolidation (durable handoff) · **Discipline:** scope-(a); no fit; nothing wired; no
`c_k`; L2 unchanged (2/7). **Epic:** `qou-x631`; attack plan `qou-v8t7`.

This is the single durable map of the covariance-kernel epic: the conjecture, why it matters, every
route attacked (with verdicts), the current sharpest form, and the honest open frontier. It supersedes
scattered per-route status notes as the entry point; the individual audits remain the detailed record.

## 1. The conjecture and why it is load-bearing

The **covariance kernel** is

> `cov(k) = Σ_{λ⊢k} (f^λ)³ · ω₃(λ) ≤ 0`,   `ω₃(λ) = Σ_□ c(□)² − C(k,2)`,

equivalently `Cov_Planch(f^λ, Σ_□ c²) ≤ 0` (Plancherel covariance of the dimension and the content
spread). It is the **sole open input** of the Δ_λ growth chain (the per-isotope binding-energy
closure), so proving it discharges that chain's remaining gap. Numerically `cov(k) < 0` for all `k`
tested (exact base values `k=3..7`: `−4, −16, −320, −10400, −163520`). It is an open **§3b conjecture**
— everything below is a *sharpening* or *route-elimination*, never a claimed proof.

## 2. Equivalent forms (the object seen from several angles)

- **Character form:** `ω₃ = dim λ · χ^λ(σ₃) · 3/(k(k−1)(k−2))`; `ω₃` is the degree-3 shifted-symmetric
  3-cycle central character (Ivanov–Olshanski), Plancherel-mean 0.
- **Content/hook form:** via the classical identity `Σ_□ h² = Σ_□ c² + k²`, `ω₃ = Σ_□ h² − k² − C(k,2)`
  — an affine function of the second hook moment.
- **Dimension-tilt form:** `cov(k) = k! · Cov_Planch(dim, ω₃)` — the kernel is the first-order response
  to *one extra* `dim` factor beyond the `dim²`-weighted average (§4).
- **Maya / DPP form:** with occupations `m_a = 1_{a∈{λ_i−i}}`, both `N_v` (hook-length counts) and `ω₃`
  are **quadratic** in `m` (§6), so `cov` is a quadratic-statistic covariance of a determinantal
  process.

## 3. The unifying obstruction — the dim²→dim³ threshold

Weight `ω₃` by `(dim λ)^t` under the counting (un-normalized Plancherel) sum:

| `t` | `Σ_λ (dim)^t ω₃` | status |
|---|---|---|
| `2` | `0` **exactly** | CLOSED — Plancherel expectation of a positive-degree shifted-symmetric function (IO Prop 5.1) |
| `3` | `= cov(k) ≠ 0` | **non-holonomic** — one extra `dim = χ^λ(e)`, *not* a shifted-symmetric diagram functional |

Every elementary framework handles the `dim²`-weighted shifted-symmetric average but is **blind to the
extra `dim`**. This is the single reason the problem is hard, and it is why so many routes die the same
death: they need a **dimension-functional expansion** (`dim` or `ln dim`) against Plancherel — the one
tool outside the character / shifted-symmetric / genus machinery.

## 4. Routes attacked — verdicts

**Full-route eliminations (each an honest scope-(a) negative — "this route cannot deliver the sign",
not "the kernel is false"):**

| # | Route | Verdict / why it dies |
|---|---|---|
| 1 | Holonomic / P-recursive `cov(k)` | non-holonomic; OEIS-absent |
| 2 | β-ensemble monotonicity (`E_β[C₂]`) | not monotone in β |
| 3 | Sub-family truncation | truncation flips sign |
| 4 | Murnaghan–Nakayama peeling | no sign-definite recursion |
| 5 | Closed form for `T₃`/envelope | none exists (agent-confirmed; even `Σ dim³` has no closed form) |
| 6 | FKG on dominance order | fails at `k=8` (ω₃ not monotone on dominance) |
| 7 | Chebyshev / comonotone | ~77 % only; not a certificate |
| 8 | Per-edge Dirichlet form | no per-edge sign |
| 9 | NQD / Hoeffding kernel | kernel not sign-definite |
| 10 | Complete monotonicity / Bernstein | signature holds but genuine CM **refuted** (Hankel/Stieltjes PSD test) |
| 11 | Śniady genus expansion | `dim ∉ A` (algebra of polynomial diagram functions); no genus/leading term |
| 12 | Exact `T₃` evaluation (shifted-symmetric) | the extra `dim` is non-shifted-symmetric → non-holonomic |

**Sub-certificate eliminations within the leading (A2) leg (§5):** ν single-signed-crossing (FALSE
∀`n≥6`); cumulative `S_v ≤ 0` (counterexample `n=6`); `R` nonnegative coefficients (counterexample
`n=6`); `K` (hook-count covariance matrix) M-matrix structure (mixed off-diagonal signs); linear-
response (Gaussian) depoissonization (recovers only 5–8/8 signs).

## 5. The A2 leg — pointwise reduction ELIMINATED with an exact counterexample

The leading term A2 = `Cov_Planch(ln f^λ, ω₃) ≤ 0`. With `ν_v = Cov_Planch(N_v, ω₃)` and
`P(x) = Σ_v ν_v x^v`: `Cov(H_s, ω₃) = P(e^{−s})`, `P(0)=P(1)=0`, so `P(x) = x(x−1)·R(x)` and (since
`x(x−1)<0` on `(0,1)`) the *sufficient* condition **A2 ⟸ `R(x) ≥ 0` on `(0,1)`** (⟺ pointwise
`Cov(H_s,ω₃) ≤ 0 ∀s`).

> **⛔ This pointwise target is FALSE for `n ≥ 29`** (exact; first failure `n=29`,
> `max_s Cov(H_s,ω₃)=+0.056`; `R` gains a root in `(0,1)` at `n=30`; grows with `n`). It was verified
> only to `n ≤ 13/15` — a small-`n` artifact. So the polynomial-positivity / pointwise route **cannot**
> prove A2 (the implication is valid but the premise is false). Correction:
> [`2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md`](2026-07-25-covariance-kernel-A2-pointwise-reduction-falsified.md).

**A2 and the kernel themselves SURVIVE** (verified exactly, `k,n ≤ 40`): `A2 = −Σ_v ln(v) ν_v ≤ 0`
holds by **cancellation** in the full Frullani integral `∫(1/s)Cov(H_s,ω₃)ds` even though the
integrand goes positive. The three easy-proof sub-certificate eliminations of #4242 (ν
single-crossing, cumulative `S_v≤0`, `R` nonneg-coefficients) remain correct — early symptoms that no
pointwise certificate exists. **A proof of A2 must be global** (the full signed integral / a
dimension-functional expansion), not pointwise.

## 6. The identified tool — determinantal (DPP), and its obstruction

Encode `λ` by its Maya diagram. Exactly (`n ≤ 10`): `N_v = Σ_a (1−m_a) m_{a+v}` (hook = particle–hole
distance) and `ω₃ = Σ_v v² N_v − n² − C(n,2)` — **both quadratic** in the occupations. Under
θ-poissonized Plancherel the occupations are a determinantal point process (discrete-Bessel kernel,
Borodin–Okounkov–Olshanski `math/9905032`), so `Cov(N_v, N_w)` reduces by Wick to kernel contractions.

**Obstruction:** the kernel condition `Σ_v ν_v = 0` holds at fixed `n` because `Σ_v N_v = n` is
constant; at poissonized level `|λ|` fluctuates and *dominates* — `Cov_θ(N_v, Σh²)` is all-positive.
So the DPP kernel must be **depoissonized** (conditioned on `|λ| = n`), and this conditioning is
**non-perturbative** (linear response fails). The route therefore needs the fixed-`n`
discrete-orthogonal-polynomial (Hahn/Charlier-type) kernel and steepest descent; the realistic payoff
is a *large-`n` asymptotic* sign, not a finite-`n` proof. Detail:
[`2026-07-25-covariance-kernel-A1b-dpp-maya-representation.md`](2026-07-25-covariance-kernel-A1b-dpp-maya-representation.md).

## 7. Honest open frontier

- **The proof must be global, not pointwise.** §5's correction shows no pointwise `R`-positivity /
  `Cov(H_s,ω₃)≤0` certificate exists (`R` has a root in `(0,1)` for `n≥29`). A proof of A2 must use the
  full signed Frullani integral (cancellation) or a dimension-functional expansion — not a term-by-term
  sign.
- **Asymptotic sign:** depoissonize the discrete-Bessel kernel (fixed-`n` DOP + steepest descent) for a
  large-`n` sign of `Cov(N_v, ω₃)`. Non-perturbative in the `|λ|`-conditioning.
- **Not excluded, not proved:** the kernel `cov(k) ≤ 0` and the A2 leg `Cov(ln f,ω₃) ≤ 0` both hold
  exactly for all `k,n ≤ 40` and remain well-characterized open §3b conjectures. Nothing here is a
  `(b)`-scope structural exclusion of the *kernel*; the one exact refutation is scoped to the *pointwise
  route* (a method, not the claim) — all other negatives are scope-(a) "this route cannot deliver".

## 8. Lean state

[`YoungDiagramKernel.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/YoungDiagramKernel.lean)
carries the elementary carrier sorry-free except the open `covariance_kernel_conjecture`: the kernel is
`decide`-verified for `3 ≤ k ≤ 7`, the `dim²`-vanishing (`secondMomentKernel_eq_zero_of_le_seven`) is
encoded, and the conjugation symmetry of `ω₃` is proved for `k ≤ 6`.

## 9. Provenance (per-route detail)

- A2 polynomial positivity: `2026-07-25-covariance-kernel-A2-polynomial-positivity.md`
- A2 hook/Frullani reduction: `2026-07-25-covariance-kernel-A2-hook-reduction.md`
- A1/A5 dim²→dim³ threshold: `2026-07-25-covariance-kernel-A1-eliminated-dim-threshold.md`
- A5 genus eliminated + A4 Lean: `2026-07-25-covariance-kernel-A5-genus-eliminated-A4-lean.md`
- A3 complete-monotonicity refuted: `2026-07-25-covariance-kernel-complete-monotonicity-target.md`
- DPP Maya representation + obstruction: `2026-07-25-covariance-kernel-A1b-dpp-maya-representation.md`
- Beans: epic `qou-x631`, plan `qou-v8t7`; `qou-ogrk` (A2), `qou-g0n2` (DPP), `qou-4wl1` (A3),
  `qou-q8g5` (A4), `qou-4hq0` (A1), `qou-9clc` (A5), `qou-mdbh` (full-kernel), `qou-9rbo` (this map).
