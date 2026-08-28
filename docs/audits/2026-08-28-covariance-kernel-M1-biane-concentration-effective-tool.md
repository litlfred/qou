# Covariance-kernel epic (`qou-x631`) — the finite-n tool: Biane concentration is quantitative but INSUFFICIENT; the gap is a second-order CLT rate

**Date:** 2026-08-28 · **Branch:** `claude/m1-biane-concentration-effective-tool-2026-08-28` · **Tier:**
tool assessment with a **self-correction** (an initial "effective tool found" over-claim, retracted
here on reflection) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged.
**Epic:** `qou-x631`; gap `qou-k5r5`.

## What the finite-n step needs

The finite-n step ([`…-finite-n-cs-closure-step.md`](2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md),
PR #5903) reduced `M₁>0` to: keep the (CS) margin `m(n) = ρ_P(n) − σ_D(n)/σ_A(n)` positive for
`n ≥ N₀`, where `m(n) → 0.30` (leading, derived, 52 % headroom). Because `m(n)` is a **ratio of
standard deviations plus a correlation**, closing it needs the **second-order** convergence
`σ_D/σ_A → 0.6796`, `ρ_P → 0.9798` **with an explicit rate** — a *variance/covariance-CLT* statement.

## Candidate: Biane concentration (`arxiv-math-0006111`) — quantitative, but the wrong order

Biane's **Theorem 1 / Corollary 1**: for the approximate-factorization class (Plancherel, `δ→0`),
`|R_l(λ) − R̄_l| ≤ K·n^{l/2 − 1/4}` on a set of probability `≥ 1 − n^{-1/2}`. This is a genuine
**quantitative** result with an explicit `n^{-1/4}` relative rate — the closest in-corpus quantitative
tool.

**But it is insufficient for the (CS) margin, and an earlier draft of this note claiming otherwise is
retracted.** The reason is an order/side mismatch:

- Biane gives **one-sided, first-order** control: a high-probability *deviation* (LLN-with-rate) bound.
  It bounds the *fluctuation size*, hence gives a **crude upper** bound on a variance
  (`Var ≲ (n^{l/2−1/4})² = n^{l−1/2}`, overestimating the true `n^{l−1}` by `n^{1/2}`), and gives **no
  lower bound** on any variance or correlation.
- The (CS) margin needs **two-sided, second-order** control: `σ_D/σ_A` and `ρ_P` converging to their
  leading values with a rate. That requires an **upper** bound on `σ_D` *and a lower* bound on `σ_A`
  (and a lower bound on `ρ_P`) — none of which a one-sided deviation bound provides, and none of which
  survives Biane's `n^{1/2}` crudeness.

A deviation/LLN-with-rate bound does not yield a variance-ratio convergence rate. So Biane, though
quantitative, does **not** close the finite-n step.

## The sharpened "need lit?" answer

The missing ingredient is a **quantitative (effective) SECOND-ORDER Kerov CLT** — an explicit rate for
the *variance/covariance* convergence of Plancherel linear statistics (specifically the non-`A`
statistics `Σ|c|`, `ΣD²` and their covariance with `ω₃`). The corpus provides:

- the **qualitative** second-order CLT (Ivanov–Olshanski `0304010`, Dołęga–Féray `1402.4615`,
  Dołęga–Śniady `1704.02352`) — a *limit*, no rate;
- **first-order** quantitative concentration (Biane `0006111`) — a *deviation* rate, wrong order;
- a **marginal** Berry–Esseen (Fulman `0305423`) — ruled out (#5887).

**None gives a second-order variance-convergence rate.** That specific result — an effective/Edgeworth
version of the Kerov CLT at the *variance* level — is what would close `M₁>0` via the (CS) route, and it
is **not in the corpus**. (Whether it exists in the wider literature is the open lit question; arxiv is
firewalled here.)

## Honest status

- **Self-correction recorded:** Biane concentration is quantitative but is **not** the effective tool
  for the (CS) margin (first-order/one-sided vs the required second-order/two-sided). The initial
  "effective tool IS in the corpus" claim is **withdrawn**.
- **Sharper frontier:** the one open ingredient is a *quantitative second-order (variance-level) Kerov
  CLT* for `Σ|c|`, `ΣD²`. Absent that, the alternative is a bespoke direct derivation of the
  variance-convergence rate — a genuine analysis project, but with 52 % headroom (crude rate suffices).
- Gap `qou-k5r5` stays **OPEN**; the leading order remains proved (#5901), `M₁>0` exact to n=78.

## Cross-references

- Finite-n step: [`2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md`](2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md)
- Leading-order (CS) derivation: [`2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md`](2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md)
- Shape-field CLT tools (qualitative): [`2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md`](2026-08-28-covariance-kernel-M1-sigmah-not-in-free-cumulant-algebra.md)
- Gap bean `qou-k5r5`.
