**Proposition (binding and $\beta$-decay are the two bar-parities of one element).**

The bar-involution $\sigma$ ($q \mapsto q^{-1}$, $\sigma^2 = \mathrm{id}$;
[`def:bar-involution`](#def:bar-involution)) splits every element into a
$\sigma$-fixed **even** part and a $\sigma$-anti **odd** part:
$$
\mathrm{even}(x) = x + \sigma x \ (\sigma\text{-fixed}), \qquad
\mathrm{odd}(x) = x - \sigma x \ (\sigma\text{-anti}), \qquad
\mathrm{even}(x) + \mathrm{odd}(x) = 2x .
$$

Applied to the fibre Habiro element $F$ controlling the substrate, the two
parities carry the two observables:

- **even ($\cosh$, bar-symmetric)** — the binding trace
  $\tau = \operatorname{tr} B$ of
  [`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence) (the
  curvature-free transport, $(q+q^{-1})/2 = \cosh\lambda$);
- **odd ($\sinh$, bar-antisymmetric)** — the $Q_\beta$ residue-A / $c_k$ ladder
  (the curvature defect, $(q-q^{-1})/2 = \sinh\lambda$), the bar-odd Habiro dual
  of $\alpha_{\mathrm{EM}}$.

So binding (mass-average) and $\beta$-decay ($Q_\beta$) are **not two problems
but one** — the even and odd parities of a single bar-graded element. Pinning
either parity (the keystone $\tau$, or the $c_k$ kernel) constrains the other
through the shared element. The Lean witnesses
[`QOU.Mass.evenPart_add_oddPart`](#prop:bar-parity-split), `evenPart_fixed`, and
`oddPart_anti` prove the decomposition and the parity of each part, sorry-free.

Although the even/odd involution split is implemented using standard linear algebraic techniques, attributing this mathematical decomposition to a concrete physical dichotomy—where the even component describes binding and the odd component captures decay processes—represents a mathematically novel interpretive framework developed for the Quantum Observable Universe.
