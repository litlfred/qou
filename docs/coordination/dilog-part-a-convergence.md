# Coordination ledger — dilog Part-A Tauberian/DCT convergence

**Status (2026-07-24): Part A is CLOSED.** The one remaining open item of
`conj:dilogarithm-archimedean-limit` — the Tauberian/DCT convergence
`(1−q)·log Φ_n(x;q) → Li₂(x)` for `x∈(0,1)` (inhabiting the `ArchimedeanLimit x`
typeclass off `x=0`) — is now Lean-proved sorry-free. Everything in the dilog
thread (special values, reflection, duplication, derivative, integral rep,
Clausen, Part-A Bricks 1–2) was already closed on `main`; the convergence
itself landed via **#4157** (merged).

## What closed it (the leading Riemann-sum route)

`archimedeanLimit_Ioo {x} (hx0 : 0 < x) (hx1 : x < 1) : ArchimedeanLimit x`
in `Archimedean/DilogPartAConvergence.lean` (B3.5), assembled from the landed
B3.1–B3.4 bricks:

- `(1−q)·log Φ_n = S_n` (Bricks 1–2), then
- `|S_n − ∫_{qⁿ}^1 h| ≤ (1−q)(h(1)−h(qⁿ))` (`riemann_error_bound`),
- `∫_{qⁿ}^1 h = Li₂(x) − ∫_0^{qⁿ} h` (`integral_zero_one_eq_LiTwo` +
  `tail_bound`, `|tail| ≤ qⁿ·x/(1−x)`),
- ε-δ closed via `qⁿ ≤ e^{−n(1−q)}` (`pow_le_exp_neg_mul`) and
  `(1−q)(−log(1−x)) → 0`.

The unconditional consumer form `partialProduct_to_LiTwo_Ioo` wires it in.
`#4106` (the branch that carried B3.1–B3.4) was **superseded and closed**; #4157
rebased its bricks onto current `main` and added B3.5.

## The two routes — final disposition

| Route | Branch / PR | State |
|---|---|---|
| **Riemann-sum (CLOSED Part A)** | #4106 → **#4157 (merged)** | `archimedeanLimit_Ioo` sorry-free; #4106 closed as superseded. |
| **m-series (ingredients, this branch)** | `claude/dilog-tauberian-coeff-limit-2026-07-24` / #4152 | Two sorry-free termwise-limit lemmas: `tendsto_one_sub_div_pow_sub_one` (coeff `→ −1/(m+1)`), `tendsto_pow_mul_nhds_zero` (tail `→ 0`), in `Archimedean/DilogPartARiemannSum.lean`. Retained as an **independent-route cross-check** of the same DCT (both termwise limits agree with the Riemann-sum assembly); the m-series route was **stood down from full closure** per converge-on-landing once #4157 landed. |

Per the converge-on-landing directive: the m-series route now **verifies rather
than re-derives** — its two clean standalone `Tendsto` limits document the
independent termwise-convergence path and stay as complementary ingredients; no
second full `ArchimedeanLimit` instance is pursued.

## Consumer discharge

- **α_EM `1/π` per-mode weight** (merged #3831/#3834; audits
  `2026-07-17-alpha-em-permode-weight-localization.md`,
  `2026-07-17-alpha-em-zeta-anomaly-b1-count.md`). That thread localized the
  photon 1-loop measure `1/(π·b₁)=1/(8π)` to: (i) the bare `b₁` count —
  **derived** (`ζ_{Δ₁}(0)=−b₁`, area-free), and (ii) the `1/π` per-mode weight —
  reduced to *"the open `conj:dilogarithm-archimedean-limit` (Bloch–Suslin
  archimedean π) plus an explicit `2πg` identity on Bring."*
  **The Part-A half of that dilog dependency is now discharged** by #4157: the
  archimedean `Li₂` limit through which the `π` enters is proved on the
  sub-unity side. The **residual** α_EM wall is therefore narrowed to the
  conjecture's **Part B** (the substrate continuation `q→1⁺` / `x→1⁻`
  cross-cusp, where the Bloch–Suslin `π` and branch-cut cancellation live) plus
  the separate `2πg` genus identity — not the whole conjecture. (Notify recorded
  here rather than on the α_EM PRs, which are all merged/closed; bean qou-3nk0.)

## Remaining open content of the conjecture — Part B

`conj:dilogarithm-archimedean-limit` stays a `conjecture` block: **Part B** (the
substrate continuation `q→1⁺` and the `x→1⁻` cross-cusp uniformity, requiring
exact cancellation among algebraic poles before evaluating the principal branch)
is untouched and is now the conjecture's entire open content. Attack toolkit:
`log_neg_factor_split` (pole subtraction) + the numerics in
`docs/audits/2026-07-17-dilog-archimedean-limit-partB-pole-cancellation.md`.
Tracked in bean qou-ips1.
