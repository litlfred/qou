**Conditional on [proton's Borromean mass assembly](proton-borromean-assembly.md).**

*Let $q_0 \approx 1.10978$ be the substrate parameter, $m_e$ the
electron mass (CAL-1), $m_\mu$ the muon mass (derived from CAL-2
$P_{\mathrm{skew}}^{\beta}$), and let $F_{\mathrm{Bor}}$ denote the
Borromean categorical observable
([Borromean categorical observable](../braids-and-knots/f-bor-borromean-observable.md)).
Then the proton mass satisfies the approximate substrate identity*

$$
  \boxed{\;m_p \;=\; 2 \cdot m_\mu \cdot F_{\mathrm{Bor}}(q_0) \;-\; 12 \cdot m_e\;}
$$

*to a residual of $0.24\,\mathrm{ppm}$ at $q = q_0$ (50-dps MPFR
verified).*

*Equivalently, factoring $12 = \dim V_{(2,1)} \cdot |S_3| = 2 \cdot 6$:*

$$
  \boxed{\;m_p \;=\; \dim V_{(2,1)} \cdot \bigl(m_\mu \cdot F_{\mathrm{Bor}}(q_0) \;-\; |S_3| \cdot m_e\bigr)\;}
$$

*where the structural integers $\dim V_{(2,1)} = 2$ and $|S_3| = 6$
are the categorical invariants of $H_3(q)$ recorded in
[Borromean categorical observable](../braids-and-knots/f-bor-borromean-observable.md).*

The comparison has two qualifications. First, the normaliser $[3]_q!/q^3$ in $F_{\mathrm{Bor}}$ is asserted, not derived ([normaliser conjecture](../braids-and-knots/proton-normaliser-kl-coordinate.md)). Replacing it by the bar-symmetric $[3]_q!$ moves $m_p$ by $+37\,\%$, and none of the normalisers supplied by a convention-D closure reproduces $m_p$. The identity is therefore fitted in that factor. Second, the $0.24\,\mathrm{ppm}$ residual is evaluated at the muon-pinned $q_0$. At the proton-pinned $q_0$ the identity holds exactly, because that $q_0$ is solved from it.

The numerical verification, the per-order $h$-expansion, the combined nucleon-mass derivation, and the sub-ppm precision frontier are recorded in the [derivation note](#rem:proton-mass-substrate-identity-derivation).
