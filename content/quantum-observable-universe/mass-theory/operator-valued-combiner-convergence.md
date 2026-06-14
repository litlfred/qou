<!-- Proposition (conditional on:
       conj:crystal-graph-realization (via the Wenzl A-operator class),
       prop:crystal-r-matrix-sub-lemma,
       prop:lr-coefficient-hecke). -->

**Proposition (operator-valued combiner convergence, conditional on
[`conj:crystal-graph-realization`](crystal-graph-realization.md) via the
Wenzl A-operator class).**
*Let $\beta_{\mathrm{atom}}$ be the canonical $A$-nucleon atomic braid in
$\mathbf{H}_{3A}(q)$, with inter-nucleon interfaces at the peel levels
$n_k = 3(A - k + 1)$. Write $\chi^\lambda_A := \chi^\lambda(\beta_{\mathrm{atom}})$
for the level-$A$ character. Then the iterated application of the
operator-valued [Sub-lemma 2.1](crystal-r-matrix-sub-lemma.md) — each peel
weighted by the [Littlewood–Richardson coefficient](lr-coefficient-hecke.md)
$c^\lambda_{\mu\nu}$ — assembles into a single convergent representation:
the value at level $A + 1$ is the LR-weighted value at level $A$,*

$$
  \boxed{\;\;
    \mathrm{cv}(A + 1) \;=\; w(A)\,\cdot\,\mathrm{cv}(A),
    \qquad A \ge 2,
  \;\;}
$$

*so that the character of an arbitrarily large atom is the deuteron
($A = 2$) base case accumulated through the LR-weight tower:*

$$
  \mathrm{cv}(2 + m) \;=\; \Bigl(\textstyle\prod_{j = 0}^{m - 1} w(2 + j)\Bigr)\,\cdot\,\mathrm{cv}(2),
  \qquad m \ge 0,
$$

*where $\mathrm{cv}(A)$ is the combiner value at peel level $A$ and $w(A)$
is the LR weight entering the peel $A \to A + 1$.*

## Categorical interpretation

The proposition is the **convergence content** of the operator-valued
Wenzl branching combiner: the atomic Markov trace
$\mathrm{tr}_M(\beta_{\mathrm{atom}}) = \sum_\lambda y_\lambda\,\chi^\lambda_A$
need not be recomputed at full strand count $3A$ for each isotope.
Instead it is *peeled* one nucleon at a time — each peel is a single
application of Sub-lemma 2.1, multiplying the running value by the
LR-weighted A-operator contribution of the newly attached nucleon block.
The recursion bottoms out at the deuteron, the smallest two-nucleon
interface, which is computed directly at $\mathbf{H}_6$. The "tower" of
weights $w(2), w(3), \dots$ is exactly the per-interface
[`def:wenzl-A-operator`](wenzl-A-operator.md) data, and the product form
exhibits the per-isotope binding tower as a telescoping accumulation
rather than an independent high-strand computation.

## Conditional-class hypothesis (CLAUDE.md §3b-cond)

The compiled Lean home is
[`QOU.BraidKnot.OperatorValuedCombiner`](../../../content/quantum-observable-universe/lean/QOU/BraidKnot/OperatorValuedCombiner.lean),
which axiomatises the combiner as a `class WenzlAOperator` carrying
`combinerValue`, `lrWeight`, and the `branching_recursion` field
(the one-step recursion above). The convergence theorem

```lean
theorem operator_valued_combiner_convergence
    [W : WenzlAOperator R q] :
    ∀ n : ℕ, W.combinerValue (n + 2) = iteratedCombinerValue W n
```

is proved by `Nat.rec` from that field, so it is **fully Lean-verified
modulo the `[WenzlAOperator R q]` instance hypothesis**. No instance is
provided: the missing instance — universal $A^\lambda_{\mu\nu}(I)$
extracts at $\mathbf{H}_{9+}$ — *is* the research-grade conjecture, and
the dependency cone reaches
[`conj:crystal-graph-realization`](crystal-graph-realization.md) through
[`prop:crystal-r-matrix-sub-lemma`](crystal-r-matrix-sub-lemma.md).

## Production wiring and verification

The recursion is realised in
[`canonical_tr_m_via_branching.py`](../../../folio-assistant/computations/canonical_tr_m_via_branching.py)
(`compute_tr_m_via_branching`), wired into the canonical mass table via
`--method branching` in
[`canonical_mass_table_extended.py`](../../../folio-assistant/computations/canonical_mass_table_extended.py):

- **$A = 2$ (deuteron)** runs the operator-valued branching end-to-end,
  agreeing with `markov_peel.tr_M_atomic` at $0.72$ ppb (Phase A
  baseline).
- **$A \ge 3$** delegates to the production native Hoefsmit kernel
  $\mathrm{tr}_M = \sum_\lambda y_\lambda\,\chi^\lambda$, which handles
  every $A$ — including the color-weighted $p$–$n$ interface that the
  symbolic `markov_peel` path cannot represent.

## Lean formalization

**Conditional theorem (Lean-verified modulo the
[`def:wenzl-A-operator`](wenzl-A-operator.md) class instance).** The
convergence recursion and its product unwinding hold for every commutative
ring $R$; the only unproved input is the existence of a concrete combiner
instance, which is the universal-extract conjecture documented in the audit
trail (`docs/audits/2026-06-02-subgoal-1-phase-a-baseline.md`).
