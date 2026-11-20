*Let $R$ be a commutative ring and $R[X]$ its polynomial ring in one indeterminate. The map*

$$
\overline{(\cdot)} \colon R[X] \to R[X], \qquad p(X) \mapsto p(-X)
$$

*is a ring involution. Under this bar:*

- *the indeterminate $X$ is **bar-anti-symmetric** ($\overline X = -X$);*
- *every constant $c \in R \hookrightarrow R[X]$ is **bar-symmetric**;*
- *every even-degree monomial $X^{2n}$ is **bar-symmetric**;*
- *every odd-degree monomial $X^{2n+1}$ is **bar-anti-symmetric**;*
- *the bar-symmetric subring contains $R[X^2]$, and equals it when $2$ is not a zero divisor in $R$. Over $\mathbb{F}_2$ the inclusion is strict, since $X = -X$ there.*

## Categorical role

This is the canonical non-trivial bar-involution in QOU. It provides a concrete categorical setting where the polynomial indeterminate $X$ plays the role of the bar-anti-symmetric Hecke skein

$$h \;=\; q - q^{-1},$$

with the correct bar-action $h \mapsto -h$ matching the general definition ([Bar-involution and its $P_{\mathrm{avg}}$ / $P_{\mathrm{skew}}$ projections: the canonical $q \leftrightarrow q^{-1}$, $\sigma \leftrightarrow \sigma^{-1}$ involution on the Hecke algebra, splitting every $H_n(q)$-quantity into a bar-symmetric (even/cosh/cos/$\mathrm{Li}_2^q$-like) part the framework retains and a bar-anti-symmetric (odd/sinh/sin/$\Phi_q$-like) part the framework projects away](#def:bar-involution)).

We work in $R[X]$ rather than directly with the Hecke skein for three reasons. First, algebraic decidability: `Polynomial.comp` lemmas give the four ring-involution axioms for free. Second, no analysis is needed: unlike $\mathbb{C}$ with conjugation, the bar map is defined by formal substitution. Third, concrete bar-symmetric subring identification: when $2$ is not a zero divisor in $R$, the bar-symmetric subring is exactly $R[X^2]$, providing a concrete model of "$P_{\mathrm{avg}}$ kills odd powers".

## Proved theorems (Lean)

The Lean sibling [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean) proves the following (see [Table](#tbl:polynomial-bar-involution-table-data)). All proofs use only `Polynomial.comp` lemmas from Mathlib.

## Connection to the three-layer synthesis

In `prop:bar-symmetric-three-layer-synthesis`, the universal kernel is bar-anti-symmetric. The polynomial indeterminate $X$ is the canonical such kernel. The series, phase, and gain layers are all even-power polynomials in $X$, hence in $R[X^2]$. Each layer functor is concretely realised as a `BarHeckeFunctor R[X]` sending bar-anti-symmetric inputs to bar-symmetric outputs. The synthesis-class fields become explicit elements of $R[X^2]$.

## Proofs (Lean $\leftrightarrow$ paper bridge)

Every Lean theorem below has both a narrative proof here and a fully formalised Lean proof in [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean). The core bar-involution proofs use only the four ring-involution axioms plus Mathlib's `Polynomial.comp` lemmas.

### Core bar-involution axioms

**Proposition (Lean: `barPoly_X`).** $\overline X = -X$.
