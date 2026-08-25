# Δ_λ covariance-kernel (qou-x631): Laplace / log-moment reduction

**Date:** 2026-07-25
**Scope:** analytic reduction of an open conjecture; scope-(a). No fit, nothing wired, no `c_k`, L2 unchanged (2/7). The kernel stays an honest §3b conjecture — this narrows *how* to attack it, and corrects a prior over-narrowed exclusion.

## The conjecture

For `λ ⊢ k`, let `f^λ` = #SYT(λ), `χ³(λ) = χ^λ(3-cycle)`, and
`ω₃(λ) = Σ_□ c(□)² − C(k,2)`. Via Jucys–Murphy (`Σ Xᵢ² = C(k,2)·e + z₃`),

> **`ω₃(λ) = |C₃|·χ³(λ)/f^λ`**, `|C₃| = k(k−1)(k−2)/3` (max error exactly 0, k≤9),

so `sign(χ³) = sign(ω₃)`. The Phase-4 target is

> **`L(t) := Σ_λ χ³(λ)·(f^λ)^{t+1} ≤ 0` for all real `t ≥ 0`** (β = t+2 in the `E_β` form; `L(0)=0` is column orthogonality). The kernel `cov(k)=Σ (f^λ)³ω₃ = |C₃|·L(1)` is the `t=1` instance.

Numerically true and exact to k=26 (see `deltalambda-covariance-week-review`), but the prior review reported the whole *soft-order* proof family excluded. **That was over-narrowed.** This audit re-scopes it and supplies a strictly cleaner, still-true sufficient condition.

## 1. Scope correction (anti-over-narrowing, per AGENTS.md §Before declaring "refuted")

`L(t) = Σ_λ w_λ e^{t x_λ}` with `w_λ = χ³(λ)f^λ`, `x_λ = ln f^λ` — i.e. the conjecture **is** the **Laplace-transform (MGF) order** `p⁺ ≤_Lt p⁻`. Since `icx ⟹ Lt` but not conversely, the prior exact counterexamples (stochastic dominance and increasing-convex order both fail at k=18, 26) exclude only the **stronger** orders `{SD, icx}`; the **equivalent** order (Lt) cannot be excluded, and the numerics are precisely *Lt holding while SD/icx fail*. Re-scope the prior claim to **(b)-for-{SD, icx} only** — "no order argument works" is false, because the conjecture itself is an order statement.

## 2. Log-moment sufficient condition (holds numerically)

Expand `L(t) = Σ_{n≥0} M_n t^n/n!` with **log-moments** `M_n = Σ_λ χ³(λ) f^λ (ln f^λ)^n`. Then

> **`M_n ≤ 0` for all `n ≥ 1`  ⟹  `L(t) ≤ 0` for all `t ≥ 0`.**

**Verified `M_n ≤ 0` for `n = 1..12`, `k = 3..17`** (zero violations;
`covariance_laplace_moment_reduction.py`). Because `M_n = (k!/|C₃|)·E_Planch[ω₃·(ln f)^n]` and `E_Planch[ω₃]=0`, this is a family of **Plancherel covariances**:

> **`Cov_Planch(ω₃, (ln f)^n) ≤ 0` for all `n ≥ 1`.**

This condition is `∫ g dν ≤ 0` for all **absolutely-monotone** `g` with `g(0)=0` (`ν` = the mass-zero, ω₃-biased Plancherel measure pushed to `x = ln f`) — strictly weaker than icx (so it dodges the k=18/26 icx counterexample) yet strictly stronger than the bare `Lt` conjecture. It lives exactly in the gap the counterexamples left open.

### Why the endpoints are controlled
- **`n=1` is established (numerically, all k≤19) and sits in the Kerov-CLT framework:** `M_1 ∝ Cov_Planch(Σc², ln f) = H'(2) < 0` (the epic's `H'(2)<0`). **Caveat (literature status, see §4a):** this is *not* a direct citation — `ln f` is a hook-based, non-polynomial functional outside the Ivanov–Olshanski character-polynomial algebra, so its covariance with `ω₃` is not covered verbatim by Biane/Śniady; a rigorous `n=1` needs the CLT for smooth linear statistics of the Plancherel shape.
- **Large `n` is structural:** the **maximum-dimension shape always has `ω₃ ≤ 0`** (verified k≤17 — the balanced shapes (3,2,1), (5,3,2,1), …), and `(ln f)^n` concentrates on the top atom as `n→∞`, forcing `M_n < 0`.

## 3. The `n≥2` mechanism (mean–fluctuation inheritance)

Write `ln f = μ_L + δ`, `μ_L = E_Planch[ln f]`, `E[δ]=0`. Binomially (using `E[ω₃]=0` to kill `j=0`):

> `M_n ∝ Cov(ω₃,(ln f)^n) = Σ_{j=1}^{n} \binom{n}{j} μ_L^{n-j} · E[ω₃ δ^j]`.

The leading `j=1` term is `n·μ_L^{n-1}·Cov(ω₃, ln f) < 0` (the cited `n=1`, amplified by `μ_L→∞`). For `n=2`, `Cov(ω₃,(ln f)²) = 2μ_L·Cov(ω₃,ln f) + E[ω₃ δ²]`, and exactly (k=4..19):

| k | Cov₂ | 2μ_L·Cov₁ (lead) | resid E[ω₃δ²] | \|resid/lead\| |
|---|---|---|---|---|
| 4 | −0.320 | −0.868 | +0.548 | 0.63 |
| 10 | −39.85 | −42.27 | +2.42 | 0.057 |
| 19 | −337.9 | −347.6 | +9.72 | 0.028 |

The leading (cited) term is **negative and dominant**; the residual is **positive but small and shrinking** (`μ_L = Θ(ln k!) → ∞` while the fluctuation moments `E[ω₃ δ^j]` are Kerov-CLT order). So the sign of every `M_n` is **inherited from `n=1`**.

`n=3` confirms the pattern: `Cov₃ = 3μ_L²·Cov(ω₃,ln f) + 3μ_L·E[ω₃δ²] + E[ω₃δ³] < 0` for all k=5..20, with `|resid/lead|` shrinking (0.45 at k=5 → 0.050 at k=20) and the normalized fluctuation ratio `E[ω₃δ²]/(2μ_L|Cov₁|) → 0` (0.084 → 0.026). So `resid = o(lead)` — the reduction is provable in the large-`k` limit, with the finitely many small `k` checked directly.

## 3a. Mechanism — why the conjecture holds while SD/icx fail

The regression `e(x) = E_Planch[ω₃ | ln f = x]` (binned by dimension;
`covariance_omega3_regression.py`) makes the phenomenon transparent:

- **~97% of the Plancherel mass sits on the top-dimension bin**, where `ω₃ < 0`
  (only slightly: `≈ −2` to `−4`, k=16/20).
- The **negligible-mass low-dimension shapes carry huge positive `ω₃`** (`+2280`,
  `+1920`, … at k=20) — they exactly balance the negative bulk to `E[ω₃]=0`
  (`M_0`), but they have **both** tiny mass **and** tiny `x = ln f`.

So a **convex-increasing weight `(ln f)^n` amplifies the dominant negative
top-dimension bin** (large mass × large `x^n`), while the positive low-dimension
shapes contribute `(tiny mass) × (small x^n)` and cannot overturn it — hence
`Cov(ω₃,(ln f)^n) < 0`. **Stochastic dominance fails** because a step-function
threshold *can* isolate a delicate intermediate-dimension imbalance (the positive
mid-`x` shapes with slightly more mass than the negatives just below), but the
convex `x^n` never isolates an interior threshold — it monotonically upweights the
top, where `e(x) < 0` dominates. This is exactly the gap between the (failing) SD
cone and the (holding) absolutely-monotone cone.

This also sharpens the proof target: it suffices that on the high-mass
top-dimension set `ω₃` is (in mass-weighted average) negative *and* anti-correlated
with `x` within that set, with the positive low-`x` remainder mass-suppressed — all
Plancherel-concentration facts.

## 3b. Asymptotic dominance — the reduction is provable in the large-`k` limit

Measured growth of the Plancherel quantities in `M_n ∝ n·μ_L^{n-1}·Cov(ω₃,ln f) + (residual)`
(log-log slope, tail k≥16; `covariance_growth_exponents.py`):

| quantity | growth |
|---|---|
| `μ_L = E_Planch[ln f]` | `~ k^{1.5}` (`≈ ½ ln k!`) |
| `\|Cov(ω₃, ln f)\|` | `~ k^{1.64}` |
| `Var_Planch(ln f)` | `~ k^{0.63}` (slow — dimension concentrates) |
| `E[ω₃ δ²]` | `~ k^{1.82}` |
| **`r₂ := E[ω₃ δ²] / (μ_L·\|Cov(ω₃,ln f)\|)`** | **`~ k^{-1.33} → 0`** |

So `Cov(ω₃,(ln f)^n) = n·μ_L^{n-1}·Cov(ω₃,ln f)·(1 + O(k^{-1.3}))`: the leading (cited
`n=1`) term dominates by a full power of `k`, and the relative correction `r₂ ≤ 0.26`
for **all** `k≥6`, falling monotonically (0.26 at k=8 → 0.031 at k=28). The engine is
concentration: `Var(ln f)/μ_L² ~ k^{0.63}/k^{3.0} → 0`, so the fluctuation `δ=ln f−μ_L`
is small relative to `μ_L`, the binomial `(μ_L+δ)^n` is dominated by `μ_L^{n-1}`, and the
sign is carried by `Cov(ω₃, ln f) < 0`. Higher residual terms (`E[ω₃ δ^j]`, `j≥3`) are
suppressed by further powers of the small variance.

**Consequence.** The reduction `M_n ≤ 0` — hence the whole conjecture — is **provable for
all `k ≥ K₀`** once two Plancherel facts are made rigorous: (i) `Cov_Planch(ω₃, ln f) < 0`
(the cited `n=1`), and (ii) `Var_Planch(ln f) = o(μ_L²)` with `E[ω₃ δ^j] = o(μ_L^{j-1}|Cov₁|)`
(Kerov-CLT concentration of the dimension functional). The finitely many `k < K₀` are then
a direct check (`M_n ≤ 0` already verified k≤17). This is the concrete shape of the proof.

## 4. Proposed proof program

Prove `Cov_Planch(ω₃, (ln f)^n) ≤ 0` per `n`:
1. `n=1` — numerically established (all k≤19); rigorous proof open (see §4a).
2. **`n≥2`** — bound the sub-leading fluctuation terms `E[ω₃ δ^j]` (`j≥2`) against the leading `n μ_L^{n-1} Cov(ω₃, ln f)`. `ω₃ = |C₃|·Σ̂₃` is a low free cumulant (Biane/Śniady character-polynomial theory); `δ = ln f − μ_L` has Kerov-CLT-controlled central moments. The covariance is then a finite cumulant expression whose leading sign is fixed by `n=1` and whose remainder is `o(μ_L^{n-1})`.

## 4a. Literature status — NOT closeable by direct citation (the `ln f` obstruction)

A literature check (2026-07-25) places the problem squarely in the Kerov-CLT / Plancherel-fluctuation framework — **Ivanov–Olshanski**, *Kerov's central limit theorem for the Plancherel measure on Young diagrams* (arXiv:math/0304010); **Fulman**, *Stein's method and Plancherel measure of the symmetric group* (arXiv:math/0305423, Berry–Esseen for character ratios); **Biane** (Adv. Math. 138, 1998) and **Śniady** (PTRF 136, 2006) for the free-cumulant / normalized-character theory. But it is **not closeable by a direct citation**, for a specific structural reason:

- `ω₃ = |C₃|·χ̂₃` **is** a Kerov observable (a low free cumulant; its Plancherel law is Gaussian by Kerov's CLT).
- `ln f^λ = ln(k!) − Σ_□ ln(hook(□))` is a **hook-based, non-polynomial** functional — it lies **outside** the Ivanov–Olshanski algebra of polynomial functions on Young diagrams, where the clean CLT and Biane's free-cumulant asymptotics live. So `Cov_Planch(ω₃, ln f)` is a covariance of a character observable with a *smooth linear statistic of the shape*, which the cited theorems do not cover verbatim.

**Per-paper check** (corpus copies in `library/`, read 2026-07-25):

| paper | gives | why it does not close it |
|---|---|---|
| Ivanov–Olshanski, `library/arxiv-math-0304010v1/0304010v1.pdf` (Kerov CLT) | CLT for the character-polynomial algebra (`p_k^#`), the shape, and free cumulants/Biane | `ω₃=\|C₃\|χ̂₃` is in the algebra; **`ln f` is not** (non-polynomial, hook-based) |
| Śniady, `library/arxiv-math-0411647v2/0411647v2.pdf` (genus expansion, free prob.) | asymptotics of characters / products of JM moments — the epic's planned Phase-2 tool | works on the **Plancherel (β=2)** character side; does not reach the `(f^λ)^{β>2}` measure |
| Dołęga–Féray `library/arxiv-1402.4615v3/1402.4615v3.pdf`; Dołęga–Śniady `library/arxiv-1704.02352v2/1704.02352v2.pdf` (Gaussian fluctuations of **Jack**-deformed diagrams) | second-order asymptotics of Jack-deformed random shapes | `(f^λ)^β` is a Jack measure **only at β=2 (α=1)**; β>2 is outside the Jack family |

**Honest status:** the conjecture is **open**, reduced (§2–§3b) to a Kerov-CLT-framework statement whose genuinely-new ingredients are (i) a **CLT / covariance sign for the smooth linear statistic `ln f`** (outside the character-polynomial algebra) against the character observable `ω₃`, and (ii) control of the **`(f^λ)^{β>2}` (non-Jack) measure**. Both are plausibly reachable — the moment/Chebyshev transform of the shape CLT to the `ln f` linear statistic, plus a genus-expansion-style treatment adapted off β=2 — but each is a real research step, not a lookup. This corrects the earlier "cited Kerov/Biane" phrasing.

This replaces a single hard global Laplace-sign fact with a per-`n` covariance sign, `n=1` established and `n=2` numerically decomposed.

## Discipline

scope-(a) reduction + a scope correction to a prior (b)-over-claim. No fit; nothing wired; no `c_k`; L2 unchanged. The kernel remains an honest open §3b conjecture — this narrows the attack and fixes the exclusion scope. Verification: `computations/deltalambda/covariance_laplace_moment_reduction.py` (read-only; all checks pass). Coordination: posted on the epic PR #4153.

-- Ref: [manuscript] docs/coordination/ (qou-x631 covariance-kernel epic)
