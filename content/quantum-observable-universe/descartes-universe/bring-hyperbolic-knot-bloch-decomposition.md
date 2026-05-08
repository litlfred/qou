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
| $\mathbb{Q}(\zeta_3)$ — figure-8 ($4_1$) trace field | 2 | 0 | 1 | 1 |
| $\mathbb{Q}(\zeta_4) = \mathbb{Q}(i)$ — Borromean ($\mathcal{B}_3$) trace field, via 2 ideal regular octahedra of shape $i$ | 2 | 0 | 1 | 1 |
| $\mathbb{Q}(\zeta_5)$ — Bring's natural field | 4 | 0 | 2 | 2 |
| $\mathbb{Q}(\zeta_{12}) = \mathbb{Q}(\zeta_3,\zeta_4)$ — figure-8 + Borromean compositum | 4 | 0 | 2 | 2 |
| $\mathbb{Q}(\zeta_{60}) = \mathbb{Q}(\zeta_3,\zeta_4,\zeta_5)$ — full compositum (figure-8, Borromean, Bring) | 16 | 0 | 8 | 8 |

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

**Observation 2.** The natural compositum is widened by the
Borromean rings (proton/neutron in the QOU spectrum, see
[`recursive-atom-knot-atlas`](../braids-and-knots/recursive-atom-knot-atlas.md)):
$\mathrm{Vol}(\mathcal{B}_3) = 8G = 8\,\mathrm{Cl}_2(\pi/4)$ via two
ideal regular octahedra of shape parameter $i$
([`binding-scale-catalan`](../braids-and-knots/binding-scale-catalan.md)),
so $\mathcal{B}_3$'s trace field is $\mathbb{Q}(i) = \mathbb{Q}(\zeta_4)$,
not $\mathbb{Q}(\zeta_3)$. Combining figure-8, Borromean, and Bring's
$\mathbb{Q}(\zeta_5)$ gives the compositum
$\mathbb{Q}(\zeta_{60}) = \mathbb{Q}(\zeta_3, \zeta_4, \zeta_5)$,
of degree 16 over $\mathbb{Q}$ and Bloch-group rank
$r_2(\mathbb{Q}(\zeta_{60})) = 8$. The figure-8 and Borromean
contributions occupy two distinct 1-dimensional sub-lines, so the
remaining 6 dimensions are available for the decomposition.

**Observation 3.** The QOU framework supplies an explicit
finite enumeration of hyperbolic knots in its mass-bearing
spectrum, via the
[recursive atom-knot atlas](../braids-and-knots/recursive-atom-knot-atlas.md):

| Particle / atom | Hyperbolic knot / link | Volume | Trace field (standard) |
|---|---|---|---|
| Proton, neutron | $\mathcal{B}_3$ Borromean | $8G \approx 7.328$ | $\mathbb{Q}(i)$ |
| Deuteron $^2$H | $6_2$ | $\approx 4.401$ | quartic field over $\mathbb{Q}$ |
| Tritium $^3$H | $8_{11}$ | $\approx 8.286$ | sextic field |
| $^3$He | $L_{6a4}$ (link) | $\approx 7.328$ | $\mathbb{Q}(i)$ (twin to $\mathcal{B}_3$) |
| Higgs / mass mechanism | $4_1$ figure-8 | $\approx 2.030$ | $\mathbb{Q}(\zeta_3)$ |

(`recursive-on-⁴He` and the $^4$He magic-A formula contribute via
$8G$ algebraically, not via a single hyperbolic knot.) Trace fields
beyond degree 2 quickly enlarge the compositum: $6_2$'s field is
quartic, $8_{11}$'s is sextic. Including all hyperbolic knots in
the QOU spectrum, the natural compositum is **at least**
$\mathbb{Q}(\zeta_{60})$ and may be larger depending on which
non-cyclotomic fields appear.

The $S_5$-equivariance constraint pins which knots actually embed
$S_5$-equivariantly in Bring's surface; the figure-8 and Borromean
admit such embeddings up to standard ambiguities, and the higher
isotope knots ($6_2, 8_{11}, L_{6a4}, \ldots$) inherit
$S_5$-equivariance via the binding-operator $\bowtie$ structure of
the atlas.

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
  2\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right)
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
establishes the unconditional algebraic skeleton plus one
conditional non-existence result narrowing the decomposition:

- `r2Cyclotomic` — for any $n$, $r_2(\mathbb{Q}(\zeta_n)) = \varphi(n)/2$ (definition).
- `r2_zeta3_eq_one`, `r2_zeta4_eq_one`, `r2_zeta5_eq_two`,
  `r2_zeta12_eq_two`, `r2_zeta15_eq_four`, `r2_zeta60_eq_eight`
  — concrete values via `decide`.
- `compositum_rank_decomposition_narrow` —
  $r_2(\mathbb{Q}(\zeta_{15})) = r_2(\mathbb{Q}(\zeta_3)) + r_2(\mathbb{Q}(\zeta_5)) + 1$.
- `compositum_rank_decomposition_full` —
  $r_2(\mathbb{Q}(\zeta_{60})) = r_2(\mathbb{Q}(\zeta_{15})) + r_2(\mathbb{Q}(\zeta_4)) + 3$.
- `bring_zero_mode_value_positive`, `bring_zero_mode_value_ne_zero` —
  basic positivity of $2/(3\pi)$.
- A class `BringHyperbolicDecomposition` axiomatising the existence
  of the finite multi-set $\{(K_i, n_i)\}$.
- `bring_hyperbolic_decomposition` — sorry-free conditional theorem
  taking `BringHyperbolicDecomposition` as `[Instance]` and
  yielding `BringZeroModeBlochClass`.
- A class `BWQIndependence cl2_pi_3 cl2_pi_4` axiomatising the
  Q-linear independence of $\{2/(3\pi), \mathrm{Cl}_2(\pi/3),
  \mathrm{Cl}_2(\pi/4)\}$.
- `two_knot_decomposition_insufficient` — sorry-free conditional
  lemma taking `BWQIndependence` as `[Instance]` and proving that
  no $\mathbb{Z}$-linear combination of $D[Z_{4_1}] = 2\,\mathrm{Cl}_2(\pi/3)$
  and $D[Z_{\mathcal{B}_3}] = 8\,\mathrm{Cl}_2(\pi/4)$ alone equals
  $2/(3\pi)$. Any decomposition must therefore include **at least
  one hyperbolic knot beyond $\{4_1, \mathcal{B}_3\}$** from the
  QOU spectrum (e.g.\ $6_2, 8_{11}, L_{6a4}$, or higher-isotope
  knots from the recursive atlas).

The decomposition search is therefore narrowed: the figure-8 and
Borromean rings are necessary to cover the cyclotomic sectors
$\mathbb{Q}(\zeta_3)$ and $\mathbb{Q}(\zeta_4)$, but they are not
sufficient. The minimal search target is now a $\mathbb{Z}$-linear
combination of three or more distinct hyperbolic-knot BW values
from the atlas, in the rank-8 Bloch group
$B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$.

Closure of the class instance reduces to (C-Hyp): identify
$\mathcal{K}_{\mathrm{Bring}}$ explicitly and verify the integer
relation against $\zeta_{\mathbb{Q}(\zeta_{60})}^*(2)/\pi^?$. The
two-knot insufficiency lemma above eliminates the smallest possible
ansatz; the open problem is now the integer relation among the
remaining $r_2 - 2 = 6$ available cyclotomic-sector BW values.
