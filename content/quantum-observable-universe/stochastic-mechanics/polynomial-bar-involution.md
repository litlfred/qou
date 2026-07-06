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

See [Table](#tbl:polynomial-bar-involution-table-data).

All proofs use only `Polynomial.comp` lemmas from Mathlib
(`X_comp`, `add_comp`, `mul_comp`, `one_comp`, `zero_comp`,
`neg_comp`, `comp_assoc`).

## Connection to the three-layer synthesis

In `prop:bar-symmetric-three-layer-synthesis`,
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
## Proofs (Lean $\leftrightarrow$ paper bridge)

Every Lean theorem below has both a narrative proof here and a
fully formalised Lean proof in [`polynomial-bar-involution.lean`](polynomial-bar-involution.lean).
The **core** bar-involution proofs (axioms, `barPoly_X_pow_*`,
`barPoly_natCast`, arbitrary-truncation theorems, generic `evenPoly_*`)
use only the four ring-involution axioms plus Mathlib's
`Polynomial.comp` lemmas — no archimedean or analytic infrastructure
invoked. The trailing $\mathbb{R}[X]$ section (`c5_taylor_6`,
`cos_truncated_6`, `cosh_truncated_6` and their concrete evaluations
via `norm_num`) specialises to the archimedean base ring to produce
falsifiable numerical predictions; per AGENTS.md §7c the generic /
specialised cut is a soft boundary inside this file, marked by the
"Concrete archimedean instances over $\mathbb{R}$" section header,
and may be moved to a sibling block under `observations/` in a
follow-up if reviewers prefer a hard split.

### Core bar-involution axioms

**Proposition (Lean: `barPoly_X`).** $\overline X = -X$.
