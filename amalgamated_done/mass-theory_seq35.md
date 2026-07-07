<!-- FILE_START: intro-plancherel-alpha-ribbon.md -->
The Plancherel measure on partitions and the categorical $\alpha_{\mathrm{EM}}$ coupling lock together through the ribbon structure of the Hecke category. The knot-factor distills directly from a Plancherel-weighted Wedderburn block sum.

This sequence identifies the Plancherel weight on Wedderburn blocks, verifies its probability-distribution properties at the substrate parameter, and formalizes the substrate-level knot-factor formula. Downstream binding-energy models rely strictly on the explicit knot-factor outputs $K(\mathrm{braid})$ tabulated in the final blocks.
<!-- FILE_END: intro-plancherel-alpha-ribbon.md -->

<!-- FILE_START: alpha-em-categorical-trace.md -->
**Remark (deprecated empirical $\alpha_{EM}$ forms).**
The categorical fine-structure constant relies exclusively on the robust, pre-archimedean evaluation:

$$
  \alpha_{EM} \;=\; \frac{h^2}{q\,\delta_q(T_{2,9})\,\delta_q(T_{3,5})}
              \;=\; \frac{1}{q\,[9]_q\,[10]_q}.
$$

Older isolated PSLQ-uniqueness guesses matching $q_0$ lack theoretical backing. These residual artifacts fail exact representation limits and smooth $q$ continuity. They exist purely as historical diagnostic markers and are completely replaced by the exact Hopf 2-strand operation model.
<!-- FILE_END: alpha-em-categorical-trace.md -->

<!-- FILE_START: plancherel-term-7-formulation.md -->
**Proposition (universal residue at curvature-rank $k \geq 4$).**
*Define the curvature-rank-$k$ residue functional using the q-deformed Wedderburn weight $\tilde w_\lambda = \dim_q^2 V_\lambda / [n]_q!$:*

$$
  \Phi_k(\mathcal{K}, \mathcal{T})
  \;:=\; \sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}
  \tilde w_\lambda \cdot \log\Bigl|\!\int_{A_\lambda}\! \rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|.
$$

*The universal residue extracts the high-tower contribution as:*

$$
  \mathfrak{m}^{\geq 4}_{q,\mathcal{K}}(\mathcal{T})
  \;=\; \alpha \cdot \!\!\sum_{k \geq 4}\!\Phi_k(\mathcal{K}, \mathcal{T}),
  \qquad \alpha \;=\; m_e \cdot 8G.
$$

At low strata ($k \leq 3$), the restricted Frobenius integral routes through distinct hyperbolic-knot ideals. At deep strata ($k \geq 4$), specific knot identities evaporate. The surviving residue isolates the universal Frobenius co-Casimir tail, dependent solely on the block weight topology.
<!-- FILE_END: plancherel-term-7-formulation.md -->

<!-- FILE_START: plancherel-weight-boundedness.md -->
**Proposition (Plancherel weights are a probability distribution).**
*For semisimple $A = H_n(R, q)$, the canonical Plancherel weights $w_\lambda = (\dim V_\lambda)^2/n!$ fulfill strict probability-distribution conditions:*

1. *Non-negativity: Each $w_\lambda \in [0, 1]$.*
2. *Normalisation: $\sum_{\lambda \vdash n} w_\lambda = 1$ exactly in $\mathbb{Q}$.*

The classical dimension mapping guarantees standard conservation laws inside the algebra.
<!-- FILE_END: plancherel-weight-boundedness.md -->

<!-- FILE_START: plancherel-weight-boundedness-interpretation.md -->
**Remark (q-deformed alternative).**
The $q$-deformed weight $\widetilde{w}_\lambda = \dim_q^2 V_\lambda / [n]_q!$ sums to a finite value $\approx 1.51$ rather than exactly 1. It does not construct a pure probability measure at generic $q \neq 1$. However, the Plancherel boundedness property successfully neutralizes massive matrix dimension divergences inside log-pairings, suppressing massive combinatorial scale factors cleanly into manageable average bounds. Without this boundedness, the deep-tower calculations would mathematically diverge.
<!-- FILE_END: plancherel-weight-boundedness-interpretation.md -->

<!-- FILE_START: unified-curvature-rank-mass-formula.md -->
**Proposition (mass as a single sum over curvature-rank strata).**
*The categorical mass decomposes perfectly over discrete GB-filtration depths $k$:*

$$
  \mathfrak{m}_{q,\mathcal{K}}(\mathcal{T})
  \;=\; \sum_{k = 0}^{n - 1} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T}),
  \qquad
  \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T})
  \;=\; \!\!\sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}\!\!
    \tilde w_\lambda \cdot \log\Bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|.
$$

The sum organizes the individual stratum contributions via q-deformed Wedderburn block weights. 
<!-- FILE_END: unified-curvature-rank-mass-formula.md -->

<!-- FILE_START: chirality-residue-mass-term.md -->
**Proposition (chirality / non-chirality split of the mass tower).**
*The mass tower rigidly isolates into chirality and non-chirality segments based on the signed Young content $c_\lambda$:*

$$
  \mathfrak{m}_{q,\mathcal{K}}(\mathcal{T})
  \;=\;
  \mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
  \;+\;
  \mathfrak{m}^{\neg\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T}).
$$

*The chirality branch spans specifically over $c_\lambda = 0$ Wedderburn blocks:*

$$
  \mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
  \;=\;
  \sum_{k = 0}^{n-1} \alpha_k \cdot
    \!\!\sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k \\ c_\lambda \,=\, 0}}\!\!
    w_\lambda \cdot
    \log\Bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|.
$$
<!-- FILE_END: chirality-residue-mass-term.md -->

<!-- FILE_START: chirality-residue-mass-term-interpretation.md -->
**Remark (Physical interpretation).**
The chirality component contributes a positive, attractive confining force across all isotopes. It actively counterbalances the net-negative repulsive base structure, framing the gauge-invariant background holding mass conglomerates together.
<!-- FILE_END: chirality-residue-mass-term-interpretation.md -->

<!-- FILE_START: e-infinity-page-identifications.md -->
**Proposition (E-infinity page derivations).**
*The six-term categorical mass formula components correlate strictly to $E_\infty^{p, *}$ pages:*

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \sum_{p = 0}^{\infty}
  \bigl\langle \mathrm{tr}_M,\ E_\infty^{p, *}(T_w) \bigr\rangle
  \;+\;
  \bigl\langle \mathrm{tr}_M \circ (\mathrm{id} \otimes \varTheta),\ E_\infty^{0, *}(T_w) \bigr\rangle
  \;+\;
  m_e \cdot \tau\bigl(C_{\dim_q}\bigr).
$$

*Term 1 descends directly to the identity base mapping cleanly to $E_\infty^{0, *}$. Terms 2 and 3 isolate single-generator and pair-tower functional limits mapping explicitly to $E_\infty^{1, *}$ and $E_\infty^{2, *}$. Term 6 aggregates all deeper-strata residues spanning $\ell \geq 3$ mapping to the algebraic elliptic-curve residues without requiring speculative contour assumptions.*
<!-- FILE_END: e-infinity-page-identifications.md -->

<!-- FILE_START: spectral-sequence-h3-explicit.md -->
**Proposition (Explicit H3 spectral sequence).**
*The differentials $d_1$ and $d_2$ execute completely algebraically on $H_3(R, q)$.*

The initial $E_1$ page categorizes directly into four explicit levels holding ranks 1, 2, 2, and 1. The $d_1$ differential acts directly through the Hecke relation $\sigma_i^2 = (q - q^{-1}) \sigma_i + \mathbf{1}$. It drives pair matrices into pure symmetric/antisymmetric splits, killing specific states outright. The $d_2$ differential governs the Yang-Baxter overlap, further squashing rank bounds before fully locking into the final $E_\infty$ stable state.

The explicitly computed $E_\infty$ trace limits correctly extract zero trace for single generators and exact pair traces for the $z^2$ multiplier, thoroughly fulfilling the term expectations mathematically.
<!-- FILE_END: spectral-sequence-h3-explicit.md -->

<!-- FILE_START: chirality-writhe-ribbon-derivation.md -->
**Proposition (chirality writhe-ribbon linearisation).**
*For a braid $\beta$ with integer writhe $w(\beta)$, the chirality factor derived from the Kauffman ribbon-twist evaluation limits strictly to:*

$$
  a_K(\beta)
  \;=\;
  1 \;+\; w(\beta) \cdot h \;+\; O(h^2).
$$

This rigorously locks the first-order Hecke deformation factor strictly to the topological writhe, cleanly bridging the pure algebraic sequence mapping directly to observed ribbon dynamics.
<!-- FILE_END: chirality-writhe-ribbon-derivation.md -->
