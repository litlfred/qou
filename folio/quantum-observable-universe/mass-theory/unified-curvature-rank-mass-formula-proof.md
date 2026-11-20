*Proof.*

By [spectral sequence collapse](#prop:spectral-sequence-collapse),
$\mathrm{HH}^k(H_n(R, q)) = 0$ for $k \geq 1$ at generic $q$, so only
$\mathrm{HH}^0 = Z(H_n(R, q)) = \bigoplus_\lambda R \cdot e_\lambda$
survives the GB-filtration spectral sequence.
[Curvature-rank stratification](#prop:curvature-rank-gb-stratification)
stratifies $H_n(R, q)$ by the curvature rank of **words**; that
$e_\lambda$ carries a GB-depth $\mathrm{depth}(\lambda)$ indexed by the
*partition* is a further identification, not stated there and assumed
here.
Granting it, the centre splits as $Z = \bigoplus_{k} Z_k$ with $Z_k$ the
depth-$k$ direct summand. The block-restricted Frobenius integral
$\int_{A_\lambda} = \int_A \circ\, e_\lambda$
([Markov–Frobenius pairing](#conj:knot-factor-frobenius-pairing))
extracts the $\lambda$-component. Wedderburn-weighted logarithms of
those components, binned by depth, give the $\mathfrak{m}^{(k)}$
functionals. $\square$

**Mapping to the "six terms + Term 7" labelling.**
*The seven named terms each map to a curvature-rank stratum or
partial sum:*

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

*The chirality part is the gauge-invariant background contribution;
empirically it accounts for $\sim 3\%$ of the binding energy of $^4$He
(the formal derivation witness) and dominates the deepest
curvature-rank strata.*
