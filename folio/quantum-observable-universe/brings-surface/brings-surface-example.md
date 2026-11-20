Bring's surface $\Sigma_4$ is the projective curve in $\mathbb{CP}^4$ defined by three equations:

$$
  x_1 + x_2 + x_3 + x_4 + x_5 = 0
$$

$$
  x_1^2 + x_2^2 + x_3^2 + x_4^2 + x_5^2 = 0
$$

$$
  x_1^3 + x_2^3 + x_3^3 + x_4^3 + x_5^3 = 0
$$

This is a smooth curve of genus 4, yielding $\chi = 2 - 2g = 2 - 8 = -6$. Its automorphism group is $S_5$, acting by permutations of the five coordinates.

**Genus 4.** The lifting obstructions require only $g \geq 1$; the value $\chi_{\mathrm{eu}}(M_0) = -6$ comes from the six-branch-point count of the geometric descent ([the $\chi_{\mathrm{eu}}(M_0) = -6$ chain](#ex:chi-minus-six-derivation)). Riemann–Roch for the rank-2 bundle $V$ over the base curve converts it: $\chi(V) = \deg(V) + \mathrm{rank}(V)(1-g) = 0 + 2(1-g)$, so $\chi(V) = -6$ yields $g = 4$.

**Minimality of Bring's surface.** Among all genus-4 curves, Bring's surface is the **terminal object**. It has the largest automorphism group ($S_5$ has order 120), and any other genus-4 QOU maps to it. This establishes the Descartes theorem.

**Concrete coordinates.** Pick the affine patch $x_5 = 1$. Then $x_4 = -(x_1+x_2+x_3+1)$ and the remaining two equations define a curve in $\mathbb{C}^3$. At $(x_1,x_2,x_3,x_4,x_5) = (1, \zeta, \zeta^2, \zeta^3, \zeta^4)$ where $\zeta = e^{2\pi i/5}$, all three power sums vanish.
