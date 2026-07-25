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

| Piece | Sum | Limit | Vector |
|---|---|---|---|
| **W-P1** positive factors `k ≤ k*` | `−(1−q)Σ_{k≤k*} log(1−x qᵏ)` | `Li₂(x) − π²/6` | V3 |
| **W-P2** regularized negative factors `k > k*` | `−(1−q)Σ_{k>k*} log(1−(x qᵏ)⁻¹)` | `−π²/6` | V1+V2 |

Sum `= Li₂(x) − π²/3`. ✓

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

- **V1 (W-P2a, cheap, formalize-first):** the constant as a Lean integral —
  `∫₀^∞ log(1 − e^{−s}) ds = −ζ(2) = −π²/6`, via
  `−log(1−e^{−s}) = Σ_{j≥1} e^{−js}/j` (nonneg) ⇒ `integral_tsum` ⇒
  `Σ_j (1/j)(1/j) = ζ(2)` (`hasSum_zeta_two`). Mirrors the merged `LiTwo_one`.
- **V2 (W-P2b, medium):** the Riemann-sum / dominated-convergence exchange
  `(1−p)·Σ_{m≥1} log(1−pᵐ) → ∫₀^∞ log(1−e^{−s}) ds`, reducing the eta asymptotic
  to V1.

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
