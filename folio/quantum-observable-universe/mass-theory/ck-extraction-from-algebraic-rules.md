**$c_k$ extraction from four algebraic reduction rules on the typed-$\mathbf{B}_3$ word.**

The $\mathfrak{Q}_\beta$ categorical precision ladder
([$\mathfrak{Q}_\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder))
displays per-rung coefficients

$$
  c_1 = b, \quad c_2 = b^2, \quad c_3 = -2, \quad
  c_4 = c_3 \cdot b^4 = -2 b^4, \quad
  c_5 = -(b^2 + \tfrac{1}{2})
$$

with $b = \sqrt{q^4+q^2+1}/(q^2+1)$ (Hoefsmit $V_{(2,1)}$ off-diagonal
coupling). The claim made here is that these closed forms
are **derivable outputs** of four algebraic reduction rules, not
phenomenological identifications.

## The four reduction rules

See [Table 1](#tbl:ck-extraction-from-algebraic-rules-table1-data).

## The extraction function

The extraction is a function $k \mapsto c_k(q)$, real-valued at real
$q$, returning the closed-form scalar value that Rules 1-4 jointly
determine at order $\varepsilon^{2k}$ on the canonical typed-$\mathbf{B}_3$
word:

See [Table 2](#tbl:ck-extraction-from-algebraic-rules-table2-data).

## Per-order agreement

For $k = 1, \ldots, 4$ the extracted value equals the coefficient the
precision ladder uses at order $k$. **That agreement holds by
definition:** the extraction returns, at each order, the same
expression the ladder writes inline, so the four equalities are
identities of definitions and are not an independent derivation of
$c_1, \ldots, c_4$. The joint statement assumes all four reduction
rules as hypotheses.

## Significance of the reframing

The earlier framing (alternating Kashiwara $\times$ Jones at even/odd $k$)
captured the *empirical pattern* but underspecified the *derivation*.
The four-rule reframing shifts the conjectural content from
"the alternation happens" to **"the four reduction rules jointly
determine the unique normal form"** — which is checkable rule by rule:

- Rules 1, 3 are already discharged for $V_{(2,1)}$ at $H_3(q)$ by the
  Hoefsmit matrix theorems.
- Rule 2 (Hecke idempotents) reduces to the standard
  Iwahori-Hecke decomposition.
- Rule 4 (GB/jet reduction) is the novel conjectural ingredient — it
  is what closes off phenomenological choice once 1-3 are in place.

Stating each rule as a separate hypothesis makes each one a separate
statement to prove, which turns the $c_k$ extraction into a list of
four checkable steps rather than a single open conjecture.

## What remains open

- State the content of Rules 1 and 3, which are at present carried as
  hypotheses with no content: the Yang–Baxter cubic and the Hecke
  quadratic of the Hoefsmit matrices of $\sigma_1, \sigma_2$ on
  $V_{(2,1)}$. The matrix identities themselves are proved; the
  hypotheses of the extraction do not yet say them.
- Prove Rule 2, the existence of the $q$-Young symmetrisers of
  $H_3(q)$, from the Iwahori–Hecke decomposition or from the explicit
  $H_3$ idempotent table.
- Prove the GB/jet normal-form procedure for $k = 1, 2$
  (where the reduction is short enough to discharge by
  case-analysis on the typed-$\mathbf{B}_3$ word structure).
- Extend the extraction to $k \geq 5$ — the simple alternating
  Kashiwara $\times$ Jones pattern breaks at $c_5, c_6$, an open point recorded
  in [$\mathfrak{Q}_\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder);
  the four-rule reframing may identify which rule's discharge needs
  enrichment (likely Rule 2 + Rule 4) to capture multi-link Jones
  contributions.
