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

**Observation 2.** The Borromean rings expand the natural compositum ([`recursive-atom-knot-atlas`](../appendix-knot-periodic-table/recursive-atom-knot-atlas.md)). Two ideal regular octahedra of shape parameter $i$ define the geometry ([`binding-scale-catalan`](../mass-theory/binding-scale-catalan.md)). The volume is $\mathrm{Vol}(\mathcal{B}_3) = 8G = 8\,\mathrm{Cl}_2(\pi/4)$. The trace field of $\mathcal{B}_3$ is $\mathbb{Q}(i) = \mathbb{Q}(\zeta_4)$. Combining the figure-8, Borromean, and Bring fields produces the compositum $\mathbb{Q}(\zeta_{60}) = \mathbb{Q}(\zeta_3, \zeta_4, \zeta_5)$. This field has degree 16 over $\mathbb{Q}$ and Bloch-group rank $r_2(\mathbb{Q}(\zeta_{60})) = 8$. The figure-8 and Borromean contributions occupy two distinct 1-dimensional lines. The remaining 6 dimensions remain available for the decomposition.

**Observation 3.** The mass-bearing spectrum supplies a finite enumeration of hyperbolic knots ([`recursive-atom-knot-atlas`](../appendix-knot-periodic-table/recursive-atom-knot-atlas.md)).

| Particle / atom | Hyperbolic knot / link | Volume | Trace field |
|---|---|---|---|
| Proton, neutron | $\mathcal{B}_3$ Borromean | $8G \approx 7.328$ | $\mathbb{Q}(i)$ |
| Deuteron $^2$H | $6_2$ | $\approx 4.401$ | quartic field over $\mathbb{Q}$ |
| Tritium $^3$H | $8_{11}$ | $\approx 8.286$ | sextic field |
| $^3$He | $L_{6a4}$ (link) | $\approx 7.328$ | $\mathbb{Q}(i)$ |
| Higgs / mass mechanism | $4_1$ figure-8 | $\approx 2.030$ | $\mathbb{Q}(\zeta_3)$ |

The $^4$He formula contributes via $8G$ algebraically. Trace fields beyond degree 2 enlarge the compositum. The field for $6_2$ is quartic. The field for $8_{11}$ is sextic. Including all hyperbolic knots in the spectrum forces a natural compositum of at least $\mathbb{Q}(\zeta_{60})$. The $S_5$-equivariance constraint identifies knots that embed in Bring's surface. The figure-8 and Borromean knots admit such embeddings. Higher isotope knots inherit $S_5$-equivariance via the binding-operator $\oplus$ structure.

**Observation 4.** The electroweak knot operators $W \leftrightarrow \sigma_1^4 \to T(2,4)$, $Z \leftrightarrow \sigma_3^6 \to T(2,6)$, and $H \leftrightarrow \sigma_5^8 \to T(2,8)$ ([`ew-interface-knot`](../braids-and-knots/ew-interface-knot.md), [`categorical-higgs-mechanism`](../mass-theory/categorical-higgs-mechanism.md)) and the strong-force pair $T(2,9)$ and $T(3,5)$ ([$(T_{2,9}, T_{3,5})$ is the unique pair of genus-$4$ torus knots](#prop:force-carrier-bring-uniqueness)) are torus links. These links are Seifert-fibered and non-hyperbolic. They lack ideal-tetrahedron triangulations. They contribute zero to the Bloch-Wigner image $D \colon B(F)\otimes\mathbb{Q} \to \mathbb{R}^{r_2(F)}$. Only mass-bearing knots carry Bloch-Wigner content.

**Observation 5.** The five atlas entries $\{4_1, \mathcal{B}_3, 6_2, 8_{11}, L_{6a4}\}$ represent established particles. The Bloch-Wigner image is generated by the closures of all normal-form basis triple products $b_i \cdot \beta(T_{m,n}) \cdot b_j$ across the relevant Hecke algebras $H_n(q)$ ([Knot operators are selected per confinement by the Frobenius Gram-inverse LP/SDP dual basis](#prop:knot-operator-lp-selection)). The normal-form basis for $H_3(q)$ is six-dimensional. Products with the torus operators $T_{1,0}, T_{2,1}, T_{2,2}, T_{2,3}$, and $T_{2,5}$ generate demand-channel identifiers. The normal-form basis grows polynomially at higher $n$. The closure space includes many hyperbolic knots beyond the five atlas entries. The dimension of the accessible sub-space inside $B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$ is not bounded by 5. The rank-8 ambient image is reachable through normal-form basis closures.

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
  {{ qou.computations.q-pinning-50-digit.calibration_inputs.Vol_4_1_str | precision: 6 }}\ldots
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

The algebraic constraints are as follows:

- $r_2(\mathbb{Q}(\zeta_n)) = \varphi(n)/2$.
- Concrete values: $r_2(\mathbb{Q}(\zeta_3)) = r_2(\mathbb{Q}(\zeta_4)) = 1$, $r_2(\mathbb{Q}(\zeta_5)) = r_2(\mathbb{Q}(\zeta_{12})) = 2$, $r_2(\mathbb{Q}(\zeta_{15})) = 4$, $r_2(\mathbb{Q}(\zeta_{60})) = 8$.
- $r_2(\mathbb{Q}(\zeta_{15})) = r_2(\mathbb{Q}(\zeta_3)) + r_2(\mathbb{Q}(\zeta_5)) + 1$.
- $r_2(\mathbb{Q}(\zeta_{60})) = r_2(\mathbb{Q}(\zeta_{15})) + r_2(\mathbb{Q}(\zeta_4)) + 3$.
- $2/(3\pi)$ is positive, hence nonzero.
- The existence of the finite multi-set $\{(K_i, n_i)\}$ is taken as a hypothesis; it is not established.
- Conditional on that decomposition, the Bloch-group class realising the zero mode exists.
- The linear independence of $\{2/(3\pi), \mathrm{Cl}_2(\pi/3), \mathrm{Cl}_2(\pi/4)\}$ over $\mathbb{Q}$ is taken as a hypothesis; it is not established.
- Conditional on that independence hypothesis, no $\mathbb{Z}$-linear combination of $D[Z_{4_1}]$ and $D[Z_{\mathcal{B}_3}]$ equals $2/(3\pi)$.

The decomposition requires at least one hyperbolic knot beyond the figure-8 and Borromean rings. The remaining task identifies $\mathcal{K}_{\mathrm{Bring}}$ and confirms the integer relation across the remaining cyclotomic-sector values.
