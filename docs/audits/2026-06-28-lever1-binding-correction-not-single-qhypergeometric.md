# Lever-1 fibre kernel, Stage 6: the binding correction tower is not a single low-order q-hypergeometric element

**Date:** 2026-06-28
**Bean:** `z2bn` (Lever 1 [FOCUS] — fibre q-difference kernel `R(q,x)` for the binding genfun)
**Compute:** [`computations/substrate/lever1_binding_habiro_single_element_test.py`](../../computations/substrate/lever1_binding_habiro_single_element_test.py)
**Witness:** [`computations/substrate/lever1-binding-habiro-single-element-test.witness.json`](../../computations/substrate/lever1-binding-habiro-single-element-test.witness.json)
**Serves:** `kehn` (Q_β / m_n c_k closure via a Habiro element), `s5bb` (the Habiro-element keystone blocker)
**Precedes:** [`2026-06-27-lever1-qinvolution-cyclotomic-kernel.md`](2026-06-27-lever1-qinvolution-cyclotomic-kernel.md) §"Next decidable steps" item 1.

## What was already established (Stages 1–5)

The binding selection-rule period `S(m) = Σ_{λ⊢m} dim_q(λ)` (with `lw(c) = S(c+1)/(c+1)`) is:

- the **q-involution skeleton** `S(m) = S(m−1) + [m−1]_q·S(m−2)`, exact at the calibration seed
  (`m ≤ 3`), `q=1` → the involution numbers `1,1,2,4,10,26,76,…`;
- dressed by a **cyclotomic (Habiro) correction** `D(m) := S(m) − (S(m−1) + [m−1]_q·S(m−2))` with a
  universal `(q−1)²` prefactor and `Φ_d` factor tower (Stage 1);
- **not** q-holonomic of small order (≤3) and bidegree — no finite low-order q-difference operator
  reproduces it (Stages 3–4);
- with an explicit q-EGF `Ŝ(z) = Σ S(m) z^m/[m]_q! = exp(Σ_m L_m z^m)`, a q-Gaussian
  (`L_1,L_2 → 1,½` at `q=1`) plus a suppressed Habiro tail `L_{≥3} ∼ (q−1)^{2⌊(m−1)/2⌋}` with
  cyclotomic denominators including the `Φ₄ = ζ₄` residue (Stage 5).

The single stated next-decidable step was: *fit the `D(m)` cyclotomic cofactors to a **single**
q-hypergeometric / Habiro element (contiguity-ratio template), verified on held-out `m`.* This audit
executes that step.

## The test (decidable, no fit to a physical target)

A sequence `T(m)` is **q-hypergeometric** iff its ratio `T(m+1)/T(m)` is a *fixed* rational function
`R(q, q^m)` — equivalently there exist fixed bivariate Laurent polynomials `A(q,X), B(q,X)`
(`X := q^m`), of bounded bidegree, with

```
  A(q, q^m)·T(m+1) + B(q, q^m)·T(m) = 0   for all m.
```

This is **homogeneous-linear** in the coefficients of `A, B`. The probe fits the nullspace on three
consecutive training pairs and then **verifies each candidate relation on the held-out indices**
(never used in the fit) — the Stages 3–4 guess-and-verify methodology applied to the order-1
(q-hypergeometric) case, on the correction towers rather than on `S(m)` itself. Two towers tested:
the additive `D(m)` (nonzero `m = 4..10`) and the log-EGF `L_m` (nonzero `m = 1..10`). The literal
audit contiguity template `r_k = −q^k/[(1−q^{k+1})(1−a q^k)]` (one parameter `a`) is tested
separately: solve `(a, C)` from the first two ratio pairs, verify the rest.

Symbolic, exact in `q` (sympy 1.14), `S(m)` up to `m = 10` via the shared cached `young_qdim`.

## Result — negative, and sharp

| tower | bidegree (q±dq, X≤dX) | unknowns / constraints | train nullspace | held-out survivors |
|---|---|---:|---:|---:|
| `D(m)` | (±1, 1) | 12 / 66 | 0 | 0 |
| `D(m)` | (±2, 2) | 30 / 87 | 0 | 0 |
| `D(m)` | (±2, 3) | 40 / 102 | 0 | 0 |
| `D(m)` | (±3, 3) | 56 / 108 | 0 | 0 |
| `L_m` | (±1, 1) | 12 / 41 | 0 | 0 |
| `L_m` | (±2, 2) | 30 / 53 | 0 | 0 |
| `L_m` | (±2, 3) | 40 / 59 | 0 | 0 |
| `L_m` | (±3, 3) | 56 / 65 | 3 | **0** |
| contiguity template (1 param `a`) | — | — | — | **0** (both towers) |

At every **strongly over-determined** bidegree the training nullspace is **empty** — no order-1
q-difference relation even fits the training window. The only nonzero nullspace (`L_m` at the
near-square (±3, 3), 56 unknowns vs 65 constraints — effectively under-constrained) is a fit
artifact: **all three candidates fail the held-out test**. The literal one-parameter contiguity
template fails held-out for both towers.

## Interpretation and scope (AGENTS.md refuted-claim discipline)

- **(a) scope-limited negative** on the *single-low-order-q-hypergeometric* ansatz: neither the
  additive `D(m)` nor the log-EGF `L_m` tower is the coefficient sequence of a single ₂φ₁-type
  element of bidegree up to (q±3, X≤3), order 1. This **sharpens** the Stages 3–4 finding: not only
  is `S(m)` not low-order q-holonomic, its Habiro *correction* towers are not single low-order
  q-hypergeometric elements either.
- **Not a (b) structural exclusion.** No proved invariant forbids a *higher-order* or
  *cyclotomic-completion* element. The Habiro-ring class is **not** refuted — the test constrains the
  element's order/shape (the bounded-bidegree order-1 window is empty), exactly as the formalize-
  first discipline intends: it prunes the cheap hypothesis so the search narrows to the genuine
  cyclotomic-completion object.

This is consistent with — and reinforces — the Stage 5 picture: the explicit binding-side object is
the q-Gaussian `exp(z + L₂ z²)` dressed by a genuinely non-q-hypergeometric Habiro tail. The exact
data (`D(m)`, `L_m` symbolic in `q`) remains the parameter-free target any candidate kernel must
reproduce.

## What this does and does not change

- **Does not wire anything**; no production consumer touched; no tier change.
- **Does not** touch the owner-gated geometric side (the `λ_SW`-holonomy keystone / `tr B`); this is
  the algebraic correction-tower face, with exact data.
- **Does** close off "the binding correction is a single low-order ₂φ₁" as a productive hypothesis,
  leaving the higher-order / cyclotomic-completion element (the `kehn` / `s5bb` shared object) as the
  remaining live target.

## Next decidable step (not run here)

The element, if it exists in closed form, is **not** order-1 q-hypergeometric — so the productive
remaining attack is the **cyclotomic-expansion** form directly: expand `D(m)` (or the correction
generating function `C(z) = Σ_{m≥3} L_m z^m`) in the Habiro basis `(q;q)_n = ∏_{k≤n}(1−q^k)` and test
whether the basis coefficients stabilise / follow a single rule across `m` (the canonical Habiro-ring
fingerprint), rather than searching for a finite q-difference operator that Stages 3–6 have now shown
does not exist at low order.

## Cross-reference — the merged Hahn–Exton q-Bessel claim (#3000), re-scoped

PR #3000 (merged to `main` 2026-06-28, same bean `z2bn`) adds to
`content/quantum-observable-universe/lean/QOU/QBeta/QBesselContiguityRecurrence.lean` a
`lever1_habiro_closed_form` theorem plus a docstring asserting that the lever-1 correction `D(m)`
*"contiguity is governed identically by the Hahn–Exton q-Bessel ratio … two localizations of the same
q-difference operator."*

- **The Lean theorem is sound and not in dispute.** `lever1_habiro_closed_form` is a *conditional*
  (it assumes the q-Bessel recurrence `D(k+1)·((1−q^{k+1})(1−a q^k)) = −q^k·D(k)` as a hypothesis
  `hrec` and concludes the product form). It is a sorry-free alias of `qbessel_coeff_closed_form`; it
  does **not** assert that `D(m)` actually satisfies that recurrence.
- **The docstring's identity claim is over-scoped — refuted by this Stage-6 probe.** The probe tests
  exactly that recurrence as the *literal contiguity template* `r_k = −q^k/[(1−q^{k+1})(1−a q^k)]`
  (one parameter `a`), and it **fails held-out**: no single `a` fit on `m=4,5` reproduces `m=6,7,8`.
  Stages 7–9 add that `D(m)` is a product of **pairwise-coprime irreducible** cores (not a single
  q-hypergeometric element), and the merged 2026-06-20 Hahn–Exton audit independently *structurally*
  excludes the bare Hahn–Exton ratio for the parallel `c_k` (`r₂ = +2` in the forbidden gap).
- **Re-scope (per the AGENTS.md (a)/(b) discipline):** the Hahn–Exton form is a correct
  **shared-Habiro-ring-class analogy** (both objects live in the cyclotomic completion, with `ζ₄`
  residues), **not** a literal contiguity identity for `D(m)`. The owner-merged conditional theorem
  stands; its docstring should be read as the ring-class connection, not as "`D(m)` satisfies the
  single-parameter q-Bessel recurrence." A docstring correction on `QBesselContiguityRecurrence.lean`
  is the clean follow-up (held pending owner direction, since #3000 is owner-authored and merged).
