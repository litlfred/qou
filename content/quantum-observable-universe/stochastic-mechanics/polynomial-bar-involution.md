**Proposition (polynomial bar-involution).**

Let $R$ be a commutative ring and $R[X]$ its polynomial ring in one indeterminate. The map

$$
\overline{(\cdot)} \colon R[X] \to R[X], \qquad p(X) \mapsto p(-X)
$$

is a ring involution. Under this bar:

- the indeterminate $X$ is bar-anti-symmetric ($\overline X = -X$);
- every constant $c \in R \hookrightarrow R[X]$ is bar-symmetric;
- every even-degree monomial $X^{2n}$ is bar-symmetric;
- every odd-degree monomial $X^{2n+1}$ is bar-anti-symmetric;
- the bar-symmetric subring is exactly $R[X^2]$.

## Categorical role

This is the canonical non-trivial bar-involution in QOU. It provides a concrete categorical setting where the polynomial indeterminate $X$ plays the role of the bar-anti-symmetric Hecke skein

$$h \;=\; q - q^{-1}.$$

The bar-action $h \mapsto -h$ matches the general [`def:bar-involution`](#def:bar-involution) statement.

We work in $R[X]$ rather than directly with the Hecke skein for three reasons:

1. **Algebraic decidability:** Mathlib's `Polynomial.comp` lemmas provide the four ring-involution axioms. The proofs are short and complete.
2. **No analysis needed:** Unlike complex conjugation, $R[X]$ requires no analytic infrastructure. Formal substitution defines the bar map.
3. **Concrete bar-symmetric subring identification:** The bar-symmetric subring is exactly $R[X^2]$, the ring of even polynomials. This gives a concrete polynomial model of the projection $P_{\mathrm{avg}}$.

## Proved theorems (Lean)

The Lean sibling [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean) formalises the following propositions.

See [Table](#tbl:polynomial-bar-involution-table-data).

All proofs use only `Polynomial.comp` lemmas from Mathlib (`X_comp`, `add_comp`, `mul_comp`, `one_comp`, `zero_comp`, `neg_comp`, `comp_assoc`).

## Connection to the three-layer synthesis

In `prop:bar-symmetric-three-layer-synthesis`, the universal kernel is bar-anti-symmetric. The polynomial indeterminate $X$ is the canonical such kernel.

- **Series layer:** $F_{\text{series}}(X)$ is an even polynomial, hence in $R[X^2]$.
- **Phase layer:** This is similarly an even polynomial.
- **Gain layer:** This is also an even polynomial.

Each layer functor manifests as a `BarHeckeFunctor R[X]`. These functors send bar-anti-symmetric inputs to bar-symmetric outputs. Consequently, the synthesis-class fields `series_avatar`, `phase_avatar`, and `gain_avatar` become explicit elements of $R[X^2]$.

## Proofs (Lean $\leftrightarrow$ paper bridge)

We provide narrative proofs below. The corresponding formal proofs reside in [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean). The core bar-involution proofs use only the four ring-involution axioms and Mathlib's `Polynomial.comp` lemmas. They invoke no archimedean or analytic infrastructure. The concrete archimedean section over $\mathbb{R}$ specialises to the archimedean base ring to yield falsifiable numerical predictions.

### Core bar-involution axioms

**Proposition (Lean: `barPoly_X`).** $\overline X = -X$.
