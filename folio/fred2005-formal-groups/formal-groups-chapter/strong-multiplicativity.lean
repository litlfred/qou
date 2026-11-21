/-!
# Strong multiplicativity — formalised in the library

Sibling of content block
[`def:strong-multiplicativity`](strong-multiplicativity.md), Def. 1.11 of
arXiv:math/0602138. The condition is stated in the library file
`Fred2005/StrongMultiplicativity.lean` as
`Fred2005.StrongMult.IsStronglyMultiplicative μ Δ π`, which is what this
block's `lean.ref` names. There `μ` is the ordered product `·` of `S = ⊗ A_i`
transported to the splay `T` (not the product of `T`), `Δ` the comultiplication
and `π` the Poisson structure. The same file proves Remark 1.12: on primitive
elements the condition says that `π(x, y)` is primitive.

This sibling carries no declaration of its own, so it does not shadow the
library one.

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Def. 1.11, Remark 1.12.
-/
