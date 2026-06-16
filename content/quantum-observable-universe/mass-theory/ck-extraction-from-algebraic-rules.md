*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**$c_k$ extraction from four algebraic reduction rules on the typed-$\mathbf{B}_3$ word.**

The $\mathfrak{Q}_\beta$ categorical precision ladder
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

See [Table 1](#tbl:ck-extraction-from-algebraic-rules-table1-data).

## The extraction function

The Lean module exports
```
noncomputable def ckFromReduction (q : ℝ) : ℕ → ℝ
```
returning the closed-form scalar value that Rules 1-4 jointly
determine at order $\varepsilon^{2k}$ on the canonical typed-$\mathbf{B}_3$
word:

See [Table 2](#tbl:ck-extraction-from-algebraic-rules-table2-data).

## Per-order agreement

The Lean theorems
`ckFromReduction_eq_c1`, $\ldots$, `ckFromReduction_eq_c4` discharge each
agreement equality by `rfl` against the inline coefficients used in
`N1_factor`, $\ldots$, `N4_factor` of the precision ladder.

The synthesis theorem `ckFromReduction_matches_ladder` records the
joint statement under all four class instances.

## Why this reframing matters

The earlier framing (alternating Kashiwara $\times$ Jones at even/odd $k$)
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

- Replace the `True` ansatz fields with the substantive matrix
  identities they encode (`yb_cubic` $\leftarrow$ Hoefsmit YB cubic; `hecke_quad`
  $\leftarrow$ `hoefsmit_sigma{0,1}_hecke_quadratic`).
- Discharge `QYoungSymmetrizers 3 q` via the Mathlib Iwahori-Hecke
  module (when complete) or via the explicit $H_3$ idempotent table.
- Formalise the GB/jet normal-form procedure for $k = 1, 2$
  (where the reduction is short enough to discharge by
  case-analysis on the typed-$\mathbf{B}_3$ word structure).
- Extend the extraction to $k \geq 5$ — the simple alternating
  Kashiwara $\times$ Jones pattern breaks at $c_5, c_6$ per the open R&D in
  [`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder);
  the four-rule reframing may identify which rule's discharge needs
  enrichment (likely Rule 2 + Rule 4) to capture multi-link Jones
  contributions.
