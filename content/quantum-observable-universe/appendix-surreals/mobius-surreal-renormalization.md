The [Möbius energy](#prop:mobius-energy) (O'Hara \cite{ohara1991}; Freedman–He–Wang \cite{freedman1994}) acts as a renormalized quadratic interaction. The integrals $\iint |\varrho(s)-\varrho(t)|^{-2}$ and $\iint D(s,t)^{-2}$ each diverge on the diagonal, but the divergences cancel. Under the surreal lift, this renormalization becomes surreal arithmetic: a difference of two infinite surreals.

**Remark.** Excise a diagonal band of width $\varepsilon = 1/\omega$ ([surreal blow-up calculus](#def:surreal-blowup-calculus)) and set:

$$
  I_1 = \iint_{|s-t|>1/\omega}\!\frac{|\varrho'(s)|\,|\varrho'(t)|}{|\varrho(s)-\varrho(t)|^2},
  \qquad
  I_2 = \iint_{|s-t|>1/\omega}\!\frac{|\varrho'(s)|\,|\varrho'(t)|}{D(s,t)^2}.
$$

Both are infinite surreals of $\operatorname{ord}_\omega = +1$ ([Conway normal form](#rem:conway-normal-form)). Each diverges like $c\,\omega$ as the cutoff shrinks. Because $|\varrho(s)-\varrho(t)| = D(s,t) + O(|s-t|^3)$ near the diagonal, $I_1$ and $I_2$ share the same leading coefficient $c$. Consequently, the $\omega^{+1}$ parts cancel. $I_1 - I_2$ becomes appreciable (finite), and:

$$
  E(\varrho) \;=\; \operatorname{std}\!\bigl(I_1 - I_2\bigr).
$$

The analytic Hadamard finite part becomes "subtract two infinite surreals of equal leading $\omega$-order, then take the standard part". The finiteness bound reduces to an algebraic leading-coefficient match $[\omega^{+1}]I_1 = [\omega^{+1}]I_2$.

**General principle — dimension as a surreal order.** The same mechanism governs the Frostman/Riesz $s$-energy $I_s = \iint |x-y|^{-s}$. This is infinite below the dimension and appreciable above. The Hausdorff dimension acts as the $\operatorname{ord}_\omega$ boundary at which $I_s$ flips from infinite to appreciable. This forms a single valuation statement rather than the analytic $\sup\{s : I_s < \infty\}$. In this repository, the Julia-set dimension provides an instance: $d_H(q) = (2q-1)^2/q^3$.

**Scope.** This provides a surreal language for a renormalization that is also expressible classically via the Hadamard finite part over $\mathbb{R}$. It transforms the divergent quadratic interaction's finiteness bound into an algebraic leading-coefficient check. It adds no archimedean obligation. $E(\varrho)$ produces the same real number either way. The contrast with the measure-value side is sharp. $\mathbf{No}$ carries no Lebesgue measure, but Hausdorff dimension (an exponent) and renormalized energies (a difference of infinite surreals) are surreal-native.
