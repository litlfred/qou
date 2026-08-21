*Proof.*
Let $s_0$ be a root of $s^2 + s - 1 = 0$. Multiplying by $-s_0^{-2}$ yields $-1 - s_0^{-1} + s_0^{-2} = 0$. Substituting $u = s_0^{-1}$ gives $u^2 - u - 1 = 0$. Thus, $s_0 = 1/\varphi \Leftrightarrow s_0^{-1} = \varphi$. Squaring gives $1/\varphi^2 \leftrightarrow \varphi^2$ on the $q$-line. $\square$

**Two-sided stability margin.**

The physical parameter $q_0 = 1.109978595554181\ldots$ (muon pin, 16 dps) lies in the open interval $(1, \varphi^2)$. The two golden nodes bracket this regime to define a two-sided stability margin:

See [Table: Golden-ratio dual nodes](#tbl:golden-skew-dual-node-table-data).

The asymmetry places $q_0$ closer to the sub-classical node. The ratio $(\varphi^2 - q_0)/(q_0 - 1/\varphi^2) \approx 2.07$ varies smoothly with $q_0$, achieving unity at the arithmetic midpoint $q = (1/\varphi^2 + \varphi^2)/2 = 3/2$. It has no closed form in $\varphi$ alone.

**Appearance of $\varphi^2$ on the physical side.**

The Descartes elliptic curve $\mathcal{E}_q$ does not acquire a node at $q = \varphi^2$, as its Weierstrass factor $s^2 + s - 1$ remains non-zero. Instead, the bar-dual node signifies the degeneration of the dual curve $\mathcal{E}^{*}_q := \mathcal{E}_{q^{-1}}$. The $q \leftrightarrow q^{-1}$ symmetry of the Iwahori--Hecke algebra $H_n(q)$ identifies this dual curve with the original curve by exchanging the Hecke eigenvalues $\{q, -q^{-1}\}$.

The skew-dual node is the threshold where the inverse substrate $q^{-1}$ falls into the sub-golden regime. Equivalently, it is where the symmetric channel of the Hecke generator decouples from the antisymmetric channel.

**Connection to the Möbius fixed points.**

The fixed points $\{1/\varphi, -\varphi\}$ of the baryon integration-limit Möbius map $f(q) = (4 - q)/(4q + 3)$ extend under bar conjugation to the full quartet $\{1/\varphi, -\varphi, \varphi, -1/\varphi\}$. The positive roots $\{1/\varphi, \varphi\}$ are the bar-paired thresholds bracketing the physical band.

**Falsifiability.**

We predict that any observable monotone in $q - q_{\mathrm{gold}}$ on the sub-classical side has a bar-paired analogue monotone in $\varphi^2 - q$ on the super-classical side. The same Hecke skew-symmetry that exchanges $L_+$ and $L_-$ in the Skein relation relates their sensitivities. At $q = q_0$, the super-classical margin $\approx 1.508$ dominates. This aligns with the empirical observation that nuclear physics is more robust against substrate compression than rarefaction.
