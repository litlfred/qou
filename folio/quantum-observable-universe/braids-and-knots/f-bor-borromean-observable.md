The **Borromean categorical observable** is
$$
  F_{\mathrm{Bor}}(q) \;:=\;
    \frac{\bigl|\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)\bigr| \cdot [3]_q!}{q^3}.
$$
The normaliser $[3]_q!/q^3 = 1 + 2q^{-2} + 2q^{-4} + q^{-6}$ is the Schur element $c_{\mathrm{sign}}$ of the sign character of $H_3(q)$, with $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$. The Schur elements $c_\chi$ are the constants in the decomposition $\tau = \sum_\chi \chi / c_\chi$ of the symmetrising trace $\tau(T_w) = \delta_{w,1}$. They are
$$
  c_{\mathrm{triv}} = q^3\,[3]_q!, \qquad c_{\mathrm{sign}} = [3]_q!/q^3, \qquad c_{\mathrm{refl}} = [3]_q .
$$
So $F_{\mathrm{Bor}}(q) = |\mathrm{tr}_M(\beta_{\mathrm{Bor}}, q)| \cdot c_{\mathrm{sign}}(q)$. The same constant appears in $x_-^2 = c_{\mathrm{sign}}\,x_-$ for the unnormalised $q$-antisymmetriser $x_- = \sum_{w \in S_3} (-q)^{-\ell(w)}\,T_w$.

**Status of the normaliser: asserted, not derived.** Every normaliser $q^k [3]_q!$ equals $|S_3| = 6$ at $q = 1$, so the classical limit does not fix $k$. For $q > 1$, $q^k [3]_q!$ is the Schur element of a linear character only for $k = 3$ (trivial) or $k = -3$ (sign), and it is invariant under $q \mapsto q^{-1}$ only for $k = 0$. The observable uses $k = -3$. Nothing in the Markov axioms selects it:

- The convention-D normalisation of a writhe-zero three-strand closure is $[2]_q^2$, since $z_D \cdot \mathrm{tr}_M(\sigma^{-1}) = [2]_q^{-2}$.
- The word $V^3 = (\sigma_0 \sigma_1^{-1})^3$ has writhe zero and is a pure braid, so every framing correction is $1$.

Convention D also gives the sign block weight $y_{(1^3)} = 0$, while this normaliser is that block's Schur element. That tension is open. The earlier reading of $q^3/[3]_q!$ as the Markov weight $y_{(3)}$ of the trivial partition does not hold under convention D, where $y_{(3)} = (q^4+1)/(q^2+1)^2$. In the variable $q^{-1}$ the trivial and sign characters swap, which is the only sense in which that reading survives.

Every coefficient of $F_{\mathrm{Bor}}$ in the variable $h = q - q^{-1}$ is an exact rational number:
$$
  F_{\mathrm{Bor}}(h)
  \;=\; 6 \;-\; 9h \;+\; \tfrac{19}{2}h^2 \;-\; \tfrac{57}{8}h^3
        \;-\; \tfrac{1}{2}h^4 \;+\; \tfrac{649}{128}h^5 \;-\; 7h^6 \;+\; \cdots
$$
The observable attaches two structural integers: $2$ (the classical dimension of the standard irrep of $S_3$) and $12$ (the order of $S_3$ scaled by this dimension). These integers carry no archimedean information and are available over any base ring.
