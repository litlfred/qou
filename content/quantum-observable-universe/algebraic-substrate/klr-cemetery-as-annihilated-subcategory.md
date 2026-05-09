## Statement

**Theorem (conditional on
[`prop:crystal-graph-realization-stable-states`](#prop:crystal-graph-realization-stable-states)
+ [`prop:observation-frame`](#prop:observation-frame)).**
*Let $\mathcal{C}_n$ be the categorified $R_n^\Lambda$-module
category from [`prop:crystal-graph-realization-stable-states`](#prop:crystal-graph-realization-stable-states),
and let*

$$
  \tau : \bigoplus_{n \geq 0} \mathcal{C}_n \;\longrightarrow\; \mathbf{f}^-_{\mathbb{Z}[v, v^{-1}]}
$$

*be the Observation Frame functor (decategorification via the split
Grothendieck group, taking the graded Euler characteristic). Define
the **cemetery subcategory***

$$
  \mathcal{Z}_n \;:=\; \ker(\tau \restriction \mathcal{C}_n)
   \;=\; \bigl\{ M \in \mathcal{C}_n : [M]_\tau = 0 \bigr\}.
$$

*Then:*

1. *$\mathcal{Z}_n$ is a **localizing Serre subcategory** of
   $\mathcal{C}_n$ (closed under sub-objects, quotients, and
   extensions).*
2. *$\mathcal{Z}_n$ consists exactly of the **homologically acyclic
   complexes** in $\mathcal{C}_n$ — modules whose alternating sum of
   graded multiplicities cancels.*
3. *The cemetery group **emerges**: it is not posited; it is the
   kernel of the decategorification functor $\tau$.*

## Algorithmic consequence — kill switch

When the Gröbner-Shirshov reduction engine, running as a Kashiwara
crystal-graph traversal per [`prop:crystal-graph-realization-stable-states`](#prop:crystal-graph-realization-stable-states),
applies a sequence of operators $\tilde e_{i_1} \tilde e_{i_2} \cdots$
to an ansatz state $M$, it can detect entry into $\mathcal{Z}_n$ by
checking whether the partial result has zero graded Euler
characteristic:

$$
  M' \in \mathcal{Z}_n
    \quad \iff \quad
    [M']_\tau = 0 \in \mathbf{f}^-_{\mathbb{Z}[v, v^{-1}]}.
$$

If detected, the branch is **instantly truncated** — no algebraic
cancellations need be computed because $\tau$ will map the entire
branch to zero downstream. This is the **physical interpretation
of the cemetery group**: it is the locus of decoupled / non-observable
states, by the categorical structure of observation.

## Proof

**Step 1 — Serre subcategory.** $\tau$ is exact (preserves short
exact sequences) by construction (it is a Grothendieck-group functor).
The kernel of any exact functor is closed under sub-objects, quotients,
and extensions; this is a standard categorical fact (Gabriel 1962,
*Des catégories abéliennes*, §III.1).

**Step 2 — homologically acyclic complexes.** A module $M \in
\mathcal{C}_n$ is in $\ker(\tau)$ iff its image in
$K_0(\mathcal{C}_n)$ (the split Grothendieck group) is zero.
Equivalently, viewing $M$ as a complex, its alternating sum of
graded multiplicities vanishes — this is the categorical
characterisation of homological acyclicity for the relevant abelian
category.

**Step 3 — emergence.** $\mathcal{Z}_n$ is constructed entirely from
$\tau$ and $\mathcal{C}_n$; nothing is added by hand. The cemetery
group is, by definition, the kernel of decategorification —
**this is the proposition's content**.

**Step 4 — kill-switch correctness.** If the GS engine truncates a
branch upon entering $\mathcal{Z}_n$, the final $\tau$-evaluated
output is unchanged: the truncated branch would have contributed
$\tau(\text{anything below}) = 0$ regardless. So the kill-switch
preserves correctness while bypassing potentially long algebraic
cancellation computations.

$\square$

## Cross-references

* [`prop:crystal-graph-realization-stable-states`](#prop:crystal-graph-realization-stable-states)
  — the KLR machinery defining $\mathcal{C}_n$ and the crystal operators
* [`prop:observation-frame`](#prop:observation-frame)
  — the $\tau$ functor (graded Euler characteristic / split
  Grothendieck-group decategorification)
* [`prop:atomic-mass-gb-nf`](#prop:atomic-mass-gb-nf)
  — the GS engine that consumes the kill-switch
* [`prop:confinement-as-z-grading`](#prop:confinement-as-z-grading)
  — companion grading-bound filter

## References

* M. Khovanov, A. D. Lauda. *A diagrammatic approach to
  categorification of quantum groups I.* Representation Theory **13**
  (2009).
* J. Brundan, A. Kleshchev. *Blocks of cyclotomic Hecke algebras and
  Khovanov–Lauda algebras.* Inventiones mathematicae **178** (2009).
* P. Gabriel. *Des catégories abéliennes.* Bull. Soc. Math. France
  **90** (1962), 323–448.
