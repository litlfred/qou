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

**Proposition (Lean: `barPoly_neg_X`).** $\overline{-X} = X$.
*Proof.* $(-X).\mathrm{comp}(-X) = -(X.\mathrm{comp}(-X)) = -(-X) = X$ via `neg_comp`, `X_comp`, `neg_neg`. $\square$

**Proposition (Lean: `barPoly_C c`).** $\overline{C c} = C c$.
*Proof.* Constants are bar-fixed: $(C c).\mathrm{comp}(-X) = C c$ (Mathlib `C_comp`). $\square$

**Proposition (Lean: `barPoly_add p q`).** $\overline{p+q} = \overline p + \overline q$.
*Proof.* Direct from `Polynomial.add_comp`. $\square$

**Proposition (Lean: `barPoly_mul p q`).** $\overline{p \cdot q} = \overline p \cdot \overline q$.
*Proof.* Direct from `Polynomial.mul_comp`. $\square$

**Proposition (Lean: `barPoly_one`, `barPoly_zero`).** $\overline 1 = 1$ and $\overline 0 = 0$.
*Proof.* Direct from `one_comp`, `zero_comp`. $\square$

**Proposition (Lean: `barPoly_involutive p`).** $\overline{\overline p} = p$.
*Proof.* $(p.\mathrm{comp}(-X)).\mathrm{comp}(-X) = p.\mathrm{comp}((-X).\mathrm{comp}(-X)) = p.\mathrm{comp}(X) = p$ via `comp_assoc`, `barPoly_neg_X`, and `comp_X`. $\square$

### Power identities

**Proposition (Lean: `barPoly_X_pow_two`).** $\overline{X^2} = X^2$.
*Proof.* $X^2 = X \cdot X$, so $\overline{X^2} = \overline X \cdot \overline X = (-X)(-X) = X^2$. $\square$

**Proposition (Lean: `barPoly_X_pow n`).** $\overline{X^n} = (-1)^n \cdot X^n$.
*Proof.* Induction on $n$. Base ($n=0$): $\overline 1 = 1$. Step: $\overline{X^{k+1}} = \overline{X \cdot X^k} = (-X) \cdot (-1)^k X^k = (-1)^{k+1} X^{k+1}$. $\square$

**Proposition (Lean: `barPoly_X_pow_even n`).** $\overline{X^{2n}} = X^{2n}$.
*Proof.* From `barPoly_X_pow`: coefficient is $(-1)^{2n} = ((-1)^2)^n = 1$. $\square$

**Proposition (Lean: `barPoly_X_pow_odd n`).** $\overline{X^{2n+1}} = -X^{2n+1}$.
*Proof.* From `barPoly_X_pow`: coefficient is $(-1)^{2n+1} = -1$. $\square$

### Scalar identities

**Proposition (Lean: `barPoly_natCast n`).** Every natural-number scalar is bar-fixed in $R[X]$.
*Proof.* Induction on $n$. Base: $\overline 0 = 0$. Step: $\overline{k+1} = \overline k + \overline 1 = k + 1$. $\square$

**Proposition (Lean: `barPoly_sub p q`).** $\overline{p - q} = \overline p - \overline q$.
*Proof.* $p - q = p + (-1) \cdot q$; bar commutes with $+$ and $\cdot$, and $\overline{-1} = -1$ (from `neg_comp` + `one_comp`). $\square$

**Proposition (Lean: `barPoly_neg p`).** $\overline{-p} = -\overline p$.
*Proof.* Take $p = 0$ in `barPoly_sub`: $\overline{-q} = \overline{0 - q} = 0 - \overline q = -\overline q$. $\square$

### Concrete bar-symmetric polynomials

**Proposition (Lean: `barPoly_c5_denominator`).** $\overline{4 + X^2} = 4 + X^2$.
*Proof.* $\overline 4 = 4$ by `barPoly_natCast` (with $4 = (4:\mathbb{N})$); $\overline{X^2} = X^2$ by `barPoly_X_pow_two`; combine with `barPoly_add`. $\square$

**Proposition (Lean: `barPoly_c5_taylor_6`).** The polynomial $c_5^{[6]}(X) := -\tfrac{5}{4} - \tfrac{X^2}{16} + \tfrac{X^4}{64} - \tfrac{X^6}{256}$ is bar-symmetric.
*Proof.* Every term has the form $C(c) \cdot X^{2k}$ with $c \in \mathbb{R}$ and $k \in \{0,1,2,3\}$. Constants fixed by `barPoly_C`; even powers fixed by `barPoly_X_pow_even`. Sum and difference of bar-symmetric is bar-symmetric. $\square$

**Proposition (Lean: `barPoly_cos_truncated_6`, `barPoly_cosh_truncated_6`).** $\cos^{[6]}(X) := 1 - X^2/2 + X^4/24 - X^6/720$ and $\cosh^{[6]}(X) := 1 + X^2/2 + X^4/24 + X^6/720$ are bar-symmetric.
*Proof.* Same structure as `c5_taylor_6`: each term $C(c) \cdot X^{2k}$ with bar-fixed coefficient and bar-fixed even power. $\square$

**Theorem (Lean: `three_layer_truncated_all_bar_symmetric`).** All three layer truncations — series $c_5^{[6]}$, phase $\cos^{[6]}$, gain $\cosh^{[6]}$ — are bar-symmetric in the **same** polynomial ring $\mathbb{R}[X]$ under the **same** bar-involution $X \mapsto -X$.
*Proof.* Conjunction of the three propositions above. The three layer avatars live in the same ambient ring with the same bar — this is the **categorical-derivation unification at the truncated-polynomial level**. $\square$

### Pre-archimedean generic versions

**Proposition (Lean: `barPoly_evenPoly_6 c0 c1 c2 c3`).** Over any commutative ring $R$ (no field needed), the polynomial $c_0 + c_1 X^2 + c_2 X^4 + c_3 X^6$ is bar-symmetric for arbitrary $c_0, c_1, c_2, c_3 \in R$.
*Proof.* Per-term: $C(c_i)$ bar-fixed by `barPoly_C`; $X^{2k}$ bar-fixed by `barPoly_X_pow_even`. Sum bar-symmetric by `barPoly_add`. **No archimedean structure invoked.** $\square$

**Theorem (Lean: `barPoly_even_truncated_arbitrary n c`).** For any $n \in \mathbb{N}$ and any $c : \mathbb{N} \to R$, the polynomial $P_n(X) := \sum_{k=0}^{n-1} c_k X^{2k}$ is bar-symmetric.
*Proof.* Induction on $n$. Base: empty sum $= 0$ bar-symmetric. Step: $P_{k+1} = P_k + C(c_k) X^{2k}$; IH gives $P_k$ bar-symmetric, per-term argument gives $C(c_k) X^{2k}$ bar-symmetric; sum bar-symmetric. **Holds for arbitrary truncation degree over any CommRing.** $\square$

**Theorem (Lean: `barPoly_odd_truncated_arbitrary n c`).** Sums of odd-power monomials with arbitrary $R$-coefficients are bar-anti-symmetric.
*Proof.* Induction analogous to even case, using `barPoly_X_pow_odd` to flip sign on each term. $\square$

### Evaluations

**Proposition (Lean: `c5_taylor_6_eval_zero`).** $c_5^{[6]}(0) = -5/4$.
*Proof.* All positive-degree terms vanish at $X = 0$; constant term is $-5/4$. By `Polynomial.eval_*` lemmas. $\square$

**Proposition (Lean: `c5_taylor_6_eval_one`).** $c_5^{[6]}(1) = -333/256$.
*Proof.* $-5/4 - 1/16 + 1/64 - 1/256 = -320/256 - 16/256 + 4/256 - 1/256 = -333/256$ by `norm_num`. Approximates exact $c_5(1) = -13/10 = -332.8/256$ with relative error $\approx 0.06\%$ (consistent with $O(X^8 / 4^4)$ Taylor truncation at $X = 1$). $\square$

Polynomial-level work is **complete** — every theorem here has a narrative proof above and a `sorry`-free Lean proof in the sibling. Future extensions: `RatFunc R` for rational-function functors realising the proved $c_5 = -3/2 + 1/(X^2 + 4)$ closed form, and `PowerSeries R` for the formal power-series limit of the truncated avatars.
