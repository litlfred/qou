*Let $\mathcal{S}_N$ be a composite of $N$ baryon-number units of strange quark matter. Each unit contains one up, one down, and one strange quark in a Borromean triple $\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{s})$ linked by the Hopf link $\mathcal{L}_H$. Then:*

*1. Electromagnetic neutrality.*
*The Coulomb charge ([Coulomb charge](#def:coulomb-charge)) of each baryon-number unit vanishes:*
$$
  Q(\mathcal{B}_3(\mathfrak{u}, \mathfrak{d}, \mathfrak{s}))
  =  +\tfrac{2}{3} - \tfrac{1}{3} - \tfrac{1}{3}
  =  0.
$$
*The strangelet is electromagnetically neutral for all $q > 0$. The vanishing depends only on the crossing orientation partition within the Borromean structure, evaluated on the canonical $n = 3$ word.* It is an invariant of that canonical presentation, not a topological invariant of the closure: $Q$ is writhe-derived, and the writhe shifts by $\pm 1$ under stabilisation. Fixing the minimal level is what makes the statement well-posed, and the Borromean word is already at its braid index.

*2. Purely antisymmetric crossing energy.*
*With $Q = 0$ the symmetric channel vanishes and the [crossing energy](#def:crossing-energy) reduces to:*
$$
  \mathfrak{E}_{\mathrm{cross}}(\mathcal{S}_N)
  =
  N \cdot \tfrac{1}{2}(n_+ + n_-)(q - q^{-1}).
$$
*The entire crossing energy lies in the antisymmetric channel ([decomposition](#prop:crossing-energy-decomposition)): the symmetric multiplicity is the writhe $n_+ - n_-$, which is what $Q = 0$ annihilates, while the antisymmetric multiplicity is the crossing count $n_+ + n_-$, which $Q = 0$ leaves untouched.*

> **Open.** Under this assignment the strangelet has *zero* symmetric content and *maximal* antisymmetric content, which is the opposite of the physical reading in items 1 and 3. Whether "electromagnetic neutrality" survives, and whether the enhanced-binding argument below still follows, requires re-deriving those items rather than relabelling them — the identification of the antisymmetric channel with electromagnetism is itself [not established](#def:coulomb-charge).
>
> **Separately: the $Q$ values used in item 1 are not representable.** [The Coulomb charge](#def:coulomb-charge) is $\tfrac{1}{2}(n_+ - n_-) \in \tfrac{1}{2}\mathbb{Z}$, so $+\tfrac{2}{3}$ and $-\tfrac{1}{3}$ are outside its range for every braid word. Item 1 computes $Q$ from assigned quark charges rather than from crossing counts, so the two are distinct quantities sharing a symbol. The vanishing of the *sum* is unaffected, but it is not a statement about the crossing-count $Q$ that item 2 uses.

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
