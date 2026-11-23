The **Borromean categorical observable** is
$$
  F_{\mathrm{Bor}}(q) \;:=\;
    \frac{\bigl|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)\bigr| \cdot [3]_q!}{q^3}.
$$
The normaliser $[3]_q!/q^3 = 1 + 2q^{-2} + 2q^{-4} + q^{-6}$ is the Schur element $c_{\mathrm{sign}}$ of the sign character of $H_3(q)$, with $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$. For $w \in S_3$ write $\sigma_w$ for its positive braid lift in $H_3(q)$. The Schur elements $c_\chi$ are the constants in the decomposition $\tau = \sum_\chi \chi / c_\chi$ of the symmetrising trace $\tau(\sigma_w) = \delta_{w,1}$. They are
$$
  c_{\mathrm{triv}} = q^3\,[3]_q!, \qquad c_{\mathrm{sign}} = [3]_q!/q^3, \qquad c_{\mathrm{refl}} = [3]_q .
$$
So $F_{\mathrm{Bor}}(q) = |\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)| \cdot c_{\mathrm{sign}}(q)$. The same constant appears in $x_-^2 = c_{\mathrm{sign}}\,x_-$ for the unnormalised $q$-antisymmetriser $x_- = \sum_{w \in S_3} (-q)^{-\ell(w)}\,\sigma_w$. The relation $x_-^2 = c_{\mathrm{sign}}\,x_-$ is the standard quasi-idempotent identity for the sign block.

The normaliser is asserted, not derived. Every normaliser $q^k [3]_q!$ equals $|S_3| = 6$ at $q = 1$, so the classical limit does not fix $k$. For $q > 1$, $q^k [3]_q!$ is the Schur element of a linear character only for $k = 3$ (trivial) or $k = -3$ (sign), and it is invariant under $q \mapsto q^{-1}$ only for $k = 0$. The observable uses $k = -3$. Two candidate algebraic routes do not produce it:

- Let $z_D = q^3/(q^2+1)$ be the convention-D Markov parameter, $\mathrm{tr}_M(\sigma_i) = z_D$. The convention-D normalisation of a writhe-zero three-strand closure is $[2]_q^2$, since $z_D \cdot \mathrm{tr}_M(\sigma_i^{-1}) = [2]_q^{-2}$.
- The braid word of the Borromean rings is $V^3 = (\sigma_0 \sigma_1^{-1})^3$. It has writhe zero and is a pure braid, so every framing correction is $1$.

Convention D also gives the sign block weight $y_{(1^3)} = 0$, while this normaliser is that block's Schur element. That tension is open. Under convention D the Markov weight of the trivial partition is $y_{(3)} = (q^4+1)/(q^2+1)^2$, so $q^3/[3]_q!$ is not $y_{(3)}$. Relabelling the root $q \mapsto -q^{-1}$ swaps the trivial and sign characters, and only in that relabelled frame is $q^3/[3]_q!$ attached to the trivial partition.

A modified-trace reading of the factor $q^{-3}$, as a derivative in an integral, bar-invariant coordinate, is recorded with its negative result in [the Kazhdan–Lusztig coordinate conjecture](proton-normaliser-kl-coordinate.md); it does not derive the normaliser.

Every coefficient of $F_{\mathrm{Bor}}$ in the variable $h = q - q^{-1}$ is an exact rational number:
$$
  F_{\mathrm{Bor}}(h)
  \;=\; 6 \;-\; 9h \;+\; \tfrac{19}{2}h^2 \;-\; \tfrac{57}{8}h^3
        \;-\; \tfrac{1}{2}h^4 \;+\; \tfrac{649}{128}h^5 \;-\; 7h^6 \;+\; \cdots
$$
The observable attaches two structural integers: $2$ (the classical dimension of the standard irrep of $S_3$) and $12$ (the order of $S_3$ scaled by this dimension). These integers carry no archimedean information and are available over any base ring.
