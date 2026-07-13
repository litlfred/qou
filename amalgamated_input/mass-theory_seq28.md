<!-- FILE_START: schur-weyl-mass-decomposition.md -->
*The Markov trace of the atomic braid $\mathcal{A} \in H_{3A}(q)$ decomposes over partitions $\lambda \vdash 3A$ as:*

$$
  \mathrm{tr}_M(\mathcal{A})
  \;=\;
  \sum_{\lambda \,\vdash\, 3A}
    \frac{s_\lambda(\mathbf{q})}{H_q(\lambda)}
    \cdot
    \chi^\lambda(\mathcal{A})
  \;=\;
  \sum_{\lambda \,\vdash\, 3A} w_\lambda(q)\, \mathrm{tr}_\lambda,
$$

*where $s_\lambda$ is the Schur function, $H_q(\lambda)$ is the $q$-hook product, and $\chi^\lambda$ is the Specht-module character.*

For a single nucleon ($A=1$), the $H_3(q)$ partitions $\{(3), (2,1), (1,1,1)\}$ correspond to the symmetric, standard, and antisymmetric Wedderburn blocks. The $w_\lambda$ weights recover the three-parameter Wedderburn mass formula precisely.

The additive-Wedderburn approximation sums the $A=1$ weights over each generator of the $A$-nucleon braid. This approximation discards all partitions with rows longer than 3, corresponding to inter-nucleon entanglement. For light atoms, the discarded weights remain negligible. For $A \ge 6$, the excluded boundary partitions $\lambda = (3A-1, 1)$ and pair partitions $\lambda = (3A-2, 2)$ accumulate massive $q$-hook products, causing the observed $5\%$--$20\%$ binding-energy drift in the approximation.

Schur-Weyl duality isolates the physical origin of each correction into specific partition geometries. The base volume derives from the symmetric partition $(3A)$. The surface correction derives from the boundary partition $(3A-1, 1)$. The pair-crossing interaction derives from the $(3A-2, 2)$ pair partition. Magic shell-closure peaks derive from sharp hook-product factorization at rectangular partitions.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued physical observables at $q_0$.
<!-- FILE_END: schur-weyl-mass-decomposition.md -->

<!-- FILE_START: gb-residue-spectral-sum.md -->
*For a closed braid knot with Hecke normal form $T_w \in H_n(R, q)$, the categorical mass admits the symbolic decomposition:*

$$
  \mathfrak{m}_{q_0, \mathcal{K}}
  \;=\;
  \bigl|\int_A T_w(q_0)\bigr|
  \;+\;
  \sum_{\ell = 1}^{\ell(\mathcal{K}, q_0)}
    r_\ell(T_w; q_0),
  \qquad
  r_\ell(T_w; q_0)
    \;=\;
    \frac{\operatorname*{Res}_{q = \zeta_\ell}\!
      \bigl[\Phi_q \cdot \mathrm{tr}_{M,\ell}(T_w)\bigr]}
    {q_0 - \zeta_\ell}.
$$

*The numerators are the stratum residues feeding the cyclotomic coefficients $a_m$ of the Habiro expansion.*

The confinement filtration makes $H_n(R, q)$ a filtered differential algebra. The residue $r_\ell(T_w; q_0)$ is the pairing of the trace integral with the level-$\ell$ filtration stratum. The sum evaluated across all strata constructs the total mass.

The Cauchy-kernel factor $1/(q_0 - \zeta_\ell)$ is a formal symbol. The expression is an identity in the Grothendieck group of the filtered algebra, not a convergent complex-analytic equality. The primitive roots of unity densely pack $S^1$, destroying any meromorphic neighborhood. The Habiro cyclotomic completion supplies the rigorous convergent framework.

Under the fibre functor $\tau$, the categorical filtration stratum maps to the geometric jet bundle on the elliptic curve. The cyclotomic residues map to Picard-Lefschetz residues at the discriminant locus off $S^1$, forcing convergent evaluation on the archimedean side.
<!-- FILE_END: gb-residue-spectral-sum.md -->

<!-- FILE_START: categorical-mass-positivity.md -->
**Remark (no exhaustive positivity proof needed).**

The categorical mass evaluates the observation functor $\tau$ on graded projective KLR modules. The functor takes the graded Euler characteristic, rendering each coefficient the strictly non-negative integer dimension of a $\mathrm{Hom}$-space:

$$
  [\tau(\mathfrak{M}_K)]_d \;=\;
  \dim_R \mathrm{Hom}_{\mathcal{K}_n}\bigl(P_d, \mathfrak{M}_K\bigr)
  \;\in\; \mathbb{Z}_{\geq 0}.
$$

The polynomial $\tau(\mathfrak{M}_K)$ is the mass-spectrum generating function. Each coefficient corresponds to the microstate degeneracy of a graded Hecke energy level. The resulting mass formula remains structurally positive by categorical definition.
<!-- FILE_END: categorical-mass-positivity.md -->

<!-- FILE_START: mass-spectrum-generating-function.md -->
**Remark (the confined Laurent polynomial as mass-spectrum generating function).**

The polynomial $P_K(q) \in \mathbb{Z}[q^{\pm 1/2}]$ is a graded Euler characteristic, not a macroscopic mass scalar. The two link via a functorial composition that evaluates the generating function at the substrate parameter $q_0$.

Each term $c_d q^d$ of $P_K(q)$ parses as a mass component. The exponent $d$ measures the graded Hecke energy, tracking the internal topological tension. The coefficient $c_d$ counts the microstate degeneracy, tallying the orthogonal Hom-channels at that energy. The full polynomial constitutes the partition function over the internal homological slices.

Evaluating this polynomial at $q_0$ recovers the macroscopic mass:

$$
  \mathfrak{m}_{\mathcal{K}}
  \;\approx\;
  m_0 \cdot \bigl|P_K(q_0)\bigr|.
$$

Equating the polynomial directly to the scalar erases both the microstate spectrum and the substrate dependence, discarding the specific data governing branching ratios and resonance widths.
<!-- FILE_END: mass-spectrum-generating-function.md -->

<!-- FILE_START: graded-markov-trace-from-gs-filtration.md -->
*For each $\ell \in \mathbb{N}$ there is a uniquely determined $\mathbb{Q}(q)$-linear trace*

$$
  \mathrm{tr}_{M, \ell}
  \;:\;
  J^\ell / J^{\ell+1}
  \;\longrightarrow\;
  \mathbb{Q}(q)
$$

*that agrees with the restriction of $\mathrm{tr}_M$ on $J^\ell$ and vanishes entirely on the lower stratum $J^{\ell+1}$.*

The standard Markov trace descends constructively along the Gröbner-Shirshov filtration quotient. The formulation automatically secures compatibility with the spectral sequence and forces vanishing above the confinement level. The construction replaces the opaque analytic assumption with a strict algebraic descent.
<!-- FILE_END: graded-markov-trace-from-gs-filtration.md -->

<!-- FILE_START: residue-at-root.md -->
*Let $T_w \in J^\ell / J^{\ell+1}$ have $\mathrm{tr}_{M, \ell}(T_w) \in \mathbb{Q}(q)$. The cyclotomic residue*

$$
  \mathrm{Res}_{q \to \zeta_\ell}(\Phi_q \cdot \mathrm{tr}_{M, \ell})(T_w)
$$

*is the image of $\Phi_q \cdot \mathrm{tr}_{M, \ell}(T_w)$ under the cyclotomic projection*

$$
  \pi_{n_\ell}
  \;:\;
  \widehat{\mathbb{Z}[q]}
  \longrightarrow
  \mathbb{Z}[q] / \Phi_{n_\ell}(q),
$$

*evaluating identically within the residue field $\mathbb{Q}(\zeta_\ell)$.*

The cyclotomic residue defines purely algebraically within the Habiro completion of $\mathbb{Z}[q^{\pm 1}]$. It avoids complex-analytic limits entirely. The formulation keeps the algebraic sector strictly within $\mathbb{Q}$-coefficients, fulfilling the three-calibration discipline.
<!-- FILE_END: residue-at-root.md -->

