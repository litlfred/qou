# Keystone `W_λ`: a new falsifiable necessary-condition — super-exponential branched-tower growth

**Date:** 2026-07-11 · **Axis:** s5-so3-keystone (geometric origin of `W_λ`) + GAP-A-3
cross-link · **Type:** necessary-condition gate (falsifiable) · **No fit; no closure.**
**Discipline:** adds a *test* for any candidate geometric `W_λ`; does not construct one.

## Context

The keystone's single open object is the **geometric origin of the q-Plancherel
measure** `W_λ = d_q(λ)²/[n]_q!` — at `q₀ ≈ 1.10998` (real `>1`), via the non-compact
`SU_q(2) → E_q(2)` Hahn–Exton q-Bessel contraction / colored Σ(2,3,5) WRT q-series
(owner-gated; `s5-so3-keystone` §Current state). Any candidate index must satisfy the
**existing necessary conditions**: C1 (normalisation `Σ_λ W_λ = 1`), C2
(chirality-blindness `W_{λ′}=W_λ`), C6 (full support `W_λ>0`), the **defect cubic**
`144·C(n) = −n(n−1)(2n−13)` on `1−Z(n)` (`WLambdaDefectClosedForm.lean`), and the
`f_pn` bracket. All of these constrain `W_λ` **pointwise** or via the **unweighted**
sum `Z(n) = Σ_λ W_λ`.

## The new gate (independent of the existing ones)

The `W_λ` transfer-matrix / binding thread (sibling PR #3548) surfaced a quantity the
existing gates do **not** constrain: the **multiplicity-weighted branched sum**

$$w_{\mathrm{std}}(k) \;=\; \sum_{\lambda\vdash k}\; W_\lambda\;\cdot\;\operatorname{mult}_{(2,1)}(\lambda\!\downarrow\! H_3)\;=\;\mathbb{E}_{W}\!\big[f^{\lambda/(2,1)}\big],$$

the `W`-expected multiplicity of the standard `(2,1)` rep in the restriction
`H_k ↓ H_3` (the connected binding channel). At `q=1` (`Σ W_λ = 1`) this is exactly the
Plancherel expectation `E_Planch[f^{λ/(2,1)}]`.

> **Necessary condition (C8, super-exponential growth).** Any geometric realisation of
> `W_λ` must reproduce `w_std(k)` growing **super-exponentially** — successive ratios
> `w_std(k)/w_std(k−1)` strictly increasing and unbounded (verified `1.38 → 2.88` over
> `k=3..10`, exact at `q=1`; `w_std(k)/2^k` increasing in the tail → factorial growth
> class), with the substrate deformation `q₀` preserving the class.

This is **independent** of C1/C2/C6 (pointwise / unweighted) and of the defect cubic
(which constrains `1−Z`, the leading deviation of the *unweighted* sum). It constrains
how `W_λ` distributes across the **multiplicity-heavy** partitions — a datum the
pointwise conditions leave free. Provenance: `wlambda_wstd_growth_bound_probe.py` +
witness (sibling thread #3548), exact-integer verified.

## Why the keystone should carry it — the μ/e ↔ binding cross-link

`W_λ` is the **single shared object** between the two open frontiers: the keystone's
**generation-selection (μ/e mass)** mechanism and **GAP-A-3/A-4 binding**. The new gate
ties them:

- On the binding side it is the provable core of a **GAP-A-3 result** (#3548): inverting
  the super-exponential `w_std` against extensive `B∝A` forces the brane-tower
  **level-selection `k(A)` to be logarithmic** (`k∝A` and `k∝`bond-count falsified
  scale-free, R²=0.67/0.49 vs log-type 0.88).
- On the keystone side it is a **new falsifiable test**: a candidate WRT(S³/2I) /
  `E_q(2)` q-Bessel index that reproduces C1/C2/C6 + the defect cubic but gives the
  wrong `w_std` growth class is **excluded** — even though it passes every current gate.

So a single geometric `W_λ` must simultaneously satisfy the μ/e gates *and* the
binding-side super-exponential growth. That is a stronger joint constraint than either
frontier alone, and it is the honest content of "the keystone and GAP-A-3 share `W_λ`."

## Honest scope — what is proved vs open

- **Verified (exact, k=3..10):** `w_std(k)` is super-exponential (the gate's content).
- **Lean/proof target:** a super-exponential lower bound on `E_Planch[f^{λ/(2,1)}]` — a
  self-contained combinatorial lemma (the natural next Lean piece; would upgrade the
  gate from "verified k≤10" to "proved"). Full conditional argument (`k(A)~log` from
  this core) is in the sibling binding thread, [PR #3548](https://github.com/litlfred/qou/pull/3548).
- **Still open (unchanged):** the geometric construction of `W_λ` itself (owner-gated
  q-series). This note adds a *test*, not a construction; it does **not** close the
  keystone, set a scale, or wire anything.

## Ledger action

Recorded as **necessary condition C8** on the `s5-so3-keystone` gate list. Any future
candidate index (WRT / q-Bessel) is to be checked against `w_std` super-exponential
growth alongside C1/C2/C6 + the defect cubic + `f_pn` bracket.
