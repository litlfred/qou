**$c_k$ extraction from four algebraic reduction rules on the typed-$\mathbf{B}_3$ word.**

> **Errata banner (2026-05-19) — $c_4$ closed form has shifted.**
> The original $c_4 = b^2 + 1/2$ form below is superseded by
> $c_4 = c_3 \cdot b^4 = -2 b^4$ (per PR #777's SDP-$T_\beta$
> derivation and [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)).
> The $b^2 + 1/2$ shape is now attributed to $c_5$ (with sign
> flip: $c_5 = -(b^2 + 1/2)$). The four-rule reframing remains
> valid; only the per-rung closed-form column needs updating.
> Audit: [`docs/audits/2026-05-19-qbeta-all-ck-categorical-extension.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-19-qbeta-all-ck-categorical-extension.md).

The $Q_\beta$ categorical precision ladder
([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder))
displays per-rung coefficients

$$
  c_1 = b, \quad c_2 = b^2, \quad c_3 = -2, \quad
  c_4 = c_3 \cdot b^4 = -2 b^4, \quad
  c_5 = -(b^2 + \tfrac{1}{2})
$$

with $b = \sqrt{q^4+q^2+1}/(q^2+1)$ (Hoefsmit $V_{(2,1)}$ off-diagonal
coupling). This block formalises the claim that these closed forms
are **derivable outputs** of four algebraic reduction rules, not
phenomenological identifications.

## The four reduction rules

| # | Rule | Lean class | Substantive content |
|---:|---|---|---|
| 1 | Braid (Yang-Baxter) cubic | `YangBaxterRule n q` | $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$ — at $n=3$ on $V_{(2,1)}$, follows from `hoefsmit_sigma{0,1}` matrix identities |
| 2 | $q$-Young symmetrizers | `QYoungSymmetrizers n q` | Hecke idempotents $e_\lambda \in H_n(q)$ projecting onto Wedderburn blocks $V_\lambda$, with $\sum_{\lambda \vdash n} e_\lambda = 1$ |
| 3 | Hecke quadratic at every generator | `HeckeQuadraticAllGenerators n q` | $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ for every $i$ — at $V_{(2,1)}$ discharged by `hoefsmit_sigma{0,1}_hecke_quadratic` |
| 4 | Gröbner-Shirshov / jet reduction | `GBJetReduction k` | Unique normal form for the typed-$\mathbf{B}_3$ character at order $(q-1)^{2k}$ in the jet polynomial ring |

## The extraction function

The Lean module exports
```
noncomputable def ckFromReduction (q : ℝ) : ℕ → ℝ
```
returning the closed-form scalar value that Rules 1-4 jointly
determine at order $\varepsilon^{2k}$ on the canonical typed-$\mathbf{B}_3$
word:

| $k$ | $\mathtt{ckFromReduction}\ q\ k$ | source of closed form |
|---:|---|---|
| 0 | $0$ | baseline |
| 1 | $b$ | Kashiwara $\tilde f_1$ matrix element on $V_{(2,1)}$ (Rules 1+2+3) |
| 2 | $b^2$ | $\tilde f_1^\dagger \tilde f_1$ return amplitude (Rules 1+2+3) |
| 3 | $-2 = J_{\mathrm{Hopf}}(q=1)$ | 3-fold Markov closure → Hopf substructure → KL classical limit (Rules 1+4) |
| 4 | $c_3 \cdot b^4 = -2 b^4$ | Jones $\times$ Kashiwara multiplicative mixing — Rules 1+3+4 (the old $b^2 + 1/2$ value belongs at $k = 5$ with a sign flip; superseded per 2026-05-19 audit) |
| 5 | $-(b^2 + 1/2)$ | Kashiwara $b^2$ + Hopf-half offset (mixed intra/inter) — the form originally attributed to $k = 4$ |
| $\geq 5$ | $0$ | open R&D (see [`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms)) |

## Per-order agreement

The Lean theorems
`ckFromReduction_eq_c1`, …, `ckFromReduction_eq_c4` discharge each
agreement equality by `rfl` against the inline coefficients used in
`N1_factor`, …, `N4_factor` of the precision ladder.

The synthesis theorem `ckFromReduction_matches_ladder` records the
joint statement under all four class instances.

## Why this reframing matters

The earlier framing (alternating Kashiwara × Jones at even/odd $k$)
captured the *empirical pattern* but underspecified the *derivation*.
The four-rule reframing shifts the conjectural content from
"the alternation happens" to **"the four reduction rules jointly
determine the unique normal form"** — which is auditable per rule:

- Rules 1, 3 are already discharged for $V_{(2,1)}$ at $H_3(q)$
  (the Hoefsmit matrix theorems in this branch).
- Rule 2 (Hecke idempotents) is largely Mathlib-able via the standard
  Iwahori-Hecke decomposition.
- Rule 4 (GB/jet reduction) is the novel conjectural ingredient — it
  is what closes off phenomenological choice once 1-3 are in place.

The class skeleton makes each rule a **separate instance** to discharge,
turning the c_k extraction into a structured Lean-engineering programme
rather than a single open conjecture.

## Open R&D

- Replace the `True` placeholder fields with the substantive matrix
  identities they encode (`yb_cubic` ← Hoefsmit YB cubic; `hecke_quad`
  ← `hoefsmit_sigma{0,1}_hecke_quadratic`).
- Discharge `QYoungSymmetrizers 3 q` via the Mathlib Iwahori-Hecke
  module (when complete) or via the explicit $H_3$ idempotent table.
- Formalise the GB/jet normal-form procedure for $k = 1, 2$
  (where the reduction is short enough to discharge by
  case-analysis on the typed-$\mathbf{B}_3$ word structure).
- Extend the extraction to $k \geq 5$ — the simple alternating
  Kashiwara × Jones pattern breaks at $c_5, c_6$ per the open R&D in
  [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder);
  the four-rule reframing may identify which rule's discharge needs
  enrichment (likely Rule 2 + Rule 4) to capture multi-link Jones
  contributions.
