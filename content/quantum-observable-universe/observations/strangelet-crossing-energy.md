*Let $\mathcal{S}_N$ be a composite of $N$ baryon-number units of strange quark matter. Each unit contains one up, one down, and one strange quark in a Borromean triple $\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})$ linked by the Hopf link $\mathcal{L}_H$. We have:*

*1. Electromagnetic neutrality.*
*The Coulomb charge ([Coulomb charge](#def:coulomb-charge)) of each baryon-number unit vanishes:*
$$
  Q(\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{s}))
  =  +\tfrac{2}{3} - \tfrac{1}{3} - \tfrac{1}{3}
  =  0.
$$
*The strangelet is electromagnetically neutral for all $q > 0$. The vanishing depends only on the crossing orientation partition within the Borromean structure, evaluated on the canonical $n = 3$ word.* It is an invariant of that canonical presentation, not a topological invariant of the closure: $Q$ is writhe-derived, and the writhe shifts by $\pm 1$ under stabilisation (`QOU/StandardModel/WritheMarkovInvariance.lean`, `writhe_stabilize`). Fixing the minimal level is what makes the statement well-posed, and the Borromean word is already at its braid index.

*2. Purely strong crossing energy.*
*With $Q = 0$, the [crossing energy](#def:crossing-energy) reduces to:*
$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{S}_N)
  = 
  N \cdot \tfrac{1}{2}(n_+ + n_-)(q + q^{-1}).
$$
*There is no Coulomb correction. The entire crossing energy lies in the symmetric (strong) channel ([decomposition](#prop:crossing-energy-decomposition)).*

*3. Enhanced binding per baryon.*
*The strange quark $\mathfrak{s} \leftarrow T_{2,5}^{\sigma}$ contributes $5$ negative crossings to the Borromean braid word, versus $3$ for the down quark $\mathfrak{d} \leftarrow T_{2,3}^{\sigma}$. For each baryon unit:*

> The arrow is the [knot-particle dictionary](#tbl:knot-particle-dictionary-table4-data)'s **lepton-descent** relation, not an identity: that table gives the quark's *braid element in* $\mathcal{B}_3$ as a single generator, $\sigma_i$ for $\mathfrak{u}$ and $\sigma_i^{-1}$ for $\mathfrak{d}$, $\mathfrak{s}$ — consistent with [the up quark](#def:up-quark) being "the unknot distinguished by its environment". The crossing counts $5$ and $3$ are read off the descent partner and are unaffected.
$$
  n_-^{(\mathrm{uds})} = 3 + 5 = 8,
  \qquad
  n_-^{(\mathrm{udd})} = 3 + 3 = 6.
$$
*The binding component per baryon satisfies:*
$$
  \mathfrak{E}_{\mathrm{bind}}^{(\mathrm{uds})}
  =  8q^{-1}
   >  6q^{-1}
  =  \mathfrak{E}_{\mathrm{bind}}^{(\mathrm{udd})}.
$$
*Strange matter has strictly more strong binding per baryon than neutron matter for all $q > 0$.*
