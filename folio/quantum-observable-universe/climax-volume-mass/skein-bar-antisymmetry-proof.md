*Proof.*
The bar involution swaps $L_+ \leftrightarrow L_-$ and $q
\leftrightarrow q^{-1}$ while fixing $L_0$.  Direct substitution
gives both equalities above. $\square$

**Corollary (case-split collapse).**

Any proof in the braid--knot framework that establishes a property
$\Phi(L_+)$ for the positive crossing automatically establishes
$\Phi(L_-)$ for the negative crossing, **provided** $\Phi$ is
formulated $\overline{\,\cdot\,}$-equivariantly (i.e., $\Phi(\overline{x})
= \overline{\Phi(x)}$ on the relevant target).  The bar involution
transports the proof verbatim.

Wherever the corollary applies — a pair of positive/negative
crossing computations, a per-crossing-sign feasibility check, an
enumeration of $L_+$ and $L_-$ contributions to a state sum — the
bar-antisymmetry of (S) means those contributions enter the
analysis as **bar-paired** terms rather than independent ones.  The
case-split is pure bookkeeping.

**Connection to aether bar T-duality.**

Bar-antisymmetry of (S) is the **algebraic origin** of the
aether-level bar T-duality
([bar T-duality aether](#prop:bar-t-duality-substrate)):
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
