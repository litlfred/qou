**Proposition (polynomial bar-involution).**

*Let $R$ be a commutative ring and $R[X]$ its polynomial ring in
one indeterminate. The map*

$$
\overline{(\cdot)} \colon R[X] \to R[X], \qquad p(X) \mapsto p(-X)
$$

*is a ring involution. Under this bar:*

- *the indeterminate $X$ is **bar-anti-symmetric** ($\overline X = -X$);*
- *every constant $c \in R \hookrightarrow R[X]$ is **bar-symmetric**;*
- *every even-degree monomial $X^{2n}$ is **bar-symmetric**;*
- *every odd-degree monomial $X^{2n+1}$ is **bar-anti-symmetric**;*
- *the bar-symmetric subring is exactly $R[X^2]$.*

## Categorical role

This is the **canonical non-trivial bar-involution** in QOU. It
provides a concrete categorical setting where the polynomial
indeterminate $X$ plays the role of the bar-anti-symmetric Hecke
skein

$$h \;=\; q - q^{-1},$$

with the correct bar-action $h \mapsto -h$ matching the general
[`def:bar-involution`](#def:bar-involution) statement.

Three motivations for working in $R[X]$ rather than directly with
the Hecke skein:

1. **Algebraic decidability** — `Polynomial.comp` lemmas in
   Mathlib give the four ring-involution axioms for free; the
   proofs are short and `sorry`-free.
2. **No analysis needed** — unlike $\mathbb{C}$ with conjugation,
   $R[X]$ requires no analytic infrastructure; the bar map is
   defined by formal substitution.
3. **Concrete bar-symmetric subring identification** — the bar-
   symmetric subring is exactly $R[X^2]$, which is precisely the
   ring of "even" polynomials. This gives a concrete model of
   "$P_{\mathrm{avg}}$ kills odd powers" at the polynomial level.

## Proved theorems (Lean)

The Lean sibling [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean)
proves the following, all `sorry`-free:

| Theorem | Statement |
|---|---|
| `barPoly_X` | $\overline X = -X$ |
| `barPoly_neg_X` | $\overline{(-X)} = X$ |
| `barPoly_C c` | $\overline{c} = c$ for $c \in R$ |
| `barPoly_add` | $\overline{p+q} = \overline p + \overline q$ |
| `barPoly_mul` | $\overline{p\cdot q} = \overline p \cdot \overline q$ |
| `barPoly_one` | $\overline 1 = 1$ |
| `barPoly_zero` | $\overline 0 = 0$ |
| `barPoly_involutive` | $\overline{\overline p} = p$ |
| `barPoly_X_pow_two` | $\overline{X^2} = X^2$ (concrete bar-symmetry) |
| `barPoly_X_pow n` | $\overline{X^n} = (-1)^n \cdot X^n$ |

All proofs use only `Polynomial.comp` lemmas from Mathlib
(`X_comp`, `add_comp`, `mul_comp`, `one_comp`, `zero_comp`,
`neg_comp`, `comp_assoc`).

## Connection to the three-layer synthesis

In [`prop:bar-symmetric-three-layer-synthesis`](#prop:bar-symmetric-three-layer-synthesis),
the universal kernel is bar-anti-symmetric. The polynomial
indeterminate $X$ is the **canonical such kernel**:

- Series layer: $F_{\text{series}}(X)$ is an even-power polynomial
  in $X$, hence in $R[X^2]$.
- Phase layer: similarly an even-power polynomial.
- Gain layer: similarly.

Each layer functor is concretely realised as a `BarHeckeFunctor R[X]`
sending bar-anti-symmetric inputs (degree-odd polynomials, in
particular $X$ itself) to bar-symmetric outputs (degree-even
polynomials). The synthesis-class fields `series_avatar`,
`phase_avatar`, `gain_avatar` then become explicit elements of
$R[X^2]$.

## Status

Type-level infrastructure complete. Future work: instantiate
specific `BarHeckeFunctor R[X]` examples corresponding to
truncated $\cos$ / $\cosh$ / Li_2^q expansions in $X$, and
extend to `RatFunc R = FractionRing (R[X])` for rational-function
functors like the proved $c_5 = -3/2 + 1/(X^2 + 4)$ form.
