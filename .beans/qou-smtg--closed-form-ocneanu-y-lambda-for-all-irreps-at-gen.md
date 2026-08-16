---
# qou-smtg
title: Closed-form Ocneanu y_lambda for ALL irreps at general z (and at z_D)
status: todo
type: task
priority: normal
created_at: 2026-08-10T17:43:03Z
updated_at: 2026-08-16T12:56:32Z
---


## Why this exists

PR #4928 moved the corpus to convention D by re-issuing the symbolic `y_λ` root
with

    y_λ = [n-2k+1]_q / [2]_q^n     for λ = (n-k, k)
    y_λ = 0                        for ℓ(λ) ≥ 3

That form is **verified but not derived for general n**. What it actually
passes:

- both n=3 closed forms from `qou-u2jg`, and all three n=3 Markov conditions
  including the defining `tr(σ) = z_D`;
- `tr(1) = Σ_λ dim_λ · y_λ = 1` symbolically for n = 2..8.

What it does **not** have: a derivation from the Ocneanu/Markov structure at
general n, and no check of `tr(σ) = z_D` for n > 3. The two-row restriction is
consistent with `H_n/rad = TL_n`, but that identification is itself *measured*
(`qou-8iru`, n = 2..7, residual 1.34e-51), not proved. So a wrong weight at
some n ≥ 4 would currently be caught only by the normalisation, which is one
scalar equation per n and cannot separate the individual weights.

## What is already established

**Recursion A (consistency) — verified.** Because the Markov trace is a
consistent family, `tr_n|_{H_{n-1}} = tr_{n-1}`, and branching gives

    Σ_{λ = μ + □} y_λ^{(n)} = y_μ^{(n-1)}

Checked symbolically at n=3 → n=2 for both μ.

**n=2 and n=3 at GENERAL z, solved.**

    y_(2)   = (qz + 1)/(q² + 1)
    y_(1,1) = q(q - z)/(q² + 1)

    y_(3)     = (qz+1)(q³z+qz+1) / ( q³ [3]_q [2]_q )
    y_(2,1)   = (q-z)(qz+1)      / ( q  [3]_q )
    y_(1³)    = (z-q)(z(q²+1)-q³)/ ( q  [3]_q [2]_q )

The `y_(1³)` numerator is exactly the `qou-u2jg` factorisation
`y_(1³)(q²+1)(q⁴+q²+1) = q²(z-q)(z(q²+1)-q³)`, recovered independently here.

**The product structure is visible.** Each weight is a product of linear-in-`z`
factors over the cells of λ other than (1,1), over hook-length brackets — the
classic Ocneanu shape. The factors are indexed by cell **content** and are
shared across partitions:

| content c | factor |
|---|---|
| +1 | `(qz + 1)` |
| −1 | `(q - z)` |
| +2 | `(q³z + qz + 1)` |
| −2 | `z(q²+1) - q³` |

`(2,1)` carries exactly the `c=+1` and `c=−1` factors; `(3)` carries `+1,+2`;
`(1³)` carries `−1,−2`. Denominators are hook products: `(2,1)` has
`q[3]_q`, and `(3)`/`(1³)` both have `q^a [3]_q [2]_q`, matching
`∏_{cells}[h(i,j)]_q` up to a power of q that differs between them and needs
pinning.

## What was tried and does NOT work

**A content-only box weight in recursion B.** The Markov property gives

    Σ_{λ = μ + □} d(λ/μ) y_λ^{(n)} = z y_μ^{(n-1)}

Fixing `d(+1) = q`, `d(−1) = −q⁻¹` from n=2 (where they are forced) and
assuming `d` depends only on the box content makes the n=3 system
**inconsistent** — four equations in three unknowns with no solution. Solving
for `d(±2)` instead returns `z`-dependent rational functions
(`d(+2) = (q⁴z+q³+q)/(q³z+qz+1)`), which no genuine box weight can be. So
either `d` is not a function of content alone, or the single scalar equation per
μ underdetermines it and the partial trace must be taken properly over the
branching subspace rather than as one scalar. Do not retry the content-only
ansatz.

## The task

1. Derive the general-`n` Ocneanu weight in closed form at general `z`:
   identify the content → linear-factor map `f_c(z)` (the table above gives it
   for `|c| ≤ 2`), pin the hook-product denominator and the q-power, and prove
   it satisfies both recursions.
2. Specialise at `z_D = q³/(q²+1)` and **prove** that every `ℓ(λ) ≥ 3` weight
   vanishes identically — currently asserted from the n=3 case plus the TL
   identification, not proved for general n.
3. Check the specialisation reproduces `[n-2k+1]_q/[2]_q^n` on two-row λ, or
   correct the shipped root if it does not.
4. Verify numerically at n = 4,5,6 against the repo's own seminormal machinery
   (`chi_lambda_all_partitions_mpfr`, `_build_seminormal_matrices_mpf`) by
   testing `tr(xσ) = z·tr(x)` on random `x`, which is a per-weight check rather
   than a single normalisation scalar.

## Close condition

A closed form for `y_λ(q,z)` valid for all λ ⊢ n, all n in 2..12, with the
`z_D` specialisation proved to kill `ℓ(λ) ≥ 3`, verified against the seminormal
machinery at n ≥ 4, and the shipped symbolic root either confirmed or
regenerated from it. Formalize-first applies: the vanishing claim in step 2 is
a Lean target, alongside the existing `ConventionPinning` section.


---

## UPDATE 2026-08-16 — step 2 is PROVED. Steps 1, 3, 4 remain open.

**Step 2 of "The task" above** — *"Specialise at `z_D = q³/(q²+1)` and **prove**
that every `ℓ(λ) ≥ 3` weight vanishes identically — currently asserted from the
n=3 case plus the TL identification, not proved for general n"* — **landed in
PR #5217**, sorry-free, in
[`QOU/QBeta/WenzlWeightVanishing.lean`](../content/quantum-observable-universe/lean/QOU/QBeta/WenzlWeightVanishing.lean).

What was proved, and it is stronger than step 2 asked for:

- `schurPrincipal_eq_zero_iff` — the level-`r` principal specialisation
  vanishes **iff** `ℓ(λ) > r`. Quantified over **every** `YoungDiagram` and
  **every** level `r`; `n` does not appear in the statement.
- `wenzlLevel_conventionD` — convention D **is** Wenzl level `r = 2`, exactly
  (`Q^r = q⁴ = Q²` at `Q = q²`, `z_W = q·z_D`). An algebraic identity, proved.
- `conventionD_weight_eq_zero_iff` — the `r = 2` corollary: `y_λ = 0 ⟺ λ has
  ≥ 3 rows`.

The mechanism is a single cell: the numerator factor `1 − Q^{r+c(x)}` vanishes
exactly at content `c(x) = −r`, the cell `(r,0)` exists exactly when the diagram
has more than `r` rows, and Young diagrams are down-left closed so no other cell
can do it first. At `r = 2` that is `(2,0)`, of content `−2` — the TL row cap.

Non-vacuity is proved rather than asserted: the genericity hypothesis holds at
every positive `Q ≠ 1` (so at the substrate `Q = q₀² ≈ 1.232`), and
`discriminates_at_n_three` derives that `(1³)` dies while `(2,1)` survives.

### Read the conditionality before citing this

The proof is about `schurPrincipal`, the hook-content product. The bridge from
that formula to the **actual Ocneanu weight** is Wenzl (1988), which is an
external input — cited in #5217, and **axiomatised** in PR #5230 as the class
`IsOcneanuWeightSystem`. So the statement about the actual weight,
`conventionD_ocneanuWeight_eq_zero_iff_of_wenzl`, is *proved conditional on
Wenzl 1988*, not proved outright. Cite it that way. The route to unconditional
(formalising `H_n(q)` + the Ocneanu trace) is scoped in its own bean.

### What this bean still owns

Steps 1, 3 and 4 are untouched by #5217:

1. the general-`n` closed form at **general `z`** — the content → linear-factor
   map `f_c(z)`, the hook-product denominator, the q-power, and both
   recursions. #5217 proves vanishing *at* Wenzl's parameter; it does not
   derive the weights at arbitrary `z`.
3. checking the specialisation reproduces `[n−2k+1]_q/[2]_q^n` on two-row `λ` —
   the probe verifies this at `n = 2..7` but it is not proved.
4. the per-weight numerical verification at `n = 4,5,6` against the seminormal
   machinery via `tr(xσ) = z·tr(x)` on random `x`.

The "close condition" is therefore **not** met. Do not close this bean on the
strength of #5217.
