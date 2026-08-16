---
# qou-k4f8
title: 'Dual certificate existence for the operator-selection LP: formalize first, then symbolic'
status: in-progress
type: task
priority: normal
created_at: 2026-08-16T12:50:00Z
updated_at: 2026-08-16T13:05:56Z
---

Follows `k4ul` (#5216, theorem proved) and `0tjt` (#5231, box shown
non-binding by the paper's own text). Those establish that
`operator_selection_lp` holds **given** a dual certificate. This bean asks
whether one exists.

## The question, stated exactly

`k4ul`'s hypotheses require `s : Fin d → R` with

```
s ≥ 0        and        ∀ j,  t j = y_0_star + Σᵢ sᵢ · G i j
```

`G` is the Frobenius Gram matrix `Gᵢⱼ = tr_M(bᵢbⱼ)`, hence **symmetric**, so in
vector form the second condition is

```
t = y₀ · 𝟙 + G s ,      s ≥ 0
```

— `d` equations in `d + 1` unknowns `(y₀, s)` with a sign constraint. Existence
is **not** automatic: it asks whether `t` lies in the cone `{y₀𝟙 + Gs : s ≥ 0}`,
`y₀ ∈ ℝ`. That is a genuine Farkas-type question about the substrate data.

## Method: formalize first, then compute

Per AGENTS.md. Do not start from numerics.

1. **Lean, statement.** Define
   `DualCertificateExists (t G) : Prop := ∃ y₀ s, (∀ i, 0 ≤ s i) ∧ ∀ j, t j = y₀ + Σᵢ s i * G i j`
   and prove the two reductions that make it checkable:
   - if `G` is invertible, `s = G⁻¹(t − y₀𝟙)`, so existence reduces to
     `∃ y₀, ∀ i, 0 ≤ (G⁻¹(t − y₀𝟙))ᵢ` — a one-parameter sign condition;
   - the certificate, once exhibited, discharges `k4ul`'s fields directly.
   Both are elementary and need no Farkas — Farkas would only be needed for the
   *converse* (non-existence ⇒ something), which is not wanted here.
2. **Symbolic.** For `n = 2` (`d = 2`) and `n = 3` (`d = 6`), build the NF basis
   of `H_n(q)`, compute `tᵢ = tr_M(bᵢ)` and `Gᵢⱼ = tr_M(bᵢbⱼ)` **symbolically in
   `q`**, not at a pinned `q₀`. Then evaluate the sign condition from step 1.
3. **Instantiate.** If a certificate exists for those `n`, supply it as a
   `OperatorSelectionLpContext` instance — that turns `k4ul` from conditional
   into an unconditional statement about the small cases.

## Why symbolic before numeric

A numeric check at `q₀` cannot distinguish "the certificate exists" from "the
certificate exists at this `q₀`". The proposition is stated for general `q`, and
the sign condition can change across `q`. This corpus has a `q-usage` QA axis
precisely because pinning `q` early hides that.

## Starting points

- `computations/aK_via_lp_dual_hecke_basis.py` + its witness
  `a-K-via-lp-dual-hecke-basis.witness.json` — the closest existing artifact,
  and it is **live**, not deprecated. Read before writing anything new.
- `computations/alpha-k-jones-markov-h3.witness.json`,
  `alpha-k-jones-markov-h4.witness.json` — Markov traces for `H₃`, `H₄`
  already computed. These may already contain `t` for `n = 3, 4`.
- `computations/_deprecated/symbolic-lp.py` — deprecated; check what replaced it
  before reusing.

`pyhecke` is **not importable** in this sandbox as of 2026-08-16, so the Hecke
machinery has to come from the checked-in computations or be rebuilt.

## Stage 1 DONE (2026-08-16) — the Lean is in place, sorry-free

`operator_selection_lp.lean` now carries the whole reduction. Compiled clean
against the pinned mathlib (zero errors, zero warnings, hence no `sorry`).

**The algebra was factored out first.** `sum_cost_mul_eq` is the dual
decomposition `Σⱼ tⱼxⱼ = y₀·n_target + Σᵢ sᵢ(Gx)ᵢ` over *raw data* — no order
on `R`, no sign hypotheses. Everything else is a corollary, including the
optimality bound the main theorem used to inline.

**The two reductions this bean asked for:**

1. `dualCertificateExists_of_left_inverse` — given `K` with
   `Σᵢ K k i · G i j = δₖⱼ`, the dual equation *determines* `s`:
   `s i = Σₖ (t k − y₀)·K k i`. So existence collapses to: **does some single
   scalar `y₀` make all `d` entries non-negative?** A `d`-dimensional
   feasibility question becomes a one-parameter search.

   Deliberately phrased with a *given* left inverse rather than `G⁻¹`: no
   invertibility API, no determinant, no `Matrix` import (`Data/Matrix/Defs`
   is **not** in the olean cache, though `Basic`/`Mul`/`NonsingularInverse`
   are). The symbolic stage supplies `K` explicitly and `hK` is checked by
   multiplication.

2. `OperatorSelectionLpContext.ofCertificate` — builds the class from data
   plus four checkable facts (`s ≥ 0`, the dual equation, the net constraint,
   Frobenius positivity, per-index complementary slackness) and **derives**
   `zero_gap` via `zero_gap_of_complementary_slackness`.

   Deriving it is the point. `zero_gap` is the one field that looks like the
   block's own conclusion, and hand-supplying it is exactly where the
   §3b-cond self-assuming instance would creep back in — the defect `k4ul`
   was filed for. A raw-data lemma is required here: a lemma assuming the
   class could never supply one of its own fields.

**Complementary slackness is the whole content of the gap.**
`zero_gap_iff_complementary_slackness` shows that for feasible `x`, attaining
the dual bound is *equivalent* to `∀i, sᵢ(Gx)ᵢ = 0` — each Frobenius
constraint inactive (`sᵢ = 0`) or tight (`(Gx)ᵢ = 0`). One equation in the
whole data becomes `d` independent scalar equations. That is what makes the
certificate checkable rather than merely stateable.

## What stage 2 must now produce

The Lean fixes the contract exactly. For `n = 2` (`d = 2`) and `n = 3`
(`d = 6`), symbolically in `q`:

- [ ] `t : Fin d → ℚ(q)` — `tᵢ = tr_M(bᵢ)` on the NF basis
- [ ] `G : Fin d → Fin d → ℚ(q)` — `Gᵢⱼ = tr_M(bᵢbⱼ)`
- [ ] `K` with `K·G = I`, **plus the product** as the witness of `hK`
- [ ] `s(y₀)ᵢ = Σₖ (tₖ − y₀)·K k i` as a rational function of `q` and `y₀`,
      and the set of `y₀` making all `d` entries `≥ 0` — **as a condition on
      `q`, not at a pinned `q₀`** (the sign condition can change across `q`;
      that is why the `q-usage` axis exists)
- [ ] `x*` and the per-index products `sᵢ·(Gx*)ᵢ`, which must all vanish

Stage 3 is then mechanical: feed those to `ofCertificate`.

## Still open

If **no** `y₀` works for some `q`, that is a content finding about the claimed
optimum — the proposition would be false there, not unproven. Farkas
(`qou/kl8z`) is still not needed for any of this; it would only be needed for
the converse direction, which nothing here asks for.
