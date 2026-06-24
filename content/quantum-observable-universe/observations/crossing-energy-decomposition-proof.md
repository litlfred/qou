Write $\lambda = \ln q$ for the crossing rapidity (positive when $q > 1$). The decomposition rests on one algebraic fact: the symmetric and antisymmetric halves of the crossing weight $q$ are $\cosh\lambda$ and $\sinh\lambda$.

**Symmetric/antisymmetric weights are $\cosh$/$\sinh$.** For $q > 0$, $q = e^{\lambda}$ and $q^{-1} = e^{-\lambda}$, so
$$
  \frac{q + q^{-1}}{2} = \cosh\lambda, \qquad \frac{q - q^{-1}}{2} = \sinh\lambda
$$
(`symmetricWeight_eq_cosh`, `antisymmetricWeight_eq_sinh`). Hence $q = \cosh\lambda + \sinh\lambda$ and $q^{-1} = \cosh\lambda - \sinh\lambda$ (`q_eq_cosh_add_sinh`, `q_inv_eq_cosh_sub_sinh`; the bare forms `q_decomposition`, `q_inv_decomposition` close by `ring`).

**Channels (1)–(2): mirror symmetry.** The mirror $\sigma$ reverses every crossing sign, fixing each $|\epsilon_i|$ while sending $\mathrm{sgn}(\epsilon_i) \mapsto -\mathrm{sgn}(\epsilon_i)$. The $\cosh$ (strong) channel weights each crossing by magnitude only and is mirror-even; the $\sinh$ (Coulomb) channel carries the full sign and is mirror-odd. Equivalently, $q = \cosh\lambda + \sinh\lambda$ and $q^{-1} = \cosh\lambda - \sinh\lambda$ show a positive crossing $(+q)$ and its mirror negative crossing $(-q^{-1})$ share the same $\cosh\lambda$ part and carry opposite $\sinh\lambda$ parts.

**Channel (3): pair cancellation.** For a particle–antiparticle pair the mirror-even $\cosh$ parts cancel across the pair and the mirror-odd $\sinh$ parts add, leaving the crossing energy of $(\mathfrak{H}, \mathfrak{H}^{\sigma})$ purely antisymmetric — the per-crossing identity $\tfrac12[(\cosh+\sinh) - (\cosh-\sinh)] = \sinh\lambda$ summed over crossings.

**Channel (4): ratio identity.** For $q > 1$ both weights are positive (`symmetric_pos`, `antisymmetric_pos`), and the common crossing factor cancels in the ratio:
$$
  \frac{E_{\mathrm{asym}}}{E_{\mathrm{sym}}} = \frac{\sinh\lambda}{\cosh\lambda} = \frac{q - q^{-1}}{q + q^{-1}} = \tanh(\ln q),
$$
independent of $\mathfrak{H}$ (`em_strong_ratio_tanh`).

**Algebraic–hyperbolic bridge.** The per-crossing identity is the $n=1$ case of $q^{n} = e^{n\lambda} = \cosh(n\lambda) + \sinh(n\lambda)$ (`q_pow_eq_cosh_add_sinh`). Subtracting the conjugate gives $q^{n} - q^{-n} = 2\sinh(n\lambda)$ (`two_sinh_nat_log`), and dividing by the $n=1$ case $q - q^{-1} = 2\sinh\lambda$ yields the quantum integer as a ratio of hyperbolic sines,
$$
  [n]_q = \frac{q^{n} - q^{-n}}{q - q^{-1}} = \frac{\sinh(n\lambda)}{\sinh\lambda}
$$
(`qbracket_eq_sinh_ratio`). Thus the discrete Hecke datum $[n]_q$ is a value of $\sinh$ at the rapidity $\lambda = \ln q$ — the archimedean seed of the Kashaev volume realisation. All supporting identities are discharged sorry-free over $\mathbb{R}$ in `QOU.Braiding`. $\qquad\blacksquare$
