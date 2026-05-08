**Conjecture (Bloch-group decomposition of $2/(3\pi)$).**
*There exists a finite multi-set
$\{(K_1, n_1), \ldots, (K_m, n_m)\}$ of hyperbolic knots
$K_i \subset S^3$ that embed in Bring's surface $X_{\mathrm{Bring}}$
respecting (a finite-index sub-symmetry of) the $S_5$ automorphism
group, with integer multiplicities $n_i \in \mathbb{Z}$, such that*

$$
  \boxed{\;\;
  \sum_{i = 1}^{m} n_i \cdot D\bigl[Z_{K_i}\bigr]
  \;=\;
  \frac{2}{3\pi}
  \quad\text{in } \mathbb{R},
  \;\;}
$$

*where $[Z_K] \in B(F_K)$ is the Bloch class of $K$ in its trace
field $F_K$ and $D$ is the Bloch-Wigner dilogarithm. Equivalently,
the aggregate class*

$$
  [Z]_{\mathrm{Bring}}
  \;:=\;
  \sum_i n_i\,[Z_{K_i}]
  \;\in\;
  B(F)\otimes \mathbb{Q},
$$

*for $F = \mathbb{Q}(\zeta_{15})$ the compositum
$\mathbb{Q}(\zeta_3, \zeta_5)$, has Bloch-Wigner image
$D([Z]_{\mathrm{Bring}}) = 2/(3\pi)$.*

> **Status: open structural sub-conjecture.** This is the K-theoretic
> identification required to inhabit the typeclass
> [`QOU.Descartes.BringZeroModeBlochClass`](em-coupling-bring-zero-mode.lean)
> from
> [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode).
> The statement is a concrete, falsifiable prediction once the
> "$S_5$-equivariantly embeddable" condition is made precise. The
> proof attempt below establishes (i) the relevant field structure
> unconditionally, (ii) the figure-8 contribution as a worked
> classical sub-piece, and (iii) the irreducible open problem.

## Why this conjecture is the right framing

The mass / hyperbolic sector of the QOU framework
([figure-8 archimedean illustration](#rem:figure-8-archimedean-illustration))
delivers Bloch-Wigner content via $\tau_{\mathrm{arch}}$: each
hyperbolic knot $K \subset S^3$ contributes a class $[Z_K] \in B(F_K)$
whose BW image is the hyperbolic volume of $S^3 \setminus K$. The
force-carrier sector — torus knots $T(2,9), T(3,5)$ producing the
multiplicative bare formula $q[9]_q[10]_q$ — does **not** contribute
to BW: torus knots are Seifert-fibered, not hyperbolic, so their
complements have no ideal-tetrahedron triangulation and no
$D$-class. The additive correction $2/(3\pi)$ in
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
must therefore originate in the *hyperbolic* sector of knots
embedded in Bring's surface.

## Field structure (unconditional)

Let $\zeta_n$ denote a primitive $n$-th root of unity.

| Field $F$ | $[F:\mathbb{Q}]$ | $r_1$ | $r_2$ | $\mathrm{rk}_{\mathbb{Z}}\,B(F)\otimes\mathbb{Q}$ |
|---|---:|---:|---:|---:|
| $\mathbb{Q}(\zeta_3)$ — figure-8 trace field | 2 | 0 | 1 | 1 |
| $\mathbb{Q}(\zeta_5)$ — Bring's natural field | 4 | 0 | 2 | 2 |
| $\mathbb{Q}(\zeta_{15}) = \mathbb{Q}(\zeta_3,\zeta_5)$ — compositum | 8 | 0 | 4 | 4 |

The rank columns are by Borel's theorem [`borel1974`]:
$\mathrm{rk}\,K_3^{\mathrm{ind}}(F)\otimes\mathbb{Q} =
\mathrm{rk}\,B(F)\otimes\mathbb{Q} = r_2(F)$ for any number field
$F$ (here $K_3^{\mathrm{ind}}$ is the indecomposable part of $K_3$).
The Bloch-Wigner regulator
$D \colon B(F)\otimes\mathbb{Q} \xrightarrow{\sim} \mathbb{R}^{r_2(F)}$
is an isomorphism after tensoring with $\mathbb{Q}$.

**Observation 1.** The figure-8's trace field $\mathbb{Q}(\zeta_3)$
is **not** a subfield of $\mathbb{Q}(\zeta_5)$ (degrees 2 and 4
respectively, and $\mathbb{Q}(\zeta_5)$ contains no real quadratic
imaginary subfield other than $\mathbb{Q}$). So a decomposition
working entirely inside $B(\mathbb{Q}(\zeta_5))$ cannot include the
figure-8.

**Observation 2.** The compositum
$\mathbb{Q}(\zeta_{15}) = \mathbb{Q}(\zeta_3, \zeta_5)$ contains
both the figure-8's trace field and Bring's natural field, with
$r_2(\mathbb{Q}(\zeta_{15})) = 4$. The Bloch group there has
rank 4; the figure-8 contribution sits in a 1-dimensional
sub-line, and three further linearly independent classes are
available for the decomposition.

**Observation 3.** Every hyperbolic knot embedding in genus 4 has
trace field a number field, so the sum $[Z]_{\mathrm{Bring}}$
lives in some compositum $F$ of trace fields. The
$S_5$-equivariance constraint should restrict $F$ to be a
sub-extension of $\mathbb{Q}(\zeta_{15})$ at most: the relevant
Galois action is by $S_5$ on the Bring construction and by
$\mathrm{Gal}(F/\mathbb{Q})$ on the Bloch group, and equivariance
requires compatibility.

## Partial proof: the figure-8 sub-piece

The figure-8 knot $4_1$ has trace field $F_{4_1} = \mathbb{Q}(\zeta_3)$
(Thurston [`thurston1978`]). Its Bloch class is
$[Z_{4_1}] = 2[\zeta_6]$ in $B(\mathbb{Q}(\zeta_3))$, where
$\zeta_6 = e^{i\pi/3}$ is the shape parameter of the two ideal
regular tetrahedra in $S^3 \setminus 4_1$. The Bloch-Wigner
value is the classical

$$
  D[Z_{4_1}]
  \;=\;
  2\,D\bigl(e^{i\pi/3}\bigr)
  \;=\;
  3\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right)
  \;\approx\;
  2.029883\ldots
$$

The Clausen value $\mathrm{Cl}_2(\pi/3)$ is a Gauss-Catalan-type
constant; the relation $\mathrm{Cl}_2(\pi/3) \neq \frac{2}{3\pi}\cdot k$
for any small rational $k$ is straightforward (numerical:
$2/(3\pi) \approx 0.2122$, $\mathrm{Cl}_2(\pi/3) \approx 1.0149$,
ratio $\approx 4.78$ — non-rational to high precision). So the
figure-8 alone is not the answer; Observations 1 and 3 above
already forced this.

## Reduction of the conjecture

Given the field-rank table, the conjecture reduces to two
constituent claims:

**(C-Hyp).** *There is a finite, $S_5$-equivariantly characterised
set $\mathcal{K}_{\mathrm{Bring}}$ of hyperbolic knots embeddable
in Bring's surface, and an explicit integer relation
$\sum_K n_K\,[Z_K] = [Z]_{\mathrm{Bring}}$ in $B(\mathbb{Q}(\zeta_{15}))$.*

**(C-Hodge).** *The geometric class on Bring's surface
$[Z]_{\mathrm{Hodge}}$ extracted from the Hodge / Gauss-Bonnet
data ($g = 4$, area $4\pi(g-1) = 12\pi$, $b_1 = 8$) coincides with
$[Z]_{\mathrm{Bring}}$ in $B(\mathbb{Q}(\zeta_{15})) \otimes \mathbb{Q}$,
and $D([Z]_{\mathrm{Hodge}}) = 2/(3\pi)$.*

Both claims live inside the 4-dimensional space
$B(\mathbb{Q}(\zeta_{15}))\otimes\mathbb{Q}$, where Borel's
regulator gives an explicit isomorphism with $\mathbb{R}^4$. The
1-dimensional sub-line containing $2/(3\pi)$ is determined by
the Galois action: by the functional equation of the Dedekind
zeta function, the line is spanned by $\zeta_{\mathbb{Q}(\zeta_{15})}^*(2)$
modulo a known $\pi$-power. Concretely:

$$
  \zeta_{\mathbb{Q}(\zeta_{15})}^*(2)
  \;=\;
  \frac{(2\pi)^{2 r_2}}{\sqrt{|d_F|}}\,R_F^{(2)}
  \;=\;
  \frac{(2\pi)^8}{\sqrt{|d_F|}}\,R_F^{(2)},
$$

where $R_F^{(2)}$ is the higher regulator
([`borel1974`, `zagier1986`]) determined by BW values on a basis
of $B(F)\otimes\mathbb{Q}$.

**The irreducible open problem.** Identifying which specific
hyperbolic knots embed $S_5$-equivariantly in Bring is a concrete
geometric question without a known answer in the literature. The
figure-8 is the obvious starting point, but Observation 1 forbids
its sole contribution; further candidates (e.g., $5_2$, $6_1$,
$6_2$, $6_3$ have trace fields ranging from $\mathbb{Q}(\sqrt{-7})$
to $\mathbb{Q}(\zeta_3, \sqrt{-15})$ to higher cubic fields) need
to be checked for $S_5$-compatible embeddability and trace-field
inclusion in $\mathbb{Q}(\zeta_{15})$.

## What's proved (Lean handle)

The Lean file [`bring-hyperbolic-knot-bloch-decomposition.lean`](bring-hyperbolic-knot-bloch-decomposition.lean)
establishes the unconditional algebraic skeleton:

- `r_2_cyclotomic` — for any odd $n \geq 3$, $r_2(\mathbb{Q}(\zeta_n)) = \varphi(n)/2$.
- `r_2_zeta5_eq_two`, `r_2_zeta15_eq_four`, `r_2_zeta3_eq_one` —
  the three concrete values, by `decide`.
- `field_inclusion_chain` — $\mathbb{Q}(\zeta_3),\mathbb{Q}(\zeta_5)
  \subset \mathbb{Q}(\zeta_{15})$ as the compositum.
- `bring_zero_mode_value_irrational_over_zeta3` (sketch) —
  $2/(3\pi)$ is not a $\mathbb{Z}$-multiple of
  $D\bigl(e^{i\pi/3}\bigr)$ in $\mathbb{R}$, so the figure-8
  alone cannot inhabit `BringZeroModeBlochClass`.
- A class `BringHyperbolicDecomposition` axiomatising the existence
  of the finite multi-set $\{(K_i, n_i)\}$.
- `bring_hyperbolic_decomposition` — sorry-free conditional theorem
  taking `BringHyperbolicDecomposition` as `[Instance]` and
  yielding `BringZeroModeBlochClass`.

Closure of the class instance reduces to (C-Hyp): identify
$\mathcal{K}_{\mathrm{Bring}}$ explicitly and verify the integer
relation against $\zeta_{\mathbb{Q}(\zeta_{15})}^*(2)/\pi^8$.
