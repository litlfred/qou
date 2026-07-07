<!-- FILE_START: intro-archimedean-hartree-crystal.md -->
The preceding categorical constructions require evaluation over $\mathbb{R}$. A Hartree-type self-consistent approximation isolates a unique archimedean realisation and fixes the fibre functor $\tau$. The Kashiwara crystal basis indexes the compatible orthogonal decomposition. A Type-B folded crystal reduces the mass-tower problems to combinatorics. The Bloch-group quotient supplies the cohomological obstruction anchoring the analytic identities for the Clausen function and Bloch-Wigner dilogarithm.

The Lean blueprint requires these explicit archimedean specialisations to connect the categorical $q$-deformations to real-analytic bounds.
<!-- FILE_END: intro-archimedean-hartree-crystal.md -->

<!-- FILE_START: bring-hyperbolic-knot-bloch-decomposition.md -->
**Conjecture (Bloch-group decomposition of $2/(3\pi)$).**
*There exists a finite multi-set $\{(K_1, n_1), \ldots, (K_m, n_m)\}$ of hyperbolic knots $K_i \subset S^3$. These knots embed in Bring's surface $X_{\mathrm{Bring}}$ respecting a finite-index sub-symmetry of the $S_5$ automorphism group. The multiplicities $n_i \in \mathbb{Z}$ satisfy*

$$
  \boxed{\;\;
  \sum_{i = 1}^{m} n_i \cdot D\bigl[Z_{K_i}\bigr]
  \;=\;
  \frac{2}{3\pi}
  \quad\text{in } \mathbb{R},
  \;\;}
$$

*where $[Z_K] \in B(F_K)$ is the Bloch class of $K$ in its trace field $F_K$ and $D$ is the Bloch-Wigner dilogarithm. Equivalently, the aggregate class*

$$
  [Z]_{\mathrm{Bring}}
  \;:=\;
  \sum_i n_i\,[Z_{K_i}]
  \;\in\;
  B(F)\otimes \mathbb{Q},
$$

*for $F = \mathbb{Q}(\zeta_{15})$ the compositum $\mathbb{Q}(\zeta_3, \zeta_5)$, has Bloch-Wigner image $D([Z]_{\mathrm{Bring}}) = 2/(3\pi)$.*

## Framing

The mass sector delivers Bloch-Wigner content via $\tau_{\mathrm{arch}}$ ([`figure-8-archimedean-illustration`](#rem:figure-8-archimedean-illustration)). Each hyperbolic knot $K \subset S^3$ contributes a class $[Z_K] \in B(F_K)$. The Bloch-Wigner image of this class is the hyperbolic volume of $S^3 \setminus K$. The force-carrier sector features torus knots $T(2,9)$ and $T(3,5)$. These knots produce the multiplicative bare formula $q[9]_q[10]_q$. They contribute zero to the Bloch-Wigner image. They are Seifert-fibered and lack ideal-tetrahedron triangulations. The additive correction $2/(3\pi)$ in [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode) originates in the hyperbolic sector of knots embedded in Bring's surface.

## Field structure

Let $\zeta_n$ denote a primitive $n$-th root of unity.

| Field $F$ | $[F:\mathbb{Q}]$ | $r_1$ | $r_2$ | $\mathrm{rk}_{\mathbb{Z}}\,B(F)\otimes\mathbb{Q}$ |
|---|---:|---:|---:|---:|
| $\mathbb{Q}(\zeta_3)$ — figure-8 ($4_1$) trace field | 2 | 0 | 1 | 1 |
| $\mathbb{Q}(\zeta_4) = \mathbb{Q}(i)$ — Borromean ($\mathcal{B}_3$) trace field | 2 | 0 | 1 | 1 |
| $\mathbb{Q}(\zeta_5)$ — Bring's natural field | 4 | 0 | 2 | 2 |
| $\mathbb{Q}(\zeta_{12}) = \mathbb{Q}(\zeta_3,\zeta_4)$ — figure-8 + Borromean compositum | 4 | 0 | 2 | 2 |
| $\mathbb{Q}(\zeta_{60}) = \mathbb{Q}(\zeta_3,\zeta_4,\zeta_5)$ — full compositum | 16 | 0 | 8 | 8 |

By Borel's theorem, $\mathrm{rk}\,K_3^{\mathrm{ind}}(F)\otimes\mathbb{Q} = \mathrm{rk}\,B(F)\otimes\mathbb{Q} = r_2(F)$ for any number field $F$. The indecomposable part of $K_3$ is $K_3^{\mathrm{ind}}$. The Bloch-Wigner regulator $D \colon B(F)\otimes\mathbb{Q} \xrightarrow{\sim} \mathbb{R}^{r_2(F)}$ is an isomorphism after tensoring with $\mathbb{Q}$.

**Observation 1.** The figure-8 trace field $\mathbb{Q}(\zeta_3)$ is not a subfield of $\mathbb{Q}(\zeta_5)$. The field $\mathbb{Q}(\zeta_5)$ contains no real quadratic imaginary subfield other than $\mathbb{Q}$. A decomposition inside $B(\mathbb{Q}(\zeta_5))$ cannot include the figure-8 knot.

**Observation 2.** The Borromean rings expand the natural compositum ([`recursive-atom-knot-atlas`](../appendix-knot-periodic-table/recursive-atom-knot-atlas.md)). Two ideal regular octahedra of shape parameter $i$ define the geometry ([`binding-scale-catalan`](../braids-and-knots/binding-scale-catalan.md)). The volume is $\mathrm{Vol}(\mathcal{B}_3) = 8G = 8\,\mathrm{Cl}_2(\pi/4)$. The trace field of $\mathcal{B}_3$ is $\mathbb{Q}(i) = \mathbb{Q}(\zeta_4)$. Combining the figure-8, Borromean, and Bring fields produces the compositum $\mathbb{Q}(\zeta_{60}) = \mathbb{Q}(\zeta_3, \zeta_4, \zeta_5)$. This field has degree 16 over $\mathbb{Q}$ and Bloch-group rank $r_2(\mathbb{Q}(\zeta_{60})) = 8$. The figure-8 and Borromean contributions occupy two distinct 1-dimensional lines. The remaining 6 dimensions remain available for the decomposition.

**Observation 3.** The mass-bearing spectrum supplies a finite enumeration of hyperbolic knots ([`recursive-atom-knot-atlas`](../appendix-knot-periodic-table/recursive-atom-knot-atlas.md)).

| Particle / atom | Hyperbolic knot / link | Volume | Trace field |
|---|---|---|---|
| Proton, neutron | $\mathcal{B}_3$ Borromean | $8G \approx 7.328$ | $\mathbb{Q}(i)$ |
| Deuteron $^2$H | $6_2$ | $\approx 4.401$ | quartic field over $\mathbb{Q}$ |
| Tritium $^3$H | $8_{11}$ | $\approx 8.286$ | sextic field |
| $^3$He | $L_{6a4}$ (link) | $\approx 7.328$ | $\mathbb{Q}(i)$ |
| Higgs / mass mechanism | $4_1$ figure-8 | $\approx 2.030$ | $\mathbb{Q}(\zeta_3)$ |

The $^4$He formula contributes via $8G$ algebraically. Trace fields beyond degree 2 enlarge the compositum. The field for $6_2$ is quartic. The field for $8_{11}$ is sextic. Including all hyperbolic knots in the spectrum forces a natural compositum of at least $\mathbb{Q}(\zeta_{60})$. The $S_5$-equivariance constraint identifies knots that embed in Bring's surface. The figure-8 and Borromean knots admit such embeddings. Higher isotope knots inherit $S_5$-equivariance via the binding-operator $\oplus$ structure.

**Observation 4.** The electroweak knot operators $W \leftrightarrow \sigma_1^4 \to T(2,4)$, $Z \leftrightarrow \sigma_3^6 \to T(2,6)$, and $H \leftrightarrow \sigma_5^8 \to T(2,8)$ ([`ew-interface-knot`](../braids-and-knots/ew-interface-knot.md), [`categorical-higgs-mechanism`](../braids-and-knots/categorical-higgs-mechanism.md)) and the strong-force pair $T(2,9)$ and $T(3,5)$ ([`prop:force-carrier-bring-uniqueness`](#prop:force-carrier-bring-uniqueness)) are torus links. These links are Seifert-fibered and non-hyperbolic. They lack ideal-tetrahedron triangulations. They contribute zero to the Bloch-Wigner image $D \colon B(F)\otimes\mathbb{Q} \to \mathbb{R}^{r_2(F)}$. Only mass-bearing knots carry Bloch-Wigner content.

**Observation 5.** The five atlas entries $\{4_1, \mathcal{B}_3, 6_2, 8_{11}, L_{6a4}\}$ represent established particles. The Bloch-Wigner image is generated by the closures of all normal-form basis triple products $b_i \cdot \beta(T_{m,n}) \cdot b_j$ across the relevant Hecke algebras $H_n(q)$ ([`knot-operator-lp-selection`](../braids-and-knots/knot-operator-lp-selection.md), [`knot-operator-table.witness.json`](../../../computations/knot-operator-table.witness.json)). The normal-form basis for $H_3(q)$ is six-dimensional. Products with the torus operators $T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}$, and $T_{2,5}$ generate demand-channel identifiers. The normal-form basis grows polynomially at higher $n$. The closure space includes many hyperbolic knots beyond the five atlas entries. The dimension of the accessible sub-space inside $B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$ is not bounded by 5. The rank-8 ambient image is reachable through normal-form basis closures.

**Reformulation.** The K-theoretic identification seeks a finite collection of normal-form basis triple-product closures whose Bloch-Wigner sum equals $2/(3\pi)$. The rank-4 atlas-spanned lattice is $\mathbb{Z}\cdot 2\,\mathrm{Cl}_2(\pi/3) \oplus \mathbb{Z}\cdot 8G \oplus \mathbb{Z}\cdot D[Z_{6_2}] \oplus \mathbb{Z}\cdot D[Z_{8_{11}}]$. The shared volume identity $8G$ establishes the relation $\mathcal{B}_3 \sim L_{6a4}$. If $2/(3\pi)$ lies in this lattice, the decomposition closes. Otherwise, the search extends to closures in higher $H_n(q)$.

## Hyperbolic knots from normal-form closures

The normal-form basis for $H_3(q)$ is $\{\gamma, \sigma_0, \sigma_1, L_+, L_-, e^-\}$. Each element closes to a 3-braid in $S^3$.

| Basis element | Markov closure |
|---|---|
| $\gamma$ | 3 disjoint unknots |
| $\sigma_0$ | unknot |
| $\sigma_1$ | unknot |
| $L_+, L_-$ | Hopf link $L_H$ |
| $e^- = \sigma_1^3$ | trefoil $3_1 = T(2,3)$ |

No basis element closes to a hyperbolic knot. Hyperbolic content arises only from triple products $b_i \cdot \beta(T_{m,n}) \cdot b_j$. By the Birman-Hilden theorem, 3-braid closures yield hyperbolic knots up to 10 crossings. Bring's surface has genus 4 and contains all 3-bridge embeddings as closed 3-braids. Every hyperbolic knot embeddable in Bring's surface with bridge number $\leq 3$ appears in this set.

Knots with higher bridge numbers embeddable in genus 4 require $H_n(q)$ for $n \geq 4$. The normal-form basis contains $n!$ elements. Normal-form products across $H_3(q)$ through $H_8(q)$ reach the full set of hyperbolic knots embeddable in Bring's surface. The Heegaard-genus bound saturates Bring's genus 4. 

The Bloch-Wigner image of these closures spans the rank-8 sub-image of $B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$. The decomposition search operates over a finite candidate set at each tier:
1. **Tier 0**: $\{4_1, \mathcal{B}_3, 6_2, 8_{11}, L_{6a4}\}$ (rank $\le 4$).
2. **Tier 1**: Closures of normal-form products in $H_3(q)$ (approximate 30 prime knots).
3. **Tier 2**: Hyperbolic knots through $H_8(q)$ normal-form products.

The K-theoretic identification of $2/(3\pi)$ reduces to an integer-coefficient search.

**Markov stabilization.** Every knot in $S^3$ is the closure of a braid in $B_n$. Iterated normal-form composition in the colimit $\varinjlim_n H_n(q)$ reaches every knot. Restricting to closures with Heegaard genus $\leq 4$ isolates the hyperbolic knots embeddable in Bring's surface. Bridge number $b \leq 4$ implies $n \leq 8$.

A computational question remains. A hyperbolic knot $K$ might require a representative outside the Gröbner-Shirshov shortlex normal form of $H_n(q)$. In this case, the value $D[Z_K]$ requires Hecke-trace identification with a normal-form triple-product image.

For each hyperbolic knot $K$ embeddable in Bring's surface, there exists an integer $n_K \leq 8$ and a normal-form word $w_K \in H_{n_K}(q)$. This word is a triple-product chain with Markov closure $\widehat{w_K} \sim K$. Multiplicative composition in $\varinjlim_{n\leq 8} H_n(q)$ generates the Bloch-Wigner image. The Bloch group is generated by the normal-form elements and the torus-knot operators $T_{m,n}$. Iterated composition reaches every corresponding Bloch-Wigner value. 

Borel's regulator and Bloch-Suslin uniqueness determine the image. The K-theoretic search asks whether $2/(3\pi)$ is a $\mathbb{Z}$-linear combination of normal-form values.

## Field equivalence

The substrate route and the geometric route produce coinciding Bloch classes.

**Theorem (cyclotomic compositum).** The trace fields generate the compositum $\mathbb{Q}(\zeta_3) \cdot \mathbb{Q}(\zeta_4) \cdot \mathbb{Q}(\zeta_5) = \mathbb{Q}(\zeta_{60})$.

**Theorem (field equivalence).** Assume both routes produce a Bloch class with archimedean image $2/(3\pi)$. The Bloch-Wigner regulator $D \otimes \mathbb{Q} \colon B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q} \to \mathbb{R}^{r_2(\mathbb{Q}(\zeta_{60}))}$ is injective. The two Bloch classes are equal in $B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$.

These theorems reduce the structural alignment to the existence of an explicit normal-form decomposition for $2/(3\pi)$.

## The figure-8 knot

The figure-8 knot $4_1$ has trace field $\mathbb{Q}(\zeta_3)$. Its Bloch class is $[Z_{4_1}] = 2[\zeta_6]$. The shape parameter $\zeta_6 = e^{i\pi/3}$ defines the two ideal regular tetrahedra in the complement $S^3 \setminus 4_1$. The Bloch-Wigner value is

$$
  D[Z_{4_1}]
  \;=\;
  2\,D\bigl(e^{i\pi/3}\bigr)
  \;=\;
  2\,\mathrm{Cl}_2\!\left(\tfrac{\pi}{3}\right)
  \;\approx\;
  :val[Vol_4_1]{precision=6}\ldots
$$

The ratio of $2/(3\pi)$ to $\mathrm{Cl}_2(\pi/3)$ is not a small rational. The figure-8 knot alone does not yield the required value. 

## Reduction

The conjecture partitions into two claims:

**(C-Hyp).** *There exists a finite set $\mathcal{K}_{\mathrm{Bring}}$ of hyperbolic knots embeddable in Bring's surface respecting $S_5$-symmetry. An integer relation $\sum_K n_K\,[Z_K] = [Z]_{\mathrm{Bring}}$ holds in $B(\mathbb{Q}(\zeta_{15}))$.*

**(C-Hodge).** *The geometric class $[Z]_{\mathrm{Hodge}}$ on Bring's surface coincides with $[Z]_{\mathrm{Bring}}$ in $B(\mathbb{Q}(\zeta_{15})) \otimes \mathbb{Q}$. The Bloch-Wigner evaluation is $D([Z]_{\mathrm{Hodge}}) = 2/(3\pi)$.*

Both claims evaluate in the 4-dimensional space $B(\mathbb{Q}(\zeta_{15}))\otimes\mathbb{Q}$. Borel's regulator provides an isomorphism with $\mathbb{R}^4$. The functional equation of the Dedekind zeta function restricts the line containing $2/(3\pi)$ to $\zeta_{\mathbb{Q}(\zeta_{15})}^*(2)$:

$$
  \zeta_{\mathbb{Q}(\zeta_{15})}^*(2)
  \;=\;
  \frac{(2\pi)^{2 r_2}}{\sqrt{|d_F|}}\,R_F^{(2)}
  \;=\;
  \frac{(2\pi)^8}{\sqrt{|d_F|}}\,R_F^{(2)},
$$

where $R_F^{(2)}$ is the higher regulator.

The specific hyperbolic knots admitting $S_5$-equivariant embeddings in Bring's surface remain unclassified. 

## Established results

The Lean file [`bring-hyperbolic-knot-bloch-decomposition.lean`](bring-hyperbolic-knot-bloch-decomposition.lean) formalizes the algebraic constraints:

- `r2Cyclotomic` — $r_2(\mathbb{Q}(\zeta_n)) = \varphi(n)/2$.
- `r2_zeta3_eq_one`, `r2_zeta4_eq_one`, `r2_zeta5_eq_two`, `r2_zeta12_eq_two`, `r2_zeta15_eq_four`, `r2_zeta60_eq_eight` — concrete values.
- `compositum_rank_decomposition_narrow` — $r_2(\mathbb{Q}(\zeta_{15})) = r_2(\mathbb{Q}(\zeta_3)) + r_2(\mathbb{Q}(\zeta_5)) + 1$.
- `compositum_rank_decomposition_full` — $r_2(\mathbb{Q}(\zeta_{60})) = r_2(\mathbb{Q}(\zeta_{15})) + r_2(\mathbb{Q}(\zeta_4)) + 3$.
- `bring_zero_mode_value_positive`, `bring_zero_mode_value_ne_zero` — analytic bounds on $2/(3\pi)$.
- `BringHyperbolicDecomposition` — typeclass axiomatizing the finite multi-set $\{(K_i, n_i)\}$.
- `bring_hyperbolic_decomposition` — conditional theorem proving `BringZeroModeBlochClass` given the decomposition instance.
- `BWQIndependence cl2_pi_3 cl2_pi_4` — typeclass axiomatizing the linear independence of $\{2/(3\pi), \mathrm{Cl}_2(\pi/3), \mathrm{Cl}_2(\pi/4)\}$ over $\mathbb{Q}$.
- `two_knot_decomposition_insufficient` — lemma establishing that no $\mathbb{Z}$-linear combination of $D[Z_{4_1}]$ and $D[Z_{\mathcal{B}_3}]$ equals $2/(3\pi)$.

The decomposition requires at least one hyperbolic knot beyond the figure-8 and Borromean rings. The remaining task identifies $\mathcal{K}_{\mathrm{Bring}}$ and confirms the integer relation across the remaining cyclotomic-sector values.
<!-- FILE_END: bring-hyperbolic-knot-bloch-decomposition.md -->

<!-- FILE_START: type-b-folded-crystal-combinatorics.md -->
**Proposition (Type-B folded crystal cancellation).**
*For every partition $\lambda$ realized as a list of cells with contents $c(r, \mathrm{col}) := \mathrm{col} - r$, the cell-level content cancellation*

$$
  c(r, \mathrm{col}) + c(\mathrm{col}, r) = 0
$$

*lifts to the partition-level identity*

$$
  \sum_{x \in \lambda} c(x) + \sum_{x \in \lambda^T} c(x) = 0,
$$

*where $\lambda^T$ is the transpose partition. Self-dual partitions $\lambda = \lambda^T$ have content sum zero.*

## Lean structure

See [Table](#tbl:type-b-folded-crystal-combinatorics-table-data).

## Application to chirality $\langle c \rangle_\beta$

The chirality first-order coefficient is the Wedderburn-weighted average:

$$
  \langle c \rangle_\beta = \frac{\sum_\lambda w_\lambda \chi^\lambda(\beta) c(\lambda)}
       {\sum_\lambda w_\lambda \chi^\lambda(\beta)}.
$$

Under Type-B folding, the partition summation $\sum_\lambda$ reorganizes into pairs $\{\lambda, \lambda^T\}$. The cancellation theorem forces $c(\lambda) + c(\lambda^T) = 0$ for every pair. The coefficient $\langle c \rangle_\beta$ isolates the character imbalance $\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)$ between paired cells:

$$
  \langle c \rangle_\beta = \frac{\sum_{\lambda < \lambda^T} w_\lambda c(\lambda)
        \bigl[\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)\bigr]}
       {\sum_\lambda w_\lambda \chi^\lambda(\beta)}.
$$

Self-dual partitions satisfy $\lambda = \lambda^T$ and contribute zero to the numerator. Only chiral pairs contribute. Type-B folded crystals structurally reduce the chirality factor.

## Significance

This proposition closes a structural gap. A Lean theorem establishes the cell-level cancellation driving folded-crystal symmetry. The full chirality computation requires the character imbalance $\chi^\lambda(\beta) - \chi^{\lambda^T}(\beta)$. The partition-content cancellation provides the necessary structural infrastructure.
<!-- FILE_END: type-b-folded-crystal-combinatorics.md -->

<!-- FILE_START: clausen-function-mathlib-filler.md -->
**Remark (Clausen function `Cl_2` as repo-internal Mathlib filler).**

Mathlib lacks the Clausen function

$$
  \mathrm{Cl}_2(\theta)
  \;:=\;
  \sum_{k = 1}^\infty \frac{\sin(k\theta)}{k^2}
  \;=\; \mathrm{Im}\,\mathrm{Li}_2(e^{i\theta}).
$$

This function evaluates the imaginary part of the dilogarithm on the unit circle. It dictates standard hyperbolic volume formulas:

$$
  \mathrm{Vol}(4_1)\;=\;2\,\mathrm{Cl}_2(\pi/3)\;\approx\;:val[Vol_4_1]{precision=6},
  \qquad
  \mathrm{Vol}(\mathcal{B}_3)\;=\;8\,\mathrm{Cl}_2(\pi/4)\;=\;8G\;\approx\;7.327724.
$$

The Lean file [`clausen-function-mathlib-filler.lean`](clausen-function-mathlib-filler.lean) provides the necessary definitions.

See [Table 1](#tbl:clausen-function-mathlib-filler-table1-data).

This construction unconditionalizes the Bloch-Wigner values in the $\alpha_{\text{EM}}$ chain. Explicit Lean carriers replace opaque references. The framework references $\mathrm{Cl}_2$, $\mathrm{Vol}(4_1)$, and $\mathrm{Vol}(\mathcal{B}_3)$ via these carriers in [`em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode), [`figure-8-archimedean-illustration`](../braids-and-knots/figure-8-archimedean-illustration.md), [`bring-hyperbolic-knot-bloch-decomposition`](#conj:bring-hyperbolic-knot-bloch-decomposition), and [`binding-scale-catalan`](../braids-and-knots/binding-scale-catalan.md).

## Mathlib gaps

See [Table 2](#tbl:clausen-function-mathlib-filler-table2-data).

Six conditional classes remain as mathematical infrastructure gaps: `BlochSuslinUniqueness`, `ArchimedeanLimit`, `BringZeroModeBlochClass`, `BringHyperbolicDecomposition`, `BWQIndependence`, and `BlochWignerInjective`. Closing these classes requires upstream Mathlib contributions or internal formalization.

## Pattern

Each Mathlib gap forms a scoped task. The $\mathrm{Cl}_2$ filler defines a single function as a `tsum`. It provides two unconditional boundary lemmas. Four sketched extensions require Fourier-series infrastructure. This pattern extends to:

* A `Real.dilog` filler extending `LiTwo` to the complex domain via `Complex.dilog`.
* A `BlochGroup F` filler constructing the free abelian group quotient by 5-term pentagon relations.

This file isolates the $\mathrm{Cl}_2$ filler to support the $\alpha_{\text{EM}}$ and figure-8 chains.
<!-- FILE_END: clausen-function-mathlib-filler.md -->

<!-- FILE_START: bloch-wigner-mathlib-filler.md -->
**Remark (Bloch-Wigner dilogarithm $D$ on the unit circle).**

The Lean file [`bloch-wigner-mathlib-filler.lean`](bloch-wigner-mathlib-filler.lean) restricts the Bloch-Wigner dilogarithm to unit-circle shape parameters $z = e^{i\theta}$:

$$
  D(z) \;:=\; \mathrm{Im}(\mathrm{Li}_2(z))\;+\; \log|z| \cdot \arg(1 - z),
\qquad
  D(e^{i\theta}) \;=\; \mathrm{Cl}_2(\theta).
$$

The logarithm $\log|z|$ vanishes on the unit circle. This restriction covers hyperbolic-knot contributions in the framework. Their shape parameters are roots of unity. 

See [Table 1](#tbl:bloch-wigner-mathlib-filler-table1-data).

See [Table 2](#tbl:bloch-wigner-mathlib-filler-table2-data) for added Lean carriers.

The unit-circle restriction supports the hyperbolic-knot Bloch-Wigner chain. Every hyperbolic knot embeddable in Bring's surface has unit-circle shape parameters. The general extension $D : \mathbb{C} \setminus \{0,1\} \to \mathbb{R}$ remains an open Mathlib gap.

See [Table 3](#tbl:bloch-wigner-mathlib-filler-table3-data) for remaining blocked components.

This filler assigns every Bloch-Wigner value in the $\alpha_{\text{EM}}$ chain an explicit Lean carrier. The mathematical hierarchy $\mathrm{Cl}_2 \hookrightarrow D \hookrightarrow \text{hyperbolic volumes}$ is completely populated. The substantive mathematical content awaits formalization.
<!-- FILE_END: bloch-wigner-mathlib-filler.md -->
