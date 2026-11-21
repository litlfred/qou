The two quadratic orders of [The winding lattice of a braid-word geodesic](winding-lattice-norm-form.md) suggest a reading of the sign carried by the $S$-channel, which this remark states and then bounds.

The canonical braid words of the fundamental knots are powers of the half-figure-eight word $w = \sigma_1\sigma_2^{-1}$: the figure-eight is $4_1 = w^2$ and the Borromean rings are $L6a4 = w^3$ ([`fundamental-knots-operator-basis`](fundamental-knots-operator-basis.md)). Reading the exponent $n$ as the winding number of the associated geodesic, the golden order's alternating norm $N(\varphi^n) = (-1)^n$ assigns a sign to each knot by the *parity* of $n$ alone:
$$
  4_1 = w^2 \ (n \text{ even}) \ \longmapsto\ +, \qquad
  L6a4 = w^3 \ (n \text{ odd}) \ \longmapsto\ -.
$$
Both match the observed signs at the corresponding anchors, with no free parameter. The rule is parameter-free in a strong sense: nothing in it refers to $q_0$, so it is insensitive to the $\sim 10^{-8}$ separation between the two anchor moduli. This is the structural interest of the reading — a sign difference between two knots need not be produced by a hypersensitive function of $q_0$ at all, if it is produced by their winding parity instead.

The bar-parity split displays the same parity as a channel exchange. For $x = \varphi^n$ the split of [Cusp-shape bar-parity: the figure-eight modulus splits as $\mathfrak{V} = \mathrm{Vol} + i\,\mathrm{CS}$](cusp-shape-bar-parity.md) gives $\mathrm{barEven}(x) = x + x^{-1}$ and $\mathrm{barOdd}(x) = x - x^{-1}$, and *which* of the two integer sequences $L_n$ and $F_n\sqrt5$ realizes the $\cosh$ and which the $\sinh$ exchanges with the parity of $n$:
$$
  n \text{ even}: (\mathrm{barEven}, \mathrm{barOdd}) = (L_n,\, F_n\sqrt5),
  \qquad
  n \text{ odd}: (\mathrm{barEven}, \mathrm{barOdd}) = (F_n\sqrt5,\, L_n),
$$
both satisfying $\mathrm{barEven}^2 - \mathrm{barOdd}^2 = 4$. The even and odd channels are exchanged by the parity of the winding, which is the same datum that flips the norm.

**Scope.** Two limitations are essential.

First, the identification of the $S$-channel sign with $\mathrm{Im}\,\mathfrak{V}$ is derived on the *cusp torus*, where the relevant order is the silver one, of discriminant $12$. There the norm of every unit power is $+1$, so no parity flip exists; the sign there is carried by the winding *slope*, not the winding parity. Transporting the mechanism to the golden order requires the corresponding complex-volume computation on Bring's surface, which is not carried out. The parity reading is therefore an analogy supported by two sign agreements — a conjectural mechanism, not a derivation.

Second, the magnitudes are not accounted for. Since $\lvert N(\varphi^n)\rvert = 1$ for every $n$, the parity rule alone predicts equal magnitudes at the two anchors, whereas the observed ratio is about $4.08$; the closest natural golden candidate, $\varphi^3 \approx 4.236$, misses by roughly $4\%$. No winding pair is selected to close that gap. The reason for the restraint is structural rather than tactical: Dang and Purcell show that cusp shapes of tunnel-number-one manifolds are dense in the Teichmüller space of the torus, so for a general cusp shape $\tau$ the form becomes $(m + \ell\tau_1)^2 - \ell^2\tau_2^2$ and a knot may be chosen to realize essentially any desired value. Selecting a knot or a winding pair to reproduce a magnitude would therefore be unconstrained curve-fitting, and the agreement it produced would carry no evidential weight.

What survives is narrow: the sign is available from arithmetic rather than from sensitivity to $q_0$, and of the two orders in play only the golden one can supply it.
