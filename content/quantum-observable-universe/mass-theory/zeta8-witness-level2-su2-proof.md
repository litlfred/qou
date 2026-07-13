**Proof.** **(1)** From the cyclotomic factorisation
$X^8 - 1 \;=\; \prod_{k=0}^{7}\,(X - \zeta_8^k)$,
dividing by $(X - 1)$ gives
$X^7 + X^6 + \cdots + 1 \;=\; \prod_{k=1}^{7}\,(X - \zeta_8^k).$
Evaluating at $X = 1$: LHS $= 8$ and RHS $= \prod_{k=1}^{7}\,(1 - \zeta_8^k)
= (\zeta_8;\zeta_8)_7$, so $(\zeta_8;\zeta_8)_7 = 8$. ∎

**(2)** Since $\zeta_8 = e^{2\pi i / 8}$ is a primitive 8th root of unity,
$\zeta_8^k = 1$ iff $8 \mid k$, so $\zeta_8^k \neq 1$ for $1 \leq k \leq 7$.
The Hecke quadratic relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ at
$q = \zeta_8$ gives eigenvalues $\sigma_i \in \{\zeta_8, -\zeta_8^{-1}\}$.
Both eigenvalues have order $8$: $\zeta_8$ directly, and
$-\zeta_8^{-1} = \zeta_8^4 \cdot \zeta_8^{-1} = \zeta_8^3$ which is also
a primitive 8th root of unity. The order of $\sigma_i$ is therefore
$\mathrm{lcm}(8, 8) = 8$. ∎

**(3)** At $q = \zeta_8$, $q^4 = (e^{i\pi/4})^4 = e^{i\pi} = -1$, so
$q^4 = -1 = q^{-4}$, giving $q^4 - q^{-4} = 0$. Since $q - q^{-1} \neq 0$
(as $\zeta_8 \neq ± 1$), $[4]_q = 0/(q - q^{-1}) = 0$. ∎
