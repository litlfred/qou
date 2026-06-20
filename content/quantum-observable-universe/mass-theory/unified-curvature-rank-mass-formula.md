*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition (mass as a single sum over curvature-rank strata).**

*Per [spectral sequence collapse](#prop:spectral-sequence-collapse)
and [curvature-rank stratification](#prop:curvature-rank-gb-stratification),
the categorical mass of a knot $\mathcal{K}$ probed by test element
$\mathcal{T} \in A = H_n(R, q)$ decomposes as a single sum over
GB-filtration depths $k = 0, 1, \ldots, n - 1$:*

$$
  \boxed{\;
    \mathfrak{m}_{q,\mathcal{K}}(\mathcal{T})
    \;=\; \sum_{k = 0}^{n - 1} \alpha_k \cdot \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T}),
    \qquad
    \mathfrak{m}^{(k)}_{q,\mathcal{K}}(\mathcal{T})
    \;=\; \!\!\sum_{\substack{\lambda \,\vdash\, n \\ \mathrm{depth}(\lambda) = k}}\!\!
      \tilde w_\lambda \cdot \log\Bigl|\!\int_{A_\lambda}\!\rho(\beta_\mathcal{K}) \cdot \mathcal{T}\Bigr|
  \;}
$$

*with $\alpha_k$ stratum-dependent prefactors, $A_\lambda = e_\lambda A
e_\lambda$ the Wedderburn block, and $\tilde w_\lambda = \dim_q^2
V_\lambda / [n]_q!$ the **q-deformed Wedderburn-block weight**
([prop:wedderburn-weight-canonical](#prop:wedderburn-weight-canonical)).
The classical Plancherel measure $w_\lambda = (\dim V_\lambda)^2/n!$
([prop:plancherel-weight-boundedness](#prop:plancherel-weight-boundedness))
satisfies $\sum_\lambda w_\lambda = 1$ exactly; the q-deformed
analogue $\tilde w_\lambda$ has $\sum_\lambda \tilde w_\lambda$
finite but generally $\neq 1$ at $q \neq 1$ (empirically $\approx
1.51$ at $q_0, n = 12$). The two coincide at $q = 1$.*

*The total mass is the sum, with $\mathcal{T} = 1$:*
$\mathfrak{m}_{q,\mathcal{K}} := \mathfrak{m}_{q,\mathcal{K}}(1)$.
*Low-tower and high-tower partial sums are abbreviated*
$\mathfrak{m}^{<k}_{q,\mathcal{K}}(\mathcal{T})$ *and*
$\mathfrak{m}^{\geq k}_{q,\mathcal{K}}(\mathcal{T})$ *respectively.*

*Proof.*

By [spectral sequence collapse](#prop:spectral-sequence-collapse),
$\mathrm{HH}^k(H_n(R, q)) = 0$ for $k \geq 1$ at generic $q$, so only
$\mathrm{HH}^0 = Z(H_n(R, q)) = \bigoplus_\lambda R \cdot e_\lambda$
survives the GB-filtration spectral sequence. By
[curvature-rank stratification](#prop:curvature-rank-gb-stratification),
$e_\lambda$ has GB-depth $\mathrm{depth}(\lambda)$, so the centre
splits as $Z = \bigoplus_{k} Z_k$ with $Z_k$ the depth-$k$ direct
summand. The block-restricted Frobenius integral
$\int_{A_\lambda} = \int_A \circ\, e_\lambda$
([Markov–Frobenius pairing](#conj:knot-factor-frobenius-pairing))
extracts the $\lambda$-component. Wedderburn-weighted logarithms of
those components, binned by depth, give the $\mathfrak{m}^{(k)}$
functionals. $\square$

**Mapping to the historical "six terms + Term 7" labelling.**
*Earlier drafts named seven terms; in the unified picture each maps
to a curvature-rank stratum or partial sum:*

See [Table](#tbl:unified-curvature-rank-mass-formula-table-data).

*The Term 6 / Term 7 split is historical: Term 6 was originally a
catch-all "jet-prefix at depth $\geq 3$" before stratum-by-stratum
decomposition was available. In the unified picture, Term 6 $=
\mathfrak{m}^{(3)}$ and Term 7 $= \mathfrak{m}^{\geq 4}$ are two
adjacent strata of the same tower. Future work should reference
$\mathfrak{m}^{(k)}$ uniformly.*

**Chirality / non-chirality refinement.**

*Per [prop:chirality-residue-mass-term](#prop:chirality-residue-mass-term),
the mass tower further splits along the signed-content predicate
$c_\lambda = 0$ (chirality cells, where $D_q^2(\lambda) = 0$):*

$$
  \mathfrak{m}_{q,\mathcal{K}}(\mathcal{T})
  \;=\;
  \mathfrak{m}^{\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T})
  \;+\;
  \mathfrak{m}^{\neg\mathrm{chir}}_{q,\mathcal{K}}(\mathcal{T}).
$$

*The chirality part is the gauge-invariant background contribution
([rem:confinement-curvature-rank](#rem:confinement-curvature-rank));
empirically it accounts for $\sim 3\%$ of the binding energy of $^4$He
([atomic_chirality_residue.py witness](#)) and dominates the deepest
curvature-rank strata.*
