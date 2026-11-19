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

with the bar action $h \mapsto -h$ matching the general [bar involution](#def:bar-involution).

Working in $R[X]$ rather than directly with the Hecke skein provides three structural advantages. First, algebraic decidability: formal polynomial composition $p(X) \mapsto p(-X)$ gives the four ring-involution axioms directly over any commutative ring $R$. Second, no analysis is needed: unlike $\mathbb{C}$ with complex conjugation, the bar map is defined purely by formal substitution. Third, concrete bar-symmetric subring identification: when $2$ is not a zero divisor in $R$, the bar-symmetric subring is exactly $R[X^2]$, providing an explicit algebraic model in which $P_{\mathrm{avg}}$ annihilates odd powers.

## Elementary identities

The defining ring-involution and monomial parity identities are summarised in [Table](#tbl:polynomial-bar-involution-table-data) and established in the accompanying proof.

## Connection to the three-layer synthesis

In the bar-symmetric three-layer synthesis, the universal kernel is bar-anti-symmetric, and the polynomial indeterminate $X$ is the canonical such kernel. The truncated series, phase, and gain layers are all even-power polynomials in $X$, hence elements of $R[X^2]$: each layer map sends bar-anti-symmetric inputs to bar-symmetric outputs inside $R[X^2]$.
