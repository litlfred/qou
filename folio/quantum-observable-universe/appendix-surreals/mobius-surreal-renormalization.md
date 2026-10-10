The [Möbius energy](#prop:mobius-energy) is a renormalized quadratic interaction: $\iint |\varrho(s)-\varrho(t)|^{-2}$ and $\iint D(s,t)^{-2}$ each diverge on the diagonal, and the divergences cancel. Under the surreal lift, this renormalization becomes a difference of two infinite surreals.

Excise a diagonal band of width $\varepsilon = 1/\omega$ and set
$$
  I_1 = \iint_{|s-t|>1/\omega}\!\frac{|\varrho'(s)|\,|\varrho'(t)|}{|\varrho(s)-\varrho(t)|^2}, \qquad I_2 = \iint_{|s-t|>1/\omega}\!\frac{|\varrho'(s)|\,|\varrho'(t)|}{D(s,t)^2}.
$$
Both are infinite surreals of $\mathrm{ord}_\omega = +1$; each diverges like $c\,\omega$. Because $|\varrho(s)-\varrho(t)| = D(s,t) + O(|s-t|^3)$ near the diagonal, $I_1$ and $I_2$ share the same leading coefficient $c$. The $\omega^{+1}$ parts cancel, $I_1 - I_2$ is finite, and
$$
  E(\varrho) = \mathrm{std}\!\bigl(I_1 - I_2\bigr).
$$
The analytic Hadamard finite part becomes the standard part of a difference of two infinite surreals of equal leading $\omega$-order. The finiteness bound reduces to an algebraic leading-coefficient match $[\omega^{+1}]I_1 = [\omega^{+1}]I_2$.

This applies generally. For the Frostman/Riesz $s$-energy $I_s = \iint |x-y|^{-s}$, the Hausdorff dimension is the $\mathrm{ord}_\omega$ boundary at which $I_s$ flips from infinite to finite.

This provides surreal language for a classical renormalization. It adds no archimedean obligation: $E(\varrho)$ is the same real number. However, while $\mathbf{No}$ carries no Lebesgue measure, Hausdorff dimension (an exponent) and renormalized energies (a difference of infinite surreals) are surreal-native.
