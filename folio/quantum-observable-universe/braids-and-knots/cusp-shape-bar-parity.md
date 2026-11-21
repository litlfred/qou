The cusp shape of the figure-eight knot $4_1$ is $\omega = e^{i\pi/3}$, a primitive sixth root of unity — the root of the cyclotomic polynomial $\Phi_6(z) = z^2 - z + 1$ in the upper half-plane, with trace field $\mathbb{Q}(\sqrt{-3})$ \cite{neumann-reid}. Split $\omega$ along the bar-involution $\sigma\colon x \mapsto x^{-1}$ into its symmetric and antisymmetric shapes:
$$
  \mathrm{barEven}(x) = x + x^{-1}, \qquad \mathrm{barOdd}(x) = x - x^{-1}.
$$
Then the cusp shape realizes the two faces of the Neumann–Zagier complex volume $\mathfrak{V} = \mathrm{Vol} + i\,\mathrm{CS}$:
$$
  \mathrm{barEven}(\omega) = 1, \qquad \mathrm{barOdd}(\omega)^2 = -3.
$$
The bar-even part is the rational Volume normalization $2\cos(\pi/3) = 1$; the bar-odd part is the $\sqrt{-3}$ Chern–Simons modulus $(2i\sin(\pi/3))^2 = -3$.

The identity holds over any field carrying a root of $\Phi_6$. From $\omega^2 - \omega + 1 = 0$ one gets $\omega^{-1} = 1 - \omega$ (since $\omega(1-\omega) = 1$), whence
$$
  \mathrm{barEven}(\omega) = \omega + (1 - \omega) = 1,
  \qquad
  \mathrm{barOdd}(\omega) = 2\omega - 1,
$$
and $(2\omega - 1)^2 = 4\omega^2 - 4\omega + 1 = -3$ using $\omega^2 = \omega - 1$. The computation uses only field operations over a generic field (no archimedean structure).
