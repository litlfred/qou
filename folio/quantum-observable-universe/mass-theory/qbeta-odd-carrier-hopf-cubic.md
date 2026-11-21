**Remark (why the $\mathfrak{Q}_\beta$ odd channel resists a real-$q$ closure).**
The precision-ladder coefficient $c_3$ splits under the bar involution
$q \mapsto q^{-1}$ into a bar-even part (exactly measured) and a bar-odd part,
the latter being the open channel. Its carrier is the bar-odd part of the net
decay-width Laurent polynomial $\Delta_{\mathrm{net}} = \Delta(\mathfrak{n}) - \Delta(\mathfrak{p})$
on the $\mathbf{H}_3$ normal-form basis, whose numerator over $4q^7$ is

$$
\mathrm{num}(q) = q^{14} - 5q^{12} + 10q^{10} - 16q^{8} + 16q^{6} - 10q^{4} + 5q^{2} - 1.
$$

**The cyclotomic content factors cleanly into a quantum differential.** Exactly,
$\mathrm{num}(q) = (q^2 - 1)\,R_{12}(q)$, which means the bar-odd part of the categorical net evaluates *exactly* to:

$$
\Delta_{\mathrm{net}}^{\mathrm{odd}} = \frac{q - q^{-1}}{4} \cdot C(y) = \frac{h}{4} \cdot C(y)
$$

where $h = q - q^{-1}$ is the quantum differential and $C(y)$ is a cubic in the bar-even loop-trace variable $y = q^2 + q^{-2} = 2\cosh 2\lambda$ given by:

$$
C(y) = y^3 - 4y^2 + 3y - 2.
$$

$C$ is irreducible over $\mathbb{Q}$ (its only possible rational roots $\pm 1, \pm 2$
are all nonzero), so its root generates a genuine **degree-3 field**
(discriminant $-152 = -2^3 \cdot 19$, Galois group $S_3$). Every substrate
*quadratic* anchor sits at a rational trace value — golden $\varphi \mapsto y = 3$,
silver $1 + \sqrt{2} \mapsto y = 6$, classical $q = 1 \mapsto y = 2$ — and $C$ is
nonzero at each. A degree-$\le 2$ number can never be a root of an irreducible
cubic, so **no quadratic-anchor or real-$q$ construction can reproduce the odd
carrier**: this is the structural reason the real-$q$ $c_3$ closures fail.

**The degree-3 comes from the Hopf (double-crossing) sector.** Decomposing the
bar-odd carrier over the knot sectors of the $\mathbf{H}_3$ normal form isolates
the origin of the cubic:

| knot sector | crossings | $\Delta^{\mathrm{odd}}_{\mathrm{sector}}$ |
|---|---|---|
| virtual ($\sigma_0, \sigma_1$) | 1 | $0$ |
| electron ($\sigma_0\sigma_1\sigma_0$) | 3 | $0$ |
| unknot ($\mathbf{1}$) | 0 | $\frac{h}{4} \cdot (2y^2 - 7y + 4) = \frac{h}{4} \cdot C_{\mathrm{unknot}}(y)$ |
| Hopf ($\sigma_0\sigma_1 + \sigma_1\sigma_0$) | 2 | $\frac{h}{4} \cdot (y^3 - 6y^2 + 10y - 6) = \frac{h}{4} \cdot C_{\mathrm{Hopf}}(y)$ |

with $C = C_{\mathrm{Hopf}} + C_{\mathrm{unknot}}$. The odd-crossing sectors
(virtual, electron) are bar-even and vanish; the identity contributes only a
quadratic; the **cubic — hence the degree-3 field — is sourced entirely by the
Hopf-link (double-crossing) sector**. $C_{\mathrm{Hopf}}$ is itself irreducible
(discriminant $-76 = -2^2 \cdot 19$), and the prime $19$ is the arithmetic
fingerprint shared with the total $C$. So the obstruction is not a
$3$-dimensional representation ($\mathbf{H}_3$ has none — its Wedderburn blocks
are $1, 2, 1$) nor a single knot invariant, but the two-crossing isospin
amplitude difference. Any genuine odd-channel closure must supply the cubic
field of $C_{\mathrm{Hopf}}$, routed through the archimedean evaluation of the
Markov crossing term, rather than a fibre-level real-$q$ formula.
