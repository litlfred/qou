*Proof.*
The bar involution swaps $L_+ \leftrightarrow L_-$ and $q \leftrightarrow q^{-1}$ while fixing $L_0$. Direct substitution gives both equalities. $\square$

**Refactoring corollary (case-split collapse).**

Any proof in the braid-knot framework establishing a property $\Phi(L_+)$ for the positive crossing automatically establishes $\Phi(L_-)$ for the negative crossing, provided we formulate $\Phi$ $\overline{\,\cdot\,}$-equivariantly, meaning $\Phi(\overline{x}) = \overline{\Phi(x)}$. The bar involution transports the proof verbatim.

Concretely, we can collapse several case-split arguments in `braids-and-knots/`:

| Block | Current structure | Simplification |
|-------|-------------------|----------------|
| `commutative-crossing-energy` | separate positive/negative crossing computations | one computation + bar-apply |
| `phase-scoped-applicability` | per-crossing-sign Slater feasibility | one feasibility check + bar-apply |
| Jones-polynomial state-sum decomposition | $L_+$ and $L_-$ contributions enumerated | bar-equivariant sum |

The bar-antisymmetry of (S) requires contributions from $L_+$ and $L_-$ to enter as bar-paired terms, not independent ones. The case-split is merely bookkeeping.

**Connection to substrate bar T-duality.**

Bar-antisymmetry of (S) is the algebraic origin of the substrate-level bar T-duality ([bar T-duality substrate](#prop:bar-t-duality-substrate)). The Markov trace $\mathrm{tr}_M \colon H_n(q) \to \mathbb{C}(q)$ commutes with $\overline{\,\cdot\,}$ up to sign on antisymmetric elements. The geometric bar-pairing on the moduli of $\mathcal{E}_q$ inherits its sign structure from (S).

**Categorical statement.**

The bar involution defines a contravariant functor $\overline{\,\cdot\,} \colon H_n(q) \to H_n(q^{-1})^{\mathrm{op}}$ sending each generator $\sigma_i$ to $\sigma_i^{-1}$ in the opposite algebra. The Skein relation asserts that this functor intertwines the two crossing types. The sign flip in (S) encodes the antisymmetry.
