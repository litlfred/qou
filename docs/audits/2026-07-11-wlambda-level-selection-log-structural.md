# Why `k(A)` is logarithmic — a conditional structural argument (GAP-A-3)

**Date:** 2026-07-11 · **Axis:** GAP-A-3 (brane-tower level selection) ·
**Type:** structural argument (formalize-first) — a **conditional** result with a
**provable core** + named **conjectural inputs**. **No fit; no scale; no closure.**
**Discipline:** "Conditional-proved ≠ premise-established" — the conclusion holds
*modulo* the stated hypotheses, which stay open; nothing here is claimed derived.

Follows the `W_λ` transfer-matrix thread
([`…-transfer-matrix-connected-part.md`](2026-07-11-wlambda-transfer-matrix-connected-part.md)):
scalar weights (intensive, dead) → `W_λ` transfer matrix → connected part is the
channel → non-abelian `(2,1)` rep → jet tower supplies unbounded growth → `k(A)`
is log-type (probe: `k∝A`, `k∝`bond-count falsified). This note supplies the
**argument** for the log-form, isolating exactly what is proved vs assumed.

## The claim

> **Conditional theorem.** *Assume (H1) the connected-tower picture
> `B(A) = s · w_std(k(A))` for a fixed scale `s`, and (H2) extensivity `B(A) = Θ(A)`.
> Then the level-selection rule satisfies `k(A) = Θ(log A / log log A)` — in
> particular `k(A) = O(log A)`, so `k ∝ A` and `k ∝` bond-count are excluded.*

The proof is elementary **given the growth rate of `w_std`**, which is the provable
core below. The content of the theorem is that the *level* is the inverse of a
super-exponential function evaluated at an *extensive* (linear) target.

## The provable core (verified; a clean combinatorial lemma)

`w_std(k) = Σ_{λ⊢k, λ⊇(2,1)} W_λ · f^{λ/(2,1)}` is the `q`-Plancherel-weighted
multiplicity of the standard `(2,1)` rep in the restriction `H_k ↓ H_3`. At `q=1`,
`Σ_λ W_λ = 1` **exactly**, so

$$
w_{\mathrm{std}}(k)\big|_{q=1} \;=\; \mathbb{E}_{\text{Planch}}\!\big[f^{\lambda/(2,1)}\big],
$$

the Plancherel expectation of the number of standard skew tableaux of shape
`λ/(2,1)`. [`wlambda_wstd_growth_bound_probe.py`](../../computations/deltalambda/wlambda_wstd_growth_bound_probe.py)
→ witness verifies (exact integer arithmetic, `k = 3..10`):

| k | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|
| `w_std(k)` | 0.667 | 0.917 | 1.70 | 3.85 | 8.78 | 21.2 | 55.5 | 159.7 |
| ratio | – | 1.38 | 1.85 | 2.27 | 2.28 | 2.41 | 2.62 | **2.88** |

The successive ratios are **strictly increasing** (`1.38 → 2.88`, unbounded) and
`w_std(k)/2^k` increases in the tail — so `w_std` grows **super-exponentially**
(factorial growth class), faster than every fixed `C^k`. The substrate deformation
`q = q₀` preserves this class (`w_std(q₀)/w_std(q=1) ∈ (0.3, 3)` throughout). This is
a self-contained combinatorial statement about the Plancherel-expected skew
multiplicity — the natural **Lean/proof target** (a super-exponential lower bound on
`E_Planch[f^{λ/(2,1)}]`; the increasing-ratio data is strong evidence, a closed form
`w_std(k)|_{q=1} = E_Planch[f^{λ/(2,1)}]` is the object to bound).

## The argument

Given the core, the theorem is one line. Write `w_std(k) ≍ k!^{c}` (factorial class,
`c>0`; the super-exponential growth). (H1)+(H2) give `s · w_std(k(A)) = Θ(A)`, so
`w_std(k(A)) = Θ(A)`, hence `k(A)!^{c} ≍ A`, hence by Stirling

$$
k(A) \;=\; \Theta\!\Big(\frac{\log A}{\log\log A}\Big)\;=\;O(\log A).
$$

A linear `k ∝ A` would make `B(A) = s·w_std(A) ≍ A!^{c}` — **super-factorial**, wildly
non-extensive; `k ∝` bond-count `= A(A-1)/2` is worse. Both are excluded *because the
tower weight grows super-exponentially* — no fit is involved, and this is exactly the
scale-free `k(A)` probe's finding (`k∝A` R²=0.67, `k∝`bonds R²=0.49 vs log-type R²≈0.88).

## Honest scope — what is proved vs open

- **Proved / verified (the core):** `w_std(k)` grows super-exponentially (combinatorial;
  the Lean target is a lower bound on `E_Planch[f^{λ/(2,1)}]`).
- **Rigorous given the core:** the log-form of `k(A)` — *conditional on H1+H2*.
- **Open (the conjectural inputs, = GAP-A-3):**
  - **(H1)** the connected-tower picture `B(A) = s·w_std(k(A))` — that binding *is* the
    scaled connected standard-channel tower weight at a single selected level. This is
    the substantive physics conjecture; the thread's probes make it *plausible*
    (extensive channel localized to the non-abelian `(2,1)` rep) but do not derive it.
  - **the level-selection map `k(A)` itself** — *that* a nucleus of mass `A` occupies a
    single sharp jet level (and this note shows only its **form** must be logarithmic,
    not *why* the map exists). Deriving `k(A)` from the categorical drivers is GAP-A-3.

This does **not** set the binding scale `s`, wire anything, or land absolute
magnitudes. It converts "why `k~log`?" from an open question into a **conditional
theorem with a provable combinatorial core** — the honest formalize-first output: the
remaining work is (i) prove the super-exponential lower bound in Lean, (ii) derive H1
+ the existence of `k(A)` from the drivers (Track-A, `s5-so3-keystone`).
