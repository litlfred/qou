# Coordination ledger — dilog Part-B cusp cancellation attack

**Goal.** Close (or reduce to a minimal named residual) the genuine Part-B wall of
`conj:dilogarithm-archimedean-limit`: the **uniform iπ-tower + linear-pole
cancellation across the cusp** yielding

$$
  \mathrm{reg}_n(x;q) \;\longrightarrow\; \mathrm{Li}_2(x) - \frac{\pi^2}{3}
  \qquad (q\to1^+,\ n\to\infty),
$$

where `reg_n` is the bare `(1−q)·log Φ_n(x;q)` with the exact per-factor
asymptotic `log(x qᵏ) + iπ` subtracted from every negative factor (`k > k*`,
`k* = log_q(1/x)`). Part A (`q→1⁻`) is CLOSED sorry-free (`archimedeanLimit_Ioo`,
merged #4157). Numerics + constant-identification: audit
`docs/audits/2026-07-17-dilog-archimedean-limit-partB-pole-cancellation.md`.

## The decomposition (what the wall actually is)

Using `clog_one_sub_pole_phase_split` (PR #4173, sorry-free): for a negative
factor `1 − x qᵏ` (`x qᵏ > 1`),

$$
  \mathrm{Log}(1 - x q^k) = \log(x q^k) + \log\!\big(1-(x q^k)^{-1}\big) + i\pi .
$$

Subtracting `log(x qᵏ) + iπ` (no free parameter) leaves `log(1-(x qᵏ)^{-1})`.
So (with `log Φ_n = −Σ_{k<n} log(1 − x qᵏ)`):

$$
  \mathrm{reg}_n = (1-q)\Big[\; -\!\!\sum_{k \le k_*}\!\log(1-x q^k)
     \;-\!\!\sum_{k_* < k < n}\!\log\!\big(1-(x q^k)^{-1}\big)\;\Big].
$$

The **iπ-tower cancellation is per-factor exact** (each negative factor's `+iπ`
is removed by the subtraction) — so `Im(reg_n) ≡ 0`. The **linear pole**
`log(x qᵏ)` is likewise removed per-factor by definition. The remaining content
is the convergence of the two **real** pieces:

| Piece | Sum | Limit | Vector | Status |
|---|---|---|---|---|
| **W-P1** positive factors `k ≤ k*` | `−(1−q)Σ_{k≤k*} log(1−x qᵏ)` | `Li₂(x) − π²/6` | V3 | open |
| **W-P2** regularized negative factors `k > k*` | `−(1−q)Σ_{k>k*} log(1−(x qᵏ)⁻¹)` | `−π²/6` | V1+V2 | **PROVED sorry-free (#4191)** |

Sum `= Li₂(x) − π²/3`. ✓

> **W-P2 CLOSED (2026-07-25, #4191).** The regularized negative-factor half is
> fully proved sorry-free in `DilogPartBEulerTail.lean`: the eta asymptotic
> `euler_tail_asymptotic` — `(1−p)·Σ'_m −log(1−p^{m+1}) → π²/6` as `p→1⁻`
> (`p = 1/q`) — assembled from V1 (`euler_tail_coeff_limit` + `_le` + `_nonneg`),
> V2b (`euler_tail_jseries_tendsto`, Tannery), and V2a
> (`euler_tail_lambert_rearrange`, nonneg Fubini). This is the classical
> Hardy–Ramanujan / Dedekind-eta limit `(1−p)log∏(1−pᵐ) → −π²/6`, previously
> absent from Mathlib and the corpus.

### W-P2 is the Euler-function / Dedekind-eta asymptotic

Substituting `m = k − k*` and `x q^{k*} = 1`: `(x qᵏ)⁻¹ = q^{−m}`. With
`p = 1/q ∈ (0,1)` (so `q→1⁺ ⟺ p→1⁻`), the piece is
`−(1−q)Σ_{m≥1} log(1 − pᵐ)`, and

$$
  \boxed{\;\lim_{p\to1^-}(1-p)\cdot\log\!\prod_{m\ge1}(1-p^m) \;=\; -\frac{\pi^2}{6}\;}
$$

— the **Euler-function / Dedekind-eta / Hardy–Ramanujan asymptotic**. This is a
genuine Mathlib gap (not present in Mathlib or the QOU corpus as of 2026-07-25).
It splits into:

- **V1 (cheap, LANDED sorry-free — #4191):** the two Tannery/DCT inputs for the
  Lambert `j`-series, `DilogPartBEulerTail.lean`:
  - `euler_tail_coeff_limit` — termwise `(1−p)pʲ/(1−pʲ) → 1/j`;
  - `euler_tail_coeff_le` + `euler_tail_coeff_nonneg` — uniform `0 ≤ · ≤ 1/j`
    (⇒ `·×(1/j)` dominated by summable `1/j²`).
- **V2 (medium):**
  - **V2b (heart, LANDED sorry-free — #4191):** `euler_tail_jseries_tendsto` —
    `Σⱼ (1/j)(1−p)pʲ/(1−pʲ) → Σⱼ 1/j² = π²/6` via Tannery
    (`tendsto_tsum_of_dominated_convergence`, arbitrary filter) + `hasSum_zeta_two`.
  - **V2a (remaining — the Lambert rearrangement):** for `p∈(0,1)`,
    `Σ'_m −log(1−p^{m+1}) = Σ'_j (1/(j+1))·p^{j+1}/(1−p^{j+1})`, a **nonneg Fubini**
    (`tsum_comm` / `summable_prod_of_nonneg`) on `a m j = p^{(m+1)(j+1)}/(j+1)`:
    - row: `Σ'_j a m j = −log(1−p^{m+1})` — reuse the corpus primitive
      `neg_log_one_sub_hasSum` (`DilogarithmArchimedeanLimit.lean:264`).
    - col: `Σ'_m a m j = (1/(j+1))·p^{j+1}/(1−p^{j+1})` — geometric shift
      `Σ'_m r^{m+1} = r/(1−r)`.
    - summability of the uncurried family from rows-summable + row-sums-summable
      (`Σ_m −log(1−p^{m+1})` summable, the one nontrivial bound).
    Combined with V2b this gives the eta asymptotic
    `(1−p)·Σ'_m −log(1−p^{m+1}) → π²/6`, i.e. `(1−p)·log ∏(1−pᵐ) → −π²/6`.

### W-P1 is the Part-A Riemann sum on the far side of the branch point

- **V3 (hard):** `−(1−q)Σ_{k≤k*} log(1−x qᵏ) → Li₂(x) − π²/6` for the `q>1`
  geometric partition in `u = qᵏ` running from `u=1` (k=0) **up to the branch
  point** `u = 1/x` (k=k*, where `x u = 1`). Reuse the Part-A integrand
  machinery in `DilogPartAConvergence.lean` (`integral_zero_one_eq_LiTwo`,
  `riemann_error_bound`, `tail_bound`, the convexity/monotonicity bricks) adapted
  to the `u>1` side with the integrable `log` singularity at the branch point.

### V4 (assembly)

Combine V1–V3 + `clog_one_sub_pole_phase_split` (#4173) into
`reg_n → Li₂(x) − π²/3`, with the uniform `q→1⁺ × n→∞` exchange.

## Discipline

Formalize-first; anti-fit (no constant is fitted — `π²/6 = ζ(2) = Li₂(1)` is the
theorem-forced dilog-inversion / Faddeev-`Φ_b` modular anomaly, audit §"Derivation").
Each vector lands sorry-free or honestly reduces to a minimal named residual. The
block stays `kind:conjecture` until V4 assembles the whole limit.

Beans: milestone `qou-icx5`; V1 `qou-sbfy`, V2 `qou-tt1l`, V3 `qou-jplv`,
V4 `qou-9m98`. Building block already landed: `qou-ips1` / #4173.

---

## 2026-07-25 — W-P1 status: fully assembled, reduced to one scalar limit

**W-P2 is CLOSED** (the Dedekind-eta asymptotic, #4191). **W-P1's entire
machinery is now landed sorry-free** in
`content/quantum-observable-universe/lean/QOU/Archimedean/DilogPartBBranchPointSum.lean`:

| Brick | Lemma | PR |
|---|---|---|
| interior target integral | `integral_Icc_eq_LiTwo_sub` | #4210 |
| improper target limit | `tendsto_integral_x_to_c_nhdsWithin_one` (→ `π²/6 − Li₂(x)`) | #4210 |
| going-up convexity/monotonicity | `convexOn_neg_log_one_sub_mul_Icc`, `h_monotoneOn_Ioc` | #4215 |
| going-up per-cell squeeze | `h_integral_le_right_Icc`, `h_integral_ge_left_Icc` | #4219 |
| **going-up telescoping bound** | `riemann_error_bound_up` (majorant `qⁿ(q−1)(h(qⁿ)−h(1))`) | #4241 |
| log-sum = Riemann sum | `partialSum_up_eq` | #4247 |
| change of variables | `integral_one_to_c_eq_LiTwo_sub` | #4257 |
| error decomposition | `error_up_eq` | #4262 |
| **assembly** | `wp1_riemann_bound` | #4262 |

`wp1_riemann_bound` gives, for `1 < q`, `x·qⁿ < 1`:
`0 ≤ (Li₂(xqⁿ) − Li₂(x)) − (1−q)Σ_{k<n} log(1−xqᵏ) ≤ (q−1)(−log(1−xqⁿ)) − (q−1)qⁿ(−log(1−x))`.

As `q→1⁺` with `xqⁿ→1⁻`: `Li₂(xqⁿ)→π²/6` (brick 2 Abel), the
`(q−1)qⁿ(−log(1−x))` term `→0` (bounded × `q−1`). **So W-P1 → `Li₂(x) − π²/6`
iff the single scalar limit `(q−1)·log(1−xqⁿ) → 0`.**

### The residual: `(q−1)·log(1−xqⁿ) → 0` is non-uniform (NOT closeable as a brick)

This is the irreducible open input, and it does **not** admit a clean
unconditional proof:

- With `n = k*(q) = ⌊log_q(1/x)⌋` (the last positive factor), the endpoint sits
  against the branch point: `x·q^{k*} ∈ [1/q, 1)`, so `δ := 1−xq^{k*} ∈ (0,(q−1)/q]`.
  That is only an **upper** bound on `δ` (a *lower* bound on `−log δ`), never the
  **lower** bound on `δ` needed to force `(q−1)(−log δ)→0`.
- `δ` is governed by the **fractional part of `log_q(1/x)`**, which oscillates as
  `q→1⁺`. The limit is genuinely **conditional** — it holds under the Faddeev
  scaling (or a Diophantine no-resonance condition on `x`), not for every `q→1⁺`.
  This is the same analytic-number-theoretic subtlety the conjecture itself flags
  ("exact cancellation among algebraic poles before evaluating the principal
  branch").
- **Trivial sub-case (bulk):** if `x·qⁿ ≤ ρ < 1` (endpoint bounded away from the
  branch point) then `δ ≥ 1−ρ` and `(q−1)(−log δ)→0` immediately — proving the
  *bulk*, short of the branch point.

**A future proof needs the sequence-indexed Faddeev-scaling machinery** (joint
limits of the integer `nⱼ` and real `qⱼ`, with floor functions + equidistribution
of `frac(log_{qⱼ}(1/x))`), or a Diophantine hypothesis on `x`. That is genuine
research-level analytic number theory, not a Lean brick — do **not** fabricate a
one-liner (anti-laundering). The clean analytic seed to start from: `t·log t → 0`
as `t→0⁺`, applied once a lower bound `δ ≥ c(q−1)` is available from the scaling.

Bean `qou-jplv` carries this. V4 (`reg_n → Li₂(x) − π²/3`) then glues W-P1 + W-P2
(#4191) + the `clog_one_sub_pole_phase_split` per-factor split (#4173), and is
gated on this same scalar limit.
