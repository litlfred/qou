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
coupling). The claim recorded here is that these closed forms
are **derivable outputs** of four algebraic reduction rules, not
phenomenological identifications.

## The four reduction rules

See [Table 1](#tbl:ck-extraction-from-algebraic-rules-table1-data).

## The extraction function

The extraction function $k \mapsto c_k^{\mathrm{red}}(q)$ returns the
closed-form scalar value that Rules 1-4 jointly
determine at order $\varepsilon^{2k}$ on the canonical typed-$\mathbf{B}_3$
word:

See [Table 2](#tbl:ck-extraction-from-algebraic-rules-table2-data).

## Per-order agreement

For $k = 1, \ldots, 4$ the extracted value agrees with the coefficient
used in the corresponding rung factor of the precision ladder. The agreement
holds by definition: $c_k^{\mathrm{red}}$ is given by the same closed forms
the ladder uses, so this step checks consistency and does not by itself derive
the closed forms from the rules.

The joint statement is recorded conditionally on all four rules, taken as
hypotheses.

## Significance of the reframing

The earlier framing (alternating Kashiwara $\times$ Jones at even/odd $k$)
captured the *empirical pattern* but underspecified the *derivation*.
The four-rule reframing shifts the conjectural content from
"the alternation happens" to **"the four reduction rules jointly
determine the unique normal form"** — which is checkable rule by rule:

- Rules 1, 3 are already discharged for $V_{(2,1)}$ at $H_3(q)$ by the
  Hoefsmit matrix theorems.
- Rule 2 (Hecke idempotents) is expected to follow from the standard
  Iwahori-Hecke decomposition.
- Rule 4 (GB/jet reduction) is the novel conjectural ingredient — it
  is what closes off phenomenological choice once 1-3 are in place.

Taking each rule as a **separate hypothesis** to discharge turns the
$c_k$ extraction into a structured programme of separate verifications
rather than a single open conjecture.

## What remains open

- Connect Rules 1 and 3 to the substantive matrix identities they
  encode (Rule 1 $\leftarrow$ the Hoefsmit Yang–Baxter cubic; Rule 3
  $\leftarrow$ the Hoefsmit Hecke quadratic for $\sigma_0, \sigma_1$); as
  stated, these two rules are placeholders that do not yet carry those
  identities.
- Establish Rule 2 ($q$-Young symmetrizers at $n = 3$) from the
  Iwahori-Hecke decomposition or from the explicit $H_3$ idempotent table.
- Establish the GB/jet normal-form procedure (Rule 4) for $k = 1, 2$
  (where the reduction is short enough to discharge by
  case-analysis on the typed-$\mathbf{B}_3$ word structure).
- Extend the extraction to $k \geq 5$ — the simple alternating
  Kashiwara $\times$ Jones pattern breaks at $c_5, c_6$, an open point recorded
  in [$\mathfrak{Q}_\beta$ categorical-derivation precision ladder](#prop:q-beta-categorical-precision-ladder);
  the four-rule reframing may identify which rule's discharge needs
  enrichment (likely Rule 2 + Rule 4) to capture multi-link Jones
  contributions.
