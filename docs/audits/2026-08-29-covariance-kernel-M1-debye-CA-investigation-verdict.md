# Covariance-kernel epic (`qou-x631`) — M₁>0: Debye `C_A` investigation + verdict

**Date:** 2026-08-29 · **Branch:** `claude/m1-debye-CA-investigation-2026-08-29` · **Tier:**
investigation (large-θ constant measurement) + reasoned verdict · **Discipline:** no fit; nothing
wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## Question

Close `M₁>0` for all n *outright* by pinning the rigorous Olver/Debye bulk constant `C_A` for
`Var(Σ|c|)` (⟹ explicit `C ≤ 2.668`, `N₀ ≤ 79`), **or** accept the "rigorous modulo one explicit
constant" state? This decides between doing the multi-page hard-analysis constant-tracking and banking
the arc at its current resting point.

## Investigation — the true asymptotic constants at large θ

`wlambda_covariance_epic_M1_debye_CA_investigation.py` (exit 0; exact Bessel sums, `O(M²)`, no
partitions; mpmath 40 dps; NO float64) pushes the poissonized descent-DPP ingredients to θ=1280:

| quantity | measured | vs the rigorous worst case |
|---|---|---|
| `V_A/θ² → v_A` | `0.810557` (Richardson) | — |
| `V_A/θ²` convergence exponent | **a ≈ 1.18** | worst-case kink bound is θ^{−1/2}; true is ~2× faster |
| `C_A^emp = sup\|V_A/θ²−v_A\|√θ` | **0.0076** | the constant a rigorous θ^{−1/2} bound must exceed |
| `ρ_P → ρ_∞` exponent | **θ^{−1}** (`\|ρ−ρ_∞\|·θ = 0.13` flat) | — |
| fixed-n margin constant (PR #5934) | `≈ 0.087`, decreasing | target `C ≤ 2.668` |

**Two findings that settle the feasibility:**

1. **The convergence is θ^{−1} to θ^{−1.18}, materially faster than the θ^{−1/2} worst case.** The `|u|`
   kink does not, at scale, slow `V_A` to θ^{−1/2} — the measured exponent is ≈1.18. So the rigorous
   θ^{−1/2} bound (all one can *prove* cheaply) is very loose; the *true* deviation is far smaller.
2. **The true constants are tiny.** `C_A^emp = 0.0076`; the margin constant is `≈ 0.087`. Against the
   `C ≤ 2.668` target the headroom is **30–300×**.

## Verdict — accept "rigorous modulo one explicit constant" (recommended)

The evidence says closing outright would **succeed**: a rigorous Olver bound's constant is a small
multiple of the true asymptotic coefficient (Olver's DLMF §10.41 error bounds are sharp), and the true
coefficient here is `~0.008–0.09`, 30–300× under target. **But producing the *verified* `C` requires
carrying the explicit Olver `θ^{−1/2}` remainder through the `x²`-weighted bulk sum to `C_A`, then
through the ratio `m = ρ_P − σ_D/σ_A` — a multi-page hard-analysis computation.** Executing it in one
session without an independent check (no Lean formalization of Bessel asymptotics is in reach) carries
a real risk of a sign/factor error, and a *wrong* "rigorous `C`" is worse than an honest open — it
would be exactly the laundering the epic's discipline forbids.

**Recommendation: accept the resting point.** The honest, defensible statement of the arc is:

> `M₁ > 0` is **proved for all n ≤ 78** (exact `Fraction`, Track B), and **reduced, for n > 78, to a
> single explicit constant** — the Olver/Debye bulk-remainder `C_A` — in a rigorous three-region
> (BOO sine bulk + BDJ Airy edge + Olver tail) + de-poissonization scheme whose exponents are
> validated and whose true constant carries 30–300× headroom against the threshold that would close it.

This is a strong, publishable resting state: the mathematics is complete in shape and the one missing
number is explicit-in-principle with large measured headroom. Closing it outright is a well-scoped
follow-on (the Debye constant-tracking), not a new idea.

**If the owner prefers to close outright:** the single remaining computation is the explicit Olver
remainder (DLMF §10.41.10) for `J_x(2√θ)` in the bulk `|x| < 2√θ(1−ε)`, converted to
`|J(x,y) − S(x−y;ρ)|`, summed against `(g_A(x)−g_A(y))²` to bound `|V_A/θ² − v_A| ≤ C_A θ^{−1/2}`,
with `C_A` explicit; then the analogous (easier, smooth-weight) `C_W`, `C_P`, the de-poissonization
`O(1/n)` constant, and the Lipschitz ratio propagation. Each is standard; the labor is the bookkeeping.

## Compute

- [`wlambda_covariance_epic_M1_debye_CA_investigation.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_debye_CA_investigation.py)
  (exit 0; large-θ exact Bessel sums; NO float64).

## Cross-references

- Constant-C landscape: [`2026-08-29-covariance-kernel-M1-constant-C-and-N0.md`](2026-08-29-covariance-kernel-M1-constant-C-and-N0.md)
- Rigorous finite-n bound: [`2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md`](2026-08-29-covariance-kernel-M1-rigorous-finite-n-bound.md)
- Descent-DPP reduction: [`2026-08-28-covariance-kernel-M1-descent-dpp-variance-rate.md`](2026-08-28-covariance-kernel-M1-descent-dpp-variance-rate.md)
- Gap bean `qou-k5r5`.
