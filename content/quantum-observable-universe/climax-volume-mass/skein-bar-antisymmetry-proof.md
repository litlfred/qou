*Proof.*
The bar involution swaps $L_+ \leftrightarrow L_-$ and $q
\leftrightarrow q^{-1}$ while fixing $L_0$.  Direct substitution
gives both equalities above. $\square$

**Refactoring corollary (case-split collapse).**

Any proof in the braid--knot framework that establishes a property
$\Phi(L_+)$ for the positive crossing automatically establishes
$\Phi(L_-)$ for the negative crossing, **provided** $\Phi$ is
formulated $\overline{\,\cdot\,}$-equivariantly (i.e., $\Phi(\overline{x})
= \overline{\Phi(x)}$ on the relevant target).  The bar involution
transports the proof verbatim.

Concretely, several existing case-split arguments in
`braids-and-knots/` can be collapsed using this principle:

| Block | Current structure | Simplification |
|-------|-------------------|----------------|
| `commutative-crossing-energy` | separate positive/negative crossing computations | one computation + bar-apply |
| `phase-scoped-applicability` | per-crossing-sign Slater feasibility | one feasibility check + bar-apply |
| Jones-polynomial state-sum decomposition | $L_+$ and $L_-$ contributions enumerated | bar-equivariant sum |

In each case, the bar-antisymmetry of (S) means the contributions
from $L_+$ and $L_-$ enter the analysis as **bar-paired** terms,
not independent ones.  The case-split is bookkeeping, not new
content.

**Connection to substrate bar T-duality.**

Bar-antisymmetry of (S) is the **algebraic origin** of the
substrate-level bar T-duality
([bar T-duality substrate](#prop:bar-t-duality-substrate)):
the Markov trace $\mathrm{tr}_M \colon H_n(q) \to \mathbb{C}(q)$
commutes with $\overline{\,\cdot\,}$ up to sign on antisymmetric
elements, so the geometric bar-pairing on the moduli of
$\mathcal{E}_q$ inherits its sign structure from (S).

**Categorical statement.**

The bar involution defines a contravariant functor
$\overline{\,\cdot\,} \colon H_n(q) \to H_n(q^{-1})^{\mathrm{op}}$
sending each generator $\sigma_i$ to $\sigma_i^{-1}$ in the opposite
algebra.  The Skein relation is the assertion that this functor
intertwines the two crossing types, with the sign flip in (S)
encoding the antisymmetry.
