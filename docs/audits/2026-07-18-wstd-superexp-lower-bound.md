# A rigorous super-exponential lower bound on the GAP-A-3 tower weight w_std(k)

**Date:** 2026-07-18 · **Branch:** `claude/deltalambda-wstd-superexp-lower-bound-2026-07-18` ·
**Tier:** rigorous provable-core (exact integer arithmetic + Lean lemma) · **Discipline:**
scope-(a); no fit; no scale; nothing wired; no `c_k`; L2 unchanged (2/7). **Upgrades:** the
empirical growth check `wlambda_wstd_growth_bound_probe.py` (strictly-increasing ratios to k=10).

## What this establishes

The GAP-A-3 level-selection argument (Δ_λ magnitude leg) needs the jet-tower weight to grow
super-geometrically, so that inverting it against an **extensive** (linear-in-A) binding target
forces `k(A) = O(log A)` — structurally excluding `k~A` and `k~bond-count`. The prior probe verified
super-geometric growth **empirically** (k≤10). This gives the **rigorous lower bound** behind it,
reducing the "super-geometric lower bound" Lean target to a fully-classical inequality plus one
clean symmetric-function sub-lemma.

The chain (all steps verified exactly for k=3..12):

    w_std(k)|_{q=1} = E_Planch[f^{λ/(2,1)}] = (1/k!) Σ_{λ⊢k} (f^λ)² f^{λ/(2,1)}.

**(A) Level-3 branching identity** (exact, per λ):
`f^λ = f^{λ/(3)} + 2·f^{λ/(2,1)} + f^{λ/(1,1,1)}` — an SYT of λ is a choice of its first-3-cells
shape μ⊢3 (`f^μ` ways) and an SYT of λ/μ.

**(B) Exact Plancherel identity.** Multiply (A) by `(f^λ)²/k!`, sum, and use conjugation symmetry
of Plancherel measure (`P_k(λ)=P_k(λ')`, `f^{λ/(3)}=f^{λ'/(1,1,1)}` ⇒ `E[f^{λ/(3)}]=E[f^{λ/(1,1,1)}]`):

    Σ_{λ⊢k} (f^λ)³ / k!  =  2·w_std(k)  +  2·E_Planch[f^{λ/(3)}].

**(C) Rigorous super-exponential lower bound on the classical cube moment:**

    Σ_{λ⊢k}(f^λ)³/k!  ≥  (max_λ f^λ)³/k!  ≥  (k!/p(k))^{3/2}/k!  =  √(k!)/p(k)^{3/2},

using `max_λ f^λ ≥ √(k!/p(k))` (since `Σ(f^λ)² = k!` over `p(k)` partitions ⇒ the max square ≥ the
mean). By Stirling `√(k!) = (k/e)^{k/2}·poly` beats every fixed `C^k`, while `p(k) = exp(π√(2k/3))·poly`
is sub-exponential, so the bound → ∞ **super-exponentially**.

**(D) Transfer to w_std** via the sub-lemma `w_std(k) ≥ E_Planch[f^{λ/(3)}]` (the (2,1)
channel dominates the (3) channel in expectation; verified k≤14). Then (B) gives
`Σ(f^λ)³/k! = 2w_std + 2E[f^{λ/(3)}] ≤ 4·w_std`, so

    w_std(k)  ≥  ¼·Σ(f^λ)³/k!  ≥  ¼·√(k!)/p(k)^{3/2}  →  super-exponential.

**(D-reform) Sagan–Stanley reduction of (D).** The classical identity
`Σ_{λ⊢k} f^λ f^{λ/μ} = (k!/m!)·f^μ` (verified exactly for every μ⊢3, k≤14) says that in the joint
(Plancherel λ, uniform SYT) law the **first-3-cell shape is Plancherel-distributed on μ⊢3**:
`P(shape₃=μ) = (f^μ)²/6`. This reformulates (D) into the clean conditional-expectation inequality

    2·E[f^λ | shape₃=(2,1)]  ≥  E[f^λ | shape₃=(3)].

The Sagan–Stanley backbone is rigorous; the conditional inequality itself remains verified-not-proved
(the one open sub-goal).

## The Lean lemma (rigorous core C)

The analytic heart of (C) is the **pigeonhole cube–square inequality**, formalized rpow-free in
[`QOU/BraidsAndKnots/WstdSuperExpBound.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/WstdSuperExpBound.lean):

> For a nonnegative real family `a : ι → ℝ` over a nonempty finite index type with `∑ aᵢ² = S` and
> `N = card ι`:  `S³ ≤ N³·(∑ aᵢ³)²`.

Applied with `aᵢ = f^λ`, `S = Σ(f^λ)² = k!`, `N = p(k)`, this is `(k!)³ ≤ p(k)³·(Σ(f^λ)³)²`, i.e.
`Σ(f^λ)³ ≥ (k!)^{3/2}/p(k)^{3/2}`, whence `Σ(f^λ)³/k! ≥ √(k!)/p(k)^{3/2}` — exactly (C). The proof
is pigeonhole (some square ≥ the mean `S/N`) + single-term-≤-sum + cube/square monotonicity.

A second lemma `wstd_ge_quarter_lower_bound` formalizes the **(B)+(D) algebraic transfer**: from
`cube = 2·w_std + 2·e`, `0 ≤ e`, `e ≤ w_std`, and a lower bound `L ≤ cube`, conclude `L/4 ≤ w_std`
(`linarith`). Together the two lemmas discharge the entire analytic/algebraic skeleton of the bound;
the residual inputs are the SYT-combinatorial facts (A), (B)'s identity, Sagan–Stanley, and (D)'s
inequality — verified computationally (k≤14), and Lean-targets pending Mathlib SYT machinery.

## Status of the pieces

- **(A) branching, (B) Plancherel identity, (C) cube bound** — rigorous ((C)'s core is the Lean
  lemma above; (A)/(B) are exact combinatorial identities, verified per-λ to k=12, Lean-ready via
  Mathlib SYT machinery).
- **(D) `w_std ≥ E[f^{λ/(3)}]`** — the one remaining clean symmetric-function inequality, verified
  k≤12; its general proof (or a weaker explicit `w_std ≥ ε·Σ(f^λ)³/k!`) is the next Lean sub-goal.

## What this does NOT do

Sets no scale; closes no binding; the connected-tower picture `B(A) ~ scale·w_std(k(A))` and
extensivity `B~A` remain the conjectural inputs. It supplies the *provable growth* that the
log-type `k(A)` rests on. No fit; nothing wired; μ–p / Δ_λ closure NOT achieved.

## Compute

- Probe: [`computations/deltalambda/wlambda_wstd_superexp_lower_bound.py`](../../computations/deltalambda/wlambda_wstd_superexp_lower_bound.py) (exit 0)
- Witness: `computations/deltalambda/wlambda-wstd-superexp-lower-bound.witness.json`
- Lean: [`content/quantum-observable-universe/lean/QOU/BraidsAndKnots/WstdSuperExpBound.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/WstdSuperExpBound.lean)

## Cross-references

- The empirical growth probe this upgrades: `computations/deltalambda/wlambda_wstd_growth_bound_probe.py`
- GAP-A-3 gate-open ruling: [`2026-07-13-delta-lambda-gate-open-for-all.md`](2026-07-13-delta-lambda-gate-open-for-all.md)
- Adjacent binding-frontier work (P1/P2 prunes, distinct piece): PR #3808
- Option E ledger: [`docs/coordination/option-e.md`](../coordination/option-e.md)
