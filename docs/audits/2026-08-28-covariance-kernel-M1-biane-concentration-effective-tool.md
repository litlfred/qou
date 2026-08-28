# Covariance-kernel epic (`qou-x631`) — the effective tool for the M₁>0 finite-n bound IS in the corpus (Biane concentration)

**Date:** 2026-08-28 · **Branch:** `claude/m1-biane-concentration-effective-tool-2026-08-28` · **Tier:**
tool identification (answers "need lit?"; states the remaining derivation precisely — does NOT execute
it) · **Discipline:** scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`;
gap `qou-k5r5`.

## The gap this closes (partially)

The finite-n step ([`…-finite-n-cs-closure-step.md`](2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md),
PR #5903) reduced `M₁>0` to one requirement: an **effective / quantitative** bound on the IO-CLT
variance asymptotics, trapping the damped-oscillatory (CS) margin below the derived `0.30` leading
value for `n ≥ N₀`. It stated this was "not off-the-shelf (Fulman's marginal Berry–Esseen ruled out;
qualitative CLT gives no rate)." **That was too pessimistic — the effective tool is in the corpus.**

## The tool: Biane, *Approximate factorization and concentration for characters of symmetric groups* (`arxiv-math-0006111`)

**Theorem 1** (moments) and its **Corollary 1** (free cumulants). For a positive-definite normalised
`ψ` in the approximate-factorization class `F^n_{c,δ}` on `S_q`, there is a constant `K` such that `ψ`
is `(δ+q^{-1})^{1/2}`-supported by the set of Young diagrams `λ` with

> `|m_l(λ) − m_l(ψ)| ≤ K(δ+q^{-1})^{1/4} q^{l/2}`  (Cor 1: same for free cumulants `|R_l(λ)−R_l(ψ)|`),
> for all `l ≤ n/2`.

**Plancherel is in this class with `δ → 0`** (the regular-representation character factorises exactly),
so with `q = n`:

> **`|R_l(λ) − R̄_l| ≤ K·n^{l/2 − 1/4}` on a set of Plancherel-probability `≥ 1 − n^{-1/2}`.**

This is an **explicit, quantitative** deviation bound with a concrete `n^{-1/4}` relative rate — exactly
the *effective* control the finite-n step lacked, and **crude** (the CLT fluctuation is the sharper
`n^{l/2 − 1/2}`; Biane's is looser by `n^{1/4}`), which is **fine**: the leading (CS) margin is `0.30`
(52 % headroom), so a crude rate is all that is required. (An earlier note dismissed Biane as
"character-algebra, `Σh∉A` bites" — wrong: concentration is a *deviation* bound on the diagram, broader
than exact membership in the polynomial-function algebra.)

## The remaining derivation (concrete, no longer tool-less)

`M₁>0` for all n now reduces to executing the **concentration → (CS)-margin chain**:

1. **Moments/cumulants → the three (CS) quantities.** `ω₃ = (R₄+R₂)/3` is directly a cumulant
   (Cor 1 applies verbatim). `Σ|c| = ∫|x|dm` is a **Lipschitz, non-polynomial** functional — bound it by
   approximating `|x|` by polynomials on the (concentrated, bounded) support, controlling the error by
   Thm 1's moment bounds. `ΣD² = Σ_u D(u)²` is **quadratic** in the profile — its fluctuation
   linearises to `2⟨D⟩δD` (a moment-linear statistic, Thm 1 applies) plus an `O(√n)` remainder to be
   bounded.
2. **Deviation → variance.** Biane gives a high-probability *support* statement, not a variance bound.
   Convert via: (concentration on the bulk set) + (a tail bound on the exceptional `n^{-1/2}` set using
   crude a-priori moment bounds). This yields `|σ_A²/n² − V_A| ≤ C n^{-a}`, likewise `σ_D²`, `ρ_P`, with
   `a > 0` explicit (expected `a = 1/4` from the rate).
3. **Absorb in the margin.** With `|margin(n) − 0.30| ≤ C' n^{-a}`, pick `N₀` with `C' N₀^{-a} < 0.30`;
   then `(CS)` holds for `n ≥ N₀`, and `4 ≤ n < N₀` is closed by the exact table (have `(CS)` to n=40,
   `M₁>0` to n=78). That **completes `M₁>0` for all n**.

## Honest status

- **Answered:** "need lit?" — the effective tool is **in the corpus** (`arxiv-math-0006111`, Thm 1 /
  Cor 1); the finite-n step is **not tool-less**. This supersedes the #5903 audit's "not off-the-shelf".
- **Not executed:** the three-step chain above is a real derivation (steps 1–2 need care for the
  non-polynomial `Σ|c|` and quadratic `ΣD²`, and for the deviation→variance conversion). No claim that
  `M₁>0` is proved — only that the last missing ingredient has a named, in-corpus quantitative tool with
  adequate (crude) rate.
- Gap `qou-k5r5` stays **OPEN** — but the "effective bound" is now a concrete derivation against a
  cited theorem, not an open search for a tool.

## Cross-references

- Finite-n step (the requirement this addresses): [`2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md`](2026-08-28-covariance-kernel-M1-finite-n-cs-closure-step.md)
- Leading-order (CS) derivation: [`2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md`](2026-08-28-covariance-kernel-M1-io-leading-order-CS-derived.md)
- Gap bean `qou-k5r5`.
