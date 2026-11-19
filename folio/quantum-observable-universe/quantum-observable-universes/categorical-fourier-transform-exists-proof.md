The proof strategy is constructive. Forming the operator $\mathcal{F}[f](\xi) = \mathrm{tr}_M(\exp_q(i \xi \cdot) \cdot f)$ explicitly via the categorical trace and the quantum exponential yields a map satisfying all monoidal functor properties required for the categorical Fourier transform.

Identical to
([existence of categorical Laplace transform](#prop:categorical-laplace-exists))
with the substitution $s \mapsto -i\xi$: the grouplike
$\exp_q(i\xi\cdot)$ exists for every categorical spectrum value
$\xi \in \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, A^\vee)$, and pairing
against the Markov trace yields a well-defined :refterm[monoidal functor]{#monoidal-functor}.
Equivalently, $\mathcal{F}[f](\xi) = \mathcal{L}[f](-i\xi)$ (Wick
rotation) inherits existence from the Laplace case.
