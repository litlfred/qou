**Per-Wedderburn-block $c_5/c_6$ scaffolding for the
$Q_\beta$ precision-ladder investigation.**

The simple alternating Kashiwara $\times$ Jones pattern from $c_3 = -2$
does **not** extend to $c_5, c_6$: empirically $c_5 \approx -395$
and $c_6 \approx -45485$, 50–3000$\times$ off any simple multi-link Jones
candidate (see
[`rem:multi-link-jones-q1-extension`](#rem:multi-link-jones-q1-extension)).

## Status: open R&D — no known non-trivial per-block decomposition rule

The $\dim_q^2$ weighting hypothesis below was the original scaffolding
direction. The 2026-05-19 audit ([`per-block-ck-extraction-rule.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-19-per-block-ck-extraction-rule.md))
showed it is **falsified** at $c_3 = -2$: $\sum_\lambda \dim_q^2 \cdot c_3^{(\lambda)}$
under the per-block LO $\varepsilon^1$ pattern $(-2, -1, -2)$ gives
$-8$, not $-2$. A $y_\lambda$-weighted uniform-rule alternative ALSO
fails at $q_0$ across all $c_k$ tested (since $\sum_\lambda y_\lambda(q_0) \neq 1$;
verified in `qbeta_per_block_uniform_rule_verify.py`). With
normalised weights the rule becomes tautological.

**Conclusion: there is currently NO known non-trivial uniform-per-block
decomposition rule for $c_k$ consistent at $q_0$.** The per-block
structure that IS real operates at the $\chi_\lambda$-character level
(LO $\varepsilon^1 = (-2, -1, -2)$ pattern in
[`rem:per-block-hopf-jones-absorption-pattern`](#rem:per-block-hopf-jones-absorption-pattern)),
not at the precision-ladder coefficient level.

The original $\dim_q^2$ hypothesis is retained below as **falsified
working hypothesis** for record-keeping; the substantive next direction
is the Khovanov-Rozansky / KLR-canonical-basis route (Path 2 of
[`2026-05-19-qbeta-ladder-closure-path.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-19-qbeta-ladder-closure-path.md)),
which operates at the link-Markov-closure level rather than per-block.

## Original (falsified) working hypothesis

Per the open R&D pointer in
[`rem:multi-link-jones-q1-extension`](#rem:multi-link-jones-q1-extension)
and [`rem:h3-hecke-idempotents`](#rem:h3-hecke-idempotents):

$$
  c_k(q_0) \;=\;
  \sum_{\lambda \vdash 3}\; \dim_q^2(V_\lambda) \cdot c_k^{(\lambda)}(q_0),
  \quad k \in \{5, 6\} \quad \text{(FALSIFIED)}
$$

where $c_k^{(\lambda)}(q)$ are per-block scalar functions of $q$,
extracted at order $\varepsilon^{2k}$ of the per-irrep $\tau_M$
expansion.

| block | $\dim_q^2$ at $q_0$ | $c_5^{(\lambda)}$ | $c_6^{(\lambda)}$ |
|:---:|:---:|:---:|:---:|
| $V_{(3)}$ | $1$ | — | — |
| $V_{(2,1)}$ | $(q + q^{-1})^2 \approx 3.61$ | — | — |
| $V_{(1,1,1)}$ | $1$ | — | — |

The — values are the **open R&D content** this scaffolding awaits.

## What this block provides

Lean module `QOU.BraidKnot.per_wedderburn_block_c5_c6`:

1. Six per-block contribution functions
   `c{5,6}_from_V{3,21,111} : ℝ → ℝ` (currently `0` placeholders).
2. Two weighted-sum aggregators
   `c{5,6}_total_weighted q : ℝ` computing
   $\sum_\lambda \dim_q^2 \cdot c_k^{(\lambda)}$.
3. A `PerWedderburnBlockC5C6 q` class encoding the residual of the
   weighted sum against the empirical target (explicit-residual
   pattern), with `c{5,6}_residual_eq_zero` fields asserting they
   vanish at substrate $q$.
4. A `defaultPerWedderburnBlockC5C6` instance — a deliberate
   **ansatz** (six $0$ contributions $\to$ both residuals trivially
   $0$) awaiting the substantive probe content.

## Concrete next-probe path

A Python probe `probe_per_wedderburn_block_ck.py` (open) would:

1. Extend the existing Wenzl-bridge $y_\lambda$ infrastructure to
   $\varepsilon^{10}, \varepsilon^{12}$ via per-irrep $\tau_M$
   evaluations on $V_{(3)}, V_{(2,1)}, V_{(1,1,1)}$.
2. Solve for $c_k^{(\lambda)}(q_0)$ at $k = 5, 6$ per block from the
   weighted-sum equation against empirical $c_5, c_6$.
3. Identify whether the resulting per-block values match known
   categorical scalars (Hoefsmit $b^k$ + Jones at $q=1$ extensions,
   or new categorical inputs).

If the working hypothesis holds, the per-block formulae substantively
discharge the `PerWedderburnBlockC5C6` class instance and the
precision-ladder extension naturally extends to $N = 6$.

## Status

**Open R&D recorded as Lean scaffolding.** The class hook lets
downstream theorems take
`[PerWedderburnBlockC5C6 q]` as an explicit hypothesis; once the
probe lands a substantive instance, the auto-elaboration picks it up
without changes to the surrounding API.
